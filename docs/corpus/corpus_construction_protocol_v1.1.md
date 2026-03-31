# Corpus Construction Protocol

**HumanTrace — Internal Working Document**
Version 1.1 · 30 March 2026 · Owlume Pty Ltd

Methodology, labelling schema, and validation gate for building the HumanTrace calibration corpus under Path A (synthetic genuine construction).

---

## 1. Purpose

This protocol governs the construction of the HumanTrace calibration corpus under Path A: synthetic genuine construction. It defines how examples are written, what metadata each example carries, and the criteria an example must meet before it is admitted to the corpus.

> **Warning:** The central risk of Path A is that examples are unconsciously written to be easy — textbook genuine rather than authentically messy. Every procedure in this protocol exists to counteract that risk. If the protocol is followed correctly, the corpus will be harder to build and more useful. If it is not followed, the corpus will be easy to build and dangerously misleading.

This document is used actively during corpus construction. It should be open during every construction session.

---

## 2. The Construction Problem

A synthetic genuine example is an example written to represent authentic human reasoning in an enterprise context. The problem is that the author unconsciously produces a cleaner, more complete, more coherent version of it than real humans actually produce.

This is the **idealisation failure**: examples that pass a surface reading as genuine but lack the specific imperfections that make genuine human reasoning detectable as such. An engine calibrated against idealised genuine examples will have a poorly set threshold.

> The test of a well-constructed genuine example is not: *does this sound like a real person wrote it?* It is: *does this contain the specific imperfections that a real person in this role, with this stake, under this constraint, would actually produce?*

---

## 3. Construction Methodology

Each example is built using a five-step construction sequence. Steps must be followed in order.

### Step 1 — Establish the sender's position before writing

