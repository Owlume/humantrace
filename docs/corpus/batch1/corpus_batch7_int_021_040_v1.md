# Calibration Corpus — Batch 7, Examples 21–40 (Internal)

**HumanTrace — Internal Document**
Internal Organisational — IT, HR, and Policy Communications · CB-INT-021 through CB-INT-040
Ground truth: GENUINE · Path A synthetic genuine construction
Version 1.0 · 30 March 2026 · Owlume Pty Ltd
Constructed under `corpus_construction_protocol_v1.1`

> **Batch construction note:** This batch tests institutional authority without interpersonal relationship. The authority in these communications is the role, not the person — IT security, HR, compliance, operations. The engine must learn that institutional urgency with a traceable regulatory or operational basis is a positive human marker in this context, not a synthetic pressure signal. Every example in this batch must contain a traceable basis for whatever urgency is present. Examples that lack traceable urgency have none at all.

---

## CB-INT-021

**Context / subtype:** INT — IT security — phishing attempt notification, specific affected users
**Sender role:** IT security analyst — phishing notification to specific users whose credentials were targeted
**Word count:** 142
**Ground truth:** GENUINE

### Sender profile

Kevin, IT security analyst. The company's email gateway flagged a sophisticated phishing campaign this morning — 34 employees received the email, of whom 8 clicked the link. Kevin has the list of 8 who clicked and is writing to them specifically. His notification explains what happened, what the risk is, and what each person needs to do. The urgency is genuine — if credentials were entered, the accounts may be compromised.

### Example text

---

**To:** [8 specific staff members]
**From:** Kevin Osei, IT Security
**Re:** URGENT — Phishing Email Action Required — Your Account

You received a phishing email this morning and our logs show you clicked the link in that email. We need you to take immediate action.

**What happened:** A fraudulent email impersonating Microsoft 365 was sent to a number of staff this morning. The link in the email directed to a fake login page designed to capture your credentials.

**What you need to do right now:**
1. Do not enter any further credentials into any prompt until IT has cleared your account.
2. Call the IT helpdesk on extension 4400 immediately — tell them you are calling about the phishing response.
3. Do not use your work email until you have spoken to IT.

We are treating this as a priority. IT will work through each affected account today.

Kevin Osei
IT Security

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | "Our logs show you clicked the link" — Kevin is asserting this as a documented fact from the email gateway logs. Firm on all three action instructions — no hedge. High conviction appropriate to a security analyst who has the logs and knows what needs to happen. |
| Epistemic humility | M | "Designed to capture your credentials" — Kevin knows the design of the phishing page from his analysis. What he does not know is whether any credentials were actually entered — the action instructions are precautionary because he cannot be certain. The "we are treating this as a priority" framing reflects genuine uncertainty about the extent of the compromise. |
| Investment asymmetry | H | The three specific action instructions receive the most structured attention — this is what the recipients need to do and the sequence matters. The explanation of what happened is brief. Kevin's stake is in the three actions being taken immediately. |
| Blind spots | M | Assumes the recipients know what "credentials" means in this context, what a fake login page does with entered credentials, and what "cleared your account" means in the IT security process. Standard assumptions for office workers in a Microsoft 365 environment. |
| Reasoning texture | M | "Tell them you are calling about the phishing response" — Kevin has anticipated that the helpdesk will receive a surge of calls and has given the recipients a specific identifier to use so their calls are prioritised. That anticipatory instruction — knowing how the helpdesk triage works and including it in the user communication — is the trace of an IT security analyst who has managed security incidents before. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. Two shared-context artefacts: the email gateway logs (Kevin has specific documented evidence of which users clicked) and the helpdesk extension 4400 with a specific call identifier ("phishing response"). The logs reference is the strongest trace — it establishes that Kevin has specific evidence about these 8 specific recipients, which distinguishes this from a blanket security alert. The helpdesk identifier reflects Kevin's knowledge of how his own IT department's incident response process works. |
| Idealisation risks | Risk of making the urgency feel synthetic (security alert + authority + immediate action required). Counteracted by the specific log evidence ("our logs show you clicked") and the specific helpdesk protocol ("tell them you are calling about the phishing response") — both require genuine operational knowledge. |
| Imperfection checklist | PASS. High conviction on logged evidence. Epistemic humility MEDIUM (credential entry uncertain). Investment asymmetry HIGH (three action instructions). Blind spots MEDIUM. Reasoning texture MEDIUM — helpdesk triage knowledge. Human trace: email gateway logs and helpdesk identifier as non-replicable operational knowledge. |
| Validation gate | PASS |

---

## CB-INT-022

**Context / subtype:** INT — IT security — mandatory password reset, vendor breach notification
**Sender role:** IT manager — mandatory password reset following third-party credential exposure
**Word count:** 118
**Ground truth:** GENUINE

### Sender profile

Sandra, IT manager. The company uses a third-party HR software vendor — Workday. Workday has notified all enterprise clients that they experienced a credential exposure incident affecting a subset of accounts. The company's security team has assessed that the company's Workday credentials may be in the affected subset. Sandra is requiring all staff who have Workday access to reset their passwords within 24 hours. The urgency is external — the vendor breach notification is the traceable basis.

### Example text

---

**To:** All Workday Users (156 staff)
**From:** Sandra Webb, IT Manager
**Re:** MANDATORY — Workday Password Reset Required Within 24 Hours

Workday has notified us that they experienced a security incident affecting customer credentials. While we cannot confirm whether our accounts were specifically affected, the company's security policy requires us to treat this as a precautionary reset.

**You must reset your Workday password within the next 24 hours.**

To reset: log into Workday > click your profile icon > Security > Change Password. Use a password that is at least 12 characters and has not been used for any other account.

If you do not reset within 24 hours, your Workday access will be suspended until the reset is completed.

IT has notified HR of this requirement. If you have difficulty resetting, contact the helpdesk on extension 4400.

Sandra Webb
IT Manager

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | M | Firm on the requirement (mandatory reset within 24 hours, suspension if not completed). Appropriately uncertain on the specific impact: "we cannot confirm whether our accounts were specifically affected" — Sandra is being honest about what the vendor told her and what she does not know. Medium intensity reflects the asymmetry: certain on the required action, honest about the uncertain scope. |
| Epistemic humility | M | "We cannot confirm whether our accounts were specifically affected" — Sandra is explicitly stating the limit of her knowledge. The "precautionary reset" framing is honest — it is precautionary, not certain. The 24-hour deadline reflects a security policy standard, not Sandra's personal assessment of the risk level. |
| Investment asymmetry | M | The reset instruction (specific path: profile icon > Security > Change Password) receives the most structured attention — this is what every recipient needs to be able to do. The consequence (suspension) is stated clearly. The vendor notification background is brief. |
| Blind spots | M | Assumes all 156 Workday users know what Workday is (they use it), where their profile icon is, and what a 12-character password requirement means. Standard assumptions for active users of a system. |
| Reasoning texture | L | "IT has notified HR of this requirement" — Sandra has pre-coordinated with HR because the Workday system contains HR data and HR needs to be aware of the suspension risk. This pre-coordination, made visible in one sentence, reflects Sandra's knowledge of which other teams are affected by the Workday access suspension risk. Near-template institutional communication with one co-ordination disclosure. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. Two shared-context artefacts: the Workday vendor notification (a specific external communication Sandra received, triggering this action) and the HR pre-coordination (a specific internal action Sandra has already taken). The "we cannot confirm whether our accounts were specifically affected" is the strongest trace — it is Sandra's honest communication of the limit of the vendor's disclosure, which requires her to have received and read the actual vendor notification. |
| Idealisation risks | Risk of making the reset instruction too vague — losing the specific path that reduces helpdesk load. Counteracted by the specific path (profile icon > Security > Change Password). Risk of making the urgency feel synthetic. Counteracted by the explicit vendor notification basis and the honest uncertainty about scope. |
| Imperfection checklist | PASS. Medium conviction (precautionary, scope uncertain). Epistemic humility MEDIUM (honest about vendor disclosure limits). Investment asymmetry MEDIUM (reset path and consequence). Reasoning texture LOW (one co-ordination disclosure). Human trace: vendor notification basis and HR pre-coordination. |
| Validation gate | PASS |

---

## CB-INT-023

**Context / subtype:** INT — IT systems — planned maintenance window, scheduled downtime
**Sender role:** IT systems administrator — planned maintenance notification, no urgency
**Word count:** 104
**Ground truth:** GENUINE

### Sender profile

Marcus, IT systems administrator. The company's ERP system (SAP) has scheduled maintenance on Saturday night — 10pm to 2am Sunday. This is a regular quarterly maintenance window. Marcus is sending the advance notification to all relevant staff. No urgency — this is a planned, scheduled event. The communication is informational and practical.

### Example text

---

**To:** All SAP Users
**From:** Marcus Tan, IT Systems
**Re:** Scheduled SAP Maintenance — Saturday 28 March, 10:00 PM to Sunday 29 March, 2:00 AM

Please be advised that SAP will be unavailable for scheduled maintenance from 10:00 PM Saturday 28 March to 2:00 AM Sunday 29 March 2026.

During this window, you will not be able to access SAP, including all modules (FI, CO, MM, SD).

If you have time-sensitive reports or transactions that need to be completed before the maintenance window, please ensure these are done by 9:30 PM Saturday.

SAP will be fully restored by 2:00 AM Sunday. If the maintenance runs longer than expected, IT will send an update.

For urgent issues during the maintenance window, contact the on-call IT team on 0400 XXX XXX.

Marcus Tan
IT Systems

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | Firm on the maintenance window (specific dates and times), firm on what will be unavailable (all modules listed), firm on the restoration time ("fully restored by 2:00 AM Sunday"). These are scheduled facts. |
| Epistemic humility | L | "If the maintenance runs longer than expected, IT will send an update" — the one genuine uncertainty. Marcus is being honest that maintenance windows can overrun. Low overall epistemic humility — this is a planned event with known parameters. |
| Investment asymmetry | L | Flat attention across all elements — the maintenance window, the unavailable modules, the pre-maintenance action recommendation, the restoration time, and the on-call contact all receive equal treatment. No personal stake creates flat attention distribution. |
| Blind spots | M | Assumes SAP users know what FI, CO, MM, SD modules are and which ones they use. Standard assumption for active SAP users. |
| Reasoning texture | L | "If you have time-sensitive reports or transactions that need to be completed before the maintenance window, please ensure these are done by 9:30 PM Saturday" — Marcus has added a 30-minute buffer before the 10pm maintenance start. This is practical knowledge about how long it takes to complete a transaction after initiating it — the buffer prevents users from starting something at 9:58pm that they cannot finish. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS — minimal but present. The 9:30 PM buffer recommendation is the human trace — it reflects Marcus's operational knowledge that users need lead time before the hard cutoff. A fully automated maintenance notification would say "ensure work is completed before 10:00 PM." Marcus's version adds the 30-minute buffer from experience. |
| Idealisation risks | This example tests the engine's LOW threshold on informational IT communications with no urgency. The risk is making it too interesting. Counteracted by keeping the register purely informational and the content purely practical. |
| Imperfection checklist | PASS — modified. High conviction (scheduled event). Low epistemic humility (one overrun acknowledgment). Flat investment asymmetry. Low reasoning texture (appropriate). Human trace: 30-minute buffer from operational experience. |
| Validation gate | PASS |

---

## CB-INT-024

**Context / subtype:** INT — IT systems — software licence expiry notification to department heads
**Sender role:** IT helpdesk manager — licence expiry notification, procurement action required
**Word count:** 112
**Ground truth:** GENUINE

### Sender profile

Amy, IT helpdesk manager. The Adobe Creative Cloud licences for the Marketing and Design teams expire on 15 April 2026. Renewal requires department head approval before IT can process the procurement. Amy is writing to the two department heads — the marketing director and the creative director — with the specific information they need to approve the renewal. The deadline is practical — procurement takes 10 business days, so approval is needed by 31 March.

### Example text

---

**To:** Marketing Director, Creative Director
**From:** Amy Walsh, IT Helpdesk Manager
**Re:** Adobe Creative Cloud Licence Renewal — Approval Required by 31 March

Your team's Adobe Creative Cloud licences expire on 15 April 2026. Renewal requires your approval before IT can process the order.

**Current licences:**
- Marketing team: 8 licences (Adobe CC All Apps)
- Design team: 6 licences (Adobe CC All Apps)

**Annual cost:** $14,280 (total, both teams — same as last year)

Procurement takes approximately 10 business days, which is why I need approval by 31 March to ensure no gap in access.

To approve: reply to this email confirming you approve renewal for your team's licences. That's all I need — IT will handle the rest.

If either team's requirements have changed (additional licences needed, or any to remove), please let me know at the same time.

Amy Walsh
IT Helpdesk Manager

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | Firm on all specifics: the expiry date (15 April 2026), the licence counts (8 Marketing, 6 Design), the cost ($14,280, same as last year), the procurement timeline (10 business days), and the approval deadline (31 March). All documented facts from the IT procurement system. |
| Epistemic humility | L | "If either team's requirements have changed...please let me know at the same time" — Amy is acknowledging that requirements may have changed since last year. Low overall epistemic humility — the facts are documented and the process is clear. |
| Investment asymmetry | M | The licence counts and cost receive structured attention — the department heads need this information to approve. The approval process ("reply to this email") is deliberately simple. Amy's stake is in getting approval before the deadline; the simplicity of the approval path reflects that. |
| Blind spots | M | Assumes the department heads know what Adobe Creative Cloud All Apps includes, what the procurement process involves, and why a 10-business-day lead time requires a 31 March deadline for an 15 April expiry. Standard assumptions for department heads who manage team software needs. |
| Reasoning texture | M | "Same as last year" — Amy has included this because department heads will want to know whether the cost has changed before approving. The three-word comparison is her anticipation of their question. "To approve: reply to this email...That's all I need — IT will handle the rest" — Amy has made the approval path as simple as possible because she has learned that complex approval processes create delays. Both reflect operational knowledge of how department head approvals actually work. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. Two shared-context artefacts: the specific licence counts (8 + 6 — pulled from the IT asset management system) and the "same as last year" cost comparison (which requires Amy to have the prior year's cost on hand). The 10-business-day procurement timeline is also a trace — it is Amy's knowledge of how long the specific procurement process takes for software licences. |
| Idealisation risks | Risk of making the approval request too complex — losing the "simplest possible approval path" design. Counteracted by "reply to this email...That's all I need." |
| Imperfection checklist | PASS. High conviction (documented licence facts). Low epistemic humility (requirements change acknowledged). Investment asymmetry MEDIUM. Reasoning texture MEDIUM — "same as last year" anticipation and simplified approval path. Human trace: specific licence counts and prior year cost comparison. |
| Validation gate | PASS |

---

## CB-INT-025

**Context / subtype:** INT — IT security — MFA enforcement rollout, new requirement with deadline
**Sender role:** IT security manager — MFA enforcement notification, explains why without being preachy
**Word count:** 121
**Ground truth:** GENUINE

### Sender profile

Jerome, IT security manager. The company is rolling out mandatory multi-factor authentication for all remote access. The board approved the security uplift in February following the company's cyber insurance renewal, which required MFA as a condition. The deadline for all staff to have MFA configured is 14 April 2026, after which remote access without MFA will be blocked. Jerome is writing the all-staff notification. He wants to explain the why without being preachy or making people feel surveilled.

### Example text

---

**To:** All Staff
**From:** Jerome Castillo, IT Security Manager
**Re:** Multi-Factor Authentication — Required for All Remote Access by 14 April 2026

From 14 April 2026, multi-factor authentication (MFA) will be required for all remote access to company systems, including email access outside the office.

**Why this is happening:** Our cyber insurance renewal in February included MFA as a condition of coverage. This is standard across the industry and reflects the genuine risk environment for businesses of our size.

**What you need to do:** Set up MFA on your device before 14 April. IT has prepared a step-by-step guide available on the intranet under IT > Security > MFA Setup. The setup takes approximately 10 minutes.

**What happens after 14 April:** Remote access without MFA will not be possible. If you work remotely or travel for work, this affects you.

If you need help with setup, the IT helpdesk is running drop-in sessions Tuesday and Thursday afternoons in the IT office (Level 3) from now until 14 April.

Jerome Castillo
IT Security Manager

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | Firm on all specifics: the 14 April deadline, the insurance condition basis, the intranet path, the setup time (10 minutes), the drop-in session schedule. These are all verified facts from the rollout plan. |
| Epistemic humility | L | "If you work remotely or travel for work, this affects you" — Jerome is being practical about who is affected. Low epistemic humility — the requirements are clear and the timeline is fixed. |
| Investment asymmetry | M | The why-this-is-happening section receives specific attention — Jerome has decided that explaining the insurance basis will make the requirement more credible. The setup instructions are structured and practical. The drop-in sessions are specific (days, times, location). |
| Blind spots | M | Assumes all staff know what MFA is at a basic level, where the intranet is and how to navigate to IT > Security, and what "remote access" means for their specific situation. Standard assumptions for a modern office workforce. |
| Reasoning texture | M | "This is standard across the industry and reflects the genuine risk environment for businesses of our size" — Jerome is contextualising the requirement without overstating the threat. He is not generating fear (which would be synthetic pressure); he is being honest about why the insurance requirement exists. The drop-in sessions in the IT office (specific location, Level 3) are Jerome's practical addition — he has set up the sessions and knows where they are. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. Two shared-context artefacts: the February cyber insurance renewal (a specific event with a specific month that triggered this requirement) and the Level 3 IT office drop-in sessions (a specific physical location and schedule that Jerome has organised). The insurance renewal basis is the strongest trace — it is a specific internal event that required board approval and that Jerome knows because he was part of that process. |
| Idealisation risks | Risk of making the why-explanation too prominent — making employees feel surveilled. Counteracted by "standard across the industry and reflects the genuine risk environment" — normalising the requirement rather than dramatising the threat. |
| Imperfection checklist | PASS. High conviction (fixed requirements). Low epistemic humility (clear rollout). Investment asymmetry MEDIUM (why-explanation and drop-in sessions). Reasoning texture MEDIUM — industry context explanation, Level 3 location specificity. Human trace: February insurance renewal and organised drop-in session location. |
| Validation gate | PASS |

---

## CB-INT-026

**Context / subtype:** INT — HR policy — parental leave policy update, improved entitlements
**Sender role:** HR manager — parental leave improvement notification, positive news with implementation detail
**Word count:** 119
**Ground truth:** GENUINE

### Sender profile

Rachel, HR manager. The company has improved its parental leave policy — primary carer leave increases from 12 to 16 weeks at full pay, effective 1 May 2026. This is positive news. Rachel is writing the all-staff communication. The challenge is communicating a policy improvement clearly without generating confusion about who is eligible or when the new entitlement applies.

### Example text

---

**To:** All Staff
**From:** Rachel Osei, HR Manager
**Re:** Parental Leave Policy Update — Improved Entitlements from 1 May 2026

We are pleased to advise that the company's parental leave policy has been updated, effective 1 May 2026.

**Key change:** Primary carer leave increases from 12 weeks to 16 weeks at full pay.

**Who this applies to:** All permanent employees who become primary carers of a new child (birth, adoption, or long-term foster placement) on or after 1 May 2026.

**What about leave that has already started?** If you commenced primary carer leave before 1 May 2026, the previous entitlement (12 weeks) applies to your current leave. If your leave commences on or after 1 May 2026, the new entitlement (16 weeks) applies.

The updated policy is available on the HR portal. If you have questions about how this applies to your specific situation, please contact your HR business partner.

Rachel Osei
HR Manager

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | Firm on all specifics: the 1 May effective date, the 12-to-16-week change, the eligibility criteria (permanent employees, on or after 1 May), the transition rule (commenced before vs on or after). These are policy facts. |
| Epistemic humility | M | "If you have questions about how this applies to your specific situation, please contact your HR business partner" — Rachel is acknowledging that individual circumstances vary and she cannot address all situations in one communication. The transition rule section (before vs on or after 1 May) reflects genuine complexity that Rachel has thought through but acknowledges may not cover all edge cases. |
| Investment asymmetry | M | The transition rule (who gets the old vs new entitlement) receives the most structured attention — this is the question that will generate the most individual queries and Rachel has pre-empted it. The key change is stated simply. |
| Blind spots | M | Assumes employees understand what "primary carer" means legally, what "permanent employee" means vs casual, and what "long-term foster placement" includes. The HR business partner referral partially addresses this for edge cases. |
| Reasoning texture | M | The transition rule section is Rachel's addition to the standard policy announcement format — she has thought about who will read this and what their first question will be (does this apply to me if I'm currently on leave?). The specific addressing of the before/after distinction reflects her anticipation of that question from employees currently on leave or about to start. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The transition rule section is the human trace — specifically the before/after 1 May distinction for currently-on-leave employees. A template policy announcement would state the new entitlement and the effective date. Rachel's version adds the transition rule because she has thought about the employees who will read this and worry that the improvement does not apply to them. That anticipatory inclusion reflects knowledge of how employees process policy changes. |
| Idealisation risks | Risk of making the positive news too promotional — over-celebrating the improvement. Counteracted by keeping the tone informational throughout and focusing on practical clarity rather than organisational celebration. |
| Imperfection checklist | PASS. High conviction (policy facts). Epistemic humility MEDIUM (individual situations vary, HR business partner referral). Investment asymmetry MEDIUM (transition rule attention). Reasoning texture MEDIUM — transition rule as pre-emptive question addressing. Human trace: transition rule inclusion from employee-perspective thinking. |
| Validation gate | PASS |

