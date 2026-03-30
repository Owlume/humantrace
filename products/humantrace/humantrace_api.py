# humantrace_api.py
# HumanTrace — FastAPI Backend
# Powered by Owlume
#
# How to run:
#   python -m uvicorn humantrace_api:app --reload --host 0.0.0.0 --port 8000
#
# Open in browser:      http://localhost:8000
# Open on iPhone:       http://192.168.0.42:8000  (your ThinkPad IP)
# Institutional UI:     http://localhost:8000/institutional

# ── Standard library ──────────────────────────────────────────────────────────

import json
import os
import sys
import time
import glob
import base64
import io

# ── FastAPI ───────────────────────────────────────────────────────────────────

from fastapi import FastAPI, Request, UploadFile, File, Form
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Optional

# ── Path setup ────────────────────────────────────────────────────────────────

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

# ── Import engine ─────────────────────────────────────────────────────────────

from humantrace_logger import log_humantrace_session

try:
    from humantrace_url_scanner import scan_url
    URL_SCANNER_AVAILABLE = True
except Exception:
    URL_SCANNER_AVAILABLE = False

try:
    from humantrace_adapter import scan_message_via_engine as scan_message
    ADAPTER_AVAILABLE = True
except Exception:
    from humantrace_scanner import scan_message
    ADAPTER_AVAILABLE = False

# ── Import OCR ────────────────────────────────────────────────────────────────

try:
    import pytesseract
    from PIL import Image
    _tess_paths = [
        r"C:\Users\Brian-Owlume\AppData\Local\Programs\Tesseract-OCR\tesseract.exe",
        r"C:\Program Files\Tesseract-OCR\tesseract.exe",
        r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe",
    ]
    for _tp in _tess_paths:
        if os.path.exists(_tp):
            pytesseract.pytesseract.tesseract_cmd = _tp
            break
    OCR_AVAILABLE = True
except Exception:
    OCR_AVAILABLE = False

# ── Import BSE ────────────────────────────────────────────────────────────────

try:
    from humantrace_bse import get_bse_context, store_scan_fingerprint, build_bse_meta
    BSE_AVAILABLE = True
except Exception:
    BSE_AVAILABLE = False

# ── Import governance gate ────────────────────────────────────────────────────

try:
    from runtime_finalize import finalize_output
    GOVERNANCE_AVAILABLE = True
except Exception:
    GOVERNANCE_AVAILABLE = False

# ── Import institutional modules ──────────────────────────────────────────────

from src.humantrace_consistency import (
    DocumentInput, score_consistency, consistency_report_to_dict
)
from src.humantrace_bse_matcher import (
    match_across_applications, match_report_to_dict
)
from src.humantrace_document_extractor import (
    extract_text, check_dependencies
)

# ── Session store (file-based, survives restarts) ─────────────────────────────

SESSION_DIR = os.path.join(os.path.dirname(__file__), "data", "sessions")

def _session_path(scan_id: str) -> str:
    os.makedirs(SESSION_DIR, exist_ok=True)
    return os.path.join(SESSION_DIR, f"{scan_id}.json")

