"""
HumanTrace — Pressure / Urgency Detector
Signal family: PRESS
Canonical IDs: HT.PRESS.URG.01 through HT.PRESS.URG.04

Detects forced narrowing of decision space or time compression —
artificial urgency, threat of loss, false deadlines, and option
narrowing that funnel the recipient toward action before reflection.

Design note: This family has the highest raw signal weight in the
fusion layer (0.22, tied with TRUST) because urgency compression
is the most consistent structural feature of malicious synthetic
reasoning across fraud categories. However, urgency alone is not
sufficient for a high-risk verdict — legitimate communications
(genuine fraud alerts, time-sensitive service notices) also carry
urgency language. Negative features handle this distinction.

Partially implemented in existing L4 pattern_library. This detector
formalises and extends that logic with canonical signal IDs.

Build step: 3
Status: partial (formalised from L4)
"""

import re
from typing import NamedTuple


# ---------------------------------------------------------------------------
# Types
# ---------------------------------------------------------------------------

class DetectedFeature(NamedTuple):
    signal_id: str
    label: str
    evidence: str
    score_contribution: float


class PressureDetectionResult(NamedTuple):
    score: float
    features: list[DetectedFeature]
    negative_feature_hits: list[str]


# ---------------------------------------------------------------------------
# Lexicons
# ---------------------------------------------------------------------------

# HT.PRESS.URG.01 — urgency escalation
# Time-pressure language designed to suppress deliberation
URGENCY_ESCALATION = [
    "act now", "act immediately", "act today", "act urgently",
    "urgent", "urgently", "urgent action", "urgent action required",
    "action required", "action needed", "immediate action",
    "immediate attention", "immediate response",
    "immediately", "right now", "right away",
    "today only", "today is the last day",
    "within 24 hours", "within 48 hours", "within the hour",
    "within the next hour", "within minutes",
    "as soon as possible", "asap",
    "do not delay", "no time to waste", "time is running out",
    "time sensitive", "time-sensitive",
    "respond today", "reply today", "respond immediately",
    "reply immediately", "respond now", "reply now",
    "must be completed today", "must be done today",
    "must respond today", "must act today",
]

# HT.PRESS.URG.02 — threat of immediate loss
# Consequences framed as imminent and concrete
THREAT_OF_LOSS = [
    "account will be suspended", "account will be closed",
    "account will be terminated", "account will be deactivated",
    "account will be locked", "account has been locked",
    "account has been suspended", "access will be revoked",
    "access will be terminated", "access will be removed",
    "you will lose access", "you will lose your",
    "funds will be frozen", "funds will be held",
    "funds will be seized", "your funds are at risk",
    "will be reported to", "will be referred to",
    "will face legal action", "legal action will proceed",
    "legal action will be taken", "legal proceedings will",
    "will result in prosecution", "will result in penalty",
    "will result in a fine", "penalty will apply",
    "warrant will be issued", "arrest warrant",
    "services will be discontinued", "service will be terminated",
    "benefits will be cancelled", "payments will stop",
    "your claim will be", "your application will be rejected",
    "irreversible", "cannot be undone", "permanent",
]

# HT.PRESS.URG.03 — false deadline
# Specific time constraints that serve only to compress decision time
FALSE_DEADLINE_PATTERNS = [
    r"\bby\s+(midnight|tonight|end\s+of\s+day|eod|cob)\b",
    r"\bexpires?\s+(in|within)\s+\d+\s+(hour|minute|day)s?\b",
    r"\bexpires?\s+(today|tonight|now)\b",
    r"\bvalid\s+(for|until)\s+\d+\s+(hour|minute|day)s?\s+only\b",
    r"\b\d+\s*(hour|minute)s?\s+(left|remaining|only)\b",
    r"\blast\s+(chance|opportunity|day|notice)\b",
    r"\bdeadline\s*[:\-]?\s*(today|tonight|now|immediately)\b",
    r"\bmust\s+(be\s+)?(completed?|done|actioned?|respond(ed)?)\s+by\s+\w+\s*\d*",
    r"\bresponse\s+required\s+by\s+\w+",
    r"\bclose[sd]?\s+(tonight|today|at\s+midnight|in\s+\d+\s+hour)",
    r"\bwindow\s+(close[sd]?|expire[sd]?)\b",
    r"\bno\s+extension[s]?\s+will\b",
    r"\bfinal\s+(deadline|date|day|notice|warning)\b",
]

# HT.PRESS.URG.04 — option narrowing
# Language that eliminates alternatives and funnels toward one path
OPTION_NARROWING = [
    "the only way", "only way to resolve", "only option",
    "only option available", "no other option", "no other way",
    "no alternative", "there is no alternative",
    "you must use this link", "you must use the link",
    "only through this", "only via this",
    "must go through", "cannot be done any other way",
    "only accepted method", "only accepted form",
    "do not contact anyone else", "do not use other channels",
    "do not use normal channels", "bypass normal",
    "this is the only channel", "must use this number",
    "must call this number", "only call this number",
    "do not call the number on your card",
    "do not visit the branch",
    "under no circumstances should you",
]

