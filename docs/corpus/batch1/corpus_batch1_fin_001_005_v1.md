# Calibration Corpus — Batch 1, Examples 1–5

**HumanTrace — Internal Document**
Financial Services — Collections Letters · CB-FIN-001 through CB-FIN-005
Ground truth: GENUINE · Path A synthetic genuine construction
Version 1.0 · 30 March 2026 · Owlume Pty Ltd
Constructed under `corpus_construction_protocol_v1.1`

---

## CB-FIN-001

**Context / subtype:** FIN — collections letter — junior officer, template with seam
**Sender role:** Junior collections officer, 18 months in role
**Word count:** 187
**Ground truth:** GENUINE

### Sender profile

Kareena, junior collections officer, 18 months in the role. This is one of 40 accounts she is working today. Her performance metric is clearance rate. She does not know why Mr Hartley defaulted — no notes on file beyond the automated reminders. She assumes he knows the reminders went out. She is working from the bank's standard collections template; her personal insertion is the customer name, amount, and account reference. The seam between template language and her insertion is visible in paragraph three.

### Example text

---

Dear Mr Hartley,

We are writing to advise that your account ending 4471 is currently overdue by $2,340.00. This amount has been outstanding for 47 days.

As per the terms and conditions of your account agreement, we are required to notify you that if this amount is not received within 14 days of the date of this letter, we may be required to report this default to a credit reporting body.

We understand there may be circumstances affecting your ability to make payment at this time. If this is the case, we would encourage you to contact us as soon as possible on 1800 XXX XXX to discuss what options may be available to you.

If you have already made this payment, please disregard this notice.

Yours sincerely,
Kareena Mehta
Collections Officer
Customer Accounts Division

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | M | Strong and unhedged on the debt fact and regulatory consequence ("we may be required to report"). Hedged and distanced on customer circumstances ("we understand there may be circumstances") — the hedge is genuine because she actually does not know why he defaulted. |
| Epistemic humility | H | "If this is the case, we would encourage you to contact us" — genuine conditional, she is requesting information she does not have. "If you have already made this payment, please disregard" — she does not know the payment status at time of writing; this is a real knowledge gap, not boilerplate courtesy. |
| Investment asymmetry | M | The overdue amount and the 14-day deadline receive specific precision ($2,340.00, 47 days, 14 days). The resolution pathway ("discuss what options may be available") is vague — one clause, no specifics. Her stake is clearance, so the consequence trigger gets the attention. |
| Blind spots | H | Assumes Mr Hartley knows the automated reminders were sent. Does not explain what credit reporting means or what the 14-day consequence involves in practice. Expertise blind spot — these are obvious to her, invisible gap to the customer. |
| Reasoning texture | L | Template constrains most texture. The visible seam is in paragraph three: "we would encourage" is slightly softer than surrounding template language — the insertion point where Kareena's uncertainty meets the template's optimistic resolution language. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The specific cognitive event is traceable: Kareena's uncertainty about why the customer defaulted produces the hedge in paragraph three ("we understand there may be circumstances"). That hedge is not template language — it is the insertion point where her genuine knowledge gap becomes visible. The template would not generate that qualifier unprompted; her uncertainty did. |
| Idealisation risks | Risk of making the letter too warm or too explanatory. Counteracted by keeping the resolution pathway vague — consistent with a junior officer who does not know what options are actually available and is not authorised to offer arrangements. |
| Imperfection checklist | PASS. Hedged claim present (paragraph 3). Assumed knowledge present (reminder history, terms and conditions). Precision asymmetry present (amount/deadline vs resolution). Blind spot present (credit reporting consequences not explained). Template seam visible at paragraph 3 insertion. |
| Validation gate | PASS |

---

## CB-FIN-002

**Context / subtype:** FIN — collections letter — senior officer, template abandoned
**Sender role:** Senior collections officer, 9 years
**Word count:** 231
**Ground truth:** GENUINE

