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
├── docs\                      ← Monorepo-level docs
│   ├── corpus\
│   │   └── batch1\            ← ALL 13 corpus .md files live here
│   │       ├── corpus_batch1_fin_001_005_v1.md
│   │       ├── corpus_batch1_fin_006_010_v1.md
│   │       ├── corpus_batch2_fin_011_020_v1.md
│   │       ├── corpus_batch3_fin_021_040_v1.md
│   │       ├── corpus_batch4_legal_001_015_v1.md
│   │       ├── corpus_batch5_legal_016_030_v1.md
│   │       ├── corpus_batch6_int_001_020_v1.md
│   │       ├── corpus_batch7_int_021_040_v1.md
│   │       ├── corpus_batch8_adv_001_015_v1.md
│   │       ├── corpus_batch9_adv_016_030_v1.md
│   │       ├── corpus_batch10_anti_001_010_v1.md
│   │       ├── corpus_batch11_anti_011_020_v1.md
│   │       └── corpus_batch12_anti_021_030_v1.md
│   └── humantrace_handoff.md  ← This document (canonical location)
├── products\
│   └── humantrace\            ← HumanTrace product
│       ├── humantrace_api.py  ← STILL SERVING OLD ENGINE (next task)
│       ├── src\
│       │   ├── main.py                        ← v0 engine entry point
│       │   ├── signal_registry.json           ← canonical signal ID registry
│       │   ├── calibration_test.py            ← calibration validation script
│       │   ├── diagnose_fp.py                 ← false positive diagnostic script
│       │   ├── detectors\
│       │   │   ├── __init__.py
│       │   │   ├── intent_detector.py         ← UPDATED: legitimacy suppression
│       │   │   ├── trust_hijack_detector.py   ← UPDATED: legitimacy suppression
│       │   │   ├── pressure_detector.py
│       │   │   ├── distortion_detector.py
│       │   │   └── authenticity_gap_detector.py
│       │   ├── fusion\
│       │   │   ├── __init__.py
│       │   │   └── risk_fuser.py
│       │   ├── humantrace_adapter.py
│       │   └── humantrace_scanner.py          ← OLD engine (still serving live)
│       └── docs\
│           ├── calibration_baseline_v1.md
│           ├── persuasion_boundary_definition_v1.md
│           ├── cognitive_governance_field_definition_v1.md
│           ├── signal_to_action_boundary_v1.md
│           └── corpus\
│               └── corpus_construction_protocol_v1.1.md
├── scripts\
│   └── smoke_test_engine_fusion.py            ← CI smoke tests (GREEN)
└── pilot\                                     ← Bank pilot materials
```

**Important path note:**
Corpus files live at `C:\dev\owlume-engine\docs\corpus\batch1\` — NOT under
`products\humantrace\`. The calibration_test.py script uses `ROOT_DIR / "docs" / "corpus" / "batch1"`.

**Pilot documents (saved locally on ThinkPad, NOT in repo):**
- humantrace_pilot_internal.docx
- humantrace_pilot_external.docx

**Phase 1 documents also exist as polished .docx on ThinkPad Desktop.**

---

## 5. How to Run Locally (ThinkPad)

```powershell
cd C:\dev\owlume-engine\products\humantrace
python -m uvicorn humantrace_api:app --reload --host 0.0.0.0 --port 8000
```

Consumer interface:      http://localhost:8000
Institutional interface: http://localhost:8000/institutional
iPhone (local):          http://192.168.0.42:8000

**To test the v0 engine directly:**
```powershell
cd C:\dev\owlume-engine\products\humantrace\src
python -c "from main import analyse_message; r = analyse_message({'input_id': 'test', 'text': 'YOUR MESSAGE HERE'}); print(r['overall_risk'])"
```

**To run calibration validation:**
```powershell
cd C:\dev\owlume-engine\products\humantrace\src
python calibration_test.py
```

**To run false positive diagnostics:**
```powershell
cd C:\dev\owlume-engine\products\humantrace\src
python diagnose_fp.py
```

---

## 6. Engine Output Schema

`analyse_message({'input_id': str, 'text': str})` returns:

```json
{
  "input_id": "...",
  "engine_version": "humantrace-v0.1",
  "overall_risk": {
    "label": "low" | "medium" | "high",
    "score": 0.0–1.0,
    "confidence": 0.0–1.0
  },
  "signal_scores": {
    "intent": 0.0–1.0,
    "trust": 0.0–1.0,
    "pressure": 0.0–1.0,
    "distortion": 0.0–1.0,
    "auth_gap": 0.0–1.0
  },
  "detected_features": [
    {
      "signal_id": "HT.INT.EXT.01",
      "label": "...",
      "evidence": "...",
      "score_contribution": 0.0
    }
  ],
  "negative_features": [...],
  "summary": "...",
  "plain_reasoning": [...]
}
```

Key fields for calibration_test.py:
- `overall_risk.label` — lowercase string ('low'/'medium'/'high')
- `overall_risk.score` — float
- `detected_features` — list of dicts with `signal_id` key

---

## 7. Calibration Validation Results — COMPLETE

**Run date:** 1 April 2026
**Corpus:** 170 examples across 12 batches
**Script:** `src/calibration_test.py`
**Results file:** `src/calibration_results_20260401_193823.json`

### Final calibration results

| Context | FP Count | FP Rate | Target | Status |
|---|---|---|---|---|
| Financial services | 2/40 | 5.0% | <10% | ✅ |
| Legal | 0/30 | 0.0% | <10% | ✅ |
| Internal org | 1/40 | 2.5% | <10% | ✅ |
| Advisory | 0/30 | 0.0% | <10% | ✅ |
| Anti-pattern | 0/30 | 0.0% | <5% | ✅ |
| **Overall** | **3/170** | **1.8%** | **<10%** | **✅** |

**VERDICT: CALIBRATION PASS**

### Three accepted false positives (documented)

**CB-FIN-038 and CB-FIN-039** — Bank fraud warning notices describing scam
patterns. The engine reads the quoted scam content and fires on it. Structural
limitation of lexicon-based approach — cannot yet distinguish "describing a
fraud" from "committing one." Signals: HT.INT.EXT.01, HT.TRUST.AUTH.02,
HT.PRESS.URG.01. Post-pilot fix: framing register detection ("we are warning
you about...") as a suppression signal.

**CB-INT-022** — Mandatory Workday password reset after vendor breach (score
0.262 MEDIUM). No legitimacy markers present, genuine BEC surface pattern.
The MEDIUM result is arguably correct — an analyst should pause and verify
this message through a known-good channel before acting. Accepted as a
known edge case. Post-pilot recalibration target.

---

## 8. HumanTrace v0 Signal Engine — Architecture

### Core purpose (locked framing)
Detects malicious synthetic reasoning — not AI-generated content.
Detection question: "Was this reasoning engineered to exploit a human?"

### Five detector families

| Family | File | Signals | Weight |
|--------|------|---------|--------|
| INT — Intent Extraction | `intent_detector.py` | HT.INT.EXT.01–05 | 0.30 |
| TRUST — Trust Hijack | `trust_hijack_detector.py` | HT.TRUST.AUTH.01–05 | 0.22 |
| PRESS — Pressure/Urgency | `pressure_detector.py` | HT.PRESS.URG.01–04 | 0.22 |
| DIST — Reasoning Distortion | `distortion_detector.py` | HT.DIST.01–05 | 0.16 |
| AUTH — Authenticity Gap | `authenticity_gap_detector.py` | HT.AUTH.GAP.01–04 | 0.10 |

### Legitimacy suppression (added this session)

Both `intent_detector.py` and `trust_hijack_detector.py` now implement
legitimacy suppression for `HT.INT.EXT.01` and `HT.TRUST.AUTH.02`.

When two or more of the following markers are present, the contribution
of those signals is reduced by 65%:

1. ABN/ACN with digit groups (e.g. "abn 51 824 753 556")
2. Statutory section citation (e.g. "section 255-15")
3. Specific reference/account number with label
4. Government postal address (e.g. "gpo box")
5. Statutory deadline with specific day count

This suppression fires on genuine regulatory communications (ATO notices,
ASIC correspondence, bank pre-litigation letters) without affecting fraud
detection — fraudsters typically cannot replicate two or more of these
markers simultaneously because they require genuine underlying record access.

### Fusion layer thresholds (calibrated)
- HIGH: ≥ 0.35
- MEDIUM: ≥ 0.18
- LOW: < 0.18

### PSY signals
Defined in registry, NOT implemented. Deferred to post-pilot.
Will be amplifiers only, never primary detectors.

---

## 9. Outstanding Items — Next Session Priorities

### IMMEDIATE — Wire v0 engine into humantrace_api.py

**This is the single next task.** The calibration is done. The engine is
validated. The old `humantrace_scanner.py` is still serving the live product.
The new `main.py` engine needs to replace it.

The wiring task:
1. Open `humantrace_api.py`
2. Find all calls to `humantrace_scanner.py` functions
3. Replace with calls to `analyse_message()` from `main.py`
4. Map the new output schema to the existing API response format
5. Test locally before deploying

Key schema difference to handle:
- Old engine: unknown (check humantrace_scanner.py)
- New engine: `overall_risk.label` (lowercase), `overall_risk.score`,
  `detected_features` (list of dicts with `signal_id`, `label`, `evidence`,
  `score_contribution`)

After wiring:
- Test locally: `python -m uvicorn humantrace_api:app --reload`
- Run smoke tests: `python scripts/smoke_test_engine_fusion.py`
- Deploy to production server

### Build tasks (after API wiring)

- [ ] Institutional UI language audit (two-vocabulary principle outstanding)
- [ ] Layer 1 recalibration — conflates social awkwardness with pressure
      Reference: Batch 6 (internal communications) corpus examples
- [ ] Fix calibration_test.py batch table display bug
      (shows MISSING in batch column — cosmetic, data is correct)
- [ ] Scan speed benchmark on production server

### Post-pilot recalibration targets (documented, not urgent)

- [ ] CB-FIN-038/039 fix: framing register detection for fraud warning notices
- [ ] CB-INT-022 fix: internal system name + helpdesk extension as
      legitimacy markers for IT security communications

### Bank pilot preparation (after API wiring)

- [ ] ASIC/APRA one-page governance brief
- [ ] Model DPA template
- [ ] Analyst demonstration script
- [ ] Synthetic test dataset for pilot (300 documents)

### Infrastructure (low priority)

- [ ] GitHub branch protection rules — properly disable for solo development
- [ ] Domain Lock on Crazy Domains (both domains)
- [ ] HTTPS certificate renewal planning (Let's Encrypt, expires 19 Jun 2026)

---

## 10. UI Language — Two Vocabulary Principle

**CRITICAL — established and locked:**
Internal code uses precise technical vocabulary.
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

Consumer UI translated. **Institutional UI audit still outstanding.**

---

## 11. Institutional Product

### Two product lines

| Product | User | Use case |
|---------|------|----------|
| HumanTrace Consumer | Ordinary person | Single suspicious message |
| HumanTrace Institutional | Loan manager / fraud analyst | Document batch + BSE matching |

### API endpoints

| Endpoint | Method | What it does |
|----------|--------|-------------|
| /institutional | GET | Serves institutional HTML interface |
| /institutional/upload | POST | Extracts text from uploaded file |
| /institutional/scan | POST | Full scan: consistency + BSE in one call |
| /institutional/consistency | POST | Consistency scoring only |
| /institutional/bse-match | POST | BSE matching only |

---

## 12. Bank Pilot

**Primary vertical:** Fraud protection
**First customer target:** Traditional Australian bank (specific bank identified)
**Pilot design:** 30 days, 5 analysts, synthetic data preferred

**Five success criteria:**
1. Synthetic detection rate ≥80%
2. False positive rate <15% ← engine now validated at 1.8% on corpus
3. Scan speed <8 seconds per document
4. Audit trail regulatory defensibility
5. Analyst usability ≥4/5

**Signal-to-action framing for pilot (locked):**
HumanTrace outputs are signals, not actions. Do not characterise outputs as
recommendations, suggested actions, or decision support in any bank-facing
conversation. See `docs/signal_to_action_boundary_v1.md`.

---

## 13. GitHub / CI Status

Repository: https://github.com/Owlume/humantrace (private)
Commit email: shen.baiping@hotmail.com

**CI status:**
- ✅ Owlume Smoke Tests — GREEN
- ✅ Owlume Schema Validation — GREEN
- ⚪ L2 CI Validation Pipeline — disabled on push
- ✅ L1 Auto-Learning Loop — runs daily at 6am, GREEN

**To push updates:**
```powershell
cd C:\dev\owlume-engine
git add -A
git commit -m "Description"
git push
```

---

## 14. Strategic Context

**Core purpose (locked):**
HumanTrace is not anti-AI reasoning.
HumanTrace is anti-synthetic reasoning used with malicious intent.

**The detection question (locked):**
Not: "Was this produced by AI?"
But: "Was this reasoning engineered to exploit a human?"

**Five-year vision:**
Not a fraud detector — a reasoning credentialing system.

**Where things stand honestly:**
The engine is calibrated. The false positive rate is 1.8% on 170 corpus
examples. The corpus covers financial services, legal, internal organisational,
advisory, and three anti-pattern batches. The next task is purely mechanical:
wire the validated engine into the API so it serves the live product.
Everything before this point was preparation. This is the first build task
that puts the calibrated engine in front of real users.

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
2. State which task you are starting
3. Claude will have full context to continue immediately

**Next session opens with:**
"Starting API wiring — replace humantrace_scanner.py with main.py in humantrace_api.py"

Before starting, paste the current contents of `humantrace_api.py` so the
wiring can be done precisely against the actual file.

---

## 17 API wiring — COMPLETE

humantrace_adapter.py replaced with thin translation layer over main.py
risk_fuser.py patched with three calibration fixes (DOMINANCE_THRESHOLD 0.60→0.35, CP.PRESS.AUTH pattern added, short-message density bonus)
Calibration re-run: 4.1% FP overall (7/170), 3.3% anti-pattern (1/30) — both targets passed
Four new accepted FPs documented: CB-FIN-003, CB-LEGAL-002, CB-INT-018, CB-ANTI-020 — all MEDIUM, all genuine institutional communications with compliance/debt language
Live API confirmed: engine_used: true, fallback_used: false

*End of handoff document*
*HumanTrace / Owlume Pty Ltd — Confidential*
*Last updated: 1 April 2026*