---

## CB-INT-027

**Context / subtype:** INT — HR policy — flexible work arrangement review, annual process
**Sender role:** HR business partner — flexible work arrangement annual review, careful about anxiety
**Word count:** 107
**Ground truth:** GENUINE

### Sender profile

Michelle, HR business partner. The company conducts annual reviews of flexible work arrangements — employees with approved arrangements need to confirm they want to continue and managers need to confirm the arrangement is still operationally viable. The process is not a threat to existing arrangements — most will be renewed without change. Michelle is writing to employees who currently have approved arrangements. She wants to communicate the process clearly without generating anxiety that arrangements are at risk.

### Example text

---

**To:** Employees with Approved Flexible Work Arrangements
**From:** Michelle Torres, HR Business Partner
**Re:** Annual Review of Your Flexible Work Arrangement — Action Required by 11 April 2026

Your flexible work arrangement is due for its annual review. This is a standard process that applies to all employees with approved arrangements.

**What you need to do:** Complete the Annual Review Form (available on the HR portal under Flexible Work) and submit it to your manager by 11 April 2026. Your manager will then confirm the arrangement for the coming year.

In most cases, reviews result in continuation of the existing arrangement. If there are any changes to consider, your manager will discuss these with you directly.

If you have questions or concerns about the review process, please reach out to me directly.

Michelle Torres
HR Business Partner

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | M | Firm on the process (Annual Review Form, 11 April deadline, manager confirmation). Deliberately reassuring on the likely outcome: "in most cases, reviews result in continuation of the existing arrangement." Michelle is being honest about the most common outcome without guaranteeing it. |
| Epistemic humility | M | "In most cases" — Michelle does not know which specific arrangements will be continued or changed; she knows the historical pattern. The "if there are any changes to consider" framing acknowledges that some arrangements may change without specifying which. Medium intensity — the process is clear but individual outcomes are not predetermined. |
| Investment asymmetry | M | The reassurance paragraph ("in most cases, reviews result in continuation") receives disproportionate attention relative to its length — it is one sentence but it is the sentence that matters most to the recipients. Michelle's professional stake is in the communication not generating unnecessary anxiety. |
| Blind spots | M | Assumes employees know where the HR portal is and how to navigate to Flexible Work, what the Annual Review Form involves, and what "manager confirmation" means as a process step. Standard assumptions for employees who have been through this process before. |
| Reasoning texture | M | The "in most cases" reassurance is Michelle's deliberate insertion into what would otherwise be a process notification. She has included it because she knows employees with flexible work arrangements will read this communication with anxiety about whether their arrangement is at risk. The reassurance is honest (most arrangements are continued) and strategically placed (after the process instruction, before the closing) to reduce that anxiety without making a promise she cannot keep. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The "in most cases" reassurance is the human trace — Michelle has included it because she knows the emotional response this communication will trigger in its recipients. A template annual review notification would state the process and the deadline. Michelle's version adds the reassurance because she has spoken to employees who have been anxious about previous reviews and knows this information matters to them. |
| Idealisation risks | Risk of making the reassurance too strong — implying arrangements will not change. Counteracted by "in most cases" (not "arrangements will be continued") and "if there are any changes to consider, your manager will discuss these with you directly" (which acknowledges changes are possible). |
| Imperfection checklist | PASS. Medium conviction (process firm, outcome appropriately uncertain). Epistemic humility MEDIUM ("in most cases" honest qualifier). Investment asymmetry MEDIUM (reassurance prominence). Reasoning texture MEDIUM — employee-anxiety awareness driving reassurance insertion. Human trace: "in most cases" reassurance from knowledge of employee anxiety pattern. |
| Validation gate | PASS |

---

## CB-INT-028

**Context / subtype:** INT — HR policy — superannuation change notification, legislative change
**Sender role:** HR director — superannuation legislative change notification, regulatory basis clear
**Word count:** 116
**Ground truth:** GENUINE

### Sender profile

Catherine, HR director. The superannuation guarantee rate increases from 11% to 11.5% effective 1 July 2026 — a legislated increase under the Superannuation Guarantee (Administration) Act. Catherine is writing the all-staff notification. The change is external and legislated — Catherine's role is to communicate it accurately and explain what employees need to do (which is nothing — the change is automatic). The clarity challenge is making sure employees understand they do not need to take action.

### Example text

---

**To:** All Staff
**From:** Catherine Okafor, HR Director
**Re:** Superannuation Guarantee Rate Increase — Effective 1 July 2026

The superannuation guarantee rate will increase from 11% to 11.5% of ordinary time earnings, effective 1 July 2026. This is a legislated change under the Superannuation Guarantee (Administration) Act.

**What this means for you:** Your employer superannuation contributions will increase from 1 July 2026. You do not need to take any action — the change will be applied automatically through payroll.

