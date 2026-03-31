# Calibration Corpus — Batch 2, Examples 11–20

**HumanTrace — Internal Document**
Financial Services — Lending Decisions / Notices · CB-FIN-011 through CB-FIN-020
Ground truth: GENUINE · Path A synthetic genuine construction
Version 1.0 · 30 March 2026 · Owlume Pty Ltd
Constructed under `corpus_construction_protocol_v1.1`

---

## CB-FIN-011

**Context / subtype:** FIN — lending notice — conditional loan approval, credit analyst
**Sender role:** Credit analyst — conditional approval, owns the conditions assessment
**Word count:** 198
**Ground truth:** GENUINE

### Sender profile

Rachel, credit analyst. She has assessed the application and approved the loan subject to three conditions. She is confident in the approval but she is not fully confident the conditions are sufficient — if the property valuation comes in low, the whole structure changes. Her stake is the conditions: if the loan defaults, her assessment will be reviewed. She has inserted the conditions with more precision than the template requires because that precision is her professional protection.

### Example text

---

Dear Mr and Mrs Papadopoulos,

We are pleased to advise that your application for a home loan of $620,000 has been approved, subject to the following conditions. Please read these conditions carefully, as the approval is conditional on all three being satisfied prior to settlement.

**Condition 1 — Valuation:** An independent valuation of the security property must be completed by a panel valuer approved by Meridian Bank. The approval is based on an assumed property value of $775,000. If the valuation result is materially below this figure, the approved loan amount and loan-to-value ratio will be reassessed.

**Condition 2 — Income verification:** Current payslips dated within 30 days of settlement must be provided for both applicants. The income figures used in this assessment were those provided in your application. Any material change to income between now and settlement must be disclosed to us immediately.

**Condition 3 — Discharge of existing liability:** Evidence of discharge of the personal loan ending 8821 must be provided prior to settlement. This liability was included in the serviceability assessment and its discharge is a requirement of this approval.

Please contact your lending manager if you have questions about any of these conditions.

Yours sincerely,
Rachel Osei
Credit Analyst
Home Lending — Meridian Bank

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | M | Confident on the approval itself ("we are pleased to advise that your application...has been approved"). Immediately conditional — the approval is hedged by three conditions, each of which reflects genuine uncertainty about whether the approval structure will hold. "If the valuation result is materially below this figure, the approved loan amount...will be reassessed" — the hedge is genuine, not formulaic. Rachel does not know the valuation outcome. |
| Epistemic humility | M | Condition 1 reflects genuine uncertainty about the property valuation. Condition 2 reflects genuine uncertainty about income stability between approval and settlement. "Any material change to income between now and settlement must be disclosed to us immediately" — she is explicitly asking for information she does not yet have. These are not standard boilerplate conditions; they reflect the specific gaps in her certainty about this application. |
| Investment asymmetry | H | The three conditions — particularly their precise formulation — receive the most detailed language in the letter. The approval itself is one sentence. The conditions are three structured paragraphs with specific figures, timeframes, and account references. Rachel's stake is in the conditions; her professional protection is in their precision. |
| Blind spots | H | Assumes the Papadopouloses understand what LVR means, what a panel valuer is, what "discharge of liability" involves practically, and why the personal loan matters to the serviceability assessment. None of these are explained. The letter assumes financial literacy consistent with a customer who has engaged a mortgage broker or is familiar with the lending process. |
| Reasoning texture | L | Formal template with precise insertions. The conditions are structured and closed — each condition has a clear trigger, requirement, and consequence. The precision is Rachel's but the structure is the template's. The only visible texture is the specificity of the insertions relative to what a generic template would produce — the account number (8821), the specific assumed property value ($775,000), the 30-day payslip window. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The human trace is in the specificity of the conditions — particularly the assumed property value ($775,000) and the specific personal loan account (8821). These figures are Rachel's assessment, not template defaults. A template would produce generic conditions; Rachel's professional judgment produced these specific figures and this specific structure. The "if the valuation result is materially below this figure" language is also a trace — "materially" is a judgment word, not a system-generated threshold. |
| Idealisation risks | Risk of making the conditions too generic — losing the specificity that carries Rachel's professional trace. Counteracted by using specific figures throughout. Risk of making the approval too warm. Counteracted by the clinical condition structure with no relationship language anywhere in the letter. |
| Imperfection checklist | PASS. Hedged claim present (valuation conditional). Assumed knowledge HIGH (LVR, panel valuer, liability discharge). Precision asymmetry HIGH (conditions vs approval statement). Blind spots HIGH. Reasoning texture LOW with justification — professional protection requires precise, closed condition language. Template seam visible in the precision of insertions relative to surrounding template structure. |
| Validation gate | PASS |

---

## CB-FIN-012

**Context / subtype:** FIN — lending notice — loan decline, mortgage broker delivering lender decision
**Sender role:** Mortgage broker — delivering lender's decline, does not have lender's full reasoning
**Word count:** 211
**Ground truth:** GENUINE

### Sender profile

David, mortgage broker. His client, Ms Petrov, has been declined by the lender. David received the decline notification through the lender's broker portal — he has the reason code (CB04: insufficient serviceability based on existing commitments) but not the detailed reasoning behind it. He did not make this decision. His stake is the relationship with Ms Petrov — he will keep working with her, possibly with a different lender or after addressing the serviceability issue. He is delivering news he cannot fully explain, and the letter reflects that gap.

### Example text

---

Dear Ms Petrov,

I'm writing to let you know that your application with Harbour Lending has been assessed and unfortunately has not been approved at this time.

