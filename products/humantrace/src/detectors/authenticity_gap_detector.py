"""
HumanTrace — Authenticity Gap Detector
Signal family: AUTH
Canonical IDs: HT.AUTH.GAP.01 through HT.AUTH.GAP.04

Detects absence of natural human cognitive texture — the friction,
uncertainty, and lived specificity that genuine human reasoning
carries in authentic communication contexts.

Architecture note:
  HT.AUTH.GAP.01, .02, .03 implement the same signal logic as
  humantrace_behavioural_signals.py (micro-variation, limbic leakage,
  investment asymmetry). When that module exists as a file in
  src/trace_signals/, replace the internal implementations below
  with an import and adapter call. The SignalLibraryResult interface
  contract is preserved.

  HT.AUTH.GAP.04 (low lived specificity) is new — not in the prior
  behavioural signals module.

Critical design constraint (from signal_registry.json):
  AUTH family CANNOT contribute more than 0.10 to the overall
  weighted score. It is a texture signal. It amplifies other signals
  but cannot drive a verdict independently.

  This cap is enforced in the fusion layer, but is also enforced
  here: the raw score returned by this detector is clamped at 0.40
  before weighting. With fusion weight 0.10, that produces a maximum
  contribution of 0.04 — well within the 0.10 ceiling.

Build step: 5
Status: exists (GAP.01–03) / new (GAP.04)
"""

import re
import math
from typing import NamedTuple


# ---------------------------------------------------------------------------
# Types
# ---------------------------------------------------------------------------

class DetectedFeature(NamedTuple):
    signal_id: str
    label: str
    evidence: str
    score_contribution: float


class AuthenticityGapResult(NamedTuple):
    score: float                        # 0.0–0.40, capped before fusion weighting
    features: list[DetectedFeature]
    negative_feature_hits: list[str]
    human_texture_score: float          # inverse: higher = more human-like
    synthetic_texture_score: float      # higher = more synthetic


# ---------------------------------------------------------------------------
# Signal implementation
# ---------------------------------------------------------------------------

# ── HT.AUTH.GAP.01 — Unnatural fluency (micro-variation) ─────────────────
#
# Human writing shows natural variation in sentence length, register
# shifts, and self-interruption. Synthetic text tends toward uniform
# sentence length and consistent register.
#
# Proxy measures:
#   - Sentence length variance (low variance = synthetic signal)
#   - Absence of hedging / self-correction phrases
#   - Absence of register shifts (e.g., sudden informality)

HEDGING_PHRASES = [
    "i think", "i believe", "i'm not sure", "i'm not certain",
    "maybe", "perhaps", "possibly", "might be", "could be",
    "i could be wrong", "not entirely sure", "roughly",
    "something like", "i'd guess", "as far as i know",
    "to my knowledge", "if i recall", "i may be mistaken",
    "i suppose", "i imagine", "i'd say",
]

SELF_CORRECTION_PHRASES = [
    "actually", "wait", "no —", "no,", "sorry —", "sorry,",
    "let me rephrase", "what i mean is", "to be clear",
    "or rather", "i mean", "that is to say",
]


def _sentence_length_variance(text: str) -> float:
    """
    Return coefficient of variation of sentence lengths.
    High CoV = natural human variation.
    Low CoV = suspiciously uniform = synthetic signal.
    """
    sentences = re.split(r'[.!?]+', text)
    lengths = [len(s.split()) for s in sentences if s.strip()]
    if len(lengths) < 3:
        return 1.0  # too short to measure — return neutral
    mean = sum(lengths) / len(lengths)
    if mean == 0:
        return 1.0
    variance = sum((l - mean) ** 2 for l in lengths) / len(lengths)
    return math.sqrt(variance) / mean  # coefficient of variation


