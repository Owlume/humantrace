"""
HumanTrace — Risk Fusion Layer
File: risk_fuser.py

Takes the five detector scores and produces a single overall risk
score with label, confidence, and composite pattern matches.

Design decisions made from actual detector output analysis
(Step 6 pre-build calibration, 2026-03-30):

  Problem observed: naive weighted average bunches all fraud cases
  between 0.19–0.29 regardless of how strongly individual families
  fire. A TRUST score of 0.88 (ATO impersonation) should dominate
  the verdict. A PRESS score of 0.74 (urgency scam) should dominate.
  The naive average dilutes these.

  Solution: peak signal amplification.
  When any single family scores above a dominance threshold (0.65),
  that signal is given amplified weight. The amplification pulls the
  overall score toward the peak signal rather than averaging it away.

  Interaction boosts: applied when two or more families co-fire
  above their individual thresholds. These are additive boosts on
  top of the weighted base.

  Composite patterns: named pattern matches that apply a labelled
  boost and appear in output for analyst explanation.

  Confidence: separate from score. Low confidence when only texture
  signals (AUTH) are present, or when the message is very short
  with weak signals. High confidence when multiple families agree
  and evidence is explicit.

Build step: 6
"""

from dataclasses import dataclass, field


# ---------------------------------------------------------------------------
# Types
# ---------------------------------------------------------------------------

@dataclass
class SignalScores:
    intent: float       # HT.INT.*
    trust: float        # HT.TRUST.*
    pressure: float     # HT.PRESS.*
    distortion: float   # HT.DIST.*
    auth_gap: float     # HT.AUTH.*  (capped at 0.40 by detector)


@dataclass
class CompositePatternMatch:
    pattern_id: str
    label: str
    boost_applied: float
    description: str


@dataclass
class FusionResult:
    overall_score: float                            # 0.0–1.0, clamped
    risk_label: str                                 # low / medium / high
    confidence: float                               # 0.0–1.0
    signal_scores: SignalScores
    dominant_family: str | None                     # family that drove verdict
    composite_patterns: list[CompositePatternMatch] # named patterns matched
    score_breakdown: dict                           # for audit trail


# ---------------------------------------------------------------------------
# Fusion constants
# ---------------------------------------------------------------------------

# Base weights (from signal_registry.json)
BASE_WEIGHTS = {
    "intent":      0.30,
    "trust":       0.22,
    "pressure":    0.22,
    "distortion":  0.16,
    "auth_gap":    0.10,
}

# Dominance threshold: when a single family exceeds this,
# it receives amplified weight in the final calculation
DOMINANCE_THRESHOLD = 0.60
DOMINANCE_AMPLIFICATION = 0.20     # added to base weight of dominant family
                                    # redistributed proportionally from others

# Interaction boost thresholds and values
# Applied additively when two+ families co-fire above these levels
INTERACTION_BOOSTS = [
    {
        "id": "IB.INT_PRESS",
        "condition": lambda s: s.intent > 0.45 and s.pressure > 0.45,
        "boost": 0.08,
        "description": "Intent extraction and pressure co-firing",
    },
    {
        "id": "IB.TRUST_PRESS",
        "condition": lambda s: s.trust > 0.40 and s.pressure > 0.35,
        "boost": 0.07,
        "description": "Trust hijack and urgency pressure co-firing",
    },
    {
        "id": "IB.INT_TRUST",
        "condition": lambda s: s.intent > 0.40 and s.trust > 0.40,
        "boost": 0.06,
        "description": "Intent extraction and trust hijack co-firing",
    },
    {
        "id": "IB.THREE_FAMILY",
        "condition": lambda s: sum(
            1 for v in [s.intent, s.trust, s.pressure, s.distortion]
            if v > 0.30
        ) >= 3,
        "boost": 0.06,
        "description": "Three or more primary families firing above threshold",
    },
    {
        "id": "IB.DIST_PRESS",
        "condition": lambda s: s.distortion > 0.30 and s.pressure > 0.35,
        "boost": 0.05,
        "description": "Reasoning distortion combined with pressure",
    },
]

