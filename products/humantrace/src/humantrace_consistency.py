"""
humantrace_consistency.py
Cross-document consistency scoring for HumanTrace Institutional.

Takes a batch of documents (raw text + metadata) from a single loan application
and returns a ConsistencyReport: five dimension scores, an overall score,
flagged anomalies, and a structured record ready for DilemmaNet logging.

Design contract:
- Input:  list of DocumentInput (text, doc_type, doc_id)
- Output: ConsistencyReport (scores, flags, overall, log_record)
- No external dependencies beyond stdlib + existing project imports
- Output kind: SIGNAL only — no recommendations, no decisions
"""

from __future__ import annotations

import re
import math
import json
import hashlib
import itertools
from dataclasses import dataclass, field, asdict
from typing import Optional
from collections import Counter
from datetime import datetime, timezone


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------

@dataclass
class DocumentInput:
    """One document from a loan application batch."""
    doc_id: str                     # e.g. "personal_statement", "employment_letter"
    doc_type: str                   # "applicant_authored" | "employer_authored" | "third_party"
    text: str
    label: Optional[str] = None     # human-readable name for UI display


@dataclass
class DimensionScore:
    name: str
    score: float                    # 0.0 (no consistency) — 1.0 (full consistency)
    weight: float
    signals: list[str] = field(default_factory=list)   # what drove this score
    anomalies: list[str] = field(default_factory=list) # what was flagged


@dataclass
class ConsistencyReport:
    application_id: str
    timestamp: str
    document_ids: list[str]
    dimensions: list[DimensionScore]
    overall_score: float            # weighted average of dimension scores
    overall_signal: str             # "GREEN" | "YELLOW" | "RED"
    cross_doc_flags: list[str]      # high-level anomaly statements for analyst
    log_record: dict                # ready for DilemmaNet / audit trail


# ---------------------------------------------------------------------------
# Signal thresholds
# ---------------------------------------------------------------------------

GREEN_THRESHOLD  = 0.70
YELLOW_THRESHOLD = 0.40
# below 0.40 = RED


def _signal_from_score(score: float) -> str:
    if score >= GREEN_THRESHOLD:
        return "GREEN"
    if score >= YELLOW_THRESHOLD:
        return "YELLOW"
    return "RED"


# ---------------------------------------------------------------------------
# Text utilities
# ---------------------------------------------------------------------------

def _tokenize(text: str) -> list[str]:
    """Lowercase word tokens, letters only."""
    return re.findall(r"[a-z]+", text.lower())


def _sentences(text: str) -> list[str]:
    """Rough sentence split."""
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if len(s.strip()) > 10]


def _extract_years(text: str) -> list[int]:
    """Extract four-digit years plausibly in a loan context (1950–2030)."""
    return [int(y) for y in re.findall(r"\b(19[5-9]\d|20[0-2]\d)\b", text)]


def _extract_named_entities(text: str) -> set[str]:
    """
    Lightweight named entity extraction: capitalised multi-word sequences
    that are not sentence-initial. Imperfect but dependency-free.
    """
    entities: set[str] = set()
    # Match sequences of Title Case words (2+ words) mid-sentence
    for match in re.finditer(r"(?<=[a-z,;]\s)([A-Z][a-z]+(?:\s[A-Z][a-z]+)+)", text):
        entities.add(match.group(1).strip())
    return entities


def _vocabulary_profile(tokens: list[str]) -> dict:
    """Type-token ratio, average word length, function-word ratio."""
    if not tokens:
        return {"ttr": 0.0, "avg_len": 0.0, "func_ratio": 0.0}
    FUNCTION_WORDS = {
        "the","a","an","and","or","but","in","on","at","to","for","of","with",
        "by","from","as","is","was","are","were","be","been","being","have",
        "has","had","do","does","did","will","would","could","should","may",
        "might","shall","not","no","so","if","that","this","these","those",
        "it","its","we","our","they","their","he","she","his","her","i","my",
    }
    ttr = len(set(tokens)) / len(tokens)
    avg_len = sum(len(t) for t in tokens) / len(tokens)
    func_ratio = sum(1 for t in tokens if t in FUNCTION_WORDS) / len(tokens)
    return {"ttr": round(ttr, 4), "avg_len": round(avg_len, 4), "func_ratio": round(func_ratio, 4)}


