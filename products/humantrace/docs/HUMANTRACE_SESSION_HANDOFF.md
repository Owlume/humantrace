# HumanTrace — Session Handoff Document
*For continuity between Claude sessions*
*Last updated: 22 March 2026*

---

## 1. Project Identity

**Owlume** — reasoning clarity infrastructure (the engine)
**HumanTrace** — human reasoning presence verification (the product)
Tagline: *"Tells you if a real human sent that message — before you respond."*

Domains: humantrace.au / humantrace.com.au
GitHub: https://github.com/Owlume/humantrace (private)
Full brief: docs/humantrace_owlume_brief.md

---

## 2. What HumanTrace Does

Detects whether genuine human reasoning is present behind a communication —
or whether it is synthetic fraud designed to deceive.

Not a style detector. Not an AI content detector.
A reasoning authenticity verifier.

Three signals: 🔴 RED / 🟡 YELLOW / 🟢 GREEN

---

## 3. Live Deployment — Production Server

**Status: LIVE**

| Detail | Value |
|--------|-------|
| URL | https://humantrace.au |
| Institutional URL | https://humantrace.au/institutional |
| Server | DigitalOcean Droplet — Sydney (SYD1) |
| IP address | 134.199.149.238 |
| OS | Ubuntu 24.04 LTS |
| Plan | 1GB RAM / 1 CPU / 25GB SSD — $6 USD/month |
| HTTPS | Let's Encrypt — auto-renews, expires 19 Jun 2026 |
| Process manager | systemd — auto-starts on reboot |
| Web gateway | Nginx |

**To SSH into the server from ThinkPad PowerShell:**
```powershell
ssh root@134.199.149.238
```

**To deploy an update:**
```bash
cd /var/www/humantrace
git pull
systemctl restart humantrace
systemctl status humantrace
```

**To check server logs:**
```bash
journalctl -u humantrace -n 100
```

---

## 4. Complete File Architecture

```
/var/www/humantrace/  (production server)
C:\dev\owlume-engine\ (local ThinkPad)
├── humantrace_api.py              ← FastAPI backend
├── src/
│   ├── humantrace_scanner.py      ← Five-layer detection engine
│   ├── humantrace_adapter.py      ← ElenxEngine adapter
│   ├── humantrace_logger.py       ← DilemmaNet logging
│   ├── humantrace_bse.py          ← Bias Signature Engine
│   ├── humantrace_url_scanner.py  ← URL/domain fraud detection
│   ├── humantrace_consistency.py  ← Cross-doc consistency scorer
│   ├── humantrace_bse_matcher.py  ← Cross-app BSE matching
│   ├── humantrace_document_extractor.py ← Format-aware text extraction
│   ├── elenx_engine.py            ← Core Owlume reasoning engine
│   ├── trace_signals/             ← Signal library architecture — NEW
│   │   ├── __init__.py
│   │   └── humantrace_behavioural_signals.py ← Hughes framework v1
│   └── [other engine files]
├── assets/
│   ├── humantrace_interface.html  ← Consumer UI
│   └── humantrace_institutional.html ← Institutional UI
├── data/
│   ├── bse/                       ← Sender fingerprints (runtime)
│   ├── logs/                      ← DilemmaNet JSONL logs (gitignored)
│   └── sessions/                  ← File-based session store (gitignored)
└── docs/
    ├── humantrace_owlume_brief.md
    ├── humantrace_session_handoff.md
    └── humantrace_deployment_guide.md
```

**Pilot documents (saved locally on ThinkPad, NOT in repo):**
- humantrace_pilot_internal.docx — internal planning, negotiating positions
- humantrace_pilot_external.docx — bank-facing proposal

---

## 5. How to Run Locally (ThinkPad)

```powershell
cd C:\dev\owlume-engine
.\.venv\Scripts\Activate.ps1
python -m uvicorn humantrace_api:app --reload --host 0.0.0.0 --port 8000
```

Consumer interface:      http://localhost:8000
Institutional interface: http://localhost:8000/institutional
iPhone (local):          http://192.168.0.42:8000
Tesseract OCR:           C:\Users\Brian-Owlume\AppData\Local\Programs\Tesseract-OCR\tesseract.exe

---

## 6. Validated Accuracy Results

Dataset: 60 labeled messages, 4 categories

| Metric | Result | Target |
|--------|--------|--------|
| Synthetic fraud detection | 85% | ≥80% ✅ |
| False positive rate | 6.7% | <15% ✅ |
| Mixed content detection | 90% | ≥70% ✅ |
| Genuine human accuracy | 100% | — ✅ |

