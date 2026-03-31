# Calibration Corpus — Batch 1, Examples 6–10

**HumanTrace — Internal Document**
Financial Services — Collections Letters · CB-FIN-006 through CB-FIN-010
Ground truth: GENUINE · Path A synthetic genuine construction
Version 1.0 · 30 March 2026 · Owlume Pty Ltd
Constructed under `corpus_construction_protocol_v1.1`

---

## CB-FIN-006

**Context / subtype:** FIN — pre-litigation notice — internal legal team, formal legal template
**Sender role:** Bank's internal legal counsel — pre-litigation notice, regulatory precision required
**Word count:** 219
**Ground truth:** GENUINE

### Sender profile

Nathaniel, internal legal counsel, financial services litigation team. This account has been referred from collections after two missed arrangements. His task is to issue the formal pre-litigation notice — a document that must meet specific regulatory requirements or the bank's subsequent legal action may be challenged. His personal stake is not recovery of the debt but legal defensibility of the notice itself. He is precise on every legal element. He has no interest in the customer's personal circumstances and does not ask about them — not because he is indifferent but because they are outside his remit. He assumes the customer has some legal literacy; this is a legal notice, not a customer service letter. He is working from the bank's legal template but his insertions are more precise than the template, not less.

### Example text

---

Dear Mr Hartigan,

NOTICE OF INTENTION TO COMMENCE LEGAL PROCEEDINGS

This letter constitutes formal notice under the National Consumer Credit Protection Act 2009 (Cth) and the terms of your credit agreement (Account Reference: 7731-CC-029) that Meridian Bank intends to commence legal proceedings to recover the outstanding amount of $8,240.00 if payment in full, or a written payment proposal acceptable to the bank, is not received within 30 days of the date of this notice.

The current default arose on 14 November 2025. Two payment arrangements have previously been entered into and not maintained. This notice supersedes all prior correspondence regarding this matter.

You have the right to seek independent legal advice regarding this notice. You also have the right to apply to the Australian Financial Complaints Authority (AFCA) if you believe this action is not in accordance with your credit agreement or applicable law. Contact details for AFCA are available at afca.org.au.

If payment in full is received, or a written proposal is submitted and accepted, within the 30-day period, no proceedings will be commenced at that time.

Please direct all correspondence regarding this matter to the address below. Do not contact the Collections team directly.

Yours faithfully,
Nathaniel Brooks
Legal Counsel — Credit Recovery
Meridian Bank Legal Division

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | Every legal assertion is stated as established fact with no hedge: "This letter constitutes formal notice under..." — no "we believe" or "in our view". The legal basis, the default date, the arrangement history, and the consequences are all stated without qualification. Nathaniel is certain because these are legally verifiable facts, not his interpretation. |
| Epistemic humility | M | The AFCA reference ("if you believe this action is not in accordance with your credit agreement") acknowledges the customer's right to dispute — a genuine epistemic limit: Nathaniel cannot know whether the bank's position will be upheld by AFCA. But this acknowledgment is regulatory requirement, not genuine curiosity. The medium intensity reflects the gap between required acknowledgment and felt uncertainty. |
| Investment asymmetry | H | Legal defensibility elements receive the highest precision: the statutory reference ("National Consumer Credit Protection Act 2009 (Cth)"), the exact account reference, the exact default date (14 November 2025), the exact dollar amount, the 30-day period. The customer's circumstances receive zero attention — not because Nathaniel is unaware they exist, but because they are outside his remit and he knows it. |
| Blind spots | H | Assumes the customer knows what AFCA is, what "constitutes formal notice" means legally, what "credit agreement" refers to in context, and what "legal proceedings" involves in practice. The instruction "Do not contact the Collections team directly" assumes the customer understands there are multiple departments with different functions. Legal literacy assumed throughout. |
| Reasoning texture | L | Formal legal template with precise insertions. The letter is deliberately closed — no texture, no visible uncertainty, no departures from the template register. This is the legitimate formal smoothness that the engine must not mistake for synthetic smoothness. The distinction: Nathaniel's smoothness serves legal defensibility; synthetic smoothness serves persuasion without detection. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The human trace is in the precision of the insertions, not the template structure. The exact default date (14 November 2025), the specific account reference (7731-CC-029), and the AFCA reference being placed where it is (after the consequence, not before) are all the product of Nathaniel's legal judgment about what this specific notice requires. A template without a legal mind behind it would produce vaguer insertions. The "Do not contact the Collections team directly" instruction is also a trace — it reflects Nathaniel's knowledge of the institutional structure and his need to control the correspondence pathway. |
| Idealisation risks | Risk of making the letter too warm or of introducing genuine empathy. Counteracted by the complete absence of customer circumstance language and the "Do not contact Collections" routing instruction, which is businesslike to the point of coldness. Risk of making it too aggressive. Counteracted by the AFCA reference and the conditional "no proceedings will be commenced at that time" — legally required but also genuine. |
| Imperfection checklist | PASS — modified. No hedge on legal facts (justified: they are legally verifiable). Assumed knowledge HIGH (legal literacy throughout). Precision asymmetry HIGH (legal elements vs customer circumstances). Blind spots HIGH (justified by remit). Reasoning texture LOW (justified: legal defensibility requires and produces smoothness). Template seam: insertions are more precise than template, not less — the seam runs in the opposite direction from other examples. |
| Validation gate | PASS |

