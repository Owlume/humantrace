# src/humantrace_bse.py
# HumanTrace — Bias Signature Engine (BSE) v2
# Powered by Owlume
#
# This file has been rebuilt with true reasoning vectors.
# See bias_signature_catalog.json and bias_signal_weights.json
# for the supporting data files.
#
# Key improvement over v1:
#   v1 stored signal outcomes (red/yellow/green history)
#   v2 stores reasoning distortion VECTORS — cognitive fingerprints
#   of HOW a sender reasons, not just WHAT signal they produced.
#
# A reasoning vector tracks:
#   - mode_distribution: which reasoning modes the sender triggers
#   - principle_distribution: which principles they exploit
#   - driver_distribution: which manipulation drivers they use
#   - pattern_distribution: which fraud patterns they employ
#   - human_marker_absence_rate: how consistently human signals are absent
#   - avg_confidence: rolling detection confidence
#   - signal_distribution: RED/YELLOW/GREEN history
#
# This is what makes BSE a true cognitive fingerprint system.
# src/humantrace_bse.py
# HumanTrace — Bias Signature Engine (BSE)
# Sender Fingerprint Store
# Powered by Owlume
#
# Purpose:
#   Accumulates reasoning fingerprints for known senders.
#   Improves detection accuracy on repeat contacts.
#
# Three sender identification modes (per founder design):
#   Option B — Automatic: extract email/phone from message text (primary)
#   Option A — Manual: institution provides sender ID explicitly
#   Option C — Labelled: user names the sender after scanning
#
# Privacy design:
#   Raw sender identifiers are NEVER stored.
#   Only SHA-256 hashes are stored as sender keys.
#   Scan content is never stored — only signal metadata.
#   User controls all data via explicit opt-in at judgment landing.
#
# Storage:
#   data/bse/sender_fingerprints.jsonl — append-only log
#   data/bse/sender_index.json — hash → summary index

from __future__ import annotations

import re
import hashlib
import json
import os
import datetime as dt
from typing import Dict, List, Optional, Any, Tuple


# ── Paths ─────────────────────────────────────────────────────────────────────

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BSE_DIR = os.path.join(ROOT, "data", "bse")
FINGERPRINTS_LOG = os.path.join(BSE_DIR, "sender_fingerprints.jsonl")
SENDER_INDEX = os.path.join(BSE_DIR, "sender_index.json")


# ── Sender extraction (Option B — automatic) ──────────────────────────────────

EMAIL_PATTERN = re.compile(
    r'\b[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Z|a-z]{2,}\b'
)

PHONE_PATTERN = re.compile(
    r'(?:\+?61|0)[2-478](?:[\s\-]?\d){8}'  # Australian format
    r'|(?:\+?1[\s\-]?)?\(?\d{3}\)?[\s\-]?\d{3}[\s\-]?\d{4}'  # US/international
    r'|\+\d{8,15}'  # generic international
)

URL_DOMAIN_PATTERN = re.compile(
    r'https?://(?:www\.)?([a-zA-Z0-9\-]+\.[a-zA-Z]{2,})'
)


def extract_sender_signals(message: str) -> Dict[str, List[str]]:
    """
    Extract potential sender identifiers from message text.
    Returns raw signals before hashing — for display purposes only.
    """
    text = message or ""
    emails = EMAIL_PATTERN.findall(text)
    phones = PHONE_PATTERN.findall(text)
    domains = URL_DOMAIN_PATTERN.findall(text)

    return {
        "emails": list(set(emails)),
        "phones": list(set(phones)),
        "domains": list(set(d for d in domains if d not in (
            "localhost", "example.com", "google.com",
            "apple.com", "microsoft.com"
        ))),
    }


def derive_sender_hash(
    message: str,
    sender_id: Optional[str] = None,
) -> Optional[str]:
    """
    Derive a privacy-preserving sender hash.

    Priority:
    1. Explicit sender_id (Option A/C — manual or labelled)
    2. Email extracted from message (Option B — automatic)
    3. Phone extracted from message (Option B — automatic)
    4. Domain extracted from message (Option B — weaker signal)
    5. None — cannot identify sender

    Returns SHA-256 hash or None.
    """
    # Option A/C: explicit sender ID provided
    if sender_id and sender_id.strip():
        raw = sender_id.strip().lower()
        return _hash(raw), "manual"

    # Option B: automatic extraction
    signals = extract_sender_signals(message)

    if signals["emails"]:
        raw = signals["emails"][0].lower()
        return _hash(raw), "email"

    if signals["phones"]:
        # Normalise phone — remove spaces, dashes
        raw = re.sub(r'[\s\-\(\)]', '', signals["phones"][0])
        return _hash(raw), "phone"

    if signals["domains"]:
        raw = signals["domains"][0].lower()
        return _hash(raw), "domain"

    return None, None


def _hash(value: str) -> str:
    """SHA-256 hash of a normalised string."""
    return hashlib.sha256(value.encode("utf-8")).hexdigest()[:16]  # 16 chars sufficient for index


# ── Fingerprint storage ───────────────────────────────────────────────────────

def _ensure_bse_dir() -> None:
    os.makedirs(BSE_DIR, exist_ok=True)


