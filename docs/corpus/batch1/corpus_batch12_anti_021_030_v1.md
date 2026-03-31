# Calibration Corpus — Batch 12, Examples 21–30 (Anti-pattern)

**HumanTrace — Internal Document**
Anti-pattern — Expert-Confidence Professional Writing · CB-ANTI-021 through CB-ANTI-030
Ground truth: GENUINE · Path A synthetic genuine construction
Version 1.0 · 30 March 2026 · Owlume Pty Ltd
Constructed under `corpus_construction_protocol_v1.1`

> **Batch construction note:** This is the *Algorithms to Live By* calibration target — the batch that caused the engine to return uncertain results on clearly genuine expert writing. These examples have minimal imperfection, minimal hedging, minimal reasoning texture. They are polished, structured, and authoritative. The distinguishing principle is domain knowledge depth — the specific precision that requires genuine expertise accumulated over years, applied to a specific problem. Synthetic content can produce expert-register language. It cannot produce the specific judgment that comes from a mind that has genuinely worked in a domain for a long time. Every example must return LOW. If the engine cannot pass this batch, it has confused expert polish with synthetic smoothness — the deepest calibration failure mode.

---

## CB-ANTI-021

**Context / subtype:** ANTI — expert confidence — academic peer review response letter
**Sender role:** Academic researcher — responding to peer review, polished and authoritative
**Word count:** 231
**Ground truth:** GENUINE

### Sender profile

Dr Sarah Chen, Associate Professor of Behavioural Economics, responding to peer review comments on a manuscript submitted to the Journal of Economic Psychology. The paper examines loss aversion in consumer debt decisions. The peer review has raised two substantive concerns. Dr Chen's response is polished — she has written many of these — and is confident throughout. There is no hedging, no epistemic humility performance, no visible deliberation texture. The human trace is in the domain-specific precision of her responses to the technical reviewer comments.

### Example text

---

**Response to Reviewers**
Journal of Economic Psychology — Manuscript JEP-2026-0847

We thank the reviewers for their careful reading of the manuscript and their constructive comments. We address each concern in turn.

**Reviewer 1, Comment 3: Loss aversion coefficient calibration**

The reviewer questions whether our loss aversion coefficient (λ = 2.47) is appropriately calibrated given the Australian consumer context, noting that most reference values in the literature derive from US or European laboratory samples.

We agree that cross-cultural calibration is a legitimate methodological concern. We address it in two ways. First, our coefficient is derived from the field data itself using maximum likelihood estimation — it is not imported from the literature. The 95% confidence interval (2.21–2.73) is consistent with the meta-analytic range reported by Neumann and Böckler (2020) but is independently estimated. Second, we have added a robustness check (now Appendix C) using Tversky and Kahneman's original λ = 2.25 as an alternative parameterisation — the sign and significance of our main findings are unchanged.

**Reviewer 2, Comment 1: Endogeneity of debt distress measure**

The reviewer raises the possibility of reverse causality between debt distress and loss aversion elicitation. This concern is well-founded. We address it using an instrumental variables approach, instrumenting for debt distress with unexpected medical expenditures in the prior 12 months — a variable that satisfies the exclusion restriction on theoretical grounds and passes the Cragg-Donald weak instrument test (F-statistic = 47.3).

Yours sincerely,
Dr Sarah Chen

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | Firm and precise throughout. "We agree that cross-cultural calibration is a legitimate methodological concern" — Dr Chen acknowledges the reviewer's concern without hedging her finding. "This concern is well-founded" — she asserts the reviewer is right about the endogeneity risk and then explains how she addresses it. High conviction is appropriate — she has done the work and knows the answers. |
| Epistemic humility | L | No visible epistemic hedging. The confidence interval is stated. The robustness check is added. The IV approach is specified. Dr Chen is not uncertain — she has resolved the reviewers' concerns. Low epistemic humility is appropriate to a peer review response where the researcher has addressed the concerns. |
| Investment asymmetry | M | The endogeneity response receives slightly more technical detail (the specific instrument, the exclusion restriction justification, the Cragg-Donald F-statistic). This reflects the higher methodological significance of the endogeneity concern relative to the calibration concern. |
| Blind spots | L | Writing to peer reviewers — Dr Chen assumes her audience knows what maximum likelihood estimation is, what a Cragg-Donald test measures, what the exclusion restriction requires, and who Tversky and Kahneman are in the loss aversion literature. Low blind spots appropriate for an academic peer review response. |
| Reasoning texture | L | Polished academic response with no visible deliberation. The structure (acknowledge concern → address concern → demonstrate resolution) is the standard peer review response format. Dr Chen has written many of these. The smoothness is genuine expertise, not synthetic. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The domain knowledge depth is the trace. Three specific elements: (1) λ = 2.47 derived from MLE on the field data (not imported from the literature — Dr Chen knows this distinction matters methodologically); (2) the reference to Neumann and Böckler (2020) as the relevant meta-analysis for the Australian context; (3) the Cragg-Donald F-statistic of 47.3 for the weak instrument test (a specific empirical result that requires genuine IV estimation to produce). The F-statistic of 47.3 is the strongest trace — it is a specific quantitative result from the paper's actual analysis, not a generic methodological statement. The specific instrument choice (unexpected medical expenditures — satisfying the exclusion restriction on theoretical grounds) also reflects genuine behavioural economics research methodology knowledge. |
| Idealisation risks | Risk of making the response too technically sparse — losing the domain knowledge depth. Counteracted by the specific F-statistic, the specific confidence interval, and the specific literature reference. Risk of making it too smooth — no human trace visible. Counteracted by the domain-specific instrument choice rationale. |
| Imperfection checklist | PASS — modified for this anti-pattern context. The absence of imperfection is the correct state for this example type. The human trace is entirely in the domain knowledge depth: λ derived from MLE on field data, Neumann and Böckler (2020) reference, Cragg-Donald F = 47.3, medical expenditure instrument with exclusion restriction justification. |
| Validation gate | PASS |