# Negative features — markers of legitimate urgency communication
NEGATIVE_MARKERS = [
    ("genuine time constraint with grounding", [
        "as per our earlier conversation",
        "as discussed in your application",
        "as outlined in your contract",
        "per the terms you agreed to",
        "as advised in your previous correspondence",
    ]),
    ("alternative resolution pathway", [
        "alternatively you can", "or you can contact",
        "you may also", "another option is",
        "you have several options", "you can choose to",
        "at your convenience", "when you are ready",
    ]),
    ("no-action safety statement", [
        "no action required if", "if you did not request",
        "disregard if", "ignore this if",
        "if this was not you", "if you believe this is an error",
        "you are not required to", "this is optional",
    ]),
    ("verifiable deadline grounding", [
        "as stated in your contract", "per your policy end date",
        "your annual renewal", "your subscription expires",
        "as per the court order dated", "per the agreement signed",
    ]),
]

SCORE_WEIGHTS = {
    "HT.PRESS.URG.01": 0.18,   # urgency escalation — strong
    "HT.PRESS.URG.02": 0.22,   # threat of loss — strongest
    "HT.PRESS.URG.03": 0.16,   # false deadline — moderate-strong
    "HT.PRESS.URG.04": 0.18,   # option narrowing — strong
}

NEGATIVE_REDUCTION = 0.08


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _normalise(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower().strip())


def _find_hits(text_norm: str, lexicon: list[str]) -> list[str]:
    return [phrase for phrase in lexicon if phrase in text_norm]


def _find_pattern_hits(text_norm: str, patterns: list[str]) -> list[str]:
    matched = []
    for pattern in patterns:
        m = re.search(pattern, text_norm)
        if m:
            matched.append(m.group(0))
    return matched


def _best_evidence(hits: list[str], text_norm: str, window: int = 60) -> str:
    if not hits:
        return ""
    anchor = max(hits, key=len)
    idx = text_norm.find(anchor)
    if idx == -1:
        return f"...{anchor}..."
    start = max(0, idx - 15)
    end = min(len(text_norm), idx + len(anchor) + window)
    excerpt = text_norm[start:end].strip()
    return f"...{excerpt}..." if start > 0 else f"{excerpt}..."


# ---------------------------------------------------------------------------
# Public interface
# ---------------------------------------------------------------------------

def detect_pressure(text: str) -> PressureDetectionResult:
    """
    Analyse a message for pressure and urgency signals.

    Parameters
    ----------
    text : str
        Raw message text.

    Returns
    -------
    PressureDetectionResult
        score                 — 0.0–1.0, clamped
        features              — list of DetectedFeature
        negative_feature_hits — legitimate urgency markers that reduced score
    """
    text_norm = _normalise(text)
    features: list[DetectedFeature] = []
    negative_hits: list[str] = []
    raw_score = 0.0

    # ── HT.PRESS.URG.01 — urgency escalation ──────────────────────────────
    hits_01 = _find_hits(text_norm, URGENCY_ESCALATION)
    if hits_01:
        contribution = SCORE_WEIGHTS["HT.PRESS.URG.01"]
        features.append(DetectedFeature(
            signal_id="HT.PRESS.URG.01",
            label="Urgency escalation",
            evidence=_best_evidence(hits_01, text_norm),
            score_contribution=contribution,
        ))
        raw_score += contribution

    # ── HT.PRESS.URG.02 — threat of immediate loss ────────────────────────
    hits_02 = _find_hits(text_norm, THREAT_OF_LOSS)
    if hits_02:
        contribution = SCORE_WEIGHTS["HT.PRESS.URG.02"]
        features.append(DetectedFeature(
            signal_id="HT.PRESS.URG.02",
            label="Threat of immediate loss",
            evidence=_best_evidence(hits_02, text_norm),
            score_contribution=contribution,
        ))
        raw_score += contribution

    # ── HT.PRESS.URG.03 — false deadline ──────────────────────────────────
    hits_03 = _find_pattern_hits(text_norm, FALSE_DEADLINE_PATTERNS)
    if hits_03:
        contribution = SCORE_WEIGHTS["HT.PRESS.URG.03"]
        features.append(DetectedFeature(
            signal_id="HT.PRESS.URG.03",
            label="False deadline",
            evidence=f"...{hits_03[0]}...",
            score_contribution=contribution,
        ))
        raw_score += contribution

    # ── HT.PRESS.URG.04 — option narrowing ────────────────────────────────
    hits_04 = _find_hits(text_norm, OPTION_NARROWING)
    if hits_04:
        contribution = SCORE_WEIGHTS["HT.PRESS.URG.04"]
        features.append(DetectedFeature(
            signal_id="HT.PRESS.URG.04",
            label="Option narrowing",
            evidence=_best_evidence(hits_04, text_norm),
            score_contribution=contribution,
        ))
        raw_score += contribution

    # ── Negative feature reduction ─────────────────────────────────────────
    for label, markers in NEGATIVE_MARKERS:
        if any(m in text_norm for m in markers):
            negative_hits.append(label)
            raw_score -= NEGATIVE_REDUCTION

    # ── Clamp ──────────────────────────────────────────────────────────────
    score = round(min(max(raw_score, 0.0), 1.0), 3)

    return PressureDetectionResult(
        score=score,
        features=features,
        negative_feature_hits=negative_hits,
    )