# =============================================================================
# humantrace_api_institutional.py
#
# Paste the contents of this file into humantrace_api.py.
#
# Prerequisites — add to imports at top of humantrace_api.py:
#   from fastapi import UploadFile, File, Form
#   from fastapi.staticfiles import StaticFiles
#   from fastapi.responses import FileResponse
#
# Prerequisites — install if not present:
#   pip install python-docx pdfminer.six
#
# New imports to add alongside existing ones:
# =============================================================================

from fastapi import UploadFile, File, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from typing import Optional
from pydantic import BaseModel

from src.humantrace_consistency import (
    DocumentInput, score_consistency, consistency_report_to_dict
)
from src.humantrace_bse_matcher import (
    match_across_applications, match_report_to_dict
)
from src.humantrace_document_extractor import (
    extract_text, check_dependencies
)


# =============================================================================
# Serve the institutional interface
# Add this alongside the existing route that serves humantrace_interface.html
# =============================================================================

@app.get("/institutional")
async def institutional_interface():
    return FileResponse("assets/humantrace_institutional.html")


# =============================================================================
# Pydantic models
# =============================================================================

class DocPayload(BaseModel):
    doc_id:   str
    doc_type: str    # "applicant_authored" | "employer_authored" | "third_party"
    text:     str
    label:    str = ""


class BatchConsistencyRequest(BaseModel):
    application_id: str
    documents:      list[DocPayload]


class BSEMatchRequest(BaseModel):
    application_id: str
    documents:      list[DocPayload]


class FullInstitutionalRequest(BaseModel):
    application_id: str
    documents:      list[DocPayload]


# =============================================================================
# Endpoint 1: Cross-document consistency scoring
# POST /institutional/consistency
# =============================================================================

@app.post("/institutional/consistency")
async def institutional_consistency(req: BatchConsistencyRequest):
    """
    Score cross-document consistency for a batch of documents
    from a single loan application.

    Returns: ConsistencyReport as JSON
    """
    docs = [
        DocumentInput(
            doc_id   = d.doc_id,
            doc_type = d.doc_type,
            text     = d.text,
            label    = d.label,
        )
        for d in req.documents
    ]
    report = score_consistency(req.application_id, docs)
    return consistency_report_to_dict(report)


# =============================================================================
# Endpoint 2: BSE cross-application matching
# POST /institutional/bse-match
# =============================================================================

@app.post("/institutional/bse-match")
async def institutional_bse_match(req: BSEMatchRequest):
    """
    Compare reasoning vectors from a target application against all
    stored BSE fingerprints. Returns cluster signals.

    Returns: MatchReport as JSON
    """
    docs = [
        DocumentInput(
            doc_id   = d.doc_id,
            doc_type = d.doc_type,
            text     = d.text,
            label    = d.label,
        )
        for d in req.documents
    ]
    report = match_across_applications(req.application_id, docs)
    return match_report_to_dict(report)


# =============================================================================
# Endpoint 3: Full institutional scan (consistency + BSE in one call)
# POST /institutional/scan
#
# This is what the UI calls. Runs both analyses and returns a combined result.
# =============================================================================

@app.post("/institutional/scan")
async def institutional_scan(req: FullInstitutionalRequest):
    """
    Full institutional scan: consistency scoring + BSE matching in one call.
    This is the primary endpoint used by the institutional UI.

    Returns: combined report with both analyses
    """
    docs = [
        DocumentInput(
            doc_id   = d.doc_id,
            doc_type = d.doc_type,
            text     = d.text,
            label    = d.label,
        )
        for d in req.documents
    ]

    consistency_report = score_consistency(req.application_id, docs)
    bse_report         = match_across_applications(req.application_id, docs)

    # Derive overall application signal — worst of the two
    signals = [consistency_report.overall_signal, bse_report.overall_signal]
    if "RED" in signals:
        overall = "RED"
    elif "YELLOW" in signals:
        overall = "YELLOW"
    else:
        overall = "GREEN"

    return {
        "application_id":  req.application_id,
        "overall_signal":  overall,
        "consistency":     consistency_report_to_dict(consistency_report),
        "bse_match":       match_report_to_dict(bse_report),
    }


# =============================================================================
# Endpoint 4: File upload — extract text from .docx / .pdf / .txt
# POST /institutional/upload
#
# Accepts a single file upload and returns extracted text + metadata.
# The UI calls this when a document is dropped/selected, then stores
# the returned text locally before calling /institutional/scan.
# =============================================================================

@app.post("/institutional/upload")
async def institutional_upload(
    file:     UploadFile = File(...),
    doc_type: str        = Form("applicant_authored"),
    doc_id:   str        = Form(""),
    label:    str        = Form(""),
):
    """
    Extract text from an uploaded .docx, .pdf, or .txt file.

    Returns extracted text + metadata ready for use in /institutional/scan.
    The UI stores the returned text and doc_id, then batches multiple
    uploads into a single /institutional/scan call.
    """
    data     = await file.read()
    filename = file.filename or ""
    result   = extract_text(data, filename=filename)

    # Auto-generate doc_id from filename if not supplied
    if not doc_id:
        stem   = filename.rsplit(".", 1)[0] if "." in filename else filename
        doc_id = stem.lower().replace(" ", "_")[:40] or "doc_001"

    if not result.ok:
        return {
            "success":  False,
            "doc_id":   doc_id,
            "filename": filename,
            "error":    result.warning or "Text extraction failed.",
            "text":     "",
            "method":   result.method,
        }

    return {
        "success":  True,
        "doc_id":   doc_id,
        "filename": filename,
        "label":    label or filename,
        "doc_type": doc_type,
        "text":     result.text,
        "method":   result.method,
        "warning":  result.warning,
        "char_count": len(result.text),
    }


# =============================================================================
# Startup dependency check — add to your existing startup event or app init
# =============================================================================

@app.on_event("startup")
async def check_institutional_deps():
    deps = check_dependencies()
    missing = [name for name, ok in deps.items() if not ok]
    if missing:
        print(f"[HumanTrace] WARNING: Missing optional dependencies: {missing}")
        print(f"[HumanTrace] Install with: pip install {' '.join(missing)}")
    else:
        print("[HumanTrace] Institutional dependencies: all present.")