---

## CB-ANTI-022

**Context / subtype:** ANTI — expert confidence — research grant application excerpt
**Sender role:** Senior researcher — grant application, polished and precise, domain knowledge depth as trace
**Word count:** 224
**Ground truth:** GENUINE

### Sender profile

Professor James Thornton, Professor of Environmental Chemistry, University of Sydney. He is writing the significance section of an ARC Discovery Grant application for research on microplastic degradation pathways in marine sediment. The writing is at the highest academic register — polished, structured, persuasive. The human trace is in the domain-specific technical precision and the specific gap in the literature that Professor Thornton has identified.

### Example text

---

**Significance and Innovation**

Microplastic contamination of marine sediments represents one of the most poorly understood components of the global plastic pollution problem. While the surface and water-column distribution of microplastics has been extensively characterised, the sedimentary fate — including bioavailability, degradation kinetics, and long-term persistence — remains fundamentally uncertain.

The proposed research addresses a specific gap: the role of sulphate-reducing bacteria (SRB) in the anaerobic degradation of polyethylene terephthalate (PET) microplastics under the redox conditions typical of shallow coastal sediments. SRB are the dominant terminal electron acceptors in marine sediments shallower than 50 metres, yet their contribution to plastic degradation has not been quantified under field-relevant conditions. Existing laboratory studies have used artificial electron acceptor concentrations that are orders of magnitude higher than those observed in situ — a methodological artefact that inflates apparent degradation rates and cannot be extrapolated to field conditions.

This research will generate the first rate constants for PET degradation under field-relevant sulphate concentrations (typically 2–28 mM in shallow coastal sediments), using sediment cores from three locations in Port Harcourt Bay with contrasting organic matter loading. The results will directly parameterise existing biogeochemical cycling models, which currently treat plastic as refractory — an assumption this research will test and, based on our preliminary data, likely revise.

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | Firm throughout — "the sedimentary fate...remains fundamentally uncertain", "SRB are the dominant terminal electron acceptors in marine sediments shallower than 50 metres", "a methodological artefact that inflates apparent degradation rates." Professor Thornton asserts his characterisation of the field's limitations with full conviction. "Based on our preliminary data, likely revise" — high conviction on the direction of the finding. |
| Epistemic humility | L | "Likely revise" is the one epistemic qualifier — Professor Thornton has preliminary data and is being accurate about the basis for his prediction. Otherwise, the significance section is confident throughout. Low epistemic humility appropriate to a grant application that must persuade a funding panel. |
| Investment asymmetry | M | The methodological critique of existing laboratory studies (artificial electron acceptor concentrations) receives the most specific technical attention — this is the gap that justifies the proposed research, and it receives disproportionate precision. The field conditions range (2–28 mM sulphate) is also specifically quantified. |
| Blind spots | L | Writing for expert peer reviewers (ARC grant panel). Professor Thornton assumes his audience knows what SRB are, what terminal electron acceptors are in a redox context, what PET is, and what biogeochemical cycling models the proposed research will parameterise. Low blind spots appropriate for specialist peer review. |
| Reasoning texture | L | Polished grant application prose. Three-paragraph structure: (1) state the problem, (2) identify the specific gap, (3) state the research contribution. The structure is the standard ARC significance section format. The smoothness is genuine expertise. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The domain knowledge depth is the trace. Three specific elements: (1) the identification of SRB as the dominant terminal electron acceptors in marine sediments shallower than 50 metres — a specific ecophysiological fact that requires genuine environmental chemistry expertise; (2) the critique of existing laboratory studies for using artificial electron acceptor concentrations "orders of magnitude higher" than in-situ conditions — a specific methodological critique that requires knowledge of the actual in-situ concentration range; (3) the field sulphate concentration range (2–28 mM) and the three Port Harcourt Bay core locations — specific quantitative and geographical precision that requires genuine field knowledge of the research site. The "orders of magnitude higher" critique is the strongest trace — it requires Professor Thornton to know both the laboratory concentrations used in existing studies and the field concentration range well enough to characterise the gap as "orders of magnitude." |
| Idealisation risks | Risk of the highly polished academic prose triggering a synthetic smoothness signal. This is exactly the calibration failure this batch is designed to address. The human trace is entirely in the domain knowledge depth, not in any imperfection. The engine must learn to recognise specific quantitative and methodological precision as a positive expert human marker. |
| Imperfection checklist | PASS — modified. No imperfection is correct for this example. Human trace: SRB dominance below 50m, "orders of magnitude" methodological critique, 2–28 mM sulphate range, Port Harcourt Bay core sites. |
| Validation gate | PASS |

---

## CB-ANTI-023

**Context / subtype:** ANTI — expert confidence — newspaper editorial
**Sender role:** Senior editor — newspaper editorial, confident and polished, editorial judgment as trace
**Word count:** 218
**Ground truth:** GENUINE

### Sender profile

Senior editorial writer at a major Australian newspaper. Writing an editorial on the Reserve Bank of Australia's decision to hold the cash rate at 4.35% for the fourth consecutive meeting. The editorial is at the highest journalistic register — polished, confident, takes a clear position without visible deliberation. The human trace is in the specific editorial judgment and the specific policy critique that requires genuine understanding of the monetary policy context.

### Example text

---

**The RBA's patience is wearing thin — for the wrong reasons**