def score_unnatural_fluency(text: str, text_norm: str) -> tuple[float, str]:
    """
    Returns (score_contribution, evidence_note).
    Score is higher when the text is suspiciously uniform and frictionless.
    """
    cov = _sentence_length_variance(text)
    has_hedging = any(p in text_norm for p in HEDGING_PHRASES)
    has_self_correction = any(p in text_norm for p in SELF_CORRECTION_PHRASES)

    score = 0.0
    notes = []

    # Low sentence length variation — synthetic signal
    if cov < 0.25:
        score += 0.12
        notes.append(f"uniform sentence length (CoV={cov:.2f})")

    # No hedging — synthetic signal (humans hedge when uncertain)
    if not has_hedging:
        score += 0.08
        notes.append("no hedging language")

    # No self-correction — synthetic signal
    if not has_self_correction:
        score += 0.05
        notes.append("no self-correction markers")

    evidence = "; ".join(notes) if notes else ""
    return round(min(score, 0.20), 3), evidence


# ── HT.AUTH.GAP.02 — Absence of bounded uncertainty (limbic leakage) ─────
#
# Genuine human communication, even in professional contexts, shows
# bounded uncertainty — the writer acknowledges limits of knowledge
# or expresses genuine emotional investment inconsistently (leaking).
# Synthetic text tends toward over-qualification or zero qualification,
# neither of which matches authentic human ambivalence.

ABSOLUTE_CERTAINTY_PHRASES = [
    "guaranteed", "guarantee", "100%", "absolutely certain",
    "there is no doubt", "without question", "undoubtedly",
    "definitively", "with certainty", "i can assure you",
    "rest assured", "there is no risk", "perfectly safe",
    "completely safe", "will definitely", "will certainly",
    "always works", "never fails",
]

EMOTIONAL_LEAKAGE_PHRASES = [
    "honestly", "frankly", "to be honest", "if i'm honest",
    "between you and me", "i have to say", "i must admit",
    "i'll be straight with you", "look,", "look —",
    "here's the thing", "the truth is", "genuinely",
]


def score_bounded_uncertainty(text_norm: str) -> tuple[float, str]:
    """
    Returns (score_contribution, evidence_note).
    Fires when message shows zero bounded uncertainty AND
    high certainty framing — both together signal synthetic texture.
    """
    has_absolute = any(p in text_norm for p in ABSOLUTE_CERTAINTY_PHRASES)
    has_leakage = any(p in text_norm for p in EMOTIONAL_LEAKAGE_PHRASES)
    has_hedging = any(p in text_norm for p in HEDGING_PHRASES)

    score = 0.0
    notes = []

    if has_absolute and not has_hedging:
        score += 0.12
        notes.append("absolute certainty without hedging")

    if not has_leakage and not has_hedging:
        score += 0.05
        notes.append("no emotional leakage or bounded uncertainty")

    evidence = "; ".join(notes) if notes else ""
    return round(min(score, 0.15), 3), evidence


# ── HT.AUTH.GAP.03 — Investment asymmetry ────────────────────────────────
#
# Genuine human communication shows proportionality between the
# emotional weight or urgency expressed and the actual size of the
# ask or the relationship context. Malicious synthetic text
# characteristically over-invests emotionally relative to the ask,
# or under-invests in ways that feel detached.

HIGH_STAKES_CLAIM_PHRASES = [
    "your entire account", "all your funds", "your life savings",
    "everything you have", "your whole", "total loss",
    "catastrophic", "devastating", "irreversible damage",
    "cannot be recovered", "permanently lost",
    "most important", "most urgent", "most critical",
    "extremely urgent", "extremely important", "extremely serious",
]

LOW_RELATIONSHIP_MARKERS = [
    # Messages claiming high stakes but showing no relational history
    "dear customer", "dear account holder", "dear valued customer",
    "dear sir", "dear madam", "dear sir/madam",
    "to whom it may concern", "dear user", "dear member",
]