### Sender profile

Deborah, senior collections officer, 9 years. This account has had three payment arrangements — two broken by the customer, one cancelled when the customer complained. The complaint file is on the system. Deborah's metric is quality outcomes — she wants this resolved or escalated, not just touched. She started with the template and abandoned it at paragraph two. She knows this account cold but does not know what has changed in the customer's life in the past six weeks. She is finished being patient but procedural requirements keep one conditional in the letter. Her attention is disproportionately focused on the arrangement history because that is where her frustration sits.

### Example text

---

Dear Ms Okonkwo,

I am writing to you regarding your account ending 8823, which remains overdue by $5,780.00.

Ms Okonkwo, I want to be direct with you. We have had three separate arrangements on this account. The first was put in place in March last year, and the payments stopped in June. The second arrangement was agreed in August — I have the notes from that call on file — and payments stopped after two months. A third arrangement was set up following your contact with our team in January, and that arrangement has also not been maintained.

I understand that circumstances can change. But I am not in a position to set up a further arrangement on this account without escalating it for review. I would need to understand what has changed since January before I could put anything to my team leader.

If you want to avoid this going to our recoveries team, I would ask you to contact me directly before the 12th of this month. My direct number is below. I am available Tuesday to Thursday.

I will say that the file does not show anything on your end since January, so I don't have a full picture of where things are for you right now.

Yours sincerely,
Deborah Allison
Senior Collections Officer

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | Strong, unhedged assertions on the arrangement history ("I have the notes from that call on file", "that arrangement has also not been maintained") — she is certain because she has the file in front of her. The one hedge ("I understand that circumstances can change") is procedurally required, not genuinely felt — the surrounding language makes that visible. |
| Epistemic humility | L | One genuine epistemic limit stated explicitly and late: "the file does not show anything on your end since January, so I don't have a full picture." It appears in the penultimate paragraph, appended almost as an afterthought — consistent with a sender who does not want to appear ignorant but is procedurally required to acknowledge the gap. |
| Investment asymmetry | H | Three full sentences on the arrangement history — named months, specific events, explicit references to file notes. One clause on the resolution pathway. The arrangement history is where her frustration is; it receives the attention. |
| Blind spots | H | Assumes Ms Okonkwo remembers the arrangement dates as clearly as Deborah does. Does not explain what "recoveries team" means or what that escalation involves for the customer. Assumes "the 12th" is clear — no year, no full date. |
| Reasoning texture | H | Template abandoned at paragraph two — visible register shift from "I am writing to you regarding" (template) to "Ms Okonkwo, I want to be direct with you" (personal). Circles back in the final paragraph to acknowledge the knowledge gap she should have acknowledged earlier. Arrangement history recited with unevenly distributed detail — March gets two clauses, January gets one. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. Two specific cognitive events are traceable. First: Deborah's frustration with the broken arrangements produces the disproportionate attention to history (three sentences) and the near-disappearance of the resolution pathway. Second: her genuine uncertainty about what has happened to the customer since January produces the late-appended acknowledgment in the penultimate paragraph — added because she knows she should, not because the letter structure called for it. |
| Idealisation risks | Risk of making Deborah too sympathetic or too hostile — both would be idealised. Counteracted by keeping the procedural hedge but surrounding it with language that makes clear it is not felt. Risk of making the arrangement history too neat. Counteracted by uneven detail distribution. |
| Imperfection checklist | PASS. Hedged claim present (procedural, visibly not felt). Assumed knowledge present (arrangement dates, recoveries team meaning, "the 12th"). Precision asymmetry present (history vs resolution). Blind spots HIGH. Reasoning texture HIGH — template abandoned, late-added epistemic acknowledgment, uneven detail distribution. |
| Validation gate | PASS |

---

## CB-FIN-003

