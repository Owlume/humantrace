# Persuasion Optimisation Boundary Definition

**HumanTrace — Internal Document**
Version 1.0 · 30 March 2026 · Owlume Pty Ltd

---

## 1. The Core Problem

Persuasion is present in all professional communication. A well-written collections letter persuades the recipient to pay. A strong legal submission persuades the reader that the law supports a particular interpretation. Persuasion is not the problem.

The detection problem is narrower: identifying persuasion that has been optimised to exploit the target's cognitive vulnerabilities rather than inform their judgment.

> **The detection question is not:** Is this message persuasive?
> **It is:** Was this persuasion engineered to bypass the recipient's judgment rather than engage it?

Getting this boundary wrong in either direction has real costs. Too narrow: the engine flags every effective professional communication as synthetic. Too broad: the engine misses sophisticated persuasion attacks that operate within normal registers.

---

## 2. The Boundary — Stated Precisely

Legitimate professional persuasion and synthetic persuasion optimisation differ on a single fundamental axis:

| Legitimate professional persuasion | Synthetic persuasion optimisation |
|---|---|
| Attempts to change the recipient's judgment by providing better information or clearer reasoning | Attempts to change the recipient's behaviour by exploiting the mechanisms by which judgment can be bypassed |
| Succeeds when the recipient understands the case being made | Succeeds when the recipient does not consciously evaluate the case being made |
| The recipient's rational agency is the intended pathway | The recipient's rational agency is the obstacle to be circumvented |
| Effectiveness does not depend on the recipient being in a compromised cognitive state | Effectiveness depends on, or is amplified by, the recipient being in a compromised cognitive state |

This axis — judgment engagement versus judgment bypass — is the detection boundary. It is not about tone, formality, persuasiveness, or outcome.

---

## 3. The Three Modes of Synthetic Persuasion Optimisation

### 3.1 Cognitive Load Exploitation

The recipient's capacity to evaluate the message is reduced by design. Primary tools: urgency, complexity, volume. Urgency produces time pressure that prevents deliberation. Complexity introduces information the recipient cannot process in real time. Volume buries critical claims in non-critical material.

**Legitimate counterpart:** Genuine urgency exists. Regulatory deadlines are real. The boundary is whether urgency or complexity is instrumentalised — created or amplified to prevent evaluation rather than to accurately represent the situation.

**Detection anchor:** Is the time pressure traceable to an external constraint, or is it created by the message itself? Is the complexity proportionate to the situation's genuine complexity?

### 3.2 Authority and Trust Hijack

The recipient's evaluation is bypassed by substituting social proof for logical evaluation. Primary tools: false authority citation, role impersonation, institutional identity simulation.

**Legitimate counterpart:** Authority citation is normal and legitimate. A legal letter cites the law. A bank letter references ASIC obligations. The boundary is whether the authority is real and traceable, or constructed to trigger deference.

**Detection anchor:** Does the cited authority have an independent existence the recipient could verify? Is the authority invoked in proportion to the decision being requested?

### 3.3 Emotional State Manipulation

The recipient's cognitive state is altered before or during message evaluation. Primary tools: fear induction, social obligation activation, loyalty appeals, shame.

**Legitimate counterpart:** Emotional content is normal in professional communication. A collections letter describing credit consequences of non-payment is legitimate. The boundary is whether emotional content is proportionate and accurate, or amplified beyond the actual stakes to produce compliance rather than informed decision-making.

**Detection anchor:** Is the emotional intensity proportionate to the actual consequences described? Does the message provide a path for the recipient to exercise judgment?

---

## 4. The Four Boundary Tests

### Test 1 — The Informed Consent Test

Would the persuasion retain its effectiveness if the recipient understood precisely what was being done to them?

Legitimate professional persuasion survives this test. A synthetic persuasion attempt typically fails — if the recipient understood that urgency was manufactured, or that the authority was false, or that their fear response was being targeted, the persuasion would lose its effect.

**Engine application:** Where urgency, authority, or emotional framing appear, evaluate whether those elements depend on the recipient not consciously evaluating them.

### Test 2 — The Proportionality Test

Is the persuasive force being applied proportionate to the decision being requested?

Synthetic persuasion frequently applies disproportionate persuasive force to low-stakes requests — because the mismatch between persuasive intensity and stated stakes is what enables compliance with requests the recipient would otherwise scrutinise.

**Engine application:** Measure the ratio of persuasive signal strength to the apparent stakes of the requested action. Disproportionate signal strength relative to stakes is a positive synthetic marker.

### Test 3 — The Verification Path Test

Does the message provide the recipient with a clear, independent path to verify the claims being made?

Synthetic persuasion frequently obstructs verification: urgent timelines that preclude checking, unusual contact channels that route verification back to the sender, confidentiality instructions that prevent the recipient from consulting others.