def score_investment_asymmetry(text: str, text_norm: str) -> tuple[float, str]:
    """
    Returns (score_contribution, evidence_note).
    Fires when high-stakes claims appear alongside low-relationship
    generic salutations — a structural mismatch.
    """
    has_high_stakes = any(p in text_norm for p in HIGH_STAKES_CLAIM_PHRASES)
    has_low_relationship = any(p in text_norm for p in LOW_RELATIONSHIP_MARKERS)

    # Also check: very short message with very high urgency density
    word_count = len(text.split())
    urgency_density = sum(
        1 for p in ["urgent", "immediately", "now", "critical", "severe"]
        if p in text_norm
    ) / max(word_count, 1)

    score = 0.0
    notes = []

    if has_high_stakes and has_low_relationship:
        score += 0.12
        notes.append("high-stakes claim with generic salutation")

    if urgency_density > 0.04 and word_count < 80:
        score += 0.08
        notes.append(f"high urgency density in short message ({word_count} words)")

    evidence = "; ".join(notes) if notes else ""
    return round(min(score, 0.15), 3), evidence


# ── HT.AUTH.GAP.04 — Low lived specificity ───────────────────────────────
#
# Genuine human communication in high-stakes contexts (fraud alerts,
# loan applications, compliance notices) contains concrete personal
# detail: named individuals, specific amounts, specific dates,
# specific account references that match the recipient's actual
# situation. Synthetic text tends toward generic placeholders.

SPECIFIC_DETAIL_PATTERNS = [
    r"\$[\d,]+(\.\d{2})?",          # dollar amounts
    r"\b\d{1,2}/\d{1,2}/\d{2,4}\b", # dates
    r"\b\d{4}\s?\d{4}\s?\d{4}\b",   # account-like numbers
    r"\baccount\s+ending\s+in\s+\d+", # partial account references
    r"\btransaction\s+(of|for)\s+\$", # specific transaction reference
    r"\bon\s+\d{1,2}\s+\w+\s+\d{4}", # "on 12 March 2026"
    r"\breference\s+number\s+[A-Z0-9\-]{6,}", # specific reference numbers
]

GENERIC_PLACEHOLDER_PHRASES = [
    "your account", "your details", "your information",
    "your funds", "your data", "your records",
    "recent activity", "unusual activity", "suspicious activity",
    "a transaction", "certain transactions",
    "your recent", "a recent",
]


def score_lived_specificity(text: str, text_norm: str) -> tuple[float, str]:
    """
    Returns (score_contribution, evidence_note).
    Fires when message is high-stakes but contains only generic
    placeholders with no concrete verifiable specifics.
    """
    specific_hits = [
        p for p in SPECIFIC_DETAIL_PATTERNS
        if re.search(p, text_norm)
    ]
    generic_hits = [p for p in GENERIC_PLACEHOLDER_PHRASES if p in text_norm]

    # High-stakes signals (borrowed from PRESS/TRUST families for context)
    is_high_stakes_context = any(p in text_norm for p in [
        "suspended", "frozen", "legal", "fraud", "urgent", "immediately",
        "account", "funds", "verify", "confirm",
    ])

    score = 0.0
    notes = []

    if is_high_stakes_context and not specific_hits and len(generic_hits) >= 2:
        score += 0.10
        notes.append(f"high-stakes context with only generic placeholders ({len(generic_hits)} found, 0 specifics)")

    evidence = "; ".join(notes) if notes else ""
    return round(min(score, 0.10), 3), evidence


# ---------------------------------------------------------------------------
# Negative features
# ---------------------------------------------------------------------------

NEGATIVE_MARKERS = [
    ("concrete personal detail present", [
        r"\$[\d,]+",
        r"\d{1,2}/\d{1,2}/\d{2,4}",
        r"account ending in \d+",
        r"reference number [A-Z0-9]{4,}",
    ]),
    ("genuine hedging or uncertainty", HEDGING_PHRASES),
    ("emotional leakage markers", EMOTIONAL_LEAKAGE_PHRASES),
]

AUTH_GAP_SCORE_CAP = 0.40   # raw cap before fusion weighting


# ---------------------------------------------------------------------------
# Public interface
# ---------------------------------------------------------------------------