def _store_session(scan_id: str, data: dict) -> None:
    try:
        with open(_session_path(scan_id), "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, default=str)
    except Exception:
        pass

def _load_session(scan_id: str) -> dict:
    try:
        path = _session_path(scan_id)
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
    except Exception:
        pass
    return {}

def _delete_session(scan_id: str) -> None:
    try:
        path = _session_path(scan_id)
        if os.path.exists(path):
            os.remove(path)
    except Exception:
        pass

def _cleanup_old_sessions(max_age_hours: int = 24) -> None:
    try:
        cutoff = time.time() - (max_age_hours * 3600)
        for path in glob.glob(os.path.join(SESSION_DIR, "*.json")):
            if os.path.getmtime(path) < cutoff:
                os.remove(path)
    except Exception:
        pass

try:
    _cleanup_old_sessions()
except Exception:
    pass

# ── App setup ─────────────────────────────────────────────────────────────────

app = FastAPI(
    title="HumanTrace API",
    description="Human reasoning presence verification. Powered by Owlume.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Load consumer interface ───────────────────────────────────────────────────

def _load_interface() -> str:
    candidates = [
        os.path.join(os.path.dirname(__file__), "assets", "humantrace_interface.html"),
        os.path.join(os.path.dirname(__file__), "interface", "humantrace_interface.html"),
        os.path.join(os.path.dirname(__file__), "humantrace_interface.html"),
    ]
    for path in candidates:
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                return f.read()
    return "<h1>Interface file not found. Check humantrace_interface.html location.</h1>"

# ── Request models ────────────────────────────────────────────────────────────

class ScanRequest(BaseModel):
    message: str
    context_hint: Optional[str] = None

class JudgmentRequest(BaseModel):
    scan_id: str
    judgment_type: str
    statement: str
    confidence: float
    acknowledged: bool
    share_status: str = "skipped"

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

# ── Helper: run scan with BSE and governance ──────────────────────────────────

def _run_scan(message: str, context_hint: Optional[str], input_method: str = "text") -> dict:
    """Shared scan logic for both text and image endpoints."""
    _t0 = time.time()

    bse_context = {}
    if BSE_AVAILABLE:
        try:
            bse_context = get_bse_context(message=message, sender_id=None)
        except Exception:
            pass

    result = scan_message(
        message=message,
        context_hint=context_hint or None,
        bse_history=bse_context.get("history") if bse_context else None,
    )
    _scan_ms = round((time.time() - _t0) * 1000)

    result_dict = result.to_dict()
    result_dict.setdefault("meta", {}).update({
        "scan_time_ms": _scan_ms,
        "input_method": input_method,
        "message_preview": message[:120],
    })

    if BSE_AVAILABLE and bse_context:
        result_dict["meta"].update(build_bse_meta(bse_context))
        adj = bse_context.get("confidence_adjustment", 0.0)
        if adj != 0.0:
            result_dict["confidence"] = round(
                min(max(result_dict["confidence"] + adj, 0.0), 0.99), 3
            )

    if GOVERNANCE_AVAILABLE:
        try:
            final_kind, final_content, decision_info = finalize_output(
                did=result.scan_id,
                input_type="EXTERNAL_MESSAGE",
                output_kind="SIGNAL",
                content=result.plain_english,
                irreversible_risk=False,
                distortion_present=result.signal == "red",
                insufficient_reflection_window=False,
            )
            result_dict["meta"]["governance"] = {"final_kind": final_kind, "passed": True}
        except Exception as ge:
            result_dict["meta"]["governance"] = {"passed": False, "error": str(ge)}

    _store_session(result.scan_id, {**result_dict, "_bse_context": bse_context})
    return result_dict

# ── Startup event ─────────────────────────────────────────────────────────────

@app.on_event("startup")
async def check_institutional_deps():
    deps = check_dependencies()
    missing = [name for name, ok in deps.items() if not ok]
    if missing:
        print(f"[HumanTrace] WARNING: Missing optional dependencies: {missing}")
        print(f"[HumanTrace] Install with: pip install {' '.join(missing)}")
    else:
        print("[HumanTrace] Institutional dependencies: all present.")

# ═════════════════════════════════════════════════════════════════════════════
# CONSUMER ROUTES
# ═════════════════════════════════════════════════════════════════════════════

@app.get("/", response_class=HTMLResponse)
async def serve_interface():
    """Serve the HumanTrace consumer interface."""
    return HTMLResponse(content=_load_interface())


@app.post("/scan")
async def scan(req: ScanRequest):
    """
    Scan a text message for human reasoning presence.
    Output kind: SIGNAL — not advice, not instruction.
    """
    if not req.message or not req.message.strip():
        return JSONResponse(status_code=400, content={"error": "No message provided."})
    try:
        result_dict = _run_scan(req.message.strip(), req.context_hint, input_method="text")
        return JSONResponse(content=result_dict)
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": f"Scan error: {str(e)}"})


@app.post("/scan-image")
async def scan_image(request: Request):
    """
    Scan a screenshot image for human reasoning presence.
    Accepts: JSON with base64 image OR multipart form upload.
    """
    if not OCR_AVAILABLE:
        return JSONResponse(
            status_code=503,
            content={
                "error": "OCR not available on this server.",
                "fallback": "Please copy and paste the message text manually."
            }
        )

    try:
        content_type = request.headers.get("content-type", "")
        context_hint = None

        if "multipart/form-data" in content_type:
            form = await request.form()
            file = form.get("file")
            if not file:
                return JSONResponse(status_code=400, content={"error": "No file provided."})
            image_bytes = await file.read()
            context_hint = form.get("context_hint")

        elif "application/json" in content_type:
            body = await request.json()
            b64 = body.get("image", "")
            context_hint = body.get("context_hint")
            if not b64:
                return JSONResponse(status_code=400, content={"error": "No image provided."})
            if "," in b64:
                b64 = b64.split(",", 1)[1]
            image_bytes = base64.b64decode(b64)

        else:
            return JSONResponse(status_code=400, content={"error": "Unsupported content type."})

        # OCR
        image = Image.open(io.BytesIO(image_bytes))
        if image.mode not in ("RGB", "L"):
            image = image.convert("RGB")

        extracted_text = pytesseract.image_to_string(image, config="--psm 6").strip()

        if not extracted_text or len(extracted_text) < 10:
            return JSONResponse(
                status_code=422,
                content={
                    "error": "Could not extract readable text from this image.",
                    "suggestion": "Try a clearer screenshot or copy and paste the text manually.",
                    "extracted_text": extracted_text,
                }
            )

        result_dict = _run_scan(extracted_text, context_hint, input_method="screenshot")
        result_dict["meta"]["extracted_text"] = extracted_text
        result_dict["meta"]["extracted_text_length"] = len(extracted_text)

        return JSONResponse(content=result_dict)

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": f"Image scan error: {str(e)}"})


@app.post("/judgment")
async def judgment(req: JudgmentRequest):
    """
    Receive judgment landing from user.
    Logs completed session to DilemmaNet.
    Governance: user owns the decision. HumanTrace does not decide.
    """
    scan_result = _load_session(req.scan_id)
    if not scan_result:
        scan_result = {
            "scan_id": req.scan_id,
            "signal": "yellow",
            "confidence": 0.5,
            "layers": [],
            "meta": {},
        }

    try:
        record = log_humantrace_session(
            scan_result=scan_result,
            judgment_type=req.judgment_type,
            judgment_statement=req.statement,
            judgment_confidence=req.confidence,
            acknowledged=req.acknowledged,
            share_status=req.share_status,
        )

        # Store BSE fingerprint if sender identified and user opted in
        if BSE_AVAILABLE:
            try:
                bse_ctx = scan_result.get("_bse_context", {})
                sender_hash = bse_ctx.get("sender_hash")
                id_method = bse_ctx.get("id_method")
                if sender_hash and id_method:
                    store_scan_fingerprint(
                        sender_hash=sender_hash,
                        id_method=id_method,
                        scan_result=scan_result,
                        share_status=req.share_status,
                    )
            except Exception:
                pass

        _delete_session(req.scan_id)

        return JSONResponse(content={
            "logged": True,
            "session_id": record.get("session_id"),
            "judgment_type": req.judgment_type,
            "share_status": req.share_status,
        })

    except ValueError as ve:
        return JSONResponse(status_code=400, content={"error": str(ve)})
    except Exception as e:
        return JSONResponse(content={
            "logged": False,
            "error": str(e),
            "note": "Session complete for user. Logging failed silently."
        })


@app.post("/scan-url")
async def scan_url_endpoint(request: Request):
    """
    Scan a URL, domain, or email address for fraud signals.
    Output kind: SIGNAL — not advice, not instruction.
    """
    if not URL_SCANNER_AVAILABLE:
        return JSONResponse(
            status_code=503,
            content={"error": "URL scanner not available."}
        )
    try:
        body = await request.json()
        url_input = (body.get("url") or body.get("domain") or "").strip()
        if not url_input:
            return JSONResponse(
                status_code=400,
                content={"error": "No URL or domain provided."}
            )
        result = scan_url(url_input)
        _store_session(result["scan_id"], result)
        return JSONResponse(content=result)
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": f"URL scan error: {str(e)}"}
        )


@app.get("/health")
async def health():
    return {
        "status": "running",
        "product": "HumanTrace",
        "powered_by": "Owlume",
        "version": "1.0.0",
        "ocr_available": OCR_AVAILABLE,
        "bse_available": BSE_AVAILABLE,
        "adapter_available": ADAPTER_AVAILABLE,
        "governance_available": GOVERNANCE_AVAILABLE,
    }


# ═════════════════════════════════════════════════════════════════════════════
# INSTITUTIONAL ROUTES
# ═════════════════════════════════════════════════════════════════════════════

@app.get("/institutional")
async def institutional_interface():
    """Serve the HumanTrace institutional interface."""
    return FileResponse("assets/humantrace_institutional.html")


@app.post("/institutional/consistency")
async def institutional_consistency(req: BatchConsistencyRequest):
    """
    Score cross-document consistency for a batch of documents
    from a single loan application.
    Output kind: SIGNAL — not advice, not instruction.
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


@app.post("/institutional/bse-match")
async def institutional_bse_match(req: BSEMatchRequest):
    """
    Compare reasoning vectors from a target application against all
    stored BSE fingerprints. Returns cluster signals.
    Output kind: SIGNAL — not advice, not instruction.
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


@app.post("/institutional/scan")
async def institutional_scan(req: FullInstitutionalRequest):
    """
    Full institutional scan: consistency scoring + BSE matching in one call.
    Primary endpoint used by the institutional UI.
    Output kind: SIGNAL — not advice, not instruction.
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

    # Overall signal — worst of the two analyses
    signals = [consistency_report.overall_signal, bse_report.overall_signal]
    if "RED" in signals:
        overall = "RED"
    elif "YELLOW" in signals:
        overall = "YELLOW"
    else:
        overall = "GREEN"

    return {
        "application_id": req.application_id,
        "overall_signal": overall,
        "consistency":    consistency_report_to_dict(consistency_report),
        "bse_match":      match_report_to_dict(bse_report),
    }


@app.post("/institutional/upload")
async def institutional_upload(
    file:     UploadFile = File(...),
    doc_type: str        = Form("applicant_authored"),
    doc_id:   str        = Form(""),
    label:    str        = Form(""),
):
    """
    Extract text from an uploaded .docx, .pdf, .txt, or image file.
    Returns extracted text + metadata ready for /institutional/scan.
    """
    data     = await file.read()
    filename = file.filename or ""
    result   = extract_text(data, filename=filename)

    # Auto-generate doc_id from filename if not supplied
    if not doc_id:
        stem   = filename.rsplit(".", 1)[0] if "." in filename else filename
        doc_id = stem.lower().replace(" ", "_")[:40] or "doc_001"

    if not result.ok:
        return JSONResponse(content={
            "success":  False,
            "doc_id":   doc_id,
            "filename": filename,
            "error":    result.warning or "Text extraction failed.",
            "text":     "",
            "method":   result.method,
        })

    return JSONResponse(content={
        "success":    True,
        "doc_id":     doc_id,
        "filename":   filename,
        "label":      label or filename,
        "doc_type":   doc_type,
        "text":       result.text,
        "method":     result.method,
        "warning":    result.warning,
        "char_count": len(result.text),
    })


# ═════════════════════════════════════════════════════════════════════════════
# ENTRY POINT
# ═════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("humantrace_api:app", host="0.0.0.0", port=8000, reload=True)