**What this means for the company:** The company's payroll costs will increase proportionally. This has been budgeted for.

If you have questions about how the change applies to your specific situation (for example, if you are on a package that includes super), please contact your HR business partner or payroll.

Catherine Okafor
HR Director

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | Firm on the legislative fact (11% to 11.5%, 1 July 2026, legislated under the SGAA). The "this has been budgeted for" statement is a specific internal fact that Catherine is asserting with confidence. |
| Epistemic humility | L | "If you have questions about how the change applies to your specific situation (for example, if you are on a package that includes super)" — Catherine is acknowledging that individual circumstances vary. Low overall epistemic humility — the legislative change is clear and the internal implications are known. |
| Investment asymmetry | M | The "you do not need to take any action" statement receives prominent placement — this is the most important practical information for most employees. The company cost impact is included specifically to pre-empt the question of whether the company has budgeted for this. |
| Blind spots | M | Assumes employees understand what "ordinary time earnings" means as a superannuation base, what a "total remuneration package that includes super" means for the calculation, and what the payroll process involves. The HR business partner referral addresses the edge cases. |
| Reasoning texture | M | "This has been budgeted for" — Catherine has included this because she knows employees sometimes worry that legislated employer cost increases will affect their other conditions. The "budgeted for" statement pre-empts that concern. It is a small but deliberate inclusion that reflects Catherine's knowledge of the questions she typically receives after payroll-affecting announcements. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The "this has been budgeted for" statement is the human trace — it is Catherine's pre-emption of a specific concern (will the cost increase affect my salary review?) that she knows employees will have. A template legislative change notification would not include this. Catherine's version includes it because she has experience with how employees respond to payroll cost announcements. |
| Idealisation risks | Risk of making the "you do not need to take any action" too prominent — causing employees on total remuneration packages to incorrectly assume they need no action. Counteracted by the specific exception note for package employees. |
| Imperfection checklist | PASS. High conviction (legislative fact). Low epistemic humility (clear legislative change). Investment asymmetry MEDIUM ("no action needed" prominence). Reasoning texture MEDIUM — "budgeted for" pre-emption. Human trace: "budgeted for" from knowledge of employee salary-concern pattern. |
| Validation gate | PASS |

---

## CB-INT-029

**Context / subtype:** INT — HR — Employee Assistance Program communication, supportive register
**Sender role:** HR manager — EAP communication, reaching people who may not seek support
**Word count:** 108
**Ground truth:** GENUINE

### Sender profile

Rebecca, HR manager. The company's Employee Assistance Program (EAP) provides confidential counselling and support services to all employees. The company has recently renewed the EAP contract and Rebecca is sending a reminder communication — not because there is a specific trigger event, but because EAP usage tends to drop after the initial announcement and regular reminders increase uptake for employees who need it but have not yet reached out. Her register is supportive and non-pressuring.

### Example text

---

**To:** All Staff
**From:** Rebecca Morrison, HR Manager
**Re:** Employee Assistance Program — Free Confidential Support Available

A reminder that our Employee Assistance Program (EAP) is available to all employees and their immediate family members, free of charge.

The EAP provides confidential counselling and support for a range of personal and work-related concerns — including stress, mental health, relationships, financial concerns, and grief. Services are provided by qualified counsellors and are completely confidential — your employer does not receive information about who uses the service or what it is used for.

**To access the EAP:** Call 1800 XXX XXX (available 24/7) or visit [EAP provider website].

You do not need to be in crisis to use this service. Support is available for any concern, large or small.

Rebecca Morrison
HR Manager

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | M | Firm on the facts of the service (what it covers, who is eligible, that it is confidential, that the employer does not receive information). The "completely confidential — your employer does not receive information about who uses the service" is stated with full conviction because it is a contractual commitment from the EAP provider. |
| Epistemic humility | L | The EAP services are known and documented. Low epistemic humility appropriate to a communication about a known available service. |
| Investment asymmetry | M | The confidentiality assurance receives the most specific language — "your employer does not receive information about who uses the service or what it is used for." Rebecca knows this is the primary barrier to EAP use and has addressed it explicitly. |
| Blind spots | M | Assumes employees know what the EAP is at a basic level (returning employees may not), what "qualified counsellors" means in this context, and that "immediate family members" includes partners and children. The communication is deliberately written for employees who may not know the service exists. |
| Reasoning texture | M | "You do not need to be in crisis to use this service. Support is available for any concern, large or small" — Rebecca has included this because research on EAP usage consistently shows that employees who would most benefit delay contact because they believe their concern is not serious enough. This sentence addresses that barrier directly. It is not template language — it is Rebecca's translation of EAP usage research into actionable communication. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The "you do not need to be in crisis" sentence is the human trace. It exists because Rebecca has seen EAP usage data and knows the most common reason employees do not use the service is believing their concern does not justify it. That knowledge — specific to the challenge of EAP communication — and the sentence it produced, is the trace of an HR professional who has thought about why this particular kind of communication typically fails to reach the people who need it. |
| Idealisation risks | Risk of making the EAP communication too clinical — losing the supportive register. Counteracted by the "large or small" framing and the 24/7 access note. Risk of making it too warm — creating an emotional tone that feels performative. Counteracted by keeping the register informational and the warmth implicit in the content (confidentiality assurance, family member inclusion). |
| Imperfection checklist | PASS. Medium conviction (service facts). Low epistemic humility (known service). Investment asymmetry MEDIUM (confidentiality prominence). Reasoning texture MEDIUM — "not in crisis" sentence from EAP usage research. Human trace: "not in crisis" sentence from knowledge of specific EAP uptake barrier. |
| Validation gate | PASS |

---

## CB-INT-030

**Context / subtype:** INT — HR — workplace investigation notification to manager, most sensitive HR communication in batch
**Sender role:** HR business partner — notifying a manager that a complaint has been raised about their team
**Word count:** 121
**Ground truth:** GENUINE

### Sender profile

Michelle, HR business partner. A complaint has been raised by an employee in the Finance team about conduct in the workplace. Michelle cannot share the details of the complaint with the team's manager, Daniel, because the investigation is confidential — but she needs to notify Daniel that an investigation is underway so he does not interfere inadvertently. Daniel is not under investigation himself — the complaint is about a peer-level conduct issue within his team. Michelle's communication must be precise about what she can and cannot tell him, and what she needs from him.

### Example text

---

Dear Daniel,

I am writing to let you know that HR is conducting a confidential workplace investigation involving a member of your team. I am not in a position to share the details of the complaint at this stage, and I ask that you treat this communication as confidential.

What I need from you: please continue to manage your team's day-to-day work as normal. Do not discuss this matter with any member of your team, including the individual(s) who may be involved. If any team member raises this matter with you, please direct them to me.

This is not a reflection on your management — I want to be clear about that. It is a standard HR process and you have done the right thing by being informed.

I will update you as soon as I am in a position to do so.

