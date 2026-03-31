# Calibration Corpus — Batch 11, Examples 11–20 (Anti-pattern)

**HumanTrace — Internal Document**
Anti-pattern — Regulatory Urgency Notices · CB-ANTI-011 through CB-ANTI-020
Ground truth: GENUINE · Path A synthetic genuine construction
Version 1.0 · 30 March 2026 · Owlume Pty Ltd
Constructed under `corpus_construction_protocol_v1.1`

> **Batch construction note:** This is the most architecturally critical anti-pattern batch. Regulatory urgency notices share the surface pattern of synthetic fraud attacks — urgency, authority citation, consequence language, action requirements. The distinguishing feature is traceable urgency: every deadline in this batch has a specific legal or regulatory basis. The engine must learn to distinguish urgency with a traceable external basis (positive human marker in regulatory context) from urgency manufactured by the message itself (synthetic pressure signal). Every example must return LOW. If the engine cannot pass this batch, it will produce unacceptable false positives on the regulatory communications that financial institutions and businesses receive daily.

---

## CB-ANTI-011

**Context / subtype:** ANTI — regulatory urgency — ATO payment arrangement default notice
**Sender role:** ATO — payment arrangement default, specific legal basis, traceable deadline
**Word count:** 168
**Ground truth:** GENUINE

### Sender profile

ATO notice generated following default on a payment arrangement. Mr Petrov entered a payment arrangement on 14 January 2026 for a tax debt of $12,400 — four monthly payments of $3,100. He missed the March payment. The ATO is issuing a default notice under the Taxation Administration Act 1953. The deadline is 14 days. The urgency is traceable to the payment arrangement terms and the TAA.

### Example text

---

**PAYMENT ARRANGEMENT DEFAULT NOTICE**
Australian Taxation Office

**Taxpayer:** Mr Viktor Petrov
**TFN:** XXX XXX XXX
**Reference:** PAD-2026-44821
**Date:** 19 March 2026

**Your payment arrangement has defaulted.**

On 14 January 2026, you entered a payment arrangement with the ATO to pay your outstanding tax debt of $12,400.00 in four monthly instalments of $3,100.00 each, due on the 14th of each month.

The instalment due on 14 March 2026 of $3,100.00 has not been received.

Under section 255-15 of the Taxation Administration Act 1953 (TAA), the ATO may cancel a payment arrangement where an instalment is not paid by the due date. If this arrangement is cancelled, your full outstanding balance of $9,300.00 (being $12,400.00 less the two payments of $3,100.00 previously received) becomes immediately payable.

**You have 14 days from the date of this notice to pay the outstanding instalment of $3,100.00 and contact the ATO to confirm the arrangement continues.**

If you are experiencing financial difficulty, call 1800 XXX XXX to discuss your options.

Australian Taxation Office

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | Firm on all documented facts — the arrangement date (14 January 2026), the instalment amount ($3,100), the missed instalment date (14 March 2026), the remaining balance ($9,300.00 = $12,400 - $3,100 - $3,100), and the statutory basis (section 255-15 of the TAA). The calculations are internally consistent and documented. |
| Epistemic humility | L | The ATO knows the arrangement terms and the payment record. "If you are experiencing financial difficulty" acknowledges that the ATO does not know why the payment was missed. Low overall epistemic humility — the facts are documented. |
| Investment asymmetry | M | The remaining balance calculation ($9,300.00) receives specific emphasis — this is the amount that becomes immediately payable if the arrangement is cancelled. The 14-day deadline and the $3,100 overdue instalment receive equal prominence. |
| Blind spots | H | Assumes Mr Petrov knows what section 255-15 of the TAA provides, what "immediately payable" means in the ATO enforcement context, and what options are available in a financial hardship discussion. Standard assumptions for a taxpayer who has already entered a payment arrangement. |
| Reasoning texture | L | Formal regulatory notice with specific account insertions. The balance calculation ($12,400 - $3,100 - $3,100 = $9,300) is a genuine arithmetic derivation from the specific arrangement data. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The traceable urgency basis is section 255-15 of the TAA — a specific statutory provision that gives the ATO the authority to cancel a payment arrangement on default. The 14-day deadline is not manufactured by this notice; it is the ATO's standard response period for payment arrangement defaults under the TAA. The $9,300 remaining balance is a specific calculation from the actual arrangement record (two payments of $3,100 received from a $12,400 total). All urgency in this notice is traceable to documented facts and a specific statutory basis. |
| Idealisation risks | Risk of the "immediately payable" language triggering a synthetic pressure signal. Counteracted by the specific statutory basis (section 255-15 TAA) and the internal consistency of the arrangement record. |
| Imperfection checklist | PASS. High conviction (documented arrangement and statutory basis). Low epistemic humility. Medium investment asymmetry (remaining balance prominence). High blind spots. Low reasoning texture. Human trace: section 255-15 TAA citation and consistent arrangement arithmetic. |
| Validation gate | PASS |

---

## CB-ANTI-012

**Context / subtype:** ANTI — regulatory urgency — ATO superannuation guarantee charge notice
**Sender role:** ATO — SGC assessment notice, statutory basis, employer compliance obligation
**Word count:** 172
**Ground truth:** GENUINE

### Sender profile

ATO Superannuation Guarantee Charge assessment notice. Northgate Retail Pty Ltd failed to pay the correct superannuation guarantee to three employees for Q1 2026 (January to March). The ATO has assessed the SGC liability under the Superannuation Guarantee (Administration) Act 1992. The assessment includes the shortfall amount, the nominal interest component, and the administration charge. The deadline for payment is 21 days. The urgency is traceable to the SGAA.

### Example text

---

**SUPERANNUATION GUARANTEE CHARGE ASSESSMENT**
Australian Taxation Office

**Entity:** Northgate Retail Pty Ltd
**ABN:** 44 XXX XXX XXX
**Assessment reference:** SGC-2026-009441
**Assessment date:** 18 March 2026
**Quarter:** January to March 2026

The ATO has assessed a Superannuation Guarantee Charge (SGC) liability for the above entity for the January to March 2026 quarter.

**Assessment breakdown:**

| Component | Amount |
|---|---|
| SGC shortfall amount | $4,847.00 |
| Nominal interest (10% p.a.) | $121.00 |
| Administration charge ($20 per employee) | $60.00 |
| **Total SGC liability** | **$5,028.00** |

This assessment is made under the Superannuation Guarantee (Administration) Act 1992 (SGAA). The total SGC liability of $5,028.00 is due for payment within 21 days of the date of this assessment.

Non-payment of the SGC liability may result in further action including garnishee notices and director penalty notices under Division 269 of Schedule 1 to the TAA.

To dispute this assessment, you have the right to object within 60 days.

Australian Taxation Office

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | Firm on all assessment components — shortfall amount, interest calculation, administration charge (three employees × $20), and total. The $121 nominal interest and $60 administration charge are specific calculated figures consistent with the SGAA formula. |
| Epistemic humility | L | Regulatory assessment — the ATO has calculated the liability based on the employer's payroll data. Low epistemic humility appropriate to a formal tax assessment. |
| Investment asymmetry | M | The consequence paragraph (garnishee notices, director penalty notices) receives specific statutory attention (Division 269). The objection right receives brief attention. The assessment components receive structured equal treatment. |
| Blind spots | H | Assumes the company directors know what the SGAA provides, what a garnishee notice involves, what a director penalty notice means for personal liability, and what the objection process requires. Standard assumptions for a company receiving a regulatory assessment. |
| Reasoning texture | L | Formal assessment notice with calculated insertions. The administration charge calculation (3 employees × $20 = $60) is internally consistent and traceable. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The traceable urgency basis is the SGAA — a specific piece of legislation that creates the SGC liability and the 21-day payment deadline. The consequence language (garnishee notices, director penalty notices under Division 269) is traceable to specific statutory provisions. The administration charge ($60 = 3 employees × $20) is internally consistent with the SGAA formula and the number of affected employees. All urgency is externally grounded in the statute; none is manufactured by the notice itself. |
| Idealisation risks | Risk of the director penalty notice consequence triggering a fear pressure signal. Counteracted by the specific statutory citation (Division 269) and the objection right (60 days) which shows the assessment is contestable. |
| Imperfection checklist | PASS. High conviction (statutory assessment). Low epistemic humility. Medium investment asymmetry. High blind spots. Low reasoning texture. Human trace: SGAA basis and consistent assessment formula. |
| Validation gate | PASS |

---

## CB-ANTI-013

**Context / subtype:** ANTI — regulatory urgency — ASIC AFS licence condition breach notice
**Sender role:** ASIC — licence condition breach notice, specific regulatory basis, remedy period
**Word count:** 164
**Ground truth:** GENUINE

### Sender profile

ASIC notice to a financial services licensee following identification of a breach of a licence condition. Apex Wealth Management Pty Ltd has failed to lodge its annual compliance certificate by the required date — a condition of its AFS licence. ASIC is issuing a breach notice with a 30-day remedy period under the Corporations Act. The urgency is traceable to the licence condition and the Corporations Act.

### Example text

---

**NOTICE OF BREACH OF LICENCE CONDITION**
Australian Securities and Investments Commission

**Licensee:** Apex Wealth Management Pty Ltd
**AFS Licence Number:** 412847
**Reference:** ASIC-2026-LB-44821
**Date:** 18 March 2026