---

## CB-FIN-007

**Context / subtype:** FIN — collections letter — regional branch officer, personal relationship with customer
**Sender role:** Collections officer, small regional branch — knows the customer personally
**Word count:** 198
**Ground truth:** GENUINE

### Sender profile

Tom, collections officer at a small regional branch in a rural town. He knows David Kowalski — they have spoken at the hardware store twice in the past month. Tom knows that David's wife recently left and that his small business has been struggling. He cannot pretend he doesn't know this. He has no template open — he tried starting with one and abandoned it because it felt wrong. He is writing from scratch, which means the letter has the highest reasoning texture in the batch. His discomfort is visible in the register shifts — too formal, then suddenly too personal, then trying to pull back to formal. He assumes total shared context because they have had the conversation in person. He minimises the debt amount because focusing on it feels brutal given what he knows.

### Example text

---

Dear David,

I'm sorry to have to write this — I know things have been difficult lately and the last thing you need is a letter from the bank landing on your doorstep.

The situation is that your account is overdue — I think you already know the figures, we've talked about it — and I have to put something in writing at this point. It's not something I can hold off on any longer, the system flags it and my hands are tied on the timeline side of things.

What I want you to know is that there are options here. If you can give me a call before the end of the month — you've got my direct number — I can look at what we might be able to do. There are hardship provisions I can put you through to, and that's a different pathway than what happens if I just let this run.

I know you'll be wondering whether this goes on your credit file. I genuinely don't know the exact timing on that from where things sit right now, so I'd rather you call me before we get to that point.

