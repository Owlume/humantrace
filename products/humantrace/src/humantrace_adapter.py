# src/humantrace_adapter.py
# HumanTrace — Elenx Engine Adapter
# Powered by Owlume
#
# Purpose:
#   Routes external fraud messages through the existing ElenxEngine
#   rather than running parallel detection logic.
#   Makes HumanTrace a true Owlume application layer.
#
# Architecture:
#   External message
#        downarrow
#   HumanTraceAdapter.analyze()
#   - reframes message for Critical mode reasoning audit
#   - calls ElenxEngine.analyze()
#        downarrow
#   ElenxEngine (existing, unchanged)
#   - detects reasoning patterns via Questioncraft Matrix
#   - generates blind spot questions (Thiel/Peterson/Feynman)
#        downarrow
#   _map_engine_to_signal()
#   - maps engine output to RED/YELLOW/GREEN
#   - maps context drivers to manipulation tactics
#   - combines with pattern library for fraud-specific detection
#        downarrow
#   ScanResult (same structure as humantrace_scanner.py)
#
# Governance alignment:
#   Inherits all Owlume governance constraints.
#   Output kind: SIGNAL - not ACTION, ADVICE, or INSTRUCTIONS.
#   Stage 14 BLOCK does not apply.

from __future__ import annotations

import re
import uuid
import datetime as dt
from typing import Dict, List, Optional, Any, Tuple

# Import Owlume infrastructure
import sys as _sys
import os as _os
_sys.path.insert(0, _os.path.join(_os.path.dirname(__file__), "..", "..", "..", "owlume_core"))

try:
    from elenx_loader import load_all
    from elenx_engine import ElenxEngine, DetectionResult
    ELENX_AVAILABLE = True
except ImportError:
    ELENX_AVAILABLE = False

# Import HumanTrace pattern library (reuse from scanner)
try:
    from humantrace_scanner import (
        SYNTHETIC_PATTERNS,
        HUMAN_MARKERS,
        CONTEXT_PLAUSIBILITY,
        LayerResult,
        ScanResult,
        RED_THRESHOLD,
        GREEN_THRESHOLD,
        YELLOW_LOW,
    )
    SCANNER_AVAILABLE = True
except ImportError:
    SCANNER_AVAILABLE = False


# Engine singleton - load once, reuse across requests
_engine_instance: Optional[Any] = None
_engine_load_error: Optional[str] = None


def _get_engine() -> Optional[Any]:
    """Get or initialise the ElenxEngine singleton."""
    global _engine_instance, _engine_load_error
    if _engine_instance is not None:
        return _engine_instance
    if _engine_load_error is not None:
        return None
    if not ELENX_AVAILABLE:
        _engine_load_error = "ElenxEngine not available"
        return None
    try:
        packs = load_all()
        _engine_instance = ElenxEngine(packs)
        return _engine_instance
    except Exception as e:
        _engine_load_error = str(e)
        return None


# Fraud mode reframing
# The Questioncraft Matrix Critical mode questions map directly to
# fraud detection when reoriented from inward to outward.

# Primers are designed to activate Critical mode in the ElenxEngine.
# They inject Critical mode keywords: incentive, risk, conflict, pressure,
# stakeholder, bias, contradict, challenge — which bias the engine toward
# Critical x Stakeholder / Risk / Assumption detection.

FRAUD_CONTEXT_PRIMERS = {
    "bank_officer": (
        "Critical analysis of a suspicious communication. "
        "Incentive misalignment risk: the sender may have conflicting interests. "
        "Stakeholder pressure detected. Hidden risk and second-order consequences. "
        "Challenge: whose interests does this message actually serve? "
        "What assumption must I accept for this to work? "
        "What irreversible risk exists if I act on this now?"
    ),
    "investment_opportunity": (
        "Critical analysis of an investment claim. "
        "Incentive distortion: guaranteed returns contradict market risk reality. "
        "Stakeholder conflict: sender benefits from my action regardless of my outcome. "
        "Second-order risk: what is the hidden downside being concealed? "
        "Bias challenge: what assumption is being planted about risk and reward? "
        "What evidence is missing that a legitimate opportunity would provide?"
    ),
    "friend_in_distress": (
        "Critical analysis of a distress communication. "
        "Stakeholder pressure: emotional urgency being used to override careful thought. "
        "Incentive misalignment: payment method requested is inconsistent with genuine distress. "
        "Risk: irreversible financial transfer being requested under time pressure. "
        "Challenge: what would a genuine friend in this situation actually say and do? "
        "What assumption must I accept about the sender's identity and situation?"
    ),
    "default": (
        "Critical analysis of a suspicious communication. "
        "Stakeholder conflict: whose interests does this message serve? "
        "Incentive misalignment: what does the sender gain from my action? "
        "Hidden risk: what irreversible consequence could follow if I comply? "
        "Bias challenge: what assumption is being planted to override careful thought? "
        "Second-order consequence: what happens after I take the action being requested?"
    ),
}


