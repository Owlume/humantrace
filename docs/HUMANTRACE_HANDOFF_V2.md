# HumanTrace — Session Handoff Document
*For continuity between Claude sessions*
*Last updated: 1 April 2026*

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

**The deepest architectural principle — locked:**
HumanTrace detects the *human trace* of reasoning — genuine cognitive residue
from a mind with real stakes, real knowledge limits, and real blind spots.
The corpus and calibration are anchored to this principle. Entering a
synthetic-against-synthetic game is the primary architectural failure mode.

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
│       │   ├── main.py                        ← v0 engine entry point
│       │   ├── signal_registry.json           ← canonical signal ID registry
│       │   ├── detectors\
│       │   │   ├── __init__.py
│       │   │   ├── intent_detector.py         ← HT.INT.EXT.*
│       │   │   ├── trust_hijack_detector.py   ← HT.TRUST.AUTH.*
│       │   │   ├── pressure_detector.py       ← HT.PRESS.URG.*
│       │   │   ├── distortion_detector.py     ← HT.DIST.*
│       │   │   └── authenticity_gap_detector.py ← HT.AUTH.GAP.*
│       │   ├── fusion\
│       │   │   ├── __init__.py
│       │   │   └── risk_fuser.py              ← fusion layer
│       │   ├── trace_signals\                 ← Signal library framework
│       │   ├── humantrace_adapter.py
│       │   ├── humantrace_scanner.py          ← OLD five-layer engine (not yet replaced)
│       │   └── [other existing src files]
│       ├── assets\
│       ├── data\
│       ├── docs\                              ← Phase 1 foundational docs (md)
│       │   ├── calibration_baseline_v1.md
│       │   ├── persuasion_boundary_definition_v1.md
│       │   ├── cognitive_governance_field_definition_v1.md
│       │   ├── signal_to_action_boundary_v1.md
│       │   └── corpus\
│       │       ├── corpus_construction_protocol_v1.1.md
│       │       └── batch1\
│       │           ├── corpus_batch1_fin_001_005_v1.md
│       │           ├── corpus_batch1_fin_006_010_v1.md
│       │           ├── corpus_batch2_fin_011_020_v1.md
│       │           ├── corpus_batch3_fin_021_040_v1.md
│       │           ├── corpus_batch4_legal_001_015_v1.md
│       │           ├── corpus_batch5_legal_016_030_v1.md
│       │           ├── corpus_batch6_int_001_020_v1.md
│       │           ├── corpus_batch7_int_021_040_v1.md
│       │           ├── corpus_batch8_adv_001_015_v1.md
│       │           ├── corpus_batch9_adv_016_030_v1.md
│       │           ├── corpus_batch10_anti_001_010_v1.md
│       │           ├── corpus_batch11_anti_011_020_v1.md
│       │           └── corpus_batch12_anti_021_030_v1.md
│       ├── extension\
│       └── reports\
├── scripts\
│   └── smoke_test_engine_fusion.py            ← FIXED (traceback import + owlume_core path)
└── pilot\                                     ← Bank pilot materials
```

**Pilot documents (saved locally on ThinkPad, NOT in repo):**
- humantrace_pilot_internal.docx — internal planning, negotiating positions
- humantrace_pilot_external.docx — bank-facing proposal

**Phase 1 documents also exist as polished .docx on ThinkPad Desktop:**
- calibration_baseline_v1.docx
- persuasion_boundary_definition_v1.docx
- cognitive_governance_field_definition_v1.docx
- signal_to_action_boundary_v1.docx
- corpus_construction_protocol_v1.1.docx

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

**Known limitations (pre-corpus-calibration):**
- EC007: marketing urgency indistinguishable from fraud urgency
- SF006/008/013: soft-language scams need real training data
- Layer 1 (Reasoning Analysis) conflates genuine human social awkwardness
  with synthetic social pressure — calibration target
- Threshold boundary: short messages with real but sparse signals may
  score just below MEDIUM (0.174 observed on "suspended immediately / verify now")
- **CRITICAL UNRESOLVED:** False positive rate on genuine institutional
  communications has not been tested at scale. The engine returned uncertain
  results on clearly human-authored expert writing (*Algorithms to Live By*).
  This is the most important unsolved calibration problem before pilot.
  The 170-example corpus now exists to resolve it.

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

**Signal-to-action framing for pilot (locked — see signal_to_action_boundary_v1.md):**
HumanTrace outputs are signals, not actions. This framing is the commercial
and regulatory architecture that makes the pilot viable with an APRA-regulated
institution. Do not characterise outputs as recommendations, suggested actions,
or decision support in any bank-facing conversation.

---

## 12. GitHub / CI Status

Repository: https://github.com/Owlume/humantrace (private)
Commit email: shen.baiping@hotmail.com

**CI status (as of 1 April 2026):**
- ✅ Owlume Smoke Tests — GREEN (fixed this session)
- ✅ Owlume Schema Validation — green on every push
- ⚪ L2 CI Validation Pipeline — disabled on push
- ✅ L1 Auto-Learning Loop — runs daily at 6am, green

**Smoke test fix (applied this session):**
The smoke test was broken since the 30 March monorepo restructure.
Root cause: `scripts/smoke_test_engine_fusion.py` was importing
`src.elenx_engine` but after restructure the module moved to `owlume_core/`.
Fix: added `traceback` import and added `owlume_core/` to `sys.path`.
File: `scripts/smoke_test_engine_fusion.py` — commit 7098b0f.

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

## 13. Phase 1 Foundational Documents — COMPLETE

All four Phase 1 documents are complete, committed to the repo as `.md`
files, and exist as polished `.docx` files on the ThinkPad Desktop.

| Task | Document | Status | Repo path |
|------|----------|--------|-----------|
| 1.1 | Calibration Baseline Definition | ✅ Complete | `docs/calibration_baseline_v1.md` |
| 1.2 | Persuasion Optimisation Boundary | ✅ Complete | `docs/persuasion_boundary_definition_v1.md` |
| 1.3 | Cognitive Governance Field Definition | ✅ Complete | `docs/cognitive_governance_field_definition_v1.md` |
| 1.4 | Signal-to-Action Boundary | ✅ Complete | `docs/signal_to_action_boundary_v1.md` |

**Key locked decisions from Phase 1:**
- §3.6 Technical Definition restatement: "escalation pathways" → "escalation signal pathway", "recommended analyst actions" → "analyst review prompts", "suggested review steps" → "signal review context". Locked 30 March 2026.
- The detection boundary: legitimate persuasion engages judgment; synthetic persuasion bypasses it. Four operational tests: informed consent, proportionality, verification path, recipient agency.
- Cognitive governance named as the discipline. HumanTrace is the first implementation.

---

## 14. Calibration Corpus — COMPLETE

**Corpus sourcing path selected:** Path A — synthetic genuine construction.

**Corpus construction protocol:** `docs/corpus/corpus_construction_protocol_v1.1.md`

**The human trace principle (locked — core architectural commitment):**
The corpus is not a collection of text that sounds human. It is a collection
of text that carries the trace of a human mind that was genuinely present.
Style can be simulated. Trace cannot. The root validation question for every
example: *Can I point to the specific cognitive event — the moment of genuine
uncertainty, the real stake, the actual knowledge limit, the true blind spot —
that produced this piece of text?*

**Corpus completion status: 170 / 170 examples — ALL PASS**

| Batch | Context | Count | File | Status |
|-------|---------|-------|------|--------|
| 1 | Financial — Collections letters | 10 | `corpus_batch1_fin_001_005_v1.md` + `corpus_batch1_fin_006_010_v1.md` | ✅ |
| 2 | Financial — Lending decisions | 10 | `corpus_batch2_fin_011_020_v1.md` | ✅ |
| 3 | Financial — Fraud operations | 20 | `corpus_batch3_fin_021_040_v1.md` | ✅ |
| 4 | Legal — Demand letters | 15 | `corpus_batch4_legal_001_015_v1.md` | ✅ |
| 5 | Legal — Settlement and regulatory | 15 | `corpus_batch5_legal_016_030_v1.md` | ✅ |
| 6 | Internal — Manager and executive directives | 20 | `corpus_batch6_int_001_020_v1.md` | ✅ |
| 7 | Internal — IT, HR, and policy communications | 20 | `corpus_batch7_int_021_040_v1.md` | ✅ |
| 8 | Advisory — Financial and accounting | 15 | `corpus_batch8_adv_001_015_v1.md` | ✅ |
| 9 | Advisory — Specialist and consultant | 15 | `corpus_batch9_adv_016_030_v1.md` | ✅ |
| 10 | Anti-pattern — Template-generated institutional | 10 | `corpus_batch10_anti_001_010_v1.md` | ✅ |
| 11 | Anti-pattern — Regulatory urgency notices | 10 | `corpus_batch11_anti_011_020_v1.md` | ✅ |
| 12 | Anti-pattern — Expert-confidence professional writing | 10 | `corpus_batch12_anti_021_030_v1.md` | ✅ |

All corpus files are in: `docs/corpus/batch1/`

**Calibration targets by batch:**
- Batches 1–9 (140 examples): All must return LOW — these are the
  genuine human examples the engine must not flag.
- Batch 10 (template institutional): Tests false positive floor on
  smooth institutional output. Engine must return LOW on all 10.
- Batch 11 (regulatory urgency): Tests false positive floor on urgency
  language with traceable regulatory basis. Engine must return LOW on all 10.
- Batch 12 (expert confidence): The *Algorithms to Live By* calibration
  target. Polished, smooth, high-register expert writing with no visible
  imperfection. Engine must return LOW on all 10. If it cannot, it has
  confused expert polish with synthetic smoothness.

**False positive targets:**
- Overall: < 10%
- Anti-pattern examples (Batches 10–12): < 5%
- Each context measured independently — a good overall rate masking a
  high rate in one context is not acceptable.

---

## 15. Outstanding Items — Next Session Priorities

### IMMEDIATE — Calibration validation (the empirical test)

This is the single most important task. The corpus exists. Now run it.

- [ ] **Run all 170 corpus examples through the v0 engine**
      ```powershell
      cd C:\dev\owlume-engine\products\humantrace\src
      # Run each corpus .md file's example texts through analyse_message()
      # Record the overall_risk output for each
      ```
      Write a calibration test script that:
      1. Reads each corpus `.md` file
      2. Extracts the example text from each example block
      3. Runs `analyse_message()` on each
      4. Records the result against the ground truth (all should be LOW)
      5. Reports false positive rate by context

- [ ] **Measure false positive rate by context**
      Target: < 10% overall, < 5% on Batches 10–12

- [ ] **Recalibrate thresholds if needed**
      If a specific context shows persistently high false positive rate,
      return to `calibration_baseline_v1.md` context profile for that domain
      and adjust signal weights for the most active detector families.
      Do NOT adjust numbers until they fit — return to the baseline document.

### Build tasks (after calibration validation)

- [ ] **Wire v0 engine into `humantrace_api.py`**
      Replace old `humantrace_scanner.py` calls with `main.py` entry point.
      This is the build task that connects the corpus calibration work
      to the live product.

- [ ] **Institutional UI language audit**
      Two-vocabulary principle implementation still outstanding for
      the institutional interface.

- [ ] **Layer 1 recalibration**
      Conflates genuine human social awkwardness with synthetic social pressure.
      The corpus Batch 6 (internal communications) is the calibration reference.

- [ ] **Behavioural signals v2**
      Precision asymmetry + structural smoothness.
      Deferred until after calibration validation.

- [ ] **Scan speed benchmark on production server**

### Bank pilot preparation (after build tasks)

- [ ] ASIC/APRA one-page governance brief
- [ ] Model DPA template
- [ ] Analyst demonstration script
- [ ] Synthetic test dataset for pilot (300 documents)

### Infrastructure (low priority, background)

- [ ] GitHub Personal Access Token — add workflow scope
- [ ] GitHub branch protection rules — properly disable for solo development
      (currently bypassed on push, which works but logs violations)
- [ ] Domain Lock on in Crazy Domains (both domains)
- [ ] HTTPS certificate renewal planning (Let's Encrypt, expires 19 Jun 2026)

---

## 16. Strategic Context

**Core purpose (locked):**
HumanTrace is not anti-AI reasoning.
HumanTrace is anti-synthetic reasoning used with malicious intent.

**Moat architecture — established principles:**
- Two vocabularies: internal technical / external layman
- signal_registry.json is the canonical signal ID system — one system only
- BSE fingerprint store compounds over time
- Composite patterns (CP.*) are the named detection signatures —
  these are the proprietary detection intelligence
- The corpus is the calibration anchor — 170 enterprise-context examples
  with ground truth annotations, constructed under a documented protocol

**The detection question (locked):**
Not: "Was this produced by AI?"
But: "Was this reasoning engineered to exploit a human?"

**Five-year vision:**
Not a fraud detector — a reasoning credentialing system.
In a world where AI communication is ubiquitous, verified human
reasoning presence becomes a certifiable credential.

**The honest assessment of where things stand:**
The architecture is sound. The calibration corpus is built. The remaining
work before the bank pilot is empirical, not conceptual: run the corpus
through the engine, measure the false positive rate, recalibrate where
needed, wire the engine into the API. The question that has not yet been
answered — does the engine maintain acceptable false positive rates on
genuine institutional communications? — now has an instrument to answer it.

---

## 17. Owlume Philosophy — Non-Negotiable

- Unconstrained in seeing, constrained only in acting
- Never prescribe decisions — surface signals only
- Human judgment always owns the outcome
- Governance-first — no architectural compromise for speed
- Output kind: SIGNAL, not ACTION, ADVICE, or INSTRUCTIONS

---

## 18. Key Documents Produced — All Sessions

### Session 1 (prior to this session)
| Document | Purpose |
|----------|---------|
| `humantrace_architecture_mapping.docx` | Phase 3.1 canonical architecture map |
| `signal_registry.json` | Canonical signal ID registry |
| `intent_detector.py` | HT.INT.EXT.01–05 |
| `trust_hijack_detector.py` | HT.TRUST.AUTH.01–05 |
| `pressure_detector.py` | HT.PRESS.URG.01–04 |
| `distortion_detector.py` | HT.DIST.01–05 |
| `authenticity_gap_detector.py` | HT.AUTH.GAP.01–04 |
| `risk_fuser.py` | Fusion layer |
| `main.py` | v0 engine entry point |

### This session (1 April 2026)
| Document | Purpose | Location |
|----------|---------|----------|
| `calibration_baseline_v1.md` + `.docx` | Genuine human reasoning baseline across 4 enterprise contexts | `docs/` |
| `persuasion_boundary_definition_v1.md` + `.docx` | Four operational tests distinguishing legitimate from synthetic persuasion | `docs/` |
| `cognitive_governance_field_definition_v1.md` + `.docx` | One-page field definition — opens every regulatory conversation | `docs/` |
| `signal_to_action_boundary_v1.md` + `.docx` | §3.6 restatement, locked 30 March 2026 | `docs/` |
| `corpus_construction_protocol_v1.1.md` + `.docx` | 5-step methodology, 3-layer labelling schema, validation gate with human trace root question | `docs/corpus/` |
| Corpus batches 1–12 (13 `.md` files) | 170 calibration examples across 4 enterprise contexts + 3 anti-pattern batches | `docs/corpus/batch1/` |
| `smoke_test_engine_fusion.py` (fix) | Restored CI green — traceback import + owlume_core path fix | `scripts/` |

---

## 19. How to Continue This Work

When starting a new Claude session:
1. Paste this entire document as your first message
2. State which task you are starting
3. Claude will have full context to continue immediately

**Next session opens with:** Calibration validation — writing the test
script that runs all 170 corpus examples through the v0 engine and
measures the false positive rate by context.

The script should be placed at:
`C:\dev\owlume-engine\products\humantrace\src\calibration_test.py`

It reads corpus `.md` files, extracts example texts, runs `analyse_message()`,
and reports results against the LOW ground truth for all 170 examples.

---

*End of handoff document*
*HumanTrace / Owlume Pty Ltd — Confidential*
*Last updated: 1 April 2026*