Known limitations:
- EC007: marketing urgency indistinguishable from fraud urgency
- SF006/008/013: soft-language scams need real training data
- Layer 1 (Reasoning Analysis) conflates genuine human social awkwardness
  with synthetic social pressure — calibration target for next session

---

## 7. Input Methods Built

| Method | Status | How |
|--------|--------|-----|
| Paste text | ✅ | Tab 1 in consumer interface |
| Screenshot | ✅ | Tab 2 — OCR via Tesseract |
| Link / URL | ✅ | Tab 3 — domain reputation |
| Browser extension | ✅ | Edge/Chrome — right-click + popup |
| Batch document upload | ✅ | Institutional UI — .docx/.pdf/.txt/.png/.jpg |
| iPhone web app | ✅ | https://humantrace.au in Safari |
| Email forward | Planned | Future |
| WhatsApp/SMS | Planned | After bank pilot |
| iPhone native app | Planned | App Store — separate build project |

---

## 8. UI Language — Two Vocabulary Principle

**CRITICAL — established and locked in:**

Internal code, schemas, logs, DilemmaNet, BSE, handoff docs use precise
technical vocabulary. User-facing UI uses layman language only.

| Internal (code) | User-facing (UI) |
|-----------------|------------------|
| engine_mode_detection | Reasoning Analysis |
| manipulation_driver_analysis | Influence Patterns |
| conviction_cost | Personal Investment |
| pattern_library | Known Fraud Patterns |
| absence_signals | Missing Human Signals |
| engine_question_quality | Investigation Questions |
| structural_reasoning | Writing Consistency |
| contextual_plausibility | Specific Detail |

All layer names and body text in consumer UI have been translated.
Institutional UI language audit still outstanding.

---

## 9. Signal Architecture

### Five-layer engine (humantrace_scanner.py + humantrace_adapter.py)

| Layer | Internal name | User label | What it measures |
|-------|--------------|------------|-----------------|
| L1 | engine_mode_detection | Reasoning Analysis | Owlume mode detection, persuasion architecture |
| L2 | contextual_plausibility | Specific Detail | Context plausibility vs claimed role |
| L3 | conviction_cost | Personal Investment | Personal stakes, emotional cost |
| L4 | pattern_library | Known Fraud Patterns | Known synthetic fraud topologies |
| L5 | absence_signals | Missing Human Signals | Purpose-purity, absence of human irregularity |

### trace_signals/ — Signal library architecture (NEW)

A separate, extensible signal library framework. Each module follows
a common interface contract returning `SignalLibraryResult`.

**humantrace_behavioural_signals.py — v1 (Hughes framework)**
Derived from intelligence and interrogation tradecraft (*The Ellipsis Manual*).

Three signal categories implemented:

| Signal | Weight | What it measures |
|--------|--------|-----------------|
| Micro-variation | 0.35 | Self-interruption, topic drift, register shifts, sentence length variance |
| Limbic leakage | 0.40 | Emotional leakage, over/under-qualification, spontaneous self-disclosure |
| Investment asymmetry | 0.25 | Whether emotional weight matches the size of the ask |

Two further categories specified for v2:
- Precision asymmetry (generic vs specific references, round vs exact numbers)
- Structural smoothness (transition word density, paragraph regularity)

**Smoke test results:**

| Test case | Human | Synthetic | Verdict |
|-----------|-------|-----------|---------|
| Genuine personal message | 0.338 | 0.035 | ✅ Correct |
| Sophisticated fraud (short, intellectual) | 0.000 | 0.230 | ✅ Correct |
| Book passage | 0.070 | 0.122 | ✅ Honest (uncertain) |
| Phishing email | 0.000 | 0.140 | ✅ Correct |

**Wiring:** BSL results feed into L3 (Personal Investment). If human_score
> 0.20, L3 confidence increases and findings are augmented. If
synthetic_score > 0.15, L3 confidence decreases.

**Future modules:** Add new `.py` files to `src/trace_signals/` following
the same `SignalLibraryResult` interface. Each module is independently
versioned, tested, and validated.

---

## 10. Institutional Product

### Two product lines

| Product | User | Use case |
|---------|------|----------|
| HumanTrace Consumer | Ordinary person | Single suspicious message |
| HumanTrace Institutional | Loan manager / fraud analyst | Document batch + BSE matching |

### Modules (src/)

**humantrace_consistency.py** — Cross-document consistency scorer
- Five dimensions: authorial_voice (0.25), vocabulary_register (0.20),
  timeline_coherence (0.20), named_entity_alignment (0.20), employment_narrative (0.15)
- Thresholds: GREEN ≥0.70 / YELLOW ≥0.40 / RED <0.40

