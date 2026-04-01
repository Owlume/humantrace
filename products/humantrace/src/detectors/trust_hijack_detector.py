"""
HumanTrace — Trust Hijack Detector
Signal family: TRUST
Canonical IDs: HT.TRUST.AUTH.01 through HT.TRUST.AUTH.05

Detects whether a message borrows legitimacy it has not earned —
through authority claims, institution impersonation, procedural
intimidation, synthetic empathy, or false legitimacy markers.

Key design constraint: trust hijack signals must be interpreted
against the presence or absence of grounding. A message that
invokes authority AND provides an independent verification pathway
is materially different from one that invokes authority alone.
The negative feature system handles this distinction.

Build step: 2
Status: updated — HT.TRUST.AUTH.02 legitimacy suppression added
"""

import re
from typing import NamedTuple


# ---------------------------------------------------------------------------
# Types (mirrors intent_detector.py for consistency)
# ---------------------------------------------------------------------------

class DetectedFeature(NamedTuple):
    signal_id: str
    label: str
    evidence: str
    score_contribution: float


class TrustDetectionResult(NamedTuple):
    score: float
    features: list[DetectedFeature]
    negative_feature_hits: list[str]


# ---------------------------------------------------------------------------
# Lexicons
# ---------------------------------------------------------------------------

# HT.TRUST.AUTH.01 — authority invocation without grounding
# Role claims that manufacture compliance pressure
AUTHORITY_INVOCATION = [
    "as your manager", "as your supervisor", "as your director",
    "as your ceo", "as your boss", "on behalf of management",
    "on behalf of the board", "on behalf of leadership",
    "this is official", "this is an official", "official communication",
    "official notification", "official request", "authorised by",
    "authorised request", "by order of", "under instruction from",
    "as directed by", "i am authorised", "acting on behalf of",
    "executive request", "urgent executive",
]

# HT.TRUST.AUTH.02 — institution impersonation
# Named institutions used to manufacture legitimacy
INSTITUTION_IMPERSONATION = [
    # Financial
    "bank fraud team", "fraud department", "fraud prevention team",
    "fraud investigation", "fraud protection",
    "commonwealth bank", "nab fraud", "anz fraud", "westpac fraud",
    "your bank", "your financial institution",
    # Government / regulatory
    "australian tax office", "ato", "australian taxation office",
    "asic", "apra", "centrelink", "services australia",
    "department of home affairs", "australian federal police",
    "afp cybercrime", "police cybercrime", "cybercrime unit",
    "federal police", "state police", "revenue office",
    "fair work", "medicare fraud",
    # Legal / compliance
    "legal department", "compliance department", "compliance team",
    "risk and compliance", "legal notice from", "law enforcement",
    "court order", "official government",
    # Generic impersonation patterns
    "it department", "it security", "system administrator",
    "help desk", "support team", "customer security team",
    "account security team", "security operations",
]

# HT.TRUST.AUTH.03 — procedural intimidation
# Legal/process language used to manufacture compliance without substance
PROCEDURAL_INTIMIDATION = [
    "final notice", "final legal notice", "final warning",
    "mandatory compliance", "mandatory action required",
    "failure to respond", "failure to act", "failure to comply",
    "failure to respond constitutes", "non-compliance will result",
    "legal proceedings", "legal action will", "legal action may",
    "will be reported", "reported to authorities",
    "subject to penalty", "subject to fine", "subject to prosecution",
    "warrant has been", "warrant will be", "summons",
    "immediate legal action", "without further notice",
    "last opportunity", "final opportunity",
]

# HT.TRUST.AUTH.04 — synthetic empathy framing
# Manufactured concern used to disarm scepticism before a request
SYNTHETIC_EMPATHY = [
    "we understand this is stressful", "we understand this may be concerning",
    "we understand this is unexpected", "we know this is difficult",
    "we know this may seem", "we appreciate your concern",
    "we are here to help you", "we are here to assist you",
    "we want to help you", "our priority is your",
    "your wellbeing is our priority", "your security is our priority",
    "your safety is our priority", "your protection is",
    "we care about your", "we value your",
    "we are reaching out because we care",
    "this is for your protection", "this is for your security",
    "we have detected suspicious", "we noticed unusual activity",
    "we are concerned about your account",
    "to protect you", "to keep you safe", "to safeguard your",
]

# HT.TRUST.AUTH.05 — false legitimacy markers
# Formatting and reference patterns that simulate official documentation
# These are pattern-based, not exact phrases
FALSE_LEGITIMACY_PATTERNS = [
    # Reference number patterns
    r"\bcase\s*(id|no|number|#|ref)[\s:]*\w+",
    r"\breference[\s:]+[a-z0-9\-]{4,}",
    r"\bref[\s:]+[a-z0-9\-]{4,}",
    r"\bticket[\s:#]+\w+",
    r"\bincident[\s:#]+\w+",
    r"\bclaim[\s:#]+\w+",
    r"\bfile[\s:#]+\w+",
    # Official notice patterns
    r"\bofficial\s+(notice|notification|alert|warning|request|communication)\b",
    r"\b(important|urgent|critical)\s+security\s+(alert|notice|notification)\b",
    r"\bdo\s+not\s+ignore\s+this",
    r"\byour\s+reference\s+number\s+is",
    # Verification code / OTP patterns that impersonate legitimate flows
    r"\byour\s+(security\s+)?(verification\s+)?code\s+is\s+\d+",
    r"\bone.time\s+(password|code|pin)\b",
]

# Grounding markers — presence of these reduces trust hijack score
# because they indicate the authority claim is accompanied by
# independently verifiable information
GROUNDING_MARKERS = [
    ("independent verification pathway", [
        "you can verify by calling", "call us on the number on the back",
        "visit your nearest branch", "check our official website",
        "independently verify", "confirm through your own",
        "contact us at our official", "our official number",
        "you can find us at", "look us up at",
    ]),
    ("balanced process explanation", [
        "as part of our standard", "our normal process",
        "as we do for all", "our policy is to",
        "you are not required to", "you can always decline",
        "this is optional", "at your discretion",
    ]),
    ("explicit opt-out", [
        "if you did not request", "if this was not you",
        "you can ignore this", "no action required if",
        "disregard if", "if you believe this is an error",
    ]),
]

# Legitimacy markers — presence of two or more suppresses HT.TRUST.AUTH.02
# by 65%. Genuine regulatory/institutional communications consistently carry
# multiple verifiable markers; synthetic impersonation typically lacks two
# or more of these because they require genuine underlying record access.
_LEGITIMACY_CHECKS = [
    # ABN/ACN with digit groups (e.g. "abn 51 824 753 556")
    (r"\b(abn|acn)\s+\d{2}\s+\d{3}\s+\d{3}\s+\d{3}", "ABN/ACN"),
    # Statutory section citation (e.g. "section 255-15", "s.120")
    (r"\b(section|s\.)\s*\d+[\-\.]\d+", "statutory section"),
    # Specific reference/account number with label
    (r"(reference|ref|account\s+number|loan\s+account|notice\s+number)\s*[:\-]\s*[a-z0-9\-]+",
     "specific reference number"),
    # Government postal address (e.g. "gpo box", "locked bag")
    (r"(gpo\s+box|locked\s+bag|po\s+box\s+\d)", "government postal address"),
    # Statutory deadline with specific day count
    (r"within\s+(7|14|21|28|30|60|90)\s+days\s+of\s+(the\s+)?(date|this)",
     "statutory deadline"),
]