Michelle Torres
HR Business Partner

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | M | Firm on what she needs from Daniel (continue normal management, do not discuss, direct any questions to her). Explicitly limited on what she can share: "I am not in a position to share the details of the complaint at this stage." Medium intensity reflects the deliberate asymmetry — certain about the process requirements, constrained on the factual details. |
| Epistemic humility | M | "I will update you as soon as I am in a position to do so" — Michelle does not know when she will be able to share more. She is being honest about the limit of her ability to communicate at this stage rather than giving a false timeline. |
| Investment asymmetry | H | "This is not a reflection on your management — I want to be clear about that" — this sentence receives disproportionate attention for its length. Michelle's professional stake is in Daniel not feeling implicated when he is not, and in him not interfering with the investigation because he is anxious about his own position. |
| Blind spots | L | Michelle has thought carefully about how Daniel will receive this communication. She knows he will be anxious and is pre-empting the most likely anxiety (that he is under investigation). Low blind spots — she has anticipated Daniel's experience of receiving this communication. |
| Reasoning texture | H | The "not a reflection on your management" sentence is the most carefully constructed in this sub-type. Michelle is doing two things simultaneously: reassuring Daniel that he is not under investigation, and framing the investigation as a standard HR process that he should support rather than resist. The "you have done the right thing by being informed" closing is also deliberate — it frames his knowledge of the investigation as a process step, not a burden. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The human trace is the "not a reflection on your management" sentence. Michelle has included this because she has managed workplace investigations before and knows that managers who receive this communication typically assume they are implicated, which leads to defensive behaviour that can interfere with the investigation. The pre-emptive reassurance is the product of that experience — it could only be included by someone who knows what managers typically feel when they receive this kind of notification. |
| Idealisation risks | Risk of making the reassurance too prominent — suggesting Michelle knows more about who is involved than she is allowed to share. Counteracted by keeping the "not a reflection on you" framing as a process statement, not a factual disclosure about who the complaint involves. |
| Imperfection checklist | PASS. Medium conviction (process requirements clear, facts constrained). Epistemic humility MEDIUM (update timeline unknown). Investment asymmetry HIGH ("not a reflection" prominence). Low blind spots (Daniel's anticipated experience considered). Reasoning texture HIGH — "not a reflection" and "you have done the right thing" as experienced-investigator trace. Human trace: pre-emptive reassurance from knowledge of manager anxiety pattern in investigation notifications. |
| Validation gate | PASS |

---

## CB-INT-031

**Context / subtype:** INT — compliance — annual compliance declaration, all-staff, regulatory basis
**Sender role:** Compliance manager — annual compliance declaration requirement, regulatory deadline
**Word count:** 108
**Ground truth:** GENUINE

### Sender profile

Daniel, compliance manager. All staff in regulated roles must complete the annual compliance declaration by 31 March 2026 — the last day of the compliance year. The declaration confirms they have read and complied with the company's key compliance policies during the year. ASIC requires the company to maintain records of these declarations. Daniel is writing the final reminder — the deadline is in three days and 47 staff have not yet completed it.

### Example text

---

**To:** [47 staff members — regulated roles]
**From:** Daniel Park, Compliance Manager
**Re:** FINAL REMINDER — Annual Compliance Declaration Due 31 March 2026

Your annual compliance declaration has not yet been completed. The deadline is 31 March 2026 — three days from today.

The declaration is required for all staff in regulated roles and forms part of the company's regulatory obligations to ASIC. Non-completion will be recorded and escalated to your line manager and the Chief Compliance Officer.

**To complete:** Log into the Compliance Portal > Declarations > Annual Compliance Declaration 2026. The declaration takes approximately 5 minutes.

If you have a genuine reason why you cannot complete the declaration by 31 March (for example, you are on approved leave), please contact me directly today.

Daniel Park
Compliance Manager

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | Firm on the deadline (31 March 2026), the regulatory basis (ASIC obligations), and the consequence (recorded, escalated to line manager and Chief Compliance Officer). All stated without hedge — these are documented regulatory requirements. |
| Epistemic humility | L | "If you have a genuine reason why you cannot complete the declaration by 31 March (for example, you are on approved leave), please contact me directly today" — Daniel is acknowledging that exceptions exist. Low overall epistemic humility — the requirement is clear and the deadline is fixed. |
| Investment asymmetry | M | The consequence statement (recorded, escalated) receives specific prominent placement — Daniel needs this to be taken seriously and the consequence is the mechanism. The portal path is specific. |
| Blind spots | M | Assumes the 47 recipients know what the compliance portal is, what a compliance declaration involves, what ASIC's role is in this context, and why their role is categorised as regulated. Standard assumptions for staff who have completed this in prior years. |
| Reasoning texture | L | "Three days from today" — Daniel has added the day count to the date because he knows that "31 March" is more abstract than "three days from today" for recipients who receive many deadline communications. The specific exception example (approved leave) prevents ambiguous responses while acknowledging that real exceptions exist. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The 47-staff specificity (mentioned in sender profile) is the strongest trace — Daniel has run the completion report and is writing only to the non-completers. The "three days from today" addition is also a trace — it reflects Daniel's knowledge that deadline communications need to make the urgency concrete, not abstract. The approved leave exception reflects Daniel's operational knowledge that some non-completers have legitimate reasons that need to be handled separately. |
| Idealisation risks | Risk of making the consequence language too aggressive — generating resentment rather than compliance. Counteracted by including the legitimate exception pathway ("if you have a genuine reason"). |
| Imperfection checklist | PASS. High conviction (regulatory requirements). Low epistemic humility (exception pathway noted). Investment asymmetry MEDIUM (consequence prominence). Reasoning texture LOW (appropriate). Human trace: 47-staff targeting from completion report, "three days from today" from deadline-concreteness knowledge. |
| Validation gate | PASS |

---

## CB-INT-032

**Context / subtype:** INT — compliance — internal audit documentation request, specific documents, specific people
**Sender role:** Internal audit manager — requesting documentation for upcoming audit, specific and targeted
**Word count:** 112
**Ground truth:** GENUINE

### Sender profile

Sarah, internal audit manager. The Q1 internal audit of the procurement function begins on 7 April. Sarah is writing to the three people in the procurement team whose areas are being audited, requesting specific documents she needs before the audit begins. She has done this audit three times before — she knows exactly what she needs.

### Example text

---

**To:** James Okafor (Procurement), Lisa Chen (Supplier Management), Mark Webb (Contract Administration)
**From:** Sarah Thornton, Internal Audit Manager
**Re:** Q1 Procurement Audit — Documentation Required by 4 April 2026

The Q1 procurement audit begins on 7 April 2026. I need the following documentation from each of you before 4 April.

**From James:** Procurement approvals register for Q1 2026, with supporting purchase orders for any transaction over $50,000.

**From Lisa:** Supplier performance review records for Q1 2026, including any performance issues raised and their resolution.

**From Mark:** Contract variations register for Q1 2026, including the change control documentation for any variation over $25,000.

Please send directly to sarah.thornton@company.com. Do not send through the general audit inbox — I need to review these before the opening meeting.

Sarah Thornton
Internal Audit Manager

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | Firm on all specifics: the audit start date, the documentation deadline, the three named individuals, the specific documents required from each, the dollar thresholds ($50,000 and $25,000), and the specific email address (not the general inbox). All reflect Sarah's prior audit knowledge of what she needs. |
| Epistemic humility | L | Sarah knows what she needs. Three prior audits have told her exactly which documents are relevant and what thresholds trigger mandatory supporting documentation. Low epistemic humility appropriate to an experienced auditor preparing a known audit. |
| Investment asymmetry | M | The three document requests receive equal structured attention — each is equally important to the audit. The "do not send through the general audit inbox" instruction receives specific emphasis — Sarah needs the documents before the opening meeting, which requires her to have them in her specific inbox for pre-review. |
| Blind spots | M | Assumes the three recipients know where their respective registers are and what format the documentation should be in, what "change control documentation" involves for contract variations, and why the $25,000 and $50,000 thresholds are specifically relevant. Standard assumptions for experienced procurement team members. |
| Reasoning texture | M | The specific email address with the instruction "do not send through the general audit inbox — I need to review these before the opening meeting" is Sarah's operational requirement made visible. She is directing the documents to her specific inbox rather than the shared audit inbox because she needs to review them before the team sees them. That pre-review requirement, and the specific instruction it generates, is the trace of an experienced auditor who knows what she needs to prepare for the opening meeting. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The dollar thresholds ($50,000 for procurement approvals, $25,000 for contract variations) are the strongest traces — these are the specific materiality thresholds Sarah has established through three prior audits of this function. A template audit documentation request would not specify these thresholds. Sarah's version reflects her accumulated knowledge of what level of transaction requires supporting documentation in this specific procurement function. |
| Idealisation risks | Risk of making the document requests too generic — losing the threshold specificity. Counteracted by including both the $50,000 and $25,000 thresholds explicitly. |
| Imperfection checklist | PASS. High conviction (experienced auditor, known requirements). Low epistemic humility (prior audit knowledge). Investment asymmetry MEDIUM (three equal requests). Reasoning texture MEDIUM — personal inbox requirement from pre-review need. Human trace: dollar thresholds from three prior audit cycles. |
| Validation gate | PASS |

---

## CB-INT-033

**Context / subtype:** INT — compliance — GDPR data processing audit notification, international regulatory
**Sender role:** Risk and compliance officer — GDPR data processing audit, technical and regulatory audience
**Word count:** 114
**Ground truth:** GENUINE

### Sender profile

Claire, risk and compliance officer. The company processes personal data of EU residents through its European operations. The annual GDPR data processing audit is due — the company's data protection officer has confirmed the audit scope and Claire is notifying the IT and operations teams who manage the relevant data processing systems. The audience is technically literate and familiar with GDPR. The communication is precise.

### Example text

---

**To:** IT Director, Operations Director, Data Engineering Lead
**From:** Claire Whitfield, Risk and Compliance
**Re:** Annual GDPR Data Processing Audit — Scope Confirmation and Documentation Requirements

The annual GDPR data processing audit will be conducted by [External Auditor] from 14–18 April 2026. The audit covers all personal data processing activities within scope of the EU GDPR for the period 1 January to 31 March 2026.

**Documentation required from each team by 7 April 2026:**
- IT: Updated Records of Processing Activities (RoPA) for all systems processing EU personal data; Data Processing Agreements with third-party processors active during the period.
- Operations: Processing logs for the customer data pipeline (Q1 2026); any Data Subject Access Requests received and their resolution.
- Data Engineering: Data lineage documentation for the EU data segment; pseudonymisation controls documentation.

Questions regarding scope to claire.whitfield@company.com or the DPO directly.

Claire Whitfield
Risk and Compliance

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | Firm on all specifics: the audit dates (14–18 April), the period covered (Q1 2026), the documentation deadline (7 April), and the specific documents required from each team. These are confirmed audit parameters. |
| Epistemic humility | L | The documentation requirements are precisely specified — this is not a general request but a specific list derived from the confirmed audit scope. Low epistemic humility appropriate to a compliance professional communicating confirmed audit requirements. |
| Investment asymmetry | M | The three teams receive equal structured attention — all are equally important to the audit. The specific documents required reflect Claire's knowledge of which documents are relevant to each team's processing activities. |
| Blind spots | L | Technical audience — IT Director, Operations Director, Data Engineering Lead. Claire assumes all three know what RoPA, DPAs, data lineage documentation, and pseudonymisation controls are. Low blind spots appropriate for this technically and regulatory-literate audience. |
| Reasoning texture | M | The technical specificity of the documentation requirements — RoPA, DPAs, pseudonymisation controls — reflects Claire's GDPR expertise applied to a specific audit scope. Each item is the right item for each team; the matching of team to document type requires knowledge of what each team does with EU personal data. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The team-to-document matching is the human trace — Claire has matched each team's specific documentation requirements to their specific processing activities. IT gets RoPA and DPAs (because IT manages the processing systems and their third-party agreements), Operations gets processing logs and DSARs (because Operations manages the customer data pipeline and customer requests), and Data Engineering gets data lineage and pseudonymisation documentation (because Data Engineering built and maintains the technical controls). That matching requires knowledge of what each team actually does. |
| Idealisation risks | Risk of making the documentation list too generic — losing the team-specific matching. Counteracted by the specific documents assigned to each team with their specific relevance. |
| Imperfection checklist | PASS. High conviction (confirmed audit scope). Low epistemic humility (technical audience, specific requirements). Investment asymmetry MEDIUM (three equal teams). Reasoning texture MEDIUM — team-to-document matching from GDPR expertise. Human trace: team-specific documentation matching from processing activity knowledge. |
| Validation gate | PASS |

---

## CB-INT-034

**Context / subtype:** INT — compliance — gifts and entertainment register update, regulated employees
**Sender role:** Compliance officer — gifts and entertainment register update requirement, routine but time-sensitive
**Word count:** 97
**Ground truth:** GENUINE

### Sender profile

Michael, compliance officer. The company's gifts and entertainment register must be updated by 31 March (the compliance year end) by all employees in regulated roles who received or gave any gifts or entertainment during Q1. The register is an ASIC regulatory requirement for financial services employees. Michael is sending the quarterly reminder. Most employees will have no entries — only those who did receive or give something need to act.

### Example text

---

**To:** All Regulated Role Employees (87 staff)
**From:** Michael Torres, Compliance
**Re:** Q1 Gifts and Entertainment Register — Update Required by 31 March 2026

All employees in regulated roles are required to update the Gifts and Entertainment Register for Q1 2026 (1 January to 31 March) by 31 March 2026.

**If you gave or received any gift, hospitality, or entertainment during Q1:** Log into the Compliance Portal > Registers > G&E Register and add your entries.

**If you gave or received nothing during Q1:** No action is required. The register will default to nil for your name.

The register is an ASIC regulatory requirement. Incomplete registers are a compliance breach.

Questions to michael.torres@company.com.

Michael Torres
Compliance

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | Firm on the requirement (ASIC regulatory), the deadline (31 March), and the consequence (compliance breach if incomplete). Direct on what action is required and what is not. |
| Epistemic humility | L | "The register will default to nil for your name" — Michael knows the system's default behaviour. Low epistemic humility — the requirement and the system behaviour are known. |
| Investment asymmetry | M | The "if you gave or received nothing — no action required" statement receives equal prominence to the "if you did" instruction — Michael's stake is in the register being accurate, which requires both the entries and the confirmed nil entries. Making the nil case explicit reduces anxiety and reduces unnecessary portal access. |
| Blind spots | M | Assumes the 87 regulated role employees know what the G&E register is, what counts as a registrable gift or entertainment, where the Compliance Portal is, and why ASIC requires this. Standard assumptions for employees who have been through this process before. |
| Reasoning texture | L | The nil-case clarity ("if you gave or received nothing — no action required") is Michael's operational addition. Without it, employees who had nothing to report would either log into the portal unnecessarily or worry that they need to submit a nil return. The explicit nil-case instruction prevents both. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The nil-case clarity is the human trace — Michael has included it because he has managed this register before and knows that the most common employee response to a G&E register reminder is confusion about whether they need to do anything if they have nothing to report. The explicit "no action required" instruction addresses that confusion directly. |
| Idealisation risks | Risk of making the compliance breach consequence too prominent — generating disproportionate anxiety. Counteracted by "Incomplete registers are a compliance breach" as a brief factual statement rather than an elaborated threat. |
| Imperfection checklist | PASS. High conviction (regulatory requirement). Low epistemic humility (known system behaviour). Investment asymmetry MEDIUM (nil case equal prominence). Reasoning texture LOW (appropriate). Human trace: nil-case clarity from knowledge of employee confusion pattern. |
| Validation gate | PASS |

---

## CB-INT-035

**Context / subtype:** INT — compliance — Board Risk Committee update request, board-adjacent register
**Sender role:** Chief Risk Officer — requesting quarterly risk update from function heads for Board Risk Committee
**Word count:** 103
**Ground truth:** GENUINE

### Sender profile

Patricia, Chief Risk Officer. The Board Risk Committee meets on 15 April. Patricia needs updated risk ratings and commentary from each function head by 8 April for inclusion in the Board Risk Committee pack. This is a quarterly process — each function head knows what is required. Patricia's communication is precise and board-register appropriate. The function heads know this material goes to the board.

### Example text

---

**To:** CFO, COO, CTO, CCO, General Counsel
**From:** Patricia Sinclair, Chief Risk Officer
**Re:** Board Risk Committee — Q1 Risk Register Update — Required by 8 April 2026

The Board Risk Committee meets on 15 April 2026. I need updated risk ratings and commentary for each function's top five risks by 8 April.

Please update your section of the risk register in RiskCloud and confirm to me by email once done. Use the Q4 2025 ratings as your baseline — if a risk rating has changed since Q4, please include a brief explanation of the change.

If any new material risks have emerged in your function during Q1 that are not currently on the register, please flag these to me separately before 5 April so I can assess whether they should be added to the board pack.

Patricia Sinclair
Chief Risk Officer

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | Firm on all specifics: the board meeting date (15 April), the update deadline (8 April), the format (top five risks, RiskCloud, Q4 2025 baseline), and the new risk escalation deadline (5 April). These are confirmed board calendar and process requirements. |
| Epistemic humility | M | "If any new material risks have emerged in your function during Q1 that are not currently on the register, please flag these to me separately before 5 April so I can assess whether they should be added to the board pack" — Patricia genuinely does not know whether new material risks have emerged in each function. The 5 April separate deadline for new risks reflects her awareness that the board pack inclusion decision requires her assessment. Medium intensity — the process is clear but the content is uncertain. |
| Investment asymmetry | H | The new material risk escalation pathway receives specific and separate treatment — it has a different deadline (5 April vs 8 April) and a different process (flag to Patricia for assessment vs direct RiskCloud update). Patricia's professional stake is in the board pack being complete; the separate pathway for new risks reflects the additional step required to assess whether they meet the board-pack threshold. |
| Blind spots | L | Senior executive audience (CFO, COO, CTO, CCO, General Counsel). Patricia assumes all five know what RiskCloud is, what their section of the risk register contains, what the Q4 2025 ratings are, and what the Board Risk Committee expects. Low blind spots appropriate for this senior executive audience. |
| Reasoning texture | M | "Use the Q4 2025 ratings as your baseline — if a risk rating has changed since Q4, please include a brief explanation of the change" — Patricia has specified the baseline and the explanation requirement because she knows that uncommented rating changes will generate board questions that she cannot answer. The baseline instruction and the explanation requirement both reflect her knowledge of how the board processes risk rating changes. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The 5 April new risk escalation deadline (earlier than the 8 April main deadline) is the human trace — Patricia has set two separate deadlines because new risks require her personal assessment before they can be included in the board pack, and she needs three days to make that assessment and incorporate the new risks into the pack if required. That two-deadline structure requires knowledge of her own board pack preparation process. |
| Idealisation risks | Risk of making the new risk escalation process too complex — confusing the function heads about what to submit and when. Counteracted by clearly separating "update the register" (8 April) from "flag new risks" (5 April, separately to Patricia). |
| Imperfection checklist | PASS. High conviction (board calendar). Epistemic humility MEDIUM (new risk content unknown). Investment asymmetry HIGH (new risk escalation separate treatment). Low blind spots (senior executive audience). Reasoning texture MEDIUM — baseline and explanation requirement from board question-anticipation. Human trace: two-deadline structure from board pack preparation process knowledge. |
| Validation gate | PASS |

---

## CB-INT-036

**Context / subtype:** INT — operational policy — new procurement process rollout, multiple teams affected
**Sender role:** Operations manager — new procurement process rollout, practical and acknowledges adjustment required
**Word count:** 113
**Ground truth:** GENUINE

### Sender profile

David, operations manager. The company is transitioning from a decentralised procurement model (each team orders what it needs directly) to a centralised procurement model (all orders go through a new procurement team). This affects every team. The change is unpopular with some teams who have had operational autonomy. David's communication is practical and honest about the fact that the change will require adjustment — he is not pretending the new process is easier than the old one for everyone.

### Example text

---

**To:** All Department Heads
**From:** David Osei, Operations Manager
**Re:** Centralised Procurement — Effective 1 April 2026

From 1 April 2026, all procurement requests must be submitted through the new centralised procurement team, using the Procurement Portal.

I'll be honest — for teams that have managed their own ordering, this will require some adjustment. The new process is designed to deliver better pricing and consolidated supplier relationships, but it does add a step. We've tried to make that step as simple as possible.

**To submit a request:** Log into the Procurement Portal and complete the Purchase Request form. Standard requests under $10,000 will be processed within 2 business days. Requests over $10,000 require CFO approval and will take up to 5 business days.

A training session on the Procurement Portal is scheduled for 28 March — calendar invite to follow.

David Osei
Operations Manager

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | Firm on the effective date (1 April 2026), the process requirement (all requests through the Procurement Portal), and the processing timelines (2 business days under $10,000, 5 business days with CFO approval for over $10,000). |
| Epistemic humility | M | "For teams that have managed their own ordering, this will require some adjustment" — David is acknowledging a genuine impact rather than minimising it. He does not know how much adjustment each team will need. The training session is offered because he knows some teams will need help. |
| Investment asymmetry | M | The practical submission process receives equal attention to the honest acknowledgment of adjustment — both are necessary for the communication to be effective. David's stake is in the process being adopted smoothly; the honesty about adjustment serves that goal better than minimisation would. |
| Blind spots | M | Assumes department heads know what "centralised procurement" means operationally, where the Procurement Portal is, and what the CFO approval process involves. The training session partially addresses this. |
| Reasoning texture | H | "I'll be honest — for teams that have managed their own ordering, this will require some adjustment. The new process is designed to deliver better pricing and consolidated supplier relationships, but it does add a step. We've tried to make that step as simple as possible" — this three-sentence construction is David's honest communication of a change that he knows will be unwelcome. He is acknowledging the additional burden, explaining the benefit, and reassuring about the effort to minimise the burden — all in three sentences. The "I'll be honest" framing is unusual in operational change communications and reflects David's decision that honesty about the cost of the change will produce better adoption than minimisation. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. "I'll be honest" is the human trace. This phrase — and the three-sentence construction that follows it — could only be written by someone who has thought about how teams who value their procurement autonomy will receive this change, and has decided that honest acknowledgment of the cost will produce better adoption than institutional boosterism. That reader-awareness, and the "I'll be honest" framing it produced, is the trace of an operations manager who has managed process changes before and knows what works. |
| Idealisation risks | Risk of making the honesty too prominent — suggesting David himself is unhappy with the change. Counteracted by "designed to deliver better pricing and consolidated supplier relationships" — David is supporting the change while being honest about its cost. |
| Imperfection checklist | PASS. High conviction (effective date and process). Epistemic humility MEDIUM (adjustment acknowledged). Investment asymmetry MEDIUM. Reasoning texture HIGH — "I'll be honest" framing from change management experience. Human trace: honest acknowledgment of cost from knowledge of how teams will receive this change. |
| Validation gate | PASS |

---

## CB-INT-037

**Context / subtype:** INT — operational — office relocation logistics, practical and detailed
**Sender role:** Facilities manager — office relocation logistics for affected team
**Word count:** 116
**Ground truth:** GENUINE

### Sender profile

Jennifer, facilities manager. The Finance team is moving from Level 4 to Level 6 over the Easter long weekend (Friday 18 April to Monday 21 April). Jennifer is writing to the Finance team with the practical logistics they need to know before the move. Her communication is detailed and practical — she has managed six office moves in this building and knows what Finance teams typically forget.

### Example text

---

**To:** Finance Team (all members)
**From:** Jennifer Huang, Facilities Manager
**Re:** Finance Team Relocation — Level 4 to Level 6 — Easter Weekend

Your team is relocating from Level 4 to Level 6 over the Easter long weekend (Friday 18 April to Monday 21 April). You will be in your new space when you return to the office on Tuesday 22 April.

**Before you leave on Thursday 17 April:**
- Pack all personal items and desk contents into the boxes IT has left at your workstation. Label with your name and the box number.
- Log off all systems and leave your computer on your desk — IT will handle the hardware.
- Return your Level 4 access card to reception before 5pm Thursday.

**Your new space:** Workstation assignments on Level 6 are attached. The Level 6 kitchen is equipped. The Level 6 server room access codes will be sent separately to those who need them.

Jennifer Huang
Facilities Manager

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | Firm on all logistics: the specific dates, the specific floors, the three pre-move actions, the Tuesday 22 April return. These are confirmed move logistics. |
| Epistemic humility | L | "The Level 6 server room access codes will be sent separately to those who need them" — Jennifer knows the server room access list will be determined separately. Low epistemic humility — the logistics are confirmed. |
| Investment asymmetry | M | The three Thursday pre-move actions receive the most structured attention — these are what Finance team members need to do before the move, and the sequence matters. The new space information is brief because Jennifer has attached the workstation assignments. |
| Blind spots | M | Assumes Finance team members know where reception is on Level 4, where their workstations are currently, that IT has already left boxes at their workstations, and that "log off all systems" includes specific systems they use. Some of these the team will know; some Jennifer has ensured by having IT prepare the boxes in advance. |
| Reasoning texture | M | "Return your Level 4 access card to reception before 5pm Thursday" — Jennifer has included the specific time (5pm) because she has experienced access card returns arriving after security has left for the long weekend, which creates problems with building access management. The 5pm specificity reflects her operational knowledge of how building security works over a long weekend. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. Two shared-context artefacts: the IT boxes at workstations (a specific action IT has already taken that Jennifer knows about because she coordinated it) and the 5pm Thursday access card return deadline (a specific operational requirement from her experience managing long-weekend moves). The IT box preparation is the strongest trace — it requires coordination between Facilities and IT that Jennifer has already completed. |
| Idealisation risks | Risk of making the logistics too generic — losing the specific operational detail. Counteracted by the 5pm Thursday deadline and the IT box reference. |
| Imperfection checklist | PASS. High conviction (confirmed move logistics). Low epistemic humility (logistics confirmed). Investment asymmetry MEDIUM (Thursday pre-move actions). Reasoning texture MEDIUM — 5pm deadline from long-weekend access management experience. Human trace: IT box coordination and 5pm access card deadline. |
| Validation gate | PASS |

---

## CB-INT-038

**Context / subtype:** INT — operational — ERP system migration notification, major system change
**Sender role:** Operations director — ERP migration notification, significant operational impact, technical audience
**Word count:** 121
**Ground truth:** GENUINE

### Sender profile

Sandra, operations director. The company is migrating from SAP ECC to SAP S/4HANA over a six-month program. Go-live is 1 July 2026. Sandra is writing to the operations leadership team — the heads of finance, logistics, procurement, and manufacturing — who will be most affected by the migration. They are operationally sophisticated and will understand the technical implications. Sandra is being honest about the impact and the timeline.

### Example text

---

**To:** Head of Finance, Head of Logistics, Head of Procurement, Head of Manufacturing
**From:** Sandra Webb, Operations Director
**Re:** SAP S/4HANA Migration — Program Update and Key Dates

The SAP S/4HANA migration program is on track for a 1 July 2026 go-live. I want to make sure you have the key dates and what they mean for your teams.

**Key dates:**
- 1 April 2026: Data cleansing phase begins. Each function will receive a data quality report for their domain this week. Review and remediation is due by 30 April.
- 1–30 May: User acceptance testing (UAT). Your team leads will receive UAT scripts from the project team.
- 1–30 June: Parallel running. Both SAP ECC and S/4HANA will be live. This is operationally demanding — please plan for additional team capacity during this period.
- 1 July 2026: Go-live. SAP ECC decommissioned.

The parallel running period is the critical risk window. If your team identifies issues during UAT or parallel running, escalate immediately to the project team — do not wait for the next status meeting.

Sandra Webb
Operations Director

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | Firm on all key dates and their operational implications. "The parallel running period is the critical risk window" — Sandra's professional assessment stated directly. "Escalate immediately — do not wait for the next status meeting" — directive, no hedge. |
| Epistemic humility | M | "This is operationally demanding — please plan for additional team capacity during this period" — Sandra is honest about the parallel running burden without knowing exactly how much additional capacity each team will need. The "please plan for" framing acknowledges that the specific capacity requirement depends on each team's situation. |
| Investment asymmetry | H | The parallel running period receives the most specific attention — the "critical risk window" characterisation, the escalation instruction, and the capacity planning warning. Sandra's professional assessment is that parallel running is where the migration risk lives; her attention reflects that assessment. |
| Blind spots | L | Senior operations leadership audience. Sandra assumes all four know what SAP ECC and S/4HANA are, what data cleansing, UAT, and parallel running involve, and what the project team escalation channel is. Low blind spots appropriate for this technically sophisticated audience. |
| Reasoning texture | M | "Do not wait for the next status meeting" — Sandra is overriding the normal escalation channel (the weekly status meeting) for issues during parallel running. This override reflects her knowledge that status meetings are not frequent enough to catch issues that could derail a go-live, and that the project team needs real-time escalation during the high-risk period. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The "critical risk window" characterisation for parallel running is the human trace — it is Sandra's professional assessment of where the migration risk is concentrated, based on her operational experience with system migrations. A template program update would list the parallel running period as a key date without characterising its risk level. Sandra's version names it as the critical risk window because she has seen migrations fail during parallel running and knows what escalation channels need to be in place. |
| Idealisation risks | Risk of making the risk characterisation too alarming — generating anxiety that disrupts rather than focuses attention. Counteracted by framing the parallel running period as "operationally demanding" (honest) rather than threatening, and giving the specific mitigation (escalate to project team, plan for additional capacity). |
| Imperfection checklist | PASS. High conviction (confirmed program timeline). Epistemic humility MEDIUM (team capacity needs uncertain). Investment asymmetry HIGH (parallel running attention). Low blind spots (operations leadership audience). Reasoning texture MEDIUM — "critical risk window" from migration experience, status meeting override from escalation knowledge. Human trace: parallel running risk characterisation from system migration experience. |
| Validation gate | PASS |

---

## CB-INT-039

**Context / subtype:** INT — operational — process mapping session invitation, collaborative peer request
**Sender role:** Business analyst — process mapping session invitation, peer register, collaborative
**Word count:** 94
**Ground truth:** GENUINE

### Sender profile

Tom, business analyst. He is leading the process mapping workstream for the ERP migration (related to CB-INT-038). He needs to run a two-hour process mapping session with the Finance team's accounts payable sub-team — three people who own the current AP process in SAP ECC. He is writing the session invitation. He is a peer — not a manager — and his register reflects that. He also knows the AP team is busy and is genuinely asking rather than directing.

### Example text

---

Hi Priya, Sarah, and James —

I'm hoping to get the three of you together for a two-hour process mapping session for the SAP migration — specifically the accounts payable process in SAP ECC. I need to capture how the current process works before we can design the S/4HANA equivalent.

I'm flexible on timing but would like to get this done before the end of April (we're targeting May for UAT). Can you let me know your availability for the week of 7 April or 14 April?

