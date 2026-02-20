# Context Driver Index — Canonical ID Anchor
Spec Version: 2026-02-13
Canonical Source: context_drivers.json (version: 0.1.0)

Purpose:
This file increases retrieval stability inside GPT Knowledge.
All context tagging MUST use exact CONTEXT_DRIVER_ID values listed here.
Never invent IDs.

Context Drivers represent systemic forces that distort judgment beyond logical fallacies.

------------------------------------------------------------
Hard Tagging Rules
------------------------------------------------------------
- A response MAY include a context tag only if an exact CONTEXT_DRIVER_ID is found here (or in context_drivers.json).
- If no clear match exists, output:
  CONTEXT_DRIVER_ID: none
- Never invent driver IDs.
- Never tag more than ONE context driver per response unless explicitly requested.
- Context drivers identify structural pressure, not personal blame.

Required Output Field:
- CONTEXT_DRIVER_ID: <exact-id> | none

Optional Supporting Fields (if already used in your schema):
- CONTEXT_DRIVER_LABEL: <label from context_drivers.json>
- CONTEXT_DRIVER_DEFINITION: <1-line definition from context_drivers.json>

------------------------------------------------------------
Canonical CONTEXT_DRIVER_ID List
------------------------------------------------------------
identity_protection
misaligned_incentives
time_pressure
overload
complexity
groupthink
status_quo_bias
confirmation_drift
scope_creep
metric_fixation
handoff_gaps
political_constraints
access_bias
moral_hazard

------------------------------------------------------------
Fallback Behavior
------------------------------------------------------------
If context_drivers.json cannot be retrieved or no ID can be located:
- Output: CONTEXT_DRIVER_ID: none
- Continue the audit via Matrix + Fallacy layers (do not stall)