def _cosine_similarity(vec_a: Counter, vec_b: Counter) -> float:
    """Cosine similarity between two term-frequency counters."""
    if not vec_a or not vec_b:
        return 0.0
    common = set(vec_a) & set(vec_b)
    dot = sum(vec_a[t] * vec_b[t] for t in common)
    mag_a = math.sqrt(sum(v ** 2 for v in vec_a.values()))
    mag_b = math.sqrt(sum(v ** 2 for v in vec_b.values()))
    if mag_a == 0 or mag_b == 0:
        return 0.0
    return round(dot / (mag_a * mag_b), 4)


# ---------------------------------------------------------------------------
# Dimension 1: Authorial voice consistency
#
# Measures whether applicant-authored documents share a consistent writing
# voice. Compares vocabulary profiles and lexical similarity across docs
# of the same authorship type.
# ---------------------------------------------------------------------------

def _score_authorial_voice(docs: list[DocumentInput]) -> DimensionScore:
    applicant_docs = [d for d in docs if d.doc_type == "applicant_authored"]
    signals: list[str] = []
    anomalies: list[str] = []

    if len(applicant_docs) < 2:
        # Only one applicant-authored doc — cannot compare, neutral score
        return DimensionScore(
            name="authorial_voice",
            score=0.5,
            weight=0.25,
            signals=["Only one applicant-authored document — voice comparison unavailable"],
        )

    profiles = []
    tf_vectors = []
    for d in applicant_docs:
        tokens = _tokenize(d.text)
        profiles.append((d.doc_id, _vocabulary_profile(tokens)))
        tf_vectors.append((d.doc_id, Counter(tokens)))

    # Pairwise cosine similarities across applicant docs
    pair_scores = []
    for (id_a, vec_a), (id_b, vec_b) in itertools.combinations(tf_vectors, 2):
        sim = _cosine_similarity(vec_a, vec_b)
        pair_scores.append((id_a, id_b, sim))
        signals.append(f"Lexical similarity {id_a} / {id_b}: {sim:.2f}")

    # Vocabulary profile divergence
    ttr_values = [p["ttr"] for _, p in profiles]
    ttr_spread = max(ttr_values) - min(ttr_values) if len(ttr_values) > 1 else 0.0
    if ttr_spread > 0.15:
        anomalies.append(
            f"Type-token ratio spread {ttr_spread:.2f} across applicant docs — "
            "vocabulary richness inconsistent with single author"
        )

    avg_sim = sum(s for _, _, s in pair_scores) / len(pair_scores) if pair_scores else 0.5

    # Penalise for high TTR spread
    penalty = min(ttr_spread * 1.5, 0.3)
    score = max(0.0, min(1.0, avg_sim - penalty))

    return DimensionScore(
        name="authorial_voice",
        score=round(score, 3),
        weight=0.25,
        signals=signals,
        anomalies=anomalies,
    )


# ---------------------------------------------------------------------------
# Dimension 2: Vocabulary register consistency
#
# Measures whether the formality register is stable across all documents
# that should share a register (applicant-authored). Sudden register shifts
# (very formal → very casual, or vice versa) flag synthetic assembly.
# ---------------------------------------------------------------------------

# Formal markers (Latinate / bureaucratic vocabulary)
_FORMAL_MARKERS = {
    "pursuant","herein","aforementioned","notwithstanding","endeavour","endeavor",
    "facilitate","utilise","utilize","implement","demonstrate","comprehensive",
    "substantial","regarding","therefore","furthermore","moreover","nevertheless",
    "subsequent","prior","approximately","initial","primary","commence","require",
    "ensure","maintain","provide","assist","conduct","obtain","establish",
    "professional","opportunity","experience","position","employment","responsible",
}

# Informal markers
_INFORMAL_MARKERS = {
    "basically","stuff","things","really","very","just","kind","sort","bit",
    "got","get","gonna","wanna","lots","plenty","great","awesome","cool",
    "yeah","yep","ok","okay","sure","pretty","super","totally","honestly",
    "literally","actually","like","so","well","anyway","though","right",
}


