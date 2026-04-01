# Calibration Corpus — Batch 8, Examples 1–15 (Advisory)

**HumanTrace — Internal Document**
Professional Advisory — Financial and Accounting · CB-ADV-001 through CB-ADV-015
Ground truth: GENUINE · Path A synthetic genuine construction
Version 1.0 · 30 March 2026 · Owlume Pty Ltd
Constructed under `corpus_construction_protocol_v1.1`

> **Batch construction note:** Expert advisory communications carry a specific epistemic profile that the engine must learn to recognise. The authority register is high — confident assertions, technical precision, specific recommendations. The domain limits are equally specific — genuine experts hedge precisely where their expertise ends and nowhere else. The disclosure language required by regulation (Corporations Act, Tax Practitioners Board) is not boilerplate; it reflects genuine epistemic limits that the regulatory framework exists to communicate. Every example in this batch must demonstrate visible domain limits alongside confident expertise. An example that is uniformly confident is not genuine expert advisory communication — it is synthetic.

---

## CB-ADV-001

**Context / subtype:** ADV — financial planning — retirement planning advice, 58-year-old client
**Sender role:** Financial adviser — retirement strategy advice, confident on structure, genuine uncertainty on outcomes
**Word count:** 231
**Ground truth:** GENUINE

### Sender profile

Sophie, financial adviser, eight years in financial planning. She is writing to Mr and Mrs Kowalski following a review of their retirement planning strategy. Mr Kowalski is 58 and plans to retire at 63. The advice is tailored to their specific circumstances — Sophie knows their asset position, their superannuation balances, their debt situation, and their income needs in retirement. She is confident in the structural strategy (transition to retirement, salary sacrifice optimisation) but genuinely uncertain on the return assumptions because market performance cannot be predicted.

### Example text

---

**STATEMENT OF ADVICE**
**Prepared for:** Mr and Mrs Kowalski
**Prepared by:** Sophie Lam, Financial Adviser — Meridian Financial Planning
**Date:** 18 March 2026
**This advice is personal advice prepared specifically for Mr and Mrs Kowalski based on the information provided to us at the time of preparation.**

Dear Mr and Mrs Kowalski,

Following our meeting on 12 March 2026, I am pleased to provide my recommendations for your retirement planning strategy.

**My recommendation:** I recommend you implement a Transition to Retirement (TTR) strategy from 1 July 2026, combined with maximising salary sacrifice contributions to superannuation for the period to Mr Kowalski's planned retirement date of June 2031.