The reason provided by Harbour Lending is that the application did not meet their serviceability requirements based on your current financial commitments. I want to be upfront with you that this is the reason code provided to me through their assessment system — I don't have visibility into the detailed reasoning behind their decision, and I'm not in a position to give you a more specific explanation than what they've provided.

I know this isn't the news you were hoping for, and I want to make sure we use this as a starting point rather than a full stop. There are a few things I'd like to talk through with you: whether there are other lenders whose serviceability calculations might produce a different result, whether addressing any of your current commitments before reapplying might improve the outcome, and whether the loan structure we applied with is the right one for your situation.

I'll call you this week to have that conversation. In the meantime, if you have questions or just want to talk it through, please don't hesitate to reach out.

Warm regards,
David Nakamura
Principal Broker
Nakamura Lending Solutions

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | L | David is reporting someone else's decision. "The reason provided by Harbour Lending is..." — he is quoting, not asserting. "I don't have visibility into the detailed reasoning behind their decision" — explicit acknowledgment that he cannot vouch for the completeness of what he is conveying. The low conviction is structural — he genuinely cannot assert a decision he did not make. |
| Epistemic humility | H | "I'm not in a position to give you a more specific explanation than what they've provided" — explicit epistemic limit, stated upfront. The three options he outlines for next steps are framed as possibilities to "talk through", not as recommendations — he does not know which applies until he has the conversation. The call at the end is an information-gathering step, not a follow-through on a recommendation already made. |
| Investment asymmetry | H | The path forward — the three options and the offer to call — receives more space than the decline itself. The decline is delivered in one sentence. The reason code explanation is one paragraph. The forward-looking framing is one paragraph. David's stake is in the relationship; that stake drives the attention toward what comes next rather than what just happened. |
| Blind spots | M | Assumes Ms Petrov knows what "serviceability" means in a lending context, what "current commitments" refers to specifically, and why a different lender might produce a different result. He does not explain the serviceability calculation. Medium intensity — he is somewhat more aware of his client's potential confusion than a bank officer would be, which is why he offers to "talk through" rather than simply listing options. |
| Reasoning texture | M | The seam between the reported decision (lender's language) and David's own framing is visible throughout. "Unfortunately has not been approved at this time" — the "at this time" is David's softener, not lender language. The three options are hedged as things "I'd like to talk through" rather than stated as recommendations — David has not yet assessed which applies because he has not had the conversation. The offer to call is both genuine and a mechanism to gather the information he needs to actually advise. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The specific cognitive event is David's awareness that he is a messenger without full information. This produces: the explicit epistemic disclaimer ("I don't have visibility into the detailed reasoning"), the three options framed as conversation starters rather than recommendations, and the call offer (which is both relationship management and information gathering). A template decline letter would deliver the reason code and close. David's professional stake in the ongoing relationship produces everything after the reason code. |
| Idealisation risks | Risk of making David too apologetic — an idealised version would be more sympathetic. Counteracted by keeping the decline delivery direct in the first paragraph and the forward framing practical rather than emotional. Risk of making the three options too specific — an idealised version would have David recommend one path clearly. Counteracted by framing all three as things to talk through, reflecting his genuine uncertainty about which applies. |
| Imperfection checklist | PASS. Low conviction on decline (justified: reported decision). Epistemic limit stated explicitly. Precision asymmetry HIGH (forward path vs decline reason). Assumed knowledge MEDIUM. Reasoning texture MEDIUM — seam between reported language and personal framing visible throughout. |
| Validation gate | PASS |

---

## CB-FIN-013

**Context / subtype:** FIN — lending notice — partial approval, senior credit manager explains reasoning
**Sender role:** Senior credit manager — partial approval, reduced loan amount, owns the decision
**Word count:** 234
**Ground truth:** GENUINE

### Sender profile

Joanna, senior credit manager. Mr Svensson applied for $480,000. She approved $360,000. The serviceability analysis showed the higher amount was outside her comfort zone given the customer's income structure — self-employed, two years of financials, one of which was a COVID-affected year. She is not going to apologise for the reduced amount but she wants the customer to understand the reasoning. She owns this decision. She has written it herself with no template.

### Example text

---

Dear Mr Svensson,

Thank you for your home loan application. I have completed the assessment of your application and I'm writing to let you know the outcome and the reasoning behind it.

Your application has been approved for a loan amount of $360,000. I want to be direct with you about why this is lower than the amount you applied for.

The assessment considered two years of financial statements for your business. The 2022 financial year showed a significant reduction in net profit compared to 2023, which I understand was related to the period of disruption that affected many businesses. In assessing serviceability, I used an average of the two years rather than the most recent year alone. That averaged figure produces a serviceability outcome that supports a loan of $360,000 but not $480,000.

I want to be honest with you: if your 2024 financials — which won't be available until later this year — show a continuation of the recovery visible in 2023, that would change the assessment. You would be welcome to reapply once those financials are available.

The approved amount of $360,000 may or may not meet your needs for this purchase. If it doesn't, I understand, and I'd rather you know the full picture now than proceed with a loan structure that doesn't work for you.

Please feel free to contact me directly if you have questions.

Yours sincerely,
Joanna Bergström
Senior Credit Manager
Meridian Bank

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | "I have completed the assessment...I'm writing to let you know the outcome and the reasoning behind it" — she owns the decision personally throughout. The averaging methodology is stated as her choice ("I used an average of the two years") not as "bank policy". "I want to be honest with you" — the framing of honesty implies she is aware the customer may not like what follows, and she is choosing to say it anyway. High conviction throughout — this is her decision, she stands behind it. |
| Epistemic humility | M | "If your 2024 financials...show a continuation of the recovery visible in 2023, that would change the assessment" — genuine conditional. She does not know what the 2024 financials will show. She is acknowledging a future information state that could change her decision. The medium intensity reflects the fact that she is confident in her current decision while acknowledging the limits of the information available to her. |
| Investment asymmetry | H | The serviceability reasoning — the averaging methodology, the two-year period, the COVID year's impact — receives three sentences of explanation. The approved amount is stated in one sentence. The reapplication pathway receives two sentences. Joanna's stake is in ensuring the customer understands the reasoning; the reasoning paragraph receives the most attention. |
| Blind spots | M | Assumes Mr Svensson understands what serviceability means in this context, what averaging two years of financials produces, and why the COVID-affected year affects the outcome. She explains the COVID year's impact but does not explain what serviceability means or how the averaging methodology works mechanically. Partial awareness — she is more explanatory than a standard letter but not fully explanatory. |
| Reasoning texture | H | Written without a template — the reasoning is visible throughout. "I want to be direct with you about why this is lower" — she anticipated the customer's question and addresses it before he asks it. "The approved amount of $360,000 may or may not meet your needs for this purchase. If it doesn't, I understand" — she is acknowledging a possible outcome (the customer doesn't proceed) and releasing him from obligation. This is reasoning texture produced by genuine deliberation about what this customer needs to hear. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. Two specific cognitive events are traceable. First: Joanna's professional ownership of the decision — "I used an average" rather than "the bank's policy requires" — is the trace of someone who made a judgment call and is prepared to explain it personally. Second: the penultimate paragraph ("The approved amount may or may not meet your needs") reflects Joanna's genuine uncertainty about whether the reduced amount is useful to this customer — she does not know what the property costs or what flexibility the customer has. That uncertainty produces the most human sentence in the letter. |
| Idealisation risks | Risk of making Joanna too sympathetic — softening the decision to the point where the reasoning becomes apologetic. Counteracted by keeping "I want to be direct" as the framing and stating the serviceability methodology plainly. Risk of over-explaining the methodology to the point of sounding defensive. Counteracted by limiting the serviceability explanation to three sentences and then moving to the reapplication pathway. |
| Imperfection checklist | PASS. Hedged claim present (2024 financials conditional). Assumed knowledge MEDIUM (serviceability concept, averaging methodology). Precision asymmetry HIGH (reasoning vs approval statement). Blind spots MEDIUM. Reasoning texture HIGH — no template, personal ownership throughout, deliberation visible in penultimate paragraph. |
| Validation gate | PASS |

---

## CB-FIN-014

**Context / subtype:** FIN — lending notice — loan decline, junior lender, first time declining this customer
**Sender role:** Junior lender — delivering decline to existing customer, uncomfortable with the decision
**Word count:** 189
**Ground truth:** GENUINE

### Sender profile

Ben, junior lender, 14 months in the role. Mr and Mrs Tran have banked with Meridian for eleven years. Ben has handled their accounts for the past eight months. He likes them. This is the first time he has had to decline a loan application from a customer he knows. The system generated the decline reason — insufficient deposit for the requested LVR — and Ben is required to communicate it. He did not make the decision. He does not fully understand all the factors behind it. He wants to soften it without misleading them and he is not sure he has found the right balance.

### Example text

---

Dear Mr and Mrs Tran,

Thank you for your application and for the time you spent with me last week going through everything. I'm sorry that I'm not writing with better news.

Your application has been assessed and unfortunately it has not been approved. The assessment outcome relates to the deposit amount relative to the property value being applied for — the deposit provided does not meet the minimum requirement for the loan-to-value ratio at the requested loan amount.

I want to be honest with you that I'm limited in how much detail I'm able to provide beyond what's in the assessment outcome. If you'd like a more detailed explanation, you have the right to request that in writing and I can make sure that gets to the right person.

The situation isn't necessarily permanent. If the property value were assessed differently, or if additional savings were available, the picture could look different. I'd really like to help you work through what the options might be if you're open to that conversation.

Please give me a call when you're ready — there's no pressure, just whenever suits you.

Warm regards,
Ben Lawson
Lender
Meridian Bank Chatswood

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | L | Ben is delivering a decision he did not make and cannot fully explain. "The assessment outcome relates to..." — institutional passive, not personal assertion. "I'm limited in how much detail I'm able to provide beyond what's in the assessment outcome" — explicit low conviction on the explanation he is offering. He cannot vouch for the completeness of what he is conveying. |
| Epistemic humility | H | "If you'd like a more detailed explanation, you have the right to request that in writing and I can make sure that gets to the right person" — he is explicitly routing the question to someone who knows more than he does. "The situation isn't necessarily permanent. If the property value were assessed differently, or if additional savings were available, the picture could look different" — genuine conditional, he does not know which of these applies or whether either would be sufficient. |
| Investment asymmetry | M | The relationship reassurance and the forward-looking options receive more space than the decline reason itself. The decline is one sentence. The explanation limitation is one sentence. The options are two sentences. The relationship close ("please give me a call when you're ready — there's no pressure") is one sentence that carries the most personal weight in the letter. Ben's stake is the relationship; that stake produces the extra space given to the forward framing. |
| Blind spots | M | Assumes the Trans know what LVR means and why the deposit amount is relevant to it. Does not explain the minimum LVR requirement or what it would take to meet it precisely. Medium intensity — Ben is somewhat aware they may not fully understand, which is why he offers to have the conversation, but he does not explain the mechanism in the letter. |
| Reasoning texture | M | The discomfort is visible at the insertion points where the template language and Ben's personal language meet. "Unfortunately it has not been approved" — the "unfortunately" is Ben's insertion into what would otherwise be institutional passive. "I'd really like to help you work through what the options might be" — "really" is not template language. "There's no pressure, just whenever suits you" — the second clause was added because the first felt insufficient. The over-softening at these points is the texture of someone managing a relationship while delivering bad news. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The specific cognitive event is Ben's discomfort — knowing these customers personally and being required to deliver a decision he cannot fully explain. This produces: the opening apology ("I'm sorry that I'm not writing with better news"), the explicit epistemic disclaimer about his information limits, the routing to someone who knows more, and the relationship close ("there's no pressure, just whenever suits you"). Each of these would be absent from a standard decline template. They are the trace of a specific person managing a specific relationship tension. |
| Idealisation risks | Risk of making Ben too apologetic — over-softening to the point where the decline is unclear. Counteracted by keeping the decline statement direct in paragraph two despite the softened framing around it. Risk of making the forward options too specific — an idealised version would have Ben know exactly what the Trans need to do. Counteracted by framing the options as conditionals ("if the property value were assessed differently...the picture could look different") rather than recommendations. |
| Imperfection checklist | PASS. Low conviction throughout (justified). Epistemic limit stated explicitly. Precision asymmetry MEDIUM. Assumed knowledge MEDIUM. Reasoning texture MEDIUM — over-softening at insertion points, relationship close as texture anchor. |
| Validation gate | PASS |

---

## CB-FIN-015

**Context / subtype:** FIN — lending notice — loan variation approval, straightforward increase
**Sender role:** Credit officer — routine loan variation approval, low personal stake
**Word count:** 152
**Ground truth:** GENUINE

### Sender profile

Amy, credit officer. Ms Lindqvist requested an increase to her existing home loan of $45,000 for a renovation. The assessment was clean — her income has increased since the original loan, the LVR is comfortable, no issues. Amy approved it. Her stake is administrative. She has not thought about why Ms Lindqvist wants the money or what the renovation is. She is working from the standard variation approval template. This is a routine approval and the letter reflects that.

### Example text

---

Dear Ms Lindqvist,

We are pleased to advise that your request to increase your home loan (Account 9934) by $45,000 has been approved.

The revised loan amount is $387,000. Your new monthly repayment will be $2,104.00, based on the current variable interest rate of 6.24% per annum. Please note that if the interest rate changes, your repayment amount will be adjusted accordingly.

The additional funds will be available for drawdown within 3 business days of the date of this letter, once you have confirmed your acceptance of these revised terms by returning the enclosed variation agreement.

If you have any questions about the revised terms or the drawdown process, please contact your lending manager on the number below.

Yours sincerely,
Amy Chen
Credit Officer
Meridian Bank Home Lending

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | M | Confident on the approval and the financial terms. The one hedge: "Please note that if the interest rate changes, your repayment amount will be adjusted accordingly" — this is a genuine disclosure of uncertainty about future repayment amounts, not boilerplate. Amy does not know where interest rates will go and the disclosure reflects that real unknown. Otherwise the letter is appropriately confident on matters she knows. |
| Epistemic humility | L | No genuine information gaps acknowledged. Amy knows what she approved, on what terms, and what the customer needs to do next. The letter is complete because the decision is complete. Low epistemic humility is appropriate here — she has the full picture and is conveying it. |
| Investment asymmetry | L | Flat attention across all elements — approval, revised amount, repayment, drawdown timeline, and contact information all receive roughly equal weight. Amy has no differential stake in any element of this outcome. The flatness is appropriate to a routine approval with no personal exposure. |
| Blind spots | H | Does not explain what "variable interest rate" means in practice, what happens if Ms Lindqvist cannot make the new repayment amount, what the variation agreement involves, or what "drawdown" means for someone who has not drawn additional funds before. Assumes the customer has navigated the original loan process and will find these concepts familiar. |
| Reasoning texture | L | Clean template with factual insertions. No personal language, no register shifts, no departures from template structure. Appropriate to a routine administrative approval — the flatness is genuine, not synthetic. The interest rate disclosure is the only element that carries any real-world uncertainty and it is handled in a single standard clause. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS — minimal but present. The human trace is the interest rate disclosure clause. A fully automated letter would still include this, but Amy's insertion of the specific current rate (6.24%) and the resulting specific repayment ($2,104.00) requires a human to have looked at the current rate schedule and done the calculation. The specificity of these figures is Amy's contribution, not the template's. This is a CB-FIN-003-style example for the lending context: a genuine human producing near-template output with minimal personal stake. The engine must return LOW. |
| Idealisation risks | The primary risk is making this example too interesting — adding warmth or explanation that Amy would not produce. Counteracted by keeping the letter entirely within the template register with no personal additions. The interest rate disclosure is the only non-obvious insertion. |
| Imperfection checklist | PASS — modified. One genuine uncertainty present (interest rate variability). No assumed knowledge gaps that create information problems — the gaps are standard and appropriate to a sophisticated borrower. Precision asymmetry ABSENT (justified: flat stake). Reasoning texture LOW (justified: routine approval). Human trace: specific rate and repayment figures as Amy's calculation contribution. |
| Validation gate | PASS |

---

## CB-FIN-016

**Context / subtype:** FIN — lending notice — policy exception refused, risk analyst
**Sender role:** Risk analyst — exception request refused on policy grounds, audit awareness
**Word count:** 187
**Ground truth:** GENUINE

### Sender profile

Claire, risk analyst. Mr Okonkwo's broker submitted a request for a policy exception — specifically, to allow the loan to proceed with a non-standard income verification approach because Mr Okonkwo is a recently arrived skilled migrant with overseas income history but limited Australian income documentation. Claire reviewed the exception request and declined it — the policy is clear, the exception criteria are not met, and she is not prepared to create an audit finding by granting an exception that cannot be justified. She has no personal stake in whether Mr Okonkwo gets the loan. Her stake is policy compliance.

### Example text

---

Dear Mr Okonkwo,

We have received and considered your request, submitted through your broker, for a policy exception to the standard income verification requirements applicable to your loan application.

Having reviewed the exception request against Meridian Bank's lending policy framework, I am writing to advise that the exception cannot be approved.

The income verification requirement applicable to your application is set out in Section 4.2(c) of the Residential Lending Policy. The exception criteria in Section 7.1 of that policy provide for exceptions in three defined circumstances. Having reviewed your application against those criteria, I am not satisfied that the circumstances of your application meet any of the three defined exception grounds.

This decision does not affect your ability to submit a standard application once you have accumulated the required period of Australian income history, which under the current policy is 12 months of continuous employment with an Australian employer.

If you believe this assessment is incorrect, you may request a review by writing to the Credit Review team at the address below. Your broker has access to the relevant policy documents and can assist you in understanding the specific requirements.

Yours faithfully,
Claire Whitfield
Risk Analyst — Credit Policy
Meridian Bank

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | "I am not satisfied that the circumstances of your application meet any of the three defined exception grounds" — personal judgment stated with full confidence. No hedge. Claire is certain because the policy framework is clear and she has reviewed it. "The exception cannot be approved" — direct, no softener. The high conviction reflects the clarity of her policy position, not indifference to the customer's situation. |
| Epistemic humility | L | Claire has the policy, she has the application, she has reviewed both. She is not uncertain about the answer. The one genuine epistemic limit — whether Mr Okonkwo's understanding of the policy requirements is accurate — is addressed by routing him to his broker ("your broker has access to the relevant policy documents"). She is not curious about the customer's circumstances; the policy answer is the answer. |
| Investment asymmetry | H | The policy basis for the decline receives three sentences with specific section references (Section 4.2(c), Section 7.1). The customer's path forward receives two sentences. Claire's stake is in the policy compliance documentation — the specific section references are her professional protection, ensuring the decision is traceable to the policy framework rather than to her personal judgment. |
| Blind spots | H | Assumes Mr Okonkwo and his broker understand what Section 4.2(c) and Section 7.1 contain, what the three defined exception grounds are, and why his application does not meet them. The letter does not explain the exception grounds — it references them by section number and asserts they are not met. This is a significant expertise blind spot in a context where the customer may not have access to the policy documents. |
| Reasoning texture | L | Formal policy language throughout. Closed and precise. The policy section references, the specific exception criteria structure, and the appeal pathway are all delivered without visible deliberation. This is legitimate smoothness — the smoothness of a decision that is clear under the applicable framework. The engine must not mistake policy precision for synthetic smoothness. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The human trace is in the specific section references (Section 4.2(c), Section 7.1) and the structure of "three defined exception grounds." A template decline would say "your application does not meet our policy requirements." Claire's version names the specific sections and the specific exception structure — because those references are her audit trail, the evidence that her decision is policy-compliant. That precision is Claire's professional self-protection made visible in the letter. |
| Idealisation risks | Risk of making Claire too cold — adding no acknowledgment of the customer's situation. Counteracted by the path-forward paragraph, which is genuine (not a formality — Mr Okonkwo can reapply) and is included because Claire's policy position is not personal. Risk of including sympathy language that Claire would not write. Counteracted by keeping the tone consistently formal and policy-focused throughout. |
| Imperfection checklist | PASS — modified. No personal hedge (justified: policy is clear). Assumed knowledge HIGH (policy documents, section references, exception structure). Precision asymmetry HIGH (policy basis vs path forward). Reasoning texture LOW (justified: policy compliance requires and produces precision). Human trace: specific section references as audit-trail protection. |
| Validation gate | PASS |

---

## CB-FIN-017

**Context / subtype:** FIN — lending notice — home loan approval, first home buyer
**Sender role:** Home loan specialist — first home buyer approval, positive stake, personal addition
**Word count:** 213
**Ground truth:** GENUINE

### Sender profile

Sophie, home loan specialist. She has specialised in first home buyer lending for six years. She is genuinely pleased when first home buyers are approved — it is the part of the job she finds meaningful. She always adds a personal note to first home buyer approval letters. The Nguyens are in their late twenties, applied together, good application. Sophie is aware the settlement process can be overwhelming for first buyers and she always includes a brief heads-up about what comes next. Her personal addition is slightly warmer than the surrounding template language — the seam is visible but gentle.

### Example text

---

Dear Mr and Mrs Nguyen,

Congratulations — your home loan application has been approved.

We are pleased to confirm that your application for a home loan of $530,000 has been assessed and approved. Your loan will be established at the current variable rate of 6.18% per annum, with a monthly repayment of $3,229.00.

Your application has also been assessed for eligibility under the First Home Owner Grant scheme. Based on the information provided, you appear to be eligible for the grant, and the relevant documentation has been forwarded to the State Revenue Office. Please note that final determination of eligibility rests with the State Revenue Office, not with us, and we will advise you once their confirmation is received.

Settlement will be coordinated through our settlements team once your solicitor confirms the settlement date. I'd encourage you to stay in close contact with your solicitor over the coming weeks — the settlement process involves a number of steps that can feel like a lot when you're doing it for the first time, and it helps to have your questions answered quickly.

Congratulations again — this is a significant step and it has been a pleasure working with your application.

Yours sincerely,
Sophie Lam
Home Loan Specialist — First Home Buyers
Meridian Bank

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | Confident on the approval, the terms, and the FHOG eligibility assessment. The one careful hedge: "you appear to be eligible for the grant" and "final determination of eligibility rests with the State Revenue Office, not with us" — Sophie cannot determine FHOG eligibility definitively and she knows it. The hedge is genuine and positioned precisely where her certainty ends. |
| Epistemic humility | M | The FHOG eligibility hedge reflects genuine uncertainty — Sophie has assessed based on the application but the final determination is not hers to make. The settlement process note ("the settlement process involves a number of steps that can feel like a lot when you're doing it for the first time") reflects genuine awareness that the Nguyens may not know what is coming — she is providing information she genuinely thinks they need. Medium rather than high — she knows the outcome; the gaps are specific and bounded. |
| Investment asymmetry | M | The FHOG eligibility section receives slightly more attention than the approval terms — Sophie's awareness that this is important to first home buyers and that the outcome is uncertain drives a small attention imbalance. The personal note at the end ("it has been a pleasure working with your application") is brief but carries disproportionate warmth for its length — Sophie's genuine positive stake in this outcome visible in one sentence. |
| Blind spots | M | Does not explain what the FHOG grant involves financially, what the solicitor's role in settlement is, or what "a number of steps" means specifically. The settlement note acknowledges the Nguyens may not know what is coming but does not fully bridge the knowledge gap — Sophie is pointing at the gap and routing them to the solicitor rather than filling it herself. |
| Reasoning texture | M | Sophie's personal addition — the settlement encouragement paragraph — is slightly warmer in register than the surrounding template language. "It helps to have your questions answered quickly" is Sophie's own language, not template. The personal closing ("it has been a pleasure working with your application") is the visible seam between template and personal addition. The FHOG hedge is the most carefully worded element in the letter — Sophie has written it precisely because she has seen customers assume FHOG eligibility and be disappointed by the SRO determination. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. Three specific cognitive events are traceable. First: Sophie's genuine positive stake produces the opening "congratulations" and the personal closing — both absent from standard approval templates. Second: Sophie's awareness of first-buyer settlement anxiety produces the settlement note — she has seen this anxiety before and proactively addresses it. Third: Sophie's careful FHOG hedge reflects specific experience with the SRO determination process — she knows from experience that "appears eligible" and "is eligible" are different things, and she has learned to communicate that distinction. |
| Idealisation risks | Risk of making Sophie's warmth too uniform — an idealised version would be warm throughout. Counteracted by keeping the approval terms and FHOG eligibility in template language and reserving the personal tone for the settlement note and the closing. The seam between template and personal is what makes the personal addition genuine rather than performed. |
| Imperfection checklist | PASS. Hedged claim present (FHOG eligibility). Assumed knowledge MEDIUM (FHOG process, solicitor role, settlement steps). Precision asymmetry MEDIUM (FHOG section and settlement note vs approval terms). Blind spots MEDIUM. Reasoning texture MEDIUM — personal addition as seam, FHOG hedge as careful language, settlement note as first-buyer awareness. |
| Validation gate | PASS |

---

## CB-FIN-018

**Context / subtype:** FIN — lending notice — loan decline, income verification failure, ambiguous intent
**Sender role:** Credit manager — decline with careful handling of ambiguous income documentation
**Word count:** 226
**Ground truth:** GENUINE

### Sender profile

Karen, credit manager. Mr Batista's application was declined because the income documentation he submitted was inconsistent — his payslips and his tax return showed materially different income figures, and the tax return figure produces a serviceability failure. Karen does not know whether this is a genuine documentation error (wrong documents submitted, or documents from different periods), a misunderstanding of requirements, or a deliberate misrepresentation. She cannot assert intent. Her stake is careful handling — if it is a genuine error, harsh language damages an otherwise salvageable application; if it is deliberate, she needs to have handled it correctly for any future file review. She has modified the standard decline template significantly.

### Example text

---

Dear Mr Batista,

Thank you for your home loan application. I'm writing to let you know that your application has not been approved following our assessment of your income documentation.

During the assessment, we identified a material difference between the income shown on the payslips provided and the income shown on your most recent tax return. Our assessment uses the lower of these figures where a discrepancy exists, and the income figure derived from your tax return does not support the requested loan amount.

I want to be straightforward with you about what this means and what your options are. It's possible that the documents submitted reflect income from different periods or that there has been a misunderstanding about which documents were required — if that's the case, I'd encourage you to contact us so we can clarify what documentation would be needed for a reassessment. Alternatively, if there has been a change in your income between the periods shown, that would also be worth discussing.

I'm not in a position to say more than this about the reasons for the discrepancy, and I wouldn't want to make assumptions about your situation without giving you the opportunity to provide clarification.

If you would like to discuss this further, please contact me directly on the number below.

Yours sincerely,
Karen Mensah
Credit Manager
Meridian Bank Home Lending

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | M | Firm on the decline and the reason: "we identified a material difference", "the income figure derived from your tax return does not support the requested loan amount" — no hedge on the factual basis. Deliberately careful on the interpretation: "it's possible that the documents submitted reflect income from different periods or that there has been a misunderstanding" — she cannot assert intent and does not. The medium intensity reflects genuine asymmetry: certain on facts, uncertain on interpretation. |
| Epistemic humility | H | "I'm not in a position to say more than this about the reasons for the discrepancy, and I wouldn't want to make assumptions about your situation without giving you the opportunity to provide clarification" — explicit, genuine epistemic limit on the intent question. She has the documents; she does not have the explanation. The two options she offers ("documents from different periods" and "a change in your income") reflect the two innocent explanations — she is explicitly not naming the third. |
| Investment asymmetry | H | The income discrepancy and its handling receive three careful paragraphs. The decline statement is one sentence. Karen's stake is in handling the intent question correctly — that question gets maximum attention. The two innocent explanations receive more space than the decline reason itself, because her professional need is to have handled this fairly regardless of what the explanation turns out to be. |
| Blind spots | M | Assumes Mr Batista knows which documents he submitted, what period they cover, and what the difference between payslip income and tax return income means in practice. Medium intensity — Karen is more aware than usual that the customer may be confused about what went wrong, which is why she explicitly offers to clarify the documentation requirements. |
| Reasoning texture | H | The deliberate avoidance of the third interpretation (misrepresentation) is the highest-texture element in the letter — it is visible in what Karen does not say. "I'm not in a position to say more than this about the reasons for the discrepancy" — the constraint is deliberate and Karen knows the reader may notice it. The two-option structure ("documents from different periods" or "a change in your income") is careful construction — she is offering the innocent interpretations explicitly and leaving the third unspoken. This is reasoning texture produced by genuine professional and legal caution. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The specific cognitive event is Karen's awareness that she is handling an ambiguous situation that could be innocent or fraudulent. This awareness produces: the two explicit innocent interpretations (what a template would not produce), the explicit epistemic limit ("I wouldn't want to make assumptions"), and the deliberate absence of the third interpretation (what a less careful letter would include, or a careless letter would accidentally imply). Every element of the letter's careful construction is the trace of a specific mind managing a specific ambiguity. |
| Idealisation risks | Risk of making Karen too explicit about the third interpretation — tipping the letter from careful to accusatory. Counteracted by keeping the two innocent interpretations in the foreground and the third absent. Risk of making the careful language too neat — producing a letter that reads as professionally perfect. Counteracted by "I wouldn't want to make assumptions about your situation" — a slightly informal phrase that reflects genuine discomfort with the situation. |
| Imperfection checklist | PASS. Hedged claim present (intent deliberately unasserted). Assumed knowledge MEDIUM. Precision asymmetry HIGH (discrepancy handling vs decline statement). Blind spots MEDIUM. Reasoning texture HIGH — deliberate omission of third interpretation, two-option structure, explicit epistemic limit. |
| Validation gate | PASS |

---

## CB-FIN-019

**Context / subtype:** FIN — lending notice — refinancing approval, long-term existing customer
**Sender role:** Branch manager — personal approval letter to twelve-year customer
**Word count:** 196
**Ground truth:** GENUINE

### Sender profile

Robert, branch manager, Meridian Bank Parramatta. Mr and Mrs Chen have banked with Meridian for twelve years. Robert knows them — not personally, but he knows their file and their history. There was a period in 2021 when they had genuine difficulty and the branch handled it well. The refinancing application was clean and straightforward. Robert approved it himself and is writing personally, as he does for long-term customers. He does not know why they are refinancing — the application does not say and he did not ask.

### Example text

---

Dear Mr and Mrs Chen,

Thank you for your application to refinance your home loan, and for your continued banking with us.

I am pleased to let you know that your application has been approved. Your refinanced loan of $445,000 will be established at a fixed rate of 5.89% per annum for a term of three years, reverting to the current variable rate at the conclusion of the fixed period. Your monthly repayment during the fixed period will be $2,634.00.

I've reviewed your application personally and I want to say that it has been a straightforward and well-prepared application — which, given how long we've been banking together, is exactly what I'd expect.

The loan documents will be prepared by our settlements team and sent to you within five business days. If there's anything you'd like to discuss about the terms or the process, please don't hesitate to reach out to me directly.

It has been a genuine pleasure banking with you over the years, and I hope we continue to be of service.

Yours sincerely,
Robert Fitzgerald
Branch Manager
Meridian Bank Parramatta

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | Confident throughout. The approval is stated directly. The loan terms are specific and unhedged. "I've reviewed your application personally" — Robert takes personal ownership of the decision. "A straightforward and well-prepared application — which, given how long we've been banking together, is exactly what I'd expect" — a confident assessment of the customer's financial management, stated as personal observation. |
| Epistemic humility | L | Robert has the full picture — the application was clean, his assessment is complete, the terms are set. He does not know why the Chens are refinancing but he does not ask or acknowledge that gap — because in the context of a straightforward approval, the reason is not his concern. No genuine information requests in the letter. |
| Investment asymmetry | M | The personal acknowledgment of the relationship ("how long we've been banking together", "a genuine pleasure banking with you over the years") receives attention relative to its functional importance — it doesn't change the approval terms, but Robert includes it because he values the relationship. The approval terms are stated clearly and the process next steps are brief. |
| Blind spots | H | Assumes the Chens know what "reverting to the current variable rate" means at the end of the fixed period, what the variable rate currently is, and what that reversion will mean for their repayments. Does not explain the fixed-to-variable reversion. Assumes familiarity with the settlement process — "prepared by our settlements team and sent to you within five business days" without explanation. Twelve-year customers are assumed to know the bank's processes. |
| Reasoning texture | M | The personal observation ("a straightforward and well-prepared application — which, given how long we've been banking together, is exactly what I'd expect") is Robert's own language, not template. The slight awkwardness of that sentence — the dash, the parenthetical qualifier — is the trace of a manager writing personally rather than from a template. The closing ("a genuine pleasure banking with you over the years") is warmer than a standard approval letter and positioned last, where it carries the most relational weight. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The human trace is in the personal observation paragraph. "Which, given how long we've been banking together, is exactly what I'd expect" — this sentence could only be written by someone who knows the relationship history. A template would not reference the banking relationship in the context of application quality. Robert's knowledge of the Chens' twelve-year history — and his awareness that 2021 was difficult but handled well — produces this sentence. He is affirming that the difficult period did not define the relationship. That subtext is the trace. |
| Idealisation risks | Risk of making Robert too warm — an idealised version would be more effusive. Counteracted by keeping the approval terms in standard template language and reserving the personal register for two specific moments: the personal observation paragraph and the closing sentence. Risk of referencing the 2021 difficulty explicitly. Counteracted — Robert does not mention it. The affirmation ("exactly what I'd expect") is his way of acknowledging the history without naming it. |
| Imperfection checklist | PASS. No hedge on approval (justified: clean application, confident decision). Assumed knowledge HIGH (variable rate reversion, settlement process, twelve-year familiarity with bank processes). Precision asymmetry MEDIUM (relational acknowledgment vs process steps). Reasoning texture MEDIUM — personal observation paragraph and closing as seam anchors. |
| Validation gate | PASS |

---

## CB-FIN-020

**Context / subtype:** FIN — lending notice — loan approval despite prior default on credit file
**Sender role:** Credit officer — approval with careful handling of prior default reference
**Word count:** 208
**Ground truth:** GENUINE

### Sender profile

Lisa, credit officer. Ms Walton's application was approved, but her credit file shows a prior default from 2022 — a telco debt that was eventually paid. The default is still on the file and will be for another two years. Lisa approved the loan — the default was minor, paid, and the overall application was strong. But she needs to reference it in the approval letter because the assessment was made with awareness of it, and if she does not reference it Ms Walton may be surprised to encounter it later in the process. Lisa does not know whether Ms Walton knows the default is still visible on her file. She is trying to raise it without making Ms Walton feel surveilled or penalised for something she has already resolved.

### Example text

---

Dear Ms Walton,

We are pleased to confirm that your application for a personal loan of $28,000 has been approved.

Your loan will be established at a fixed interest rate of 9.45% per annum, with monthly repayments of $583.00 over a 60-month term.

In completing the assessment of your application, we noted the presence of a previously recorded default on your credit file relating to a telecommunications account. This default has been recorded as paid. Our assessment considered this matter and we were satisfied that, given the nature of the default and your overall credit profile, it did not prevent approval of your application.

We mention this only so you are aware that the item remains on your credit file for the period required under applicable credit reporting legislation. If you have any questions about your credit file or how to access it, the Office of the Australian Information Commissioner provides guidance at oaic.gov.au.

The loan agreement and direct debit authority are enclosed. Please return the signed documents by 15 April 2026 to proceed.

Yours sincerely,
Lisa Park
Credit Officer
Meridian Bank Personal Lending

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | M | Confident on the approval and the terms. Carefully worded on the default: "we were satisfied that, given the nature of the default and your overall credit profile, it did not prevent approval" — "satisfied" is a judgment word, and the conditional framing ("given the nature") acknowledges that a different default might have produced a different result. Medium intensity reflects the asymmetry: certain on approval, carefully calibrated on the default assessment. |
| Epistemic humility | M | "We mention this only so you are aware that the item remains on your credit file" — Lisa does not know whether Ms Walton is already aware. The OAIC reference reflects genuine uncertainty about whether Ms Walton knows her rights regarding credit file access. Medium intensity — she is not gathering information, but she is acknowledging a gap in what she knows about the customer's awareness. |
| Investment asymmetry | H | The default paragraph receives three sentences — more than the approval terms (two sentences) and significantly more than the process close (two sentences). Lisa's stake is in the default reference: she needs it to be present in the letter, needs it to be accurate, and needs it not to feel punitive. That careful balance drives the disproportionate attention to that paragraph. |
| Blind spots | M | Assumes Ms Walton knows what a credit reporting default is, how long defaults remain on files generally, and what the OAIC does. Does not explain the credit reporting framework. Medium intensity — Lisa is more alert to potential knowledge gaps than average, which is why she includes the OAIC reference, but she still assumes some baseline awareness. |
| Reasoning texture | H | The default paragraph is the texture anchor. "We mention this only so you are aware" — the "only" is doing careful work: it is positioning the reference as informational rather than accusatory. "The item remains on your credit file for the period required under applicable credit reporting legislation" — Lisa's language is precise about the regulatory basis for the default's continued presence, removing any implication that the bank is keeping it there. The care in this paragraph — the specific calibration of "only", the regulatory framing — is the trace of a person who has thought carefully about how this will be received. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The specific cognitive event is Lisa's awareness of the dual risk: raise the default badly and Ms Walton feels accused of something she has already resolved; fail to raise it and Ms Walton is surprised later in the process. This awareness produces the entire construction of the default paragraph — the "only so you are aware" framing, the "recorded as paid" inclusion, the "satisfied" judgment word, and the OAIC reference. Each element is the trace of a specific professional managing a specific communication risk. A template approval would not include any of this. |
| Idealisation risks | Risk of making the default paragraph too apologetic — an idealised version would soften it further. Counteracted by keeping "we noted the presence of a previously recorded default" direct and factual before the careful framing begins. Risk of making the careful language too obvious — rendering Lisa's intent transparent. Counteracted by the OAIC reference, which reads as straightforwardly informational even though it is also a soft acknowledgment that Ms Walton may not know her rights. |
| Imperfection checklist | PASS. Hedged claim present ("satisfied that...it did not prevent approval" — judgment, not certainty). Assumed knowledge MEDIUM. Precision asymmetry HIGH (default paragraph vs approval terms). Blind spots MEDIUM. Reasoning texture HIGH — "only" as precision load-bearing word, regulatory framing of default persistence, dual-risk management visible in paragraph construction. |
| Validation gate | PASS |

---

*Owlume Pty Ltd — Confidential — corpus_batch2_fin_011_020_v1 · 30 March 2026 · Batch review pending*