def _register_score(tokens: list[str]) -> float:
    """0.0 = very informal, 1.0 = very formal."""
    if not tokens:
        return 0.5
    formal   = sum(1 for t in tokens if t in _FORMAL_MARKERS)
    informal = sum(1 for t in tokens if t in _INFORMAL_MARKERS)
    total = formal + informal
    if total == 0:
        return 0.5
    return round(formal / total, 4)


def _score_vocabulary_register(docs: list[DocumentInput]) -> DimensionScore:
    applicant_docs = [d for d in docs if d.doc_type == "applicant_authored"]
    signals: list[str] = []
    anomalies: list[str] = []

    if len(applicant_docs) < 2:
        return DimensionScore(
            name="vocabulary_register",
            score=0.5,
            weight=0.20,
            signals=["Only one applicant-authored document — register comparison unavailable"],
        )

    reg_scores = []
    for d in applicant_docs:
        tokens = _tokenize(d.text)
        rs = _register_score(tokens)
        reg_scores.append((d.doc_id, rs))
        label = "formal" if rs > 0.6 else ("informal" if rs < 0.4 else "neutral")
        signals.append(f"{d.doc_id} register: {rs:.2f} ({label})")

    values = [rs for _, rs in reg_scores]
    spread = max(values) - min(values)

    if spread > 0.30:
        anomalies.append(
            f"Register spread {spread:.2f} across applicant documents — "
            "formality level inconsistent with single author"
        )

    # Score: low spread = high consistency
    score = max(0.0, 1.0 - (spread * 2.5))

    return DimensionScore(
        name="vocabulary_register",
        score=round(score, 3),
        weight=0.20,
        signals=signals,
        anomalies=anomalies,
    )


# ---------------------------------------------------------------------------
# Dimension 3: Timeline coherence
#
# Extracts year references from all documents and checks for internal
# contradictions — e.g. employment letter claims a start year that
# predates the personal statement's claimed graduation year.
# ---------------------------------------------------------------------------

def _score_timeline_coherence(docs: list[DocumentInput]) -> DimensionScore:
    signals: list[str] = []
    anomalies: list[str] = []

    doc_years: dict[str, list[int]] = {}
    for d in docs:
        years = _extract_years(d.text)
        doc_years[d.doc_id] = years
        if years:
            signals.append(f"{d.doc_id} year references: {sorted(set(years))}")
        else:
            signals.append(f"{d.doc_id}: no year references found")

    all_years = [y for ys in doc_years.values() for y in ys]
    if not all_years:
        return DimensionScore(
            name="timeline_coherence",
            score=0.5,
            weight=0.20,
            signals=signals,
            anomalies=["No year references found in any document — timeline cannot be evaluated"],
        )

    # Flag impossible timeline spans (>50 years across a single application)
    year_range = max(all_years) - min(all_years)
    if year_range > 50:
        anomalies.append(
            f"Year span {min(all_years)}–{max(all_years)} ({year_range} years) "
            "is implausible for a single loan applicant's history"
        )

    # Check docs that should agree on key epochs: applicant + employer
    applicant_years = set(
        y for d in docs if d.doc_type == "applicant_authored"
        for y in doc_years.get(d.doc_id, [])
    )
    employer_years = set(
        y for d in docs if d.doc_type == "employer_authored"
        for y in doc_years.get(d.doc_id, [])
    )

    overlap_penalty = 0.0
    if applicant_years and employer_years:
        overlap = applicant_years & employer_years
        if not overlap:
            anomalies.append(
                "No shared year references between applicant and employer documents — "
                "employment timeline may be fabricated"
            )
            overlap_penalty = 0.35
        else:
            signals.append(f"Shared year references across applicant/employer: {sorted(overlap)}")

    # Score: penalise anomalies
    base = 0.85 if not anomalies else 0.85 - (len(anomalies) * 0.20)
    score = max(0.0, min(1.0, base - overlap_penalty))

    return DimensionScore(
        name="timeline_coherence",
        score=round(score, 3),
        weight=0.20,
        signals=signals,
        anomalies=anomalies,
    )


# ---------------------------------------------------------------------------
# Dimension 4: Named entity alignment
#
# Checks whether proper nouns (employer names, institutions, locations)
# are referenced consistently across documents. An employer named in the
# personal statement should appear in the employment letter too.
# ---------------------------------------------------------------------------