def _build_audit_prompt(message: str, context_hint: Optional[str]) -> str:
    """Reframe external message as a reasoning audit input."""
    primer = FRAUD_CONTEXT_PRIMERS.get(
        context_hint or "default",
        FRAUD_CONTEXT_PRIMERS["default"]
    )
    return f"{primer}\n\nMessage to examine:\n{message}"


# Maps Questioncraft Matrix modes to fraud signal weights
MODE_FRAUD_WEIGHTS = {
    "Critical":    0.85,
    "Analytical":  0.60,
    "Reflective":  0.35,
    "Growth":      0.30,
    "Creative":    0.25,
}

# Maps Matrix principles to specific fraud tactics
PRINCIPLE_FRAUD_MAP = {
    "Stakeholder":           "social_pressure",
    "Risk":                  "risk_concealment",
    "Assumption":            "false_premise",
    "Clarity":               "deliberate_obscurity",
    "Evidence":              "evidence_suppression",
    "Action":                "premature_action",
    "Evidence & Validation": "evidence_suppression",
    "Root Cause":            "distraction",
    "Exploration":           "false_opportunity",
    "Iteration":             "false_progress",
}

# Maps context drivers to fraud manipulation tactics
DRIVER_FRAUD_MAP = {
    "time_pressure":         "manufactured_urgency",
    "identity_protection":   "authority_impersonation",
    "misaligned_incentives": "false_reward",
    "moral_hazard":          "risk_elimination_claim",
    "overload":              "complexity_as_cover",
    "complexity":            "deliberate_obscurity",
    "confirmation_drift":    "desire_mirroring",
    "groupthink":            "social_proof_fraud",
    "status_quo_bias":       "false_normalcy",
}


def _match_any(text: str, patterns: List[str]) -> List[str]:
    """Return list of patterns that match in text."""
    return [p for p in patterns if re.search(p, text, re.IGNORECASE)]


def _run_pattern_library(text: str) -> Tuple[str, float, Optional[str]]:
    """Run the pattern library against the message."""
    if not SCANNER_AVAILABLE:
        return "uncertain", 0.45, None

    t = text.lower()
    category_scores: Dict[str, int] = {}

    for category, patterns in SYNTHETIC_PATTERNS.items():
        if category == "purpose_pure_construction":
            continue
        hits = _match_any(t, patterns)
        if hits:
            category_scores[category] = len(hits)

    if not category_scores:
        return "uncertain", 0.45, None

    top_category = max(category_scores, key=category_scores.get)
    total_hits = sum(category_scores.values())
    conf = min(0.60 + total_hits * 0.05, 0.92)
    return "synthetic", round(conf, 3), top_category