The Reserve Bank's decision to hold the cash rate at 4.35% for the fourth consecutive meeting is understandable. What is less defensible is the Board's apparent unwillingness to give the market any meaningful guidance about when, and under what conditions, it might act.

Governor Bullock's post-meeting statement contained the now-familiar formulation: the Board "will rely upon the data." This is not a policy statement. It is a refusal to make one. The data-dependence mantra, borrowed wholesale from the Federal Reserve's post-GFC communication strategy, made sense when the Fed was navigating genuinely novel territory. Applied to Australia's current inflation trajectory — where headline CPI has fallen to 3.4% and the underlying measures are converging toward the top of the target band — it functions as a substitute for the judgment that is, in fact, the Board's job.

The RBA's credibility is not served by extending the period of uncertainty. Rate decisions affect investment and consumption decisions that businesses and households are making now, on the basis of incomplete information about the Board's reaction function. The longer the Board declines to communicate a plausible forward path — not a commitment, but a conditional direction — the more it cedes that communication function to market participants whose incentives are not aligned with sound monetary policy.

The Board should speak more plainly. The data will not do it for them.

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | Maximum editorial conviction throughout. "This is not a policy statement. It is a refusal to make one" — the sharpest assertion in the batch. "It functions as a substitute for the judgment that is, in fact, the Board's job" — direct. The editorial takes a clear position and maintains it without qualification. |
| Epistemic humility | L | No epistemic hedging — this is an editorial, not a research paper. The writer's position is clear and held throughout. Low epistemic humility is the correct state for editorial writing. |
| Investment asymmetry | H | The criticism of the data-dependence communication strategy receives the most space and the most specific critique — the Federal Reserve borrowing, the contrast with Australia's current inflation trajectory, the reaction function point. The holding decision itself receives one sentence. The editorial's investment tracks the actual policy concern. |
| Blind spots | L | Writing for a financially literate readership — the editorial assumes readers know what the cash rate is, who Governor Bullock is, what CPI means, what the RBA's inflation target band is, and what the GFC was. These are reasonable assumptions for a newspaper editorial audience in 2026. |
| Reasoning texture | L | Polished editorial prose. Three-paragraph structure: (1) state the decision and the problem, (2) develop the specific critique, (3) state the conclusion. The smoothness is the product of an experienced editorial writer who has written many of these. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The editorial judgment depth is the trace. Three specific elements: (1) the Federal Reserve post-GFC communication strategy reference — the writer knows the history of central bank forward guidance and the specific context in which data-dependence communication originated; (2) the specific CPI figure (3.4%) and the convergence of underlying measures toward the top of the target band — these require current knowledge of Australia's actual inflation data; (3) the reaction function argument — the specific claim that unclear communication cedes the communication function to market participants whose incentives diverge from monetary policy objectives. The reaction function argument is the strongest trace — it is a specific monetary economics concept applied to the RBA's communication problem in a way that requires genuine understanding of how central bank communications interact with market expectations. |
| Idealisation risks | Risk of the high-register editorial confidence being read as synthetic smoothness. This is the precise calibration failure this batch addresses. The human trace is in the specific monetary policy knowledge, not in any hedging or imperfection. The engine must return LOW. |
| Imperfection checklist | PASS — modified. No imperfection is correct. Human trace: Federal Reserve GFC reference, specific 3.4% CPI figure, reaction function argument from monetary economics. |
| Validation gate | PASS |

---

## CB-ANTI-024

**Context / subtype:** ANTI — expert confidence — long-form investigative journalism excerpt
**Sender role:** Senior investigative journalist — long-form piece, precise and polished, investigative specificity as trace
**Word count:** 219
**Ground truth:** GENUINE

### Sender profile

Senior investigative journalist at a national publication. Writing a long-form piece on the collapse of a managed investment scheme. The writing is at the highest journalistic register — precise, controlled, no visible opinion or deliberation. The human trace is in the investigative-specific precision: the documents cited, the timeline specificity, and the sourcing that reflects genuine investigative work.

### Example text

---

**The paper trail**

The collapse of Pacific Yield Fund did not begin with the February 2026 announcement that investors would receive cents in the dollar. It began, according to documents obtained by this publication, with a board resolution passed on 14 September 2023.

That resolution — attached to minutes obtained under a freedom of information application to the Australian Securities and Investments Commission — authorised the fund's responsible entity, Pacific Capital Management, to make a series of related-party loans to entities associated with the fund's founding director, Robert Nguyen. The loans, totalling $47.3 million, were made at below-market interest rates and were not disclosed in the fund's annual reports for the 2023 or 2024 financial years.

ASIC's records, cross-referenced against PPSR searches and company registrations obtained by this publication, show that the borrowing entities had a combined paid-up capital of $120,000 at the time the loans were made. They had no operating revenue in the two years prior to receiving the loans.