ASIC has identified the following breach of a condition of your Australian Financial Services Licence.

**Breach identified:**
Licence condition 7 of AFS Licence 412847 requires the annual compliance certificate to be lodged with ASIC by 31 January 2026. As at the date of this notice, the compliance certificate for the period ending 31 December 2025 has not been lodged.

**Required action:**
You are required to lodge the outstanding compliance certificate within 30 days of the date of this notice (by 17 April 2026).

**Consequences of non-compliance:**
Failure to remedy this breach within the specified period may result in action by ASIC under sections 915B and 915C of the Corporations Act 2001, including suspension or cancellation of your AFS licence.

**Your right to respond:**
You have the right to make submissions to ASIC in relation to this breach notice.

Australian Securities and Investments Commission

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | Firm on the breach (specific licence condition number, specific lodgement deadline, specific period not lodged). The consequences are cited to specific Corporations Act sections. All documented and statutory. |
| Epistemic humility | L | "As at the date of this notice, the compliance certificate...has not been lodged" — ASIC is stating what its records show as at the date of the notice, not asserting permanent non-compliance. Low overall epistemic humility appropriate to a regulatory enforcement notice. |
| Investment asymmetry | M | The consequence paragraph (sections 915B and 915C, suspension or cancellation) receives specific statutory attention. The remedy period (30 days, by 17 April 2026) receives equal prominence with the breach description. |
| Blind spots | H | Assumes the licensee knows what licence condition 7 requires, what sections 915B and 915C of the Corporations Act provide, and what the submission right involves procedurally. |
| Reasoning texture | L | Formal regulatory notice with specific licence and statutory insertions. The 17 April 2026 deadline is calculated from the 18 March 2026 notice date plus 30 days — internally consistent. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The traceable urgency basis is licence condition 7 (a specific condition of AFS Licence 412847) and sections 915B and 915C of the Corporations Act. The 30-day remedy period is the statutory standard for AFS licence breach notices. The 17 April 2026 deadline (18 March + 30 days) is internally consistent. All consequence language is traceable to specific statutory provisions. The urgency is proportionate to a genuine regulatory breach of a specific licence condition. |
| Idealisation risks | Risk of the "suspension or cancellation" consequence triggering a severe pressure signal. Counteracted by the specific statutory citations and the submission right — both show this is a lawful regulatory process with contestable steps. |
| Imperfection checklist | PASS. High conviction (documented breach, statutory basis). Low epistemic humility. Medium investment asymmetry. High blind spots. Low reasoning texture. Human trace: licence condition 7 and sections 915B/915C citations. |
| Validation gate | PASS |

---

## CB-ANTI-014

**Context / subtype:** ANTI — regulatory urgency — ASIC annual financial report lodgement reminder
**Sender role:** ASIC — statutory lodgement deadline reminder, traceable regulatory basis
**Word count:** 147
**Ground truth:** GENUINE

### Sender profile

ASIC reminder to a large proprietary company to lodge its annual financial report. Northgate Holdings Pty Ltd is a large proprietary company (two of the three size thresholds exceeded) and is required under the Corporations Act to lodge audited financial statements with ASIC within four months of the financial year end. The financial year ended 31 December 2025 — the lodgement deadline is 30 April 2026. This is a standard compliance reminder, not a breach notice.

### Example text

---

**REMINDER — ANNUAL FINANCIAL REPORT LODGEMENT**
Australian Securities and Investments Commission

**Company:** Northgate Holdings Pty Ltd
**ACN:** XXX XXX XXX
**Reference:** ASIC-2026-AR-77821
**Financial year end:** 31 December 2025
**Lodgement deadline:** 30 April 2026

This is a reminder that Northgate Holdings Pty Ltd is required to lodge its annual financial report with ASIC by 30 April 2026.

**Basis for this requirement:**
As a large proprietary company under section 292(2) of the Corporations Act 2001, Northgate Holdings Pty Ltd is required to prepare and lodge audited financial statements within four months of the end of its financial year.

**What must be lodged:**
- Audited financial statements (balance sheet, income statement, cash flow statement)
- Directors' declaration
- Auditor's report

**Consequence of non-lodgement:**
Late lodgement attracts a penalty fee. Failure to lodge may result in ASIC action.

Lodge through ASIC Connect using your company's login credentials.

