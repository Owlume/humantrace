# src/humantrace_adapter.py
# HumanTrace — v0 Engine Adapter
# Powered by Owlume
#
# Purpose:
#   Routes scan requests through the validated HumanTrace v0 engine
#   (main.py / analyse_message) and translates the result into the
#   ScanResult contract expected by humantrace_api.py.
#
# Architecture:
#   External message
#        ↓
#   scan_message_via_engine()
#        ↓
#   analyse_message()  ←  main.py (five detectors + fusion layer)
#        ↓
#   _translate_to_scan_result()
#   - maps low/medium/high → green/yellow/red
#   - maps detected_features → LayerResult list
#   - builds plain_english from summary + plain_reasoning
#        ↓
#   ScanResult  (same contract as humantrace_scanner.py)
#
# Fallback:
#   If main.py is unavailable for any reason, falls back automatically
#   to humantrace_scanner.py. humantrace_api.py sees no difference.
#
# Governance:
#   Output kind: SIGNAL — not ACTION, ADVICE, or INSTRUCTIONS.
#   No recommended_action field contains prescriptive guidance.

from __future__ import annotations

import uuid
import datetime as dt
from typing import Any, Dict, List, Optional

# ── Import v0 engine ──────────────────────────────────────────────────────────

try:
    from main import analyse_message
    ENGINE_AVAILABLE = True
except ImportError:
    ENGINE_AVAILABLE = False

# ── Import ScanResult / LayerResult from scanner ─────────────────────────────
# We reuse these dataclasses — no need to duplicate them.

try:
    from humantrace_scanner import ScanResult, LayerResult
    SCANNER_AVAILABLE = True
except ImportError:
    SCANNER_AVAILABLE = False


# ── Risk label translation ────────────────────────────────────────────────────

_RISK_TO_SIGNAL = {
    "high":   "red",
    "medium": "yellow",
    "low":    "green",
}

# Human-readable family labels for layer display
_FAMILY_DISPLAY = {
    "intent":     "Extraction Intent",
    "trust":      "Trust Hijack",
    "pressure":   "Urgency Pressure",
    "distortion": "Reasoning Distortion",
    "auth_gap":   "Authenticity Gap",
}


# ── Recommended action builder ────────────────────────────────────────────────
# Non-prescriptive. Surfaces a question, not an instruction.
# Consistent with signal-to-action boundary (locked 2026-03-30).

def _build_recommended_action(signal: str) -> str:
    if signal == "red":
        return (
            "Before responding: can you verify this sender through an "
            "official channel completely independent of this message?"
        )
    if signal == "green":
        return (
            "Human presence indicators are present. "
            "Standard verification of sender identity still recommended."
        )
    return (
        "Before responding or acting: verify the sender's identity "
        "through a channel you established yourself, not one provided "
        "in this message."
    )


# ── Layer builder ─────────────────────────────────────────────────────────────

