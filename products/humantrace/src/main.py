"""
HumanTrace — Main Entry Point
File: main.py

Single entry point for the HumanTrace v0 reasoning-risk engine.
Accepts a message payload, runs all five detectors, fuses the
results, and returns a structured detection result.

This is the function humantrace_api.py calls.

Usage:
    from main import analyse_message

    result = analyse_message({
        "input_id": "msg-001",
        "text": "Your account will be suspended...",
        "channel": "sms",
        "metadata": {
            "known_sender": False,
            "has_link": True,
        }
    })

Output shape:
    {
        "input_id": str,
        "engine_version": str,
        "overall_risk": {
            "label": "low" | "medium" | "high",
            "score": float,
            "confidence": float,
        },
        "signal_scores": {
            "intent": float,
            "trust": float,
            "pressure": float,
            "distortion": float,
            "auth_gap": float,
        },
        "dominant_family": str | None,
        "composite_patterns": [
            {
                "pattern_id": str,
                "label": str,
                "description": str,
            }
        ],
        "detected_features": [
            {
                "signal_id": str,
                "label": str,
                "evidence": str,
                "score_contribution": float,
            }
        ],
        "negative_features": [str],
        "score_breakdown": dict,
        "summary": str,
        "plain_reasoning": [str],
    }

Schema constraint (locked 2026-03-30):
    Output kind is SIGNAL only.
    No advice, guidance, or action prompts in any output field.
"""

from __future__ import annotations

import re
from typing import Any

from detectors.intent_detector import detect_intent
from detectors.trust_hijack_detector import detect_trust_hijack
from detectors.pressure_detector import detect_pressure
from detectors.distortion_detector import detect_distortion
from detectors.authenticity_gap_detector import detect_authenticity_gap
from fusion.risk_fuser import fuse, SignalScores

ENGINE_VERSION = "humantrace-v0.1"


# ---------------------------------------------------------------------------
# Explanation renderer
# ---------------------------------------------------------------------------

# Family display names for plain-language explanation
FAMILY_LABELS = {
    "intent":      "extraction intent",
    "trust":       "trust hijack",
    "pressure":    "urgency pressure",
    "distortion":  "reasoning distortion",
    "auth_gap":    "authenticity gap",
}

FAMILY_EXPLANATIONS = {
    "intent": (
        "The message contains signals associated with extracting something "
        "of value — money, credentials, personal data, or compliance — "
        "often combined with a request to act before verifying."
    ),
    "trust": (
        "The message borrows authority or legitimacy it has not earned — "
        "through institution impersonation, role claims, procedural language, "
        "or manufactured empathy."
    ),
    "pressure": (
        "The message compresses decision time or narrows available options — "
        "using urgency, threats of loss, artificial deadlines, or channel "
        "restrictions that prevent independent verification."
    ),
    "distortion": (
        "The message uses manipulative reasoning patterns — false dilemmas, "
        "fear override, circular self-justification, or contradictory "
        "commitments — to move the recipient toward compliance."
    ),
    "auth_gap": (
        "The message shows a gap in authentic human reasoning texture — "
        "unusually uniform language, no hedging or uncertainty, and "
        "high-stakes framing without concrete personal detail."
    ),
}


def _render_summary(risk_label: str, dominant: str | None,
                    composite_patterns: list, signal_scores: SignalScores) -> str:
    """One-sentence summary of the risk verdict."""
    if risk_label == "low":
        return (
            "This message does not show significant signals of malicious "
            "synthetic reasoning."
        )

    active_families = [
        FAMILY_LABELS[k] for k, v in {
            "intent":     signal_scores.intent,
            "trust":      signal_scores.trust,
            "pressure":   signal_scores.pressure,
            "distortion": signal_scores.distortion,
        }.items() if v > 0.15
    ]

    if risk_label == "high":
        if dominant:
            return (
                f"This message shows a high-risk pattern driven primarily by "
                f"{FAMILY_LABELS[dominant]} signals"
                + (f", with a {composite_patterns[0].label} pattern detected."
                   if composite_patterns else ".")
            )
        elif composite_patterns:
            return (
                f"This message shows a high-risk pattern matching "
                f"{composite_patterns[0].label} — "
                f"a combination of {', '.join(active_families[:2])} signals."
            )
        else:
            return (
                f"This message shows a high-risk pattern combining "
                f"{' and '.join(active_families[:3])} signals."
            )

    # medium
    if composite_patterns:
        return (
            f"This message shows a medium-risk pattern with "
            f"{composite_patterns[0].label} indicators — "
            f"elevated {' and '.join(active_families[:2])} signals."
        )
    return (
        f"This message shows a medium-risk pattern with elevated "
        f"{' and '.join(active_families[:2]) if active_families else 'risk'} signals."
    )