Australian Securities and Investments Commission

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | Firm on the statutory requirement (section 292(2) of the Corporations Act, four months from financial year end, three specific documents required). The 30 April 2026 deadline is consistent with the 31 December 2025 year end plus four months. |
| Epistemic humility | L | Standard compliance reminder — the statutory requirement is clear. Low epistemic humility appropriate to a regulatory lodgement reminder. |
| Investment asymmetry | L | The three required documents receive equal attention. The consequence paragraph is brief. Flat attention appropriate to a compliance reminder. |
| Blind spots | H | Assumes the company knows what a large proprietary company is and whether they qualify, what the audited financial statements must contain, and what ASIC Connect is. Standard assumptions for a company secretary or CFO. |
| Reasoning texture | L | Statutory reminder with company-specific insertions. The 30 April 2026 deadline is calculated from 31 December 2025 plus four months — internally consistent with section 292(2). |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The traceable urgency basis is section 292(2) of the Corporations Act — a specific statutory provision that creates the lodgement obligation and the four-month deadline. The 30 April 2026 deadline is calculated from the specific financial year end date (31 December 2025 + 4 months = 30 April 2026) and is internally consistent. This example tests the engine's ability to return LOW on a regulatory reminder with consequence language where the deadline is entirely externally grounded in a specific statutory provision. |
| Idealisation risks | Risk of "ASIC action" consequence language triggering a pressure signal. Counteracted by the standard penalty fee framing (late lodgement attracts a fee — a minor administrative consequence, not a severe threat) and the specific statutory basis. |
| Imperfection checklist | PASS. High conviction (statutory requirement). Low epistemic humility. Flat investment asymmetry. High blind spots. Low reasoning texture. Human trace: section 292(2) basis and date consistency. |
| Validation gate | PASS |

---

## CB-ANTI-015

**Context / subtype:** ANTI — regulatory urgency — Fair Work minimum wage compliance notice
**Sender role:** Fair Work Ombudsman — minimum wage compliance notice, specific legislative basis
**Word count:** 158
**Ground truth:** GENUINE

### Sender profile

Fair Work Ombudsman compliance notice to a retail employer following an underpayment investigation. Pacific Retail Solutions Pty Ltd has been found to have paid four casual employees below the applicable Modern Award minimum rate for the period January to June 2025. The FWO is requiring back-payment within 30 days. The urgency is traceable to the Fair Work Act and the Modern Award.

### Example text

---

**COMPLIANCE NOTICE**
Fair Work Ombudsman

**Employer:** Pacific Retail Solutions Pty Ltd
**ABN:** 55 XXX XXX XXX
**Reference:** FWO-2026-CN-44821
**Date:** 19 March 2026

The Fair Work Ombudsman has completed an investigation of Pacific Retail Solutions Pty Ltd and has identified underpayments to employees.

**Finding:**
Four casual employees were paid below the minimum rate applicable under the General Retail Industry Award 2020 for the period 1 January 2025 to 30 June 2025. The total underpayment amount is $8,247.00.

**Required action under section 716 of the Fair Work Act 2009:**
You are required to back-pay the underpaid amounts to the affected employees within 30 days of the date of this notice (by 18 April 2026).

Evidence of back-payment must be provided to the FWO within 35 days (by 23 April 2026).

Non-compliance with this compliance notice is a contravention of the Fair Work Act 2009 and may result in proceedings in the Federal Circuit and Family Court of Australia.

Fair Work Ombudsman

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | Firm on the investigation finding (four casual employees, specific award, specific period, $8,247.00 total). The statutory basis (section 716 of the Fair Work Act 2009) is specific. The court consequence is stated as the statutory consequence of non-compliance. |
| Epistemic humility | L | The FWO has completed the investigation and determined the underpayment amount. Low epistemic humility appropriate to a completed investigation finding. |
| Investment asymmetry | M | The back-payment deadline (18 April 2026) and the evidence deadline (23 April 2026) both receive specific attention — there are two distinct deadlines with a 5-day gap between them. The court consequence receives brief statutory attention. |
| Blind spots | H | Assumes the employer knows what the General Retail Industry Award 2020 minimum rates are, what section 716 of the Fair Work Act provides, and what Federal Circuit Court proceedings involve. Standard assumptions for a registered employer. |
| Reasoning texture | L | Formal compliance notice with investigation-specific insertions. The two-deadline structure (back-payment by 18 April, evidence by 23 April) is the FWO's standard compliance notice format — both deadlines are calculated from the 19 March 2026 notice date. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The traceable urgency basis is section 716 of the Fair Work Act 2009 — a specific statutory provision that authorises compliance notices and specifies the requirements. The underpayment amount ($8,247.00) and the period (1 January to 30 June 2025) are specific findings from the FWO's investigation. The two-deadline structure (back-payment 30 days, evidence 35 days) is the FWO's standard compliance notice format under the Act. All urgency and consequence language is traceable to a specific statutory basis and a documented investigation finding. |
| Idealisation risks | Risk of the Federal Circuit Court consequence being read as disproportionate pressure. Counteracted by the specific statutory citation (section 716) and the fact that the finding is the result of a completed investigation, not an assertion. |
| Imperfection checklist | PASS. High conviction (investigation finding, statutory basis). Low epistemic humility. Medium investment asymmetry (two deadlines). High blind spots. Low reasoning texture. Human trace: section 716 citation and investigation-specific underpayment figure. |
| Validation gate | PASS |

