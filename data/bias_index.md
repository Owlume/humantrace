# Bias / Fallacy Index — Canonical ID Anchor
Spec Version: 2026-02-13
Canonical Source: fallacies.json (spec_version: 2025-10-08)

Purpose:
This file exists to increase retrieval stability inside GPT Knowledge.
All fallacy tagging MUST use exact FALLACY_ID values listed here.
Never invent IDs.

------------------------------------------------------------
Hard Tagging Rules
------------------------------------------------------------
- A response MAY include a fallacy tag only if an exact FALLACY_ID is found in this index (or in fallacies.json).
- If no clear match exists, output:
  FALLACY_ID: none
- Never invent fallacy IDs.
- Never tag more than ONE fallacy per response unless the user explicitly requests multi-tagging.
- The fallacy tag is a blind-spot label only; it must not be used to persuade, scold, or diagnose.

Required Output Field:
- FALLACY_ID: <exact-id> | none

Optional Supporting Fields (if you already use them elsewhere):
- FALLACY_LABEL: <label from fallacies.json>
- FALLACY_DEFINITION: <1-line definition from fallacies.json>

------------------------------------------------------------
Canonical FALLACY_ID List
------------------------------------------------------------
false_dilemma
appeal_to_authority
circular_reasoning
cherry_picking
hasty_generalization
ad_hominem
slippery_slope
post_hoc
straw_man
appeal_to_emotion
bandwagon
red_herring
false_cause
equivocation
appeal_to_tradition
appeal_to_nature
false_analogy
burden_of_proof
no_true_scotsman
appeal_to_ignorance

------------------------------------------------------------
Fallback Behavior
------------------------------------------------------------
If fallacies.json cannot be retrieved or no ID can be located:
- Output: FALLACY_ID: none
- Continue the audit via Matrix + Context Drivers (do not stall)
