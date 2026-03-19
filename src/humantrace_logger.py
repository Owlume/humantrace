# src/humantrace_logger.py
# HumanTrace — DilemmaNet Logger
# Powered by Owlume
#
# Purpose:
#   Maps HumanTrace scan results + judgment landing into valid
#   clarity_gain_record.schema.json records and logs to DilemmaNet.
#
# Schema note:
#   Uses clarity_gain_record.schema.json judgment type enums:
#   "position" | "constraint" | "next_step" | "defer"
#   NOTE: judgment_terminal_state.schema.json uses different enums
#   ("position" | "boundary" | "deferral") — this is a known schema
#   drift issue in the Owlume codebase. Using clarity_gain_record
#   enums as authoritative since they match judgment_landing.py.
#
# Governance alignment:
#   - Every HumanTrace session that completes judgment landing is logged
#   - Share status is user-controlled: "opt_in" | "skipped"
#   - CG_pre is always 0.0 (no clarity before scan)
#   - CG_post maps to scan confidence
#   - Mode is always "Critical" (fraud detection lens)
#   - Principle maps to detected fraud category

from __future__ import annotations

import datetime
import json
import os
import sys
from typing import Any, Dict, Optional

# Add src/ to path for clarity_logger import
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

try:
    from clarity_logger import log_record, make_session_id
    CLARITY_LOGGER_AVAILABLE = True
except ImportError:
    CLARITY_LOGGER_AVAILABLE = False


def _iso_now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def _map_fraud_category_to_principle(fraud_category: Optional[str]) -> str:
    """Map HumanTrace fraud category to closest Owlume Critical matrix principle."""
    mapping = {
        "phishing":                 "Stakeholder",
        "investment_fraud":         "Risk",
        "romance_scam":             "Assumption",
        "authority_impersonation":  "Clarity",
        "manufactured_urgency":     "Action",
        "purpose_pure_construction":"Evidence",
    }
    return mapping.get(fraud_category or "", "Stakeholder")


def _map_signal_to_proof(signal: str, confidence: float) -> list:
    """Map HumanTrace signal to proof signals compatible with DilemmaNet."""
    if signal == "red" and confidence >= 0.80:
        return ["Threat Identified", "Δ-Insight"]
    if signal == "red":
        return ["Threat Identified"]
    if signal == "yellow":
        return ["Δ-Insight"]
    if signal == "green":
        return ["Human Present", "Δ-Insight"]
    return []


def _map_drivers_from_layers(layers: list) -> list:
    """
    Extract context drivers from HumanTrace layer findings.
    Maps to existing context_drivers.json IDs where possible.
    """
    drivers = []
    for layer in layers:
        if not isinstance(layer, dict):
            continue
        findings = layer.get("findings", [])
        for finding in findings:
            f = finding.lower()
            if "urgency" in f or "time pressure" in f:
                drivers.append("time_pressure")
            if "incentive" in f or "guaranteed" in f or "returns" in f:
                drivers.append("misaligned_incentives")
            if "confidence" in f and "costless" in f:
                drivers.append("moral_hazard")
            if "purpose-pure" in f or "purpose pure" in f:
                drivers.append("metric_fixation")
    # Deduplicate
    seen = set()
    out = []
    for d in drivers:
        if d not in seen:
            out.append(d)
            seen.add(d)
    return out


