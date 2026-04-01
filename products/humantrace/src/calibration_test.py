"""
calibration_test.py
-------------------
Runs all 170 calibration corpus examples through the HumanTrace v0 engine
and reports the false positive rate by batch and by enterprise context.

Ground truth for all examples: LOW (GENUINE human-authored communications)
A MEDIUM or HIGH result is a false positive.

Targets (from corpus_construction_protocol_v1.1):
  - Overall false positive rate: < 10%
  - Anti-pattern batches (10, 11, 12): < 5%
  - Each context must pass independently

Usage:
  cd C:\\dev\\owlume-engine\\products\\humantrace\\src
  python calibration_test.py

Output:
  - Console: per-example results + summary tables
  - File:    calibration_results_YYYYMMDD_HHMMSS.json  (same directory)
"""

from __future__ import annotations

import sys
import os
import re
import json
import time
from pathlib import Path
from datetime import datetime

# ── Path setup ────────────────────────────────────────────────────────────────
# Script lives at:
#   C:\dev\owlume-engine\products\humantrace\src\calibration_test.py
# parents[0] = src\
# parents[1] = humantrace\
# parents[2] = products\
# parents[3] = owlume-engine\   ← ROOT_DIR
SRC_DIR    = Path(__file__).resolve().parent
HT_DIR     = SRC_DIR.parent                        # products\humantrace\
PRODUCTS_DIR = HT_DIR.parent                       # products\
ROOT_DIR   = PRODUCTS_DIR.parent                   # owlume-engine\
CORE_DIR   = ROOT_DIR / "owlume_core"
CORPUS_DIR = ROOT_DIR / "docs" / "corpus" / "batch1"

# Diagnostic — confirm paths before any file ops
print(f"[PATHS] SRC_DIR    = {SRC_DIR}")
print(f"[PATHS] ROOT_DIR   = {ROOT_DIR}")
print(f"[PATHS] CORPUS_DIR = {CORPUS_DIR}")
print(f"[PATHS] Corpus exists: {CORPUS_DIR.exists()}")

for p in [str(SRC_DIR), str(CORE_DIR)]:
    if p not in sys.path:
        sys.path.insert(0, p)

# ── Import engine ─────────────────────────────────────────────────────────────
try:
    from main import analyse_message
    print("[INIT] analyse_message imported from main.py")
except ImportError as e:
    print(f"[ERROR] Could not import analyse_message: {e}")
    print("        Run from: C:\\dev\\owlume-engine\\products\\humantrace\\src")
    sys.exit(1)

# ── Corpus file manifest ──────────────────────────────────────────────────────
# Maps filename → (batch_number, context_label, example_count)
CORPUS_FILES = [
    ("corpus_batch1_fin_001_005_v1.md",   1,  "FIN — Collections letters",          5),
    ("corpus_batch1_fin_006_010_v1.md",   1,  "FIN — Collections letters",          5),
    ("corpus_batch2_fin_011_020_v1.md",   2,  "FIN — Lending decisions",           10),
    ("corpus_batch3_fin_021_040_v1.md",   3,  "FIN — Fraud operations",            20),
    ("corpus_batch4_legal_001_015_v1.md", 4,  "LEGAL — Demand letters",            15),
    ("corpus_batch5_legal_016_030_v1.md", 5,  "LEGAL — Settlement & regulatory",   15),
    ("corpus_batch6_int_001_020_v1.md",   6,  "INT — Manager & executive",         20),
    ("corpus_batch7_int_021_040_v1.md",   7,  "INT — IT, HR & policy",             20),
    ("corpus_batch8_adv_001_015_v1.md",   8,  "ADV — Financial & accounting",      15),
    ("corpus_batch9_adv_016_030_v1.md",   9,  "ADV — Specialist & consultant",     15),
    ("corpus_batch10_anti_001_010_v1.md", 10, "ANTI — Template institutional",     10),
    ("corpus_batch11_anti_011_020_v1.md", 11, "ANTI — Regulatory urgency",         10),
    ("corpus_batch12_anti_021_030_v1.md", 12, "ANTI — Expert confidence",          10),
]

ANTI_BATCHES = {10, 11, 12}

# ── Parser ────────────────────────────────────────────────────────────────────