def _score_named_entity_alignment(docs: list[DocumentInput]) -> DimensionScore:
    signals: list[str] = []
    anomalies: list[str] = []

    doc_entities: dict[str, set[str]] = {}
    for d in docs:
        ents = _extract_named_entities(d.text)
        doc_entities[d.doc_id] = ents
        if ents:
            signals.append(f"{d.doc_id} entities: {sorted(ents)[:6]}")
        else:
            signals.append(f"{d.doc_id}: no named entities detected")

    all_entity_sets = [e for e in doc_entities.values() if e]
    if len(all_entity_sets) < 2:
        return DimensionScore(
            name="named_entity_alignment",
            score=0.5,
            weight=0.20,
            signals=signals,
            anomalies=["Insufficient named entities for cross-document comparison"],
        )

    # Pairwise Jaccard similarity between entity sets
    pair_scores = []
    for (id_a, ents_a), (id_b, ents_b) in itertools.combinations(doc_entities.items(), 2):
        if not ents_a or not ents_b:
            continue
        intersection = len(ents_a & ents_b)
        union = len(ents_a | ents_b)
        jaccard = intersection / union if union > 0 else 0.0
        pair_scores.append((id_a, id_b, jaccard))
        signals.append(f"Entity overlap {id_a} / {id_b}: {jaccard:.2f} Jaccard")
        if jaccard < 0.05 and ents_a and ents_b:
            anomalies.append(
                f"Near-zero entity overlap between {id_a} and {id_b} — "
                "documents may describe different applicants or contexts"
            )

    if not pair_scores:
        return DimensionScore(
            name="named_entity_alignment",
            score=0.5,
            weight=0.20,
            signals=signals,
            anomalies=anomalies,
        )

    avg_jaccard = sum(s for _, _, s in pair_scores) / len(pair_scores)
    # Jaccard for natural language docs is low by nature; scale 0–0.3 → 0–1.0
    scaled = min(1.0, avg_jaccard / 0.30)

    return DimensionScore(
        name="named_entity_alignment",
        score=round(scaled, 3),
        weight=0.20,
        signals=signals,
        anomalies=anomalies,
    )


# ---------------------------------------------------------------------------
# Dimension 5: Employment narrative coherence
#
# Specific to loan applications: checks that the employment claim in the
# personal statement aligns with the employer letter's claims. Looks for
# job title terms, industry vocabulary, and tenure markers.
# ---------------------------------------------------------------------------

_TENURE_PATTERNS = [
    r"\b(\d+)\s+year[s]?\b",
    r"\bsince\s+(19|20)\d{2}\b",
    r"\bfor\s+(?:over\s+)?(\d+)\s+year[s]?\b",
]

def _extract_tenure_claims(text: str) -> list[str]:
    claims = []
    for pat in _TENURE_PATTERNS:
        claims.extend(re.findall(pat, text.lower()))
    return claims