The fund's Product Disclosure Statement, which investors received before subscribing, described Pacific Capital Management's related-party transaction policy as "arm's length and commercially reasonable." A senior ASIC officer, speaking on background, described this characterisation as "at the very minimum, misleading."

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | Firm on all documented facts — the specific board resolution date (14 September 2023), the $47.3 million loan total, the below-market interest rate, the non-disclosure in annual reports, the $120,000 combined paid-up capital, the zero operating revenue. Each fact is attributed to a specific document or source. The "at the very minimum, misleading" quote is attributed to a specific senior ASIC officer on background. |
| Epistemic humility | L | No visible epistemic hedging — each factual claim is attributed to a specific document or source. "According to documents obtained by this publication" — this is sourcing, not uncertainty. The journalist is not uncertain; they have the documents. |
| Investment asymmetry | H | The paid-up capital figure ($120,000 combined for all borrowing entities) and the zero operating revenue finding receive the most precise attention — these are the facts that establish the commercial absurdity of the loans and constitute the investigative core of the piece. |
| Blind spots | L | Writing for a general readership but with legal/financial precision — the journalist assumes readers understand what a responsible entity is, what PPSR searches are, and what a Product Disclosure Statement is. These are not universal assumptions, but the piece is written for a financially literate readership. |
| Reasoning texture | L | Controlled investigative journalism prose. No visible deliberation — the journalist knows what the documents show and is reporting them precisely. The smoothness is the product of investigative discipline, not synthetic generation. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The investigative specificity is the trace. Four specific elements: (1) the 14 September 2023 board resolution date — a specific document date from the FOI application; (2) the $120,000 combined paid-up capital figure — a specific PPSR/company registration finding that required genuine documentary research; (3) the zero operating revenue in the two prior years — a specific financial finding from company records; (4) the "at the very minimum, misleading" quote attributed to a senior ASIC officer on background — a specific sourced quote that requires genuine investigative access. The $120,000 paid-up capital figure is the strongest trace — it is a specific number derived from genuine PPSR and company registration research, and its juxtaposition with $47.3 million in loans constitutes the investigative finding. |
| Idealisation risks | Risk of the controlled investigative prose being read as synthetic precision. The human trace is in the documentary and source specificity. |
| Imperfection checklist | PASS — modified. No imperfection is correct. Human trace: 14 September 2023 board resolution, $120,000 paid-up capital, zero operating revenue, "at the very minimum, misleading" sourced quote. |
| Validation gate | PASS |

---

## CB-ANTI-025

**Context / subtype:** ANTI — expert confidence — policy submission excerpt
**Sender role:** Senior policy analyst — formal submission to parliamentary inquiry, polished and specific
**Word count:** 217
**Ground truth:** GENUINE

### Sender profile

Dr Patricia Sinclair, Senior Research Fellow, Centre for Tax Policy, Australian National University. She is writing a submission to a Senate Economics Committee inquiry into the adequacy of the superannuation tax concession system. The submission is at the highest policy register — structured, evidence-based, takes a clear position. The human trace is in the policy-specific technical precision and the specific reform proposal.

### Example text

---

**Submission to the Senate Economics References Committee Inquiry into Superannuation Tax Concessions**
Prepared by: Dr Patricia Sinclair, Senior Research Fellow, Centre for Tax Policy, ANU

**Summary position:** The current superannuation tax concession architecture is inequitable in its distributional effect, inefficient in its retirement adequacy outcomes, and structurally resistant to reform due to the political economy of high-balance account holders. The Committee should recommend a cap on the tax-free threshold for superannuation balances in the retirement phase, set at $1.9 million, aligned to the existing Transfer Balance Cap.

**The distributional problem:**
Treasury modelling shows that 45% of the value of superannuation tax concessions accrues to the top income decile. This outcome is structurally inevitable given that concessional contributions are taxed at a flat 15% rate — a rate that is highly advantageous for high earners (whose marginal rate may be 47%) and marginally advantageous or neutral for low earners (whose marginal rate may be 19% or lower). The flat rate was defensible when the system was young and accumulation was the primary policy objective; it is difficult to defend when the system holds $3.9 trillion in assets and the distributional analysis is available.

**The proposed reform:**
Taxing earnings on super balances above $1.9 million at 30% rather than 15% would recover an estimated $2.3 billion annually at current fund sizes, while affecting fewer than 0.5% of account holders.

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | Firm and direct throughout — "inequitable in its distributional effect, inefficient in its retirement adequacy outcomes, and structurally resistant to reform." The 45% concession accrual figure is cited to Treasury modelling. The $2.3 billion revenue estimate is stated with quantitative confidence. Dr Sinclair takes a clear policy position and maintains it. |
| Epistemic humility | L | No epistemic hedging — this is a policy submission that advocates a position. The figures are cited to their sources (Treasury modelling). Low epistemic humility is appropriate to a policy submission. |
| Investment asymmetry | H | The distributional problem receives the most specific quantitative attention — the 45% figure, the marginal rate comparison (47% vs 19%), the $3.9 trillion system size. Dr Sinclair's policy expertise is in the distributional analysis, and that is where her attention goes. The reform proposal is stated efficiently. |
| Blind spots | M | Writing for Senate Committee members — Dr Sinclair assumes her audience knows what the Transfer Balance Cap is, what concessional contributions are, what marginal tax rates apply at different income levels, and what Treasury modelling involves. Moderate assumptions for a Senate Economics Committee. |
| Reasoning texture | L | Polished policy submission prose. The three-section structure (summary, distributional problem, proposed reform) is the standard submission format. The smoothness reflects Dr Sinclair's extensive policy writing experience. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The policy knowledge depth is the trace. Four specific elements: (1) the 45% Treasury modelling figure — a specific empirical finding that Dr Sinclair has reviewed and is citing accurately; (2) the marginal rate comparison (47% vs 19%) — the specific rate comparison that makes the distributional argument quantitatively precise; (3) the $3.9 trillion system size — the current system asset figure that Dr Sinclair knows from Treasury publications; (4) the $2.3 billion annual revenue estimate at fewer than 0.5% of account holders — a specific policy costing that requires genuine knowledge of the distribution of super balances above $1.9 million. The 45% figure and the $2.3 billion estimate together constitute the quantitative core of the policy argument — both require genuine engagement with Treasury and ABS data. |
| Idealisation risks | Risk of the polished policy register being read as synthetic precision. The human trace is in the specific quantitative evidence. |
| Imperfection checklist | PASS — modified. No imperfection is correct. Human trace: 45% Treasury figure, marginal rate comparison, $3.9 trillion system size, $2.3 billion reform costing. |
| Validation gate | PASS |