# Composite pattern definitions
# Thresholds recalibrated from actual detector output analysis
COMPOSITE_PATTERNS = [
    {
        "id": "CP.AI.FRAUD",
        "label": "AI Fraud Signature",
        "condition": lambda s: (
            s.auth_gap > 0.20 and
            s.pressure > 0.35 and
            s.intent > 0.40
        ),
        "boost": 0.08,
        "description": (
            "High authenticity gap combined with urgency pressure and "
            "extraction intent — consistent with AI-assisted fraud generation."
        ),
    },
    {
        "id": "CP.HUMAN.MANIP",
        "label": "Human Manipulator",
        "condition": lambda s: (
            s.trust > 0.25 and        # recalibrated from 0.55 — actual outputs show 0.20–0.34
            s.intent > 0.15 and       # secrecy alone is sufficient
            s.pressure > 0.15         # urgency or option narrowing present
        ),
        "boost": 0.07,
        "description": (
            "Trust hijack with authority framing and pressure signals — "
            "consistent with skilled human social engineering."
        ),
    },
    {
        "id": "CP.INST.MALICE",
        "label": "Institutional Malice",
        "condition": lambda s: (
            s.distortion > 0.25 and
            s.intent > 0.30 and
            s.trust > 0.25
        ),
        "boost": 0.07,
        "description": (
            "Reasoning distortion combined with extraction intent and "
            "trust hijack — consistent with system-driven unethical behaviour."
        ),
    },
]

# Risk label thresholds
# Calibrated against actual detector output distribution (Step 6, 2026-03-30).
# Fraud cases cluster 0.19–0.42 after boosts; legitimate cases < 0.10.
THRESHOLD_HIGH   = 0.35
THRESHOLD_MEDIUM = 0.18
THRESHOLD_LOW    = 0.00

# Dominance override: if any single primary family exceeds this,
# verdict is forced HIGH regardless of weighted total.
DOMINANCE_OVERRIDE = 0.75

# AUTH-only penalty: if AUTH is the only family firing, cap score at MEDIUM
AUTH_ONLY_CAP = 0.45


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _apply_dominance(scores: SignalScores) -> dict:
    """
    If one primary family (INT, TRUST, PRESS, DIST) dominates,
    amplify its weight and reduce others proportionally.
    Returns adjusted weight dict.
    """
    weights = dict(BASE_WEIGHTS)
    primary = {
        "intent": scores.intent,
        "trust": scores.trust,
        "pressure": scores.pressure,
        "distortion": scores.distortion,
    }

    dominant = max(primary, key=primary.get)
    dominant_score = primary[dominant]

    if dominant_score < DOMINANCE_THRESHOLD:
        return weights  # no dominance — use base weights

    # Add amplification to dominant family
    weights[dominant] += DOMINANCE_AMPLIFICATION

    # Redistribute reduction across other primary families proportionally
    others = [k for k in primary if k != dominant]
    reduction_each = DOMINANCE_AMPLIFICATION / len(others)
    for k in others:
        weights[k] = max(0.0, weights[k] - reduction_each)

    return weights


def _compute_base_score(scores: SignalScores, weights: dict) -> float:
    return (
        weights["intent"]     * scores.intent +
        weights["trust"]      * scores.trust +
        weights["pressure"]   * scores.pressure +
        weights["distortion"] * scores.distortion +
        weights["auth_gap"]   * scores.auth_gap
    )


def _apply_interaction_boosts(scores: SignalScores) -> tuple[float, list[str]]:
    """Returns (total_boost, list_of_boost_ids_applied)."""
    total = 0.0
    applied = []
    for rule in INTERACTION_BOOSTS:
        if rule["condition"](scores):
            total += rule["boost"]
            applied.append(rule["id"])
    return round(total, 3), applied


def _apply_composite_patterns(scores: SignalScores) -> list[CompositePatternMatch]:
    matched = []
    for pattern in COMPOSITE_PATTERNS:
        if pattern["condition"](scores):
            matched.append(CompositePatternMatch(
                pattern_id=pattern["id"],
                label=pattern["label"],
                boost_applied=pattern["boost"],
                description=pattern["description"],
            ))
    return matched