def _score_employment_narrative(docs: list[DocumentInput]) -> DimensionScore:
    signals: list[str] = []
    anomalies: list[str] = []

    applicant_docs = [d for d in docs if d.doc_type == "applicant_authored"]
    employer_docs  = [d for d in docs if d.doc_type == "employer_authored"]

    if not applicant_docs or not employer_docs:
        return DimensionScore(
            name="employment_narrative",
            score=0.5,
            weight=0.15,
            signals=["Missing applicant or employer document — employment narrative comparison unavailable"],
        )

    app_text = " ".join(d.text for d in applicant_docs).lower()
    emp_text = " ".join(d.text for d in employer_docs).lower()

    app_tokens = set(_tokenize(app_text))
    emp_tokens = set(_tokenize(emp_text))

    # Content word overlap (excluding function words) as proxy for narrative alignment
    FUNCTION_WORDS = {
        "the","a","an","and","or","but","in","on","at","to","for","of","with",
        "by","from","as","is","was","are","were","be","been","have","has","had",
        "do","does","did","will","would","could","should","not","it","that","this",
    }
    app_content = app_tokens - FUNCTION_WORDS
    emp_content = emp_tokens - FUNCTION_WORDS

    if app_content and emp_content:
        content_overlap = len(app_content & emp_content) / len(app_content | emp_content)
        signals.append(f"Content word overlap (applicant / employer): {content_overlap:.2f}")
    else:
        content_overlap = 0.0

    # Tenure claim comparison
    app_tenure = _extract_tenure_claims(app_text)
    emp_tenure = _extract_tenure_claims(emp_text)

    if app_tenure and emp_tenure:
        signals.append(f"Applicant tenure claims: {app_tenure}")
        signals.append(f"Employer tenure claims: {emp_tenure}")
        # If numeric tenure values differ significantly, flag it
        app_nums = [int(t) for t in app_tenure if isinstance(t, str) and t.isdigit()]
        emp_nums = [int(t) for t in emp_tenure if isinstance(t, str) and t.isdigit()]
        if app_nums and emp_nums:
            if abs(max(app_nums) - max(emp_nums)) > 2:
                anomalies.append(
                    f"Tenure claim mismatch: applicant states {max(app_nums)} years, "
                    f"employer states {max(emp_nums)} years"
                )
    elif app_tenure and not emp_tenure:
        anomalies.append("Applicant makes tenure claims that employer letter does not corroborate")
    elif emp_tenure and not app_tenure:
        signals.append("Employer letter includes tenure claims not referenced by applicant")

    # Score: weight content overlap heavily, penalise anomalies
    base = content_overlap
    penalty = len(anomalies) * 0.20
    score = max(0.0, min(1.0, base - penalty))

    return DimensionScore(
        name="employment_narrative",
        score=round(score, 3),
        weight=0.15,
        signals=signals,
        anomalies=anomalies,
    )


# ---------------------------------------------------------------------------
# Overall scorer
# ---------------------------------------------------------------------------

def score_consistency(
    application_id: str,
    documents: list[DocumentInput],
) -> ConsistencyReport:
    """
    Main entry point. Takes a batch of documents from one application,
    returns a ConsistencyReport.

    Usage:
        docs = [
            DocumentInput("ps_001", "applicant_authored", personal_statement_text, "Personal statement"),
            DocumentInput("el_001", "employer_authored",  employment_letter_text,  "Employment letter"),
            DocumentInput("bp_001", "applicant_authored", business_plan_text,      "Business plan"),
        ]
        report = score_consistency("APP-2026-03847", docs)
    """
    timestamp = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

    dimensions = [
        _score_authorial_voice(documents),
        _score_vocabulary_register(documents),
        _score_timeline_coherence(documents),
        _score_named_entity_alignment(documents),
        _score_employment_narrative(documents),
    ]

    # Weighted average
    total_weight = sum(d.weight for d in dimensions)
    overall = sum(d.score * d.weight for d in dimensions) / total_weight
    overall = round(overall, 3)
    overall_signal = _signal_from_score(overall)

    # Collect all anomalies as cross-doc flags
    cross_doc_flags = []
    for dim in dimensions:
        for anomaly in dim.anomalies:
            cross_doc_flags.append(f"[{dim.name}] {anomaly}")

    # Build audit/DilemmaNet log record
    log_record = {
        "event": "consistency_scan",
        "application_id": application_id,
        "timestamp": timestamp,
        "document_ids": [d.doc_id for d in documents],
        "overall_score": overall,
        "overall_signal": overall_signal,
        "dimensions": [
            {
                "name": dim.name,
                "score": dim.score,
                "weight": dim.weight,
                "anomaly_count": len(dim.anomalies),
            }
            for dim in dimensions
        ],
        "flag_count": len(cross_doc_flags),
        "output_kind": "SIGNAL",
        "governance": "Human judgment required. HumanTrace did not decide.",
    }

    return ConsistencyReport(
        application_id=application_id,
        timestamp=timestamp,
        document_ids=[d.doc_id for d in documents],
        dimensions=dimensions,
        overall_score=overall,
        overall_signal=overall_signal,
        cross_doc_flags=cross_doc_flags,
        log_record=log_record,
    )


# ---------------------------------------------------------------------------
# API surface — for humantrace_api.py
# ---------------------------------------------------------------------------