def extract_examples(md_path: Path) -> list[dict]:
    """
    Parse a corpus .md file and extract all examples.

    Each example is a dict:
      {
        'corpus_id': str,       e.g. 'CB-FIN-001'
        'subtype':   str,       e.g. 'FIN — collections letter...'
        'text':      str,       the example text block
      }

    Example block structure in the .md files:
      ## CB-XXX-NNN
      ...
      ### Example text
      ---
      <text content>
      ---
      ### Property annotation
    """
    content = md_path.read_text(encoding="utf-8")
    examples = []

    # Split on level-2 headings that start with CB-
    # Pattern: ## CB-FIN-001, ## CB-LEGAL-001, ## CB-INT-001, ## CB-ADV-001, ## CB-ANTI-001
    blocks = re.split(r'\n(?=## CB-)', content)

    for block in blocks:
        # Extract corpus ID from heading line
        id_match = re.match(r'^## (CB-[A-Z]+-\d+)\b', block)
        if not id_match:
            continue
        corpus_id = id_match.group(1)

        # Extract subtype from the line after the heading
        subtype_match = re.search(r'\*\*Context / subtype:\*\*\s*(.+)', block)
        subtype = subtype_match.group(1).strip() if subtype_match else ""

        # Extract example text — between the first pair of --- after "### Example text"
        # The pattern: ### Example text\n\n---\n<text>\n---\n
        text_section = re.search(
            r'### Example text\s*\n+---+\s*\n(.*?)\n---+',
            block,
            re.DOTALL
        )
        if not text_section:
            # Fallback: try without the leading ---
            text_section = re.search(
                r'### Example text\s*\n+(.*?)\n### Property annotation',
                block,
                re.DOTALL
            )

        if not text_section:
            print(f"  [WARN] Could not extract text for {corpus_id} in {md_path.name}")
            continue

        raw_text = text_section.group(1).strip()

        # Clean up: remove markdown formatting artefacts
        # Remove bold markers **text**
        raw_text = re.sub(r'\*\*(.*?)\*\*', r'\1', raw_text)
        # Remove leading/trailing --- lines within the text
        raw_text = re.sub(r'^---+\s*$', '', raw_text, flags=re.MULTILINE)
        raw_text = raw_text.strip()

        if len(raw_text) < 20:
            print(f"  [WARN] Text too short for {corpus_id} ({len(raw_text)} chars) — skipping")
            continue

        examples.append({
            'corpus_id': corpus_id,
            'subtype':   subtype,
            'text':      raw_text,
        })

    return examples


# ── Engine runner ─────────────────────────────────────────────────────────────

def run_example(corpus_id: str, text: str) -> dict:
    """
    Run a single corpus example through the engine.
    Returns the full result dict plus a 'false_positive' flag.
    """
    payload = {
        'input_id': corpus_id,
        'text':     text,
    }
    try:
        result = analyse_message(payload)
    except Exception as e:
        return {
            'corpus_id':     corpus_id,
            'overall_risk':  'ERROR',
            'score':         None,
            'false_positive': True,
            'error':         str(e),
        }

    # overall_risk is a dict: {'label': 'low'/'medium'/'high', 'score': float, 'confidence': float}
    risk_obj     = result.get('overall_risk', {})
    overall_risk = risk_obj.get('label', 'UNKNOWN').upper()
    score        = risk_obj.get('score', None)

    return {
        'corpus_id':      corpus_id,
        'overall_risk':   overall_risk,
        'score':          score,
        'false_positive': overall_risk != 'LOW',
        'summary':        result.get('summary', ''),
        'signals_fired':  [f.get('signal_id') for f in result.get('detected_features', [])],
    }


# ── Reporting ─────────────────────────────────────────────────────────────────

def print_header(text: str, width: int = 72) -> None:
    print()
    print("=" * width)
    print(f"  {text}")
    print("=" * width)

def print_section(text: str, width: int = 72) -> None:
    print()
    print("-" * width)
    print(f"  {text}")
    print("-" * width)

def fp_rate(fp_count: int, total: int) -> str:
    if total == 0:
        return "N/A"
    rate = fp_count / total * 100
    status = "✅" if rate < 10 else "❌"
    return f"{rate:.1f}% ({fp_count}/{total}) {status}"

def anti_fp_rate(fp_count: int, total: int) -> str:
    if total == 0:
        return "N/A"
    rate = fp_count / total * 100
    status = "✅" if rate < 5 else "❌"
    return f"{rate:.1f}% ({fp_count}/{total}) {status}"


# ── Main ──────────────────────────────────────────────────────────────────────