**The basis for this recommendation:** Based on your current superannuation balance of $487,000 (combined), your current income of $185,000, and your target retirement income of $85,000 per annum (today's dollars), the TTR strategy combined with salary sacrifice optimisation gives you the strongest probability of reaching your retirement income target within your planned timeframe.

**What I cannot tell you with certainty:** The projections in this advice assume a long-term average investment return of 6.5% per annum. Actual returns will vary — in some years significantly. I am confident in the structural strategy; I cannot guarantee investment returns.

This advice is prepared in accordance with the Corporations Act 2001 and the requirements of my Australian Financial Services Licence. You should read the Financial Services Guide provided separately.

Yours sincerely,
Sophie Lam
Financial Adviser

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | Confident on the structural recommendation (TTR strategy from 1 July 2026, salary sacrifice maximisation) and the basis for it (specific figures: $487,000, $185,000, $85,000). "The strongest probability of reaching your retirement income target" — Sophie is asserting her professional assessment with appropriate confidence. High conviction on the structural recommendation — this is her domain and she knows the answer. |
| Epistemic humility | H | "What I cannot tell you with certainty" — Sophie has explicitly labelled the section of her advice that acknowledges her limits. "Actual returns will vary — in some years significantly" — genuine, not boilerplate. "I am confident in the structural strategy; I cannot guarantee investment returns" — the most precise epistemic stratification in the batch. She is simultaneously asserting high confidence on the strategy and genuine uncertainty on the outcome. |
| Investment asymmetry | H | The structural recommendation and its specific numerical basis receive the most precise attention. The limitation section receives proportionate space — it is not minimised. Sophie's liability exposure is highest at the return assumption; that section receives the most careful language. |
| Blind spots | M | Assumes Mr and Mrs Kowalski understand what a TTR strategy involves mechanically, what salary sacrifice means, and what the 6.5% return assumption is based on. The FSG reference partially addresses this. Medium intensity — the statement of advice format assumes some financial literacy in the recipient. |
| Reasoning texture | H | "What I cannot tell you with certainty" as an explicit section heading is the highest reasoning texture element in the batch. Sophie has structured the advice so that the limitation is a primary element, not a disclosure appended at the end. That structural choice — making the uncertainty as prominent as the recommendation — reflects a financial adviser who understands what responsible advice looks like, not just what compliant advice looks like. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. Two specific shared-context artefacts: the 12 March meeting (a specific prior client meeting Sophie is referencing) and the specific client figures ($487,000 combined super, $185,000 income, $85,000 retirement income target). These figures could only appear in advice tailored to this specific client — they are not generic planning figures. The "What I cannot tell you with certainty" section heading is also a trace — it reflects Sophie's deliberate structural choice to make the limitation prominent, which requires a financial adviser who has thought about what genuinely helpful advice looks like rather than what compliant advice looks like. |
| Idealisation risks | Risk of making the limitation section too prominent — suggesting Sophie lacks confidence in her recommendation. Counteracted by "I am confident in the structural strategy" before the return uncertainty disclosure — the confidence and the limit are both stated explicitly and in the right sequence. |
| Imperfection checklist | PASS. High conviction on structural strategy (expert domain). Epistemic humility HIGH (explicit limitation section, stratified uncertainty). Investment asymmetry HIGH (structural recommendation and limitation). Blind spots MEDIUM. Reasoning texture HIGH — "What I cannot tell you" as structural choice. Human trace: specific client figures and explicit limitation section as deliberate structural choice. |
| Validation gate | PASS |

---

## CB-ADV-002

**Context / subtype:** ADV — financial planning — superannuation contribution strategy, regulatory clarity with individual uncertainty
**Sender role:** Senior financial planner — superannuation contribution advice, regulatory framework clear, outcomes uncertain
**Word count:** 219
**Ground truth:** GENUINE

### Sender profile

David, senior financial planner, twelve years in financial services. He is writing to Ms Chen following her query about whether she should make additional concessional contributions to superannuation before the end of the financial year. The regulatory framework (contribution caps, tax treatment) is clear — David knows this precisely. The individual outcome depends on Ms Chen's total income for the year, which has not been finalised. David is being honest about what he can advise with certainty and what depends on information not yet available.

### Example text

---

Dear Ms Chen,

Thank you for your query about additional superannuation contributions before 30 June 2026.

I can give you clear advice on the framework, and conditional advice on whether it makes sense for you specifically.

**The framework (I am certain of this):**
The concessional contribution cap for the 2025–26 financial year is $30,000. Concessional contributions are taxed at 15% within superannuation, which for most people in your income range is advantageous compared to their marginal tax rate. If you have unused concessional cap from prior years (carry-forward provisions apply if your super balance was under $500,000 on 30 June 2025), you may be able to contribute more than $30,000 this year.

**The individual calculation (I need more information):**
Whether additional contributions make sense for you depends on your total income for 2025–26, including any bonuses or investment income that may not be finalised yet. The optimal contribution amount cannot be calculated until we have your complete income picture.

My recommendation: if your total income is likely to be similar to last year ($210,000), I recommend maximising your concessional contributions to $30,000 before 30 June. However, please confirm your expected total income so I can provide a precise recommendation.

Yours sincerely,
David Nakamura
Senior Financial Planner

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | Firm on the regulatory framework ("the concessional contribution cap for the 2025–26 financial year is $30,000" — a legislative fact). "I am certain of this" — David explicitly labels his high-conviction section. The carry-forward provisions are stated with equal certainty — these are regulatory facts he knows precisely. |
| Epistemic humility | H | "I need more information" — David explicitly labels the section where his advice is conditional. "The optimal contribution amount cannot be calculated until we have your complete income picture" — a genuine epistemic limit, not a regulatory disclosure. The "if your total income is likely to be similar to last year ($210,000)" conditional recommendation is David's honest attempt to provide a working recommendation while flagging that it depends on unconfirmed information. |
| Investment asymmetry | H | The framework section receives more structured attention than the individual calculation — David knows the framework precisely and that precision is the value he is adding. The conditional recommendation is the bridge between the certain framework and the uncertain individual calculation. |
| Blind spots | M | Assumes Ms Chen knows what concessional contributions are, what the carry-forward provision involves, and what her marginal tax rate is. David has included enough context ("taxed at 15% within superannuation, which for most people in your income range is advantageous") to partially bridge the gap. |
| Reasoning texture | H | "I can give you clear advice on the framework, and conditional advice on whether it makes sense for you specifically" — David has explicitly stratified his advice before providing it. This opening framing — which categorises his advice into certain and conditional before the reader sees either — is the highest reasoning texture element in this example. It requires a financial planner who has thought about how to communicate epistemic stratification clearly to a client, not just how to present advice in a compliant format. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. Three shared-context artefacts: the carry-forward provision check ("if your super balance was under $500,000 on 30 June 2025" — David knows Ms Chen's balance or has been told it), the last year income reference ($210,000 — a specific figure David knows from Ms Chen's prior year), and the explicit section labelling ("I am certain of this" / "I need more information"). The $210,000 figure is the strongest trace — it is Ms Chen's specific prior year income that David is using as the conditional benchmark for his recommendation. |
| Idealisation risks | Risk of making the framework section too technical — losing the client communication register. Counteracted by the plain English explanation of why the 15% tax rate is advantageous. Risk of the conditional recommendation being too vague. Counteracted by the specific $210,000 benchmark. |
| Imperfection checklist | PASS. High conviction on regulatory framework. Epistemic humility HIGH (explicit conditional section, income-dependent limitation). Investment asymmetry HIGH (framework vs individual calculation). Blind spots MEDIUM. Reasoning texture HIGH — upfront stratification framing. Human trace: $210,000 prior year figure and explicit epistemic stratification structure. |
| Validation gate | PASS |

---

## CB-ADV-003

**Context / subtype:** ADV — financial planning — risk insurance review, underinsurance identified, coverage uncertain
**Sender role:** Financial adviser — insurance review, confident on underinsurance assessment, coverage specifics pending
**Word count:** 198
**Ground truth:** GENUINE

### Sender profile

Emma, financial adviser, five years in financial planning. She has reviewed Mr Obi's insurance position — life, TPD, and income protection. Her assessment is that he is significantly underinsured, particularly on income protection. She is confident in the underinsurance finding because she has the data. The specific coverage recommendation she wants to make depends on his current employer's group insurance details, which she has requested but not yet received. She is writing to communicate the underinsurance finding and explain why she needs the additional information before finalising the recommendation.

### Example text

---

Dear Mr Obi,

Thank you for providing your financial documents. I have completed my initial review of your insurance position and wanted to share my findings with you.

**My assessment — I am confident in this finding:**
Based on your current income of $145,000, your mortgage of $520,000, and your family situation (partner and two dependent children), you are materially underinsured, particularly on income protection. Your current income protection cover of $4,200 per month would replace approximately 35% of your income — the generally recommended benchmark is 75%. The gap is significant.

**What I still need before I can make a specific recommendation:**
I have requested the details of your employer's group insurance cover, which may partially offset this gap. Until I receive those details, I cannot tell you precisely how much additional individual cover you need. I am waiting on the documentation from your employer's HR team.

In the meantime, I can tell you that some level of additional income protection cover is appropriate for your circumstances — the question is how much. I will provide a specific recommendation as soon as I have the employer group insurance details.

Yours sincerely,
Emma Wilson
Financial Adviser

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | M | High conviction on the underinsurance finding (specific figures: $145,000 income, $520,000 mortgage, $4,200 per month cover, 35% replacement rate vs 75% benchmark). "I am confident in this finding" — Emma explicitly labels her high-conviction section. Deliberately held back on the specific recommendation: "I cannot tell you precisely how much additional individual cover you need" — the epistemic limit is real. |
| Epistemic humility | H | "What I still need before I can make a specific recommendation" — Emma explicitly labels the section where her advice is held back by missing information. "Until I receive those details, I cannot tell you precisely" — this is a genuine epistemic limit, not a regulatory hedge. The employer group insurance information gap is real and Emma is being accurate about it. |
| Investment asymmetry | H | The underinsurance finding receives the most specific numerical attention — the exact coverage gap (35% vs 75% benchmark) is calculated and stated. The waiting period is given its own section. Emma's stake is in the client understanding the urgency of the underinsurance without waiting for the full recommendation — the asymmetric attention drives that message. |
| Blind spots | M | Assumes Mr Obi knows what income protection insurance is, what TPD means, what "group insurance cover" from an employer involves, and why the 75% benchmark applies. Emma has partially addressed this by calculating the replacement rate explicitly ($4,200 per month = 35% of $145,000). |
| Reasoning texture | M | "In the meantime, I can tell you that some level of additional income protection cover is appropriate for your circumstances — the question is how much" — Emma is giving the client an interim answer (some additional cover is needed) while being honest that she cannot specify the amount yet. This bridge sentence — between the current uncertain state and the eventual specific recommendation — is her professional attempt to give the client actionable certainty where she can while being honest about the remaining uncertainty. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. Three specific client artefacts: $145,000 income, $520,000 mortgage, $4,200 per month current cover. The 35% calculation (derived from $4,200 × 12 / $145,000) is Emma's calculation applied to Mr Obi's specific figures. The employer group insurance documentation request is also a trace — it reflects Emma's knowledge that group insurance cover can materially affect the individual cover recommendation, and that she has already initiated the process of obtaining those details. |
| Idealisation risks | Risk of the "I cannot tell you precisely" limitation undermining the confidence in the underinsurance finding. Counteracted by the explicit "I am confident in this finding" label and the detailed numerical calculation before the limitation section. |
| Imperfection checklist | PASS. High conviction on underinsurance finding (calculated from client data). Epistemic humility HIGH (employer cover gap explicitly named). Investment asymmetry HIGH (underinsurance finding). Blind spots MEDIUM. Reasoning texture MEDIUM — bridge sentence between certain and uncertain advice. Human trace: specific client figures and employer insurance documentation request. |
| Validation gate | PASS |

---

## CB-ADV-004

**Context / subtype:** ADV — financial planning — investment portfolio rebalancing, structural confident, timing uncertain
**Sender role:** Financial planner — portfolio rebalancing advice, structural recommendation confident, market timing genuinely uncertain
**Word count:** 209
**Ground truth:** GENUINE

### Sender profile

Marcus, financial planner, ten years in investment advice. He is writing to Mrs Anderson following a review of her investment portfolio. The portfolio has drifted significantly from its target allocation — equities are now 68% of the portfolio against a target of 60%. The structural recommendation (rebalance back to 60% equities) is clear and Marcus is confident in it. The timing question — whether to rebalance now or wait given current market conditions — is genuinely uncertain and Marcus is honest about it. He gives his view while being clear it is a view, not a prediction.

### Example text

---

Dear Mrs Anderson,

Following our recent review of your portfolio, I am writing with my rebalancing recommendation.

**What the data shows:**
Your current equity allocation is 68% of the portfolio, against your agreed target of 60%. This drift has occurred because equities have performed well over the past 18 months. The portfolio is now outside the 5% tolerance band we agreed when setting your investment strategy — rebalancing is appropriate.

**My recommendation — I am confident in this:**
I recommend rebalancing the portfolio back to your 60% equity target. This involves selling approximately $47,000 of equity holdings and redirecting to fixed income and cash. This recommendation is based on your agreed risk profile and the investment policy statement you approved in September 2024.

**On the question of timing — I am less certain:**
Some clients ask whether they should wait for markets to pull back before rebalancing. My view is that market timing is very difficult to execute reliably, and that rebalancing to your agreed allocation is more important than optimising the entry point. This is my professional view, not a prediction about where markets are heading. I cannot predict market movements.

Yours sincerely,
Marcus Webb
Financial Planner

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | M | High conviction on the structural recommendation (68% vs 60% target, 5% tolerance band, $47,000 rebalancing quantum). "I am confident in this" — explicit label. Explicitly less certain on timing: "I am less certain" — the explicit label on the lower conviction section. Medium overall reflects the deliberate stratification. |
| Epistemic humility | H | "I am less certain" as an explicit section label for the timing question. "This is my professional view, not a prediction about where markets are heading. I cannot predict market movements" — the most direct epistemic limit statement in the batch. Marcus is simultaneously giving his recommendation (rebalance now) and being honest that it is a judgment, not a certainty. |
| Investment asymmetry | H | The structural recommendation and its numerical basis receive the most precise attention. The timing section receives more words — because that is the section where Marcus's genuine uncertainty is highest and where clients are most likely to push back. His attention tracks the risk points in the advice. |
| Blind spots | M | Assumes Mrs Anderson knows what equity allocation means, what fixed income and cash are as asset classes, what the investment policy statement is and what it says, and what "tolerance band" means in the context of portfolio management. The September 2024 investment policy statement reference is both context-setting and a specific shared-history artefact. |
| Reasoning texture | H | "Some clients ask whether they should wait for markets to pull back before rebalancing" — Marcus is addressing a question Mrs Anderson has not yet asked but he knows she will ask. This anticipatory framing — addressing the client's anticipated objection before she raises it — is the trace of a financial planner who knows how clients think about rebalancing decisions and has structured his advice accordingly. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. Three shared-context artefacts: the 68% current allocation (specific to Mrs Anderson's portfolio), the September 2024 investment policy statement (a specific prior document with a specific date), and the "Some clients ask" framing (Marcus's professional experience with how clients respond to rebalancing advice, applied to Mrs Anderson's likely question). The September 2024 IPS reference is the strongest trace — it is a specific prior shared document that only a genuine financial adviser who has worked with this client would know exists. |
| Idealisation risks | Risk of making the timing section too uncertain — suggesting Marcus does not have a view. Counteracted by "My view is that market timing is very difficult to execute reliably, and that rebalancing to your agreed allocation is more important than optimising the entry point" — a clear recommendation within the uncertainty. |
| Imperfection checklist | PASS. Medium conviction overall (stratified: high on structure, explicitly lower on timing). Epistemic humility HIGH ("I am less certain" explicit label, "I cannot predict" statement). Investment asymmetry HIGH (timing section attention). Blind spots MEDIUM. Reasoning texture HIGH — anticipatory client question framing. Human trace: September 2024 IPS and anticipated client question from professional experience. |
| Validation gate | PASS |