# Score weights per signal
SCORE_WEIGHTS = {
    "HT.TRUST.AUTH.01": 0.20,   # authority invocation — strong
    "HT.TRUST.AUTH.02": 0.22,   # institution impersonation — strongest
    "HT.TRUST.AUTH.03": 0.20,   # procedural intimidation — strong
    "HT.TRUST.AUTH.04": 0.14,   # synthetic empathy — moderate
    "HT.TRUST.AUTH.05": 0.12,   # false legitimacy markers — moderate
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
    """Return pattern strings that matched (for evidence reporting)."""
    matched = []
    for pattern in patterns:
        m = re.search(pattern, text_norm)
        if m:
            matched.append(m.group(0))
    return matched


def _legitimacy_marker_count(text_norm: str) -> tuple[int, list[str]]:
    """
    Count how many legitimacy markers are present in text_norm.
    Returns (count, list_of_matched_marker_names).
    Used to suppress HT.TRUST.AUTH.02 when >= 2 markers are found.
    """
    count = 0
    matched_names = []
    for pattern, name in _LEGITIMACY_CHECKS:
        if re.search(pattern, text_norm):
            count += 1
            matched_names.append(name)
    return count, matched_names


def _best_evidence(hits: list[str], text_norm: str, window: int = 60) -> str:
    if not hits:
        return ""
    anchor = max(hits, key=len)
    idx = text_norm.find(anchor)
    if idx == -1:
        # Pattern match — anchor may be a regex match string, search again
        return f"...{anchor}..."
    start = max(0, idx - 15)
    end = min(len(text_norm), idx + len(anchor) + window)
    excerpt = text_norm[start:end].strip()
    return f"...{excerpt}..." if start > 0 else f"{excerpt}..."


# ---------------------------------------------------------------------------
# Public interface
# ---------------------------------------------------------------------------

def detect_trust_hijack(text: str) -> TrustDetectionResult:
    """
    Analyse a message for trust hijack signals.

    Parameters
    ----------
    text : str
        Raw message text.

    Returns
    -------
    TrustDetectionResult
        score                — 0.0–1.0, clamped
        features             — list of DetectedFeature
        negative_feature_hits — grounding markers that reduced score
    """
    text_norm = _normalise(text)
    features: list[DetectedFeature] = []
    negative_hits: list[str] = []
    raw_score = 0.0

    # ── HT.TRUST.AUTH.01 — authority invocation ───────────────────────────
    hits_01 = _find_hits(text_norm, AUTHORITY_INVOCATION)
    if hits_01:
        contribution = SCORE_WEIGHTS["HT.TRUST.AUTH.01"]
        features.append(DetectedFeature(
            signal_id="HT.TRUST.AUTH.01",
            label="Authority invocation without grounding",
            evidence=_best_evidence(hits_01, text_norm),
            score_contribution=contribution,
        ))
        raw_score += contribution

    # ── HT.TRUST.AUTH.02 — institution impersonation ──────────────────────
    hits_02 = _find_hits(text_norm, INSTITUTION_IMPERSONATION)
    if hits_02:
        contribution = SCORE_WEIGHTS["HT.TRUST.AUTH.02"]

        # Legitimacy suppression: when two or more verifiable institutional
        # markers are present, reduce the AUTH.02 contribution by 65%.
        # Genuine regulatory/institutional communications consistently carry
        # multiple verifiable markers (ABN, statutory citations, specific
        # reference numbers, government postal addresses, statutory deadlines).
        # Synthetic impersonation typically cannot replicate two or more of
        # these because they require access to genuine underlying records.
        lm_count, lm_names = _legitimacy_marker_count(text_norm)
        if lm_count >= 2:
            contribution = round(contribution * 0.35, 4)
            negative_hits.append(
                f"institutional legitimacy markers present "
                f"({lm_count}/5: {', '.join(lm_names)}) — "
                f"HT.TRUST.AUTH.02 suppressed to {contribution:.3f}"
            )

        features.append(DetectedFeature(
            signal_id="HT.TRUST.AUTH.02",
            label="Institution impersonation",
            evidence=_best_evidence(hits_02, text_norm),
            score_contribution=contribution,
        ))
        raw_score += contribution

    # ── HT.TRUST.AUTH.03 — procedural intimidation ────────────────────────
    hits_03 = _find_hits(text_norm, PROCEDURAL_INTIMIDATION)
    if hits_03:
        contribution = SCORE_WEIGHTS["HT.TRUST.AUTH.03"]
        features.append(DetectedFeature(
            signal_id="HT.TRUST.AUTH.03",
            label="Procedural intimidation",
            evidence=_best_evidence(hits_03, text_norm),
            score_contribution=contribution,
        ))
        raw_score += contribution

    # ── HT.TRUST.AUTH.04 — synthetic empathy ──────────────────────────────
    hits_04 = _find_hits(text_norm, SYNTHETIC_EMPATHY)
    if hits_04:
        contribution = SCORE_WEIGHTS["HT.TRUST.AUTH.04"]
        features.append(DetectedFeature(
            signal_id="HT.TRUST.AUTH.04",
            label="Synthetic empathy framing",
            evidence=_best_evidence(hits_04, text_norm),
            score_contribution=contribution,
        ))
        raw_score += contribution

    # ── HT.TRUST.AUTH.05 — false legitimacy markers ───────────────────────
    hits_05 = _find_pattern_hits(text_norm, FALSE_LEGITIMACY_PATTERNS)
    if hits_05:
        contribution = SCORE_WEIGHTS["HT.TRUST.AUTH.05"]
        features.append(DetectedFeature(
            signal_id="HT.TRUST.AUTH.05",
            label="False legitimacy markers",
            evidence=f"...{hits_05[0]}...",
            score_contribution=contribution,
        ))
        raw_score += contribution

    # ── Negative feature reduction ─────────────────────────────────────────
    for label, markers in GROUNDING_MARKERS:
        if any(m in text_norm for m in markers):
            negative_hits.append(label)
            raw_score -= NEGATIVE_REDUCTION

    # ── Clamp ──────────────────────────────────────────────────────────────
    score = round(min(max(raw_score, 0.0), 1.0), 3)

    return TrustDetectionResult(
        score=score,
        features=features,
        negative_feature_hits=negative_hits,
    )