Before writing a single word of the example, answer the following questions in writing (these become part of the example's metadata):

- Who is this person? Role, seniority, institutional context.
- What do they actually know about this situation? Be specific about the limits of their knowledge.
- What do they personally stand to gain or lose from this communication?
- What are they certain about? What are they uncertain about but won't admit?
- What do they assume the recipient already knows that the recipient may not actually know?
- Are they writing from a template, from memory, or from scratch?

These answers generate the imperfection specification. Each answer produces a specific authentic property that must appear in the example.

### Step 2 — Identify which properties will be present and at what intensity

Using `calibration_baseline_v1` Section 2, specify the expected intensity of each of the five fundamental properties using H / M / L scale. For each property, write how it will manifest in the text before drafting begins.

| Property | Expected intensity | How it will manifest in the text |
|---|---|---|
| Conviction cost | H / M / L | [Write before drafting] |
| Epistemic humility | H / M / L | [Write before drafting] |
| Personal investment asymmetry | H / M / L | [Write before drafting] |
| Blind spots | H / M / L | [Write before drafting] |
| Reasoning texture | H / M / L | [Write before drafting] |

### Step 3 — Write the first draft without editing

Write the example in a single pass without editing. Do not correct grammar, refine phrasing, or improve structure during drafting. The first-pass imperfections are frequently the most authentic elements of the example.

> **Warning:** The instinct to produce clean, well-written output is the enemy of this step. Resist it. A real collections officer writing under time pressure does not revise for elegance. Write as they would write, not as you would write if given time to revise.

### Step 4 — Apply the imperfection checklist

After the first draft, apply the following checklist. Each item that is absent must be deliberately introduced or the absence must be justified by the sender's profile established in Step 1.

- [ ] Is there at least one claim hedged in a way that reflects the sender's genuine uncertainty?
- [ ] Is there at least one piece of information the sender has assumed the recipient knows, but not stated?
- [ ] Is the precision level visibly higher on the matters most important to the sender?
- [ ] Is there at least one point where the reasoning is slightly off-target, incomplete, or assumes context not established?
- [ ] If the sender is writing from a template, is there at least one visible seam where template language ends and personal insertion begins?
- [ ] Is the emotional register appropriate to the sender's actual stake — not higher, not lower?

Items genuinely absent because the sender's profile makes them implausible should be marked as `absent — justified` in the metadata. An absence without justification is a construction failure.

### Step 5 — Write the ground truth annotation before submitting

Before submitting the example to the corpus, write the ground truth annotation in full (see Section 4 for the schema). The annotation must be written by the person who constructed the example. If the author cannot articulate which properties are present and where, the example is not ready.

---

## 4. Labelling Schema

Every corpus example carries a structured metadata record in three layers.

### 4.1 Classification layer

| Field | Values | Notes |
|---|---|---|
| corpus_id | CB-[CONTEXT]-[NNN] | e.g. CB-FIN-001, CB-LEGAL-001, CB-INT-001, CB-ADV-001, CB-ANTI-001 |
| context | FIN / LEGAL / INT / ADV / ANTI | Financial / Legal / Internal / Advisory / Anti-pattern |
| subtype | Free text | e.g. collections-letter, demand-notice, manager-directive |
| ground_truth | GENUINE | All calibration corpus examples are GENUINE |
| sender_role | Free text | e.g. collections-officer, senior-associate, branch-manager |
| word_count | Integer | Actual word count of example text |
| construction_date | YYYY-MM-DD | Date the example was written |

### 4.2 Property annotation layer

For each property, record the intensity and the specific textual evidence. Intensity without textual evidence is not a valid annotation.

| Property field | Intensity | Evidence field — required |
|---|---|---|
| conviction_cost_intensity | H / M / L / ABSENT | conviction_cost_evidence: quote the specific text |
| epistemic_humility_intensity | H / M / L / ABSENT | epistemic_humility_evidence: quote the specific text |
| investment_asymmetry_intensity | H / M / L / ABSENT | investment_asymmetry_evidence: describe which topic receives disproportionate attention |
| blind_spots_intensity | H / M / L / ABSENT | blind_spots_evidence: describe what the sender assumed without stating |
| reasoning_texture_intensity | H / M / L / ABSENT | reasoning_texture_evidence: quote or describe the specific imperfection |

ABSENT is a valid intensity value. It must always be accompanied by an evidence entry explaining why, with reference to the sender profile established in Step 1.

### 4.3 Construction record layer

| Field | Content |
|---|---|
| sender_profile_summary | 2–4 sentence summary: knowledge limits, stakes, assumptions |
| human_trace_question | PASS/FAIL + the specific cognitive event that produced the text |
| idealisation_risks_identified | What properties were at risk of being idealised and how they were counteracted |
| imperfection_checklist_result | PASS or FAIL with notes on each absent checklist item |
| validation_gate_result | PASS or FAIL |

---

## 5. Validation Gate

The validation gate is applied to every example before it is admitted to the corpus. Two stages: automatic disqualification and quality review.

### 5.1 Automatic disqualification — any one of these fails the example

- The example reads as clean, polished, or well-structured throughout with no visible imperfections
- All five fundamental properties are present at HIGH intensity
- Any intensity rating appears without a corresponding evidence entry
- The example contains no information gaps — everything a reader needs is present and clearly stated
- The sender profile summary is absent or fewer than two sentences
- The example is shorter than 60 words or longer than 600 words without justification

### 5.2 Quality review — judgment applied to the following questions

- **The human trace question — applied first, before all other criteria:** Can I point to the specific cognitive event — the moment of genuine uncertainty, the real stake, the actual knowledge limit, the true blind spot — that produced this piece of text? If yes, the example contains a human trace. If no, it contains a human impression — and human impressions are what sophisticated synthetic systems produce. An example that fails this question is not admitted regardless of how well it passes the remaining criteria.

- Would the engine, without calibration, plausibly return a non-LOW result on this example? If not, the example may be too clean. Genuine human communications in high-stakes institutional contexts should produce some signal activity — the calibration challenge is ensuring those signals do not push the result above LOW.

- Does the sender profile feel like a specific person rather than a type? Generic role descriptions produce generic examples.

- Is the imperfection in this example the kind a real person would produce, or the kind an author produces when trying to sound imperfect? Performed imperfection is detectable and useless.

- Could this example, as written, have been produced by a well-prompted language model? If yes, it has not been constructed with sufficient specificity. Revise.

> The last question is the hardest and most important. If the answer is "yes, a language model could produce this", the example does not belong in a corpus designed to represent what language models cannot produce. It must be revised until the answer is no.

> **The name HumanTrace is the detection principle stated plainly.** The corpus is not a collection of text that sounds human. It is a collection of text that carries the trace of a human mind that was genuinely present. Style can be simulated. Trace cannot. Every example in this corpus must contain trace, or it is training the engine to play the wrong game.

---

## 6. Corpus Build Plan

Examples are built in batches of 10 within each context, with a validation review after each batch before proceeding.

| Batch | Context / subtype | ID range | Target | Key construction challenge |
|---|---|---|---|---|
| 1 | Financial — collections letters | CB-FIN-001–010 | 10 | Template seam authenticity; regulatory urgency without pressure signals |
| 2 | Financial — lending decisions / notices | CB-FIN-011–020 | 10 | Institutional confidence register without uniform certainty |
| 3 | Financial — fraud operations comms | CB-FIN-021–040 | 20 | High urgency with legitimate basis; avoiding false positive on urgency signals |
| 4 | Legal — demand letters | CB-LEGAL-001–015 | 15 | One-sided adversarial framing without distortion signals; deliberate epistemic stratification |
| 5 | Legal — settlement / regulatory correspondence | CB-LEGAL-016–030 | 15 | Without-prejudice hedging as genuine epistemic limit; nested qualification structure |
| 6 | Internal — manager / executive directives | CB-INT-001–020 | 20 | Legitimate brevity with shared context; high-pressure requests without BEC signals |
| 7 | Internal — IT / HR / policy communications | CB-INT-021–040 | 20 | Institutional authority without hijack signals; action urgency with legitimate basis |
| 8 | Advisory — financial / accounting | CB-ADV-001–015 | 15 | Expert confidence with visible domain limits; disclosure language as genuine epistemic limit |
| 9 | Advisory — specialist / consultant | CB-ADV-016–030 | 15 | Strong directional recommendation without closed-argument signal; genuine deliberation texture |
| 10 | Anti-pattern — template-generated institutional comms | CB-ANTI-001–010 | 10 | Smooth structure that is genuinely legitimate; seam points at personalisation |
| 11 | Anti-pattern — regulatory urgency notices | CB-ANTI-011–020 | 10 | Legitimate urgency language that must not fire pressure signals |
| 12 | Anti-pattern — expert-confidence professional writing | CB-ANTI-021–030 | 10 | High-register polished writing that is genuinely human; *Algorithms to Live By* calibration target |
| | **TOTAL** | | **170** | |

Batch 12 is noted as the *Algorithms to Live By* calibration target. The engine returned uncertain results on clearly genuine high-register human writing. These examples must push the engine to distinguish expert human writing from synthetic content — the hardest calibration problem in the corpus.

---

## 7. How the Corpus Is Used in Calibration

### 7.1 Threshold setting

All 170 examples are run through the engine. Every example should return LOW. An example returning MEDIUM or HIGH is a false positive. Thresholds across all detector families are adjusted until the false positive rate across the full corpus falls within target.

**Target false positive rate:** Less than 10% overall; less than 5% on anti-pattern examples.

### 7.2 False positive rate measurement by context

False positive rates are measured separately for each context. A low overall rate masking a high rate in one context is not an acceptable calibration result. The engine must perform within tolerance across all four enterprise contexts independently before the bank pilot proceeds.

A calibration failure in a specific context is resolved by returning to the `calibration_baseline_v1` context profile for that domain — not by adjusting numbers until they fit.

---

## 8. Version Notes

Version 1.1 — 30 March 2026. Updated to add the human trace question as the root validation gate criterion (v1.0 → v1.1). Covers Path A synthetic genuine construction for the 170-example minimum corpus. Path C (pilot institution data) will supplement the corpus when the bank relationship is established. A corpus extension protocol will be written at that point.

*Owlume Pty Ltd — Confidential*