"""
HumanTrace — Reasoning Distortion Detector
Signal family: DIST
Canonical IDs: HT.DIST.01 through HT.DIST.05

Detects manipulative logic patterns used to move a recipient
toward compliance by distorting their reasoning rather than
informing it.

Design notes:

  HT.DIST.01 (False dilemma) and HT.DIST.03 (Fear override) are
  lexicon-detectable with reasonable precision.

  HT.DIST.02 (Circular legitimacy) requires detecting self-referential
  authority claims — the message citing itself as proof of its own
  legitimacy. Detected via authority + self-referential phrase patterns.

  HT.DIST.04 (Post-hoc justification) is the hardest signal in this
  family. It describes a reasoning structure (conclusion first, evidence
  assembled afterward) that is difficult to detect deterministically in
  short messages. v0 uses proxies: conclusion-asserting openers followed
  by selective evidence phrases. Flagged as low-confidence.

  HT.DIST.05 (Contradiction masking) detects conflicting commitment
  pairs within a single message — e.g., "we will never contact you
  this way" followed by "please respond to this message". Detected
  via contradiction phrase pair patterns.

  This family carries weight 0.16 in the fusion layer — lower than
  INT and PRESS because distortion signals require more context to
  be reliable, and false positives here are more costly (legitimate
  assertive communication can superficially resemble distortion).

Build step: 4
Status: new
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


class DistortionDetectionResult(NamedTuple):
    score: float
    features: list[DetectedFeature]
    negative_feature_hits: list[str]


# ---------------------------------------------------------------------------
# Lexicons and patterns
# ---------------------------------------------------------------------------

# HT.DIST.01 — False dilemma
# Binary framing that eliminates valid alternatives
FALSE_DILEMMA = [
    "either you do this or", "either act now or",
    "either comply or", "either pay or",
    "either respond or", "either verify or",
    "your only options are", "your only option is",
    "you have two choices", "you have one choice",
    "there are only two options", "there is only one option",
    "if you don't act then", "if you don't act,",
    "if you fail to act", "if you do not act",
    "if you refuse", "if you choose not to",
    "comply or face", "pay or face",
    "respond or we will", "act or we will",
    "do this or lose", "do this or face",
    "no middle ground", "no other choice",
    "you must choose", "simple choice",
]

# HT.DIST.02 — Circular legitimacy
# Self-referential authority: the message cites itself as proof of legitimacy
CIRCULAR_LEGITIMACY = [
    "trust us because this is official",
    "this is legitimate because",
    "you can trust this message because",
    "this is genuine because",
    "this is real because",
    "this is not a scam because",
    "we are legitimate because",
    "this is authentic because",
    "proof of our legitimacy",
    "as evidence of our authority",
    "our credentials are",
    "you know this is real",
    "this proves we are",
]

# Pattern-based circular legitimacy: authority claim + self-citation
CIRCULAR_PATTERNS = [
    # Official X because we are X
    r"\bofficial\b.{0,40}\bbecause\b.{0,40}\bofficial\b",
    # Legitimate X because authorised / certified
    r"\blegitimate\b.{0,60}\b(authoris|certif|licens)\w+\b",
    # "We are [authority] and therefore you must"
    r"\bwe\s+are\s+(the\s+)?(official|authorised|certified)\b.{0,60}\b(therefore|so\s+you|which\s+means)\b",
    # Reference to unverifiable internal process as proof
    r"\b(our\s+records|our\s+system|our\s+database)\s+(show|confirm|indicate|verify)\b.{0,60}\b(therefore|so\s+you\s+must|and\s+you\s+must)\b",
]

# HT.DIST.03 — Fear override
# Emotional fear used to bypass rational evaluation
FEAR_OVERRIDE = [
    "the consequences will be severe",
    "serious consequences",
    "severe consequences",
    "severe penalty", "severe penalties",
    "you will be held responsible",
    "you will be held liable",
    "held personally responsible",
    "held personally liable",
    "you will be prosecuted",
    "criminal charges",
    "criminal prosecution",
    "criminal record",
    "you could go to jail", "you could be arrested",
    "warrant for your arrest",
    "your assets will be seized",
    "your wages will be garnished",
    "your credit will be affected",
    "your reputation will be",
    "this will affect your",
    "do not make the mistake of",
    "it would be a mistake to ignore",
    "ignoring this will result",
    "failure to respond will result",
    "failure to comply will result",
    "the situation will worsen",
    "this will only get worse",
    "delay will make this worse",
    "you have been warned",
]

# HT.DIST.04 — Post-hoc justification
# Conclusion-first structure: assertive claim followed by selectively
# assembled supporting phrases. Detected via proxy patterns.
POSTHOC_CONCLUSION_OPENERS = [
    r"^\s*(you\s+)?(owe|must|have\s+to|need\s+to|are\s+required\s+to)\b",
    r"^\s*this\s+is\s+(urgent|mandatory|required|compulsory|necessary)\b",
    r"^\s*you\s+are\s+(in\s+violation|non[- ]compliant|overdue|delinquent)\b",
    r"^\s*your\s+account\s+(is|has\s+been)\s+(suspended|flagged|compromised|locked)\b",
    r"^\s*(final|immediate|urgent)\s+(notice|action|warning)\b",
]

POSTHOC_EVIDENCE_PHRASES = [
    "as you can see", "as is clear", "as evidenced by",
    "the evidence shows", "this confirms", "this proves",
    "which proves", "which confirms", "which demonstrates",
    "our records show", "our system shows", "our investigation shows",
    "according to our records", "based on our records",
    "based on our investigation", "our analysis confirms",
]

# HT.DIST.05 — Contradiction masking
# Conflicting commitment pairs within the same message
# Detected as phrase-pair contradictions
CONTRADICTION_PAIRS = [
    (
        ["we will never contact you", "we never contact customers",
         "we will never ask you", "we never ask for"],
        ["please respond to this", "please reply to this",
         "respond to this email", "reply to this message",
         "please provide your", "please confirm your",
         "please send us"],
    ),
    (
        ["your security is our priority", "keeping you safe is",
         "we take your security seriously", "your protection is important"],
        ["do not tell anyone", "keep this confidential",
         "do not discuss", "do not contact", "bypass"],
    ),
    (
        ["no action is required", "you do not need to do anything",
         "you are not required to act"],
        ["act immediately", "act now", "respond immediately",
         "you must respond", "action required"],
    ),
    (
        ["this is not a scam", "this is not fraudulent",
         "this is a legitimate", "this is a genuine"],
        ["do not verify", "do not contact your bank",
         "do not call the number on", "bypass normal",
         "do not use normal channels"],
    ),
]

# Negative features — markers of legitimate assertive reasoning
NEGATIVE_MARKERS = [
    ("balanced evidence presentation", [
        "on the other hand", "however", "that said",
        "there are also", "alternatively", "another view",
        "you may disagree", "some people argue",
    ]),
    ("explicit acknowledgment of recipient autonomy", [
        "ultimately your decision", "the choice is yours",
        "you are free to", "you have the right to",
        "you may choose not to", "at your discretion",
        "if you prefer not to",
    ]),
    ("grounded consequence statement", [
        "as per the terms you agreed", "per your contract",
        "as outlined in the policy", "as stated in section",
        "as per the court order", "as per the legislation",
        "under the privacy act", "under the corporations act",
    ]),
]

SCORE_WEIGHTS = {
    "HT.DIST.01": 0.18,   # false dilemma — strong
    "HT.DIST.02": 0.16,   # circular legitimacy — moderate
    "HT.DIST.03": 0.18,   # fear override — strong
    "HT.DIST.04": 0.10,   # post-hoc justification — low confidence proxy
    "HT.DIST.05": 0.14,   # contradiction masking — moderate
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


def _detect_contradiction(text_norm: str) -> str | None:
    """
    Check contradiction pairs. Returns evidence string if found, else None.
    Both sides of a pair must appear in the same message for a hit.
    """
    for side_a, side_b in CONTRADICTION_PAIRS:
        a_hit = next((p for p in side_a if p in text_norm), None)
        b_hit = next((p for p in side_b if p in text_norm), None)
        if a_hit and b_hit:
            return f'..."{a_hit}" / "{b_hit}"...'
    return None


def _detect_posthoc(text_norm: str) -> str | None:
    """
    Proxy detection for post-hoc justification.
    Requires: conclusion-asserting opener AND at least one
    selectively assembled evidence phrase.
    Returns evidence string if found, else None.
    """
    opener_hit = any(
        re.search(p, text_norm) for p in POSTHOC_CONCLUSION_OPENERS
    )
    if not opener_hit:
        return None
    evidence_hit = next(
        (p for p in POSTHOC_EVIDENCE_PHRASES if p in text_norm), None
    )
    if evidence_hit:
        return f"...conclusion-first structure with: '{evidence_hit}'..."
    return None


# ---------------------------------------------------------------------------
# Public interface
# ---------------------------------------------------------------------------

def detect_distortion(text: str) -> DistortionDetectionResult:
    """
    Analyse a message for reasoning distortion signals.

    Parameters
    ----------
    text : str
        Raw message text.

    Returns
    -------
    DistortionDetectionResult
        score                 — 0.0–1.0, clamped
        features              — list of DetectedFeature
        negative_feature_hits — legitimate reasoning markers that reduced score
    """
    text_norm = _normalise(text)
    features: list[DetectedFeature] = []
    negative_hits: list[str] = []
    raw_score = 0.0

    # ── HT.DIST.01 — False dilemma ────────────────────────────────────────
    hits_01 = _find_hits(text_norm, FALSE_DILEMMA)
    if hits_01:
        contribution = SCORE_WEIGHTS["HT.DIST.01"]
        features.append(DetectedFeature(
            signal_id="HT.DIST.01",
            label="False dilemma",
            evidence=_best_evidence(hits_01, text_norm),
            score_contribution=contribution,
        ))
        raw_score += contribution

    # ── HT.DIST.02 — Circular legitimacy ──────────────────────────────────
    hits_02a = _find_hits(text_norm, CIRCULAR_LEGITIMACY)
    hits_02b = _find_pattern_hits(text_norm, CIRCULAR_PATTERNS)
    hits_02 = hits_02a + hits_02b
    if hits_02:
        contribution = SCORE_WEIGHTS["HT.DIST.02"]
        evidence = (
            _best_evidence(hits_02a, text_norm)
            if hits_02a
            else f"...{hits_02b[0]}..."
        )
        features.append(DetectedFeature(
            signal_id="HT.DIST.02",
            label="Circular legitimacy",
            evidence=evidence,
            score_contribution=contribution,
        ))
        raw_score += contribution

    # ── HT.DIST.03 — Fear override ────────────────────────────────────────
    hits_03 = _find_hits(text_norm, FEAR_OVERRIDE)
    if hits_03:
        contribution = SCORE_WEIGHTS["HT.DIST.03"]
        features.append(DetectedFeature(
            signal_id="HT.DIST.03",
            label="Fear override",
            evidence=_best_evidence(hits_03, text_norm),
            score_contribution=contribution,
        ))
        raw_score += contribution

    # ── HT.DIST.04 — Post-hoc justification (low confidence) ─────────────
    posthoc_evidence = _detect_posthoc(text_norm)
    if posthoc_evidence:
        contribution = SCORE_WEIGHTS["HT.DIST.04"]
        features.append(DetectedFeature(
            signal_id="HT.DIST.04",
            label="Post-hoc justification structure (proxy)",
            evidence=posthoc_evidence,
            score_contribution=contribution,
        ))
        raw_score += contribution

    # ── HT.DIST.05 — Contradiction masking ───────────────────────────────
    contradiction_evidence = _detect_contradiction(text_norm)
    if contradiction_evidence:
        contribution = SCORE_WEIGHTS["HT.DIST.05"]
        features.append(DetectedFeature(
            signal_id="HT.DIST.05",
            label="Contradiction masking",
            evidence=contradiction_evidence,
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

    return DistortionDetectionResult(
        score=score,
        features=features,
        negative_feature_hits=negative_hits,
    )