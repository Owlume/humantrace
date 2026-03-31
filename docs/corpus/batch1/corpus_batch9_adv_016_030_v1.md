# Calibration Corpus — Batch 9, Examples 16–30 (Advisory)

**HumanTrace — Internal Document**
Professional Advisory — Specialist and Consultant · CB-ADV-016 through CB-ADV-030
Ground truth: GENUINE · Path A synthetic genuine construction
Version 1.0 · 30 March 2026 · Owlume Pty Ltd
Constructed under `corpus_construction_protocol_v1.1`

> **Batch construction note:** Specialist advisory communications carry the highest expert confidence register in the corpus. Strong directional recommendations, technical precision, authoritative conclusions. The calibration challenge is that genuine expert deliberation is visible in the reasoning — alternatives considered, complicating facts acknowledged, uncertainty named at the precise point where it exists. Synthetic expert content reaches its conclusion too efficiently. Every example in this batch must contain visible deliberation texture alongside strong expertise. An example that is uniformly confident without visible deliberation is not genuine specialist advisory communication — it is synthetic.

---

## CB-ADV-016

**Context / subtype:** ADV — technical — structural engineering assessment, building defect, remediation urgency judgment
**Sender role:** Structural engineer — building structural assessment, diagnosis confident, remediation urgency a judgment call
**Word count:** 214
**Ground truth:** GENUINE

### Sender profile

James, structural engineer, sixteen years in building assessment. He has been engaged to assess a reported crack in the primary load-bearing wall of a three-storey commercial building. His assessment is clear — the crack is structural, not cosmetic, and requires remediation. The judgment call is urgency: in his assessment the building is safe for continued use while remediation is planned, but he is being careful about how he characterises that assessment because he knows property owners can interpret "safe for now" as "not urgent."

### Example text

---

**STRUCTURAL ASSESSMENT REPORT**
**Property:** [Address]
**Prepared by:** James Thornton, Structural Engineer — Meridian Engineering
**Date:** 18 March 2026

**Executive Summary**

I have assessed the crack reported in the primary load-bearing wall on the northern elevation at level two. My findings and recommendations are as follows.

**Findings — I am confident in these:**
The crack is structural in origin, not cosmetic. It is consistent with differential settlement of the northern footing, likely exacerbated by the dry conditions in 2024. The crack width at its widest point is 4.2mm, and I have identified propagation over the past three months based on comparison with the photographs taken in December 2024. The structural integrity of the wall is compromised and remediation is required.

**Remediation recommendation:**
I recommend underpinning of the northern footing and crack injection with structural epoxy. I estimate the remediation cost at $85,000–$120,000 depending on the contractor and soil conditions encountered during excavation.

**On urgency — this is a judgment call I want to be clear about:**
In my assessment, the building is safe for continued occupancy while remediation is planned, provided the crack is monitored monthly and I am notified of any progression beyond 5mm. This is not a recommendation to delay — I recommend commencing the procurement process immediately. It is a statement that I do not believe evacuation is necessary before remediation begins.