I'll send a structured agenda in advance so you're not coming in cold. The session will involve walking through the current end-to-end AP process — I'll need you to do most of the talking.

Tom

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | L | "I'm hoping to" and "Can you let me know your availability" — Tom is asking, not directing. He has no authority over the AP team. Low conviction appropriate to a peer cross-functional request. |
| Epistemic humility | H | "I need you to do most of the talking" — Tom is explicitly acknowledging that the AP team has the knowledge he does not. He is the facilitator; they are the subject matter experts. The session is designed around their knowledge, not his. |
| Investment asymmetry | M | The purpose of the session and the timing requirement receive equal attention. Tom's stake is in completing the process mapping before the UAT deadline; the April preference and the May UAT reference convey that stake without directing. |
| Blind spots | M | Assumes Priya, Sarah, and James know what process mapping involves, what the SAP migration AP process context is, and why capturing the current process is necessary before designing the S/4HANA equivalent. The AP team has been briefed on the migration — these are reasonable assumptions. |
| Reasoning texture | M | "I'll send a structured agenda in advance so you're not coming in cold" — Tom is managing the AP team's experience of the session, anticipating that they might find an open-ended process mapping session uncomfortable. The pre-agenda offer reflects his awareness that structured framing makes subject matter experts more comfortable in facilitated sessions. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. "I'll need you to do most of the talking" is the human trace — Tom is explicitly defining his role (facilitator) and their role (subject matter experts) in a way that reflects his genuine understanding of what process mapping requires. A template session invitation would say "please come prepared to discuss the current AP process." Tom's version specifies the role division because he knows from experience that making the expert role explicit produces better participation. |
| Idealisation risks | Risk of making the peer register too informal — losing the professional context. Counteracted by the specific ERP migration context and the UAT deadline reference. Risk of the collaborative framing being too soft — not conveying the genuine deadline pressure. Counteracted by "we're targeting May for UAT" as the timeline basis. |
| Imperfection checklist | PASS. Low conviction (peer request). Epistemic humility HIGH ("you do most of the talking"). Investment asymmetry MEDIUM. Reasoning texture MEDIUM — pre-agenda offer from facilitation experience. Human trace: facilitator/expert role division from process mapping experience. |
| Validation gate | PASS |