def detect_authenticity_gap(text: str) -> AuthenticityGapResult:
    """
    Analyse a message for authenticity gap signals.

    Parameters
    ----------
    text : str
        Raw message text.

    Returns
    -------
    AuthenticityGapResult
        score                  — 0.0–0.40, capped (contributes max 0.04
                                 to overall after fusion weight of 0.10)
        features               — list of DetectedFeature
        negative_feature_hits  — human texture markers present
        human_texture_score    — 0.0–1.0, higher = more human-like texture
        synthetic_texture_score — 0.0–1.0, higher = more synthetic texture
    """
    text_norm = _normalise(text)
    features: list[DetectedFeature] = []
    negative_hits: list[str] = []
    raw_score = 0.0
    human_signals = 0
    synthetic_signals = 0

    # ── HT.AUTH.GAP.01 — Unnatural fluency ───────────────────────────────
    s01, e01 = score_unnatural_fluency(text, text_norm)
    if s01 > 0:
        features.append(DetectedFeature(
            signal_id="HT.AUTH.GAP.01",
            label="Unnatural fluency",
            evidence=e01 or "uniform linguistic texture detected",
            score_contribution=s01,
        ))
        raw_score += s01
        synthetic_signals += 1
    else:
        human_signals += 1

    # ── HT.AUTH.GAP.02 — Absence of bounded uncertainty ──────────────────
    s02, e02 = score_bounded_uncertainty(text_norm)
    if s02 > 0:
        features.append(DetectedFeature(
            signal_id="HT.AUTH.GAP.02",
            label="Absence of bounded uncertainty",
            evidence=e02 or "no hedging or uncertainty markers",
            score_contribution=s02,
        ))
        raw_score += s02
        synthetic_signals += 1
    else:
        human_signals += 1

    # ── HT.AUTH.GAP.03 — Investment asymmetry ────────────────────────────
    s03, e03 = score_investment_asymmetry(text, text_norm)
    if s03 > 0:
        features.append(DetectedFeature(
            signal_id="HT.AUTH.GAP.03",
            label="Investment asymmetry",
            evidence=e03 or "emotional weight disproportionate to ask",
            score_contribution=s03,
        ))
        raw_score += s03
        synthetic_signals += 1
    else:
        human_signals += 1

    # ── HT.AUTH.GAP.04 — Low lived specificity ───────────────────────────
    s04, e04 = score_lived_specificity(text, text_norm)
    if s04 > 0:
        features.append(DetectedFeature(
            signal_id="HT.AUTH.GAP.04",
            label="Low lived specificity",
            evidence=e04 or "high-stakes context lacks concrete detail",
            score_contribution=s04,
        ))
        raw_score += s04
        synthetic_signals += 1
    else:
        human_signals += 1

    # ── Negative features ────────────────────────────────────────────────
    for label, markers in NEGATIVE_MARKERS:
        if isinstance(markers[0], str) and not markers[0].startswith(r'\b') and not markers[0].startswith(r'\$') and not markers[0].startswith(r'\d'):
            # Plain string list
            if any(m in text_norm for m in markers):
                negative_hits.append(label)
                human_signals += 1
                raw_score -= 0.05
        else:
            # Regex pattern list
            if any(re.search(m, text_norm) for m in markers):
                negative_hits.append(label)
                human_signals += 1
                raw_score -= 0.05

    # ── Scores ────────────────────────────────────────────────────────────
    total_signals = human_signals + synthetic_signals
    human_texture = round(human_signals / max(total_signals, 1), 3)
    synthetic_texture = round(synthetic_signals / max(total_signals, 1), 3)

    score = round(min(max(raw_score, 0.0), AUTH_GAP_SCORE_CAP), 3)

    return AuthenticityGapResult(
        score=score,
        features=features,
        negative_feature_hits=negative_hits,
        human_texture_score=human_texture,
        synthetic_texture_score=synthetic_texture,
    )


def _normalise(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower().strip())