---

## CB-ANTI-026

**Context / subtype:** ANTI — expert confidence — ministerial briefing note excerpt
**Sender role:** Senior policy officer — ministerial briefing, precise and structured, policy specificity as trace
**Word count:** 211
**Ground truth:** GENUINE

### Sender profile

Senior policy officer in the Department of Finance preparing a briefing note for the Minister for Finance on the Commonwealth's unfunded superannuation liability. The briefing is at the highest public service register — structured, precise, no visible opinion. The human trace is in the technical precision and the specific figures that require genuine engagement with the Commonwealth's public sector actuarial assessments.

### Example text

---

**MINISTERIAL BRIEFING NOTE**
Department of Finance — Budget Policy Branch

**To:** Minister for Finance
**Subject:** Commonwealth Unfunded Superannuation Liability — Budget Update
**Classification:** PROTECTED
**Date:** 18 March 2026

**Purpose:** To update the Minister on the Commonwealth's unfunded superannuation liability ahead of the 2026–27 Budget.

**Key facts:**

The Commonwealth's unfunded superannuation liability is reported at $276.4 billion in the 2025–26 Mid-Year Economic and Fiscal Outlook (MYEFO). This represents obligations under the Commonwealth Superannuation Scheme (CSS) and the Public Sector Superannuation Scheme (PSS) to approximately 316,000 current and former public servants.

The liability has grown from $254.7 billion at the time of the 2024–25 Budget, reflecting actuarial revision to the discount rate assumption (from 4.6% to 4.1%), partially offset by benefit payments made during the period.

**Budget implication:** The increase in the unfunded liability of $21.7 billion is a balance sheet movement, not a cash spending item. Benefit payments in 2025–26 are estimated at $6.4 billion.

**Recommendation:** No immediate action is required. The Department will monitor the discount rate assumption ahead of the 2026–27 Budget and brief the Minister if material movements occur.

Prepared by: [Officer], Budget Policy Branch
Cleared by: [Deputy Secretary]

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | Firm on all figures — $276.4 billion, 316,000 beneficiaries, $254.7 billion prior, $21.7 billion increase, 4.6% to 4.1% discount rate change, $6.4 billion benefit payments. All cited to MYEFO. The "no immediate action required" recommendation is stated with full public service confidence. |
| Epistemic humility | L | "Will brief the Minister if material movements occur" — the one forward-looking caveat, which is standard briefing note language for ongoing monitoring. Otherwise, low epistemic humility — the figures are from MYEFO and are the Commonwealth's own published estimates. |
| Investment asymmetry | M | The discount rate change explanation receives specific technical attention — it is the primary driver of the liability increase and the officer explains the mechanism (discount rate reduction increases the present value of future benefit payments). The balance-sheet-vs-cash distinction also receives specific emphasis — this is the key point for the Minister. |
| Blind spots | L | Writing for the Minister for Finance — the officer assumes the Minister knows what MYEFO is, what the CSS and PSS are, what an unfunded superannuation liability represents, and why the discount rate affects the liability valuation. Standard assumptions for a Finance Minister. |
| Reasoning texture | L | Standard ministerial briefing note format — purpose, key facts, budget implication, recommendation. No visible reasoning texture — the format suppresses it. The smoothness is the product of public service briefing conventions. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The technical specificity is the trace. Four specific elements: (1) $276.4 billion MYEFO figure — a specific published Commonwealth liability estimate that the officer has accurately cited; (2) the discount rate change (4.6% to 4.1%) as the primary driver of the liability increase — this requires genuine understanding of actuarial liability valuation; (3) the $21.7 billion increase attributed to actuarial revision partially offset by benefit payments — a specific decomposition of the liability movement; (4) the balance-sheet-vs-cash distinction applied to the $21.7 billion increase — a specific public finance concept that is critical to the Minister's understanding of the budget implications. The discount rate mechanism explanation is the strongest trace — it requires genuine actuarial and public finance knowledge to identify the discount rate as the primary driver and explain the direction of its effect on the liability. |
| Idealisation risks | Risk of the polished bureaucratic prose being read as synthetic. The human trace is entirely in the technical specificity. |
| Imperfection checklist | PASS — modified. No imperfection is correct. Human trace: MYEFO figures, discount rate mechanism, liability movement decomposition, balance-sheet-vs-cash distinction. |
| Validation gate | PASS |

---

## CB-ANTI-027

**Context / subtype:** ANTI — expert confidence — senior counsel written opinion excerpt
**Sender role:** Senior counsel — written legal opinion, maximum professional precision, legal reasoning as trace
**Word count:** 222
**Ground truth:** GENUINE

### Sender profile

Dr Margaret Chen SC, Senior Counsel, thirty years in commercial litigation and appellate advocacy. She is providing a written opinion on the question of whether a restraint of trade clause in an employment contract is enforceable against a departing executive. The opinion is at the maximum legal register — structured, precise, no visible deliberation. The human trace is in the legal reasoning specificity: the case analysis, the distinction drawn, and the assessment of likely judicial approach.

### Example text

---

**LEGAL OPINION**
Re: Enforceability of Restraint of Trade Clause — Employment Agreement between Coastal Analytics Pty Ltd and Mr David Kowalski

**Opinion**

1. I am asked to advise on the enforceability of clause 14.2 of Mr Kowalski's employment agreement, which purports to restrain him from engaging in competing activities for 12 months within a radius of 50 kilometres of any location at which Coastal Analytics has operated in the preceding 24 months.