def build_dilemmanet_record(
    *,
    scan_result: Dict[str, Any],
    judgment_type: str,
    judgment_statement: str,
    judgment_confidence: float,
    acknowledged: bool,
    share_status: str,
) -> Dict[str, Any]:
    """
    Build a valid clarity_gain_record.schema.json record
    from a HumanTrace scan result and judgment landing.

    Args:
        scan_result: The ScanResult.to_dict() output
        judgment_type: "position" | "constraint" | "next_step" | "defer"
        judgment_statement: User's stated decision (10-500 chars)
        judgment_confidence: 0.0 - 1.0
        acknowledged: Must be True
        share_status: "opt_in" | "skipped"

    Returns:
        Dict conforming to clarity_gain_record.schema.json
    """
    # Core scan data
    scan_id = scan_result.get("scan_id", make_session_id("HT"))
    signal = scan_result.get("signal", "yellow")
    confidence = float(scan_result.get("confidence", 0.5))
    fraud_category = scan_result.get("fraud_category")
    layers = scan_result.get("layers", [])
    timestamp = scan_result.get("timestamp", _iso_now())

    # Map to Owlume schema fields
    principle = _map_fraud_category_to_principle(fraud_category)
    proof_signals = _map_signal_to_proof(signal, confidence)
    drivers = _map_drivers_from_layers(layers)

    # Judgment terminal state
    jts_timestamp = _iso_now()
    judgment_terminal_state = {
        "type": judgment_type,
        "statement": judgment_statement.strip(),
        "confidence": round(judgment_confidence, 2),
        "owner": "user",
        "acknowledged": True,
        "timestamp": jts_timestamp,
    }

    # Clarity gain mapping
    # CG_pre = 0.0 (no clarity before scan — user had raw suspicion only)
    # CG_post = scan confidence (clarity gained from scan)
    # CG_delta = post - pre
    cg_pre = 0.0
    cg_post = round(confidence, 2)
    cg_delta = round(cg_post - cg_pre, 2)

    # Build full record
    record = {
        "session_id": scan_id,
        "user_text": scan_result.get("meta", {}).get("message_preview", "[HumanTrace scan]"),
        "judgment_landing": {
            "type": judgment_type,
            "statement": judgment_statement.strip(),
            "confidence": round(judgment_confidence, 2),
            "acknowledged": True,
        },
        "detected": {
            "mode": "Critical",
            "principle": principle,
            "drivers": drivers,
            "empathy": False,
            "confidence": confidence,
            "alt": {
                "mode": None,
                "principle": None,
                "confidence": None,
            },
            "judgment_terminal_state": judgment_terminal_state,
        },
        "voices": ["Thiel", "Feynman", "Peterson"],
        "clarity_gain": {
            "CG_pre": cg_pre,
            "CG_post": cg_post,
            "CG_delta": cg_delta,
        },
        "proof_signals": proof_signals,
        "timestamp": timestamp,
    }

    # Share metadata (privacy-first)
    if share_status == "opt_in":
        record["share"] = {
            "status": "opt_in",
            "channel": "markdown",
            "consent": True,
            "timestamp": jts_timestamp,
        }
    else:
        record["share"] = {
            "status": "skipped",
        }

    # HumanTrace extension metadata
    # Stored outside schema-validated fields for internal use
    record["_humantrace"] = {
        "signal": signal,
        "fraud_category": fraud_category,
        "first_contact": scan_result.get("first_contact", True),
        "mixed_content_warning": scan_result.get("meta", {}).get("mixed_content_warning", False),
        "layer_count": len(layers),
        "product": "HumanTrace",
        "powered_by": "Owlume",
    }

    return record


def log_humantrace_session(
    *,
    scan_result: Dict[str, Any],
    judgment_type: str,
    judgment_statement: str,
    judgment_confidence: float,
    acknowledged: bool,
    share_status: str,
    logs_dir: str = "data/logs",
) -> Dict[str, Any]:
    """
    Build and log a HumanTrace session to DilemmaNet.

    Returns the logged record.
    Raises if judgment landing is invalid.
    """
    # Validate judgment type
    valid_types = ("position", "constraint", "next_step", "defer")
    if judgment_type not in valid_types:
        raise ValueError(f"Invalid judgment type: {judgment_type}. Must be one of {valid_types}")

    # Validate statement
    stmt = (judgment_statement or "").strip()
    if len(stmt) < 10:
        raise ValueError("Judgment statement too short (minimum 10 characters)")
    if len(stmt) > 500:
        raise ValueError("Judgment statement too long (maximum 500 characters)")

    # Validate acknowledgment
    if not acknowledged:
        raise ValueError(
            "Judgment must be acknowledged. "
            "The user must confirm: 'This judgment is mine. HumanTrace did not decide for me.'"
        )

    # Build record
    record = build_dilemmanet_record(
        scan_result=scan_result,
        judgment_type=judgment_type,
        judgment_statement=stmt,
        judgment_confidence=max(0.0, min(1.0, float(judgment_confidence))),
        acknowledged=True,
        share_status=share_status if share_status in ("opt_in", "skipped") else "skipped",
    )

    # Log via clarity_logger if available
    if CLARITY_LOGGER_AVAILABLE:
        try:
            log_record(record, logs_dir=logs_dir)
        except Exception as e:
            # Log failure should not block the user
            # Record is still returned for audit
            record["_log_error"] = str(e)
    else:
        # Fallback: write directly to JSONL
        _fallback_log(record, logs_dir)

    return record


def _fallback_log(record: Dict[str, Any], logs_dir: str) -> None:
    """
    Direct JSONL logging when clarity_logger is not importable.
    Used during development and testing.
    """
    os.makedirs(logs_dir, exist_ok=True)
    month = datetime.datetime.now().strftime("%Y%m")
    path = os.path.join(logs_dir, f"humantrace_{month}.jsonl")
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")