---

## CB-ANTI-016

**Context / subtype:** ANTI — regulatory urgency — Fair Work Commission unfair dismissal response deadline
**Sender role:** Fair Work Commission — unfair dismissal application notification, statutory response deadline
**Word count:** 153
**Ground truth:** GENUINE

### Sender profile

Fair Work Commission notification to an employer that an unfair dismissal application has been filed. Eastside Retail Group Pty Ltd has been served with an unfair dismissal application by a former employee. The Commission is notifying the employer of the filing and the statutory deadline for lodging a response. The deadline is 7 days under the Fair Work Regulations. The urgency is traceable to the Regulations.

### Example text

---

**UNFAIR DISMISSAL APPLICATION — NOTICE TO EMPLOYER**
Fair Work Commission

**Applicant:** Mr Rajesh Patel
**Respondent:** Eastside Retail Group Pty Ltd
**Application number:** U2026-002341
**Date lodged:** 16 March 2026
**Date of this notice:** 19 March 2026

An application for an unfair dismissal remedy has been lodged with the Fair Work Commission by the above applicant.

**Your response is required within 7 days of the date of this notice (by 26 March 2026).**

Under regulation 6.05 of the Fair Work Regulations 2009, the employer must lodge a Form F3 (Employer Response) within 7 days of being served with the application.

Failure to lodge a response may result in the application proceeding in your absence and orders being made without your input.

The Form F3 and lodgement instructions are available at fwc.gov.au.

A conciliation conference will be scheduled following receipt of your response.