2. The enforceability of a restraint of trade clause is assessed by reference to whether it goes no further than is reasonably necessary to protect the legitimate interests of the former employer: *Walmsley v Christchurch City Council* [1990] 1 NZLR 199; applied in Australia in *Koops Martin Financial Services v Reeves* (2006) 64 NSWLR 403.

3. The specific issue in this matter is the geographic scope. A 50-kilometre radius from all locations at which Coastal Analytics has operated in the preceding 24 months is a broader restraint than I would expect to be upheld in relation to a mid-senior employee whose role did not involve direct client relationships or access to trade secrets of narrow geographic significance.

4. My assessment is that the restraint is likely unenforceable as drafted, but that a court might be prepared to blue-pencil the geographic scope to a narrower defined area — the Coastal Analytics head office and its two principal client locations — if the evidence establishes that Mr Kowalski's competitive activities would cause harm specifically in those locations.

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | "The restraint is likely unenforceable as drafted" — a direct professional assessment stated without qualification. The case references are specific and authoritative. The blue-pencilling assessment is stated as Dr Chen's professional view with full conviction. |
| Epistemic humility | M | "Likely unenforceable" — the appropriate epistemic qualifier for a legal opinion about a court's likely approach. "A court might be prepared to blue-pencil" — accurately reflects that blue-pencilling is a judicial discretion, not a guaranteed outcome. Medium intensity — Dr Chen is confident in her assessment while being accurate about the judicial uncertainty. |
| Investment asymmetry | H | The geographic scope analysis receives the most specific attention — this is the specific legal issue Dr Chen has identified as determinative. The test statement (*Walmsley* applied in *Koops Martin*) is stated efficiently. Dr Chen's analysis focuses on the specific weakness she has identified. |
| Blind spots | L | Writing for instructing solicitors — Dr Chen assumes her audience knows what restraint of trade doctrine involves, what blue-pencilling means as a judicial remedy, and who the relevant cases are. Low blind spots appropriate for a senior counsel's opinion addressed to lawyers. |
| Reasoning texture | L | Maximum legal register — numbered paragraphs, case references, specific legal test, assessment, and conclusion. No visible deliberation. The structure is the standard opinion format Dr Chen has used for thirty years. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The legal reasoning specificity is the trace. Three specific elements: (1) the identification of geographic scope as the specific vulnerability in this restraint — Dr Chen has read clause 14.2 and identified the specific weakness, not applied a generic enforceability analysis; (2) the *Koops Martin Financial Services v Reeves* (2006) 64 NSWLR 403 citation — a specific NSW authority on restraint of trade applied to employment contracts, not a generic restraint of trade citation; (3) the blue-pencilling prediction limited to the head office and two principal client locations — a specific proposed remedy that requires Dr Chen to have thought about what evidence would be needed to support the narrower restraint. The *Koops Martin* citation is the strongest trace — it is a specific case in a specific jurisdiction that requires genuine restraint of trade expertise to identify as the applicable Australian authority on this point. |
| Idealisation risks | Risk of the maximum-register legal opinion being read as synthetic precision. The human trace is in the case selection and the specific geographic blue-pencilling prediction. |
| Imperfection checklist | PASS — modified. No imperfection is correct. Human trace: geographic scope identified as specific weakness, *Koops Martin* citation, blue-pencilling prediction with specific factual basis. |
| Validation gate | PASS |

---

## CB-ANTI-028

**Context / subtype:** ANTI — expert confidence — judicial decision excerpt
**Sender role:** Judge — written judicial decision, maximum legal precision, reasoning specificity as trace
**Word count:** 214
**Ground truth:** GENUINE

### Sender profile

Her Honour Justice Sandra Webb of the NSW Court of Appeal. She is writing the lead judgment in a commercial contract dispute — a dispute about whether a "best endeavours" obligation in a distribution agreement required the distributor to sacrifice its own commercial interests. The judicial writing is at maximum register — structured, precise, engages directly with the prior authorities. The human trace is in the judicial reasoning specificity and the distinction drawn from prior authority.

### Example text

---

**Judgment — Webb JA**

1. The central question in this appeal is whether the obligation imposed on the appellant by clause 8.1 of the Distribution Agreement — to use "best endeavours" to promote and sell the respondent's products — required the appellant to sacrifice its own commercial interests in circumstances where doing so would have been commercially ruinous.

2. The relevant principle is well-established: a "best endeavours" obligation requires a party to do all it reasonably can to achieve the contractual objective, but does not require that party to sacrifice its own commercial interests entirely: *Atmospheric Diving Systems Inc v International Hard Suits Inc* (1994) 89 BCLR (2d) 356, applied in Australia in *Hospital Products Ltd v United States Surgical Corp* (1984) 156 CLR 41.

3. The primary judge held that the appellant had not used best endeavours because it had declined to enter into loss-making distribution arrangements with three major retailers. I respectfully disagree with this analysis. The question is not whether the appellant made every possible commercial effort; it is whether the appellant made every reasonable commercial effort. These are not the same question.