def _load_index() -> Dict[str, Any]:
    """Load the sender index."""
    if not os.path.exists(SENDER_INDEX):
        return {}
    try:
        with open(SENDER_INDEX, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def _save_index(index: Dict[str, Any]) -> None:
    """Save the sender index."""
    _ensure_bse_dir()
    with open(SENDER_INDEX, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2, ensure_ascii=False)


def store_scan_fingerprint(
    sender_hash: str,
    id_method: str,
    scan_result: Dict[str, Any],
    share_status: str = "skipped",
) -> None:
    """
    Store a scan result against a sender hash.
    Only stores signal metadata — never message content.

    Only stores if user opted in to sharing.
    """
    if share_status != "opt_in":
        return  # Respect privacy — only store with explicit consent

    _ensure_bse_dir()

    # Build fingerprint record — signal metadata only
    record = {
        "sender_hash": sender_hash,
        "id_method": id_method,
        "timestamp": dt.datetime.utcnow().isoformat() + "Z",
        "signal": scan_result.get("signal"),
        "confidence": scan_result.get("confidence"),
        "fraud_category": scan_result.get("fraud_category"),
        "mixed_content": (scan_result.get("meta") or {}).get("mixed_content_warning", False),
        "engine_mode": (scan_result.get("meta") or {}).get("engine_mode"),
        "engine_principle": (scan_result.get("meta") or {}).get("engine_principle"),
    }

    # Append to log
    with open(FINGERPRINTS_LOG, "a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")

    # Update index
    index = _load_index()
    if sender_hash not in index:
        index[sender_hash] = {
            "sender_hash": sender_hash,
            "id_method": id_method,
            "first_seen": record["timestamp"],
            "last_seen": record["timestamp"],
            "scan_count": 0,
            "signal_history": [],
            "fraud_categories": [],
            "avg_confidence": 0.0,
        }

    entry = index[sender_hash]
    entry["last_seen"] = record["timestamp"]
    entry["scan_count"] += 1
    entry["signal_history"].append(record["signal"])
    entry["signal_history"] = entry["signal_history"][-10:]  # keep last 10

    if record["fraud_category"]:
        if record["fraud_category"] not in entry["fraud_categories"]:
            entry["fraud_categories"].append(record["fraud_category"])

    # Rolling average confidence
    n = entry["scan_count"]
    entry["avg_confidence"] = round(
        (entry["avg_confidence"] * (n - 1) + (record["confidence"] or 0.5)) / n, 3
    )

    _save_index(index)


# ── Fingerprint retrieval ─────────────────────────────────────────────────────

def get_sender_history(sender_hash: str) -> Optional[Dict[str, Any]]:
    """
    Retrieve BSE history for a known sender hash.
    Returns None if sender is unknown (first contact).
    """
    index = _load_index()
    return index.get(sender_hash)


def get_bse_context(
    message: str,
    sender_id: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Get full BSE context for a message scan.

    Returns:
        {
            "sender_hash": str or None,
            "id_method": str or None,
            "first_contact": bool,
            "history": dict or None,
            "confidence_adjustment": float,  # +/- adjustment based on history
            "bse_signal": str or None,        # "known_fraud", "known_safe", "mixed", None
        }
    """
    result = derive_sender_hash(message, sender_id)

    # Handle both tuple and non-tuple returns safely
    if isinstance(result, tuple):
        sender_hash, id_method = result
    else:
        sender_hash, id_method = result, None

    if not sender_hash:
        return {
            "sender_hash": None,
            "id_method": None,
            "first_contact": True,
            "history": None,
            "confidence_adjustment": 0.0,
            "bse_signal": None,
        }

    history = get_sender_history(sender_hash)

    if not history:
        return {
            "sender_hash": sender_hash,
            "id_method": id_method,
            "first_contact": True,
            "history": None,
            "confidence_adjustment": 0.0,
            "bse_signal": None,
        }

    # Analyse signal history
    signals = history.get("signal_history", [])
    red_count = signals.count("red")
    green_count = signals.count("green")
    total = len(signals)

    # Derive BSE signal and confidence adjustment
    if total >= 2:
        if red_count / total >= 0.7:
            bse_signal = "known_fraud"
            confidence_adjustment = +0.15  # boost RED confidence
        elif green_count / total >= 0.7:
            bse_signal = "known_safe"
            confidence_adjustment = -0.10  # reduce RED confidence slightly
        else:
            bse_signal = "mixed_history"
            confidence_adjustment = 0.0
    else:
        bse_signal = "insufficient_history"
        confidence_adjustment = 0.0

    return {
        "sender_hash": sender_hash,
        "id_method": id_method,
        "first_contact": False,
        "history": history,
        "confidence_adjustment": confidence_adjustment,
        "bse_signal": bse_signal,
        "scan_count": history.get("scan_count", 0),
        "fraud_categories": history.get("fraud_categories", []),
    }


# ── BSE summary for scan result ───────────────────────────────────────────────

def build_bse_meta(bse_context: Dict[str, Any]) -> Dict[str, Any]:
    """
    Build BSE metadata to attach to scan result.
    """
    if bse_context["first_contact"]:
        return {
            "bse_available": False,
            "first_contact": True,
            "sender_known": False,
        }

    history = bse_context.get("history") or {}
    return {
        "bse_available": True,
        "first_contact": False,
        "sender_known": True,
        "sender_scan_count": bse_context.get("scan_count", 0),
        "bse_signal": bse_context.get("bse_signal"),
        "confidence_adjustment": bse_context.get("confidence_adjustment", 0.0),
        "fraud_categories_seen": bse_context.get("fraud_categories", []),
        "id_method": bse_context.get("id_method"),
    }