def _build_layers(engine_result: dict) -> List[Any]:
    """
    Translate v0 engine output into a list of LayerResult objects.

    We create one layer per active signal family, plus one summary layer
    for composite patterns. This gives the UI a meaningful layer breakdown
    without fabricating data.
    """
    if not SCANNER_AVAILABLE:
        return []

    layers = []
    signal_scores = engine_result.get("signal_scores", {})
    detected_features = engine_result.get("detected_features", [])
    negative_features = engine_result.get("negative_features", [])
    composite_patterns = engine_result.get("composite_patterns", [])
    dominant = engine_result.get("dominant_family")
    risk_label = engine_result.get("overall_risk", {}).get("label", "low")
    overall_signal = _RISK_TO_SIGNAL.get(risk_label, "yellow")

    # One layer per signal family that fired above noise floor
    for family, score in signal_scores.items():
        if score < 0.05:
            continue  # below noise floor — skip

        display_name = _FAMILY_DISPLAY.get(family, family.replace("_", " ").title())

        # Collect features belonging to this family
        prefix = f"HT.{family[:3].upper()}"
        family_features = [
            f for f in detected_features
            if f.get("signal_id", "").upper().startswith(prefix)
        ]

        findings = []
        for feat in family_features:
            label = feat.get("label", "")
            evidence = feat.get("evidence", "")
            if label:
                findings.append(label + (f" — {evidence}" if evidence else ""))

        if not findings:
            # Score present but no labelled features — note the score
            findings.append(
                f"{display_name} signal score: {score:.2f}"
            )

        # Map score to a layer signal
        if score >= 0.35:
            layer_signal = "synthetic"
        elif score >= 0.15:
            layer_signal = "uncertain"
        else:
            layer_signal = "human"

        layers.append(LayerResult(
            layer=family,
            signal=layer_signal,
            confidence=round(min(score + 0.45, 0.95), 3),
            findings=findings,
        ))

    # Composite pattern layer — only if patterns fired
    if composite_patterns:
        cp_findings = [
            f"{cp.get('label', '')}: {cp.get('description', '')}"
            for cp in composite_patterns
            if cp.get("label")
        ]
        layers.append(LayerResult(
            layer="composite_patterns",
            signal="synthetic",
            confidence=0.85,
            findings=cp_findings,
        ))

    # Negative features layer — only if present and signal is not red
    if negative_features and overall_signal != "red":
        layers.append(LayerResult(
            layer="legitimacy_markers",
            signal="human",
            confidence=0.70,
            findings=[f"Legitimacy marker detected: {nf}" for nf in negative_features[:4]],
        ))

    return layers


# ── Plain English builder ─────────────────────────────────────────────────────

def _build_plain_english(engine_result: dict, signal: str, confidence: float) -> str:
    """
    Build the plain_english field from the engine's summary and
    plain_reasoning sentences.
    """
    summary = engine_result.get("summary", "")
    plain_reasoning = engine_result.get("plain_reasoning", [])
    pct = int(confidence * 100)

    if signal == "red":
        composite = engine_result.get("composite_patterns", [])
        cat = composite[0].get("label", "Fraud") if composite else "Fraud"
        dominant = engine_result.get("dominant_family")
        if dominant:
            cat = _FAMILY_DISPLAY.get(dominant, cat)
        base = (
            f"No genuine human reasoning detected behind this message "
            f"({pct}% confidence). Pattern consistent with {cat}."
        )
        if plain_reasoning:
            base += f" {plain_reasoning[0]}"
        return base

    if signal == "green":
        base = f"Human reasoning presence detected ({pct}% confidence)."
        if plain_reasoning:
            base += f" {plain_reasoning[0]}"
        else:
            base += " Standard caution still applies."
        return base

    # Yellow
    if summary:
        return f"{summary} ({pct}% confidence)."
    return (
        f"Mixed reasoning signals detected ({pct}% confidence). "
        f"Insufficient evidence to confirm human presence."
    )


# ── Fraud category extractor ──────────────────────────────────────────────────

def _extract_fraud_category(engine_result: dict) -> Optional[str]:
    """
    Derive a fraud category string from composite_patterns or dominant_family.
    Returns None if signal is low-risk.
    """
    composite = engine_result.get("composite_patterns", [])
    if composite:
        return composite[0].get("pattern_id") or composite[0].get("label")
    dominant = engine_result.get("dominant_family")
    if dominant and engine_result.get("overall_risk", {}).get("label") in ("medium", "high"):
        return dominant
    return None


# ── Analyst questions builder ─────────────────────────────────────────────────

def _build_analyst_questions(engine_result: dict, signal: str) -> List[str]:
    """
    Build analyst questions from the engine result.
    Always includes the core verification question.
    """
    questions = [
        "Can the sender be verified through an official channel "
        "completely independent of this message?"
    ]

    dominant = engine_result.get("dominant_family")
    composite = engine_result.get("composite_patterns", [])

    if dominant == "pressure":
        questions.append(
            "Does the urgency in this message feel earned by the "
            "circumstances — or was it inserted to prevent careful thinking?"
        )
    if dominant == "trust":
        questions.append(
            "Can you verify the sender's claimed identity or role through "
            "a source you found independently?"
        )
    if dominant == "intent":
        questions.append(
            "What exactly is being asked of you — and what happens "
            "if you delay or decline?"
        )
    if dominant == "distortion":
        questions.append(
            "Does this message present a false choice — or suggest "
            "there is only one reasonable response?"
        )
    if dominant == "auth_gap":
        questions.append(
            "Does this message contain anything that serves no "
            "persuasive purpose — or is every element working toward one goal?"
        )
    if composite:
        questions.append(
            "Have you seen this type of message before — "
            "and what happened to people who acted on it?"
        )

    return questions[:5]