def consistency_report_to_dict(report: ConsistencyReport) -> dict:
    """Serialise ConsistencyReport to a JSON-safe dict for the API response."""
    return {
        "application_id": report.application_id,
        "timestamp": report.timestamp,
        "document_ids": report.document_ids,
        "overall_score": report.overall_score,
        "overall_signal": report.overall_signal,
        "cross_doc_flags": report.cross_doc_flags,
        "dimensions": [
            {
                "name": d.name,
                "score": d.score,
                "weight": d.weight,
                "signals": d.signals,
                "anomalies": d.anomalies,
            }
            for d in report.dimensions
        ],
        "log_record": report.log_record,
    }


# ---------------------------------------------------------------------------
# API endpoint additions — paste into humantrace_api.py
# ---------------------------------------------------------------------------

FASTAPI_ENDPOINT = '''
# ── Add to humantrace_api.py ──────────────────────────────────────────────

from src.humantrace_consistency import (
    DocumentInput, score_consistency, consistency_report_to_dict
)
from pydantic import BaseModel

class DocPayload(BaseModel):
    doc_id: str
    doc_type: str        # "applicant_authored" | "employer_authored" | "third_party"
    text: str
    label: str = ""

class BatchConsistencyRequest(BaseModel):
    application_id: str
    documents: list[DocPayload]

@app.post("/institutional/consistency")
async def institutional_consistency(req: BatchConsistencyRequest):
    docs = [
        DocumentInput(
            doc_id=d.doc_id,
            doc_type=d.doc_type,
            text=d.text,
            label=d.label,
        )
        for d in req.documents
    ]
    report = score_consistency(req.application_id, docs)
    return consistency_report_to_dict(report)
'''


# ---------------------------------------------------------------------------
# Quick smoke test — run directly to verify
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    PERSONAL_STATEMENT = """
    I have worked at Meridian Financial Services as a senior analyst for eight years,
    joining in 2016 after completing my MBA at the University of Melbourne in 2015.
    Throughout my tenure I have demonstrated a comprehensive understanding of
    credit risk assessment and portfolio management. I am seeking this loan to
    expand my consulting practice, Meridian Advisory Group, which I established
    in 2020 alongside my primary employment. The business has grown substantially
    and requires capital to hire additional staff and acquire specialist software.
    """

    EMPLOYMENT_LETTER = """
    To whom it may concern, this letter confirms that the individual named above
    has been employed with our organisation since January 2019 in the role of
    financial analyst. Their performance has been satisfactory and they remain
    a current employee on a full-time basis. Signed, Human Resources Department.
    """

    BUSINESS_PLAN = """
    Executive Summary: This document presents a comprehensive strategic framework
    for the proposed expansion of services. The methodology encompasses a
    multifaceted approach to market penetration utilising synergistic partnerships
    and leveraging existing intellectual capital to facilitate sustainable growth
    trajectories. Financial projections demonstrate substantial returns commencing
    in the initial operational period, approximately 2022 onward, notwithstanding
    prevailing market conditions. The organisation seeks to establish a primary
    position within the sector through systematic implementation of best practices.
    """

    docs = [
        DocumentInput("ps_001", "applicant_authored", PERSONAL_STATEMENT, "Personal statement"),
        DocumentInput("el_001", "employer_authored",  EMPLOYMENT_LETTER,  "Employment letter"),
        DocumentInput("bp_001", "applicant_authored", BUSINESS_PLAN,      "Business plan"),
    ]

    report = score_consistency("APP-SMOKE-TEST", docs)

    print(f"\n{'='*60}")
    print(f"APPLICATION: {report.application_id}")
    print(f"OVERALL:     {report.overall_signal}  {report.overall_score}")
    print(f"{'='*60}")
    for dim in report.dimensions:
        bar = "█" * int(dim.score * 20) + "░" * (20 - int(dim.score * 20))
        print(f"\n  {dim.name:<28}  {dim.score:.3f}  [{bar}]")
        for s in dim.signals:
            print(f"    · {s}")
        for a in dim.anomalies:
            print(f"    ⚠ {a}")

    print(f"\n{'─'*60}")
    print("CROSS-DOC FLAGS:")
    for flag in report.cross_doc_flags:
        print(f"  ⚑ {flag}")

    print(f"\n{'─'*60}")
    print("LOG RECORD (DilemmaNet):")
    print(json.dumps(report.log_record, indent=2))
    print(f"\n{'─'*60}")
    print("FASTAPI ENDPOINT (add to humantrace_api.py):")
    print(FASTAPI_ENDPOINT)
