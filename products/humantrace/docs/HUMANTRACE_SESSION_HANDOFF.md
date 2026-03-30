# HumanTrace — Session Handoff Document
*For continuity between Claude sessions*
*Last updated: 30 March 2026*

---

## 1. Project Identity

**Owlume** — reasoning clarity infrastructure (the engine)
**HumanTrace** — malicious synthetic reasoning detection (the product)
Tagline: *"Tells you if a real human sent that message — before you respond."*

Domains: humantrace.au / humantrace.com.au
GitHub: https://github.com/Owlume/humantrace (private)
Full brief: docs/humantrace_owlume_brief.md

---

## 2. What HumanTrace Does

Detects whether a message contains malicious synthetic reasoning —
reasoning engineered to exploit human trust, distort judgment, or
induce harmful action.

**Critical framing — locked:**
HumanTrace is NOT an AI-content detector. It does NOT ask "was this written by AI?"
It asks: "was this reasoning engineered to exploit a human?"

Not anti-AI reasoning. Anti-synthetic reasoning used with malicious intent.

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
C:\dev\owlume-engine\          ← Owlume platform monorepo root
├── owlume_core\               ← Shared engine
│   ├── elenx_engine.py
│   └── elenx_loader.py
├── products\
│   └── humantrace\            ← HumanTrace product
│       ├── humantrace_api.py
│       ├── src\
│       │   ├── main.py                        ← NEW v0 engine entry point
│       │   ├── signal_registry.json           ← NEW canonical signal ID registry
│       │   ├── detectors\
│       │   │   ├── __init__.py
│       │   │   ├── intent_detector.py         ← NEW HT.INT.EXT.*
│       │   │   ├── trust_hijack_detector.py   ← NEW HT.TRUST.AUTH.*
│       │   │   ├── pressure_detector.py       ← NEW HT.PRESS.URG.*
│       │   │   ├── distortion_detector.py     ← NEW HT.DIST.*
│       │   │   └── authenticity_gap_detector.py ← NEW HT.AUTH.GAP.*
│       │   ├── fusion\
│       │   │   ├── __init__.py
│       │   │   └── risk_fuser.py              ← NEW fusion layer
│       │   ├── trace_signals\                 ← Signal library framework
│       │   ├── humantrace_adapter.py
│       │   ├── humantrace_scanner.py          ← OLD five-layer engine (not yet replaced)
│       │   └── [other existing src files]
│       ├── assets\
│       ├── data\
│       ├── docs\
│       ├── extension\
│       └── reports\
└── pilot\                     ← Bank pilot materials
```

**Pilot documents (saved locally on ThinkPad, NOT in repo):**
- humantrace_pilot_internal.docx — internal planning, negotiating positions
- humantrace_pilot_external.docx — bank-facing proposal

---

## 5. How to Run Locally (ThinkPad)

```powershell
cd C:\dev\owlume-engine\products\humantrace
python -m uvicorn humantrace_api:app --reload --host 0.0.0.0 --port 8000
```

Consumer interface:      http://localhost:8000
Institutional interface: http://localhost:8000/institutional
iPhone (local):          http://192.168.0.42:8000
Tesseract OCR:           C:\Users\Brian-Owlume\AppData\Local\Programs\Tesseract-OCR\tesseract.exe

**To test the new v0 engine directly:**
```powershell
cd C:\dev\owlume-engine\products\humantrace\src
python -c "from main import analyse_message; r = analyse_message({'input_id': 'test', 'text': 'YOUR MESSAGE HERE'}); print(r['overall_risk']); print(r['summary'])"
```

---

## 6. Validated Accuracy Results

**Original engine (60-message dataset):**

| Metric | Result | Target |
|--------|--------|--------|
| Synthetic fraud detection | 85% | ≥80% ✅ |
| False positive rate | 6.7% | <15% ✅ |
| Mixed content detection | 90% | ≥70% ✅ |
| Genuine human accuracy | 100% | — ✅ |

**New v0 engine (8-case smoke test, 30 March 2026):**

| Case | Score | Label | Result |
|------|-------|-------|--------|
| Classic phishing SMS | 0.365 | HIGH | ✅ |
| ATO impersonation | 0.415 | HIGH | ✅ |
| Manager gift-card scam | 0.275 | MEDIUM | ✅ |
| Sophisticated internal fraud | 0.214 | MEDIUM | ✅ |
| Legitimate bank reminder | 0.025 | LOW | ✅ |
| False dilemma + fear | 0.188 | MEDIUM | ✅ |
| Legitimate debt collection | 0.079 | LOW | ✅ |
| Genuine personal message | 0.000 | LOW | ✅ |

Known limitations:
- EC007: marketing urgency indistinguishable from fraud urgency
- SF006/008/013: soft-language scams need real training data
- Layer 1 (Reasoning Analysis) conflates genuine human social awkwardness
  with synthetic social pressure — calibration target
- Threshold boundary: short messages with real but sparse signals may
  score just below MEDIUM (0.174 observed on "suspended immediately / verify now")

---

## 7. HumanTrace v0 Signal Engine — Architecture

### Core purpose (locked framing)
HumanTrace detects malicious synthetic reasoning — not AI-generated content.
The detection question is: "Was this reasoning engineered to exploit a human?"

### Three-tier reasoning spectrum
- **A. Benign synthetic reasoning** — AI-assisted but legitimate. No flag.
- **B. Ambiguous synthetic reasoning** — Optimised persuasion, unclear intent. Soft signal.
- **C. Malicious synthetic reasoning** — Primary target. High-confidence flag.

### Signal registry — canonical ID system
File: `src/signal_registry.json`
Format: `HT.[FAMILY].[SUBFAMILY].[NN]`

All signal IDs, families, weights, composite patterns, and schema
constraints live in this file. It is the single source of truth.
No signal ID exists outside the registry.

**Schema constraint (locked 2026-03-30):**
Output kind is SIGNAL only. No `recommended_reflection`, no advice,
no guidance language in any output field.

### Five detector families

| Family | File | Signals | Weight |
|--------|------|---------|--------|
| INT — Intent Extraction | `detectors/intent_detector.py` | HT.INT.EXT.01–05 | 0.30 |
| TRUST — Trust Hijack | `detectors/trust_hijack_detector.py` | HT.TRUST.AUTH.01–05 | 0.22 |
| PRESS — Pressure/Urgency | `detectors/pressure_detector.py` | HT.PRESS.URG.01–04 | 0.22 |
| DIST — Reasoning Distortion | `detectors/distortion_detector.py` | HT.DIST.01–05 | 0.16 |
| AUTH — Authenticity Gap | `detectors/authenticity_gap_detector.py` | HT.AUTH.GAP.01–04 | 0.10 |

**AUTH family cap:** Cannot contribute more than 0.10 to overall score.
Texture signal only — cannot drive a verdict independently.

**PSY signals (HT.PSY.*):** Defined in registry, NOT yet implemented.
Deferred to post-pilot. Will be amplifiers only, never primary detectors.

### Fusion layer
File: `src/fusion/risk_fuser.py`

Key mechanisms:
- **Dominance amplification:** If one family scores > 0.65, its weight increases by 0.20
- **Dominance override:** If one primary family scores > 0.75, verdict forced HIGH
- **Interaction boosts:** Additive boosts when families co-fire (e.g. INT+PRESS +0.08)
- **Composite patterns:** CP.AI.FRAUD, CP.HUMAN.MANIP, CP.INST.MALICE

Calibrated thresholds (from actual output distribution):
- HIGH: ≥ 0.35
- MEDIUM: ≥ 0.18
- LOW: < 0.18

### Entry point
File: `src/main.py`
Function: `analyse_message(payload: dict) -> dict`

**Not yet wired into humantrace_api.py.** The old `humantrace_scanner.py`
five-layer engine is still serving the live product. Wiring the new
engine into the API is a pending build task.

### Three composite patterns

| ID | Label | Trigger |
|----|-------|---------|
| CP.AI.FRAUD | AI Fraud Signature | AUTH>0.20 + PRESS>0.35 + INT>0.40 |
| CP.HUMAN.MANIP | Human Manipulator | TRUST>0.25 + INT>0.15 + PRESS>0.15 |
| CP.INST.MALICE | Institutional Malice | DIST>0.25 + INT>0.30 + TRUST>0.25 |

---

## 8. Input Methods Built

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

## 9. UI Language — Two Vocabulary Principle

**CRITICAL — established and locked in:**

Internal code, schemas, logs, handoff docs use precise technical vocabulary.
User-facing UI uses layman language only.

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
**Institutional UI language audit still outstanding.**

---

## 10. Institutional Product

### Two product lines

| Product | User | Use case |
|---------|------|----------|
| HumanTrace Consumer | Ordinary person | Single suspicious message |
| HumanTrace Institutional | Loan manager / fraud analyst | Document batch + BSE matching |

### Modules (src/)

**humantrace_consistency.py** — Cross-document consistency scorer
**humantrace_bse_matcher.py** — Cross-application BSE matching
**humantrace_document_extractor.py** — Format-aware text extraction

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

---

## 12. GitHub / CI Status

Repository: https://github.com/Owlume/humantrace (private)
Commit email: shen.baiping@hotmail.com

**CI status:**
- ✅ Owlume Smoke Tests — green on every push
- ✅ Owlume Schema Validation — green on every push
- ⚪ L2 CI Validation Pipeline — disabled on push
- ✅ L1 Auto-Learning Loop — runs daily at 6am, green

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

### IMMEDIATE — Pre-code action plan (Phase 1)
Start here in the next session. All writing tasks, no code, no server.

- [ ] **1.1 Calibration Baseline Definition Document** — BLOCKING
      What human baseline reasoning looks like per enterprise context.
      Output: `calibration_baseline_v1.md` — 3–5 pages.
      This is the single most important task before the bank pilot.

- [ ] **1.2 Persuasion Optimisation Boundary Definition** — BLOCKING
      Separates legitimate professional communication from synthetic
      persuasion optimisation for Signal Domain 5.
      Output: `persuasion_boundary_definition_v1.md` — 2 pages max.

- [ ] **1.3 Cognitive Governance Field Definition** — IMPORTANT
      One-page definition of cognitive governance as a named discipline.
      Output: One page — opens every regulatory conversation.

- [ ] **1.4 Signal-to-Action Boundary** — BLOCKING
      Written resolution of tension between signal-not-action principle
      and Section 3.6 of Technical Definition.
      Output: Half page appended to build memo.

### Build tasks (pending, after Phase 1)
- [ ] Wire new v0 engine (`src/main.py`) into `humantrace_api.py`
      replacing old `humantrace_scanner.py` calls
- [ ] Institutional UI language audit (two-vocabulary principle)
- [ ] Layer 1 recalibration (conflates social awkwardness with pressure)
- [ ] Behavioural signals v2: precision asymmetry + structural smoothness
- [ ] Scan speed benchmark on production server

### Bank pilot preparation (Phase 4)
- [ ] Synthetic dataset build (300 documents)
- [ ] ASIC/APRA one-page governance brief
- [ ] Model DPA template
- [ ] Analyst demonstration script

### Infrastructure
- [ ] GitHub Personal Access Token — add workflow scope
- [ ] GitHub branch protection rules — disable for solo development
- [ ] Domain Lock on in Crazy Domains (both domains)

---

## 14. Strategic Context

**Core purpose (locked):**
HumanTrace is not anti-AI reasoning.
HumanTrace is anti-synthetic reasoning used with malicious intent.

**Moat architecture — established principles:**
- Two vocabularies: internal technical / external layman
- signal_registry.json is the canonical signal ID system — one system only
- BSE fingerprint store compounds over time
- Composite patterns (CP.*) are the named detection signatures —
  these are the proprietary detection intelligence

**The detection question (locked):**
Not: "Was this produced by AI?"
But: "Was this reasoning engineered to exploit a human?"

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

## 16. Key Documents Produced This Session

| Document | Purpose |
|----------|---------|
| `humantrace_architecture_mapping.docx` | Phase 3.1 canonical architecture map — three mapping tables reconciling all prior architectural descriptions |
| `signal_registry.json` | Canonical signal ID registry — single source of truth for all HT.* IDs |
| `intent_detector.py` | HT.INT.EXT.01–05 — intent extraction detector |
| `trust_hijack_detector.py` | HT.TRUST.AUTH.01–05 — trust hijack detector |
| `pressure_detector.py` | HT.PRESS.URG.01–04 — pressure/urgency detector |
| `distortion_detector.py` | HT.DIST.01–05 — reasoning distortion detector |
| `authenticity_gap_detector.py` | HT.AUTH.GAP.01–04 — authenticity gap detector |
| `risk_fuser.py` | Fusion layer with dominance amplification, interaction boosts, composite patterns |
| `main.py` | Single entry point — `analyse_message()` |

---

## 17. How to Continue This Work

When starting a new Claude session:
1. Paste this entire document as your first message
2. State which task you are starting (e.g. "Starting Phase 1, Task 1.1")
3. Claude will have full context to continue immediately

**Next session opens with:** Phase 1, Task 1.1 —
Calibration Baseline Definition Document

---

*End of handoff document*
*HumanTrace / Owlume Pty Ltd — Confidential*