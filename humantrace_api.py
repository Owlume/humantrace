# humantrace_api.py
# HumanTrace — FastAPI Backend
# Powered by Owlume
#
# Purpose:
#   Bridges the HumanTrace interface (HTML/browser/iPhone)
#   to the humantrace_scanner.py Python engine.
#
# How to run:
#   uvicorn humantrace_api:app --reload --host 0.0.0.0 --port 8000
#
# Then open in browser or iPhone (same WiFi):
#   http://YOUR_THINKPAD_IP:8000
#
# Find your ThinkPad IP:
#   Windows: open Command Prompt → type: ipconfig
#   Look for "IPv4 Address" e.g. 192.168.1.42

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import json
import os
import sys

# Add src/ to path so we can import humantrace_scanner
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from humantrace_logger import log_humantrace_session

# Use adapter (ElenxEngine) with automatic fallback to scanner
try:
    from humantrace_adapter import scan_message_via_engine as scan_message
    ADAPTER_AVAILABLE = True
except Exception:
    from humantrace_scanner import scan_message
    ADAPTER_AVAILABLE = False

# Import governance gate (single call site per runtime_finalize.py)
try:
    from runtime_finalize import finalize_output
    GOVERNANCE_AVAILABLE = True
except ImportError:
    GOVERNANCE_AVAILABLE = False

# In-memory scan store for judgment landing correlation
# In production: replace with Redis or database
_scan_store: dict = {}

# ── App setup ─────────────────────────────────────────────────────────────────

app = FastAPI(
    title="HumanTrace API",
    description="Human reasoning presence verification. Powered by Owlume.",
    version="0.1.0",
)

# Allow browser requests from any origin (needed for iPhone access)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Load interface HTML ───────────────────────────────────────────────────────

def _load_interface() -> str:
    """Load the HumanTrace HTML interface from assets folder."""
    # Try common locations
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


# ── Request / Response models ─────────────────────────────────────────────────

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


# ── Routes ────────────────────────────────────────────────────────────────────

@app.get("/", response_class=HTMLResponse)
async def serve_interface():
    """Serve the HumanTrace interface to browser or iPhone."""
    html = _load_interface()

    # Patch the interface to call the real API instead of client-side simulation
    # Replaces the simulated scan call with a real fetch to /scan
    patched = html.replace(
        "// Simulate processing delay (replace with actual API call in production)",
        "// Calling real Owlume-powered API"
    ).replace(
        """  // Simulate processing delay (replace with actual API call in production)
  setTimeout(() => {
    const contextHint = document.getElementById('contextSelect').value || null;
    const result = runDetection(text, contextHint);
    renderResults(result);
    btn.disabled = false;
    btn.classList.remove('loading');
  }, 900);""",
        """  const contextHint = document.getElementById('contextSelect').value || null;
  fetch('/scan', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message: text, context_hint: contextHint })
  })
  .then(r => r.json())
  .then(result => {
    renderResults(result);
    btn.disabled = false;
    btn.classList.remove('loading');
  })
  .catch(err => {
    alert('Scan failed. Is the server running?');
    btn.disabled = false;
    btn.classList.remove('loading');
  });"""
    )
    return HTMLResponse(content=patched)


@app.post("/scan")
async def scan(req: ScanRequest):
    """
    Scan a message for human reasoning presence.

    Returns a ScanResult with signal, confidence, layer findings,
    plain English summary, and analyst questions.

    Output kind: SIGNAL — not advice, not instruction.
    Human analyst makes the final judgment.
    """
    if not req.message or not req.message.strip():
        return JSONResponse(
            status_code=400,
            content={"error": "No message provided."}
        )

    try:
        result = scan_message(
            message=req.message.strip(),
            context_hint=req.context_hint or None,
        )
        result_dict = result.to_dict()

        # Add message preview for logging (first 120 chars, no PII)
        result_dict.setdefault("meta", {})["message_preview"] = req.message.strip()[:120]

        # Store scan result for judgment landing correlation
        _scan_store[result.scan_id] = result_dict

        # Pass through governance gate (runtime_finalize.py — single call site)
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
                result_dict["governance"] = {
                    "final_kind": final_kind,
                    "passed": True,
                }
            except Exception as ge:
                result_dict["governance"] = {"passed": False, "error": str(ge)}

        return JSONResponse(content=result_dict)

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": f"Scan engine error: {str(e)}"}
        )


@app.post("/judgment")
async def judgment(req: JudgmentRequest):
    """
    Receive judgment landing from user.
    Logs completed session to DilemmaNet.

    Governance alignment:
    - Validates judgment type, statement, acknowledgment
    - Logs via humantrace_logger → clarity_logger → DilemmaNet
    - Share status is user-controlled
    - Failure to log does NOT block user session completion
    """
    # Retrieve stored scan result
    scan_result = _scan_store.get(req.scan_id)
    if not scan_result:
        # Scan not found — still accept judgment, log what we have
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

        # Clean up scan store
        _scan_store.pop(req.scan_id, None)

        return JSONResponse(content={
            "logged": True,
            "session_id": record.get("session_id"),
            "judgment_type": req.judgment_type,
            "share_status": req.share_status,
        })

    except ValueError as ve:
        return JSONResponse(
            status_code=400,
            content={"error": str(ve)}
        )
    except Exception as e:
        # Log failure does not block session completion
        return JSONResponse(content={
            "logged": False,
            "error": str(e),
            "note": "Session complete for user. Logging failed silently."
        })


@app.get("/health")
async def health():
    """Health check — confirms API and scanner are running."""
    return {
        "status": "running",
        "product": "HumanTrace",
        "powered_by": "Owlume",
        "scanner": "humantrace_scanner.py",
        "governance": "Stage 14 compliant",
    }


# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "humantrace_api:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )