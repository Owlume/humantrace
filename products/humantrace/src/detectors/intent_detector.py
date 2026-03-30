"""
HumanTrace — Intent Extraction Detector
Signal family: INT
Canonical IDs: HT.INT.EXT.01 through HT.INT.EXT.05

Detects whether a message's reasoning is steered toward a harmful
or extractive outcome: money, credentials, personal data, blind
compliance, or secrecy.

Build step: 1
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


class IntentDetectionResult(NamedTuple):
    score: float                        # 0.0 – 1.0, clamped
    features: list[DetectedFeature]
    negative_feature_hits: list[str]    # legitimate markers that reduce score


# ---------------------------------------------------------------------------
# Lexicons — all lowercase for case-insensitive matching
# ---------------------------------------------------------------------------

# HT.INT.EXT.01 — money / payment extraction
EXTRACTION_MONEY = [
    "pay", "payment", "transfer funds", "send funds", "wire transfer",
    "bank transfer", "direct debit", "gift card", "itunes card", "google play card",
    "crypto", "bitcoin", "ethereum", "send money", "deposit", "remittance",
    "send payment", "make a payment", "process payment", "immediate payment",
]

# HT.INT.EXT.02 — credential / identity extraction
EXTRACTION_CREDENTIAL = [
    "verify your identity", "verify your account", "confirm your identity",
    "login", "log in", "sign in", "sign-in", "reset password",
    "update your password", "confirm account details", "validate your account",
    "confirm your details", "your account details", "enter your pin",
    "security code", "one-time code", "otp", "authentication code",
    "confirm your email", "verify your email",
]

# HT.INT.EXT.03 — personal data extraction
EXTRACTION_PERSONAL_DATA = [
    "provide your details", "send your details", "confirm your address",
    "date of birth", "tax file number", "tfn", "medicare number",
    "social security", "passport number", "driver's licence", "drivers license",
    "bank account number", "bsb", "routing number", "account number",
    "mother's maiden name", "security question",
]

# HT.INT.EXT.04 — compliance without verification
EXTRACTION_COMPLIANCE = [
    "click here to resolve", "click the link below", "click here immediately",
    "follow this link", "use the link below", "tap here", "open the link",
    "do this now", "do this immediately", "act immediately",
    "respond immediately", "reply immediately", "must respond",
    "call this number immediately", "call us now",
]

# HT.INT.EXT.05 — secrecy / isolation
EXTRACTION_SECRECY = [
    "keep this confidential", "do not tell", "don't tell", "don't discuss",
    "do not discuss", "keep between us", "between you and me", "only you",
    "private matter", "discreet", "do not share", "don't share",
    "keep this private", "confidential matter", "tell no one",
    "do not contact", "avoid contacting",
]

# Negative features — markers of legitimate communication that reduce score
NEGATIVE_MARKERS = [
    ("verification pathway", [
        "you can verify", "confirm by calling", "visit your branch",
        "check our official website", "independently confirm",
        "contact us directly at", "our official number is",
    ]),
    ("multiple options", [
        "alternatively", "you may also", "another option",
        "you can choose", "if you prefer", "or you can",
    ]),
    ("process explanation", [
        "as part of our standard process", "our normal procedure",
        "as we do for all customers", "our policy requires",
        "in line with regulations",
    ]),
]

# Score contribution per signal (base values before capping)
SCORE_WEIGHTS = {
    "HT.INT.EXT.01": 0.22,   # money extraction — strong
    "HT.INT.EXT.02": 0.20,   # credential extraction — strong
    "HT.INT.EXT.03": 0.18,   # personal data — strong
    "HT.INT.EXT.04": 0.15,   # compliance without verification — moderate
    "HT.INT.EXT.05": 0.22,   # secrecy — strong (isolation is a key fraud signal)
}

NEGATIVE_REDUCTION = 0.08   # reduction per distinct negative feature hit


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _normalise(text: str) -> str:
    """Lowercase and collapse whitespace for matching."""
    return re.sub(r"\s+", " ", text.lower().strip())


def _find_hits(text_norm: str, lexicon: list[str]) -> list[str]:
    """Return all lexicon phrases found in the normalised text."""
    return [phrase for phrase in lexicon if phrase in text_norm]


def _best_evidence(hits: list[str], text_norm: str, window: int = 60) -> str:
    """
    Return the shortest excerpt from the original text that contains
    the strongest (longest) matching phrase, giving the analyst context.
    """
    if not hits:
        return ""
    anchor = max(hits, key=len)
    idx = text_norm.find(anchor)
    start = max(0, idx - 15)
    end = min(len(text_norm), idx + len(anchor) + window)
    excerpt = text_norm[start:end].strip()
    return f"...{excerpt}..." if start > 0 else f"{excerpt}..."


# ---------------------------------------------------------------------------
# Public interface
# ---------------------------------------------------------------------------

def detect_intent(text: str) -> IntentDetectionResult:
    """
    Analyse a message for intent extraction signals.

    Parameters
    ----------
    text : str
        Raw message text. May be multi-sentence.

    Returns
    -------
    IntentDetectionResult
        score        — 0.0–1.0 float, clamped
        features     — list of DetectedFeature (one per triggered signal ID)
        negative_feature_hits — list of legitimate marker labels that reduced score
    """
    text_norm = _normalise(text)
    features: list[DetectedFeature] = []
    negative_hits: list[str] = []
    raw_score = 0.0

    # ── HT.INT.EXT.01 — money extraction ──────────────────────────────────
    hits_01 = _find_hits(text_norm, EXTRACTION_MONEY)
    if hits_01:
        contribution = SCORE_WEIGHTS["HT.INT.EXT.01"]
        features.append(DetectedFeature(
            signal_id="HT.INT.EXT.01",
            label="Direct money or payment extraction",
            evidence=_best_evidence(hits_01, text_norm),
            score_contribution=contribution,
        ))
        raw_score += contribution

    # ── HT.INT.EXT.02 — credential extraction ─────────────────────────────
    hits_02 = _find_hits(text_norm, EXTRACTION_CREDENTIAL)
    if hits_02:
        contribution = SCORE_WEIGHTS["HT.INT.EXT.02"]
        features.append(DetectedFeature(
            signal_id="HT.INT.EXT.02",
            label="Credential or identity extraction",
            evidence=_best_evidence(hits_02, text_norm),
            score_contribution=contribution,
        ))
        raw_score += contribution

    # ── HT.INT.EXT.03 — personal data extraction ──────────────────────────
    hits_03 = _find_hits(text_norm, EXTRACTION_PERSONAL_DATA)
    if hits_03:
        contribution = SCORE_WEIGHTS["HT.INT.EXT.03"]
        features.append(DetectedFeature(
            signal_id="HT.INT.EXT.03",
            label="Personal data extraction",
            evidence=_best_evidence(hits_03, text_norm),
            score_contribution=contribution,
        ))
        raw_score += contribution

    # ── HT.INT.EXT.04 — compliance without verification ───────────────────
    hits_04 = _find_hits(text_norm, EXTRACTION_COMPLIANCE)
    if hits_04:
        contribution = SCORE_WEIGHTS["HT.INT.EXT.04"]
        features.append(DetectedFeature(
            signal_id="HT.INT.EXT.04",
            label="Compliance without verification request",
            evidence=_best_evidence(hits_04, text_norm),
            score_contribution=contribution,
        ))
        raw_score += contribution

    # ── HT.INT.EXT.05 — secrecy / isolation ──────────────────────────────
    hits_05 = _find_hits(text_norm, EXTRACTION_SECRECY)
    if hits_05:
        contribution = SCORE_WEIGHTS["HT.INT.EXT.05"]
        features.append(DetectedFeature(
            signal_id="HT.INT.EXT.05",
            label="Secrecy or isolation request",
            evidence=_best_evidence(hits_05, text_norm),
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

    return IntentDetectionResult(
        score=score,
        features=features,
        negative_feature_hits=negative_hits,
    )