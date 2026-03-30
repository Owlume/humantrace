"""
humantrace_bse_matcher.py
Cross-application BSE matching for HumanTrace Institutional.

Reads all fingerprint files from data/bse/, compares reasoning vectors
across applications, and returns a MatchReport: document-level matches,
application-level clusters, and a DilemmaNet log record.

Design contract:
- Input:  a target application_id + its documents (DocumentInput list)
- Output: MatchReport (document matches → application clusters → flags)
- Reads from data/bse/*.json (never writes — BSE writes handled by humantrace_bse.py)
- Output kind: SIGNAL only — no recommendations, no decisions
- Vector format agnostic: handles list[float] or dict[str, float]

File assumed per fingerprint in data/bse/:
{
  "fingerprint_id": "fp_abc123",
  "sender_id": "auto:brian@example.com" | "manual:BK" | "labelled:Brian K",
  "application_id": "APP-2026-03201",
  "doc_id": "ps_001",
  "doc_type": "applicant_authored",
  "label": "Personal statement",
  "reasoning_vector": [0.72, 0.08, 0.41, 0.04, ...]
                    OR {"conviction_cost": 0.08, "structural_coherence": 0.72, ...},
  "signal_history": [
      {"timestamp": "...", "verdict": "RED", "score": 0.19},
      ...
  ],
  "created_at": "2026-02-14T08:22:11Z",
  "opt_in": true
}
"""

from __future__ import annotations

import json
import math
import os
import re
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional, Union

from humantrace_consistency import DocumentInput, _tokenize


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

BSE_DIR = Path(__file__).parent.parent / "data" / "bse"

# Similarity thresholds
MATCH_THRESHOLD_HIGH   = 0.88   # strong match — likely same synthetic source
MATCH_THRESHOLD_MEDIUM = 0.75   # possible match — warrants analyst review
CLUSTER_MIN_SIZE       = 2      # minimum applications in a cluster to flag it


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------

@dataclass
class StoredFingerprint:
    fingerprint_id: str
    sender_id: str
    application_id: str
    doc_id: str
    doc_type: str
    label: str
    reasoning_vector: list[float]       # always normalised to list[float]
    signal_history: list[dict]
    created_at: str
    opt_in: bool


@dataclass
class DocumentMatch:
    """A single document from the target application matching a stored fingerprint."""
    target_doc_id: str
    target_doc_type: str
    matched_fingerprint_id: str
    matched_application_id: str
    matched_sender_id: str
    matched_doc_id: str
    matched_label: str
    matched_created_at: str
    similarity: float                   # cosine similarity 0.0–1.0
    strength: str                       # "HIGH" | "MEDIUM"


@dataclass
class ApplicationCluster:
    """A group of applications whose reasoning vectors are suspiciously similar."""
    cluster_id: str
    application_ids: list[str]          # includes target application
    anchor_doc_ids: list[str]           # the specific docs that triggered it
    max_similarity: float
    min_similarity: float
    signal: str                         # "RED" | "YELLOW"
    interpretation: str                 # plain-language flag for analyst


@dataclass
class MatchReport:
    target_application_id: str
    timestamp: str
    document_matches: list[DocumentMatch]
    application_clusters: list[ApplicationCluster]
    overall_signal: str                 # "RED" | "YELLOW" | "GREEN"
    cross_app_flags: list[str]
    log_record: dict


# ---------------------------------------------------------------------------
# Vector utilities
# ---------------------------------------------------------------------------

def _normalise_vector(raw: Union[list, dict]) -> list[float]:
    """
    Accept either list[float] or dict[str, float] and return list[float].
    Dict values are sorted by key for determinism.
    """
    if isinstance(raw, dict):
        return [float(v) for _, v in sorted(raw.items())]
    return [float(v) for v in raw]