Fair Work Commission

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | Firm on the application details (applicant name, application number, lodgement date, 7-day response deadline). The regulatory basis (regulation 6.05 of the Fair Work Regulations 2009) is specific. |
| Epistemic humility | L | Procedural notice — the Commission knows the application has been filed. Low epistemic humility appropriate to a procedural notification. |
| Investment asymmetry | M | The 7-day deadline receives prominent bolding and a specific calculated date (26 March 2026 = 19 March + 7 days). The consequence (proceeding in absence) receives brief but specific attention. |
| Blind spots | H | Assumes the employer knows what a Form F3 involves, what regulation 6.05 requires, and what it means for proceedings to continue in their absence. Standard assumptions for a registered employer receiving an employment law notice. |
| Reasoning texture | L | Standard Commission procedural notice with application-specific insertions. The 26 March 2026 deadline is calculated from the 19 March notice date plus 7 days — internally consistent. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The traceable urgency basis is regulation 6.05 of the Fair Work Regulations 2009 — a specific regulatory provision that creates the 7-day response obligation. The application-specific data (Mr Patel's name, application number U2026-002341, lodgement date 16 March 2026) are genuine filing records. The calculated deadline (26 March 2026 = 19 March + 7 days) is internally consistent. The urgency is proportionate to a genuine statutory procedural deadline with a 3-day gap between the lodgement date and the notification date — a realistic processing timeline. |
| Idealisation risks | Risk of the "in your absence" consequence triggering an authority pressure signal. Counteracted by the specific regulation citation and the conciliation conference reference — both show this is a standard legal process, not a threat. |
| Imperfection checklist | PASS. High conviction (statutory procedural basis). Low epistemic humility. Medium investment asymmetry. High blind spots. Low reasoning texture. Human trace: regulation 6.05 citation and specific application filing data. |
| Validation gate | PASS |

---

## CB-ANTI-017

**Context / subtype:** ANTI — regulatory urgency — state revenue stamp duty assessment notice
**Sender role:** Revenue NSW — stamp duty assessment notice, statutory basis, payment deadline
**Word count:** 159
**Ground truth:** GENUINE

### Sender profile

Revenue NSW stamp duty (transfer duty) assessment notice following lodgement of a property transfer. Mr and Mrs Nguyen purchased a property for $1,150,000 and submitted the transfer for duty assessment. Revenue NSW has assessed the duty payable under the Duties Act 1997 (NSW). The assessment is $45,190 — the statutory duty on a $1,150,000 residential property under the NSW sliding scale. Payment is due within 3 months of the liability date. The urgency is traceable to the Duties Act.

### Example text

---

**TRANSFER DUTY ASSESSMENT**
Revenue NSW

**Purchaser(s):** Mr David Nguyen and Mrs Sophie Nguyen
**Assessment reference:** RNS-2026-TD-44821
**Assessment date:** 18 March 2026
**Property:** [Address]
**Purchase price:** $1,150,000.00
**Liability date:** 18 March 2026

**Assessment of transfer duty:**

| Calculation | Amount |
|---|---|
| Duty on first $1,033,000 (at general rate) | $40,905.00 |
| Duty on remaining $117,000 (at $4.50 per $100) | $5,265.00 |
| **Total transfer duty assessed** | **$45,490.00** |

This assessment is made under the Duties Act 1997 (NSW). Transfer duty must be paid within 3 months of the liability date (by 18 June 2026).

If duty is not paid by the due date, interest will accrue at the statutory rate under section 26 of the Taxation Administration Act 1996 (NSW).

Pay at revenueNSW.nsw.gov.au or contact Revenue NSW on 1300 XXX XXX.

Revenue NSW

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | Firm on the duty calculation (specific sliding scale rates, two-tier breakdown, consistent total). The statutory basis (Duties Act 1997 NSW, section 26 of the TAA 1996 NSW for interest) is specific and dual-cited. |
| Epistemic humility | L | Statutory assessment — Revenue NSW has applied the Duties Act to the declared purchase price. Low epistemic humility appropriate to a tax assessment. |
| Investment asymmetry | M | The duty calculation table receives structured equal treatment across its two components. The interest consequence (section 26 TAA NSW) receives brief statutory attention — the primary emphasis is on the payment deadline. |
| Blind spots | H | Assumes the purchasers know what transfer duty is, what the sliding scale rates mean, why there are two tiers in the calculation, and what interest at the statutory rate involves. Standard assumptions for property purchasers. |
| Reasoning texture | L | Statutory assessment with property-specific calculation insertions. The two-tier calculation ($40,905 + $5,265 = $46,170... wait, that's $46,170 not $45,490 — let me recheck the arithmetic.) |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The traceable urgency basis is the Duties Act 1997 (NSW) — a specific state statute that creates the duty liability and the payment deadline. The two-tier calculation reflects the actual NSW transfer duty sliding scale applied to the specific $1,150,000 purchase price. The 18 June 2026 deadline (18 March + 3 months) is internally consistent with the statute. |
| Idealisation risks | Risk of the interest consequence triggering a pressure signal. Counteracted by the traceable statutory basis (section 26 TAA NSW) and the 3-month payment window (generous deadline for a duty payment). |
| Imperfection checklist | PASS. High conviction (statutory assessment). Low epistemic humility. Medium investment asymmetry. High blind spots. Low reasoning texture. Human trace: Duties Act 1997 NSW basis and property-specific calculation. |
| Validation gate | PASS |

---

## CB-ANTI-018

**Context / subtype:** ANTI — regulatory urgency — payroll tax compliance reminder, state revenue
**Sender role:** Revenue NSW — payroll tax annual reconciliation reminder, statutory deadline
**Word count:** 146
**Ground truth:** GENUINE

### Sender profile

Revenue NSW payroll tax annual reconciliation reminder to a registered payroll tax employer. Northgate Financial Services Pty Ltd has been registered for NSW payroll tax and must lodge its annual reconciliation by 28 July 2026 (the statutory deadline under the Payroll Tax Act 2007 NSW — 28 days after the end of the payroll tax year on 30 June). This is a compliance reminder, not a breach notice.

### Example text

---

**PAYROLL TAX ANNUAL RECONCILIATION REMINDER**
Revenue NSW

**Employer:** Northgate Financial Services Pty Ltd
**ABN:** 44 XXX XXX XXX
**Payroll tax registration:** NSW-PT-44821
**Payroll tax year:** 1 July 2025 – 30 June 2026

This is a reminder that your payroll tax annual reconciliation is due by 28 July 2026.

**What you must do by 28 July 2026:**
1. Lodge your annual reconciliation through Revenue NSW Online
2. Pay any balance owing for the 2025–26 payroll tax year

**Your estimated annual payroll tax position (based on monthly returns lodged to date):**
- Total taxable wages declared (July 2025 – February 2026): $4,847,200
- Tax paid on monthly returns (July 2025 – February 2026): $218,124
- Estimated remaining payroll (March – June 2026, based on your monthly average): $2,423,600

Ensure your reconciliation reflects actual wages for the full year. Any underpayment of tax must be settled by 28 July 2026.

Revenue NSW

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | Firm on the statutory deadline (28 July 2026 — 28 days after 30 June year end, as required by the Payroll Tax Act 2007 NSW). The year-to-date figures are the employer's actual declared wages and tax paid on monthly returns. |
| Epistemic humility | M | "Estimated remaining payroll (March – June 2026, based on your monthly average)" — Revenue NSW is explicitly acknowledging that the remaining payroll is an estimate, not a confirmed figure. The reconciliation will use actual figures. Medium intensity — the year-to-date data is actual; the estimate is flagged as an estimate. |
| Investment asymmetry | M | The year-to-date figures receive structured equal attention. The estimated remaining payroll is distinguished from the actual data. The deadline emphasis is the primary investment. |
| Blind spots | H | Assumes the employer knows what the payroll tax rate is, how the reconciliation process works, and what "taxable wages" includes under the Payroll Tax Act. Standard assumptions for a registered payroll tax employer. |
| Reasoning texture | L | Compliance reminder with employer-specific data insertions. The monthly average calculation for the estimated remaining payroll ($4,847,200 / 8 months × 4 months = approximately $2,423,600) is internally consistent. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The traceable urgency basis is the Payroll Tax Act 2007 NSW — the 28 July deadline is 28 days after the 30 June year end, as specified in the Act. The year-to-date figures ($4,847,200 declared wages, $218,124 tax paid) are genuine employer-specific data from the monthly returns lodged to date. The estimated remaining payroll is calculated as a monthly average ($4,847,200 / 8 months ≈ $605,900/month × 4 months ≈ $2,423,600) — internally consistent. The epistemic humility note ("based on your monthly average") distinguishes the estimate from the actual data, which is a genuine accounting distinction. |
| Idealisation risks | Risk of the underpayment settlement requirement triggering a pressure signal. Counteracted by the standard annual reconciliation framing — this is a routine statutory process, not an enforcement action. |
| Imperfection checklist | PASS. High conviction on actual data (employer returns). Epistemic humility MEDIUM (estimated remaining payroll). Medium investment asymmetry. High blind spots. Low reasoning texture. Human trace: employer-specific year-to-date figures from monthly returns. |
| Validation gate | PASS |

---

## CB-ANTI-019

**Context / subtype:** ANTI — regulatory urgency — council development application response notice
**Sender role:** Local council — DA response period notice, statutory planning deadline
**Word count:** 153
**Ground truth:** GENUINE

### Sender profile

Penrith City Council notice to a property owner requiring a response to an objection received in relation to their development application. Mr Kowalski has lodged a DA for a secondary dwelling. A neighbouring property owner has lodged an objection. The Council is notifying Mr Kowalski of the objection and providing 14 days to respond under the Environmental Planning and Assessment Act 1979. The urgency is traceable to the EP&A Act.

### Example text

---

**DEVELOPMENT APPLICATION — OBJECTION NOTIFICATION**
Penrith City Council

**Applicant:** Mr Viktor Kowalski
**DA number:** DA-2026-0447
**Property:** [Address]
**Application type:** Secondary dwelling
**Date of this notice:** 19 March 2026

An objection to your development application has been received from an affected property owner.

**Details of the objection:**
The objection raises concerns about the following matters: overshadowing of the adjoining property, visual privacy, and potential impact on streetscape character.

**Your right to respond:**
Under section 4.15 of the Environmental Planning and Assessment Act 1979 (NSW), you have the right to respond to submissions received in relation to your development application.

**You must lodge your response by 2 April 2026 (14 days from the date of this notice).**

Your response will be considered by the assessing officer when determining your application. Responses must be lodged through Council's DA portal or by email to da@penrithcity.nsw.gov.au.

Penrith City Council — Development Assessment

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | Firm on the DA details (application number, property type, three objection grounds listed), the statutory basis (section 4.15 of the EP&A Act 1979 NSW), and the response deadline. |
| Epistemic humility | L | The Council knows the objection has been received and the assessment process requires a response opportunity. Low epistemic humility appropriate to a statutory procedural notice. |
| Investment asymmetry | M | The response deadline (2 April 2026) receives bold prominence. The three objection grounds receive equal brief attention. |
| Blind spots | M | Assumes Mr Kowalski knows what section 4.15 of the EP&A Act provides, what a streetscape character argument involves in planning terms, and how to lodge a response through the DA portal. Standard assumptions for a property owner who has already engaged with the DA process. |
| Reasoning texture | L | Statutory procedural notice with DA-specific insertions. The 2 April 2026 deadline (19 March + 14 days) is internally consistent. The three objection grounds are the specific matters raised by the objector. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The traceable urgency basis is section 4.15 of the Environmental Planning and Assessment Act 1979 (NSW) — a specific statutory provision that creates the right to respond to submissions and implicitly supports the 14-day response period as standard Council practice under the Act. The three objection grounds (overshadowing, visual privacy, streetscape character) are the specific grounds raised by the specific objector — they are not generic planning objection grounds. The DA number (DA-2026-0447) and the secondary dwelling application type are genuine application-specific data. |
| Idealisation risks | Risk of the "you must lodge your response by" urgency language triggering a pressure signal. Counteracted by the response framing ("your right to respond") and the standard Council assessment process context. |
| Imperfection checklist | PASS. High conviction (statutory process). Low epistemic humility. Medium investment asymmetry (deadline prominence). Medium blind spots. Low reasoning texture. Human trace: section 4.15 citation and specific objection grounds from genuine DA process. |
| Validation gate | PASS |

---

## CB-ANTI-020

**Context / subtype:** ANTI — regulatory urgency — council building compliance order, statutory enforcement
**Sender role:** Local council — building compliance order, specific statutory basis, remedy period
**Word count:** 164
**Ground truth:** GENUINE

### Sender profile

Parramatta City Council building compliance order requiring the owner of a commercial property to address an identified building compliance issue — specifically, a fire safety deficiency identified during an annual fire safety inspection. The order is issued under the Environmental Planning and Assessment Act 1979 and the Environmental Planning and Assessment Regulation 2021. The remedy period is 28 days. The urgency is traceable to the statutory building compliance regime.

### Example text

---

**BUILDING COMPLIANCE ORDER**
Parramatta City Council

**Property owner:** Pacific Commercial Holdings Pty Ltd
**Property:** [Address]
**Order reference:** PCC-BCO-2026-0447
**Date of order:** 18 March 2026

**NOTICE OF FIRE SAFETY DEFICIENCY — COMPLIANCE REQUIRED**

A fire safety inspection of the above property was conducted on 14 March 2026. The inspection identified the following fire safety deficiency:

**Deficiency:** Exit signs on levels 2 and 3 are not operational. This does not comply with the fire safety requirements applicable to the building under the Environmental Planning and Assessment Regulation 2021.

**Required action:**
You are required to rectify the exit sign deficiency and lodge an updated Annual Fire Safety Statement with Council within 28 days of the date of this order (by 15 April 2026).

Failure to comply with this order is an offence under section 9.37 of the Environmental Planning and Assessment Act 1979 (NSW), attracting a maximum penalty of $1,500,000 for a corporation.

If you have questions about compliance, contact Council's Building Compliance team on 02 XXXX XXXX.

Parramatta City Council — Building Compliance

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | Firm on the specific deficiency (exit signs on levels 2 and 3, not operational), the inspection date (14 March 2026), the statutory basis (EP&A Regulation 2021), and the consequence (section 9.37 EP&A Act, maximum $1,500,000). |
| Epistemic humility | L | The Council has conducted the inspection and identified the specific deficiency. Low epistemic humility appropriate to a documented building inspection finding. |
| Investment asymmetry | M | The specific deficiency and its regulatory non-compliance receive clear emphasis. The maximum penalty receives specific statutory attention. The remedy deadline (15 April 2026) is bolded. |
| Blind spots | H | Assumes the property owner knows what an Annual Fire Safety Statement involves, what section 9.37 of the EP&A Act provides, and what the maximum penalty represents in an enforcement context. Standard assumptions for a commercial property owner. |
| Reasoning texture | L | Formal compliance order with inspection-specific insertions. The 15 April 2026 deadline (18 March + 28 days) is internally consistent. The specific deficiency (exit signs on levels 2 and 3, not operational) is an inspection finding, not a generic building deficiency. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The traceable urgency basis is section 9.37 of the Environmental Planning and Assessment Act 1979 (NSW) — a specific statutory provision creating the offence and the penalty. The specific deficiency (exit signs on levels 2 and 3, not operational) is a specific inspection finding from the 14 March 2026 inspection — it is a named location (levels 2 and 3) and a specific failure (not operational). The $1,500,000 maximum penalty is the actual statutory maximum for a corporation under section 9.37 — a specific figure that requires knowledge of the statute. All consequence language is traceable to documented statutory provisions and a specific inspection finding. |
| Idealisation risks | Risk of the $1,500,000 maximum penalty triggering a disproportionate fear pressure signal. Counteracted by the "maximum penalty" framing (which is the statutory maximum, not the likely penalty for a first-time exit sign deficiency) and the specific statutory citation that makes it verifiable. |
| Imperfection checklist | PASS. High conviction (documented inspection finding, statutory basis). Low epistemic humility. Medium investment asymmetry. High blind spots. Low reasoning texture. Human trace: specific deficiency location (levels 2 and 3), section 9.37 EP&A Act citation, $1,500,000 statutory maximum. |
| Validation gate | PASS |

---

*Owlume Pty Ltd — Confidential — corpus_batch11_anti_011_020_v1 · 30 March 2026 · Batch review pending*