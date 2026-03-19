# scripts/run_accuracy_validation.py
# HumanTrace — Accuracy Validation Script
# Powered by Owlume
#
# Usage:
#   python scripts/run_accuracy_validation.py
#
# Output:
#   - Console report with accuracy metrics
#   - reports/humantrace_accuracy_report.json
#   - reports/humantrace_accuracy_report.md

from __future__ import annotations

import json
import os
import sys
import datetime
from typing import Dict, List, Any, Optional

# Add src/ to path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__)), "src"))

from humantrace_scanner import scan_message

# ── Paths ─────────────────────────────────────────────────────────────────────

ROOT = os.path.dirname(os.path.dirname(__file__))
DATASET_PATH = os.path.join(ROOT, "data", "validation", "humantrace_validation_dataset.json")
REPORTS_DIR = os.path.join(ROOT, "reports")


# ── Load dataset ──────────────────────────────────────────────────────────────

def load_dataset() -> Dict[str, Any]:
    with open(DATASET_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


# ── Run single message ────────────────────────────────────────────────────────

def run_single(message_record: Dict[str, Any]) -> Dict[str, Any]:
    """Run a single message through HumanTrace and return result with evaluation."""
    msg_id = message_record["id"]
    text = message_record["text"]
    context_hint = message_record.get("context_hint")
    ground_truth = message_record["ground_truth"]
    category = message_record["category"]
    mixed_expected = message_record.get("mixed_content_expected", False)

    try:
        result = scan_message(message=text, context_hint=context_hint)

        predicted = result.signal
        confidence = result.confidence
        mixed_detected = (result.meta or {}).get("mixed_content_warning", False)
        fraud_category = result.fraud_category

        # Evaluate correctness
        correct = _evaluate_correctness(
            ground_truth=ground_truth,
            predicted=predicted,
            category=category,
            mixed_expected=mixed_expected,
            mixed_detected=mixed_detected,
        )

        return {
            "id": msg_id,
            "category": category,
            "ground_truth": ground_truth,
            "predicted": predicted,
            "confidence": round(confidence, 3),
            "correct": correct,
            "mixed_expected": mixed_expected,
            "mixed_detected": mixed_detected,
            "fraud_category": fraud_category,
            "layer_signals": {
                l.layer: {"signal": l.signal, "confidence": round(l.confidence, 3)}
                for l in result.layers
            },
            "error": None,
        }

    except Exception as e:
        return {
            "id": msg_id,
            "category": category,
            "ground_truth": ground_truth,
            "predicted": "error",
            "confidence": 0.0,
            "correct": False,
            "mixed_expected": mixed_expected,
            "mixed_detected": False,
            "fraud_category": None,
            "layer_signals": {},
            "error": str(e),
        }


def _evaluate_correctness(
    ground_truth: str,
    predicted: str,
    category: str,
    mixed_expected: bool,
    mixed_detected: bool,
) -> bool:
    """
    Evaluate whether a prediction is correct.

    Rules:
    - synthetic_fraud: correct if predicted RED
    - genuine_human: correct if predicted YELLOW or GREEN (not RED)
    - mixed_content: correct if predicted YELLOW AND mixed_content_warning detected
    - edge_case: correct if predicted YELLOW (not RED — that would be a false positive)
    """
    if category == "synthetic_fraud":
        return predicted == "red"

    if category == "genuine_human":
        # RED on a genuine human message is a false positive — incorrect
        return predicted in ("yellow", "green")

    if category == "mixed_content":
        # Must be YELLOW and detect mixed content
        return predicted == "yellow" and mixed_detected

    if category == "edge_case":
        # Must NOT be RED — that is a false positive on a legitimate message
        return predicted in ("yellow", "green")

    return predicted == ground_truth


# ── Run full validation ───────────────────────────────────────────────────────

def run_validation() -> Dict[str, Any]:
    """Run full validation suite and return results."""
    print("\n" + "="*60)
    print("HumanTrace Accuracy Validation")
    print("Powered by Owlume")
    print("="*60)

    dataset = load_dataset()
    messages = dataset["messages"]
    spec = dataset["spec"]

    print(f"\nDataset: {len(messages)} messages across 4 categories")
    print(f"Running scans...\n")

    results = []
    for i, msg in enumerate(messages):
        result = run_single(msg)
        results.append(result)

        status = "✅" if result["correct"] else "❌"
        print(f"{status} {result['id']:8s} | {result['category']:20s} | "
              f"GT: {result['ground_truth']:6s} | "
              f"Pred: {result['predicted']:6s} | "
              f"Conf: {result['confidence']:.2f}"
              + (f" | MIXED ✓" if result["mixed_detected"] else ""))

    # ── Calculate metrics ──────────────────────────────────────────────────────

    categories = ["synthetic_fraud", "genuine_human", "mixed_content", "edge_case"]
    metrics = {}

    for cat in categories:
        cat_results = [r for r in results if r["category"] == cat]
        if not cat_results:
            continue
        correct = sum(1 for r in cat_results if r["correct"])
        total = len(cat_results)
        accuracy = correct / total if total > 0 else 0.0
        metrics[cat] = {
            "total": total,
            "correct": correct,
            "accuracy": round(accuracy, 3),
            "accuracy_pct": f"{accuracy*100:.1f}%",
        }

    # Overall
    total_correct = sum(1 for r in results if r["correct"])
    total = len(results)
    overall_accuracy = total_correct / total if total > 0 else 0.0

    # False positive rate (RED on non-fraud messages)
    non_fraud = [r for r in results if r["category"] in ("genuine_human", "edge_case")]
    false_positives = [r for r in non_fraud if r["predicted"] == "red"]
    fp_rate = len(false_positives) / len(non_fraud) if non_fraud else 0.0

    # Mixed content detection rate
    mixed = [r for r in results if r["category"] == "mixed_content"]
    mixed_detected_count = sum(1 for r in mixed if r["mixed_detected"])
    mixed_detection_rate = mixed_detected_count / len(mixed) if mixed else 0.0

    # Synthetic fraud detection rate
    sf = [r for r in results if r["category"] == "synthetic_fraud"]
    sf_detected = sum(1 for r in sf if r["predicted"] == "red")
    sf_detection_rate = sf_detected / len(sf) if sf else 0.0

    # Target comparison
    targets = spec.get("target_accuracy", {})
    target_sf = targets.get("synthetic_fraud_detection_rate", 0.80)
    target_fp = targets.get("false_positive_rate_max", 0.15)
    target_mixed = targets.get("mixed_content_detection_rate", 0.70)

    # ── Print report ──────────────────────────────────────────────────────────

    print("\n" + "="*60)
    print("ACCURACY REPORT")
    print("="*60)

    print(f"\n{'Category':<25} {'Total':>6} {'Correct':>8} {'Accuracy':>10}")
    print("-"*55)
    for cat, m in metrics.items():
        print(f"{cat:<25} {m['total']:>6} {m['correct']:>8} {m['accuracy_pct']:>10}")
    print("-"*55)
    print(f"{'OVERALL':<25} {total:>6} {total_correct:>8} {overall_accuracy*100:.1f}%")

    print(f"\n{'KEY METRICS':}")
    print(f"  Synthetic fraud detection rate:  {sf_detection_rate*100:.1f}%  "
          f"(target: {target_sf*100:.0f}%)  "
          f"{'✅' if sf_detection_rate >= target_sf else '❌'}")
    print(f"  False positive rate:             {fp_rate*100:.1f}%  "
          f"(target: <{target_fp*100:.0f}%)  "
          f"{'✅' if fp_rate <= target_fp else '❌'}")
    print(f"  Mixed content detection rate:    {mixed_detection_rate*100:.1f}%  "
          f"(target: {target_mixed*100:.0f}%)  "
          f"{'✅' if mixed_detection_rate >= target_mixed else '❌'}")

    # False positives detail
    if false_positives:
        print(f"\n  FALSE POSITIVES ({len(false_positives)}):")
        for fp in false_positives:
            print(f"    {fp['id']} — {fp['category']} — conf: {fp['confidence']:.2f}")

    # Missed fraud detail
    missed = [r for r in sf if r["predicted"] != "red"]
    if missed:
        print(f"\n  MISSED FRAUD ({len(missed)}):")
        for m in missed:
            print(f"    {m['id']} — predicted: {m['predicted']} — conf: {m['confidence']:.2f}")

    print("\n" + "="*60)

    # ── Build full report ─────────────────────────────────────────────────────

    report = {
        "spec": {
            "product": "HumanTrace",
            "powered_by": "Owlume",
            "validation_date": datetime.datetime.utcnow().isoformat() + "Z",
            "dataset_size": total,
            "dataset_version": "1.0.0",
        },
        "summary": {
            "overall_accuracy": round(overall_accuracy, 3),
            "overall_accuracy_pct": f"{overall_accuracy*100:.1f}%",
            "synthetic_fraud_detection_rate": round(sf_detection_rate, 3),
            "false_positive_rate": round(fp_rate, 3),
            "mixed_content_detection_rate": round(mixed_detection_rate, 3),
            "targets_met": {
                "synthetic_fraud": sf_detection_rate >= target_sf,
                "false_positive": fp_rate <= target_fp,
                "mixed_content": mixed_detection_rate >= target_mixed,
            }
        },
        "by_category": metrics,
        "false_positives": [
            {"id": r["id"], "confidence": r["confidence"]}
            for r in false_positives
        ],
        "missed_fraud": [
            {"id": r["id"], "predicted": r["predicted"], "confidence": r["confidence"]}
            for r in missed
        ],
        "detailed_results": results,
    }

    return report


# ── Save report ───────────────────────────────────────────────────────────────

def save_report(report: Dict[str, Any]) -> None:
    os.makedirs(REPORTS_DIR, exist_ok=True)

    # JSON report
    json_path = os.path.join(REPORTS_DIR, "humantrace_accuracy_report.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"\nJSON report saved: {json_path}")

    # Markdown report
    md_path = os.path.join(REPORTS_DIR, "humantrace_accuracy_report.md")
    s = report["summary"]
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("# HumanTrace Accuracy Validation Report\n")
        f.write(f"*Generated: {report['spec']['validation_date']}*\n\n")
        f.write("## Summary\n\n")
        f.write(f"| Metric | Result | Target | Status |\n")
        f.write(f"|--------|--------|--------|--------|\n")
        f.write(f"| Overall accuracy | {s['overall_accuracy_pct']} | — | — |\n")
        f.write(f"| Synthetic fraud detection | {s['synthetic_fraud_detection_rate']*100:.1f}% | ≥80% | {'✅' if s['targets_met']['synthetic_fraud'] else '❌'} |\n")
        f.write(f"| False positive rate | {s['false_positive_rate']*100:.1f}% | <15% | {'✅' if s['targets_met']['false_positive'] else '❌'} |\n")
        f.write(f"| Mixed content detection | {s['mixed_content_detection_rate']*100:.1f}% | ≥70% | {'✅' if s['targets_met']['mixed_content'] else '❌'} |\n")
        f.write(f"\n## By Category\n\n")
        f.write(f"| Category | Total | Correct | Accuracy |\n")
        f.write(f"|----------|-------|---------|----------|\n")
        for cat, m in report["by_category"].items():
            f.write(f"| {cat} | {m['total']} | {m['correct']} | {m['accuracy_pct']} |\n")
        if report["false_positives"]:
            f.write(f"\n## False Positives\n\n")
            for fp in report["false_positives"]:
                f.write(f"- {fp['id']} (confidence: {fp['confidence']:.2f})\n")
        if report["missed_fraud"]:
            f.write(f"\n## Missed Fraud\n\n")
            for m in report["missed_fraud"]:
                f.write(f"- {m['id']} predicted {m['predicted']} (confidence: {m['confidence']:.2f})\n")
        f.write(f"\n---\n*HumanTrace — Powered by Owlume*\n")
    print(f"Markdown report saved: {md_path}")


# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    report = run_validation()
    save_report(report)