def _cosine_similarity(vec_a: list[float], vec_b: list[float]) -> float:
    """Cosine similarity between two float vectors. Returns 0.0 if either is empty."""
    if not vec_a or not vec_b:
        return 0.0
    # Pad shorter vector with zeros so lengths match
    length = max(len(vec_a), len(vec_b))
    a = vec_a + [0.0] * (length - len(vec_a))
    b = vec_b + [0.0] * (length - len(vec_b))
    dot    = sum(x * y for x, y in zip(a, b))
    mag_a  = math.sqrt(sum(x ** 2 for x in a))
    mag_b  = math.sqrt(sum(x ** 2 for x in b))
    if mag_a == 0 or mag_b == 0:
        return 0.0
    return round(dot / (mag_a * mag_b), 4)


# ---------------------------------------------------------------------------
# Reasoning vector derivation
#
# When no pre-computed BSE vector exists for a target document (e.g. it
# has just been uploaded), we derive a vector from raw text using the same
# five dimensions as humantrace_consistency.py. This ensures the target's
# vector lives in the same space as stored fingerprints.
# ---------------------------------------------------------------------------

_FORMAL_MARKERS = {
    "pursuant","herein","aforementioned","notwithstanding","endeavour","endeavor",
    "facilitate","utilise","utilize","implement","demonstrate","comprehensive",
    "substantial","regarding","therefore","furthermore","moreover","nevertheless",
    "subsequent","prior","approximately","initial","primary","commence","require",
    "ensure","maintain","provide","assist","conduct","obtain","establish",
    "professional","opportunity","experience","position","employment","responsible",
}
_INFORMAL_MARKERS = {
    "basically","stuff","things","really","very","just","kind","sort","bit",
    "got","get","gonna","wanna","lots","plenty","great","awesome","cool",
    "yeah","yep","ok","okay","sure","pretty","super","totally","honestly",
    "literally","actually","like","so","well","anyway","though","right",
}
_FUNCTION_WORDS = {
    "the","a","an","and","or","but","in","on","at","to","for","of","with",
    "by","from","as","is","was","are","were","be","been","being","have",
    "has","had","do","does","did","will","would","could","should","may",
    "might","shall","not","no","so","if","that","this","these","those",
    "it","its","we","our","they","their","he","she","his","her","i","my",
}


def _derive_vector(text: str) -> list[float]:
    """
    Derive a 5-dimensional reasoning vector from raw text.
    Dimensions (matching consistency scorer):
      [0] structural_coherence   — sentence length consistency
      [1] conviction_cost        — personal stake markers / hedging
      [2] contextual_plausibility — named entity density
      [3] register_formality     — formal vs informal marker ratio
      [4] lexical_diversity      — type-token ratio
    """
    tokens = _tokenize(text)
    sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if len(s.strip()) > 10]

    # [0] Structural coherence: consistency of sentence lengths
    if len(sentences) >= 2:
        lengths = [len(s.split()) for s in sentences]
        mean_len = sum(lengths) / len(lengths)
        variance = sum((l - mean_len) ** 2 for l in lengths) / len(lengths)
        # Low variance = high coherence; normalise to 0–1
        structural = round(max(0.0, 1.0 - (variance / (mean_len ** 2 + 1))), 4)
    else:
        structural = 0.5

    # [1] Conviction cost: personal pronouns + hedging language
    PERSONAL_STAKES = {"i","my","me","mine","myself","we","our","personally","believe","feel","think","experience","decided","chose","built","started","founded"}
    HEDGING         = {"perhaps","possibly","might","may","could","uncertain","unsure","approximately","around","roughly","about","seems","appears"}
    personal = sum(1 for t in tokens if t in PERSONAL_STAKES)
    hedging  = sum(1 for t in tokens if t in HEDGING)
    conviction = round(min(1.0, (personal * 0.04) + (hedging * 0.08)), 4)

    # [2] Contextual plausibility: named entity density
    entities = re.findall(r"(?<=[a-z,;]\s)([A-Z][a-z]+(?:\s[A-Z][a-z]+)+)", text)
    entity_density = round(min(1.0, len(entities) / max(1, len(sentences)) * 0.5), 4)

    # [3] Register formality
    formal   = sum(1 for t in tokens if t in _FORMAL_MARKERS)
    informal = sum(1 for t in tokens if t in _INFORMAL_MARKERS)
    total = formal + informal
    formality = round(formal / total, 4) if total > 0 else 0.5

    # [4] Lexical diversity (type-token ratio)
    content_tokens = [t for t in tokens if t not in _FUNCTION_WORDS and len(t) > 2]
    ttr = round(len(set(content_tokens)) / max(1, len(content_tokens)), 4)

    return [structural, conviction, entity_density, formality, ttr]