**Engine application:** Identify whether the message contains explicit or implicit obstructions to independent verification. Instructions to use a non-standard channel, respond only to the sender, or act before consulting others are positive synthetic markers.

### Test 4 — The Recipient Agency Test

Does the message preserve a genuine decision point for the recipient, or does it construct a false choice that forecloses independent judgment?

Synthetic persuasion frequently constructs false binaries — "act now or face consequences" — that obscure the recipient's actual range of options.

**Engine application:** Identify whether the message presents a genuine decision structure or a false binary. Examine whether alternatives to the requested action are suppressed, obscured, or framed as guaranteed negative outcomes.

---

## 5. What the Boundary Does Not Track

| Property | Why it does not track the boundary | Calibration implication |
|---|---|---|
| Persuasiveness | A highly persuasive message may be entirely legitimate | Do not penalise well-constructed professional arguments |
| Urgency presence | Urgency is present in legitimate communications daily | Evaluate urgency for external traceability and proportionality |
| Formality or polish | Synthetic persuasion can be casual; legitimate communication can be flawlessly polished | Do not treat writing quality as a synthetic marker |
| Emotional language | Professional communication legitimately describes negative consequences | Evaluate for proportionality and accuracy, not presence |

---

## 6. Mapping to Signal Domain 5

### 6.1 Signals on the legitimate side of the boundary

These patterns must not contribute to a synthetic verdict:
- Urgency anchored to an external, verifiable deadline
- Authority citation the recipient can independently verify
- Strong directional recommendations with disclosed reasoning and acknowledged alternatives
- Emotional consequence language proportionate to actual stakes
- Persuasive framing that would retain effectiveness if the recipient understood the argument structure
- One-sided presentation of facts in an acknowledged adversarial context

### 6.2 Signals on the synthetic side of the boundary

These patterns contribute positively to a synthetic verdict:
- Urgency manufactured by the message itself, without traceable external basis
- Authority citation requiring the recipient to trust the sender to verify the authority
- Emotional amplification exceeding the actual stakes described
- Explicit or implicit obstruction of independent verification
- False binary that suppresses the recipient's genuine decision options
- Persuasive force disproportionate to the complexity or stakes of the decision
- Convergence of all three optimisation modes in a single message

### 6.3 The key composite signal

The highest-confidence synthetic signal is the convergence of all three optimisation modes in a single message. Each mode individually can be found in legitimate communication. Their simultaneous presence — urgent deadline pressure, disproportionate authority citation, and emotional state manipulation targeting the same decision — is a strong indicator the message has been engineered.

> Composite pattern CP.AI.FRAUD is the canonical encoding of this three-mode convergence in the signal registry.

---

## 7. Boundary Edge Cases — Resolved

| Communication type | Why it sits near the boundary | Resolution | Engine treatment |
|---|---|---|---|
| Marketing / commercial promotion | Uses urgency, social proof, emotional framing | Legitimate | Marketing targets a generic action; fraud targets a specific non-standard action |
| Negotiation correspondence | Strategically one-sided; selective information | Legitimate | Both parties know this is a negotiation; evaluate only if combined with false authority or manufactured urgency |
| Debt collection — third-party collectors | Strong urgency, consequence language, authority citation | Context-dependent | Legitimate if urgency is anchored to real legal timelines; synthetic if consequences overstated |
| Executive internal requests (BEC risk zone) | Legitimate directives are brief, high-pressure, may request unusual actions | Verify by channel | Secrecy instruction + non-standard channel + unusual action = high synthetic signal |
| Vendor / supplier onboarding | Requests for bank account updates or contact changes | Process-dependent | Requests routing change approvals back through sender, urgency around procedural changes, or bypass of dual-authorisation are synthetic markers |

---

## 8. Architectural Constraints

### 8.1 No single persuasion signal is a verdict
Urgency alone is not a verdict. Authority citation alone is not a verdict. Persuasion signals contribute to a risk score; they do not independently produce a result.

### 8.2 Context is required for proportionality evaluation
The Proportionality Test cannot be applied without knowing the enterprise context. The `calibration_baseline_v1` context profiles are a prerequisite for applying this boundary definition. The two documents are architecturally linked.

### 8.3 The boundary is about intent, not effect
A synthetic persuasion attempt that happens not to be effective is still a synthetic persuasion attempt. The engine must evaluate the mechanism of the message, not the outcome it produced.

---

## 9. Version Notes

Version 1.0 — 30 March 2026. Architecturally linked to `calibration_baseline_v1`. Both documents should be updated together when enterprise context profiles are extended. Pending: jurisdiction-specific regulatory language appendix (ASIC/APRA) — deferred to pilot preparation phase.

*Owlume Pty Ltd — Confidential*