# ── Core translation ──────────────────────────────────────────────────────────

def _translate_to_scan_result(
    engine_result: dict,
    context_hint: Optional[str],
    bse_history: Optional[Dict[str, Any]],
) -> Any:
    """
    Translate analyse_message() output into a ScanResult.
    """
    risk = engine_result.get("overall_risk", {})
    risk_label = risk.get("label", "medium")
    signal = _RISK_TO_SIGNAL.get(risk_label, "yellow")
    confidence = risk.get("confidence", 0.5)

    layers = _build_layers(engine_result)
    plain_english = _build_plain_english(engine_result, signal, confidence)
    recommended_action = _build_recommended_action(signal)
    fraud_category = _extract_fraud_category(engine_result)
    analyst_questions = _build_analyst_questions(engine_result, signal)
    first_contact = not bool(bse_history)

    return ScanResult(
        scan_id=str(uuid.uuid4()),
        timestamp=dt.datetime.utcnow().isoformat() + "Z",
        signal=signal,
        confidence=round(confidence, 3),
        first_contact=first_contact,
        layers=layers,
        fraud_category=fraud_category,
        plain_english=plain_english,
        recommended_action=recommended_action,
        analyst_questions=analyst_questions,
        meta={
            "message_length": len(engine_result.get("summary", "")),
            "context_hint": context_hint,
            "bse_available": not first_contact,
            "engine_version": engine_result.get("engine_version", "humantrace-v0.1"),
            "engine_used": True,
            "fallback_used": False,
            "dominant_family": engine_result.get("dominant_family"),
            "score_breakdown": engine_result.get("score_breakdown", {}),
            "signal_scores": engine_result.get("signal_scores", {}),
            "governance": {
                "output_kind": "SIGNAL",
                "stage14_applies": False,
                "interpretation": "narrow",
                "false_green_is_catastrophic": True,
            },
        },
    )


# ── Public interface ──────────────────────────────────────────────────────────

def scan_message_via_engine(
    message: str,
    context_hint: Optional[str] = None,
    bse_history: Optional[Dict[str, Any]] = None,
) -> Any:
    """
    Scan a message through the HumanTrace v0 engine.

    Routes through analyse_message() from main.py.
    Falls back to humantrace_scanner.scan_message() if engine unavailable.

    Args:
        message:      The suspicious communication text.
        context_hint: Optional context e.g. "bank_officer".
        bse_history:  Optional longitudinal BSE data for this sender.

    Returns:
        ScanResult — same contract as humantrace_scanner.scan_message().
    """
    message = (message or "").strip()

    # Guard: engine or ScanResult unavailable — fall back immediately
    if not ENGINE_AVAILABLE or not SCANNER_AVAILABLE:
        from humantrace_scanner import scan_message
        return scan_message(
            message=message,
            context_hint=context_hint,
            bse_history=bse_history,
        )

    if not message:
        from humantrace_scanner import scan_message
        return scan_message(message="", context_hint=context_hint)

    try:
        engine_result = analyse_message({
            "input_id": "api",
            "text": message,
        })

        # Engine returned an error dict
        if "error" in engine_result:
            from humantrace_scanner import scan_message
            result = scan_message(
                message=message,
                context_hint=context_hint,
                bse_history=bse_history,
            )
            result.meta["engine_error"] = engine_result["error"]
            result.meta["fallback_used"] = True
            return result

        return _translate_to_scan_result(engine_result, context_hint, bse_history)

    except Exception as e:
        # Any failure — fall back silently, log error in meta
        from humantrace_scanner import scan_message
        result = scan_message(
            message=message,
            context_hint=context_hint,
            bse_history=bse_history,
        )
        result.meta["engine_error"] = str(e)
        result.meta["fallback_used"] = True
        return result