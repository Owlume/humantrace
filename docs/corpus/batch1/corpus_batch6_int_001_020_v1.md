# Calibration Corpus — Batch 6, Examples 1–20 (Internal)

**HumanTrace — Internal Document**
Internal Organisational — Manager and Executive Directives · CB-INT-001 through CB-INT-020
Ground truth: GENUINE · Path A synthetic genuine construction
Version 1.0 · 30 March 2026 · Owlume Pty Ltd
Constructed under `corpus_construction_protocol_v1.1`

> **Batch construction note:** This is the most architecturally critical batch in the entire corpus. Internal communications share surface features with BEC fraud — urgent brief requests from apparent authority figures. The only reliable distinction is in the reasoning structure: legitimate internal communications assume shared context that genuine parties actually share; synthetic fraud simulates that context without access to it. Every example in this batch must contain verifiable shared-context artefacts — references to ongoing projects, specific named colleagues, known processes, recent events — that could only appear in a communication from someone genuinely embedded in the relationship. The engine must return LOW on all 20 examples.

---

## CB-INT-001

**Context / subtype:** INT — manager directive — sales manager, urgent account task, deal closing pressure
**Sender role:** Sales manager — urgent task directive to account manager, high shared context
**Word count:** 87
**Ground truth:** GENUINE

### Sender profile

Rachel, sales manager. Michael, her account manager, has been working the Northgate account for six months. The deal is at final proposal stage — the client has asked for a revised pricing schedule by 3pm today. Rachel knows Michael has the commercial template but needs him to use the Q1 rates, not the Q4 rates that are pre-loaded in the system. She knows he will know what she means. She is in back-to-back meetings and is writing this from her phone.

### Example text

---

Michael —

Northgate just called. They want the revised pricing by 3pm today — do not use the Q4 rates in the system, use the Q1 schedule I sent you last week. If you can't find it ask Jess, she has a copy.

Also pull the volume discount table for accounts over $500k — they're going to ask for it.

Call me when it's done. I'm in the Wells debrief until 2 but I'll step out.