---

## CB-INT-040

**Context / subtype:** INT — operational — end-of-financial-year process, time-pressured, multiple teams
**Sender role:** General manager operations — EOFY process communication, specific and multi-team
**Word count:** 118
**Ground truth:** GENUINE

### Sender profile

James, general manager operations. End of financial year is 30 June. James is writing to the operations leadership team in early April to set expectations for the EOFY process — stock takes, system cutoffs, final invoicing, and the reporting timeline. This is the third EOFY he has managed in this role. He knows which teams tend to be late and has built that knowledge into the communication without calling them out directly.

### Example text

---

**To:** Operations Leadership Team
**From:** James Morrison, General Manager Operations
**Re:** End of Financial Year — Key Dates and Expectations — 30 June 2026

EOFY is 10 weeks away. A few things to get on your radar now so we're not scrambling in June.

**Stock take:** Physical stock take scheduled for 27–28 June. Warehouse team leads, please confirm your counts are reconciled and uploaded by COB 28 June. Last year's count took until 2 July — that is not happening again.

**System cutoff:** All transactions must be processed in SAP before 5pm 30 June. Finance will run the period close at 6pm — anything not in by then misses the year. This is a hard deadline.

**Final invoicing:** All June invoices must be issued by 25 June. Billing team, please do not wait until the last week.

