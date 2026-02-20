# Questioncraft Matrix — Canonical ID Index
Spec Version: 2026-02-13

This index defines all canonical MODE_ID and PRINCIPLE_ID values.
All classifications must use exact IDs listed here.
No alternative IDs are permitted.

------------------------------------------------------------
M1-ANALYTICAL — Analytical Mode
------------------------------------------------------------
P1-AN-EVIDENCE_VALIDATION
P2-AN-ASSUMPTION
P3-AN-EVIDENCE_SIGNAL
P4-AN-RISK
P5-AN-CLARITY
P6-AN-EFFICIENCY
P7-AN-ACTION

------------------------------------------------------------
M2-CRITICAL — Critical Mode
------------------------------------------------------------
P1-CR-ASSUMPTION
P2-CR-STAKEHOLDER
P3-CR-EVIDENCE
P4-CR-RISK
P5-CR-CLARITY
P6-CR-EFFICIENCY
P7-CR-ACTION

------------------------------------------------------------
M3-CREATIVE — Creative Mode
------------------------------------------------------------
P1-CRV-EXPLORATION
P2-CRV-ASSUMPTION_SHIFT
P3-CRV-SIGNAL
P4-CRV-RISK_REFRAME
P5-CRV-CLARITY_METAPHOR
P6-CRV-EFFICIENCY_INVERSION
P7-CRV-ACTION_BOLD

------------------------------------------------------------
M4-REFLECTIVE — Reflective Mode
------------------------------------------------------------
P1-RF-ROOT_CAUSE
P2-RF-BIAS
P3-RF-EVIDENCE_TRUST
P4-RF-RISK_MEMORY
P5-RF-CLARITY_AVOIDANCE
P6-RF-EFFICIENCY_EGO
P7-RF-ACTION_IDENTITY

------------------------------------------------------------
M5-GROWTH — Growth Mode
------------------------------------------------------------
P1-GR-ASSUMPTION_TEST
P2-GR-EVIDENCE_ACCELERATOR
P3-GR-RISK_SAFE_EXPANSION
P4-GR-CLARITY_UNLOCK
P5-GR-EFFICIENCY_RECYCLE
P6-GR-ACTION_EXPERIMENT

------------------------------------------------------------

Classification Rule:
- Every response must include exactly one MODE_ID.
- Every response must include exactly one PRINCIPLE_ID.
- PRINCIPLE_ID must belong to the selected MODE_ID.
- IDs must match exactly as written.
- No invented IDs allowed.

If no matching ID is found, respond:
NEEDS_KNOWLEDGE_LOOKUP