def _map_engine_to_signal(
    det: Any,
    questions: List[str],
    message: str,
    context_hint: Optional[str],
) -> Tuple[str, float, List[Any], Optional[str], Dict[str, Any]]:
    """Map ElenxEngine DetectionResult to HumanTrace signal."""
    t = message.lower()
    layers = []

    # Layer 1: Engine mode signal
    mode_weight = MODE_FRAUD_WEIGHTS.get(det.mode, 0.45)
    principle_tactic = PRINCIPLE_FRAUD_MAP.get(det.principle, None)

    l1_findings = [f"Reasoning pattern detected — confidence: {det.confidence:.0%}"]
    if det.mode == "Critical":
        l1_findings.append("High-confidence synthetic reasoning pattern detected")
        l1_signal = "synthetic"
        l1_conf = min(mode_weight * det.confidence + 0.15, 0.85)
    elif det.mode == "Analytical":
        l1_findings.append("Structured reasoning present — authenticity unclear")
        l1_signal = "uncertain"
        l1_conf = 0.50
    else:
        l1_findings.append(f"Low synthetic reasoning indicators detected")
        l1_signal = "human"
        l1_conf = 0.45

    if principle_tactic:
        l1_findings.append(f"Associated influence pattern: {principle_tactic.replace('_', ' ')}")

    layers.append(LayerResult(
        layer="engine_mode_detection",
        signal=l1_signal,
        confidence=round(l1_conf, 3),
        findings=l1_findings,
    ))

    # Layer 2: Context driver analysis
    detected_drivers = (det.tags or {}).get("contexts", [])
    driver_tactics = []
    l2_findings = []

    for driver in detected_drivers:
        for driver_key, tactic in DRIVER_FRAUD_MAP.items():
            if driver_key.lower() in driver.lower():
                driver_tactics.append(tactic)
                l2_findings.append(f"Driver '{driver}' -> manipulation tactic: {tactic}")

    if driver_tactics:
        l2_signal = "synthetic"
        l2_conf = min(0.55 + len(driver_tactics) * 0.10, 0.85)
    else:
        l2_signal = "uncertain"
        l2_conf = 0.45
        l2_findings.append("No influence patterns detected")

    layers.append(LayerResult(
        layer="manipulation_driver_analysis",
        signal=l2_signal,
        confidence=round(l2_conf, 3),
        findings=l2_findings,
    ))

    # Layer 3: Conviction cost
    human_score = 0.0
    l3_findings = []

    cost_hits = _match_any(t, HUMAN_MARKERS.get("cost_of_conclusion", []))
    noise_hits = _match_any(t, HUMAN_MARKERS.get("irrelevant_human_noise", []))
    correction_hits = _match_any(t, HUMAN_MARKERS.get("self_correction", []))
    eagerness_hits = _match_any(t, HUMAN_MARKERS.get("genuine_eagerness", []))

    if cost_hits:
        human_score += 0.30
        l3_findings.append("Personal investment present — genuine stakes visible")
    if noise_hits:
        human_score += 0.20
        l3_findings.append("Off-topic human noise present")
    if correction_hits:
        human_score += 0.25
        l3_findings.append("Self-correction detected - strong human authenticity signal")
    if eagerness_hits:
        human_score += 0.20
        l3_findings.append("Genuine eagerness signal detected")

    if not any([cost_hits, noise_hits, correction_hits, eagerness_hits]):
        perfect_confidence = re.search(
            r"\b(you will|you must|guaranteed|absolutely|definitely|certainly)\b",
            t, re.IGNORECASE
        )
        if perfect_confidence:
            l3_findings.append("Costless confidence - no personal stakes or doubt visible")
            l3_signal = "synthetic"
            l3_conf = 0.65
        else:
            l3_findings.append("No personal investment signals detected")
            l3_signal = "uncertain"
            l3_conf = 0.45
    else:
        l3_signal = "human"
        l3_conf = min(0.50 + human_score, 0.80)

    layers.append(LayerResult(
        layer="conviction_cost",
        signal=l3_signal,
        confidence=round(l3_conf, 3),
        findings=l3_findings,
    ))

    # Layer 4: Pattern library
    l4_signal, l4_conf, fraud_category = _run_pattern_library(message)
    l4_findings = []

    if fraud_category:
        l4_findings.append(f"Pattern match: {fraud_category.replace('_', ' ').title()}")
        l4_signal = "synthetic"
    else:
        l4_findings.append("No known fraud pattern signatures detected")

    l4_layer = LayerResult(
        layer="pattern_library",
        signal=l4_signal,
        confidence=l4_conf,
        findings=l4_findings,
    )
    l4_layer.__dict__["_top_category"] = fraud_category
    layers.append(l4_layer)

    # Layer 5: Engine question quality
    l5_findings = []
    if questions:
        critical_q_markers = [
            "incentive", "stakeholder", "assumption", "distort",
            "backfire", "hidden", "ignored", "harm", "conflict"
        ]
        critical_hits = sum(
            1 for q in questions
            if any(m in q.lower() for m in critical_q_markers)
        )
        if critical_hits >= 2:
            l5_findings.append(
                f"Generated {critical_hits} investigation questions — "
                f"pattern consistent with synthetic reasoning"
            )
            l5_signal = "synthetic"
            l5_conf = min(0.55 + critical_hits * 0.08, 0.80)
        else:
            l5_findings.append("Investigation questions show low synthetic reasoning indicators")
            l5_signal = "uncertain"
            l5_conf = 0.45
    else:
        l5_findings.append("No engine questions generated")
        l5_signal = "uncertain"
        l5_conf = 0.45

    layers.append(LayerResult(
        layer="engine_question_quality",
        signal=l5_signal,
        confidence=round(l5_conf, 3),
        findings=l5_findings,
    ))

    # Aggregate signal
    synthetic_votes = sum(1 for l in layers if l.signal == "synthetic")
    human_votes = sum(1 for l in layers if l.signal == "human")

    weights = [1.0, 1.0, 1.0, 2.0, 1.0]
    weighted_conf = sum(
        l.confidence * w for l, w in zip(layers, weights)
    ) / sum(weights)

    # Mixed content detection
    confidences = [l.confidence for l in layers]
    spread = max(confidences) - min(confidences)
    mixed_meta: Dict[str, Any] = {}
    is_mixed = (
        spread >= 0.30 or
        (synthetic_votes >= 1 and human_votes >= 1) or
        (synthetic_votes >= 2 and weighted_conf < RED_THRESHOLD)
    )
    if is_mixed and synthetic_votes >= 1:
        mixed_meta = {
            "mixed_content_warning": True,
            "mixed_content_note": (
                "Mixed signals detected across reasoning layers — "
                "result is uncertain. Verify sender independently."
            ),
            "layer_spread": round(spread, 3),
        }

    # L4 veto
    if l4_layer.signal == "synthetic" and l4_layer.confidence >= 0.65:
        if synthetic_votes >= 2:
            signal = "red"
            confidence = min(weighted_conf * 1.20, 0.95)
            return signal, round(confidence, 3), layers, fraud_category, mixed_meta

    if synthetic_votes >= 3:
        conf = weighted_conf
        signal = "red" if conf >= RED_THRESHOLD else "yellow"
        return signal, round(conf, 3), layers, fraud_category, mixed_meta

    if human_votes >= 3:
        conf = weighted_conf
        signal = "green" if conf >= GREEN_THRESHOLD else "yellow"
        return signal, round(conf, 3), layers, fraud_category, mixed_meta

    return "yellow", round(max(weighted_conf, YELLOW_LOW), 3), layers, fraud_category, mixed_meta