def main() -> int:
    print_header("HumanTrace v0 — Calibration Validation")
    print(f"  Corpus directory : {CORPUS_DIR}")
    print(f"  Timestamp        : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"  Target (overall) : false positive rate < 10%")
    print(f"  Target (anti)    : false positive rate < 5% (Batches 10–12)")

    all_results: list[dict] = []
    batch_results: dict[int, list[dict]] = {}
    context_results: dict[str, list[dict]] = {}
    false_positives: list[dict] = []

    total_examples_expected = sum(c[3] for c in CORPUS_FILES)
    total_extracted = 0
    total_run = 0

    # ── Process each corpus file ──────────────────────────────────────────────
    for filename, batch_num, context_label, expected_count in CORPUS_FILES:
        md_path = CORPUS_DIR / filename

        if not md_path.exists():
            print(f"\n[MISSING] {filename}")
            print(f"          Expected at: {md_path}")
            print(f"          Skipping {expected_count} examples.")
            continue

        print_section(f"Batch {batch_num:02d} — {context_label}  ({filename})")

        examples = extract_examples(md_path)
        if len(examples) != expected_count:
            print(f"  [WARN] Expected {expected_count} examples, extracted {len(examples)}")
        else:
            print(f"  Extracted {len(examples)} examples — running engine...")

        total_extracted += len(examples)

        for ex in examples:
            corpus_id = ex['corpus_id']
            text      = ex['text']

            # Show progress dot
            print(f"    {corpus_id} ... ", end="", flush=True)

            result = run_example(corpus_id, text)
            result['batch']         = batch_num
            result['context']       = context_label
            result['subtype']       = ex['subtype']
            result['text_preview']  = text[:120].replace('\n', ' ')

            all_results.append(result)
            batch_results.setdefault(batch_num, []).append(result)
            context_results.setdefault(context_label, []).append(result)
            total_run += 1

            risk    = result['overall_risk']
            score   = result.get('score')
            score_s = f" ({score:.3f})" if isinstance(score, float) else ""
            fp_flag = " ← FALSE POSITIVE" if result['false_positive'] else ""

            print(f"{risk}{score_s}{fp_flag}")

            if result['false_positive']:
                false_positives.append(result)

    # ── Summary tables ────────────────────────────────────────────────────────
    print_header("CALIBRATION RESULTS SUMMARY")

    # Per-batch table
    print("\n  FALSE POSITIVE RATE BY BATCH\n")
    print(f"  {'Batch':>5}  {'Context':<38}  {'FP Rate':>20}")
    print(f"  {'-----':>5}  {'-'*38}  {'-'*20}")

    overall_fp    = 0
    overall_total = 0
    anti_fp       = 0
    anti_total    = 0

    for batch_num, context_label, _, _ in CORPUS_FILES:
        if batch_num not in batch_results:
            print(f"  {batch_num:>5}  {context_label:<38}  {'MISSING':>20}")
            continue
        results = batch_results[batch_num]
        fp      = sum(1 for r in results if r['false_positive'])
        total   = len(results)

        overall_fp    += fp
        overall_total += total

        if batch_num in ANTI_BATCHES:
            anti_fp    += fp
            anti_total += total
            rate_str = anti_fp_rate(fp, total)
        else:
            rate_str = fp_rate(fp, total)

        print(f"  {batch_num:>5}  {context_label:<38}  {rate_str:>20}")

    print()
    print(f"  {'OVERALL':>5}  {'All batches (1–12)':<38}  {fp_rate(overall_fp, overall_total):>20}")
    print(f"  {'ANTI':>5}  {'Anti-pattern batches (10–12)':<38}  {anti_fp_rate(anti_fp, anti_total):>20}")

    # Per-context table
    print("\n\n  FALSE POSITIVE RATE BY ENTERPRISE CONTEXT\n")
    context_groups = {
        "Financial services": ["FIN — Collections letters", "FIN — Lending decisions", "FIN — Fraud operations"],
        "Legal":              ["LEGAL — Demand letters", "LEGAL — Settlement & regulatory"],
        "Internal org":       ["INT — Manager & executive", "INT — IT, HR & policy"],
        "Advisory":           ["ADV — Financial & accounting", "ADV — Specialist & consultant"],
        "Anti-pattern":       ["ANTI — Template institutional", "ANTI — Regulatory urgency", "ANTI — Expert confidence"],
    }

    print(f"  {'Context group':<25}  {'FP Rate':>20}")
    print(f"  {'-'*25}  {'-'*20}")

    for group_name, labels in context_groups.items():
        group_fp    = 0
        group_total = 0
        for label in labels:
            if label in context_results:
                results      = context_results[label]
                group_fp    += sum(1 for r in results if r['false_positive'])
                group_total += len(results)
        if group_total == 0:
            print(f"  {group_name:<25}  {'MISSING':>20}")
            continue
        if group_name == "Anti-pattern":
            rate_str = anti_fp_rate(group_fp, group_total)
        else:
            rate_str = fp_rate(group_fp, group_total)
        print(f"  {group_name:<25}  {rate_str:>20}")

    # False positive detail
    if false_positives:
        print_section(f"FALSE POSITIVES — {len(false_positives)} EXAMPLES FLAGGED")
        for r in false_positives:
            print(f"\n  {r['corpus_id']}  [{r['overall_risk']}]  Batch {r['batch']}")
            print(f"  Subtype : {r['subtype'][:70]}")
            print(f"  Preview : {r['text_preview'][:100]}...")
            if r.get('summary'):
                print(f"  Summary : {r['summary'][:120]}")
            if r.get('signals_fired'):
                print(f"  Signals : {r['signals_fired']}")
    else:
        print("\n  ✅ NO FALSE POSITIVES — all 170 examples returned LOW")

    # Overall verdict
    print_header("VERDICT")
    overall_rate = overall_fp / overall_total * 100 if overall_total > 0 else 0
    anti_rate    = anti_fp / anti_total * 100 if anti_total > 0 else 0

    if overall_rate < 10 and anti_rate < 5:
        print(f"  ✅ CALIBRATION PASS")
        print(f"     Overall FP rate : {overall_rate:.1f}% (target < 10%)")
        print(f"     Anti-pattern FP : {anti_rate:.1f}% (target < 5%)")
        print(f"     Engine is ready for calibration review and API wiring.")
        verdict = "PASS"
    else:
        print(f"  ❌ CALIBRATION FAIL — thresholds require adjustment")
        print(f"     Overall FP rate : {overall_rate:.1f}% (target < 10%)")
        print(f"     Anti-pattern FP : {anti_rate:.1f}% (target < 5%)")
        if overall_rate >= 10:
            print(f"     → Return to calibration_baseline_v1.md for the")
            print(f"       contexts with highest FP rate and adjust signal")
            print(f"       weights for the most active detector families.")
            print(f"       Do NOT adjust numbers until they fit — return to")
            print(f"       the baseline document first.")
        if anti_rate >= 5:
            print(f"     → Anti-pattern FP rate too high.")
            print(f"       The engine is confusing institutional template")
            print(f"       language or expert polish with synthetic smoothness.")
            print(f"       Review Batch 10/11/12 false positives specifically.")
        verdict = "FAIL"

    # ── Save results to JSON ──────────────────────────────────────────────────
    timestamp  = datetime.now().strftime("%Y%m%d_%H%M%S")
    out_path   = SRC_DIR / f"calibration_results_{timestamp}.json"

    output = {
        "timestamp":          datetime.now().isoformat(),
        "verdict":            verdict,
        "overall_fp_rate":    round(overall_rate, 2),
        "anti_fp_rate":       round(anti_rate, 2),
        "total_examples":     total_run,
        "total_fp":           overall_fp,
        "targets": {
            "overall":        "< 10%",
            "anti_pattern":   "< 5%",
        },
        "by_batch": {
            str(b): {
                "context":    CORPUS_FILES[b-1][2] if b <= len(CORPUS_FILES) else "unknown",
                "total":      len(batch_results.get(b, [])),
                "fp":         sum(1 for r in batch_results.get(b, []) if r['false_positive']),
            }
            for b in sorted(batch_results.keys())
        },
        "false_positives": [
            {
                "corpus_id":   r['corpus_id'],
                "batch":       r['batch'],
                "context":     r['context'],
                "overall_risk": r['overall_risk'],
                "score":       r.get('score'),
                "subtype":     r['subtype'],
                "text_preview": r['text_preview'],
                "summary":     r.get('summary', ''),
                "signals_fired": r.get('signals_fired', []),
            }
            for r in false_positives
        ],
        "all_results": [
            {
                "corpus_id":   r['corpus_id'],
                "batch":       r['batch'],
                "context":     r['context'],
                "overall_risk": r['overall_risk'],
                "score":       r.get('score'),
                "false_positive": r['false_positive'],
            }
            for r in all_results
        ],
    }

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"\n  Results saved to: {out_path.name}")
    print()

    return 0 if verdict == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())