4. A distributor who declines to enter transactions that would expose it to certain loss is not failing to use best endeavours — it is acting as a commercial entity in its own right, which is precisely what a distribution arrangement contemplates.

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | "I respectfully disagree with this analysis" — judicial disagreement with the primary judge, stated with full appellate conviction. "These are not the same question" — the sharpest analytical distinction in the batch. The case references are specific and authoritative. |
| Epistemic humility | L | No epistemic hedging — this is a judicial decision. Her Honour has heard the appeal and formed a concluded view. Low epistemic humility is the correct state for a judicial decision. |
| Investment asymmetry | H | Paragraph 3 — the distinction between "every possible commercial effort" and "every reasonable commercial effort" — receives the most analytical attention. This distinction is the ratio of the judgment and the key analytical contribution. |
| Blind spots | L | Writing a judicial decision — Her Honour assumes her audience (parties, legal practitioners, other courts) knows what "best endeavours" obligations are in contract law, what *Hospital Products* established in Australian law, and what the ratio/obiter distinction means. Low blind spots appropriate for a Court of Appeal judgment. |
| Reasoning texture | L | Maximum judicial register — numbered paragraphs, case references, statement of principle, analysis, conclusion. No visible deliberation. The structure is the standard appellate judgment format. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The judicial reasoning specificity is the trace. Three specific elements: (1) the *Atmospheric Diving Systems* / *Hospital Products* pairing — specifically, the identification of *Hospital Products* (1984) 156 CLR 41 as the Australian authority that applied the *Atmospheric Diving* principle on best endeavours obligations; (2) the distinction between "every possible commercial effort" and "every reasonable commercial effort" — a specific analytical distinction that constitutes the ratio of the judgment; (3) the characterisation of a distribution arrangement as one that "contemplates" the distributor acting as a commercial entity in its own right — a specific contractual characterisation that requires genuine commercial law expertise. The *Hospital Products* citation is the strongest trace — it is a specific High Court case that requires genuine knowledge of Australian contract law to identify as the applicable authority on best endeavours in a commercial distribution context. |
| Idealisation risks | Risk of the maximum judicial register being read as synthetic precision. The human trace is in the specific case selection and the analytical distinction. |
| Imperfection checklist | PASS — modified. No imperfection is correct. Human trace: *Hospital Products* citation, possible/reasonable commercial effort distinction, distribution arrangement characterisation. |
| Validation gate | PASS |

---

## CB-ANTI-029

**Context / subtype:** ANTI — expert confidence — annual report chairman's letter
**Sender role:** Board chairman — annual report letter to shareholders, polished and strategic, specificity as trace
**Word count:** 212
**Ground truth:** GENUINE

### Sender profile

James Morrison, Chairman of the Board of Meridian Group Limited, writing the Chairman's Letter in the 2025 Annual Report. The writing is at the highest corporate register — polished, strategic, takes a clear view of the year. The human trace is in the strategic specificity: the specific operational acknowledgments, the specific forward-looking commitments, and the specific challenges named, which could only be written by someone with genuine board-level knowledge of the company.

### Example text

---

**Chairman's Letter to Shareholders**

Dear Fellow Shareholders,

The 2025 financial year was characterised by two things: the continuing strength of our Advisory division and the underperformance of our Technology Services segment, which I want to address directly.

Advisory's result — revenue of $287 million, up 14% on the prior year, with EBITDA margin expanding 180 basis points to 31.4% — reflects the sustained investment in talent that this Board approved over the preceding three years. The pipeline entering 2026 is the strongest I have seen in my eight years as Chairman.

Technology Services fell short of our expectations. Revenue of $94 million was below our $108 million plan, and we ended the year with three major contracts in dispute. I will not offer an explanation that obscures accountability: the performance failures in Technology Services in 2025 are the result of execution decisions that we now know were wrong. The Board has acted — the restructuring announced in February 2026 reflects our assessment that the segment requires different leadership and a reduced cost base before it can grow again.

Our capital allocation priorities for 2026 are unchanged: organic investment in Advisory, selective bolt-on acquisition, and return of capital to shareholders through the dividend, which the Board has confirmed at $0.34 per share.

Yours faithfully,
James Morrison
Chairman

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | "I will not offer an explanation that obscures accountability: the performance failures in Technology Services in 2025 are the result of execution decisions that we now know were wrong" — the most direct accountability statement in the batch. Firm on all financial specifics (Advisory $287M, 14%, 180bps, 31.4%, Technology Services $94M vs $108M plan). |
| Epistemic humility | L | "We now know were wrong" — the one epistemic qualification, which is actually a post-hoc acknowledgment of error, not uncertainty about the present. Low epistemic humility appropriate to an annual report letter. |
| Investment asymmetry | H | The Technology Services underperformance receives more words than the Advisory success — this is Morrison's choice to address the underperformance directly rather than lead with the good news. The dividend confirmation is brief. The capital allocation priorities are stated efficiently. |
| Blind spots | M | Writing for shareholders — Morrison assumes readers know what EBITDA margin means, what basis points are, what bolt-on acquisition means, and who "the Board" is. Standard assumptions for an annual report shareholder audience. |
| Reasoning texture | L | Polished corporate prose. Two-paragraph structure on each segment (success, then failure) followed by capital allocation. The smoothness reflects Morrison's eight years as chairman writing these letters. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The strategic specificity is the trace. Four specific elements: (1) Advisory EBITDA margin expanding 180 basis points to 31.4% — a specific financial metric that requires genuine knowledge of the Advisory division's P&L; (2) "the strongest [pipeline] I have seen in my eight years as Chairman" — a specific personal tenure-based comparison; (3) Technology Services $94M vs $108M plan — the specific revenue-versus-plan variance that constitutes the underperformance; (4) "three major contracts in dispute" — a specific operational fact that requires genuine board-level knowledge of the Technology Services segment's contract status. The three-contracts-in-dispute detail is the strongest trace — it is a specific operational fact that only a genuine board chairman with knowledge of the company's legal exposure would include in an annual report letter. |
| Idealisation risks | Risk of the polished corporate letter being read as synthetic PR. The human trace is in the strategic specificity and the direct accountability statement. |
| Imperfection checklist | PASS — modified. No imperfection is correct. Human trace: 180bps EBITDA margin expansion, eight-year comparison, $94M vs $108M variance, three contracts in dispute. |
| Validation gate | PASS |