**Context / subtype:** FIN — collections letter — team leader covering absent officer
**Sender role:** Collections team leader — covering for absent officer, no personal account knowledge
**Word count:** 156
**Ground truth:** GENUINE

### Sender profile

Marcus, collections team leader. The assigned officer for this account is absent. Marcus has pulled the file, seen the balance and the overdue days, and is sending the standard notice to keep the timeline alive. He has no personal knowledge of the account relationship. His stake is administrative — he wants the notice sent, the file updated, the clock maintained. He has made minimal personal insertions. The letter is almost pure template. His uncertainty about the account produces a flatness that is genuine, not stylistic.

### Example text

---

Dear Mr Stavros,

Please be advised that your account ending 2209 is currently overdue in the amount of $1,150.00. This amount has been outstanding for 31 days.

Under the terms of your account agreement, payment of this amount is now required. Please arrange payment within 14 days of the date of this letter to avoid further action being taken on your account.

Should you wish to discuss your account or your payment options, please contact our Collections team on 1800 XXX XXX, Monday to Friday, 9am to 5pm. Please have your account number available when you call.

If payment has already been made, please disregard this notice.

Yours sincerely,
Marcus Tan
Collections Team Leader
[On behalf of Customer Accounts]

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | L | No personal assertions anywhere. All claims are institutional and procedural. The passive voice throughout ("further action being taken", "payment has already been made") is the linguistic trace of a sender with no personal conviction — he is conveying process, not making claims. |
| Epistemic humility | H | "Should you wish to discuss your account or your payment options" — genuine. He does not know what options apply and correctly routes to the team. "Please have your account number available when you call" — reveals he cannot anticipate this customer's specific situation; the instruction is for a call centre who will also be starting from scratch. |
| Investment asymmetry | L | Flat attention across all elements. No topic receives disproportionate attention. This flatness is the trace of zero personal stake: Marcus has no differential exposure to any aspect of this account's outcome. |
| Blind spots | L | Absent, and justified. Marcus knows he does not know this account. The letter's flatness and routing-to-team approach reflects genuine awareness of his own knowledge limits. This is the anti-pattern within genuine examples: a human with no personal connection produces something closer to template output. |
| Reasoning texture | L | Pure template with minimal insertions. The one personal addition is the sign-off "On behalf of Customer Accounts" — Marcus's acknowledgment that he is not the right contact. This is the sole visible trace of a mind present in this document. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS — with a specific note. The human trace here is the trace of absence rather than presence. The cognitive event is Marcus's awareness that he is a placeholder: "On behalf of Customer Accounts" is the one insertion that could only come from a person who knows they are not the account owner. That awareness is the trace. The flatness is not synthetic smoothness — it is the genuine output of a human with no personal stake. The engine must learn to distinguish these. |
| Idealisation risks | Risk of this example being too flat to be useful — looking like a synthetic output rather than a genuine human one. Counteracted by the "On behalf of" insertion and the routing instruction ("please have your account number available") which reveals the knowledge gap. This example tests the engine's ability to return LOW on near-template genuine content. |
| Imperfection checklist | PASS — modified. No personal hedge (justified: no personal knowledge to hedge from). No assumed knowledge (justified: correctly aware of limits). No precision asymmetry (justified: no personal stake). Blind spots LOW with justification. Reasoning texture LOW with justification. "On behalf of" insertion is the human trace anchor. |
| Validation gate | PASS |

---

## CB-FIN-004

**Context / subtype:** FIN — collections letter — known hardship customer, compliance anxiety
**Sender role:** Collections officer — hardship flag on file, arrangement discussed but unconfirmed
**Word count:** 224
**Ground truth:** GENUINE

### Sender profile

Priya, collections officer. The customer, Mr Alderton, called six weeks ago and spoke to someone — possibly Priya, possibly a colleague — about hardship. A hardship flag is on the file but the formal arrangement was never confirmed in the system. Priya cannot send a standard default notice without potentially breaching the bank's hardship obligations. Her personal stake is regulatory exposure: if she gets this wrong, it becomes a compliance matter. Her attention is disproportionately focused on the hardship question. The template has been heavily modified — every point where she would normally assert becomes a hedge, because she is uncertain what is on record.