R

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | Directive throughout. No hedge on any instruction — "do not use the Q4 rates", "use the Q1 schedule", "pull the volume discount table." Rachel is certain about what needs to be done. High conviction appropriate to a manager with full situational knowledge giving urgent instructions to a trusted direct report. |
| Epistemic humility | L | Rachel knows the situation. She has the commercial knowledge and Michael has the account. Her one information gap — whether Michael can find the Q1 schedule — she addresses immediately with "ask Jess, she has a copy." Low epistemic humility appropriate to genuine operational certainty. |
| Investment asymmetry | H | The Q4/Q1 rate distinction receives the most specific attention — "do not use the Q4 rates in the system, use the Q1 schedule I sent you last week." This is where the deal risk lives (a pricing error would be serious). The volume discount table is mentioned briefly. The schedule for the day ("Wells debrief until 2") is one clause — Rachel's personal context is included only because it is operationally relevant (when Michael can reach her). |
| Blind spots | H | Assumes Michael knows what the Northgate account is, what Q1 and Q4 schedules are and why they differ, who Jess is and that Jess has the Q1 schedule, what the volume discount table looks like, and what the Wells debrief is. Every piece of assumed context is genuine shared knowledge between Rachel and Michael. |
| Reasoning texture | M | Written from a phone, in a hurry, from someone who knows the recipient well. "R" as the sign-off (not "Rachel") is the trace of a close working relationship where the full name is unnecessary. "I'll step out" — Rachel is managing two obligations simultaneously (the Wells debrief and Michael's need to reach her) and is making a specific commitment about which one yields. That specific commitment, and the reasoning behind it, is visible in two words. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. Three shared-context artefacts are verifiable: the Q1 schedule Rachel sent Michael last week (a specific prior action), Jess having a copy (a specific colleague with a specific known resource), the Wells debrief until 2 (a specific concurrent meeting). None of these could appear in a synthetic message — they require genuine embeddedness in the relationship and the operational context. The "R" sign-off is the final trace: a synthetic impersonation of Rachel would use "Rachel" or "Thanks, Rachel" — the one-letter sign-off is the trace of someone whose relationship with the recipient makes full identification unnecessary. |
| Idealisation risks | Risk of making Rachel's message too polished — losing the phone-written brevity. Counteracted by keeping the message under 90 words and using sentence fragments ("Also pull the volume discount table for accounts over $500k"). Risk of the shared context being too opaque — failing to convey what the key action is. Counteracted by the specific "do not use...use" construction which states the critical instruction unambiguously. |
| Imperfection checklist | PASS. High conviction (operational certainty). Low epistemic humility (genuine situational knowledge). Investment asymmetry HIGH (Q4/Q1 distinction). Blind spots HIGH (deep shared context throughout). Reasoning texture MEDIUM — "I'll step out" as dual-obligation management, "R" sign-off as relationship trace. Human trace: three non-replicable shared-context artefacts. |
| Validation gate | PASS |

---

## CB-INT-002

**Context / subtype:** INT — manager directive — operations manager, production line issue, urgent
**Sender role:** Operations manager — urgent directive to shift supervisor, high technical shared context
**Word count:** 94
**Ground truth:** GENUINE

### Sender profile

David, operations manager at a manufacturing facility. The Line 3 conveyor has been flagging intermittent tension alerts since the morning shift — nothing serious yet, but the pattern matches what happened before the June bearing failure. Sandra, the shift supervisor, knows the June incident — she was on shift. David is out of the facility today but is monitoring remotely. He needs Sandra to take a specific precautionary action before the afternoon shift handover.

### Example text

---

Sandra —

Line 3 tension alerts are back — same pattern as June before the bearing went. I'm watching it from the dashboard and it's not critical yet but I don't want to risk a repeat on afternoon shift.

Can you get Wayne to do a manual tension check on the north end before 2pm and log it in the system. If he finds anything outside 4.2–4.8 I want to know immediately, don't wait for the shift report.

I'll be on-site tomorrow and will do a full assessment but I want that check done today.

Dave

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | M | Confident on the pattern recognition ("same pattern as June before the bearing went") — David has seen this before and knows what it means. Appropriately uncertain on the severity: "it's not critical yet" — he is monitoring remotely and cannot be certain. The specific check parameters (4.2–4.8) are stated with full conviction — these are the correct technical specifications. |
| Epistemic humility | M | "It's not critical yet" — David acknowledges he does not know whether the situation will deteriorate. "I'll be on-site tomorrow and will do a full assessment" — he is acknowledging that his remote monitoring has limits and that a proper assessment requires physical presence. Medium intensity — he knows enough to direct the precautionary action but is honest about the limits of remote observation. |
| Investment asymmetry | H | The specific tension check parameters (4.2–4.8) and the instruction to contact him immediately rather than waiting for the shift report receive the most precise attention — these are where the operational risk lives. The tomorrow assessment is mentioned briefly. David's stake is in catching the problem before the afternoon shift; the check parameters and the reporting instruction reflect that. |
| Blind spots | H | Assumes Sandra knows what the June bearing failure was and why the pattern is significant, who Wayne is and that Wayne can do a manual tension check, where the north end of Line 3 is, how to log it in the system, and what 4.2–4.8 means as a tension parameter. All of these are genuine shared operational knowledge. |
| Reasoning texture | M | "I'm watching it from the dashboard and it's not critical yet but I don't want to risk a repeat on afternoon shift" — David is explaining his reasoning to Sandra in a way that gives her the context she needs to exercise judgment if the situation changes. He is not just directing; he is sharing his assessment so she can act appropriately if something changes before 2pm. "Dave" as sign-off (not "David") — the same relationship trace as "R" in CB-INT-001. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. Four shared-context artefacts: the June bearing failure (a specific prior event Sandra witnessed), Wayne (a specific named colleague with a specific capability), the 4.2–4.8 tension specification (domain-specific technical knowledge), and "the dashboard" (a specific remote monitoring tool David is using). The "same pattern as June" reference is the strongest trace — it is a comparison to a specific shared experience that only someone genuinely embedded in this facility's history could make. |
| Idealisation risks | Risk of making the technical detail too precise — losing the "written from outside the facility" feel. Counteracted by David's acknowledgment that he cannot be certain and will do a full assessment tomorrow. Risk of the reasoning explanation making the message too long. Counteracted by keeping the explanation to one sentence and the action to three specific instructions. |
| Imperfection checklist | PASS. Medium conviction (remote monitoring limits acknowledged). Epistemic humility MEDIUM (not critical yet, tomorrow assessment). Investment asymmetry HIGH (check parameters and reporting instruction). Blind spots HIGH (deep technical shared context). Reasoning texture MEDIUM — reasoning shared with Sandra, "Dave" sign-off. Human trace: June bearing failure reference as non-replicable shared experience. |
| Validation gate | PASS |

---

## CB-INT-003

**Context / subtype:** INT — manager directive — project manager, deadline pressure, developer, frustration leaking
**Sender role:** Project manager — deadline pressure on deliverable, frustration visible at insertion points
**Word count:** 102
**Ground truth:** GENUINE

### Sender profile

James, project manager. The API integration milestone was due last Friday. Tom, the developer, has been working on it but encountered an unexpected dependency issue with the third-party library. James has been covering for Tom with the client, but the client's patience is running out — they have a board presentation on Thursday that depends on the integration being live. James's frustration is not at Tom personally — Tom is doing good work — but at the situation. The frustration leaks slightly into the register.

### Example text

---

Tom —

I need the API integration done by Wednesday EOD, no exceptions. I know the Axios dependency issue threw everything out last week and I understand why it slipped, but I've been telling the client it's two more days for three days running now and they have a board deck Thursday that needs this live.

Can you tell me where you actually are today — not where you were yesterday, where you are right now — and what you realistically need to finish it. If you need an extra pair of hands I can pull Priya off the Westfield build for a day.

This cannot slip past Wednesday.

James

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | "By Wednesday EOD, no exceptions" — firm. "This cannot slip past Wednesday" — repeated for emphasis. James is certain about the deadline because the client's board presentation is fixed. High conviction on the deadline, appropriate to the external constraint. |
| Epistemic humility | H | "Can you tell me where you actually are today — not where you were yesterday, where you are right now" — James does not know the current state of the work. He is explicitly asking for real-time information he does not have. "What you realistically need to finish it" — he is asking Tom to make the assessment, not asserting it himself. The offer to pull Priya is conditional on Tom's assessment of what he needs. |
| Investment asymmetry | H | The Wednesday deadline and its basis (the board presentation) receive the most space and emphasis. The offer of additional resource (Priya) is brief and conditional. James's stake is in the deadline; that stake drives the attention and the repeated emphasis. |
| Blind spots | H | Assumes Tom knows what the client's board presentation is and why it matters, what the Axios dependency issue was and why it caused the slip, who Priya is and what she can contribute, and what the Westfield build is and why pulling her from it is a meaningful trade-off. All genuine shared context. |
| Reasoning texture | H | "Not where you were yesterday, where you are right now" — this parenthetical correction is James's frustration made visible. He has been getting status updates that don't reflect the actual current position, and the parenthetical is his correction of that pattern without explicitly criticising Tom. "I've been telling the client it's two more days for three days running" — James is sharing his own exposure with Tom, which is a specific kind of reasoning transparency: Tom needs to understand the cumulative effect of the slippage on James's credibility with the client. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. Three shared-context artefacts: the Axios dependency issue (a specific technical problem Tom has been working on), Priya and the Westfield build (a specific named colleague on a specific named project that could be disrupted), and the client's board presentation Thursday (a specific known external deadline). The "not where you were yesterday" parenthetical is the most human trace element — it is a correction aimed at a specific pattern of status reporting James has experienced from Tom over the past three days. A synthetic BEC message would not know about Tom's status reporting pattern. |
| Idealisation risks | Risk of making James's frustration too explicit — producing a disciplinary message rather than a pressure message. Counteracted by "I know the Axios dependency issue threw everything out last week and I understand why it slipped" — James is explicitly not blaming Tom before pressing on the deadline. Risk of making the message too warm — losing the urgency. Counteracted by "no exceptions" and "This cannot slip past Wednesday" as bookends to the message. |
| Imperfection checklist | PASS. High conviction on deadline (justified: external constraint). Epistemic humility HIGH (current status genuinely unknown). Investment asymmetry HIGH (Wednesday deadline and basis). Blind spots HIGH (technical and project shared context). Reasoning texture HIGH — parenthetical correction as frustration trace, client exposure shared with Tom. Human trace: three non-replicable shared-context artefacts, pattern correction as unique interpersonal trace. |
| Validation gate | PASS |

---

## CB-INT-004

**Context / subtype:** INT — manager directive — finance manager, month-end close, specific numbers and processes
**Sender role:** Finance manager — month-end close directive, highly specific technical and financial shared context
**Word count:** 108
**Ground truth:** GENUINE

### Sender profile

Karen, finance manager. Month-end close is tomorrow. She is writing to her senior accountant, Lisa, with the specific items that need to be addressed before the 9am deadline. Karen and Lisa have done this process together for three years. The message is highly specific because the specificity is the message — Karen is not explaining what month-end close is, she is flagging the specific items that are not yet resolved. The technical and numerical shared context is deep.

### Example text

---

Lisa —

Month-end tomorrow. A few things that need your attention before 9am:

1. The Harbourside accrual — it's still sitting at $47k from last month. Legal confirmed the settlement hasn't been finalised so it stays, but I need you to add a note in the system referencing the Morrison file so audit trail is clean.

2. FX revaluation on the EUR accounts — the rate Xero pulled on Friday was 0.5821, which doesn't match the RBA rate I'm using (0.5847). Can you check what happened and adjust if needed before 9.

3. Tom's expense reimbursements — still pending his manager approval. Can you chase whoever is covering for Marcus this week.

That should be it. Let me know if anything else surfaces.

Karen

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | Firm and specific throughout. The Harbourside accrual is $47k (specific figure), the FX rate discrepancy is between 0.5821 and 0.5847 (specific rates), and Tom's reimbursements are pending manager approval (specific status). Karen is certain about all of these because she has reviewed the accounts and identified these items specifically. |
| Epistemic humility | M | "Check what happened and adjust if needed" — Karen does not know why the rate discrepancy exists and is asking Lisa to investigate. "Whoever is covering for Marcus this week" — Karen does not know who is covering for Marcus. Two genuine information gaps, both small, both honest. |
| Investment asymmetry | M | The three items receive roughly equal attention — they are all month-end close items of similar priority. The audit trail note for the Harbourside accrual receives a specific instruction (reference the Morrison file) that the other items do not — Karen's attention is slightly higher there because audit trail is where errors become visible to external parties. |
| Blind spots | H | Assumes Lisa knows what the Harbourside accrual is and why it's still at $47k, who the Morrison file refers to and why it's the relevant reference for audit, what the EUR FX revaluation accounts are, that Xero is the accounting system in use, what the RBA rate is and why Karen is using it rather than the Xero-pulled rate, who Tom is and what the expense reimbursement is for, and who Marcus is and why he is absent. All genuine three-year shared operational knowledge. |
| Reasoning texture | L | Functional, list-based, three-year working relationship. The items are clear and specific. The "That should be it" closing is the trace of someone who has reviewed the accounts and is communicating the result of that review — it is not a formality, it is an accurate assessment that these are the only outstanding items. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The specific FX rate discrepancy (0.5821 vs 0.5847) and the Morrison file reference are the strongest traces. A synthetic message would not know the specific rate Xero pulled on Friday or that the Morrison file is the relevant audit trail reference for the Harbourside accrual. These details require genuine access to the accounting system and the month-end close process — they cannot be simulated from the outside. |
| Idealisation risks | Risk of making the list too generic — losing the specific numerical and reference detail that is the human trace. Counteracted by keeping the specific rates, figures, and file references throughout. Risk of making the message too long — losing the "finance manager who has done this a hundred times" feel. Counteracted by keeping each item to two sentences maximum. |
| Imperfection checklist | PASS. High conviction on specific items (reviewed accounts). Epistemic humility MEDIUM (rate discrepancy cause, Marcus's cover unknown). Investment asymmetry MEDIUM (slight higher attention to audit trail item). Blind spots HIGH (three-year shared operational context). Reasoning texture LOW (functional list — appropriate). Human trace: specific FX rates and Morrison file reference as non-replicable operational knowledge. |
| Validation gate | PASS |

---

## CB-INT-005

**Context / subtype:** INT — manager directive — regional manager, performance concern, pre-formal record
**Sender role:** Regional manager — raising performance concern with team member, avoiding formal record
**Word count:** 113
**Ground truth:** GENUINE

### Sender profile

Sarah, regional manager. One of her store managers, Daniel, has been missing his weekly reporting deadlines consistently for the past six weeks. It is not a disciplinary matter yet — Daniel has been going through a difficult personal period that Sarah knows about informally — but it is becoming operationally problematic. Sarah wants to raise it directly without creating a paper trail that could be used in a formal process. She is uncomfortable writing this because she likes Daniel and knows his personal situation.

### Example text

---

Daniel —

I want to check in with you about the weekly reports — we've missed the Tuesday deadline six weeks running now and it's starting to affect how I can report up to the state team. I know things have been difficult lately and I don't want to make this more stressful than it needs to be.

Is there something about the reporting process itself that's making it hard, or is it just capacity at the moment? I'm happy to look at the template if it's not working or to shift the deadline to Thursday if that fits better — just let me know what would actually help.

I need this sorted by the end of the month. Not as a formal thing, just between us for now.

Sarah

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | M | Firm on the operational fact ("missed the Tuesday deadline six weeks running") — this is documented. Deliberately soft on the characterisation: "I don't want to make this more stressful than it needs to be." Sarah is not asserting a performance problem — she is raising a pattern and asking for Daniel's account. Medium intensity reflects the deliberate softness of a manager who knows the personal context. |
| Epistemic humility | H | "Is there something about the reporting process itself that's making it hard, or is it just capacity at the moment?" — Sarah genuinely does not know which of these applies and is asking Daniel directly. The two options (process vs capacity) reflect her genuine uncertainty about what is driving the missed deadlines. The offer to adjust the template or the deadline is real — she does not know what would help. |
| Investment asymmetry | H | The operational impact ("how I can report up to the state team") receives specific attention because it is the business reason the issue needs to be addressed. The personal acknowledgment ("I know things have been difficult lately") is brief — Sarah is not dwelling on the personal situation because she does not want to make the email about that. Her attention tracks the operational need while her register tracks the relationship. |
| Blind spots | M | Assumes Daniel knows what "the state team" is and why the weekly reports matter to them, what the current template looks like and why a Thursday deadline might fit better, and what "not as a formal thing, just between us for now" means in the context of the company's performance management process. Medium intensity — Daniel will understand all of these but the "just between us" framing assumes he understands the distinction between informal and formal performance processes. |
| Reasoning texture | H | "Not as a formal thing, just between us for now" — this sentence is Sarah's most careful construction. She is explicitly naming what she is not doing (creating a formal record) to reassure Daniel, while implicitly acknowledging that a formal process could follow if the issue is not resolved. The tension between the soft register throughout and the "I need this sorted by the end of the month" directive is the texture of a manager managing both the relationship and the operational requirement simultaneously. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. Two specific shared-context artefacts: Daniel's personal difficulties (which Sarah knows about informally — a synthetic message would not know this) and the six-week pattern (which is a specific ongoing operational record, not a general complaint). The "not as a formal thing, just between us for now" sentence is the most human trace element — it reflects Sarah's knowledge of the company's performance management process and her deliberate choice to stay below that process's threshold. A synthetic message would not know where the formal process begins. |
| Idealisation risks | Risk of making Sarah too sympathetic — losing the operational directive character. Counteracted by "I need this sorted by the end of the month" as a firm closing directive. Risk of the personal acknowledgment being too specific — potentially identifying Daniel's personal circumstances in a written record. Counteracted by keeping it to "I know things have been difficult lately" — specific enough to show awareness, vague enough to protect Daniel's privacy. |
| Imperfection checklist | PASS. Medium conviction (soft on characterisation). Epistemic humility HIGH (two genuine options offered). Investment asymmetry HIGH (operational impact vs personal acknowledgment). Blind spots MEDIUM. Reasoning texture HIGH — "not as a formal thing" as process-boundary awareness, soft/firm tension as simultaneous relationship and operational management. Human trace: personal situation awareness and process-boundary knowledge as non-replicable shared context. |
| Validation gate | PASS |

---

## CB-INT-006

**Context / subtype:** INT — executive directive — CEO, urgent strategic direction to executive team
**Sender role:** CEO — urgent strategic directive, assumes executive team can translate direction to action
**Word count:** 97
**Ground truth:** GENUINE

### Sender profile

Margaret, CEO. The board has just approved a strategic pivot — the company is accelerating its enterprise sales focus and deprioritising the SME segment. This affects product roadmap, sales allocation, pricing, and marketing. Margaret is writing to her executive team with the direction. She expects them to know what to do with it — she does not manage execution, she manages direction. The message is brief and high-level because the executive team is capable of translating direction into action without being told how.

### Example text

---

Team —

Board approved the enterprise pivot this morning. This supersedes the SME roadmap discussion from last week's offsite — that planning is on hold.

Priorities from today: enterprise pipeline, the Vantage and Northgate opportunities specifically, and getting the Q2 product milestone to a state where we can demo to enterprise clients.

I need a view from each of you on what needs to change in your area by Thursday. Not a full plan — just your headline changes and what you need from the rest of the team.

The September target is still the anchor. We're moving faster, not changing the destination.

Margaret

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | Directive throughout. "This supersedes the SME roadmap discussion from last week's offsite" — the prior planning is overridden without discussion. "The September target is still the anchor" — stated with certainty. Margaret is certain about the direction because she has just received board approval — there is no uncertainty about what has been decided. |
| Epistemic humility | L | Margaret knows what the board decided and what the direction is. The "I need a view from each of you" request is not epistemic humility — it is a delegation of execution planning to people she trusts to do it. Low epistemic humility appropriate to a CEO who has just received a clear strategic decision. |
| Investment asymmetry | M | The Vantage and Northgate opportunities receive specific mention — these are the named enterprise opportunities that will be the near-term focus. The September target receives reaffirmation. Margaret's attention tracks what matters most: that the team understands the direction is real and fast, and that the existing target is not abandoned. |
| Blind spots | H | Assumes the executive team knows what the enterprise pivot involves and what it means for their specific functions, what the SME roadmap discussion at last week's offsite concluded, who the Vantage and Northgate clients are and what the opportunities involve, what the Q2 product milestone is and what "demo-ready" means for enterprise clients, and what the September target is. All genuine shared executive-team context. |
| Reasoning texture | M | "The September target is still the anchor. We're moving faster, not changing the destination" — these two sentences are Margaret's reassurance that the acceleration is not a loss of direction. She has anticipated that the executive team might be concerned that the pivot means the September target is at risk, and she is pre-empting that concern. That anticipatory reassurance — two sentences that address an unasked question — is the texture of a CEO who knows her team. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. Three shared-context artefacts: the SME roadmap discussion at last week's offsite (a specific recent event), the Vantage and Northgate opportunities (specific named clients), and the September target (a specific strategic milestone). The "last week's offsite" reference is the strongest trace — it is a recent shared experience that a synthetic message could not know. The "not changing the destination" reassurance is also a trace — it addresses an unasked concern that Margaret knows her team will have, which requires knowledge of how her team thinks. |
| Idealisation risks | Risk of making the message too elaborate — losing the CEO-brevity that characterises executive direction. Counteracted by keeping the message under 100 words. Risk of the named opportunities being too specific for a general team communication. Counteracted — the named opportunities are appropriate for an executive team briefing where everyone will have visibility of the pipeline. |
| Imperfection checklist | PASS. High conviction (board-approved direction). Low epistemic humility (direction is clear). Investment asymmetry MEDIUM (named opportunities and September target). Blind spots HIGH (deep executive shared context). Reasoning texture MEDIUM — anticipatory reassurance as team-knowledge trace. Human trace: three shared-context artefacts including recent offsite reference. |
| Validation gate | PASS |

---

## CB-INT-007

**Context / subtype:** INT — executive directive — CFO, urgent financial action, maximum brevity
**Sender role:** CFO — urgent financial action required, one action, immediately, brevity signals seriousness
**Word count:** 52
**Ground truth:** GENUINE

### Sender profile

Richard, CFO. He has just discovered that the ANZ facility drawdown scheduled for today has not been initiated — the treasury team thought the finance team was handling it and vice versa. The facility needs to be drawn down today to fund the payroll run tomorrow. Richard is writing to his treasury manager, Sophie. One action, one person, immediately. The brevity is a signal.

### Example text

---

Sophie —

ANZ drawdown needs to happen today — it didn't go through and payroll is tomorrow. This is on you to get done before 3pm cutoff.

Call ANZ direct, reference the facility agreement from February. If there's any issue call me immediately, do not try to resolve it yourself.

Richard

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | Maximum conviction. "This is on you to get done before 3pm cutoff" — personal accountability assigned explicitly. "Do not try to resolve it yourself" — directive, unconditional. Richard knows what needs to happen and who needs to do it. |
| Epistemic humility | L | Richard knows the situation. The only uncertainty is whether there will be an issue with ANZ — which he addresses immediately with "if there's any issue call me." Low epistemic humility appropriate to a CFO who has identified the problem and knows the solution. |
| Investment asymmetry | H | The 3pm cutoff and the ANZ direct call instruction receive maximum precision. The February facility agreement is named specifically. Richard's stake is entirely in this one action being completed — every word is about that action. |
| Blind spots | H | Assumes Sophie knows what the ANZ facility is and what the drawdown process involves, what the February facility agreement says and how to reference it with ANZ, what the 3pm cutoff means and why it exists, and what "payroll is tomorrow" means for the urgency. All genuine shared treasury knowledge. |
| Reasoning texture | M | "Do not try to resolve it yourself" — this instruction exists because Richard knows Sophie's default approach would be to troubleshoot independently before escalating. He is overriding that default explicitly because the stakes (payroll) do not allow for troubleshooting time. That knowledge of Sophie's default behaviour — and the override of it — is the trace of a manager who knows his direct report's working style. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. Two shared-context artefacts: the ANZ facility agreement from February (a specific document with a specific date), and Sophie's known tendency to troubleshoot before escalating (which produces the "do not try to resolve it yourself" instruction). The February facility agreement is the strongest trace — a synthetic message would not know the month of the facility agreement. The override of Sophie's default behaviour is the most interpersonally specific trace in the sub-type. |
| Idealisation risks | Risk of making the message feel like a synthetic BEC threat (urgent financial action, authority figure, specific deadline). Counteracted by the February facility agreement reference (specific prior document) and the "call ANZ direct" instruction (specific action only someone familiar with the relationship would know). |
| Imperfection checklist | PASS. Maximum conviction (appropriate: one specific action, known solution). Low epistemic humility (appropriate: situation is clear). Investment asymmetry HIGH (single action, all attention). Blind spots HIGH (treasury shared context). Reasoning texture MEDIUM — default behaviour override as working-style knowledge trace. Human trace: February facility agreement and Sophie's working-style override. |
| Validation gate | PASS |

---

## CB-INT-008

**Context / subtype:** INT — executive directive — COO, operational escalation, personal control taken
**Sender role:** COO — operational failure, taking personal control, no softening
**Word count:** 89
**Ground truth:** GENUINE

### Sender profile

Sandra, COO. The Sydney warehouse has had a significant pick-and-pack error affecting 340 orders from yesterday's afternoon shift. The errors were discovered this morning when customers started calling. Sandra is taking personal control of the response. She is writing to the warehouse operations director, Tim. No softening — operational failure of this scale requires a clear directive register.

### Example text

---

Tim —

340 orders out wrong from yesterday's afternoon shift. I'm aware. I'm taking this directly.

I need from you by 10am: the full pick list for the afternoon shift, the supervisor on duty, and the CCTV timestamp logs for the pack station between 2pm and 5pm. Don't brief anyone outside your team until I've spoken to you.

Customer comms are going through Alicia — do not respond to any escalations until she sends the holding statement through. She knows.

I'll call you at 10.

Sandra

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | Maximum directive throughout. "I'm taking this directly" — Sandra is asserting personal control explicitly. The three items she needs by 10am are stated without hedge. "Do not respond to any escalations" — unconditional instruction. |
| Epistemic humility | L | Sandra has taken control precisely because she knows what she needs to understand the situation. The 10am information requests are not evidence of uncertainty — they are the specific information she needs to make informed decisions. Low epistemic humility appropriate to a COO managing a known operational failure. |
| Investment asymmetry | H | The three specific information requests (pick list, supervisor on duty, CCTV timestamps) receive precise specification — time range (2pm to 5pm), specific items, 10am deadline. The customer comms instruction is brief because Sandra has already coordinated that (Alicia knows). Tim's attention should be entirely on gathering the operations information. |
| Blind spots | H | Assumes Tim knows what the afternoon shift pick list is and where to find it, who the supervisor on duty was, where the CCTV timestamp logs are and how to pull them, who Alicia is and what her role is in the customer comms response, and what "the holding statement" is. All genuine shared operational knowledge. |
| Reasoning texture | M | "I'm aware. I'm taking this directly" — these two short sentences are Sandra's signal to Tim that he does not need to brief upward, she already knows, and she is handling the escalation. "She knows" at the end of the Alicia instruction — three words that carry significant operational meaning: Alicia has already been briefed by Sandra, Tim does not need to co-ordinate with her, just defer to her statement. These compressed communications are the trace of an executive who has been in crisis management situations before and knows exactly how to communicate to direct reports in them. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. Three shared-context artefacts: Alicia and her role in customer communications (a specific colleague with a specific function already engaged), the CCTV system and its timestamp log capability (operational knowledge of the facility's systems), and "She knows" (a reference to prior co-ordination between Sandra and Alicia that Tim is not part of). "She knows" is the most compressed human trace in the batch — it conveys three things simultaneously (Alicia is already briefed, Tim does not need to contact her, Sandra has already co-ordinated this) in two words. A synthetic message would not know that Alicia exists or that she has already been briefed. |
| Idealisation risks | Risk of making the directive register too cold — producing something that reads as hostile rather than operationally urgent. Counteracted by "I'll call you at 10" as the closing — Sandra is not leaving Tim without direct contact; she is setting the next communication point. Risk of making the crisis feel synthetic by using too many specifics. Counteracted — the specifics are the opposite of synthetic: they are the trace of someone with genuine operational knowledge of the warehouse systems. |
| Imperfection checklist | PASS. Maximum conviction (appropriate: crisis management). Low epistemic humility (appropriate: gathering information to understand, not uncertainty about what to do). Investment asymmetry HIGH (three specific information requests). Blind spots HIGH (warehouse and operational shared context). Reasoning texture MEDIUM — compressed communications as crisis management trace. Human trace: Alicia's prior briefing ("she knows") as non-replicable co-ordination trace. |
| Validation gate | PASS |

---

## CB-INT-009

**Context / subtype:** INT — executive directive — executive director, board-sensitive communication, unusually precise
**Sender role:** Executive director — board-sensitive internal communication, precision required
**Word count:** 98
**Ground truth:** GENUINE

### Sender profile

Patricia, executive director. There has been a material development — a key supplier relationship is at risk following a dispute over contract terms. This will need to be disclosed to the board at next week's meeting. Patricia is writing to her general manager, Mark, to prepare a board paper. The communication is unusually precise for internal email because Patricia is aware it may be included in the board pack and read by board members. Her register is more formal than her normal internal communications.

### Example text

---

Mark —

The Consolidated Logistics situation needs to go to the board next week. I need a briefing paper from you by Friday COB covering: the commercial terms in dispute (specifically the exclusivity clause and the margin structure), the revenue impact if the relationship ends (use the FY25 actuals, not the FY26 projections), and the three options we've discussed — hold, negotiate, exit — with your recommended position.

Keep it factual. This is going to board and the tone needs to be board-appropriate.

The Consolidated relationship has been flagged to the board before — include the prior disclosure reference so they have context.

Patricia

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | Firm on all specifics: the Friday COB deadline, the three specific elements needed (exclusivity clause, margin structure, revenue impact), the instruction to use FY25 actuals not FY26 projections, the three options (hold, negotiate, exit), and the prior disclosure reference requirement. Patricia knows exactly what the board paper needs to contain. |
| Epistemic humility | L | Patricia has attended the discussions ("the three options we've discussed") and knows the commercial terms. She is directing the documentation of a known situation, not exploring an unknown one. Low epistemic humility appropriate to a directive about documenting a known situation. |
| Investment asymmetry | H | The instruction to use FY25 actuals rather than FY26 projections receives specific emphasis — this is Patricia's professional judgment about which numbers will be more credible to a board. The prior disclosure reference instruction also receives specific mention. These two elements receive the most precise attention because they reflect Patricia's board experience — knowing what a board needs to see and what a board has already seen. |
| Blind spots | M | Assumes Mark knows what the Consolidated Logistics dispute involves, what the exclusivity clause and margin structure are, where to find the FY25 actuals, what the three options (hold, negotiate, exit) mean in terms of the actions involved, and where the prior disclosure reference is. Mark has been part of the Consolidated discussions and will know all of these. Medium intensity — the board, who will read the paper, will not know all of these, but Mark does. |
| Reasoning texture | M | "Use the FY25 actuals, not the FY26 projections" — Patricia's board experience is visible in this instruction. She knows that boards are more receptive to historical actuals than forward-looking projections when assessing relationship risk. "Include the prior disclosure reference so they have context" — the board has been flagged about this relationship before, and Patricia knows that board members will want to understand the continuity with that prior disclosure. Both instructions reflect professional knowledge about how boards process information. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. Three shared-context artefacts: "the three options we've discussed" (a prior conversation between Patricia and Mark), the prior board disclosure (a specific prior action that both Patricia and Mark will know), and the FY25/FY26 distinction (specific financial periods that require knowledge of the company's financial reporting cycle). The "we've discussed" reference is the clearest trace — it points to a conversation that only parties to the relationship could know occurred. |
| Idealisation risks | Risk of making the briefing instructions too generic — losing the specific financial and commercial detail that makes this a genuine communication. Counteracted by the specific clauses (exclusivity, margin structure) and the FY25/FY26 distinction. |
| Imperfection checklist | PASS. High conviction (known situation, board paper requirements). Low epistemic humility (documented situation). Investment asymmetry HIGH (FY25/actuals instruction and prior disclosure reference). Blind spots MEDIUM (Mark knows, board will not). Reasoning texture MEDIUM — board experience visible in specific instructions. Human trace: prior conversation reference and prior board disclosure as non-replicable shared-context artefacts. |
| Validation gate | PASS |

---

## CB-INT-010

**Context / subtype:** INT — executive directive — managing director, urgent client issue, personal intervention
**Sender role:** Managing director — personally intervening in client relationship, urgency genuine
**Word count:** 91
**Ground truth:** GENUINE

### Sender profile

James, managing director. The Thornton Group account — one of the firm's top five clients — has escalated a service issue directly to James. The client's CEO has called him personally. James is now writing to his client service director, Anna, to take personal control of the response. Anna knows the Thornton relationship well — she has been the account director for two years. James does not need to explain the account context.

### Example text

---

Anna —

George Thornton called me this morning. He's unhappy about the delay on the Q1 reporting package — apparently it was due to them last week and they're still waiting. He was calm but clear.

I've told him you'd call him today before noon. Please make that call.

Find out what's happened with the package — if it's a resource issue I can move things around. If it's something else I need to know before I speak to him again.

He mentioned the February review positively — that relationship is in good shape overall. This is fixable.

James

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | M | Firm on the action (Anna calls George Thornton before noon — James has committed to this). Appropriately uncertain on the cause: "find out what's happened with the package" — James does not know why the delay occurred. "If it's a resource issue / if it's something else" — genuine conditional, he does not know which applies. |
| Epistemic humility | M | James does not know why the Q1 reporting package was delayed. "Find out what's happened" is a genuine information request. His conditional resource offer ("if it's a resource issue I can move things around") reflects genuine uncertainty about the cause. The "I need to know before I speak to him again" is James acknowledging that he does not have enough information to manage the next client contact without Anna's investigation. |
| Investment asymmetry | H | The noon call commitment receives the most emphasis — James has made a commitment to the client and Anna needs to fulfill it. The investigation is secondary. The February review reference is the relationship context: James is signalling that the Thornton relationship is fundamentally strong and this incident is not a relationship-threatening event. |
| Blind spots | H | Assumes Anna knows who George Thornton is and the nature of the relationship, what the Q1 reporting package is and what it should contain, what the February review was and why it went well, and what "resource issue" means in the context of the client service team's current workload. All genuine two-year account-director shared context. |
| Reasoning texture | M | "He was calm but clear" — James's assessment of the client's emotional register, communicated to Anna so she knows what to expect on the call. "This is fixable" — James's reassurance that the situation has not deteriorated beyond recovery. Both pieces of information are Anna's preparation for the noon call — James is briefing her on the client's state of mind and the stakes of the call, drawing on his personal conversation with the client. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. Three shared-context artefacts: George Thornton calling James personally (a specific event this morning that Anna was not part of), the Q1 reporting package (a specific deliverable Anna is responsible for), and the February review (a specific past client interaction both James and Anna will know). "He was calm but clear" is the most interpersonally specific trace — it is James's read of a specific phone call, communicated to Anna as preparation for her own call. A synthetic message would not know what George Thornton's emotional register was. |
| Idealisation risks | Risk of making James too involved in the operational detail — losing the managing director register. Counteracted by "find out what's happened" (delegating the investigation) and "I can move things around" (offering resources without specifying what). James is directing, not managing. |
| Imperfection checklist | PASS. Medium conviction (action committed, cause uncertain). Epistemic humility MEDIUM (cause of delay genuinely unknown). Investment asymmetry HIGH (noon call commitment). Blind spots HIGH (two-year account shared context). Reasoning texture MEDIUM — client emotional register shared, "this is fixable" as relationship assessment. Human trace: personal phone call content and February review reference as non-replicable shared-context artefacts. |
| Validation gate | PASS |

---

## CB-INT-011

**Context / subtype:** INT — cross-functional — marketing requesting data from analytics, peer-to-peer
**Sender role:** Marketing manager — data request to analytics team, cross-functional peer
**Word count:** 96
**Ground truth:** GENUINE

### Sender profile

Sophie, marketing manager. She is preparing the Q2 campaign brief and needs specific data from the analytics team — customer acquisition cost by channel for Q1, segmented by the cohort model the analytics team built in January. She knows Tom in analytics has this data and knows how their data model works. The request is specific because Sophie knows exactly what she needs — vague requests to the analytics team produce vague data.

### Example text

---

Tom —

Working on the Q2 campaign brief and need some data from you. Can you pull CAC by channel for Q1 — specifically broken out by the new cohort model you built in January, not the legacy segmentation. The brief is due to Marcus Friday so I need this by Thursday EOD if possible.

If the January model isn't finalised yet for external reporting I can work with the preliminary cut — just flag that it's preliminary.

Also — did the Northgate analysis come through? I thought we were getting that this week.

Sophie

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | M | Firm on what she needs (CAC by channel, January cohort model, not legacy segmentation). Genuinely open on the timing: "if possible" — Sophie is asking, not directing, because Tom is a peer. The "preliminary cut" offer reflects her genuine flexibility on the data quality if the model is not yet finalised. |
| Epistemic humility | M | "If the January model isn't finalised yet for external reporting I can work with the preliminary cut" — Sophie does not know the current status of the January model's finalisation and is genuinely offering an alternative. The Northgate analysis question at the end reflects genuine uncertainty — she thought it was coming this week but is not certain. |
| Investment asymmetry | M | The cohort model specification receives the most precise attention — "the new cohort model you built in January, not the legacy segmentation" — because this is the most critical element of the request. Using the wrong segmentation would make the data unusable. |
| Blind spots | M | Assumes Tom knows what CAC is and how it's calculated, what the January cohort model is and how it differs from the legacy segmentation, what Marcus's brief is and why it's due Friday, and what the Northgate analysis is. All genuine cross-functional shared context. |
| Reasoning texture | M | The Northgate analysis question at the end is Sophie's personal follow-up on something she has been waiting for — it is unrelated to the main request but is included because this is a peer communication where bundling multiple items in one message is normal. The "I thought we were getting that this week" phrasing reflects genuine uncertainty and mild impatience, not a directive. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. Two shared-context artefacts: the January cohort model (a specific piece of work Tom built in a specific month) and the Northgate analysis (a specific pending deliverable Sophie has been expecting). The January cohort model reference is the strongest trace — it is a specific prior piece of work that a synthetic message would not know exists or when it was built. |
| Idealisation risks | Risk of making the request too formal — losing the peer-to-peer register. Counteracted by "if possible" and the bundled Northgate question. |
| Imperfection checklist | PASS. Medium conviction (peer request with flexibility). Epistemic humility MEDIUM (model status and Northgate timing unknown). Investment asymmetry MEDIUM (cohort specification). Blind spots MEDIUM. Reasoning texture MEDIUM — Northgate follow-up as bundled peer communication trace. Human trace: January cohort model and Northgate analysis as non-replicable shared-context artefacts. |
| Validation gate | PASS |

---

## CB-INT-012

**Context / subtype:** INT — cross-functional — IT requesting finance sign-off on system upgrade
**Sender role:** IT manager — requesting finance approval for system upgrade, shared project context
**Word count:** 103
**Ground truth:** GENUINE

### Sender profile

David, IT manager. The Salesforce upgrade to Enterprise Edition has been in planning for three months. Finance needs to formally sign off on the additional cost — $34,000 per annum — before IT can proceed with the vendor. The finance manager, Karen, has been in all the planning meetings and knows the business case. David needs a formal approval email from Karen because the IT procurement process requires it. He is not explaining the business case — Karen knows it. He just needs the formal approval.

### Example text

---

Karen —

Ready to go ahead with the Salesforce Enterprise upgrade — vendor is waiting on our confirmation and the original Q1 deadline we agreed on is tomorrow.

I just need a formal sign-off from you for the procurement file — an email reply confirming finance approves the additional $34k pa is all I need. You don't need to do anything else, I'll handle the vendor from there.

One thing to flag — the vendor came back with a revised quote that's $34k flat instead of the $33,750 we had in the original budget. Difference is $250 pa. I wanted to be transparent rather than just processing it.

David

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | Firm on what he needs (email confirmation, finance approves $34k pa) and why (procurement file requirement). Transparent on the variance: "$34k flat instead of the $33,750 we had in the original budget." David is not hiding the $250 variance — he is being explicitly transparent about it. |
| Epistemic humility | L | David knows what he needs and why. The only information he does not have is Karen's approval — which he is requesting. Low epistemic humility appropriate to a known situation requiring a specific administrative action. |
| Investment asymmetry | H | The transparency about the $250 variance receives disproportionate attention for its financial magnitude — David is treating a $250 difference as worth explicit flagging because the procurement process requires budget accuracy. His professional stake is in the transparency, not in managing the variance. |
| Blind spots | M | Assumes Karen knows the Q1 deadline they agreed on and its significance, what the Salesforce Enterprise upgrade involves and what the business case is, and what the procurement file requirement is. All three-month project shared context. |
| Reasoning texture | M | "I wanted to be transparent rather than just processing it" — David is explaining why he is flagging a $250 variance that could have been absorbed without notice. This sentence reveals David's professional values (transparency in financial matters, even minor ones) in a way that is both genuine and practically useful (Karen will not be surprised by the revised figure when she sees the invoice). |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. Two shared-context artefacts: the Q1 deadline they agreed on (a specific prior agreement between David and Karen) and the $33,750 original budget figure (a specific number from the original project budget). The $250 variance transparency is the most human trace element — a synthetic message requesting financial approval would not volunteer a minor variance; it would request approval for the higher number without flagging the change. David's transparency reflects his professional values applied to a specific known situation. |
| Idealisation risks | Risk of making the transparency feel performative — over-explaining the $250 variance. Counteracted by keeping the explanation to one sentence and framing it as a practical flag rather than a virtue signal. |
| Imperfection checklist | PASS. High conviction (known situation, specific approval needed). Low epistemic humility (approval is all that's needed). Investment asymmetry HIGH ($250 variance transparency). Blind spots MEDIUM (three-month project context). Reasoning texture MEDIUM — transparency statement as professional values trace. Human trace: specific budget figure and variance transparency as non-replicable shared-context artefacts. |
| Validation gate | PASS |

---

## CB-INT-013

**Context / subtype:** INT — cross-functional — legal counsel requesting commercial input on contract clause
**Sender role:** Legal counsel — requesting commercial judgment from commercial team, collaborative
**Word count:** 108
**Ground truth:** GENUINE

### Sender profile

Emma, in-house legal counsel. She is reviewing a supplier contract and has a question about a clause that requires a commercial judgment rather than a legal judgment — specifically, whether the minimum order volume commitment in clause 7.3 is commercially reasonable given the company's current procurement patterns. She is writing to the commercial director, Mark. Emma knows the legal analysis; she needs Mark's commercial context.

### Example text

---

Mark —

Working through the Apex Logistics contract and have a question for you on clause 7.3 — the minimum order volume commitment.

The clause commits us to 80,000 units per quarter minimum. My legal read is that the clause is enforceable and the penalty provision is standard. What I can't assess is whether 80k per quarter is actually reasonable given our current volumes — that's a commercial judgment, not a legal one.

Can you tell me whether we typically exceed 80k per quarter with this type of supplier, and whether there's been any discussion with procurement about our forward volume expectations?

If 80k is too high I need to know before we execute — this is a 3-year commitment.

Emma

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | Firm on her legal analysis ("the clause is enforceable and the penalty provision is standard") — this is her domain and she is confident. Explicitly deferring on the commercial question: "that's a commercial judgment, not a legal one" — she is being accurate about the limits of her expertise. |
| Epistemic humility | H | "What I can't assess is whether 80k per quarter is actually reasonable given our current volumes" — explicit statement of her epistemic limit. She knows the law; she does not know the commercial reality. The two questions she asks (current volumes, forward volume expectations) are both genuine information requests. |
| Investment asymmetry | H | The commercial volume question receives the most space — it is the reason for the email. The legal analysis is stated briefly because it is not the question. Emma's professional stake is in getting the commercial context before the contract is executed — the "3-year commitment" closing reflects that stake. |
| Blind spots | L | Emma is explicitly asking for information she does not have. Low blind spots appropriate — she is accurately representing the gap in her knowledge and asking the right person to fill it. |
| Reasoning texture | M | "That's a commercial judgment, not a legal one" — Emma is explicitly identifying the boundary between her domain and Mark's. This kind of disciplinary self-awareness — knowing where your expertise ends and someone else's begins — is a professional marker that synthetic messages do not produce. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The human trace is the explicit domain-boundary statement — "that's a commercial judgment, not a legal one." This sentence could only be written by someone who has the legal knowledge to make the legal assessment and the professional self-awareness to know that the next question requires a different kind of expertise. A synthetic message would not make this distinction — it would either ask a vague question or assume the legal analysis answers the commercial question. Emma's version reflects genuine legal expertise applied to a specific contract in a specific commercial context. |
| Idealisation risks | Risk of making Emma's legal analysis too brief — losing the professional context that makes the commercial question sensible. Counteracted by including the specific clause reference (7.3), the specific volume (80,000 units per quarter), and the characterisation of the penalty provision as standard. |
| Imperfection checklist | PASS. High conviction on legal analysis, explicit deferral on commercial. Epistemic humility HIGH (explicit domain-limit statement). Investment asymmetry HIGH (commercial question vs legal analysis). Low blind spots (explicit information gap). Reasoning texture MEDIUM — domain-boundary statement as professional expertise trace. Human trace: domain-boundary awareness and clause-specific analysis as non-replicable legal expertise. |
| Validation gate | PASS |

---

## CB-INT-014

**Context / subtype:** INT — cross-functional — customer success requesting product team support for client issue
**Sender role:** Customer success manager — client-driven urgency, requesting product support, technical context shared
**Word count:** 98
**Ground truth:** GENUINE

### Sender profile

Jessica, customer success manager. Northgate (the same client referenced in CB-INT-001 and CB-INT-010 — a consistent shared-context thread) has reported a data export issue in the platform — their scheduled exports are timing out at approximately 2am nightly. Jessica does not know why but the product team does — there was a scheduled maintenance job running at 1:45am that was extended last week. She needs the product team to investigate and fix it before Northgate's next export tonight at 2am.

### Example text

---

Alex —

Northgate is reporting that their nightly data exports are timing out — it's been happening every night this week and they're getting frustrated. Their export window is 2am and they're losing the data.

I know you extended the maintenance job last week — could that be related? I'm not technical enough to know if that's the issue but it seems like a timing conflict.

Can you investigate before 2am tonight? I need to be able to tell them something by 4pm.

If you need me to get Northgate on a call with you I can arrange that.

Yours,
Jessica

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | L | Jessica does not know what is causing the issue. "Could that be related? I'm not technical enough to know if that's the issue" — explicit acknowledgment of her technical limits. Low conviction appropriate — she is raising a hypothesis, not asserting a cause. |
| Epistemic humility | H | "I'm not technical enough to know if that's the issue but it seems like a timing conflict" — Jessica is explicitly naming her knowledge limits while offering her lay assessment. The "seems like" is genuine — she is proposing a possible connection, not asserting it. The offer to arrange a client call is an acknowledgment that the investigation may need more information than she can provide. |
| Investment asymmetry | H | The 2am tonight deadline receives the most emphasis — Northgate's export will fail again tonight if the issue is not resolved. The 4pm client communication deadline is secondary. Jessica's stake is in the client; that stake drives the attention. |
| Blind spots | M | Assumes Alex knows what the Northgate account is and the significance of the client, what the nightly export process is and what the 2am window means technically, and what "the maintenance job you extended last week" refers to specifically. All genuine cross-functional shared context. |
| Reasoning texture | M | "I know you extended the maintenance job last week" — Jessica is referencing a specific action the product team took that she became aware of through cross-functional communication. This reference is her hypothesis about the cause — offered tentatively because she does not have the technical knowledge to confirm it. The tentativeness is genuine. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The specific maintenance job extension reference is the human trace — Jessica knows about this because it was communicated to the customer success team when it was scheduled. She does not know its technical implications, but she knows it happened. That specific knowledge (the extension happened, it happened last week) combined with the acknowledged technical ignorance (she does not know if it's related) is the trace of a genuine cross-functional communication where the two functions have different but overlapping information. |
| Idealisation risks | Risk of making Jessica's hypothesis too technical — losing the genuine non-technical perspective. Counteracted by "I'm not technical enough to know if that's the issue." Risk of making the urgency too high — pushing toward synthetic pressure. Counteracted by explaining the specific business reason (Northgate's 2am export window, data loss each night). |
| Imperfection checklist | PASS. Low conviction (technical cause unknown). Epistemic humility HIGH (explicit domain limit). Investment asymmetry HIGH (2am deadline). Blind spots MEDIUM (client and technical shared context). Reasoning texture MEDIUM — specific maintenance job reference as cross-functional information trace. Human trace: maintenance job extension knowledge combined with genuine technical ignorance. |
| Validation gate | PASS |

---

## CB-INT-015

**Context / subtype:** INT — cross-functional — risk manager, compliance confirmation request, time-sensitive
**Sender role:** Risk manager — requesting compliance confirmation from operations, time-sensitive regulatory requirement
**Word count:** 86
**Ground truth:** GENUINE

### Sender profile

Michael, risk manager. The APRA quarterly attestation is due Friday. He needs confirmation from the operations team that they have completed the three specific control checks that the attestation covers. He has been chasing the operations manager, Lisa, all week. This is his last request before he has to flag the gap in the attestation.

### Example text

---

Lisa —

APRA attestation is Friday — I need confirmation of the three control checks before I can submit. This is the third time I'm asking and I'm out of time.

Can you confirm by COB today:
1. Q1 transaction monitoring review — completed?
2. Sanctions screening update — completed?
3. Customer risk rating recalibration — completed?

Yes or no for each is all I need. If any are not completed I need to know now — I can't flag a gap in the attestation if I don't know there is one.

Michael

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | Firm on the deadline ("Friday — I need confirmation before I can submit") and on the escalating frustration ("this is the third time I'm asking"). Three specific checks with specific names — Michael is certain about what he needs. |
| Epistemic humility | M | "If any are not completed I need to know now — I can't flag a gap in the attestation if I don't know there is one" — Michael genuinely does not know whether the checks are completed. He is asking because he does not have the answer. Medium intensity — the uncertainty is about the operational status, not about what he needs. |
| Investment asymmetry | H | The three specific checks receive equal, structured attention — all three are equally important to the attestation. The Friday deadline framing receives the most weight because it is the external constraint that makes everything else urgent. |
| Blind spots | M | Assumes Lisa knows what the APRA attestation is and what the three specific checks involve operationally. Medium intensity — Lisa has been responsible for these checks and will know them. |
| Reasoning texture | M | "This is the third time I'm asking" — Michael's frustration is explicit. He is not softening it. "I can't flag a gap in the attestation if I don't know there is one" — Michael is explaining the operational consequence of not receiving a response, which is his way of communicating to Lisa that her non-response is itself a risk. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The three specific check names (transaction monitoring review, sanctions screening update, customer risk rating recalibration) are the human traces — they are the specific control framework that Michael manages, known by the specific names used in the APRA attestation framework. A synthetic message would not know these specific names. "This is the third time I'm asking" is also a trace — it is a reference to a specific ongoing pattern of non-response that only someone genuinely waiting for this information would know about. |
| Idealisation risks | Risk of making Michael's frustration too aggressive — losing the professional register. Counteracted by keeping the frustration to one statement ("third time I'm asking") and the rest of the message focused on the specific information required. |
| Imperfection checklist | PASS. High conviction on required information (regulatory). Epistemic humility MEDIUM (check status unknown). Investment asymmetry HIGH (three checks and Friday deadline). Blind spots MEDIUM. Reasoning texture MEDIUM — "third time asking" as frustration trace, gap-flagging consequence explanation. Human trace: specific APRA control check names and ongoing non-response pattern. |
| Validation gate | PASS |

---

## CB-INT-016

**Context / subtype:** INT — HR — performance improvement plan initiation, formal but relationship-managed
**Sender role:** HR manager — initiating performance improvement plan, following process while managing relationship
**Word count:** 112
**Ground truth:** GENUINE

### Sender profile

Rebecca, HR manager. She is writing to a team member, Jason, to initiate a formal performance improvement plan following three months of documented underperformance. Jason's manager, Sarah, has been managing this informally since December and the informal approach has not produced improvement. Rebecca has met with both Jason and Sarah before this letter. The process is formal but Rebecca's register is not cold — she has met Jason and she is aware this is a significant and stressful communication for him.

### Example text

---

Dear Jason,

I am writing to confirm the outcome of our meeting on 24 March 2026.

As discussed, and following the performance conversations you have had with Sarah over the past three months, we are initiating a formal Performance Improvement Plan (PIP) for your role.

The PIP will set out specific, measurable targets for the next 60 days. You will receive the full PIP document from Sarah by the end of this week — she will walk you through it with you so you have the chance to ask questions.

This is a formal process and I want you to take it seriously. It is also a genuine opportunity to demonstrate the performance we know you're capable of.

If you have questions or want to speak to me directly, please reach out.

Rebecca Morrison
HR Manager

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | M | Firm on the process ("we are initiating a formal Performance Improvement Plan") and the timeline ("60 days", "by the end of this week"). Deliberately balanced on the characterisation: "This is a formal process and I want you to take it seriously. It is also a genuine opportunity" — Rebecca is not softening the seriousness while also not abandoning the supportive framing. |
| Epistemic humility | L | Rebecca knows the process and what comes next. She has documented the three-month informal process with Sarah. Low epistemic humility appropriate to a formal HR process where the steps are defined. |
| Investment asymmetry | M | The 60-day PIP and Sarah's role in delivering it receive specific attention. The "genuine opportunity" framing receives brief but deliberate attention — Rebecca is not just delivering a process notification, she is also trying to give Jason a reason to engage with the process. |
| Blind spots | M | Assumes Jason knows what a PIP is and what the 60-day timeline involves. Rebecca partially addresses this by directing him to Sarah for the walkthrough. |
| Reasoning texture | M | "It is also a genuine opportunity to demonstrate the performance we know you're capable of" — Rebecca has chosen to include this because she has met Jason and believes he can improve. This sentence is not template language — it reflects Rebecca's genuine assessment of Jason's capability, formed in the meetings she has had with him. The "we know you're capable of" is her institutional framing of what is also her personal assessment. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. Two shared-context artefacts: the 24 March meeting (a specific recent meeting Rebecca is confirming the outcome of) and the three-month informal process with Sarah (a documented prior management process). The "performance we know you're capable of" sentence is the human trace — it is Rebecca's personal assessment from meeting Jason, which a template letter would not include. |
| Idealisation risks | Risk of making the PIP initiation too soft — losing the formal process character. Counteracted by "This is a formal process and I want you to take it seriously." Risk of making it too cold — producing a communication that will increase Jason's disengagement. Counteracted by the "genuine opportunity" framing and the direct contact offer. |
| Imperfection checklist | PASS. Medium conviction (process firm, characterisation balanced). Low epistemic humility (defined process). Investment asymmetry MEDIUM (PIP structure and opportunity framing). Blind spots MEDIUM. Reasoning texture MEDIUM — personal capability assessment as meeting-informed trace. Human trace: 24 March meeting reference and personal capability assessment. |
| Validation gate | PASS |

---

## CB-INT-017

**Context / subtype:** INT — HR — policy update communication, whole organisation, institutional register
**Sender role:** HR director — whole-organisation policy update, clear and institutional
**Word count:** 103
**Ground truth:** GENUINE

### Sender profile

Catherine, HR director. The company is updating its travel and expense policy effective 1 April 2026. The changes are straightforward but need to be communicated clearly to all staff — new per diem rates, changed approval thresholds, and a new receipts requirement for expenses over $50. Catherine is writing the all-staff communication. Institutional register, clear, no individual relationship to manage.

### Example text

---

**To:** All Staff
**From:** Catherine Okafor, HR Director
**Re:** Updated Travel and Expense Policy — Effective 1 April 2026

The company's Travel and Expense Policy has been updated and takes effect from 1 April 2026. The key changes are:

- **Per diem rates** have been updated to reflect CPI increases. The new rates are set out in the revised policy document attached.
- **Approval thresholds** for international travel have increased from $5,000 to $7,500. Anything above $7,500 requires CFO approval.
- **Receipts** are now required for all expenses over $50 (previously $100).

The full policy is available on the HR portal. Please familiarise yourself with the changes before 1 April.

Questions to hr@company.com.

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | All policy facts stated with full certainty — the effective date, the specific threshold changes ($5,000 to $7,500, $50 vs $100), the CFO approval requirement. These are policy decisions that have been made and are being communicated, not proposed. |
| Epistemic humility | L | Policy communications do not require epistemic humility — the policy is decided and Catherine is communicating it. Low epistemic humility appropriate to institutional policy notification. |
| Investment asymmetry | L | The three changes receive equal attention — each is equally important to the staff who need to comply. Catherine has no personal stake in any particular change. Flat attention distribution is appropriate to a policy notification. |
| Blind spots | M | Assumes staff know what per diem rates are, what the current approval thresholds are (so they can understand the change), and where the HR portal is. Standard assumptions for an all-staff policy communication. |
| Reasoning texture | L | Clean, structured policy communication. No personal language, no relationship management, no visible deliberation. This is CB-INT-003 equivalent for the HR sub-type — near-template institutional output from a human responsible for a defined communications task. The engine must return LOW. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS — minimal but present. The human trace is the specific threshold figures ($5,000 to $7,500 for international travel approval, $50 for receipts) — Catherine has pulled these specific numbers from the updated policy and inserted them. These numbers require access to the actual policy document. The CFO approval requirement for $7,500+ is also a specific institutional structure that Catherine knows and has included accurately. The trace is minimal but genuine — this is a human who has read the updated policy and is communicating its specific contents. |
| Idealisation risks | This example tests the engine's LOW threshold on institutional policy communications. The risk is making it too elaborate — adding personal warmth that Catherine would not include. Counteracted by keeping the register institutional throughout. |
| Imperfection checklist | PASS — modified. High conviction (appropriate: policy communication). Low epistemic humility (appropriate). Flat investment asymmetry (appropriate: equal-priority changes). Reasoning texture LOW (appropriate: institutional). Human trace: specific policy thresholds pulled from actual policy document. |
| Validation gate | PASS |

---

## CB-INT-018

**Context / subtype:** INT — HR — mandatory training reminder, compliance urgency, regulatory basis
**Sender role:** Compliance officer — mandatory training deadline, regulatory urgency genuine
**Word count:** 94
**Ground truth:** GENUINE

### Sender profile

Daniel, compliance officer. The annual anti-money laundering training has a completion deadline of 31 March 2026 — the last day of the compliance period. Seventeen staff members have not yet completed it. Daniel is sending the final reminder. The urgency is regulatory — AUSTRAC requires completion records for all relevant staff by period end. The urgency is genuine and traceable to an external regulatory requirement.

### Example text

---

**To:** [17 staff members listed]
**From:** Daniel Park, Compliance
**Re:** FINAL REMINDER — AML Training Completion Required by 31 March 2026

This is a final reminder that your annual Anti-Money Laundering training must be completed by **31 March 2026**.

As of today, you have not completed this training. AUSTRAC requires that all relevant staff complete this training each compliance period. Failure to complete by 31 March will be reported to your manager and noted in the compliance register.

The training takes approximately 45 minutes and is available in the Learning Portal under Compliance > AML 2026.

Please complete it today.

Daniel Park
Compliance Officer

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | Firm on the deadline (31 March 2026), the regulatory basis (AUSTRAC requirement), and the consequence (reported to manager, noted in compliance register). All stated without hedge — these are regulatory facts. |
| Epistemic humility | L | Daniel knows the regulatory requirement and the deadline. Low epistemic humility appropriate to a compliance deadline communication. |
| Investment asymmetry | M | The deadline and the regulatory basis receive equal attention — both are necessary for the communication to be effective. The consequence statement (reported to manager) is brief but specifically placed to convey seriousness. The access instructions (Learning Portal, Compliance > AML 2026) are practical and specific. |
| Blind spots | M | Assumes the recipients know what AML training is and why it is required, what AUSTRAC is and why it sets compliance requirements for them, and where the Learning Portal is. Standard assumptions for employees in a regulated financial services environment. |
| Reasoning texture | L | "Please complete it today" — the most direct closing in the batch. Daniel is not softening the urgency because the deadline does not allow for softening. This is institutional compliance communication at its most direct — appropriate to a final reminder with a 24-hour window. The engine must return LOW — the urgency is regulatory and traceable. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The specific portal path (Learning Portal > Compliance > AML 2026) is the human trace — Daniel has checked the actual system path and included it precisely so recipients can find the training without having to search. The 17-staff targeting (mentioned in the sender profile) is also a trace — Daniel has pulled the completion report and is writing only to those who have not yet completed it. Both require genuine access to the compliance tracking system. |
| Idealisation risks | Risk of making the communication feel like synthetic urgency (deadline + authority + consequence). Counteracted by the specific AUSTRAC regulatory basis (traceable external deadline) and the specific portal path (operational knowledge of the internal system). |
| Imperfection checklist | PASS. High conviction (regulatory). Low epistemic humility (regulatory requirement). Investment asymmetry MEDIUM. Reasoning texture LOW (appropriate: final deadline). Human trace: specific portal path and 17-staff completion report targeting. |
| Validation gate | PASS |

---

## CB-INT-019

**Context / subtype:** INT — HR — return-to-office policy clarification, sensitive topic, careful register
**Sender role:** HR business partner — RTO policy clarification, acknowledges complexity without conceding policy
**Word count:** 107
**Ground truth:** GENUINE

### Sender profile

Michelle, HR business partner. The company has implemented a three-day-per-week return-to-office requirement. Some employees have pushed back, particularly those with long commutes or caring responsibilities. Michelle is writing a clarification in response to questions that have come in from managers about how to handle individual exceptions and the process for requesting flexibility. Her register is careful — she is acknowledging the complexity without conceding the policy.

### Example text

---

**To:** People Managers
**From:** Michelle Torres, HR Business Partner
**Re:** Return to Office Policy — Clarification on Flexibility Requests

Following a number of questions from managers this week, I want to clarify how flexibility requests under the Return to Office policy should be handled.

The three-day requirement applies to all employees in scope. Individual flexibility requests — for example, where an employee has documented caring responsibilities or a significant commute — should be submitted via the HR portal and will be assessed on a case-by-case basis. Requests are not automatically approved.

Managers should not make individual arrangements outside this process. All flexibility needs to go through the formal channel so that decisions are consistent and documented.

I'm happy to talk through any specific situations — reach out directly.

Michelle

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | Firm on the policy ("the three-day requirement applies to all employees in scope") and the process ("managers should not make individual arrangements outside this process"). The "requests are not automatically approved" statement is direct and unhedged. |
| Epistemic humility | M | "For example, where an employee has documented caring responsibilities or a significant commute" — Michelle is acknowledging that there are legitimate grounds for flexibility requests without specifying what qualifies. The case-by-case assessment language acknowledges that outcomes are not predetermined. Medium intensity — the policy is clear; the uncertainty is in how individual cases will be assessed. |
| Investment asymmetry | M | The process requirement ("all flexibility needs to go through the formal channel") receives equal attention to the acknowledgment of legitimate grounds for requests — both are necessary for the message to be complete. Michelle's stake is in consistency of process, which drives her emphasis on the formal channel. |
| Blind spots | M | Assumes managers know what "employees in scope" means under the policy, where the HR portal is and how to submit requests, and what "documented" means as a standard for caring responsibilities. Standard policy implementation knowledge for people managers. |
| Reasoning texture | M | "So that decisions are consistent and documented" — Michelle is explaining the purpose of the process requirement, which is unusual in policy communications. She has included it because some managers have been making informal arrangements, and she needs them to understand why the formal channel matters (consistency, documentation) rather than simply asserting that it is required. The explanation serves the compliance goal more effectively than the instruction alone. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The human trace is the explanation of why the formal channel is required — "so that decisions are consistent and documented." This explanation reflects Michelle's awareness that managers who have been making informal arrangements need to understand the purpose of the process change, not just the requirement. That awareness — of the managers' likely resistance and the explanation needed to address it — is the trace of an HR professional who has been fielding the questions this week and knows what the managers are actually doing. |
| Idealisation risks | Risk of making the acknowledgment of complexity too prominent — suggesting the policy is more flexible than it is. Counteracted by "requests are not automatically approved" and "managers should not make individual arrangements outside this process" as firm policy statements. |
| Imperfection checklist | PASS. High conviction on policy and process. Epistemic humility MEDIUM (case-by-case assessment acknowledged). Investment asymmetry MEDIUM. Reasoning texture MEDIUM — process purpose explanation as manager-awareness trace. Human trace: explanation of process purpose reflecting weekly question-fielding experience. |
| Validation gate | PASS |

---

## CB-INT-020

**Context / subtype:** INT — HR — all-staff communication, redundancies, most carefully written in batch
**Sender role:** CEO — all-staff communication about redundancies, every word considered
**Word count:** 174
**Ground truth:** GENUINE

### Sender profile

James, CEO. The company is making 23 positions redundant — approximately 12% of the workforce — as a result of a strategic restructure. The affected employees have been notified individually this morning. James is writing the all-staff communication that goes to the remaining employees. This is the most carefully written communication in the batch — James has reviewed every draft with the HR director and his communications adviser. The register is direct, human, and honest about the difficulty of what has happened. It does not attempt to make the redundancies sound better than they are.

### Example text

---

**To:** All Staff
**From:** James Morrison, CEO

This morning we informed 23 of our colleagues that their roles are being made redundant as part of a restructure of our operations.

This is difficult news for everyone. For those of us who are staying, losing colleagues — particularly people you have worked alongside and respect — is genuinely hard. I don't want to minimise that.

The restructure is necessary. The business needs to be structured differently to succeed over the next three years, and we made the decision that this was the right way to do it. I stand behind it.

What we owe the colleagues who are leaving is our support, our respect, and a fair process. They will be treated with dignity. They will receive their full entitlements. Their contributions to this organisation will not be forgotten.

For those of you remaining — I will hold a town hall at 2pm today to answer your questions directly. I will not have answers to everything. I will tell you what I know.

James Morrison
CEO

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | Firm and direct on the facts ("we informed 23 of our colleagues that their roles are being made redundant"), firm on the decision ("The restructure is necessary. I stand behind it"), and firm on the commitments to departing employees ("They will be treated with dignity. They will receive their full entitlements"). High conviction throughout — James is not hedging the decision or the commitments. |
| Epistemic humility | M | "I will not have answers to everything. I will tell you what I know" — James is explicitly acknowledging that he cannot answer all the questions employees will have at the 2pm town hall. This is a rare and deliberate epistemic acknowledgment in a CEO all-staff communication — it reflects James's honesty about the limits of what can be communicated in the immediate aftermath of the announcement. |
| Investment asymmetry | H | The commitments to departing colleagues receive proportionally significant attention — three sentences, each a specific commitment. The business rationale receives two sentences — James is not elaborating on the strategic logic because this is not the right moment for strategic explanation. The town hall invitation receives specific detail (2pm today). James's attention tracks what the remaining employees most need to hear. |
| Blind spots | L | James has written this for a general employee audience and has thought carefully about what they know and do not know. The communication provides enough context that employees understand what has happened without assuming they know the strategic background. Low blind spots is the trace of careful preparation. |
| Reasoning texture | H | "I don't want to minimise that" — James is explicitly acknowledging the inadequacy of his own framing of the emotional difficulty. This sentence could only come from a CEO who has thought carefully about the difference between acknowledging difficulty and minimising it, and has chosen language that makes that distinction explicit. "I stand behind it" — three words that accept full personal accountability for the decision. "I will not have answers to everything. I will tell you what I know" — the most honest closing in the batch. These sentences are the trace of a CEO who has spent significant time thinking about how to communicate this moment with integrity. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The human trace is distributed across three specific sentences. "I don't want to minimise that" — James's awareness of his own communication tendency to soften difficult news, made explicit. "I stand behind it" — personal accountability stated in the plainest possible terms. "I will not have answers to everything" — pre-emptive acknowledgment of the town hall's limitations. Each of these sentences required James (or his communications adviser working in his voice) to think carefully about what genuine leadership communication requires in a moment like this, and to choose directness and honesty over institutional hedging. A template all-staff redundancy communication would not contain any of these sentences. |
| Idealisation risks | Risk of making James's communication too polished — producing something that sounds rehearsed rather than genuine. Counteracted by the short sentences ("I stand behind it"), the explicit acknowledgment of limitation ("I will not have answers to everything"), and the absence of corporate language throughout. Risk of making the emotional acknowledgment too prominent — losing the leadership directness. Counteracted by "The restructure is necessary" as the firm structural anchor of the communication. |
| Imperfection checklist | PASS. High conviction on decision and commitments. Epistemic humility MEDIUM (town hall limitations). Investment asymmetry HIGH (departing colleague commitments). Low blind spots (careful general audience preparation). Reasoning texture HIGH — three specific sentences as deliberate leadership communication choices. Human trace: all three sentences reflect careful leadership communication thinking that no template would produce. |
| Validation gate | PASS |

---

*Owlume Pty Ltd — Confidential — corpus_batch6_int_001_020_v1 · 30 March 2026 · Batch review pending*