# ---------------------------------------------------------------------------
# BSE fingerprint loader
# ---------------------------------------------------------------------------

def _load_fingerprints(bse_dir: Path) -> list[StoredFingerprint]:
    """Load all opt-in fingerprint files from the BSE directory."""
    fingerprints = []
    if not bse_dir.exists():
        return fingerprints

    for fp_path in bse_dir.glob("*.json"):
        try:
            with open(fp_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            if not data.get("opt_in", False):
                continue
            raw_vector = data.get("reasoning_vector", [])
            if not raw_vector:
                continue
            fingerprints.append(StoredFingerprint(
                fingerprint_id = data.get("fingerprint_id", fp_path.stem),
                sender_id      = data.get("sender_id", "unknown"),
                application_id = data.get("application_id", "unknown"),
                doc_id         = data.get("doc_id", "unknown"),
                doc_type       = data.get("doc_type", "unknown"),
                label          = data.get("label", ""),
                reasoning_vector = _normalise_vector(raw_vector),
                signal_history = data.get("signal_history", []),
                created_at     = data.get("created_at", ""),
                opt_in         = True,
            ))
        except (json.JSONDecodeError, KeyError):
            continue  # skip malformed files silently

    return fingerprints


# ---------------------------------------------------------------------------
# Cluster ID generation
# ---------------------------------------------------------------------------

def _cluster_id(application_ids: list[str]) -> str:
    """Deterministic cluster ID from sorted application IDs."""
    key = "|".join(sorted(application_ids))
    import hashlib
    return "CLU-" + hashlib.sha1(key.encode()).hexdigest()[:8].upper()


# ---------------------------------------------------------------------------
# Core matcher
# ---------------------------------------------------------------------------

def match_across_applications(
    target_application_id: str,
    target_documents: list[DocumentInput],
    bse_dir: Path = BSE_DIR,
    target_vectors: Optional[dict[str, list[float]]] = None,
) -> MatchReport:
    """
    Main entry point.

    Compares reasoning vectors of target documents against all stored BSE
    fingerprints (excluding those belonging to the target application itself),
    then groups matches into application-level clusters.

    Args:
        target_application_id:  e.g. "APP-2026-03847"
        target_documents:       list of DocumentInput (same format as consistency scorer)
        bse_dir:                path to data/bse/ directory
        target_vectors:         optional pre-computed vectors keyed by doc_id.
                                If absent, vectors are derived from raw text.

    Returns:
        MatchReport
    """
    timestamp = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

    # Build vectors for target documents
    if target_vectors is None:
        target_vectors = {}
    computed_vectors: dict[str, list[float]] = {}
    for doc in target_documents:
        if doc.doc_id in target_vectors:
            computed_vectors[doc.doc_id] = _normalise_vector(target_vectors[doc.doc_id])
        else:
            computed_vectors[doc.doc_id] = _derive_vector(doc.text)

    # Load stored fingerprints (excluding this application)
    all_fingerprints = _load_fingerprints(bse_dir)
    external_fingerprints = [
        fp for fp in all_fingerprints
        if fp.application_id != target_application_id
    ]

    # ── Document-level matching ──────────────────────────────────────────
    document_matches: list[DocumentMatch] = []

    for doc in target_documents:
        target_vec = computed_vectors[doc.doc_id]
        for fp in external_fingerprints:
            sim = _cosine_similarity(target_vec, fp.reasoning_vector)
            if sim >= MATCH_THRESHOLD_MEDIUM:
                strength = "HIGH" if sim >= MATCH_THRESHOLD_HIGH else "MEDIUM"
                document_matches.append(DocumentMatch(
                    target_doc_id         = doc.doc_id,
                    target_doc_type       = doc.doc_type,
                    matched_fingerprint_id = fp.fingerprint_id,
                    matched_application_id = fp.application_id,
                    matched_sender_id     = fp.sender_id,
                    matched_doc_id        = fp.doc_id,
                    matched_label         = fp.label or fp.doc_id,
                    matched_created_at    = fp.created_at,
                    similarity            = sim,
                    strength              = strength,
                ))

    # Sort by similarity descending
    document_matches.sort(key=lambda m: m.similarity, reverse=True)

    # ── Application-level clustering ─────────────────────────────────────
    # Group document matches by matched application_id
    app_match_groups: dict[str, list[DocumentMatch]] = {}
    for match in document_matches:
        app_id = match.matched_application_id
        app_match_groups.setdefault(app_id, []).append(match)

    application_clusters: list[ApplicationCluster] = []
    for matched_app_id, matches in app_match_groups.items():
        sims = [m.similarity for m in matches]
        max_sim = max(sims)
        min_sim = min(sims)
        cluster_signal = "RED" if max_sim >= MATCH_THRESHOLD_HIGH else "YELLOW"

        # Interpretation text
        high_matches = [m for m in matches if m.strength == "HIGH"]
        if high_matches:
            doc_list = ", ".join(set(m.target_doc_id for m in high_matches))
            interpretation = (
                f"Reasoning vector from {doc_list} in {target_application_id} "
                f"matches {matched_app_id} at {max_sim:.2f} similarity — "
                "consistent with a common synthetic source across distinct applicant identities."
            )
        else:
            interpretation = (
                f"Moderate vector similarity ({max_sim:.2f}) between "
                f"{target_application_id} and {matched_app_id} — warrants analyst review."
            )

        cluster = ApplicationCluster(
            cluster_id       = _cluster_id([target_application_id, matched_app_id]),
            application_ids  = [target_application_id, matched_app_id],
            anchor_doc_ids   = list(set(m.target_doc_id for m in matches)),
            max_similarity   = max_sim,
            min_similarity   = min_sim,
            signal           = cluster_signal,
            interpretation   = interpretation,
        )
        application_clusters.append(cluster)

    # Sort clusters by max similarity descending
    application_clusters.sort(key=lambda c: c.max_similarity, reverse=True)

    # ── Overall signal ───────────────────────────────────────────────────
    high_clusters = [c for c in application_clusters if c.signal == "RED"]
    if high_clusters:
        overall_signal = "RED"
    elif application_clusters:
        overall_signal = "YELLOW"
    else:
        overall_signal = "GREEN"

    # ── Cross-app flags (plain language for analyst UI) ──────────────────
    cross_app_flags: list[str] = []
    for cluster in application_clusters:
        cross_app_flags.append(
            f"[{cluster.signal}] {cluster.interpretation}"
        )
    if not cross_app_flags:
        cross_app_flags.append(
            "No significant reasoning vector matches found across stored applications."
        )

    # ── DilemmaNet log record ────────────────────────────────────────────
    log_record = {
        "event": "bse_cross_application_match",
        "target_application_id": target_application_id,
        "timestamp": timestamp,
        "target_doc_ids": [d.doc_id for d in target_documents],
        "fingerprints_compared": len(external_fingerprints),
        "document_matches_found": len(document_matches),
        "application_clusters_found": len(application_clusters),
        "high_similarity_clusters": len(high_clusters),
        "overall_signal": overall_signal,
        "clusters": [
            {
                "cluster_id": c.cluster_id,
                "application_ids": c.application_ids,
                "max_similarity": c.max_similarity,
                "signal": c.signal,
            }
            for c in application_clusters
        ],
        "output_kind": "SIGNAL",
        "governance": "Human judgment required. HumanTrace did not decide.",
    }

    return MatchReport(
        target_application_id = target_application_id,
        timestamp             = timestamp,
        document_matches      = document_matches,
        application_clusters  = application_clusters,
        overall_signal        = overall_signal,
        cross_app_flags       = cross_app_flags,
        log_record            = log_record,
    )


# ---------------------------------------------------------------------------
# API surface — for humantrace_api.py
# ---------------------------------------------------------------------------

def match_report_to_dict(report: MatchReport) -> dict:
    """Serialise MatchReport to a JSON-safe dict for the API response."""
    return {
        "target_application_id": report.target_application_id,
        "timestamp":             report.timestamp,
        "overall_signal":        report.overall_signal,
        "cross_app_flags":       report.cross_app_flags,
        "document_matches": [
            {
                "target_doc_id":          m.target_doc_id,
                "target_doc_type":        m.target_doc_type,
                "matched_application_id": m.matched_application_id,
                "matched_sender_id":      m.matched_sender_id,
                "matched_doc_id":         m.matched_doc_id,
                "matched_label":          m.matched_label,
                "matched_created_at":     m.matched_created_at,
                "similarity":             m.similarity,
                "strength":               m.strength,
            }
            for m in report.document_matches
        ],
        "application_clusters": [
            {
                "cluster_id":      c.cluster_id,
                "application_ids": c.application_ids,
                "anchor_doc_ids":  c.anchor_doc_ids,
                "max_similarity":  c.max_similarity,
                "min_similarity":  c.min_similarity,
                "signal":          c.signal,
                "interpretation":  c.interpretation,
            }
            for c in report.application_clusters
        ],
        "log_record": report.log_record,
    }


FASTAPI_ENDPOINT = '''
# ── Add to humantrace_api.py ──────────────────────────────────────────────

from src.humantrace_bse_matcher import (
    match_across_applications, match_report_to_dict
)

class BSEMatchRequest(BaseModel):
    application_id: str
    documents: list[DocPayload]          # reuse DocPayload from consistency endpoint

@app.post("/institutional/bse-match")
async def institutional_bse_match(req: BSEMatchRequest):
    docs = [
        DocumentInput(
            doc_id=d.doc_id,
            doc_type=d.doc_type,
            text=d.text,
            label=d.label,
        )
        for d in req.documents
    ]
    report = match_across_applications(req.application_id, docs)
    return match_report_to_dict(report)
'''


# ---------------------------------------------------------------------------
# Smoke test — creates synthetic BSE files, runs matcher, cleans up
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import tempfile
    import shutil

    print("\nSetting up synthetic BSE store...")

    # Create a temporary BSE directory with three stored fingerprints
    # (simulating two prior fraudulent applications + one clean one)
    tmp_bse = Path(tempfile.mkdtemp())

    STORED_FINGERPRINTS = [
        {
            "fingerprint_id": "fp_mk2026001",
            "sender_id": "labelled:M. Karimov",
            "application_id": "APP-2026-03201",
            "doc_id": "ps_001",
            "doc_type": "applicant_authored",
            "label": "Personal statement",
            # Deliberately similar vector to what our target will produce
            "reasoning_vector": [0.68, 0.06, 0.12, 0.95, 0.61],
            "signal_history": [{"timestamp": "2026-02-14T08:22:11Z", "verdict": "RED", "score": 0.21}],
            "created_at": "2026-02-14T08:22:11Z",
            "opt_in": True,
        },
        {
            "fingerprint_id": "fp_tr2026002",
            "sender_id": "labelled:T. Rashidova",
            "application_id": "APP-2026-03519",
            "doc_id": "cc_001",
            "doc_type": "applicant_authored",
            "label": "Cover correspondence",
            # Very similar vector — same synthetic source
            "reasoning_vector": [0.71, 0.05, 0.10, 0.98, 0.59],
            "signal_history": [{"timestamp": "2026-03-04T11:45:00Z", "verdict": "RED", "score": 0.18}],
            "created_at": "2026-03-04T11:45:00Z",
            "opt_in": True,
        },
        {
            "fingerprint_id": "fp_clean001",
            "sender_id": "auto:genuine@bank.com.au",
            "application_id": "APP-2026-02100",
            "doc_id": "ps_001",
            "doc_type": "applicant_authored",
            "label": "Personal statement",
            # Clearly different vector — genuine human
            "reasoning_vector": [0.45, 0.62, 0.38, 0.30, 0.82],
            "signal_history": [{"timestamp": "2026-01-10T09:00:00Z", "verdict": "GREEN", "score": 0.91}],
            "created_at": "2026-01-10T09:00:00Z",
            "opt_in": True,
        },
    ]

    for fp in STORED_FINGERPRINTS:
        path = tmp_bse / f"{fp['fingerprint_id']}.json"
        with open(path, "w") as f:
            json.dump(fp, f)

    print(f"  Created {len(STORED_FINGERPRINTS)} stored fingerprints in {tmp_bse}")

    # Target application documents (the new suspicious one)
    TARGET_DOCS = [
        DocumentInput(
            "ps_001", "applicant_authored",
            """
            I have worked at Meridian Financial Services as a senior analyst for eight years,
            joining in 2016 after completing my MBA at the University of Melbourne in 2015.
            Throughout my tenure I have demonstrated a comprehensive understanding of
            credit risk assessment and portfolio management. I am seeking this loan to
            expand my consulting practice, Meridian Advisory Group, which I established
            in 2020 alongside my primary employment. The business has grown substantially
            and requires capital to hire additional staff and acquire specialist software.
            """,
            "Personal statement"
        ),
        DocumentInput(
            "bp_001", "applicant_authored",
            """
            Executive Summary: This document presents a comprehensive strategic framework
            for the proposed expansion of services. The methodology encompasses a
            multifaceted approach to market penetration utilising synergistic partnerships
            and leveraging existing intellectual capital to facilitate sustainable growth
            trajectories. Financial projections demonstrate substantial returns commencing
            in the initial operational period, notwithstanding prevailing market conditions.
            """,
            "Business plan"
        ),
    ]

    print("\nRunning BSE cross-application match...")
    report = match_across_applications(
        target_application_id="APP-2026-03847",
        target_documents=TARGET_DOCS,
        bse_dir=tmp_bse,
    )

    # Display results
    print(f"\n{'='*62}")
    print(f"TARGET APPLICATION: {report.target_application_id}")
    print(f"OVERALL SIGNAL:     {report.overall_signal}")
    print(f"{'='*62}")

    print(f"\nDOCUMENT-LEVEL MATCHES ({len(report.document_matches)} found):")
    if report.document_matches:
        for m in report.document_matches:
            bar = "█" * int(m.similarity * 20) + "░" * (20 - int(m.similarity * 20))
            print(f"\n  {m.target_doc_id} → {m.matched_application_id} / {m.matched_doc_id}")
            print(f"  Sender:     {m.matched_sender_id}")
            print(f"  Similarity: {m.similarity:.4f}  [{bar}]  {m.strength}")
            print(f"  Filed:      {m.matched_created_at}")
    else:
        print("  None above threshold.")

    print(f"\nAPPLICATION CLUSTERS ({len(report.application_clusters)} found):")
    for cluster in report.application_clusters:
        print(f"\n  Cluster {cluster.cluster_id}  [{cluster.signal}]")
        print(f"  Applications: {cluster.application_ids}")
        print(f"  Anchored on:  {cluster.anchor_doc_ids}")
        print(f"  Similarity:   {cluster.min_similarity:.4f} – {cluster.max_similarity:.4f}")
        print(f"  Signal:       {cluster.interpretation}")

    print(f"\n{'─'*62}")
    print("CROSS-APP FLAGS:")
    for flag in report.cross_app_flags:
        print(f"  ⚑ {flag}")

    print(f"\n{'─'*62}")
    print("LOG RECORD (DilemmaNet):")
    print(json.dumps(report.log_record, indent=2))

    print(f"\n{'─'*62}")
    print("FASTAPI ENDPOINT (add to humantrace_api.py):")
    print(FASTAPI_ENDPOINT)

    # Clean up temp directory
    shutil.rmtree(tmp_bse)
    print("\n[Temp BSE directory cleaned up]")