**humantrace_bse_matcher.py** — Cross-application BSE matching
- Document matches feed up to application clusters
- Thresholds: HIGH ≥0.88 (RED) / MEDIUM ≥0.75 (YELLOW)

**humantrace_document_extractor.py** — Format-aware text extraction
- .docx → python-docx / .pdf → pdfminer.six + OCR / images → Tesseract

### API endpoints

| Endpoint | Method | What it does |
|----------|--------|-------------|
| /institutional | GET | Serves institutional HTML interface |
| /institutional/upload | POST | Extracts text from uploaded file |
| /institutional/scan | POST | Full scan: consistency + BSE in one call |
| /institutional/consistency | POST | Consistency scoring only |
| /institutional/bse-match | POST | BSE matching only |

---

## 11. Bank Pilot

**Primary vertical:** Fraud protection
**First customer target:** Traditional Australian bank (specific bank identified)
**Pilot design:** 30 days, 5 analysts, synthetic data preferred

**Five success criteria:**
1. Synthetic detection rate ≥80%
2. False positive rate <15%
3. Scan speed <8 seconds per document
4. Audit trail regulatory defensibility
5. Analyst usability ≥4/5

**Primary blocker:** Procurement — strategy is to frame as research
collaboration, use synthetic data, stay below procurement threshold.

**Pre-meeting actions still outstanding:**
1. Benchmark scan speed on production server
2. Build synthetic dataset: 300 documents, 200 genuine / 100 synthetic-fraud
3. Prepare one-page ASIC/APRA governance brief
4. Draft model DPA template

---

## 12. GitHub / CI Status

Repository: https://github.com/Owlume/humantrace (private)
Commit email: shen.baiping@hotmail.com

**CI status:**
- ✅ Owlume Smoke Tests — green on every push
- ✅ Owlume Schema Validation — green on every push
- ⚪ L2 CI Validation Pipeline — disabled on push (pre-existing failure
  from Feb 2026, unrelated to HumanTrace). Only runs on pull requests.
- ✅ L1 Auto-Learning Loop — runs daily at 6am, green

**GitHub Personal Access Token on server:**
Needs `workflow` scope added for future workflow file changes.
Current token can push all other files — only workflow files require
the extra scope.

**Branch protection rules:** Still active — shows "bypassed rule violations"
on every push. Not blocking but worth disabling for solo development.
Go to: https://github.com/Owlume/humantrace/settings/branches

**To push updates from ThinkPad:**
```powershell
cd C:\dev\owlume-engine
git add -A
git commit -m "Description of changes"
git push
```

**Then deploy to server:**
```bash
ssh root@134.199.149.238
cd /var/www/humantrace
git pull
systemctl restart humantrace
```

---

## 13. Outstanding Items — Next Session Priorities

**Calibration (highest priority before bank pilot):**
- [ ] Layer 1 (Reasoning Analysis) conflates genuine social awkwardness
      with synthetic social pressure — needs mode detector recalibration
- [ ] Scan speed benchmark on production server — must measure before
      claiming <8 sec in bank meeting
- [ ] Behavioural signals v2: precision asymmetry + structural smoothness

**UI:**
- [ ] Institutional UI language audit — same layman label principle as consumer

**Bank pilot preparation:**
- [ ] Synthetic dataset build (300 documents)
- [ ] ASIC/APRA one-page governance brief
- [ ] Model DPA template

**Infrastructure:**
- [ ] GitHub Personal Access Token — add workflow scope
- [ ] GitHub branch protection rules — disable for solo development
- [ ] Domain Lock on in Crazy Domains (both domains)

---

## 14. Strategic Context

**Moat architecture — established principles:**
- Two vocabularies: internal technical / external layman. Never let
  internal vocabulary appear in user-facing output.
- trace_signals/ is the extensible signal library framework. Each new
  framework (Hughes v1 is first) gets its own named, versioned module.
- BSE fingerprint store accumulates with every scan — compounds over time
  in ways a competitor starting today cannot replicate.

**Five-year vision:**
Not a fraud detector — a reasoning credentialing system.
In a world where AI communication is ubiquitous, verified human
reasoning presence becomes a certifiable credential.

---

## 15. Owlume Philosophy — Non-Negotiable

- Unconstrained in seeing, constrained only in acting
- Never prescribe decisions — surface signals only
- Human judgment always owns the outcome
- Governance-first — no architectural compromise for speed
- Output kind: SIGNAL, not ACTION, ADVICE, or INSTRUCTIONS

---

## 16. How to Continue This Work

When starting a new Claude session:
1. Paste this entire document as your first message
2. Claude will have full context to continue immediately
3. Reference specific file names when asking for code changes
4. GitHub repo and live server both contain current code

---

*End of handoff document*