class HumanTraceAdapter:
    """
    HumanTrace fraud detection via Owlume Elenx Engine.
    Falls back to humantrace_scanner.py if engine unavailable.
    """

    def __init__(self, bse_history: Optional[Dict[str, Any]] = None):
        self.bse_history = bse_history or {}
        self.first_contact = not bool(bse_history)
        self._engine = _get_engine()
        self._engine_available = self._engine is not None

    def scan(self, message: str, context_hint: Optional[str] = None) -> Any:
        message = (message or "").strip()
        if not message:
            return self._empty_result()

        if not self._engine_available or not SCANNER_AVAILABLE:
            from humantrace_scanner import scan_message
            return scan_message(message=message, context_hint=context_hint,
                              bse_history=self.bse_history)

        try:
            return self._scan_via_engine(message, context_hint)
        except Exception as e:
            from humantrace_scanner import scan_message
            result = scan_message(message=message, context_hint=context_hint,
                                bse_history=self.bse_history)
            result.meta["engine_error"] = str(e)
            result.meta["fallback_used"] = True
            return result

    def _scan_via_engine(self, message: str, context_hint: Optional[str]) -> Any:
        audit_prompt = _build_audit_prompt(message, context_hint)
        det, questions = self._engine.analyze(text=audit_prompt, empathy_on=False)

        signal, confidence, layers, fraud_category, mixed_meta = _map_engine_to_signal(
            det=det, questions=questions, message=message, context_hint=context_hint,
        )

        plain_english = self._plain_english(signal, confidence, fraud_category, mixed_meta)
        recommended_action = self._recommended_action(signal)
        analyst_questions = self._build_analyst_questions(
            questions=questions, layers=layers,
            context_hint=context_hint, mixed_meta=mixed_meta,
        )

        return ScanResult(
            scan_id=str(uuid.uuid4()),
            timestamp=dt.datetime.utcnow().isoformat() + "Z",
            signal=signal,
            confidence=round(confidence, 3),
            first_contact=self.first_contact,
            layers=layers,
            fraud_category=fraud_category,
            plain_english=plain_english,
            recommended_action=recommended_action,
            analyst_questions=analyst_questions,
            meta={
                "message_length": len(message),
                "context_hint": context_hint,
                "bse_available": not self.first_contact,
                "engine_mode": det.mode,
                "engine_principle": det.principle,
                "engine_confidence": det.confidence,
                "engine_used": True,
                "fallback_used": False,
                **mixed_meta,
                "governance": {
                    "output_kind": "SIGNAL",
                    "stage14_applies": False,
                    "interpretation": "narrow",
                    "false_green_is_catastrophic": True,
                }
            }
        )

    def _plain_english(self, signal, confidence, fraud_category, mixed_meta=None):
        pct = int(confidence * 100)
        mixed_meta = mixed_meta or {}
        if signal == "red":
            cat = fraud_category.replace("_", " ").title() if fraud_category else "Fraud"
            base = (f"No genuine human reasoning detected behind this message "
                    f"({pct}% confidence). Pattern consistent with {cat}. "
                    f"Treat with extreme caution.")
            if mixed_meta.get("mixed_content_warning"):
                base += " Note: message shows mixed reasoning signals — treat with caution."
            return base
        if signal == "green":
            return (f"Human reasoning presence detected ({pct}% confidence). "
                    f"Standard caution still applies.")
        if mixed_meta.get("mixed_content_warning"):
            return (f"Mixed signals detected ({pct}% confidence) — "
                    f"some human indicators present alongside structured patterns. "
                    f"Result is uncertain. Verify sender independently.")
        if self.first_contact:
            return (f"Reasoning signal is unclear ({pct}% confidence) - "
                    f"no prior communication history for this sender. "
                    f"Verify independently before responding.")
        return (f"Mixed reasoning signals detected ({pct}% confidence). "
                f"Do not act until sender is independently verified.")

    def _recommended_action(self, signal):
        if signal == "red":
            return ("Before responding: can you verify this sender through an "
                    "official channel completely independent of this message?")
        if signal == "green":
            return "Human presence indicators are present. Standard verification still recommended."
        return ("Before responding: verify the sender's identity through a channel "
                "you established yourself, not one provided in this message.")

    def _build_analyst_questions(self, questions, layers, context_hint, mixed_meta=None):
        mixed_meta = mixed_meta or {}
        output = ["Can the sender be verified through an official channel completely independent of this message?"]

        if mixed_meta.get("mixed_content_warning"):
            output.append("Which sections feel genuinely personal - and which feel templated or too perfectly structured?")

        for q in questions[:3]:
            reframed = self._reframe_question_outward(q)
            if reframed and reframed not in output:
                output.append(reframed)

        if self.first_contact:
            output.append("This is the first communication from this sender. Why are they contacting you now?")

        return output[:5]

    def _reframe_question_outward(self, question: str) -> str:
        q = question.strip()
        for prefix in ["Thiel ->", "Peterson ->", "Feynman ->", "Thiel:", "Peterson:", "Feynman:"]:
            if q.startswith(prefix):
                q = q[len(prefix):].strip()

        rewrites = [
            (r"non.obvious assumption", "What assumption is the sender making about what you will believe?"),
            (r"must be true here for this to work", "What must you believe for this message to achieve its goal?"),
            (r"interests or incentives could distort", "Whose interests does this message actually serve?"),
            (r"counter.evidence or missing data", "What evidence is the sender NOT providing that a legitimate communicator would include?"),
            (r"hidden downside|worst.case", "What downside is this message designed to prevent you from noticing?"),
            (r"ambiguity that could conceal", "Where is the deliberate vagueness in this message?"),
            (r"action here may backfire|cause harm", "What action is this message trying to trigger - and what happens if you take it?"),
            (r"smallest actionable|smallest step", "What is the smallest thing you can verify before taking any action?"),
            (r"smart 12.year.old|explain it simply", "If you explained this message to a skeptical friend, what would sound suspicious?"),
        ]

        q_lower = q.lower()
        for pattern, rewrite in rewrites:
            if re.search(pattern, q_lower):
                return rewrite

        if q and not q.endswith("?"):
            q += "?"
        return q if q else ""

    def _empty_result(self):
        from humantrace_scanner import ScanResult
        return ScanResult(
            scan_id=str(uuid.uuid4()),
            timestamp=dt.datetime.utcnow().isoformat() + "Z",
            signal="yellow", confidence=0.0, first_contact=True,
            layers=[], fraud_category=None,
            plain_english="No message provided for analysis.",
            recommended_action="Please provide the suspicious message text.",
            analyst_questions=[], meta={"error": "empty_input"},
        )


def scan_message_via_engine(
    message: str,
    context_hint: Optional[str] = None,
    bse_history: Optional[Dict[str, Any]] = None,
) -> Any:
    """Convenience wrapper. Uses ElenxEngine if available, falls back automatically."""
    adapter = HumanTraceAdapter(bse_history=bse_history)
    return adapter.scan(message, context_hint=context_hint)