---

## CB-ADV-005

**Context / subtype:** ADV — financial planning — early superannuation access on compassionate grounds
**Sender role:** Senior financial adviser — regulatory pathway clear, outcome uncertain because decision is APRA/ATO's
**Word count:** 204
**Ground truth:** GENUINE

### Sender profile

Jennifer, senior financial adviser, fourteen years in financial planning. She is writing to Mr Petrov, who is dealing with a serious medical situation and has asked about early access to his superannuation on compassionate grounds. Jennifer knows the compassionate grounds framework precisely — it is regulated by the ATO. She can advise on eligibility and the application process. What she cannot advise on is whether the application will be approved — that decision is the ATO's, not hers. She is being honest about this distinction.

### Example text

---

Dear Mr Petrov,

Thank you for sharing the details of your situation with me. I understand this is a very difficult time, and I want to help you access the financial support that may be available to you.

**What I can advise you on with confidence:**
Based on the information you have provided, you appear to meet the eligibility criteria for early access to superannuation on compassionate grounds under regulation 6.19A of the Superannuation Industry (Supervision) Regulations. The eligible circumstances include treatment of a life-threatening illness, which applies to your situation. The application is made directly to the ATO through myGov.

**What I cannot determine:**
The ATO makes the final determination on each compassionate grounds application. I cannot tell you whether your application will be approved — that decision is the ATO's alone. What I can tell you is that your circumstances, as you have described them, appear to meet the regulatory criteria. The ATO's approval rate for applications meeting the regulatory criteria is high, but I cannot guarantee approval.

**My recommendation:**
I recommend we proceed with preparing your application as soon as possible. I will assist you through the process. Time is a factor in your situation and I do not want to delay.