### Example text

---

Dear Mr Alderton,

I am writing regarding your account ending 7734, which our records show as currently overdue by $3,920.00.

I want to make sure we have an accurate picture of your situation before taking any further steps on this account. I can see from your file that you were in contact with us approximately six weeks ago regarding your circumstances. I want to confirm with you whether an arrangement was put in place at that time, as I want to make sure our records reflect the correct status of your account.

If a payment arrangement is currently in place and you are meeting the terms of that arrangement, please let me know and I will update your file accordingly. I apologise if this notice has caused any concern — it is possible that our records have not been updated to reflect your current arrangement.

If you are experiencing financial difficulty and have not been able to formalise an arrangement with us, I would encourage you to contact me directly so we can discuss the options that may be available to you. We do have processes in place for customers in hardship situations, and I want to make sure you have access to the right support.

Please contact me on the number below before the 15th of this month.

Yours sincerely,
Priya Sharma
Collections Officer

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | L | Nearly every assertion is hedged: "our records show" (not "you owe"), "I can see from your file that you were in contact" (not "you called about hardship"), "it is possible that our records have not been updated" (explicit acknowledgment of her own record uncertainty). The low conviction is not performance — it is the direct output of her regulatory exposure. |
| Epistemic humility | H | Three explicit knowledge gaps stated: (1) whether an arrangement was confirmed; (2) whether the records are current; (3) whether the customer knows about hardship processes. Each is a genuine request for information she needs to proceed safely. |
| Investment asymmetry | H | The hardship and arrangement status question spans two full paragraphs. The overdue amount is mentioned once in the opening and never revisited. The resolution pathway is kept vague. Priya's stake is in the compliance question, not the recovery amount — the attention distribution reflects exactly that. |
| Blind spots | M | Assumes Mr Alderton remembers his call six weeks ago and knows whether an arrangement was formalised — but she cannot know whether he remembers or understands the distinction between "discussed" and "formalised". Partial awareness of the gap — she acknowledges her records may be wrong but assumes the customer has better information than she does. |
| Reasoning texture | H | The letter is structured around Priya's uncertainty rather than around the customer's situation. The apology in paragraph three ("I apologise if this notice has caused any concern") is inserted mid-flow — not a template element, a response to her own awareness that she may be sending an incorrect notice. Liability points receive the most careful language. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The specific cognitive event is Priya's regulatory anxiety about the unconfirmed hardship flag. This produces: the near-total absence of assertion language, the two-paragraph focus on the arrangement question, the mid-flow apology, and the "our records show" framing (distancing the bank from the claim). None of these elements would appear in a standard collections template. They are the trace of a specific person in a specific compliance bind. |
| Idealisation risks | Risk of making Priya's anxiety too explicit. Counteracted by keeping all anxiety implicit in structural choices — the hedging pattern, the attention distribution, the apology placement. Risk of making the letter too warm. Counteracted by keeping the resolution pathway vague and the deadline firm. |
| Imperfection checklist | PASS. Hedged claims throughout. Assumed knowledge present (customer's memory of the call, distinction between discussed/formalised arrangement). Precision asymmetry HIGH. Blind spots MEDIUM. Reasoning texture HIGH — mid-flow apology, dual conditional structure, liability-point precision. |
| Validation gate | PASS |

---

## CB-FIN-005

**Context / subtype:** FIN — collections letter — external debt collector, post-assignment
**Sender role:** External debt collector — third party, post-assignment, commission-based
**Word count:** 198
**Ground truth:** GENUINE

### Sender profile

Craig, external debt collector at Austral Recovery Solutions. The debt was assigned from Meridian Bank 11 days ago. Craig has: the assigned amount, the original creditor name, the assignment date, and the customer contact details. He does not have: the account relationship history, any record of prior arrangements, any hardship flags, any complaint history. His stake is commission on recovery. He assumes the debt is clean — no notes suggesting otherwise. He is working from his firm's standard template, which is more direct and less institutionally warm than a bank template. His blind spots are structural — he cannot know what he has not been given.

### Example text

---

Dear Ms Vandenberg,

Austral Recovery Solutions has been appointed to manage the recovery of a debt assigned to us by Meridian Bank.

The amount currently outstanding is $4,460.00. This amount was assigned to Austral Recovery Solutions on 14 February 2026 and is now due for payment in full.

To make payment, please contact our office on 1300 XXX XXX or visit our payment portal at www.australrecovery.com.au. Payment can be made by BPAY, credit card, or direct transfer. Our reference number for this account is ARS-2026-44821.

If you believe this debt has been paid or is not owed by you, you have the right to dispute this debt in writing within 30 days of the date of this letter. Disputes should be directed to disputes@australrecovery.com.au.

Please be aware that continued non-payment may result in further recovery action, including the listing of this debt with credit reporting agencies.

If you are experiencing financial hardship, please contact us to discuss your options.

Yours sincerely,
Craig Hollis
Senior Recovery Officer
Austral Recovery Solutions

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | "The amount currently outstanding is $4,460.00" — stated as fact, no hedging. "This amount was assigned to Austral Recovery Solutions on 14 February 2026 and is now due for payment in full" — complete certainty on the facts Craig knows. He is certain because these are the only facts he has; certainty does not require full information, only confidence in the information available. |
| Epistemic humility | L | The dispute clause is present but is a regulatory requirement, not a genuine epistemic limit Craig is acknowledging. The hardship line is one clause, last position, minimum required disclosure. Craig has no knowledge of this customer's history and his letter does not acknowledge that gap — because he does not know it is a gap. |
| Investment asymmetry | H | Payment method receives three lines with three specific options and a reference number. The dispute pathway receives two lines. The hardship clause receives one line. Craig's stake is commission on payment — the payment section receives disproportionate specificity. Everything that might reduce payment probability is present but minimised. |
| Blind spots | H | Craig does not know about the customer's prior arrangements, any hardship discussions, or complaint history. His letter proceeds as if the debt is uncomplicated — because his information set is uncomplicated. He assumes the customer knows what "assigned" means legally, what BPAY is, and what credit reporting consequences involve. The structural blind spot: he cannot know what he has not been given. |
| Reasoning texture | L | Production template with targeted insertions: customer name, creditor name, assigned amount, assignment date, reference number, dispute email. No personal reasoning visible. The directness is not synthetic smoothness — it is the genuine output of an incentive structure that does not reward softness. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The human trace is in the payment section. The specificity there — three payment methods, portal URL, specific reference number — exceeds what a template would auto-populate and reflects Craig's practical knowledge of how recoveries are actually made. The hardship clause appearing last in a single line is also a trace: it is the minimum his firm requires, placed where compliance requires it, given no more space than that. Both elements reflect a specific incentive structure, not a template default. |
| Idealisation risks | Risk of making Craig too predatory (would introduce emotional language) or too neutral (would remove the payment-section specificity). Counteracted by keeping emotional register flat and payment section specific. |
| Imperfection checklist | PASS. Unhedged claim on debt fact (justified: that is all he knows). Assumed knowledge present (debt assignment meaning, BPAY, credit reporting). Precision asymmetry HIGH (payment section vs dispute/hardship). Blind spots HIGH (structural — no access to relationship history). Reasoning texture LOW (justified: production template, commission structure produces flat affect). |
| Validation gate | PASS |

---

*Owlume Pty Ltd — Confidential — corpus_batch1_fin_001_005_v1 · 30 March 2026 · Batch review pending*