def _render_plain_reasoning(
    risk_label: str,
    signal_scores: SignalScores,
    features: list,
    negative_features: list[str],
) -> list[str]:
    """
    Two to four plain-language sentences explaining what the engine
    detected. Signal descriptions only — no advice, no guidance.
    """
    if risk_label == "low":
        reasons = ["No significant extraction, pressure, or trust manipulation signals were detected."]
        if negative_features:
            reasons.append(
                f"The message contained markers consistent with legitimate "
                f"communication: {', '.join(negative_features[:2])}."
            )
        return reasons

    reasons = []

    # Describe the strongest firing families in plain language
    family_scores = {
        "intent":     signal_scores.intent,
        "trust":      signal_scores.trust,
        "pressure":   signal_scores.pressure,
        "distortion": signal_scores.distortion,
        "auth_gap":   signal_scores.auth_gap,
    }
    active = sorted(
        [(k, v) for k, v in family_scores.items() if v > 0.15],
        key=lambda x: x[1], reverse=True
    )

    for family, score in active[:3]:
        reasons.append(FAMILY_EXPLANATIONS[family])

    # Note negative features if present
    if negative_features:
        reasons.append(
            f"Some markers of legitimate communication were also present "
            f"({', '.join(negative_features[:2])}), which were factored "
            f"into the score."
        )

    return reasons[:4]  # cap at four sentences


# ---------------------------------------------------------------------------
# Input validation
# ---------------------------------------------------------------------------

def _validate_payload(payload: dict) -> tuple[bool, str]:
    if not isinstance(payload, dict):
        return False, "Payload must be a dict."
    if "text" not in payload:
        return False, "Payload must contain a 'text' field."
    if not isinstance(payload["text"], str) or not payload["text"].strip():
        return False, "'text' must be a non-empty string."
    return True, ""


def _extract_text(payload: dict) -> str:
    """Return cleaned text from payload."""
    return re.sub(r"\s+", " ", payload["text"].strip())


# ---------------------------------------------------------------------------
# Public interface
# ---------------------------------------------------------------------------

def analyse_message(payload: dict[str, Any]) -> dict[str, Any]:
    """
    Run the full HumanTrace v0 detection pipeline on a message.

    Parameters
    ----------
    payload : dict
        Required: { "text": str }
        Optional: {
            "input_id": str,
            "channel": "sms" | "email" | "chat" | "other",
            "metadata": {
                "known_sender": bool,
                "has_link": bool,
                "has_phone": bool,
                "has_payment_request": bool,
                "sender_claimed_role": str,
            }
        }

    Returns
    -------
    dict
        Full structured detection result. See module docstring for schema.
    """
    # Validate
    valid, error = _validate_payload(payload)
    if not valid:
        return {
            "error": error,
            "engine_version": ENGINE_VERSION,
        }

    input_id  = payload.get("input_id", "unset")
    text      = _extract_text(payload)
    word_count = len(text.split())

    # ── Run all five detectors ────────────────────────────────────────────
    int_result   = detect_intent(text)
    trust_result = detect_trust_hijack(text)
    press_result = detect_pressure(text)
    dist_result  = detect_distortion(text)
    auth_result  = detect_authenticity_gap(text)

    # ── Fuse ──────────────────────────────────────────────────────────────
    scores = SignalScores(
        intent=int_result.score,
        trust=trust_result.score,
        pressure=press_result.score,
        distortion=dist_result.score,
        auth_gap=auth_result.score,
    )
    fusion = fuse(scores, text_word_count=word_count)

    # ── Collect all features and negative features ────────────────────────
    all_features = (
        int_result.features +
        trust_result.features +
        press_result.features +
        dist_result.features +
        auth_result.features
    )
    all_negatives = list(set(
        int_result.negative_feature_hits +
        trust_result.negative_feature_hits +
        press_result.negative_feature_hits +
        dist_result.negative_feature_hits +
        auth_result.negative_feature_hits
    ))

    # ── Render explanation ────────────────────────────────────────────────
    summary = _render_summary(
        fusion.risk_label, fusion.dominant_family,
        fusion.composite_patterns, scores
    )
    plain_reasoning = _render_plain_reasoning(
        fusion.risk_label, scores, all_features, all_negatives
    )

    # ── Assemble result ───────────────────────────────────────────────────
    return {
        "input_id": input_id,
        "engine_version": ENGINE_VERSION,
        "overall_risk": {
            "label": fusion.risk_label,
            "score": fusion.overall_score,
            "confidence": fusion.confidence,
        },
        "signal_scores": {
            "intent":     scores.intent,
            "trust":      scores.trust,
            "pressure":   scores.pressure,
            "distortion": scores.distortion,
            "auth_gap":   scores.auth_gap,
        },
        "dominant_family": fusion.dominant_family,
        "composite_patterns": [
            {
                "pattern_id":  cp.pattern_id,
                "label":       cp.label,
                "description": cp.description,
            }
            for cp in fusion.composite_patterns
        ],
        "detected_features": [
            {
                "signal_id":         f.signal_id,
                "label":             f.label,
                "evidence":          f.evidence,
                "score_contribution": f.score_contribution,
            }
            for f in sorted(all_features, key=lambda x: x.score_contribution, reverse=True)
        ],
        "negative_features": all_negatives,
        "score_breakdown": fusion.score_breakdown,
        "summary": summary,
        "plain_reasoning": plain_reasoning,
    }