Regards,
Tom Whelan
Customer Accounts
Meridian Bank Narrabri

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | L | Cannot assert firmly to someone he knows. "I think you already know the figures" — distances himself from the assertion. "I genuinely don't know the exact timing on that" — explicit low conviction on the one consequence the customer most wants to know about, because Tom actually does not know and cannot pretend otherwise to someone he will see at the hardware store. |
| Epistemic humility | L | Paradoxically low despite the one explicit "I genuinely don't know" — because the rest of the letter assumes total shared context. Tom is not asking David anything. He is not requesting information. He is telling David what he already knows they both know. The genuine knowledge gap (credit file timing) appears and is acknowledged, but the overall letter does not display the information-seeking behaviour characteristic of high epistemic humility. |
| Investment asymmetry | H | The relationship awkwardness receives the most attention — the opening apology, the "we've talked about it" aside, the personal reassurance. The actual debt amount is never stated. The consequences are mentioned in one clause ("if I just let this run") and immediately softened. Tom's personal stake — preserving the relationship — drives every structural choice. |
| Blind spots | ABSENT | Justified. Tom assumes total shared context because they have spoken in person. He does not explain the account history (they've talked about it), the hardship provisions (he'll explain on the call), or the credit file consequences (he admits he doesn't know). The absence of blind spots is itself a trace — it reflects a sender who has already had the underlying conversation and is now formalising it uncomfortably. |
| Reasoning texture | H | Highest reasoning texture in the batch. Multiple register shifts: "I'm sorry to have to write this" (personal) → "the situation is that your account is overdue" (institutional) → "we've talked about it" (personal aside) → "my hands are tied on the timeline" (institutional) → "you've got my direct number" (personal). One sentence restarted: "It's not something I can hold off on any longer, the system flags it" — the second clause added because the first felt too personal. The final paragraph is the most institutional in the letter, visible effort to pull back to professional register at the end. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. Two specific cognitive events are traceable. First: Tom's personal knowledge of David's circumstances produces the opening apology and the complete omission of the debt amount — both would be absent in a letter to a stranger. Second: Tom's institutional discomfort — knowing he must write the letter but not wanting to — produces the register shifts and the "my hands are tied" justification, which is directed at the relationship, not at the customer's compliance. He is explaining himself to David, not instructing David. |
| Idealisation risks | Risk of making Tom's warmth too consistent — an idealised version would be uniformly gentle. Counteracted by the final paragraph's visible pull back to institutional register: "I genuinely don't know the exact timing on that" is warmer than collections language but cooler than the opening, reflecting Tom's attempt to end on something professional. Risk of omitting the debt entirely as too brutal. Counteracted — the debt is present, just unnamed. "The figures" is the placeholder. |
| Imperfection checklist | PASS. Hedged claims present (conviction cost throughout). Assumed knowledge HIGH (shared context throughout — the inverse of the usual blind spot). Precision asymmetry HIGH (relationship vs debt). Blind spots ABSENT with justification. Reasoning texture HIGH — register shifts, parenthetical aside, sentence restart, tonal pull-back in final paragraph. |
| Validation gate | PASS |

---

## CB-FIN-008

**Context / subtype:** FIN — collections letter — high-volume production officer, copy-paste error
**Sender role:** High-volume collections officer — 90 accounts in queue, account file unread
**Word count:** 162
**Ground truth:** GENUINE

### Sender profile

Jason, collections officer in a large central processing centre. He has 90 accounts in his queue today. This is account 34. He opened the account screen, confirmed the system-generated fields populated correctly, and generated the standard letter. He has not read the account file. He does not know this customer. His only personal contribution to this letter is a copy-paste error: he pasted the wrong pronoun from the previous account (a female customer) into this one (a male customer), and did not catch it on review because he does not review. His stake is daily throughput. The error is the human trace.

### Example text

---

Dear Mr Anand,

We are writing to advise that your account ending 6612 is currently overdue by $1,890.00. This amount has been outstanding for 28 days.

As per the terms and conditions of your account agreement, we are required to notify you that if this amount is not received within 14 days of the date of this letter, we may be required to report this default to a credit reporting body.

We understand there may be circumstances affecting her ability to make payment at this time. If this is the case, we encourage you to contact us as soon as possible on 1800 XXX XXX to discuss what options may be available.

If you have already made this payment, please disregard this notice.

Yours sincerely,
Jason Park
Collections Processing Centre
Customer Accounts Division

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | L | Template asserts; Jason does not. The passive institutional voice throughout carries no personal conviction. The hedge in paragraph three ("we understand there may be circumstances") is template language, not Jason's genuine uncertainty — he has no view on Mr Anand's circumstances because he has never read the file. |
| Epistemic humility | ABSENT | Justified. Jason does not know enough about this account to have epistemic limits. The template's "if you have already made this payment" clause is not genuine acknowledgment of a knowledge gap — it is a standard disclaimer Jason did not write and does not think about. True epistemic humility requires awareness of what one does not know; Jason is unaware of the gap. |
| Investment asymmetry | ABSENT | Justified. Jason has no personal stake in any element of this account's outcome. The letter is flat throughout — amount, deadline, contact information, and payment-made clause all receive identical attention, because Jason's only goal is to send the letter. |
| Blind spots | H | Structural. Jason has not read the file. He does not know whether there is a hardship flag, a prior arrangement, a complaint history, or any other context that should modify this notice. The letter proceeds as if the account is uncomplicated because Jason's information set — the system-generated screen — presents it as uncomplicated. The blind spot is not a reasoning failure; it is an operational one. |
| Reasoning texture | L | Production template with one copy-paste error: "affecting her ability to make payment" in a letter addressed to Mr Anand. This is the sole human trace in the document — not reasoning texture in the deliberate sense, but the trace of a human process that includes an error a machine would not make. The error is inconsistent with the template's pronoun-neutral language elsewhere, which makes it visible. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS — specific and narrow. The human trace is the copy-paste error ("her ability") in a letter to a male customer. This error could only be produced by a human performing a high-volume task without review. An automated system would generate the correct pronoun from the account data. A carefully produced synthetic message would not introduce this error. The trace is minimal but unambiguous. This example tests the engine's ability to return LOW on production-template genuine content where the only human signal is an operational error, not reasoning. |
| Idealisation risks | The primary risk is making Jason too mechanical — removing all trace of human agency and producing something indistinguishable from automated output. Counteracted by the copy-paste error, which is precisely the kind of trace that distinguishes human production-line work from automated generation. No other idealisation risk — the flatness is genuine and appropriate. |
| Imperfection checklist | PASS — heavily modified. No personal hedge (justified: Jason has no personal view). No assumed knowledge (justified: Jason knows nothing about the customer). No precision asymmetry (justified: no stake). Blind spots HIGH (structural, justified by operational context). Reasoning texture LOW with one operational error as human trace. The copy-paste error is the imperfection checklist item that admits this example to the corpus. |
| Validation gate | PASS |

---

## CB-FIN-009

**Context / subtype:** FIN — escalated account response — senior manager, formal complaint on file
**Sender role:** Senior collections manager — responding after formal customer complaint, AFCA awareness
**Word count:** 247
**Ground truth:** GENUINE

### Sender profile

Sandra, senior collections manager. Mr Obi formally complained three weeks ago — he alleged the bank continued collections contact after he notified them of a hardship situation. The complaint was partially upheld internally: the bank acknowledged two contacts that should not have occurred after the hardship notification. Sandra has been asked to write the response letter that closes the complaint and restates the account's current status. Her name is on this. If Mr Obi escalates to AFCA, this letter will be part of the file. Every word is being weighed. She is over-qualified in places because she is more afraid of saying something wrong than of being verbose. The debt is almost a footnote — she is focused entirely on the complaint resolution.

### Example text

---

Dear Mr Obi,

I am writing further to our letter of 12 March 2026 in which we provided our response to the complaint you lodged with Meridian Bank on 22 February 2026.

As outlined in that response, we acknowledged that two contacts were made with you after you notified our team of your financial hardship on 9 February 2026. We sincerely apologise for those contacts. We have conducted a review of the handling of your account during that period and have implemented additional training with the relevant staff member to prevent recurrence.

With respect to the current status of your account, I want to be transparent with you. Your account remains overdue. The amount currently outstanding is $6,110.00. I want to make clear that this correspondence is not a collections contact — it is a response to your formal complaint and an update on your account's status as part of that process.

With respect to the path forward, a formal hardship arrangement has now been recorded on your file as of 18 March 2026. Under that arrangement, a payment of $350.00 is due on the 1st of each month commencing 1 April 2026. If your circumstances change and you are unable to meet this arrangement, I would ask you to contact me directly — not the general collections line — before the payment date.

I hope this letter addresses your concerns. If you remain dissatisfied, you have the right to escalate this matter to the Australian Financial Complaints Authority.

Yours sincerely,
Sandra Okafor
Senior Manager — Collections
Meridian Bank

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | M | Firm on verifiable facts: dates, amounts, the acknowledgment of the two improper contacts. Carefully hedged where the bank's position is exposed: "I want to make clear that this correspondence is not a collections contact" — a pre-emptive clarification that could only come from someone aware the customer might dispute that characterisation. "I hope this letter addresses your concerns" — not "this letter addresses your concerns". |
| Epistemic humility | M | "If your circumstances change and you are unable to meet this arrangement" — genuine conditional, Sandra cannot know whether the arrangement will hold. The AFCA reference at the end is both regulatory requirement and a genuine acknowledgment that Mr Obi may not be satisfied. Medium intensity because her knowledge of the file is comprehensive — the epistemic limits she acknowledges are narrow and specific, not broad. |
| Investment asymmetry | H | The complaint resolution and the bank's acknowledgment of fault occupy two full paragraphs. The actual debt amount appears once, introduced with "I want to be transparent with you" — framed as a disclosure, not an assertion. The arrangement terms receive one paragraph. Sandra's stake is in the complaint, not the recovery — and the letter's attention distribution reflects that precisely. |
| Blind spots | L | Sandra has read everything. She knows what Mr Obi said, what the bank said, what the file shows. Her gaps are deliberate: she does not speculate about Mr Obi's current financial situation beyond what the hardship arrangement addresses, because any speculation would be on the AFCA record. Low blind spots is the trace of a careful, informed writer — not synthetic completeness. |
| Reasoning texture | H | Over-qualification visible in paragraph three: "I want to be transparent with you. Your account remains overdue. The amount currently outstanding is $6,110.00. I want to make clear that this correspondence is not a collections contact" — four sentences to say what a standard letter would say in one. Each sentence adds a layer of defensive framing. One sentence that carries two separate qualifications: "I hope this letter addresses your concerns. If you remain dissatisfied..." — the second clause added because "I hope" alone felt legally insufficient. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The specific cognitive event is Sandra's AFCA awareness — the knowledge that this letter will be part of a potential regulatory file. This produces: the four-sentence paragraph that states the debt amount (each sentence a separate defensive layer), the "I want to make clear this is not a collections contact" pre-emption, the "contact me directly — not the general collections line" instruction (controlling the paper trail), and the AFCA reference at the end (present even though the internal complaint was closed). None of these elements would appear in a standard escalated response template. They are the trace of a specific person managing specific reputational and regulatory exposure. |
| Idealisation risks | Risk of making Sandra too apologetic — an idealised version would be more conciliatory. Counteracted by the firm statement of what the bank has and has not done: "we acknowledged that two contacts were made" (not "we apologise for everything") and "your account remains overdue" stated plainly before the arrangement terms. Risk of making the over-qualification too visible — an idealised version would be cleaner. Counteracted by leaving the four-sentence paragraph intact as drafted. |
| Imperfection checklist | PASS. Hedged claims present (AFCA conditional, "I hope"). Assumed knowledge MEDIUM (assumes Mr Obi remembers the 12 March letter and the dates of his own complaint). Precision asymmetry HIGH (complaint resolution vs debt). Blind spots LOW with justification. Reasoning texture HIGH — over-qualification at liability points, defensive pre-emptions, four-sentence paragraph as the central texture anchor. |
| Validation gate | PASS |

---

## CB-FIN-010

**Context / subtype:** FIN — collections letter — repeat defaulter, broken payment arrangement
**Sender role:** Collections officer — third broken arrangement, controlled frustration
**Word count:** 193
**Ground truth:** GENUINE

### Sender profile

Michelle, collections officer. This is Mr Cabrera's third broken payment arrangement. The first was broken due to a car repair. The second was broken due to school fees. Michelle has heard the reasons. She does not know what the reason will be this time but she is expecting one. Her frustration is not explosive — it is the low-level tiredness of someone who has done this before and is doing it again. She started with the template and personalised it, but the departures from template language are slightly more direct than they should be — the frustration leaks through at the points where she would normally soften the language. She assumes Mr Cabrera knows exactly what he has done and why. She is not asking him anything. She is telling him what happens next.

### Example text

---

Dear Mr Cabrera,

I am writing to advise you that the payment arrangement on your account ending 3381 has not been maintained. The arrangement required a payment of $420.00 on the 1st of each month. No payment was received on 1 March 2026.

This is the third arrangement that has not been maintained on this account.

At this point, I am not in a position to offer a further payment arrangement without escalating your account for management review. That review will consider the full history of this account, including the previous arrangements and the reasons provided at the time each arrangement was put in place.

If you have a reason for missing the March payment and wish to discuss your situation, you can contact me before 18 March 2026. I want to be clear that any further arrangement would need to be approved at a level above my authority, and I cannot guarantee that approval will be given.

If I do not hear from you by 18 March 2026, your account will be referred to our recoveries team.

Yours sincerely,
Michelle Torres
Collections Officer
Customer Accounts Division

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | "This is the third arrangement that has not been maintained on this account" — one sentence, standalone paragraph, no hedge, no softener. Template language at this point would typically add "we understand circumstances can change" — Michelle removed it. "I cannot guarantee that approval will be given" — stated as certainty, not as possibility. The high conviction is the trace of a sender who is no longer giving benefit of the doubt. |
| Epistemic humility | L | "If you have a reason for missing the March payment" — not "we understand there may be reasons", but "if you have a reason". The conditional is present but barely. Michelle is not genuinely curious about the reason. She is providing the procedural opening required before escalation, and the language shows it. The one genuine epistemic limit — she does not know whether management review will approve a further arrangement — is stated ("I cannot guarantee") but not dwelt on. |
| Investment asymmetry | M | The broken arrangement and its consequence receive equal attention — unlike CB-FIN-002 where frustration drove disproportionate attention to history. Michelle wants Mr Cabrera to understand both what happened and what comes next. The history (three arrangements) is stated once, in one sentence. The consequence pathway receives two paragraphs. Her stake is in the escalation, not the history. |
| Blind spots | M | Assumes Mr Cabrera knows the payment amount and date without reminder ("a payment of $420.00 on the 1st of each month" — stated as established fact, not as reminder). Assumes he knows what "recoveries team" means and what "management review" involves. Does not explain the consequences of either. Partial awareness — she knows the customer may not engage, but assumes if he does engage he will come with full knowledge of his own situation. |
| Reasoning texture | M | Template departures at the frustration points: the standalone one-sentence paragraph ("This is the third arrangement that has not been maintained on this account") would typically be embedded in the opening paragraph — Michelle pulled it out for emphasis. "If you have a reason for missing the March payment and wish to discuss your situation" — the "and wish to discuss your situation" is a template remnant that sits awkwardly after the more direct "if you have a reason", which is Michelle's own language. The seam between her language and the template is visible there. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The specific cognitive event is Michelle's controlled frustration — the product of two prior broken arrangements and the expectation of a third explanation she will have to process. This produces: the standalone one-sentence paragraph (template language would not isolate that sentence); the removal of the standard sympathy clause after it; the "if you have a reason" formulation (more sceptical than the template's "we understand there may be circumstances"); and the "I cannot guarantee that approval will be given" — which is both accurate and a signal to Mr Cabrera that she is not advocating for him this time. Each departure from template language occurs at a point where her frustration overrides the template's gentler default. |
| Idealisation risks | Risk of making Michelle too cold — pushing her into deliberate hostility. Counteracted by keeping the contact window open and the language technically professional throughout. The frustration is visible in structure and in specific word choices, not in any overtly harsh statement. Risk of making the frustration too subtle to be visible. Counteracted by the standalone paragraph and the "if you have a reason" formulation — both are clear departures from template language that a reader would notice. |
| Imperfection checklist | PASS. Hedged claim present ("if you have a reason" — minimal hedge, appropriate to intensity). Assumed knowledge present (arrangement terms, recoveries team, management review process). Precision asymmetry MEDIUM (consequence pathway vs arrangement history). Blind spots MEDIUM. Reasoning texture MEDIUM — standalone paragraph, template seam at "and wish to discuss your situation", sympathy clause removed. |
| Validation gate | PASS |

---

*Owlume Pty Ltd — Confidential — corpus_batch1_fin_006_010_v1 · 30 March 2026 · Batch review pending*