def _compute_confidence(
    scores: SignalScores,
    families_above_threshold: int,
    interaction_boosts_applied: list[str],
    composite_patterns: list[CompositePatternMatch],
    text_length: int,
) -> float:
    """
    Confidence is separate from risk score.
    High when: multiple families agree, evidence is explicit,
               composite patterns match.
    Low when: only AUTH fires, message is very short,
              signals are weak.
    """
    conf = 0.0

    # Family agreement
    conf += min(families_above_threshold * 0.18, 0.54)

    # Strong individual signals
    if max(scores.intent, scores.trust, scores.pressure) > 0.60:
        conf += 0.20

    # Interaction boosts signal agreement
    conf += len(interaction_boosts_applied) * 0.08

    # Composite pattern match
    conf += len(composite_patterns) * 0.10

    # Penalty: only AUTH firing
    primary_above = sum(
        1 for v in [scores.intent, scores.trust, scores.pressure, scores.distortion]
        if v > 0.15
    )
    if primary_above == 0 and scores.auth_gap > 0.10:
        conf -= 0.20

    # Penalty: very short message (harder to assess)
    if text_length < 30:
        conf -= 0.15

    return round(min(max(conf, 0.0), 1.0), 3)


def _risk_label(score: float, scores: "SignalScores | None" = None) -> str:
    # Dominance override: one primary family at extreme confidence = HIGH
    if scores is not None:
        primary_max = max(scores.intent, scores.trust, scores.pressure, scores.distortion)
        if primary_max >= DOMINANCE_OVERRIDE:
            return "high"
    if score >= THRESHOLD_HIGH:
        return "high"
    elif score >= THRESHOLD_MEDIUM:
        return "medium"
    return "low"


def _dominant_family(scores: SignalScores, weights: dict) -> str | None:
    primary = {
        "intent": scores.intent,
        "trust": scores.trust,
        "pressure": scores.pressure,
        "distortion": scores.distortion,
    }
    dominant = max(primary, key=primary.get)
    if primary[dominant] >= DOMINANCE_THRESHOLD:
        return dominant
    return None


# ---------------------------------------------------------------------------
# Public interface
# ---------------------------------------------------------------------------

def fuse(
    scores: SignalScores,
    text_word_count: int = 100,
) -> FusionResult:
    """
    Fuse five detector scores into a single risk verdict.

    Parameters
    ----------
    scores : SignalScores
        Raw scores from all five detectors.
    text_word_count : int
        Word count of the original message (for confidence calculation).

    Returns
    -------
    FusionResult
    """
    # Step 1: Dominance-adjusted weights
    weights = _apply_dominance(scores)

    # Step 2: Base weighted score
    base = _compute_base_score(scores, weights)

    # Step 3: Interaction boosts
    interaction_boost, boosts_applied = _apply_interaction_boosts(scores)

    # Step 4: Composite patterns
    composite_patterns = _apply_composite_patterns(scores)
    pattern_boost = sum(p.boost_applied for p in composite_patterns)

    # Step 5: Total score
    raw_total = base + interaction_boost + pattern_boost

    # Step 6: AUTH-only cap
    primary_firing = sum(
        1 for v in [scores.intent, scores.trust, scores.pressure, scores.distortion]
        if v > 0.15
    )
    if primary_firing == 0:
        raw_total = min(raw_total, AUTH_ONLY_CAP)

    # Step 7: Clamp
    overall_score = round(min(max(raw_total, 0.0), 1.0), 3)

    # Step 8: Label
    risk_label = _risk_label(overall_score, scores)

    # Step 9: Confidence
    families_above = sum(
        1 for v in [scores.intent, scores.trust, scores.pressure,
                    scores.distortion, scores.auth_gap]
        if v > 0.15
    )
    confidence = _compute_confidence(
        scores, families_above, boosts_applied, composite_patterns, text_word_count
    )

    # Step 10: Dominant family
    dominant = _dominant_family(scores, weights)

    # Score breakdown for audit trail
    breakdown = {
        "base_weighted_score": round(base, 3),
        "dominance_weights_applied": weights != BASE_WEIGHTS,
        "adjusted_weights": {k: round(v, 3) for k, v in weights.items()},
        "interaction_boost": interaction_boost,
        "interaction_boosts_applied": boosts_applied,
        "pattern_boost": round(pattern_boost, 3),
        "auth_only_cap_applied": primary_firing == 0,
        "raw_total_before_clamp": round(raw_total, 3),
    }

    return FusionResult(
        overall_score=overall_score,
        risk_label=risk_label,
        confidence=confidence,
        signal_scores=scores,
        dominant_family=dominant,
        composite_patterns=composite_patterns,
        score_breakdown=breakdown,
    )