The CFO presentation to the board is 14 July. I need the operations pack from each of you by 7 July.

James Morrison
General Manager Operations

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | Firm on all dates: stock take (27–28 June), system cutoff (5pm 30 June), Finance period close (6pm 30 June), final invoicing (25 June), operations pack deadline (7 July), board presentation (14 July). "This is a hard deadline" on the 5pm 30 June cutoff — no hedge. |
| Epistemic humility | L | James knows all the dates and the process from three years of managing this. "Last year's count took until 2 July — that is not happening again" — James knows the historical pattern and is setting an expectation against it. Low epistemic humility — he knows the process and its failure modes. |
| Investment asymmetry | H | The stock take and system cutoff receive the most emphatic language — these are the two areas where James has seen failures in prior years. "Last year's count took until 2 July — that is not happening again" and "This is a hard deadline" are both James's escalated conviction on the two highest-risk items. |
| Blind spots | M | Assumes the operations leadership team knows what the SAP period close involves, what "reconciled and uploaded" means for the stock count, and what the board presentation timeline requires. Standard assumptions for a team that has been through this process before. |
| Reasoning texture | M | "Last year's count took until 2 July — that is not happening again" — James's reference to a specific prior year failure is the most human element in the batch. It is a direct reference to a known operational failure that this specific team caused and that James is explicitly naming as the standard he will not accept again. Only someone who was present for last year's count — and who was affected by it — would write this sentence. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. "Last year's count took until 2 July — that is not happening again" is the human trace — it is a specific reference to a specific failure in a specific prior year that only someone who managed that EOFY and experienced the impact would include. A template EOFY communication would state the stock take deadline. James's version references the prior failure by implication and states the new expectation against that implicit standard. |
| Idealisation risks | Risk of making the prior failure reference too explicit — creating resentment in the warehouse team leads. Counteracted by keeping "last year's count took until 2 July" as a factual reference rather than a criticism. The "that is not happening again" is James's expectation, not a rebuke. |
| Imperfection checklist | PASS. High conviction on all dates (three-year process knowledge). Low epistemic humility (known process). Investment asymmetry HIGH (stock take and system cutoff emphasis). Reasoning texture MEDIUM — prior year failure reference as operational history trace. Human trace: "last year's count took until 2 July" as specific operational history reference. |
| Validation gate | PASS |

---

*Owlume Pty Ltd — Confidential — corpus_batch7_int_021_040_v1 · 30 March 2026 · Batch review pending*