James Thornton
Structural Engineer

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | High conviction on the diagnosis (structural crack, differential settlement, 4.2mm width, propagation over three months documented from December 2024 photographs). "I am confident in these" — explicit label. The remediation recommendation is specific ($85,000–$120,000 range, underpinning and epoxy injection). High conviction appropriate — James has assessed the structure and knows the diagnosis. |
| Epistemic humility | H | "On urgency — this is a judgment call I want to be clear about" — James has explicitly labelled the section where his expert opinion involves a judgment rather than a technical finding. The cost estimate range ($85,000–$120,000) reflects genuine uncertainty about soil conditions and contractor pricing. "I do not believe evacuation is necessary" — James is stating this carefully, distinguishing his professional assessment from a guarantee. |
| Investment asymmetry | H | The urgency section receives the most careful language — James's professional stake is in the property owner not misinterpreting "safe for continued occupancy" as "not urgent." The remediation recommendation itself is stated with full conviction. The urgency clarification receives more words than the diagnosis because the risk of misinterpretation is James's primary concern. |
| Blind spots | M | Assumes the property owner knows what underpinning involves, what crack injection with structural epoxy is and why it is appropriate for this type of crack, and what "differential settlement" means as a cause. James has provided enough context that the recommendation is actionable without full technical understanding. |
| Reasoning texture | H | "This is not a recommendation to delay — I recommend commencing the procurement process immediately. It is a statement that I do not believe evacuation is necessary before remediation begins" — James is explicitly disambiguating his urgency assessment into two separate statements. This dual-statement construction — anticipated misread corrected explicitly — is the trace of an engineer who has seen property owners use "safe for now" as justification for delay, and has structured his advice to pre-empt that interpretation. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. Three specific artefacts: the December 2024 photographs (prior documentation James is using to assess propagation — he has a specific prior dataset), the 4.2mm crack width (a specific measured finding from the site assessment), and the dual-statement urgency disambiguation (James's professional anticipation of how "safe for continued occupancy" will be misread). The December 2024 photographs reference is the strongest trace — it requires James to have a prior site record that he is comparing against his current assessment. |
| Idealisation risks | Risk of the urgency section being too ambiguous — leaving the property owner uncertain about what to do. Counteracted by "I recommend commencing the procurement process immediately" as a clear directive within the urgency section. |
| Imperfection checklist | PASS. High conviction on diagnosis (measured findings). Epistemic humility HIGH (judgment call explicit, cost estimate range). Investment asymmetry HIGH (urgency section). Blind spots MEDIUM. Reasoning texture HIGH — dual-statement disambiguation from misread anticipation. Human trace: December 2024 photographs and 4.2mm measured finding. |
| Validation gate | PASS |

---

## CB-ADV-017

**Context / subtype:** ADV — technical — IT architecture, cloud migration strategy, architecture confident, timeline uncertain
**Sender role:** IT architect — cloud migration recommendation, architecture confident, timeline depends on client capacity
**Word count:** 207
**Ground truth:** GENUINE

### Sender profile

Sandra, IT architect, twelve years in enterprise cloud architecture. She is writing to the CTO of a financial services company following a four-week architecture assessment. Her recommendation — migrate to AWS using a phased lift-and-shift approach — is technically sound and she is confident in it. The timeline is the genuine uncertainty: it depends on the client's internal IT team capacity, which she has assessed as limited, and on the regulatory approval requirements for data migration in a financial services context, which she has not fully worked through.

### Example text

---

Dear Mr Osei,

Following our four-week architecture assessment, I am writing with my migration strategy recommendation.

**The technical recommendation — I am confident in this:**
I recommend a phased AWS migration using a lift-and-shift approach for the legacy applications, followed by re-architecting of the core banking application in phase two. This approach minimises migration risk by preserving application functionality during the transition and allows the team to build AWS operational capability progressively. The target architecture is well-suited to your current and anticipated workload profile.

**The timeline — I am significantly less certain:**
The standard timeline for a migration of this scale is 12–18 months. My concern is that your internal IT team's capacity — based on our assessment, two engineers are currently available for migration work — is unlikely to be sufficient for the standard timeline without either additional resourcing or contractor support. I am also not certain how long APRA's data migration notification requirements will take to satisfy — I have not worked through this in detail and recommend engaging your compliance team before committing to a timeline.

**My recommendation on next steps:**
Confirm the IT resourcing position and engage your compliance team on the APRA requirements before setting a go-live date. I can support you through both of those conversations.

Yours sincerely,
Sandra Webb
IT Architect

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | M | High conviction on the technical architecture (AWS, lift-and-shift for legacy, re-architect for core banking, phased approach). "I am confident in this" — explicit label. Explicitly less certain on timeline: "I am significantly less certain" — explicit label with the "significantly" qualifier reflecting her genuine concern about the resourcing gap. |
| Epistemic humility | H | "I am also not certain how long APRA's data migration notification requirements will take to satisfy — I have not worked through this in detail" — Sandra is being specifically honest about what she has and has not assessed. The "have not worked through this in detail" is a direct acknowledgment of an analytical gap in her work, which is unusual in an advisory report. |
| Investment asymmetry | H | The timeline section receives more specific attention than the technical recommendation — because the timeline is where the real uncertainty and client risk live. The specific finding about IT resourcing (two engineers available) is precise. Sandra's professional stake is in the client not committing to a timeline before the resourcing and regulatory questions are resolved. |
| Blind spots | M | Assumes the CTO knows what lift-and-shift vs re-architecting means in cloud migration terms, what APRA's data migration notification requirements involve, and why two engineers is insufficient for the standard 12–18 month timeline. Sandra has provided enough context that the key risk is clear. |
| Reasoning texture | H | "I have not worked through this in detail and recommend engaging your compliance team before committing to a timeline" — Sandra is explicitly acknowledging an analytical gap and routing it to the appropriate expert. This double move — admitting the gap and identifying who can fill it — is the trace of an IT architect who knows the boundary of her expertise and is willing to name it rather than making assumptions she cannot support. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. Two specific artefacts: the two-engineer capacity finding (a specific finding from Sandra's internal IT team assessment) and the "I have not worked through this in detail" APRA acknowledgment (a specific gap in her assessment that she is naming rather than glossing). The two-engineer finding is the strongest trace — it is a specific operational assessment of the client's internal capacity that requires Sandra to have spoken with or reviewed the IT team structure. |
| Idealisation risks | Risk of making the APRA gap acknowledgment undermine confidence in the technical recommendation. Counteracted by keeping the technical recommendation section entirely confident before the timeline uncertainty section. The gap is in the regulatory/timeline domain, not the technical domain. |
| Imperfection checklist | PASS. Medium conviction (technical confident, timeline uncertain). Epistemic humility HIGH (APRA gap acknowledged explicitly). Investment asymmetry HIGH (timeline section). Blind spots MEDIUM. Reasoning texture HIGH — analytical gap named and routed to appropriate expert. Human trace: two-engineer capacity finding and APRA gap acknowledgment. |
| Validation gate | PASS |

---

## CB-ADV-018

**Context / subtype:** ADV — technical — environmental assessment, contamination documented, remediation pathway regulatory uncertainty
**Sender role:** Environmental consultant — contamination assessment confident, remediation pathway has regulatory uncertainty
**Word count:** 208
**Ground truth:** GENUINE

### Sender profile

Rachel, environmental consultant, nine years in contaminated land assessment. She has completed a Phase 2 Environmental Site Assessment of a former industrial site. The contamination findings are clear — elevated petroleum hydrocarbons in the soil and groundwater. The remediation recommendation is technically sound. The genuine uncertainty is the regulatory pathway: the site falls under a shared jurisdiction between the EPA and the local council, and the remediation approval process has not been clearly defined. Rachel is honest about this regulatory uncertainty while being confident on the technical findings.

### Example text

---

**PHASE 2 ENVIRONMENTAL SITE ASSESSMENT — SUMMARY OF FINDINGS AND RECOMMENDATIONS**
**Site:** [Address]
**Prepared by:** Rachel Osei, Environmental Consultant — Meridian Environmental
**Date:** 19 March 2026

**Contamination findings — these are documented:**
Phase 2 assessment has confirmed elevated total petroleum hydrocarbons (TPH) in soil samples at depths of 0.5–2.0m across the western portion of the site (refer to Figure 3). Groundwater samples from MW-4 and MW-7 also show TPH concentrations exceeding the EPA's adopted assessment criteria. The contamination is consistent with the site's former use as a fuel storage facility.

**Remediation recommendation:**
I recommend a bioremediation approach for the soil contamination, supplemented by groundwater monitoring for a minimum of 12 months. Bioremediation is the most cost-effective approach for this contamination type and concentrations. I estimate remediation cost at $180,000–$240,000 over the monitoring period.

**The regulatory approval pathway — genuine uncertainty:**
This site sits within a shared jurisdiction between the NSW EPA and Penrith Council. I have consulted with both agencies informally. The EPA's current position is that the remediation action plan requires their approval; Penrith Council believes the site falls within council jurisdiction. This jurisdictional question has not been resolved. I recommend engaging a specialist environmental lawyer to navigate the approval pathway before commencing remediation.

Rachel Osei
Environmental Consultant

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | High conviction on contamination findings (specific monitoring well references MW-4 and MW-7, specific depth range 0.5–2.0m, specific regulatory exceedance against EPA criteria). "These are documented" — explicit label. The bioremediation recommendation is stated with professional confidence. |
| Epistemic humility | H | "Genuine uncertainty" as an explicit label for the regulatory pathway section. "This jurisdictional question has not been resolved" — Rachel is being precise about what she knows (both agencies' current positions) and what she does not know (which jurisdiction will prevail). The referral to a specialist environmental lawyer is Rachel's honest acknowledgment that this question is outside her expertise. |
| Investment asymmetry | H | The regulatory pathway section receives the most careful language — Rachel's professional stake is in the client not commencing remediation before the jurisdictional question is resolved, which could lead to regulatory enforcement action. The contamination findings are stated clearly and the technical recommendation is confident. |
| Blind spots | M | Assumes the client knows what bioremediation involves, what monitoring wells are and why MW-4 and MW-7 specifically are relevant, and what a remediation action plan (RAP) is in the regulatory context. Rachel has provided enough technical explanation that the key finding and recommendation are accessible. |
| Reasoning texture | M | "I have consulted with both agencies informally" — Rachel is disclosing her preliminary regulatory engagement and being honest that it produced a jurisdictional conflict rather than a clear pathway. This disclosure of the conflict — rather than pretending the regulatory pathway is clear — is the trace of an environmental consultant who has done the work and is reporting the actual findings, including inconvenient ones. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. Three specific artefacts: MW-4 and MW-7 monitoring wells (specific named monitoring locations from the Phase 2 assessment), the informal agency consultations (Rachel has already spoken to both agencies and is reporting their conflicting positions), and the Penrith Council jurisdictional claim (a specific regulatory finding that Rachel has discovered through her agency consultations). The monitoring well references are the strongest trace — they are specific site infrastructure that only an environmental consultant who has conducted the Phase 2 assessment would know. |
| Idealisation risks | Risk of making the regulatory uncertainty section too alarming — suggesting the remediation cannot proceed. Counteracted by the specific referral recommendation (specialist environmental lawyer) which provides a clear next step rather than leaving the client in uncertainty. |
| Imperfection checklist | PASS. High conviction on contamination findings. Epistemic humility HIGH (jurisdictional conflict acknowledged, specialist referral). Investment asymmetry HIGH (regulatory pathway section). Blind spots MEDIUM. Reasoning texture MEDIUM — informal agency consultation disclosed. Human trace: monitoring well references and conflicting agency positions. |
| Validation gate | PASS |

---

## CB-ADV-019

**Context / subtype:** ADV — technical — civil engineering, infrastructure design recommendation, cost estimate uncertainty
**Sender role:** Civil engineer — infrastructure design recommendation, technical confident, cost estimate range genuine
**Word count:** 196
**Ground truth:** GENUINE

### Sender profile

Thomas, civil engineer, fourteen years in infrastructure design. He is writing to Parramatta City Council following a technical assessment of the proposed pedestrian bridge across the creek at [location]. His design recommendation is technically sound and he is confident in it. The cost estimate range is genuine — it depends on geotechnical conditions that have not been fully investigated and on steel pricing that is currently volatile.

### Example text

---

Dear Ms Chen,

Following our technical assessment of the proposed pedestrian bridge at [Location], I am writing with my design recommendation.

**Design recommendation — I am confident in this:**
I recommend a single-span composite steel and concrete bridge of 28 metres, supported on bored pier foundations. This design is appropriate for the site conditions assessed to date, the pedestrian loading requirements, and the council's aesthetic preference for a low-profile structure. The span can be prefabricated off-site, which will minimise disruption to the creek corridor during construction.

**Cost estimate — this range is genuine:**
I estimate the project cost at $1.4M–$2.1M. This is a wider range than I would normally present, and I want to explain why. The lower bound assumes standard geotechnical conditions for the pier foundations — if the underlying geology is more complex than the desktop assessment suggests, the foundation costs will be higher. The upper bound also reflects current steel pricing volatility. I recommend a geotechnical investigation before finalising the cost estimate and before council proceeds to detailed design.

Yours sincerely,
Thomas Bradley
Civil Engineer

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | Firm on the design specification (single-span, 28 metres, composite steel and concrete, bored pier foundations, off-site prefabrication). "I am confident in this" — explicit label. Technical design recommendation is stated with full professional confidence. |
| Epistemic humility | H | "This range is genuine" — Thomas has explicitly labelled his cost estimate section with a qualifier that acknowledges the width of the range is real uncertainty, not conservatism. "This is a wider range than I would normally present, and I want to explain why" — Thomas is pre-empting the council's question about why the range is so wide, and providing an honest explanation. The two specific drivers (geotechnical uncertainty, steel pricing volatility) are genuine. |
| Investment asymmetry | H | The cost estimate explanation receives more space than the design recommendation — because the cost estimate is where the council will have the most questions and where the risk of misinterpretation is highest. Thomas's professional stake is in the council understanding why the range is wide, not just seeing the range. |
| Blind spots | M | Assumes the council knows what bored pier foundations are, what a desktop geotechnical assessment involves versus a full investigation, and why steel pricing volatility specifically affects this project. Thomas has provided enough explanation for the council to understand the recommendation and the key risk. |
| Reasoning texture | M | "This is a wider range than I would normally present, and I want to explain why" — Thomas is acknowledging that his cost estimate is unusual by his own standards and providing the reasoning. This self-referential observation — comparing his current estimate to his normal practice — is the trace of an engineer who has thought about how the council will receive the wide range and has decided that transparency about why it is wide is more honest than presenting it without explanation. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. Two specific artefacts: the 28-metre span specification (a specific design parameter derived from Thomas's assessment of the site conditions and loading requirements) and the self-referential range observation ("wider than I would normally present"). The 28-metre specification is the strongest trace — it is a precise technical parameter derived from Thomas's site assessment and loading calculations. The self-referential observation is also a trace — it requires Thomas to compare this estimate to his professional norms, which requires genuine professional experience. |
| Idealisation risks | Risk of making the cost estimate section seem like a failure to deliver — the council wants a number, not a range explanation. Counteracted by the specific geotechnical investigation recommendation, which provides a clear path to a more precise estimate. |
| Imperfection checklist | PASS. High conviction on design (assessed site conditions). Epistemic humility HIGH ("this range is genuine" explicit, two specific drivers). Investment asymmetry HIGH (cost estimate explanation). Blind spots MEDIUM. Reasoning texture MEDIUM — self-referential range observation. Human trace: 28-metre specification and self-referential range observation. |
| Validation gate | PASS |

---

## CB-ADV-020

**Context / subtype:** ADV — technical — building inspection report, findings documented, significance buyer-dependent
**Sender role:** Building consultant — pre-purchase inspection, findings clear, significance depends on buyer's intended use
**Word count:** 197
**Ground truth:** GENUINE

### Sender profile

Claire, building consultant, eleven years in pre-purchase building inspections. She has completed a pre-purchase inspection of a 1960s residential property. The findings are documented — there are several items of concern, including a cracked roof tile, a rising damp issue in the southern wall, and some minor subfloor ventilation deficiencies. None of these are structurally significant. The significance of these findings, however, depends on what the buyer intends to do with the property — a buyer planning a major renovation will have different concerns from a buy-and-hold investor.

### Example text

---

**PRE-PURCHASE BUILDING INSPECTION REPORT**
**Property:** [Address]
**Prepared for:** [Buyer Name]
**Inspected by:** Claire Whitfield, Building Consultant — Meridian Building
**Date:** 18 March 2026

**Summary of findings:**
The property is a 1960s brick veneer construction in generally good structural condition. The following items require attention:

1. **Roof:** Two cracked tiles on the northern elevation. Minor repair recommended. Estimated cost: $200–$400.
2. **Southern wall:** Rising damp visible at the base of the southern external wall, consistent with failed damp course. Remediation recommended. Estimated cost: $2,500–$4,000 depending on the extent of the damp course failure.
3. **Subfloor:** Ventilation is below current standard but does not pose an immediate structural risk. Upgrading is recommended for long-term timber preservation.

**On the significance of these findings:**
None of these findings are structurally significant. However, their significance to your purchase decision depends on your intended use. If you are planning a major renovation, the rising damp will need to be addressed in any case and the subfloor ventilation can be included in the broader works. If you are purchasing as a long-term investment property, I would prioritise the damp course remediation before tenanting.

Claire Whitfield
Building Consultant

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | Firm on all findings (specific items, specific cost estimates). "None of these findings are structurally significant" — stated with professional confidence. The three findings are documented and clearly described. |
| Epistemic humility | M | "Their significance to your purchase decision depends on your intended use" — Claire is acknowledging that the same findings carry different weight depending on buyer intent, which she does not know fully. The two different buyer scenarios (renovation vs investment) reflect Claire's awareness that her findings need to be interpreted against the buyer's context. |
| Investment asymmetry | M | The rising damp finding receives the most specific cost range and the most prominence in the significance section — this is the highest-cost item and the one most likely to affect the purchase decision. The roof tiles are brief and low-cost. The subfloor ventilation is intermediate. |
| Blind spots | M | Assumes the buyer knows what rising damp is and what a damp course involves, what subfloor ventilation deficiencies mean for timber preservation, and what brick veneer construction is. These are common building terms but not universally understood. |
| Reasoning texture | M | "If you are purchasing as a long-term investment property, I would prioritise the damp course remediation before tenanting" — Claire is giving specific advice within a specific buyer scenario. This scenario-specific recommendation is Claire's professional judgment about what each type of buyer should prioritise, which requires her to have thought about the buyer's situation beyond just documenting the findings. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The buyer-intent interpretation section is the human trace. Claire has gone beyond documenting the findings (which a standard inspection report does) to interpret their significance against two different buyer scenarios. That interpretation requires Claire to know enough about the buyer's context to frame two plausible scenarios — which she knows from the engagement context (renovation buyer vs investment buyer are the two most common buyer profiles for a 1960s property of this type). |
| Idealisation risks | Risk of the significance section being too binary — real buyers are more nuanced than two scenarios. Counteracted by the section header: "their significance to your purchase decision depends on your intended use" — which opens the question rather than assuming the buyer fits one of the two scenarios. |
| Imperfection checklist | PASS. High conviction on findings (documented inspection). Epistemic humility MEDIUM (buyer intent unknown, scenarios offered). Investment asymmetry MEDIUM (rising damp prominence). Blind spots MEDIUM. Reasoning texture MEDIUM — scenario-specific recommendations. Human trace: buyer-intent interpretation from professional knowledge of buyer profiles. |
| Validation gate | PASS |

---

## CB-ADV-021

**Context / subtype:** ADV — medical — cardiologist assessment to GP, clinical findings confident, management conditional
**Sender role:** Cardiologist — specialist assessment letter, clinical findings confident, management recommendation conditional
**Word count:** 204
**Ground truth:** GENUINE

### Sender profile

Dr Margaret Sinclair, cardiologist, twenty years in clinical cardiology. She is writing to Dr Chen (GP) following a review of Mr Okafor, a 58-year-old patient referred with exertional chest pain. Her clinical assessment is clear — the history and ECG changes are consistent with stable angina. Her management recommendation is conditional on the results of a stress echo she has ordered but not yet received. She is writing now because the GP needs to know the current assessment and management plan while the investigation is pending.

### Example text

---

Dear Dr Chen,

Thank you for referring Mr Okafor for assessment of exertional chest pain.

**Clinical assessment:**
Mr Okafor presents with a three-month history of exertional chest pain, relieved by rest, with no pain at rest. His resting ECG shows non-specific ST changes in the inferior leads. His risk factor profile includes hypertension (on treatment), a 20 pack-year smoking history (ceased 2018), and a family history of ischaemic heart disease. This presentation is consistent with stable angina.

**Investigations:**
I have ordered a stress echocardiogram, which is scheduled for 28 March 2026. I have also commenced Mr Okafor on sublingual GTN for symptomatic relief.

**Management pending investigation:**
My management recommendation depends on the stress echo findings. If the stress echo demonstrates significant ischaemia, I will recommend coronary angiography with a view to revascularisation. If the stress echo is negative or mildly positive, I will manage medically with optimised antianginal therapy.

Mr Okafor has been counselled to present to the emergency department if his symptoms change in character, increase in frequency, or occur at rest.

I will write again following the stress echo results.

Yours sincerely,
Dr Margaret Sinclair
Cardiologist

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | Firm on the clinical assessment (specific symptom history, specific ECG finding, specific risk factor profile, "consistent with stable angina" — the diagnostic conclusion). The GTN prescription is stated as a clinical action taken. High conviction appropriate to a cardiologist with a clear clinical picture. |
| Epistemic humility | H | "My management recommendation depends on the stress echo findings" — Margaret is explicitly making her management plan conditional on pending investigation. The two conditional pathways (significant ischaemia → angiography; negative/mildly positive → medical management) reflect genuine clinical uncertainty — she does not know which pathway applies until the stress echo is done. |
| Investment asymmetry | H | The management pending investigation section receives the most structured clinical attention — both pathways are specified. The clinical assessment is stated efficiently because Margaret is writing to a GP who will understand the clinical language. Margaret's professional stake is in the GP understanding what is being investigated and what the two possible outcomes mean for management. |
| Blind spots | L | Writing to a GP — Dr Chen will understand all clinical terminology. Low blind spots appropriate for a clinician-to-clinician communication. |
| Reasoning texture | M | "Mr Okafor has been counselled to present to the emergency department if his symptoms change in character, increase in frequency, or occur at rest" — Margaret has included this because she knows stable angina can become unstable, and the GP needs to know that the patient has been given specific warning signs. This clinical safety-netting instruction, and its specific triggers (change in character, increase in frequency, rest pain), is the trace of a cardiologist who has thought about the clinical risk during the investigation period. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. Three specific clinical artefacts: the 28 March stress echo date (a specific booked investigation), the 2018 smoking cessation date (a specific patient history detail from the consultation), and the specific ED presentation triggers (change in character, increase in frequency, rest pain — the three warning signs of unstable angina that Margaret has specifically counselled the patient about). The 2018 cessation date is the strongest trace — it is a specific historical detail from the patient's social history that only a clinician who has taken that history would know. |
| Idealisation risks | Risk of the letter being too clinical — losing the GP communication register. Counteracted by "I will write again following the stress echo results" — a clear communication commitment that serves the GP's ongoing care of the patient. |
| Imperfection checklist | PASS. High conviction on clinical assessment (specific findings). Epistemic humility HIGH (management explicitly conditional on pending investigation). Investment asymmetry HIGH (management pending investigation section). Low blind spots (clinician audience). Reasoning texture MEDIUM — clinical safety-netting as patient risk management trace. Human trace: 28 March stress echo date, 2018 smoking cessation, specific ED triggers. |
| Validation gate | PASS |

---

## CB-ADV-022

**Context / subtype:** ADV — medical — orthopaedic surgeon pre-operative assessment, surgical recommendation clear, risks disclosed honestly
**Sender role:** Orthopaedic surgeon — pre-operative assessment, clear surgical recommendation, risks stated with genuine probability acknowledgment
**Word count:** 198
**Ground truth:** GENUINE

### Sender profile

Dr Thomas Bradley, orthopaedic surgeon, eighteen years in joint replacement surgery. He has reviewed Mrs Anderson, a 67-year-old patient with severe right knee osteoarthritis. The surgical recommendation — total knee replacement — is clear. His pre-operative assessment is complete. The risk disclosure is genuine — he is not reciting a standard consent list; he is identifying the risks that are specifically relevant to Mrs Anderson's profile (her BMI of 34 increases wound healing risk, her anticoagulation history requires specific perioperative management).

### Example text

---

**PRE-OPERATIVE ASSESSMENT — TOTAL KNEE REPLACEMENT**
**Patient:** Mrs Elizabeth Anderson, DOB [date]
**Surgeon:** Dr Thomas Bradley, Orthopaedic Surgeon
**Date:** 19 March 2026

**Surgical recommendation:**
I recommend proceeding with total right knee replacement. Mrs Anderson's radiological findings show severe tricompartmental osteoarthritis with complete loss of joint space medially. Conservative management has been optimised — she has had two corticosteroid injections in the past 18 months with diminishing benefit. Surgical intervention is appropriate.

**Patient-specific risks I want to address specifically:**
The standard surgical risks (infection, DVT, PE, neurovascular injury) apply and have been discussed with Mrs Anderson. I want to address two risks that are specifically relevant to her profile.

First, wound healing: Mrs Anderson's BMI of 34 increases the risk of wound complications, including superficial wound breakdown and deep infection. I have discussed this with her and she understands and accepts this additional risk.

Second, anticoagulation management: Mrs Anderson is on warfarin for atrial fibrillation. We will need to bridge with low molecular weight heparin perioperatively, which requires careful coordination with her cardiologist, Dr Chen.

The surgery is scheduled for 8 April 2026 subject to medical clearance from Dr Chen.

Dr Thomas Bradley
Orthopaedic Surgeon

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | Firm on the surgical recommendation (specific radiological finding — severe tricompartmental osteoarthritis, complete medial joint space loss, two prior injections with diminishing benefit). "Surgical intervention is appropriate" — professional conclusion stated with full confidence. |
| Epistemic humility | M | "Subject to medical clearance from Dr Chen" — the surgery is conditional on the cardiologist's clearance, which Thomas does not control. The perioperative anticoagulation management requires coordination with Dr Chen, whose opinion Thomas does not yet have. Medium intensity — Thomas is confident in the surgical decision; the uncertainty is in the perioperative medical management. |
| Investment asymmetry | H | The two patient-specific risks receive the most specific attention — BMI wound risk and anticoagulation management. Thomas's stake is in the patient understanding the specific risks relevant to her profile, not the generic risk list. The generic risks are acknowledged briefly. |
| Blind spots | L | Pre-operative assessment for medical record and patient communication — Thomas assumes the referring clinical team understands the terminology. Low blind spots appropriate for a clinical document. |
| Reasoning texture | M | "I want to address two risks that are specifically relevant to her profile" — Thomas is explicitly distinguishing his patient-specific risk discussion from the standard consent list. This framing — which categorises the following content as personalised, not generic — is the trace of a surgeon who has thought about what information is genuinely specific to this patient versus what is standard practice. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. Three patient-specific artefacts: BMI of 34 (a specific measured finding from the assessment), the two prior corticosteroid injections in 18 months (a specific treatment history that establishes the failure of conservative management), and the warfarin/AF perioperative bridging requirement (a specific medication and indication that requires careful management). The corticosteroid injection history is the strongest trace — it is a specific temporal record ("two in the past 18 months with diminishing benefit") that establishes the treatment pathway Thomas has assessed before recommending surgery. |
| Idealisation risks | Risk of the patient-specific risk section seeming alarmist — the two highlighted risks could make the patient anxious about the surgery. Counteracted by "she understands and accepts this additional risk" — Thomas has already had the risk conversation with Mrs Anderson, and the document is recording that conversation, not presenting it for the first time. |
| Imperfection checklist | PASS. High conviction on surgical indication (specific radiological findings). Epistemic humility MEDIUM (medical clearance conditional on cardiologist). Investment asymmetry HIGH (patient-specific risks). Low blind spots (clinical document). Reasoning texture MEDIUM — patient-specific risk framing. Human trace: BMI, injection history, and anticoagulation profile as patient-specific clinical artefacts. |
| Validation gate | PASS |

---

## CB-ADV-023

**Context / subtype:** ADV — medical — psychiatrist assessment letter to GP, provisional diagnosis, directional treatment
**Sender role:** Psychiatrist — assessment letter, diagnosis provisional, treatment directional pending more information
**Word count:** 207
**Ground truth:** GENUINE

### Sender profile

Dr Jennifer Huang, psychiatrist, fifteen years in general psychiatry. She is writing to Dr Osei (GP) following an initial consultation with Ms Torres, a 34-year-old patient presenting with low mood, sleep disturbance, and reduced motivation for approximately eight months. Her clinical impression is consistent with a depressive episode, but she wants to rule out a thyroid abnormality and assess whether there is a contributing anxiety component before confirming the diagnosis and treatment plan. She is being honest about the provisional nature of her assessment.

### Example text

---

Dear Dr Osei,

Thank you for referring Ms Torres for psychiatric assessment.

**Clinical presentation:**
Ms Torres presents with an eight-month history of low mood, early morning wakening, reduced motivation, and social withdrawal. She reports no suicidal ideation currently. Psychomotor retardation is not prominent. There is a family history of depression (mother, treated with antidepressants).

**Clinical impression — this is provisional:**
My working diagnosis is a depressive episode of moderate severity. However, I want to clarify two things before confirming this diagnosis: first, could you arrange thyroid function tests if not recently done — hypothyroidism can present with a similar clinical picture and I want to exclude this; and second, I am uncertain whether there is a significant anxiety component that is contributing to or driving the presentation. This will become clearer over subsequent sessions.

**Management:**
I have commenced Ms Torres on sertraline 50mg and will titrate to 100mg in two weeks if tolerated. I have also scheduled fortnightly sessions to monitor response and assess the anxiety component further. I will review the diagnosis once the thyroid results are available and after two to three further sessions.

I will write again in four weeks with an updated assessment.

Yours sincerely,
Dr Jennifer Huang
Psychiatrist

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | M | Confident on the clinical presentation (specific symptom history, eight-month duration, family history) and on the treatment initiation (sertraline 50mg, specific titration plan). Explicitly provisional on the diagnosis: "this is provisional" — explicit label. The two clarification requests (thyroid function, anxiety component) reflect genuine diagnostic uncertainty. |
| Epistemic humility | H | "This is provisional" as an explicit label for the clinical impression section. "I am uncertain whether there is a significant anxiety component" — Jennifer is explicitly naming a diagnostic question that further sessions will resolve. "This will become clearer over subsequent sessions" — honest acknowledgment that the clinical picture is not yet complete. |
| Investment asymmetry | M | The two clarification requests receive specific attention — these are the diagnostic questions Jennifer needs answered before confirming the diagnosis. The treatment initiation is stated clearly. Jennifer's stake is in the GP understanding that the diagnosis is working, not confirmed, and that specific further information is needed. |
| Blind spots | L | Writing to a GP — Dr Osei will understand all clinical terminology including psychomotor retardation, sertraline, and the diagnostic reasoning. Low blind spots appropriate for clinician-to-clinician communication. |
| Reasoning texture | M | "Hypothyroidism can present with a similar clinical picture and I want to exclude this" — Jennifer is explaining her diagnostic reasoning for the thyroid function request, which is not strictly necessary in a letter to a GP but reflects her clinical transparency. She is not just requesting the test; she is explaining why, which gives the GP the information needed to prioritise the investigation appropriately. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. Two specific clinical artefacts: the family history of depression (mother, treated with antidepressants — a specific family history detail from the consultation) and the sertraline titration plan (50mg with a specific two-week review for titration to 100mg — Jennifer's specific clinical decision, not a generic SSRI prescription). The family history detail is the strongest trace — it is a specific datum from the clinical interview that only a clinician who has taken that history would know. |
| Idealisation risks | Risk of the provisional diagnosis section creating clinical uncertainty that the GP finds unhelpful. Counteracted by the specific management plan — Jennifer has initiated treatment even while the diagnosis is provisional, which demonstrates clinical confidence in the working diagnosis while being honest about its provisional status. |
| Imperfection checklist | PASS. Medium conviction (working diagnosis, explicit provisional label). Epistemic humility HIGH ("this is provisional", anxiety uncertainty, thyroid exclusion). Investment asymmetry MEDIUM (two clarification requests). Low blind spots (clinician audience). Reasoning texture MEDIUM — diagnostic reasoning explained for thyroid request. Human trace: family history detail and specific sertraline titration plan. |
| Validation gate | PASS |

---

## CB-ADV-024

**Context / subtype:** ADV — medical — oncologist treatment recommendation, clinical recommendation clear, prognosis honest
**Sender role:** Oncologist — treatment recommendation after diagnosis, clinical recommendation clear, prognosis stated honestly
**Word count:** 211
**Ground truth:** GENUINE

### Sender profile

Dr Andrew Marsden, oncologist, twenty-two years in gastrointestinal oncology. He is writing to his patient, Mr Kowalski, and his treating team following the diagnosis of stage III colorectal cancer. The treatment recommendation — combined chemotherapy and radiotherapy followed by surgical resection — is the standard of care and Andrew is confident in it for this patient. The prognosis is the genuine uncertainty, and Andrew is committed to being honest with his patient about what is known and what is not, rather than offering false reassurance.

### Example text

---

Dear Mr Kowalski,

I am writing to confirm the treatment plan we discussed at our appointment on 17 March 2026 and to make sure you have a written record of what we talked about.

**Your diagnosis:**
You have been diagnosed with stage III colorectal cancer (T3N1M0). This means the cancer has grown through the wall of the bowel and has spread to nearby lymph nodes, but there is no evidence of spread to other organs.

**The treatment plan I recommend:**
I recommend a combined approach: neoadjuvant chemoradiation (chemotherapy combined with radiotherapy) for six weeks, followed by surgical resection approximately eight weeks after completing chemoradiation, followed by adjuvant chemotherapy for six months. This is the standard treatment for your stage of cancer and it gives you the best chance of a good outcome.

**What I can and cannot tell you about prognosis:**
For stage III colorectal cancer treated with this approach, the five-year survival rate is approximately 40–60%, depending on how well the tumour responds to the initial chemoradiation. I want to be honest with you about this range — I cannot tell you where you will fall within it, and I also want you to know that these statistics reflect population averages, and individual outcomes can and do vary. We will assess the tumour response after chemoradiation, which will give us more information.

Yours sincerely,
Dr Andrew Marsden
Oncologist

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | Firm on the treatment recommendation (neoadjuvant chemoradiation, surgical resection timing, adjuvant chemotherapy duration). "This is the standard treatment for your stage of cancer and it gives you the best chance of a good outcome" — Andrew's professional conviction on the treatment approach is appropriately strong. Firm on the staging (T3N1M0 — specific pathological staging). |
| Epistemic humility | H | "What I can and cannot tell you about prognosis" — Andrew has explicitly structured the most difficult section of the letter around what he knows and does not know. "I cannot tell you where you will fall within it" — direct epistemic limit statement in a patient communication. "These statistics reflect population averages, and individual outcomes can and do vary" — Andrew is being honest about the limits of prognostic statistics while not withdrawing the information. |
| Investment asymmetry | H | The prognosis section receives the most careful language — Andrew's professional stake is in his patient having honest information about what to expect, not false reassurance. The treatment plan is stated efficiently because it is the standard of care and Andrew has discussed it with the patient already. |
| Blind spots | L | Writing directly to the patient — Andrew has used plain language throughout: "grown through the wall of the bowel", "nearby lymph nodes", "spread to other organs." Low blind spots — Andrew has made a deliberate effort to make the clinical information accessible. |
| Reasoning texture | H | "I also want you to know that these statistics reflect population averages, and individual outcomes can and do vary" — Andrew is contextualising the 40–60% range in a way that gives the patient a realistic but not deterministic understanding of the statistic. This contextualisation — explaining what population statistics mean for individual outcomes — is the trace of an oncologist who has had this conversation many times and knows that patients often interpret population statistics as personal predictions. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. Three specific artefacts: the T3N1M0 staging (precise pathological staging from the diagnostic workup), the 17 March appointment reference (the specific consultation Andrew is confirming in writing), and the "cannot tell you where you will fall within it" epistemic limit statement (Andrew's deliberate choice to be honest about prognostic uncertainty rather than offering false reassurance or false precision). The T3N1M0 staging is the strongest trace — it is a specific pathological finding that requires genuine diagnostic workup. The epistemic limit statement reflects Andrew's professional values about honest communication with patients, which is visible in the specific language he chooses. |
| Idealisation risks | Risk of the prognosis section being too alarming — the 40–60% five-year survival rate is difficult information. Counteracted by "we will assess the tumour response after chemoradiation, which will give us more information" — Andrew is providing a near-term reassessment point that gives the patient something concrete to focus on. |
| Imperfection checklist | PASS. High conviction on treatment (standard of care, confident recommendation). Epistemic humility HIGH ("what I can and cannot tell you" structure, "I cannot tell you where you will fall"). Investment asymmetry HIGH (prognosis section). Low blind spots (patient-accessible language). Reasoning texture HIGH — population statistic contextualisation for individual patient. Human trace: T3N1M0 staging, 17 March appointment, and honest prognosis communication as professional values trace. |
| Validation gate | PASS |

---

## CB-ADV-025

**Context / subtype:** ADV — medical — geriatrician assessment, complex medical picture, independence vs safety judgment
**Sender role:** Geriatrician — assessment of elderly patient, complex picture, recommendation involves independence/safety judgment
**Word count:** 208
**Ground truth:** GENUINE

### Sender profile

Dr Patricia Chen, geriatrician, nineteen years in geriatric medicine. She has assessed Mrs Nakamura, an 84-year-old patient referred by her GP following a fall at home. The medical picture is complex — Mrs Nakamura has mild cognitive impairment, osteoporosis, and reduced mobility, but she is living independently, is cognitively intact enough to make her own decisions, and is strongly opposed to residential care. The recommendation involves a genuine judgment call about the balance between safety risk and the patient's right to autonomous decision-making. Patricia is being honest about this tension.

### Example text

---

Dear Dr Webb,

Thank you for referring Mrs Nakamura for geriatric assessment following her fall on 8 March 2026.

**Assessment findings:**
Mrs Nakamura is an 84-year-old woman with mild cognitive impairment (MoCA score 22/30 at today's assessment), established osteoporosis, and a six-month history of progressive mobility decline. Her fall risk assessment (STRATIFY score 3/5) indicates elevated fall risk. She is currently living alone, with family support visiting three times per week.

**My recommendation — and the judgment involved:**
I recommend a home modification assessment, referral to physiotherapy for a targeted balance program, and medication review with a focus on polypharmacy contributing to fall risk. These interventions can meaningfully reduce her fall risk.

I want to be honest about the judgment involved in this recommendation. Mrs Nakamura has the cognitive capacity to make decisions about her living situation and has expressed clearly that she does not wish to move to residential care. In my assessment, the appropriate response is to optimise her safety in her current home, respect her expressed preferences, and ensure her family understands the risks. I am not recommending residential care at this stage, but I want to be transparent that her risk profile is elevated and will require regular reassessment.

Yours sincerely,
Dr Patricia Chen
Geriatrician

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | M | Firm on the clinical findings (MoCA score 22/30, STRATIFY 3/5, established osteoporosis, six-month mobility decline) and on the specific interventions (home modification, physiotherapy, medication review). Deliberately balanced on the overall recommendation: "I want to be honest about the judgment involved." The recommendation explicitly acknowledges the tension between safety and patient autonomy. |
| Epistemic humility | H | "I want to be honest about the judgment involved in this recommendation" — Patricia is explicitly naming the value judgment embedded in her clinical recommendation. "I am not recommending residential care at this stage, but I want to be transparent that her risk profile is elevated and will require regular reassessment" — Patricia is giving a qualified recommendation that acknowledges the ongoing uncertainty and the need for future review. |
| Investment asymmetry | H | The "judgment involved" section receives the most careful language — Patricia's professional stake is in the GP understanding that the recommendation is not purely clinical but involves a value judgment about patient autonomy. The clinical findings are stated efficiently. |
| Blind spots | L | Writing to a GP — Dr Webb will understand all clinical terminology including MoCA, STRATIFY, polypharmacy, and the geriatric assessment framework. Low blind spots appropriate for clinician-to-clinician communication. |
| Reasoning texture | H | "Mrs Nakamura has the cognitive capacity to make decisions about her living situation and has expressed clearly that she does not wish to move to residential care" — Patricia is explicitly placing the patient's expressed preference at the centre of the recommendation. This explicit acknowledgment of patient autonomy as a clinical and ethical consideration — not just a background fact — is the trace of a geriatrician who has thought carefully about the tension between clinical risk management and patient self-determination. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. Three specific clinical artefacts: MoCA score 22/30 (a specific cognitive assessment score from today's consultation), STRATIFY score 3/5 (a specific fall risk assessment score), and Mrs Nakamura's expressed preference against residential care (a specific patient communication that Patricia has documented and is placing at the centre of her recommendation). The patient's expressed preference is the strongest trace — it is a specific piece of clinical communication that Patricia has incorporated into her management recommendation, which requires genuine knowledge of what the patient said and genuine professional engagement with the ethics of patient autonomy. |
| Idealisation risks | Risk of the judgment section making the recommendation seem uncertain or unsupported. Counteracted by the specific clinical findings (MoCA, STRATIFY) and the specific interventions (home modification, physiotherapy, medication review) — Patricia has a clear management plan; she is being honest that it reflects a value judgment, not that she lacks a recommendation. |
| Imperfection checklist | PASS. Medium conviction (clinical findings clear, value judgment acknowledged). Epistemic humility HIGH (judgment explicit, regular reassessment flagged). Investment asymmetry HIGH (judgment section). Low blind spots (clinician audience). Reasoning texture HIGH — patient autonomy placed at centre of clinical recommendation. Human trace: MoCA 22/30, STRATIFY 3/5, and patient's expressed preference. |
| Validation gate | PASS |

---

## CB-ADV-026

**Context / subtype:** ADV — consulting — organisational restructure recommendation, data-based, implementation risk acknowledged
**Sender role:** Strategy consultant — organisational restructure recommendation, data-based, implementation risk genuine
**Word count:** 207
**Ground truth:** GENUINE

### Sender profile

Elizabeth, strategy consultant, fourteen years in organisational design. She has completed an eight-week organisational effectiveness review of Northgate Financial Services. Her recommendation — consolidating the three regional business units into two, with a shared services function — is data-based and she is confident in it. The implementation risk is genuine: the consolidation will require restructuring of 47 roles, some redundancies, and union consultation in two of the three regions. Elizabeth is honest about this risk while maintaining her recommendation.

### Example text

---

Dear Ms Morrison,

Following our eight-week organisational effectiveness review, I am writing with my recommendations.

**The recommendation — I am confident in this:**
I recommend consolidating the three regional business units (Northern, Central, and Southern) into two (Eastern and Western), with a centralised shared services function covering finance, HR, and IT. This consolidation reduces structural duplication, brings the spans of control into line with industry best practice, and creates a cleaner accountability structure for the executive team.

**The data behind the recommendation:**
The current structure has 34% more management layers than comparable organisations of your size, and the Northern business unit, specifically, has a revenue-per-FTE ratio 28% below the other two units. The shared services consolidation is projected to reduce overhead costs by 12–15% over three years.

**The implementation risk — I want to be direct about this:**
This restructure will require role changes across 47 positions and some redundancies. The Northern and Southern regions have union representation, and consultation requirements will need to be carefully managed. I am not an industrial relations specialist — I recommend engaging one before commencing implementation. The risk to the recommendation is not structural; it is implementation. The right answer is clear. Getting there requires careful management.

Yours sincerely,
Elizabeth Marsden
Strategy Consultant

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | Firm on the recommendation (specific consolidation structure, named regions, shared services function). Firm on the data (34% more management layers, Northern unit 28% below peers on revenue-per-FTE, 12–15% cost reduction projected). "I am confident in this" — explicit label. "The right answer is clear" — stated with maximum professional conviction in the implementation risk section. |
| Epistemic humility | M | "I am not an industrial relations specialist — I recommend engaging one before commencing implementation" — Elizabeth is explicitly naming a domain where her expertise ends. "The risk to the recommendation is not structural; it is implementation" — this precise characterisation of where the uncertainty lives reflects Elizabeth's genuine assessment of the situation. |
| Investment asymmetry | H | The implementation risk section receives the most specific attention — 47 roles, union representation in two regions, IR specialist recommendation. Elizabeth's professional stake is in the client understanding that the recommendation is sound but the execution is complex. The data section is efficient and specific. |
| Blind spots | M | Assumes Ms Morrison knows what spans of control means, what a shared services function involves operationally, and what union consultation requirements entail in this context. Elizabeth has provided enough context that the recommendation and its risks are accessible. |
| Reasoning texture | H | "The right answer is clear. Getting there requires careful management" — two sentences that simultaneously assert Elizabeth's confidence in the structural recommendation and her honesty about the implementation complexity. This precise stratification — clear on the answer, honest about the path — is the trace of a consultant who has seen organisations implement correct structural recommendations badly and knows that the recommendation and the implementation are two separate problems. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. Three specific data artefacts: the 34% management layer excess (a specific finding from Elizabeth's comparative benchmarking), the Northern unit 28% below-peer revenue-per-FTE (a specific financial performance finding from the review), and the 47-role impact figure (a specific count from the restructure modelling Elizabeth has done). The Northern unit 28% finding is the strongest trace — it is a specific financial performance comparison that requires Elizabeth to have reviewed and benchmarked the financial data for all three units. |
| Idealisation risks | Risk of the IR specialist referral undermining confidence in the recommendation. Counteracted by "the right answer is clear" — Elizabeth is maintaining her structural recommendation while being honest about the implementation risk. The IR gap is in the execution domain, not the strategic domain. |
| Imperfection checklist | PASS. High conviction on structural recommendation (data-based). Epistemic humility MEDIUM (IR specialist referral). Investment asymmetry HIGH (implementation risk section). Blind spots MEDIUM. Reasoning texture HIGH — "right answer / getting there" stratification. Human trace: three specific data findings from review. |
| Validation gate | PASS |

---

## CB-ADV-027

**Context / subtype:** ADV — consulting — leadership team psychological assessment, findings clear, recommendations conditional
**Sender role:** Organisational psychologist — leadership assessment findings, psychological assessment clear, recommendations conditional on organisational willingness
**Word count:** 209
**Ground truth:** GENUINE

### Sender profile

Dr Marcus Webb, organisational psychologist, sixteen years in leadership assessment and development. He has completed a 360-degree leadership assessment of the Meridian Group executive team — six individuals assessed across leadership competencies, psychological safety, and team dynamics. His findings are clear and sometimes uncomfortable. His recommendations are conditional on the organisation's genuine willingness to act on them — he has seen organisations commission assessments and then not act, and he is being honest about what the assessment findings require.

### Example text

---

Dear Ms Chen,

I am writing to present the findings and recommendations from the Meridian Group executive team leadership assessment.

**Key findings — these are clear:**
The assessment identifies two significant patterns. First, psychological safety within the team is low — team members report limited ability to raise concerns or challenge the status quo without risk to their relationships or standing. This pattern is consistent across all six assessments. Second, two members of the executive team show divergent leadership styles that are creating visible tension in team decision-making. I will discuss both with you and the team directly.

**My recommendations — these are conditional:**
I recommend a structured team coaching program (six months, facilitated sessions monthly) and individual coaching for the two team members with divergent styles. These recommendations will have limited impact, however, if the psychological safety issue is not addressed at the leadership level — specifically, if the patterns driving low psychological safety are not examined and changed by the individuals responsible for them. This requires genuine engagement, not performative compliance.

I want to be direct: assessment findings without genuine organisational willingness to act on them produce no change. I have seen this pattern frequently. I will not recommend a program that will not be supported.

Yours sincerely,
Dr Marcus Webb
Organisational Psychologist

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | Firm on the findings (low psychological safety across all six assessments, divergent leadership styles producing visible tension — both stated as clear findings). The coaching recommendations are stated with professional confidence. "I will not recommend a program that will not be supported" — Marcus's highest conviction statement, about his own professional boundaries. |
| Epistemic humility | M | "These are conditional" — explicit label on the recommendations. "These recommendations will have limited impact, however, if the psychological safety issue is not addressed at the leadership level" — Marcus is honest about the conditions under which his recommendations will work. Medium intensity — the findings are clear; the conditional is about client engagement, not about the findings. |
| Investment asymmetry | H | The conditionality section receives the most space and the most direct language — including the unusual personal statement ("I have seen this pattern frequently. I will not recommend a program that will not be supported"). Marcus's professional stake is in the assessment producing genuine change, not in delivering a report that will be filed without action. |
| Blind spots | M | Assumes Ms Chen knows what psychological safety means in the organisational context, what 360-degree assessment involves, and what "divergent leadership styles" means for team decision-making. Marcus has provided enough context for the findings to be meaningful without full OD expertise. |
| Reasoning texture | H | "I have seen this pattern frequently. I will not recommend a program that will not be supported" — these two sentences are the most direct professional boundary statement in the advisory batch. Marcus is conditioning his recommendations on the client's genuine engagement, which requires him to have thought about his own professional standards and to be willing to state them explicitly in a client communication. This is the trace of a practitioner who has made a deliberate professional decision about what kinds of engagements he will and will not support. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. Two specific assessment artefacts: the "consistent across all six assessments" finding on psychological safety (a specific assessment-level finding, not an impression) and "the individuals responsible for them" in the psychological safety section (Marcus knows, from the assessment, which specific individuals are driving the low psychological safety pattern — he has not named them but his knowledge is specific). The "consistent across all six assessments" finding is the strongest trace — it requires Marcus to have conducted and reviewed six individual assessments and found a consistent pattern, not just a general organisational impression. |
| Idealisation risks | Risk of the "I will not recommend a program" statement seeming commercially inappropriate — a consultant threatening to withhold services. Counteracted by framing it as a professional standards statement ("I have seen this pattern frequently") rather than a commercial threat. |
| Imperfection checklist | PASS. High conviction on findings (six-assessment data). Epistemic humility MEDIUM (recommendations conditional on engagement). Investment asymmetry HIGH (conditionality and professional boundary sections). Blind spots MEDIUM. Reasoning texture HIGH — professional boundary statement from prior pattern recognition. Human trace: six-assessment consistency finding and individual identification (unstated but specific). |
| Validation gate | PASS |

---

## CB-ADV-028

**Context / subtype:** ADV — consulting — remuneration benchmarking, market data clear, application involves judgment
**Sender role:** HR consultant — remuneration benchmarking findings, market data confident, application to client judgment
**Word count:** 196
**Ground truth:** GENUINE

### Sender profile

Jennifer, HR consultant, ten years in remuneration consulting. She has completed a remuneration benchmarking review for TechStream across six roles. The market data is clear — she has used three data sources and the results are consistent. The application of the benchmarking data to TechStream's specific remuneration decisions involves judgment — specifically, TechStream's positioning strategy (where in the market range they want to pay) is a business decision, not a benchmarking determination.

### Example text

---

Dear Ms Okafor,

I am writing to present the findings of TechStream's remuneration benchmarking review.

**The market data — this is clear:**
I have benchmarked six roles against three data sources (Mercer, SEEK, and Talent.com proprietary data). The results are consistent across sources, which gives me confidence in the findings. I will present the detailed data at our scheduled meeting on 25 March — the summary is that four of the six roles are below market median, with the Head of Engineering and Head of Product roles sitting below the 25th percentile for total remuneration.

**The application of this data — this involves judgment:**
Where you position TechStream in the market range is a strategic decision, not a benchmarking determination. I can tell you what the market pays; I cannot tell you what you should pay, because that depends on your talent acquisition and retention strategy, your budget, and your culture. What the data does tell you is that the Head of Engineering and Head of Product positions carry the highest retention risk if not addressed.

I look forward to discussing the full findings on 25 March.

Yours sincerely,
Jennifer Huang
HR Consultant

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | Firm on the market data (three sources, consistent results, four of six roles below market median, two below 25th percentile). "This is clear" — explicit label. The data is Jennifer's domain and she is confident in it. |
| Epistemic humility | H | "This involves judgment" — explicit label for the application section. "I can tell you what the market pays; I cannot tell you what you should pay" — the most direct distinction between what Jennifer knows and what the client must decide in the advisory batch. The three factors she cannot determine (talent strategy, budget, culture) are genuine client-specific variables. |
| Investment asymmetry | H | The Head of Engineering and Head of Product positions appear in both sections — in the data section as the most below-market roles, and in the application section as the highest retention risk. Jennifer's professional stake is in the client understanding both the data finding and its practical implication without making the remuneration decision for them. |
| Blind spots | M | Assumes Ms Okafor knows what market median and 25th percentile mean in remuneration terms, what total remuneration includes, and what retention risk means for these specific roles. Standard assumptions for an HR director. |
| Reasoning texture | M | "I can tell you what the market pays; I cannot tell you what you should pay, because that depends on your talent acquisition and retention strategy, your budget, and your culture" — Jennifer is explaining the limits of benchmarking data precisely and completely. The three factors she names (strategy, budget, culture) are the genuine determinants of remuneration positioning that benchmarking data cannot answer. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. Two specific data artefacts: the three data sources (Mercer, SEEK, Talent.com — specific named sources Jennifer has used) and the Head of Engineering/Head of Product 25th percentile finding (a specific benchmark result for two named roles). The named data sources are the strongest trace — Jennifer has used three specific data products and is reporting their consistency, which requires genuine access to these sources. |
| Idealisation risks | Risk of the "I cannot tell you what you should pay" limitation making Jennifer seem unhelpful. Counteracted by the retention risk finding — Jennifer has identified the practical consequence of the data even while not making the strategic decision for the client. |
| Imperfection checklist | PASS. High conviction on market data (three consistent sources). Epistemic humility HIGH ("I cannot tell you what you should pay" explicit with three factors). Investment asymmetry HIGH (two roles appear in both sections). Blind spots MEDIUM. Reasoning texture MEDIUM — three genuine determinants of positioning decision. Human trace: named data sources and 25th percentile finding for specific roles. |
| Validation gate | PASS |

---

## CB-ADV-029

**Context / subtype:** ADV — consulting — market entry strategy, market analysis confident, execution risk uncertain
**Sender role:** Strategy consultant — market entry recommendation, analysis confident, execution risk genuine
**Word count:** 204
**Ground truth:** GENUINE

### Sender profile

Andrew, strategy consultant, seventeen years in market strategy and entry advisory. He is writing to the board of Meridian Group following a twelve-week market analysis of the New Zealand professional services market. His recommendation — enter via acquisition of a mid-sized NZ accounting firm rather than organic growth — is based on the market analysis and he is confident in it. The execution risk is genuine: acquisition targets in this market are limited, acquisition pricing has been elevated, and the integration of a professional services firm requires cultural alignment that cannot be assessed from the outside.

### Example text

---

Dear Ms Morrison and the Board,

Following our twelve-week market analysis, I am writing with my strategic recommendation for the New Zealand market entry.

**The market analysis — I am confident in this:**
The New Zealand professional services market offers a genuine opportunity for Meridian Group. The market is underconsolidated — the top five firms hold 41% of market share, compared to 68% in Australia — and there is appetite from mid-tier firm owners for exit conversations. Organic growth would take five to seven years to reach meaningful scale. Acquisition offers a faster path to market position.

**My recommendation:**
I recommend pursuing an acquisition of a mid-sized NZ professional services firm (target size: $8–15M revenue) as the primary market entry strategy. I have identified three firms that meet the initial screening criteria, which I will present to the board separately.

**The execution risk — this is real:**
The three identified firms are the strongest in the market — all will have competitive interest. Acquisition pricing for professional services firms in NZ is currently elevated (5–8x EBITDA), reflecting strong recent deal activity. Integration risk is the highest risk I cannot model: cultural alignment in a professional services firm is a human judgment call that due diligence can inform but not determine.

Yours sincerely,
Andrew Marsden
Strategy Consultant

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | Firm on the market analysis (41% vs 68% concentration comparison, five-to-seven year organic growth timeline, three identified acquisition candidates). "I am confident in this" — explicit label. The acquisition recommendation is stated with full strategic conviction. |
| Epistemic humility | H | "This is real" — explicit label on the execution risk section. "Integration risk is the highest risk I cannot model" — Andrew is explicitly identifying the risk that is beyond his analytical capability. "A human judgment call that due diligence can inform but not determine" — the most precise acknowledgment of the limits of consulting analysis in the advisory batch. |
| Investment asymmetry | H | The integration risk section receives the most specific analytical attention — the pricing range (5–8x EBITDA), the competitive interest assessment, and the "cannot model" integration risk acknowledgment. Andrew's professional stake is in the board understanding that the execution risk is real and specifically the integration risk is not analytically reducible. |
| Blind spots | M | Assumes the board knows what EBITDA multiples mean in M&A context, what due diligence involves in a professional services acquisition, and what "cultural alignment" means operationally. Standard assumptions for a board considering an M&A strategy. |
| Reasoning texture | H | "Integration risk is the highest risk I cannot model: cultural alignment in a professional services firm is a human judgment call that due diligence can inform but not determine" — Andrew is being precise about what his analysis can and cannot tell the board. The phrase "can inform but not determine" is the trace of a strategy consultant who understands the difference between analytical insight and predictive certainty, and who is willing to name that distinction explicitly rather than implying his analysis is complete. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. Three specific market artefacts: the 41% vs 68% market concentration comparison (a specific finding from Andrew's twelve-week market analysis), the three identified acquisition targets (specific firms Andrew has screened against criteria — he has not named them but they are specific), and the 5–8x EBITDA pricing range (a specific market data point from recent NZ deal activity). The 41% concentration figure is the strongest trace — it is a specific market data point derived from Andrew's analysis that could not be fabricated without genuine market research. |
| Idealisation risks | Risk of the "cannot model" integration risk acknowledgment undermining the acquisition recommendation. Counteracted by the specific market analysis data that supports the acquisition rationale — Andrew is not uncertain about whether to acquire; he is uncertain about the integration outcome, which is a genuinely different question. |
| Imperfection checklist | PASS. High conviction on market analysis and acquisition recommendation (twelve-week data). Epistemic humility HIGH ("I cannot model" explicit, "inform but not determine" precision). Investment asymmetry HIGH (execution risk section). Blind spots MEDIUM. Reasoning texture HIGH — "inform but not determine" from analytical limit awareness. Human trace: 41% market concentration, three screened targets, 5–8x pricing range. |
| Validation gate | PASS |

---

## CB-ADV-030

**Context / subtype:** ADV — consulting — transformation program assessment, underperforming, honest diagnosis, directional recommendations
**Sender role:** Change management consultant — transformation program mid-point assessment, honest about underperformance, directional on recovery
**Word count:** 211
**Ground truth:** GENUINE

### Sender profile

Patricia, change management consultant, eighteen years in organisational transformation. She has been engaged to conduct a mid-point assessment of a twelve-month digital transformation program at Coastal Industries — six months in, and the program is behind on three of five workstreams. Patricia's assessment is honest — the program is underperforming and the causes are identifiable. Her recommendations are directional — she knows what needs to change but cannot specify exactly how without the organisation's own leadership making some decisions about priorities.

### Example text

---

Dear Mr and Mrs Fitzpatrick,

I am writing to present my mid-point assessment of the Coastal Industries digital transformation program.

**The honest assessment:**
The program is behind schedule on three of five workstreams: data infrastructure, customer portal, and internal reporting. The two on-track workstreams — payment processing and inventory management — are proceeding well. The causes of the delay are identifiable: sponsor engagement has been inconsistent, particularly in Q1; the change management resourcing was insufficient relative to the program's scope; and the technology vendor delivered the data infrastructure module six weeks late, which created downstream delays.

**What needs to change:**
Three things need to change for the program to recover: executive sponsor engagement must increase significantly in the next 90 days; the change management team needs to be augmented by at least two resources; and the technology vendor contract must be renegotiated to include liquidated damages provisions for future delays.

**What I cannot specify without your input:**
Whether the program recovers on its current timeline or whether the timeline needs to be reset is a decision that depends on your organisation's risk tolerance and the business case for delivery by the original deadline. I can model both scenarios. I cannot make this decision for you.

Yours sincerely,
Patricia Sinclair
Change Management Consultant

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | Firm on the diagnosis (three of five workstreams behind, two on track, three specific causes identified). Firm on the three recovery actions (executive engagement, change management resourcing, vendor contract renegotiation). "Three things need to change" — stated with professional conviction. |
| Epistemic humility | H | "What I cannot specify without your input" — explicit label on the section where Patricia defers to the client. "I can model both scenarios. I cannot make this decision for you" — direct epistemic limit statement that distinguishes Patricia's analytical capability from the decision authority. |
| Investment asymmetry | H | The diagnosis section receives the most specific attention — three workstreams named, two on-track named, three specific causes identified. Patricia's professional stake is in the client having an honest diagnosis rather than a softened one. The "what needs to change" section is equally specific. |
| Blind spots | M | Assumes the Fitzpatricks know what "liquidated damages provisions" means in a technology vendor contract, what "change management resourcing" involves in practice, and what "sponsor engagement" means in a program management context. Patricia has provided enough context for the recommendations to be actionable. |
| Reasoning texture | H | "The honest assessment" as the first section label is the highest reasoning texture element in the batch — Patricia has explicitly named her diagnostic section as "honest," which signals that she is aware honest assessments are sometimes not what clients want to hear, and that she is choosing to provide one anyway. "Sponsor engagement has been inconsistent, particularly in Q1" — Patricia is identifying the client organisation's own leadership as a cause of the delay, which requires professional courage to put in writing. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. Three specific program artefacts: the five workstream structure with specific names (data infrastructure, customer portal, internal reporting as delayed; payment processing and inventory management as on-track — specific workstream names from the program plan), the Q1 sponsor engagement gap (a specific temporal finding from Patricia's assessment), and the six-week vendor delay (a specific documented delay from the technology vendor). The Q1 sponsor engagement finding is the strongest trace — it is a specific temporal assessment that requires Patricia to have reviewed the program governance and identified when sponsor engagement declined. |
| Idealisation risks | Risk of "the honest assessment" label being too confrontational — the client may resist a diagnosis that identifies their own leadership as a cause. Counteracted by naming the technology vendor delay alongside the internal causes — the causes are distributed, not entirely attributed to the client's leadership. |
| Imperfection checklist | PASS. High conviction on diagnosis and recovery actions (six months of program data). Epistemic humility HIGH ("what I cannot specify" label, "I cannot make this decision for you"). Investment asymmetry HIGH (diagnosis section specificity). Blind spots MEDIUM. Reasoning texture HIGH — "the honest assessment" label as professional courage marker, Q1 sponsor engagement finding as leadership cause. Human trace: specific workstream names, Q1 sponsor gap, and six-week vendor delay. |
| Validation gate | PASS |

---

*Owlume Pty Ltd — Confidential — corpus_batch9_adv_016_030_v1 · 30 March 2026 · Batch review pending*