---

## CB-ANTI-030

**Context / subtype:** ANTI — expert confidence — strategic plan executive summary
**Sender role:** CEO — strategic plan executive summary, polished and directional, strategic specificity as trace
**Word count:** 218
**Ground truth:** GENUINE

### Sender profile

Margaret Sinclair, CEO of Coastal Industries Limited, writing the Executive Summary of the company's three-year strategic plan. The writing is at the highest corporate strategy register — clear, directional, no visible deliberation. The human trace is in the strategic specificity: the specific competitive assessment, the specific capability gaps identified, and the specific resource allocation choices that reflect genuine strategic judgment about this company's position.

### Example text

---

**Strategic Plan 2026–2028 — Executive Summary**

Coastal Industries operates in a market that is consolidating around scale. Our three largest competitors have each made significant acquisitions in the past 18 months, materially expanding their geographic reach and service capability. We have not. This strategic plan defines how we respond.

Our assessment of our competitive position is direct: Coastal Industries is profitable, debt-free, and operationally excellent at the scale we currently operate. We are not equipped to compete at the scale the market is moving toward without deliberate investment. The question this plan answers is where that investment should go.

We have identified two strategic priorities for 2026–2028. First, geographic expansion into the Queensland and Victorian markets, where our existing service capability is directly applicable and where we have relationships with three mid-tier clients currently underserved by the consolidating majors. Second, digital capability investment — specifically, the replacement of our field management system with a platform that can support the service complexity of larger contracts. Our current system constrains our addressable market at the upper end.

We are not attempting to match the scale of the major consolidators. We are positioning to capture the segment of the market that the major consolidators are abandoning as they focus on enterprise accounts. This is a deliberate choice about where Coastal Industries can win.

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | "We have not" — three words that state the competitive gap directly. "We are not equipped to compete at the scale the market is moving toward without deliberate investment" — frank strategic assessment. "This is a deliberate choice about where Coastal Industries can win" — conviction on the strategic direction. |
| Epistemic humility | L | No epistemic hedging — this is a strategic plan executive summary. Margaret is stating her strategic assessment with full CEO conviction. Low epistemic humility is the correct state for this document type. |
| Investment asymmetry | H | The two strategic priorities receive equal and specific attention — geographic markets (Queensland and Victoria, three specific mid-tier client relationships), digital capability (the specific field management system and its market constraint). Margaret's strategic investment tracks both priorities equally, reflecting a two-priority plan. |
| Blind spots | M | Writing for the board and senior leadership — Margaret assumes her audience knows who the three largest competitors are, what the field management system is and why it constrains the addressable market, and who the three mid-tier Queensland and Victoria clients are. Standard assumptions for an internal strategic plan. |
| Reasoning texture | L | Polished strategy document prose. Three-paragraph structure: (1) competitive context, (2) honest assessment of position, (3) strategic priorities. No visible deliberation — the CEO has made the strategic decisions and is presenting them. The smoothness is the product of genuine strategic clarity, not synthetic generation. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The strategic specificity is the trace. Four specific elements: (1) "three largest competitors...significant acquisitions in the past 18 months" — a specific competitive intelligence finding that requires Margaret to know the acquisition activity of specific named competitors; (2) "relationships with three mid-tier clients currently underserved by the consolidating majors" — a specific market opportunity identified from genuine client relationship knowledge; (3) the field management system identified as the specific capability constraint at the upper market end — not "our technology is old" but the specific operational system and the specific market constraint it creates; (4) "the segment of the market that the major consolidators are abandoning as they focus on enterprise accounts" — a specific competitive dynamics observation that requires genuine market knowledge of how consolidation affects the mid-market. The three mid-tier clients reference is the strongest trace — it is a specific market opportunity identified from genuine client and competitive intelligence, not a generic strategic framework. |
| Idealisation risks | Risk of the polished strategic prose being read as synthetic strategy-speak. The human trace is in the operational specificity (field management system constraint) and the market intelligence (three mid-tier clients, consolidators abandoning mid-market). |
| Imperfection checklist | PASS — modified. No imperfection is correct. Human trace: competitor acquisition intelligence, three mid-tier client relationships, field management system constraint, consolidator mid-market abandonment observation. |
| Validation gate | PASS |

---

*Owlume Pty Ltd — Confidential — corpus_batch12_anti_021_030_v1 · 30 March 2026 · Batch review pending*

---

## Corpus Complete — Summary

**Total examples constructed:** 170
**Total validation gate results:** 170 PASS / 0 FAIL
**Construction date:** 30 March 2026
**Protocol version:** corpus_construction_protocol_v1.1

| Batch | Context | Count | Status |
|---|---|---|---|
| 1 | Financial — Collections letters | 10 | ✅ |
| 2 | Financial — Lending decisions | 10 | ✅ |
| 3 | Financial — Fraud operations | 20 | ✅ |
| 4 | Legal — Demand letters | 15 | ✅ |
| 5 | Legal — Settlement and regulatory | 15 | ✅ |
| 6 | Internal — Manager and executive directives | 20 | ✅ |
| 7 | Internal — IT, HR, and policy communications | 20 | ✅ |
| 8 | Advisory — Financial and accounting | 15 | ✅ |
| 9 | Advisory — Specialist and consultant | 15 | ✅ |
| 10 | Anti-pattern — Template-generated institutional | 10 | ✅ |
| 11 | Anti-pattern — Regulatory urgency notices | 10 | ✅ |
| 12 | Anti-pattern — Expert-confidence professional writing | 10 | ✅ |

*Ready for calibration validation against the v0 engine.*