Yours sincerely,
Jennifer Huang
Senior Financial Adviser

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | M | Confident on eligibility assessment ("you appear to meet the eligibility criteria") and on the regulatory citation (Regulation 6.19A of the SIS Regulations). Explicitly limited on the outcome: "I cannot tell you whether your application will be approved — that decision is the ATO's alone." The "appears to meet" is a genuine epistemic qualifier — Jennifer has assessed the criteria but the ATO makes the final determination. |
| Epistemic humility | H | "I cannot determine" as an explicit section label. "That decision is the ATO's alone" — Jennifer is being precise about who has decision-making authority. "The ATO's approval rate for applications meeting the regulatory criteria is high, but I cannot guarantee approval" — Jennifer is giving the client the context they need (high approval rate) while being honest that she cannot guarantee it. |
| Investment asymmetry | H | The "I cannot determine" section receives the most careful language — Jennifer's professional stake is in not over-promising an outcome she cannot control. The recommendation ("proceed with preparing the application as soon as possible") is brief but includes "time is a factor in your situation and I do not want to delay" — Jennifer's personal acknowledgment of the urgency of the client's medical situation. |
| Blind spots | M | Assumes Mr Petrov knows what superannuation is and where his balance is held, what myGov is and how to access it, and what "compassionate grounds" means in the superannuation regulatory context. Jennifer has partially addressed this by naming the regulatory citation and explaining the relevant circumstance. |
| Reasoning texture | M | "I do not want to delay" — Jennifer has included this because she is aware of the client's medical situation and the financial urgency it creates. This personal acknowledgment of the urgency — which goes beyond the professional advice and into the human context — is the trace of an adviser who has absorbed the personal reality of her client's situation and is allowing it to shape her advice. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. Two specific artefacts: Regulation 6.19A of the SIS Regulations (a specific regulatory citation that requires Jennifer to know the compassionate grounds framework precisely) and "I do not want to delay" (Jennifer's personal acknowledgment of the client's medical urgency, which requires genuine awareness of the client's situation). The regulatory citation is the strongest trace — it is a specific provision within a specific piece of subordinate legislation that Jennifer has looked up and verified against Mr Petrov's circumstances. |
| Idealisation risks | Risk of making the limitation section too prominent — suggesting Jennifer cannot help. Counteracted by "What I can advise you on with confidence" as the first section, establishing Jennifer's genuine expertise before the limitation section. |
| Imperfection checklist | PASS. Medium conviction (eligibility assessment, outcome uncertain). Epistemic humility HIGH ("I cannot determine" section, ATO decision-maker clarity). Investment asymmetry HIGH (limitation section and urgency acknowledgment). Blind spots MEDIUM. Reasoning texture MEDIUM — "I do not want to delay" as personal urgency acknowledgment. Human trace: Regulation 6.19A citation and medical urgency acknowledgment. |
| Validation gate | PASS |

---

## CB-ADV-006

**Context / subtype:** ADV — tax accounting — specific deduction claim, defensible but ATO challenge risk real
**Sender role:** Tax accountant — deduction advice, confident on technical position, honest about ATO challenge risk
**Word count:** 214
**Ground truth:** GENUINE

### Sender profile

Nathan, tax accountant, seven years in tax practice. He is writing to Ms Torres about a deduction claim she wants to make for home office expenses — specifically a claim that includes a portion of her mortgage interest as a home office expense. The technical position is defensible under the tax law, but it is in an area where the ATO has issued guidance suggesting a narrower interpretation. Nathan is confident the position can be maintained but is honest that the ATO may challenge it and that the client should understand the risk.

### Example text

---

Dear Ms Torres,

Thank you for your query about home office expense deductions for the 2024–25 income year.

**My assessment of the technical position:**
The deduction you are seeking — a portion of your mortgage interest as a home office expense — is technically supportable under section 8-1 of the Income Tax Assessment Act 1997, subject to the apportionment methodology being applied correctly. The proportion of the home used exclusively for income-producing purposes, calculated on a floor area basis, is the accepted methodology.

**The ATO's position and the risk:**
The ATO has issued guidance (PCG 2023/1) suggesting that mortgage interest is generally not deductible as a home office expense unless the home office arrangement constitutes a genuine place of business. Your situation — working from home as an employee — sits in an area where the ATO's guidance and the technical legal position are not fully aligned.

My assessment is that your claim is defensible, and I am prepared to support it in your tax return. However, I want you to understand that if the ATO audits this return, they may challenge this deduction, and the outcome of any challenge would depend on the specific facts and the ATO's assessment of your working arrangements.

Yours sincerely,
Nathan Park
Tax Accountant

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | M | Confident on the technical position (Section 8-1 ITAA 1997, floor area apportionment methodology, "technically supportable"). Explicitly honest about the risk: "if the ATO audits this return, they may challenge this deduction." "I am prepared to support it in your tax return" — Nathan is staking his professional support on the position while disclosing the risk. Medium intensity reflects the genuine risk asymmetry. |
| Epistemic humility | H | "The ATO's position and the risk" as an explicit section heading — Nathan has structured the advice so the risk is a primary element, not a footnote. "The outcome of any challenge would depend on the specific facts and the ATO's assessment of your working arrangements" — Nathan is being honest that even he cannot predict the outcome of an ATO audit. The specific PCG citation (PCG 2023/1) reflects Nathan's awareness of the ATO's guidance and the tension between it and the technical legal position. |
| Investment asymmetry | H | The ATO risk section receives equal structural prominence to the technical assessment — Nathan's professional stake is in the client understanding the risk before proceeding, not just the defensibility of the claim. |
| Blind spots | M | Assumes Ms Torres knows what Section 8-1 ITAA 1997 is, what PCG 2023/1 means and where to find it, what floor area apportionment involves, and what an ATO audit process involves. Tax clients often have limited knowledge of these. The risk section is partially accessible without this knowledge. |
| Reasoning texture | M | "Your situation — working from home as an employee — sits in an area where the ATO's guidance and the technical legal position are not fully aligned" — Nathan is explaining the specific tension between the law and the ATO's administrative position. This sentence requires a tax adviser who has read both the legislation and the PCG and understands why they produce different outcomes for employee home office arrangements. That dual-source analysis, and the sentence it produced, is the trace of genuine tax expertise. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. Two specific artefacts: PCG 2023/1 (a specific ATO guidance document with a specific reference that Nathan has read and assessed against Ms Torres's circumstances) and "working from home as an employee" (the specific characterisation of Ms Torres's working arrangement that determines which ATO guidance applies). The PCG reference is the strongest trace — it requires Nathan to have reviewed the specific ATO guidance and understood why it creates tension with the technical legal position. |
| Idealisation risks | Risk of making the ATO risk section too prominent — discouraging the client from claiming a legitimate deduction. Counteracted by "my assessment is that your claim is defensible, and I am prepared to support it in your tax return" — Nathan is not withdrawing the advice; he is fully disclosing the risk. |
| Imperfection checklist | PASS. Medium conviction (technically supportable, ATO risk real). Epistemic humility HIGH (ATO risk section prominent, PCG tension explained). Investment asymmetry HIGH (risk section equal prominence). Blind spots MEDIUM. Reasoning texture MEDIUM — PCG vs legislative position tension explained. Human trace: PCG 2023/1 citation and employee characterisation. |
| Validation gate | PASS |

---

## CB-ADV-007

**Context / subtype:** ADV — tax — company restructure with tax implications, complex, multiple unknowns
**Sender role:** Senior tax adviser — restructure advice, complex and stratified, multiple unknowns acknowledged
**Word count:** 228
**Ground truth:** GENUINE

### Sender profile

Karen, senior tax adviser, fifteen years in corporate tax. She is writing to the directors of Northgate Holdings following a meeting about a proposed corporate restructure — consolidating three operating companies into a single company. The tax implications are complex: the small business CGT concessions may apply to reduce or eliminate CGT on the consolidation, but eligibility depends on multiple conditions that Karen has partially assessed. She is providing a strategic overview with specific areas where more work is needed before she can give definitive advice.

### Example text

---

Dear Mr and Mrs Fitzpatrick,

Following our meeting on 15 March 2026, I write to provide my preliminary assessment of the tax implications of the proposed consolidation of Northgate Trading, Northgate Property, and Northgate Services into a single company structure.

**Summary of my current assessment:**
The proposed consolidation can be structured to minimise the tax impact, and I believe the small business CGT concessions have a reasonable prospect of applying to reduce or eliminate CGT on the transfer of the business assets. This is a preliminary assessment only — the definitiveness of my advice is limited by the factors below.

**What I need to confirm before I can give definitive advice:**

1. **Active asset test:** I need to confirm that each company's assets satisfy the active asset test. Based on our meeting, I believe Northgate Trading and Northgate Services are likely to satisfy this test. I have a question about the Northgate Property asset profile — I will need to review the property portfolio detail.

2. **Aggregated turnover:** The small business entity threshold requires aggregated turnover below $10 million. I believe the group is below this threshold but I need to confirm the figure for the 2024–25 year.

3. **Restructure mechanics:** The order of steps in the consolidation matters for the CGT concession eligibility. I will need to model the specific sequence once the above is confirmed.

I recommend we proceed with confirming these matters before any restructure steps are taken.

Yours sincerely,
Karen Osei
Senior Tax Adviser

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | M | Confident on the strategic direction ("can be structured to minimise the tax impact", "reasonable prospect" for CGT concessions). Explicitly stratified on the specific conditions: "this is a preliminary assessment only" and the three numbered areas where more work is needed. Medium intensity reflects the genuine complexity — Karen knows the direction but not the specifics. |
| Epistemic humility | H | Three numbered items explicitly identifying what Karen needs before she can give definitive advice. "I believe" is used consistently for assessments that are provisional. "I have a question about the Northgate Property asset profile" — Karen is specifically naming where her current information is insufficient. The "definitiveness of my advice is limited by the factors below" is Karen's honest framing of what she is and is not providing. |
| Investment asymmetry | H | The three what-I-need-to-confirm items receive structured and equal attention — each is a genuine open question that Karen has identified. The strategic overview is brief. Karen's stake is in the client understanding what she does and does not know, so that no restructure steps are taken before the unknowns are resolved. |
| Blind spots | M | Assumes the directors know what the small business CGT concessions involve, what the active asset test is, what "aggregated turnover" means and why it matters, and what "restructure mechanics" refers to in the consolidation context. These are technical tax concepts that the directors may not fully understand. Karen has partially addressed this by explaining why each matter. |
| Reasoning texture | H | "The order of steps in the consolidation matters for the CGT concession eligibility" — Karen is explaining why the restructure mechanics are a separate issue, which requires a tax adviser who understands how CGT concession eligibility can be affected by the sequencing of steps. That sequencing-awareness, and the sentence it produced, is the trace of genuine corporate tax expertise applied to a specific restructure problem. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. Three specific shared-context artefacts: the 15 March meeting reference (a specific prior meeting Karen is following up on), the Northgate Property asset profile question (Karen's specific uncertainty about one of the three companies — she knows enough to identify which company raises the question but needs more detail), and the aggregated turnover threshold ($10 million — the specific small business entity threshold Karen is applying to this group). The Northgate Property question is the strongest trace — it is Karen's specific identification of where her current information is insufficient, which requires genuine knowledge of the asset profile discussions to date. |
| Idealisation risks | Risk of making the three unknowns seem like obstacles — suggesting the restructure may not work. Counteracted by "I believe the small business CGT concessions have a reasonable prospect of applying" as the strategic overview before the unknowns are listed. |
| Imperfection checklist | PASS. Medium conviction (strategic direction, preliminary assessment). Epistemic humility HIGH (three explicit unknowns, preliminary assessment labelled). Investment asymmetry HIGH (unknowns receive equal attention). Blind spots MEDIUM. Reasoning texture HIGH — sequencing-awareness in restructure mechanics. Human trace: Northgate Property specific question and $10 million threshold application. |
| Validation gate | PASS |

---

## CB-ADV-008

**Context / subtype:** ADV — tax — year-end tax planning for small business, practical and specific
**Sender role:** Accountant — year-end tax planning advice, practical, current law basis disclosed
**Word count:** 197
**Ground truth:** GENUINE

### Sender profile

Tom, accountant, six years in small business accounting. He is writing to his client Mr Patel, a small business owner, with year-end tax planning recommendations for the 2025–26 financial year. The advice is practical and specific — prepaying deductible expenses, timing of asset purchases, superannuation contributions. Tom is confident in the advice as it stands but is clear that the advice is based on current law, which could change (especially given the pre-budget season).

### Example text

---

Dear Mr Patel,

As we approach 30 June, I want to share some year-end tax planning actions that are worth considering for your business.

**Prepay deductible expenses:** Where expenses are deductible in the year they are paid (rather than when they are incurred), prepaying before 30 June can bring the deduction forward. This applies to insurance premiums, subscription renewals, and interest on business borrowings. Check that any prepaid amount relates to a period of no more than 12 months.

**Asset purchases — instant asset write-off:** The instant asset write-off threshold for small businesses is currently $20,000 for the 2025–26 year. If you are planning to purchase eligible business assets, purchasing before 30 June allows you to claim the full deduction this year rather than next.

**Superannuation contributions:** Concessional contributions made and received by the fund before 30 June are deductible in the current year. The cap is $30,000 for 2025–26.

This advice is based on current tax law as at the date of this letter. Tax law can change, and I recommend confirming the current position with me before acting, particularly given the approaching Federal Budget.

Yours sincerely,
Tom Whitmore
Accountant

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | Firm on all three planning strategies and their specific parameters ($20,000 threshold, $30,000 super cap, 12-month prepayment rule). These are current law figures that Tom knows precisely. |
| Epistemic humility | M | "This advice is based on current tax law as at the date of this letter. Tax law can change" — a genuine disclosure, not boilerplate. The "particularly given the approaching Federal Budget" is Tom's specific timing context — the advice is being given in pre-budget season and Tom is flagging that the relevant thresholds may change. Medium intensity — the current law is clear but the pre-budget context creates genuine uncertainty. |
| Investment asymmetry | M | The three strategies receive roughly equal attention — each is a separate planning action. The disclosure receives brief but specific attention. Tom's stake is in the client acting before 30 June; the practical specificity of each strategy serves that goal. |
| Blind spots | M | Assumes Mr Patel knows what "instant asset write-off" means, what counts as an "eligible business asset," what "concessional contributions made and received by the fund" means technically, and why the 12-month rule applies to prepaid expenses. Tom has provided enough context for each to be actionable without full tax knowledge. |
| Reasoning texture | M | "Particularly given the approaching Federal Budget" — Tom has added a specific timing context to his standard disclosure language. This addition requires Tom to know that the current planning season is pre-budget, that the instant asset write-off threshold has historically been adjusted in budgets, and that this specific uncertainty is material to this specific advice. The standard disclosure would not include this — Tom has added it because of his awareness of the current timing. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The "approaching Federal Budget" addition to the standard disclosure is the human trace. It requires Tom to know the current pre-budget timing and to understand which of his recommendations is most exposed to budget changes (the instant asset write-off threshold has been modified by budget measures in recent years). That timing-awareness and its application to this specific advice is the trace of an accountant who is actively tracking the legislative environment, not just applying known rules. |
| Idealisation risks | Risk of making the advice too specific — giving dollar thresholds that may have changed between the writing and publication of this example. Counteracted by the disclosure that the advice is based on current law as at the date of the letter. |
| Imperfection checklist | PASS. High conviction on current law (specific thresholds). Epistemic humility MEDIUM (current law disclosure, Federal Budget timing). Investment asymmetry MEDIUM (three equal strategies). Blind spots MEDIUM. Reasoning texture MEDIUM — Federal Budget timing addition to standard disclosure. Human trace: pre-budget timing awareness applied to specific threshold vulnerability. |
| Validation gate | PASS |

---

## CB-ADV-009

**Context / subtype:** ADV — tax — ATO audit response strategy, high stakes, adviser owns the strategy
**Sender role:** Tax partner — ATO audit response, confident in strategy, honest about ATO may disagree
**Word count:** 221
**Ground truth:** GENUINE

### Sender profile

Margaret, tax partner, twenty years in tax dispute resolution. She is writing to Coastal Industries following the receipt of an ATO audit position paper. The ATO is proposing to disallow a $1.4 million deduction for management fees paid to a related party, on the basis that the fees were not incurred for income-producing purposes. Margaret has reviewed the position paper and the underlying facts. She believes the ATO's position is wrong and she is confident in the response strategy. She is also honest that the ATO may not agree and that the matter may need to go to the AAT or Federal Court.

### Example text

---

Dear Mr and Mrs Nguyen,

I have reviewed the ATO's position paper dated 10 March 2026 and I am writing with my response strategy.

**My assessment of the ATO's position:**
The ATO's position — that the management fees of $1.4 million were not incurred for income-producing purposes — is, in my assessment, wrong. The fees were paid to Coastal Management Pty Ltd for genuine management services, the service agreement is documented, and the services were actually rendered. The ATO's argument appears to rely on the related-party nature of the arrangement rather than the absence of genuine services.

**My recommended response strategy:**
I recommend we submit a detailed response challenging the ATO's position, supported by the service agreement, board minutes approving the arrangement, and evidence of the services rendered (emails, reports, and meeting records). I am confident this response will give us the best opportunity to resolve the matter at the audit stage.

**What I cannot guarantee:**
The ATO may maintain its position after our response. If that occurs, you have the right to object and, if unsuccessful, to appeal to the Administrative Appeals Tribunal or the Federal Court. I believe we have a strong case. I cannot guarantee the ATO will agree.

Yours sincerely,
Margaret Sinclair
Tax Partner

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | "The ATO's position is, in my assessment, wrong" — Margaret's professional judgment stated with full personal conviction. "I am confident this response will give us the best opportunity to resolve the matter at the audit stage" — high conviction on the strategy. "I believe we have a strong case" — personal professional assessment. The high conviction is appropriate — Margaret has reviewed the facts and the position paper and has formed a clear view. |
| Epistemic humility | M | "What I cannot guarantee" as an explicit section heading. "The ATO may maintain its position after our response" — genuine epistemic limit. "I cannot guarantee the ATO will agree" — the most direct epistemic limit statement in the advisory batch. Medium intensity — Margaret is highly confident in the strategy and the case, while being honest that the outcome depends on the ATO's response to her strategy. |
| Investment asymmetry | H | The assessment of the ATO's position receives the most specific analytical attention — Margaret is explaining why the ATO is wrong, which requires her to engage with the specific reasoning in the position paper. The response strategy is specific about the supporting evidence. The limitation section is brief but explicit. Margaret's professional stake is in both the strategy and the client understanding the risk. |
| Blind spots | M | Assumes the Nguyens know what the AAT is and what an appeal process involves, what "objection" means in the ATO review process, and what "income-producing purposes" means as a legal test under Section 8-1. Margaret has partially addressed the last by explaining the ATO's position in lay terms. |
| Reasoning texture | H | "The ATO's argument appears to rely on the related-party nature of the arrangement rather than the absence of genuine services" — Margaret is engaging with the specific logical structure of the ATO's position and identifying its weakness. This analytical move — identifying what the ATO is actually arguing versus what it would need to prove — is the trace of a tax dispute lawyer who has reviewed the position paper and identified the argumentative gap. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The "appears to rely on the related-party nature" analysis is the human trace — it is Margaret's specific engagement with the ATO's argumentative strategy, which requires her to have read the position paper and identified the gap between what the ATO is asserting (fees not for income-producing purposes) and what she believes it is actually relying on (related-party inference). That analytical move could only be made by someone who has read the specific position paper and has the tax dispute resolution experience to identify the argumentative strategy. |
| Idealisation risks | Risk of making the "what I cannot guarantee" section too prominent — undermining confidence in what Margaret believes is a strong case. Counteracted by "I believe we have a strong case" immediately before "I cannot guarantee the ATO will agree" — the confidence and the limit are stated in the same breath. |
| Imperfection checklist | PASS. High conviction on strategy (twenty-year experience, specific case assessment). Epistemic humility MEDIUM (ATO response uncertain). Investment asymmetry HIGH (ATO position analysis). Blind spots MEDIUM. Reasoning texture HIGH — argumentative gap identification from position paper analysis. Human trace: "appears to rely on" analysis from specific position paper reading. |
| Validation gate | PASS |

---

## CB-ADV-010

**Context / subtype:** ADV — tax — R&D tax incentive claim, technical eligibility uncertain
**Sender role:** Accountant — R&D tax incentive advice, technical eligibility assessed but ATO agreement not guaranteed
**Word count:** 208
**Ground truth:** GENUINE

### Sender profile

Claire, accountant, eight years with a focus on R&D tax incentive claims. She is writing to the directors of TechStream about their eligibility for the R&D tax incentive for the 2024–25 financial year. She has reviewed their activities and believes they are eligible — but R&D eligibility is a technical question that the ATO assesses independently, and her assessment is not the ATO's assessment. She is being honest about this distinction while giving her professional view.

### Example text

---

Dear Mr and Mrs Okafor,

Following our review of TechStream's development activities for the 2024–25 financial year, I am writing with my assessment of your eligibility for the Research and Development Tax Incentive.

**My assessment:**
Based on my review of the technical documentation provided, I believe TechStream's core development activities meet the definition of eligible R&D activities under section 355-25 of the Income Tax Assessment Act 1997. Specifically, the activities involve systematic, investigative, and experimental work in a new field with the purpose of generating new knowledge — this is the core eligibility criterion.

**The technical review process I applied:**
I reviewed the activity descriptions against the four-part eligibility test: (1) the activities constitute a core R&D activity under the legislation; (2) the activities are conducted for the purpose of generating new knowledge; (3) the outcome of the activities was not known or determinable in advance; and (4) there is a genuine hypothesis being tested. In my assessment, TechStream's activities satisfy all four parts of this test.

**What I cannot determine:**
The ATO conducts its own independent review of R&D claims. My assessment of eligibility is my professional opinion — it is not the ATO's determination. The ATO may form a different view. I believe the claim is supportable, but I cannot guarantee the ATO will agree.

Yours sincerely,
Claire Whitfield
Accountant

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | M | Confident on the technical assessment (four-part eligibility test, all four parts satisfied, specific legislative citation). "I believe TechStream's activities satisfy all four parts of this test" — professional conviction on the technical analysis. Explicitly limited on the outcome: "the ATO may form a different view." Medium intensity reflects the genuine professional/ATO distinction. |
| Epistemic humility | H | "What I cannot determine" as an explicit section heading. "My assessment of eligibility is my professional opinion — it is not the ATO's determination" — Claire is being precise about the distinction between her role (assess eligibility) and the ATO's role (determine eligibility). "I cannot guarantee the ATO will agree" — the same direct epistemic limit statement as CB-ADV-009. |
| Investment asymmetry | H | The four-part eligibility test receives the most structured attention — this is Claire's technical analysis and it is the value she is adding. The limitation section is brief but explicit. Claire's stake is in both the eligibility assessment and the client understanding that the ATO's determination is independent. |
| Blind spots | M | Assumes the directors know what the R&D tax incentive is and how it works, what section 355-25 covers, and what "systematic, investigative, and experimental work" means as a legal criterion. Claire has provided enough explanation of the test that the directors can follow the reasoning even without full technical knowledge. |
| Reasoning texture | M | The four-part test structure is Claire's analytical framework applied to TechStream's specific activities. The "(3) the outcome of the activities was not known or determinable in advance" criterion is the one that is most often contested in R&D claims — Claire has included it in the test and stated it is satisfied, which reflects her awareness of where R&D eligibility is most commonly disputed. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The four-part test application is the human trace — Claire has matched each of the four eligibility criteria to TechStream's specific activities, which requires her to have reviewed the technical documentation and made a judgment about whether each criterion is met. The "(3) outcome not known or determinable in advance" criterion is particularly specific — it is the criterion that requires the most judgment and that Claire has explicitly assessed as satisfied. |
| Idealisation risks | Risk of making the four-part test too mechanical — appearing to tick boxes rather than exercise judgment. Counteracted by the explanation of what "new knowledge" means as the core criterion — Claire is showing that she understands what the test is trying to assess, not just what it says. |
| Imperfection checklist | PASS. Medium conviction (technical assessment, ATO determination separate). Epistemic humility HIGH (professional/ATO distinction explicit). Investment asymmetry HIGH (four-part test attention). Blind spots MEDIUM. Reasoning texture MEDIUM — "not known or determinable in advance" criterion as dispute-awareness trace. Human trace: four-part test application from technical documentation review. |
| Validation gate | PASS |

---

## CB-ADV-011

**Context / subtype:** ADV — consulting — post-merger integration strategy, incomplete data, directional advice
**Sender role:** Management consultant — PMI strategy advice, data incomplete, directional not prescriptive
**Word count:** 213
**Ground truth:** GENUINE

### Sender profile

James, management consultant, nine years in M&A integration advisory. He is writing to the CEO of Meridian Group following completion of the acquisition of Coastal Analytics. The integration is three weeks in. James has completed a rapid diagnostic — reviewing the financials, key contracts, and leadership team — but the diagnostic is necessarily incomplete at this stage. His advice is directional: here is where to focus, here is what to watch. He is not yet in a position to give prescriptive integration plans — the data does not support it.

### Example text

---

Dear Ms Morrison,

Following completion of our rapid diagnostic of the Coastal Analytics integration, I am writing with my initial strategic recommendations.

**What the diagnostic shows:**
The integration has three priority areas based on the diagnostic: customer retention, technology platform consolidation, and leadership team alignment. Customer retention is the most urgent — Coastal Analytics' top 10 customers account for 67% of revenue, and several of these relationships are held primarily by individuals who have not yet committed to staying.

**My directional recommendations:**
I recommend prioritising retention of the key customer relationship holders over the next 90 days. Technology platform consolidation can follow — it is important but can withstand a 90-day delay. Leadership team alignment needs to happen in parallel with the retention effort but should not be the primary focus in the first 90 days.

**What I cannot yet advise on:**
The diagnostic was necessarily rapid and is based on three weeks of data. There are areas I have not yet fully assessed — specifically the state of the Coastal Analytics IP portfolio and the vendor contracts, both of which require deeper review. My directional recommendations should be treated as priorities for the next 90 days, not as a complete integration plan.

Yours sincerely,
James Thornton
Management Consultant

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | M | Confident on the three priority areas and the 90-day sequencing recommendation. "Customer retention is the most urgent" — stated with conviction, supported by the 67% revenue concentration figure. Explicitly limited on the incomplete areas: "the diagnostic was necessarily rapid and is based on three weeks of data." Medium intensity reflects the genuine data limitation. |
| Epistemic humility | H | "What I cannot yet advise on" as an explicit section heading. "There are areas I have not yet fully assessed — specifically the state of the Coastal Analytics IP portfolio and the vendor contracts" — James is naming the specific gaps in his diagnostic. "My directional recommendations should be treated as priorities for the next 90 days, not as a complete integration plan" — the most precise framing of the scope limitation in the advisory batch. |
| Investment asymmetry | H | Customer retention receives the most specific attention — the 67% revenue concentration figure and the relationship-holder retention framing. The other two priority areas are named but not detailed. James's stake is in the CEO understanding the urgency of the customer retention issue; that drives the attention asymmetry. |
| Blind spots | M | Assumes Ms Morrison knows what "leadership team alignment" means in the PMI context, what the IP portfolio review would involve, and what "vendor contracts" refers to in the Coastal Analytics context. James has provided enough directional framing that these terms are actionable without full PMI knowledge. |
| Reasoning texture | M | "Technology platform consolidation can follow — it is important but can withstand a 90-day delay" — James is explicitly sequencing the three priorities and explaining the basis for the sequencing. The "can withstand a 90-day delay" judgment is his professional assessment of the relative urgency, not a template output. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. Two specific artefacts: the 67% revenue concentration figure (derived from James's diagnostic of Coastal Analytics' customer data — a specific finding from specific data) and the IP portfolio and vendor contracts as the two named gaps (James has reviewed enough to know what he has not reviewed, which requires genuine diagnostic work to identify). The 67% figure is the strongest trace — it is a specific data point from James's review of Coastal Analytics' financials that could only appear in advice from someone who has done the actual diagnostic work. |
| Idealisation risks | Risk of making the directional recommendations too specific — losing the "necessarily rapid diagnostic" qualifier. Counteracted by the explicit scope limitation in the "what I cannot yet advise on" section. |
| Imperfection checklist | PASS. Medium conviction (directional, data-limited). Epistemic humility HIGH (three-week data limitation, specific gaps named). Investment asymmetry HIGH (customer retention priority). Blind spots MEDIUM. Reasoning texture MEDIUM — 90-day sequencing judgment. Human trace: 67% revenue concentration and specific diagnostic gaps identified. |
| Validation gate | PASS |

---

## CB-ADV-012

**Context / subtype:** ADV — consulting — operational efficiency review, data confident, implementation uncertain
**Sender role:** Senior consultant — operational efficiency findings, confident on data, careful on implementation
**Word count:** 209
**Ground truth:** GENUINE

### Sender profile

Rebecca, senior consultant, eleven years in operational consulting. She has completed a six-week operational efficiency review of Northgate Manufacturing's production lines. She has found significant inefficiency in the changeover process between production runs — the data is clear. Her recommendations for addressing it are also clear. But the implementation timeline depends on factors she cannot fully assess — specifically, the union consultation requirements and the current industrial relations climate, which she is not an expert in. She is honest about this limit.

### Example text

---

Dear Mr Kowalski,

I am pleased to present the findings and recommendations from our six-week operational efficiency review of the Northgate Manufacturing production lines.

**The findings — I am confident in these:**
The data shows that changeover time between production runs averages 4.2 hours against an industry benchmark of 2.8 hours. This 1.4-hour excess per changeover, across the 47 changeovers per month we observed, represents approximately 66 hours of lost production capacity per month. The root cause analysis identifies three contributing factors: non-standardised changeover procedures, tooling that is not co-located with the production lines, and a training gap in the changeover crew.

**The recommendations:**
I recommend implementing a SMED (Single Minute Exchange of Die) methodology, relocating the tooling store to adjacent the primary production line, and developing a standardised changeover procedure with training certification. Based on the data, I would expect these measures to reduce changeover time to approximately 2.5–3.0 hours.

**The implementation timeline — I am less certain:**
The implementation timeline depends in part on union consultation requirements, which I am not positioned to advise on. I recommend engaging your HR and ER teams early to understand the consultation process before committing to an implementation schedule.

Yours sincerely,
Rebecca Huang
Senior Consultant

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | M | High conviction on the findings (4.2 hours vs 2.8 hours benchmark, 47 changeovers per month, 66 hours lost capacity). "I am confident in these" — explicit label. "I would expect" for the projected improvement (2.5–3.0 hours) — appropriate confidence given the data supports it but individual results may vary. Explicitly less certain on implementation timeline. |
| Epistemic humility | H | "I am less certain" as an explicit label for the implementation timeline section. "Union consultation requirements, which I am not positioned to advise on" — Rebecca is being precise about where her expertise ends. This is genuine domain humility — she knows what SMED methodology involves; she does not know the industrial relations landscape. |
| Investment asymmetry | H | The data findings receive the most precise numerical attention — 4.2 hours, 2.8 hours benchmark, 47 changeovers, 66 hours. Rebecca's confidence lives in the data and the data receives maximum specificity. The implementation timeline caveat is brief but explicit. |
| Blind spots | M | Assumes Mr Kowalski knows what SMED methodology is, what "tooling co-location" involves in practice, and what "training certification" requires. Rebecca has named these specifically enough that they are actionable for a manufacturing client. |
| Reasoning texture | M | "I recommend engaging your HR and ER teams early to understand the consultation process before committing to an implementation schedule" — Rebecca is routing the implementation timeline question to the people who can answer it (HR and ER teams), rather than leaving the uncertainty unresolved. This referral reflects her awareness of what she does and does not know, and her knowledge of who in the client organisation can fill her gap. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The specific operational data (4.2 hours, 2.8 hour benchmark, 47 changeovers, 66 hours lost capacity) is the primary human trace — these figures come from Rebecca's six-week observation of the specific production lines and could not be fabricated without genuine site access. The union consultation referral is also a trace — it reflects Rebecca's professional awareness of the boundary between operational consulting and industrial relations consulting, which requires experience to know where that boundary sits. |
| Idealisation risks | Risk of making the implementation caveat too prominent — suggesting the recommendations cannot be implemented. Counteracted by "based on the data, I would expect these measures to reduce changeover time to approximately 2.5–3.0 hours" — the expected improvement is stated confidently before the caveat. |
| Imperfection checklist | PASS. Medium conviction (data confident, implementation uncertain). Epistemic humility HIGH ("I am not positioned to advise on" union consultation). Investment asymmetry HIGH (data findings). Blind spots MEDIUM. Reasoning texture MEDIUM — IR referral from domain-boundary awareness. Human trace: specific production data from six-week site observation. |
| Validation gate | PASS |

---

## CB-ADV-013

**Context / subtype:** ADV — consulting — founder funding round strategy, structural confident, market uncertain
**Sender role:** Business adviser — funding round advice, structural strategy confident, market conditions uncertain
**Word count:** 198
**Ground truth:** GENUINE

### Sender profile

Andrew, business adviser, thirteen years in venture capital and startup advisory. He is writing to the founder of a SaaS company, TechStream (appearing again in the corpus as a consistent shared-context thread), following discussions about a Series A raise. Andrew is confident in the structural advice — how to structure the round, what metrics to lead with, which investor profiles to target. He is genuinely uncertain about market conditions for Series A SaaS investment, which have shifted significantly over the past eighteen months.

### Example text

---

Dear Ms Chen,

Following our conversations about the Series A raise, I am writing with my strategic recommendations.

**The structural advice — I am confident in this:**
Based on TechStream's current metrics — ARR of $2.1M, 140% NRR, and 18-month cash runway — you are in a strong position to approach Series A investors. I recommend targeting a raise of $8–10M at a pre-money valuation of $18–22M, leading with the NRR metric and the enterprise pipeline. The investor profile I recommend: specialist SaaS investors with Australian portfolio experience, not generalist VCs.

**The market conditions — I am less certain:**
Series A valuations for SaaS companies have compressed significantly since 2022. The $18–22M valuation range I recommend is my assessment of the current market for companies with your metrics — it may prove conservative if conditions improve, or aggressive if they tighten further. I cannot predict where the market will be in three months when you are actively raising.

**My recommendation on timing:**
Given your 18-month runway, you have optionality on timing. I recommend beginning investor conversations now but not pressuring yourself to close before Q3. The market conditions in Q3 may be clearer than they are today.

Yours sincerely,
Andrew Marsden
Business Adviser

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | M | High conviction on the structural advice (ARR $2.1M, 140% NRR, 18-month runway — specific metrics; $8–10M raise, $18–22M valuation, NRR-led story, specialist SaaS investors — specific structural recommendations). Explicitly less certain on market conditions: "I cannot predict where the market will be in three months." Medium overall reflects the structural/market stratification. |
| Epistemic humility | H | "I am less certain" as an explicit label for the market section. "It may prove conservative if conditions improve, or aggressive if they tighten further" — genuine bilateral uncertainty. "I cannot predict where the market will be in three months" — direct epistemic limit statement. The Q3 timing recommendation reflects genuine strategic judgment in the face of acknowledged uncertainty. |
| Investment asymmetry | H | The structural metrics and recommendations receive the most specific numerical attention. The market conditions section receives more words — because that is where the genuine uncertainty lives and where Andrew's professional judgment is most needed. His attention tracks the risk points in the advice. |
| Blind spots | M | Assumes Ms Chen knows what NRR means and why it is a leading metric for SaaS investors, what a specialist SaaS investor vs a generalist VC involves in practice, and what "enterprise pipeline" means in the investor conversation context. Standard assumptions for a founder who has been building a SaaS company. |
| Reasoning texture | M | "The market conditions in Q3 may be clearer than they are today" — Andrew is not just saying wait; he is explaining why waiting may provide an informational advantage. This reasoning — that timing the raise to a period when market clarity increases reduces pricing risk — is Andrew's professional judgment about how to use the runway optionality. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. Three specific shared-context artefacts: the TechStream metrics (ARR $2.1M, 140% NRR, 18-month runway — specific figures from the company's financials that Andrew knows from prior conversations), the Series A compression since 2022 (market knowledge Andrew is applying to the specific valuation range), and the Q3 timing recommendation (Andrew's specific assessment of when market conditions may be clearer, based on his current read of the VC market cycle). |
| Idealisation risks | Risk of making the valuation range too precise — suggesting more certainty than the market conditions support. Counteracted by the explicit "may prove conservative...or aggressive" bilateral uncertainty framing. |
| Imperfection checklist | PASS. Medium conviction (structural confident, market uncertain). Epistemic humility HIGH ("I am less certain" label, bilateral uncertainty, "I cannot predict"). Investment asymmetry HIGH (market conditions attention). Blind spots MEDIUM. Reasoning texture MEDIUM — timing reasoning and optionality. Human trace: TechStream specific metrics and VC market cycle read. |
| Validation gate | PASS |

---

## CB-ADV-014

**Context / subtype:** ADV — consulting — supply chain risk assessment, multi-dimensional risk, conditional mitigation
**Sender role:** Management consultant — supply chain risk assessment, risk assessed across dimensions, mitigation conditional
**Word count:** 204
**Ground truth:** GENUINE

### Sender profile

Patricia, management consultant, fifteen years in supply chain and operations consulting. She has completed a supply chain risk assessment for Coastal Manufacturing. She has assessed risk across four dimensions: supplier concentration, geographic concentration, inventory resilience, and logistics dependency. The risk assessment is clear. The mitigation recommendations are conditional — they depend on Coastal Manufacturing's risk tolerance and the capital it is prepared to invest in mitigation. Patricia is honest about this dependency.

### Example text

---

Dear Mr and Mrs Fitzpatrick,

I am writing to present the findings of our supply chain risk assessment.

**The risk assessment — these findings are clear:**
Coastal Manufacturing faces elevated risk across three of the four dimensions assessed. Supplier concentration is the highest risk: 74% of raw material value is sourced from three suppliers, two of which are single-source relationships. Geographic concentration is elevated: 61% of your supply base is in South-East Asia, with significant exposure to the Shenzhen manufacturing cluster specifically. Inventory resilience is adequate: your current safety stock represents 34 days of production, which is within industry norms. Logistics dependency is moderate — manageable with standard contingency planning.

**The mitigation recommendations — these are conditional:**
The appropriate mitigation strategy depends on two things I cannot determine for you: your risk tolerance and the capital you are prepared to invest in mitigation. Dual-sourcing the two single-source relationships would eliminate your highest risk at an estimated 12–18% cost premium. If that premium is unacceptable, alternative mitigations include safety stock increases and supply chain insurance. I can model each scenario in detail once I understand your risk and capital parameters.

Yours sincerely,
Patricia Sinclair
Management Consultant

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | M | High conviction on the risk findings (74% supplier concentration, 61% geographic concentration in South-East Asia, 34-day safety stock, specific percentage figures throughout). "These findings are clear" — explicit label. Deliberately conditional on the mitigation: "these are conditional" — explicit label on the lower conviction section. |
| Epistemic humility | H | "These are conditional" as an explicit section label. "Two things I cannot determine for you: your risk tolerance and the capital you are prepared to invest in mitigation" — Patricia is explicitly naming the two pieces of information she needs from the client before she can give prescriptive mitigation recommendations. "I can model each scenario in detail once I understand your risk and capital parameters" — the conditionality is genuine, not a hedge. |
| Investment asymmetry | H | The supplier concentration finding receives the most specific attention (74%, three suppliers, two single-source) — this is the highest risk finding and Patricia's attention reflects that assessment. The logistics dependency finding is brief because it is the lowest risk. Patricia's attention tracks the risk level of each dimension. |
| Blind spots | M | Assumes the Fitzpatricks know what "single-source relationships" means in supply chain terms, what "Shenzhen manufacturing cluster" refers to and why geographic concentration there is specifically risky, and what "supply chain insurance" covers. Patricia has provided enough explanation that the risk findings are accessible. |
| Reasoning texture | M | "I can model each scenario in detail once I understand your risk and capital parameters" — Patricia is offering a path forward that depends on client input, not consultancy assumptions. This conditional offer — making the detailed modelling contingent on receiving the client's own parameters — is the trace of a consultant who knows that mitigation recommendations without risk tolerance input are not genuinely helpful, even if they appear to be. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The specific risk percentages (74%, 61%, 34 days) and the Shenzhen cluster reference are the primary human traces — they are derived from Patricia's specific assessment of Coastal Manufacturing's supply chain data and reflect genuine analytical work. The "cannot determine for you: your risk tolerance and the capital you are prepared to invest" sentence is also a trace — it is Patricia's professional acknowledgment that risk tolerance is a client value judgment, not a consulting determination. |
| Idealisation risks | Risk of making the conditional mitigation section seem like an avoidance of commitment. Counteracted by the "12–18% cost premium" estimate for dual-sourcing — Patricia has estimated the cost even while making the decision conditional. |
| Imperfection checklist | PASS. Medium conviction (risk confident, mitigation conditional). Epistemic humility HIGH (two client-determined inputs named explicitly). Investment asymmetry HIGH (supplier concentration attention). Blind spots MEDIUM. Reasoning texture MEDIUM — conditional modelling offer from risk-tolerance-as-client-judgment. Human trace: specific risk percentages from analytical assessment. |
| Validation gate | PASS |

---

## CB-ADV-015

**Context / subtype:** ADV — consulting — business sale process advice, process confident, outcome uncertain
**Sender role:** Senior business adviser — sale process advice, process strategy confident, market outcome uncertain
**Word count:** 214
**Ground truth:** GENUINE

### Sender profile

Elizabeth, senior business adviser, seventeen years in business sales and M&A. She is writing to the founder of a professional services business — Apex Consulting — following discussions about a potential sale. Elizabeth knows the sale process precisely — how to prepare, how to run a process, how to manage buyer interactions. She is confident in the process strategy. What she cannot advise on is the ultimate outcome — the sale price and terms depend on buyer appetite, which cannot be predicted with certainty. She is honest about both.

### Example text

---

Dear Mr Nakamura,

Following our discussions about a potential sale of Apex Consulting, I am writing with my recommendations for how to approach this process.

**The process — I know this well:**
I recommend a structured sale process beginning with preparation (financials, information memorandum, vendor due diligence) over three to four months, followed by a managed market approach targeting strategic and financial buyers. Based on Apex Consulting's revenue profile ($4.2M revenue, 28% EBITDA margin), I expect the business to generate strong buyer interest.

**The valuation range — my professional assessment:**
Based on comparable transactions in the professional services sector, I expect Apex Consulting to attract offers in the range of $8–14M, with the midpoint around $10–11M. This range reflects a 6–10x EBITDA multiple, which is typical for professional services businesses with your characteristics. I am confident in this range as my assessment of the market; I cannot tell you where in the range your business will ultimately transact.

**What I cannot guarantee:**
Buyer appetite can change. Market conditions can shift between process launch and transaction close. I believe Apex Consulting is well-positioned for a successful sale. I cannot guarantee the outcome.

Yours sincerely,
Elizabeth Marsden
Senior Business Adviser

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | M | High conviction on the process strategy (specific preparation steps, buyer targeting approach, three-to-four month preparation timeline) and the valuation range ($8–14M, 6–10x EBITDA, midpoint $10–11M). "I know this well" — explicit label. "I am confident in this range as my assessment of the market" — professional conviction stated with appropriate precision. Explicitly uncertain on the outcome: "I cannot tell you where in the range your business will ultimately transact." |
| Epistemic humility | H | "What I cannot guarantee" as an explicit section heading. "Buyer appetite can change. Market conditions can shift" — genuine bilateral uncertainty. "I cannot guarantee the outcome" — the same direct epistemic limit statement as several prior examples. Medium-high intensity — Elizabeth is highly confident in her assessment while being genuinely honest about market dependency. |
| Investment asymmetry | H | The valuation range receives the most specific attention — the specific figures ($4.2M revenue, 28% EBITDA, $8–14M range, 6–10x multiple) and the midpoint ($10–11M). This is what Mr Nakamura most wants to know and Elizabeth has provided her professional assessment with maximum specificity while being honest about the uncertainty around it. |
| Blind spots | M | Assumes Mr Nakamura knows what EBITDA means, what an information memorandum is, what "strategic and financial buyers" means in M&A terms, and what "vendor due diligence" involves. Elizabeth has provided enough context for the key figures to be meaningful. |
| Reasoning texture | M | "This range reflects a 6–10x EBITDA multiple, which is typical for professional services businesses with your characteristics" — Elizabeth is explaining the valuation methodology, not just stating the range. This explanation — connecting the specific range to the industry multiple and the business characteristics — is the trace of an adviser who wants Mr Nakamura to understand the basis for the range, not just accept the number. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The specific business metrics ($4.2M revenue, 28% EBITDA) and the EBITDA multiple range (6–10x) are the primary human traces — they are Elizabeth's assessment of Apex Consulting's specific metrics applied to comparable transaction data that she has from her seventeen years of professional services M&A experience. The "cannot tell you where in the range" acknowledgment is also a trace — it reflects Elizabeth's professional honesty that comparable transaction ranges are advisory, not predictive, which requires experience to know and honesty to say. |
| Idealisation risks | Risk of making the valuation range too precise — suggesting more certainty than the market conditions support. Counteracted by the wide $8–14M range and the explicit "I cannot tell you where in the range" acknowledgment. |
| Imperfection checklist | PASS. Medium conviction (process confident, outcome uncertain). Epistemic humility HIGH (market dependency, "I cannot guarantee" explicit). Investment asymmetry HIGH (valuation range attention). Blind spots MEDIUM. Reasoning texture MEDIUM — methodology explanation for valuation range. Human trace: specific business metrics and EBITDA multiple from comparable transaction experience. |
| Validation gate | PASS |

---

*Owlume Pty Ltd — Confidential — corpus_batch8_adv_001_015_v1 · 30 March 2026 · Batch review pending*