# Calibration Baseline Definition Document

**HumanTrace — Internal Document**
Version 1.0 · 30 March 2026 · Owlume Pty Ltd

---

## 1. Purpose and Scope

This document defines what genuine human reasoning looks like across the enterprise contexts in which HumanTrace operates. It is the calibration anchor — the reference model against which the engine determines whether a message departs from the signature of authentic human thought.

Without this baseline, the engine has no stable reference. It may flag normal human uncertainty as a synthetic signal, or miss synthetic content that mimics surface-level human patterns without containing the deeper markers of genuine reasoning. The calibration gap is an architectural dependency, not incidental to detection quality.

The document covers:

- The fundamental properties of human reasoning that are difficult to synthetically replicate
- Four enterprise contexts — financial services, legal correspondence, internal organisational communications, and professional advisory — each with context-specific baseline profiles
- Common human-authored variation patterns that must not be flagged as synthetic
- The architectural implications for each detector family

---

## 2. The Fundamental Properties of Human Reasoning

Genuine human reasoning carries markers that arise from cognitive architecture — the way humans actually form, weigh, and express beliefs. These properties are distinct from style. They are structural features of thought made visible in language.

Five properties define the baseline. Each is present in authentic human-authored messages at varying degrees. Their collective absence — not the absence of any single property — is the detection target.

### 2.1 Conviction Cost

Humans express strong positions at a cost. A genuine assertion of fact, accusation, or demand carries implicit acknowledgment that the sender could be wrong, could be challenged, or could face consequences. This cost produces characteristic hedging patterns even in confident communicators: qualifications that are positioned asymmetrically, stronger claims on matters the author has direct experience with, softer claims where they are working from second-hand information.

Synthetic persuasion typically distributes conviction evenly — all claims asserted with similar weight, because there is no differential cost to being wrong.

**Detection signal:** Asymmetric confidence distribution is a positive human marker. Uniform confidence across all claims is a negative marker.

### 2.2 Epistemic Humility

Genuine human reasoning acknowledges limits. Not as performance, but as a natural consequence of knowing what you know and knowing what you don't. This asymmetry of knowledge produces visible gaps: what is stated versus what is left implicit, requests for information rather than assertions, conditional framing.

Malicious synthetic reasoning tends to present a complete picture — all relevant facts assembled, all implications drawn, a closed argument.

**Detection signal:** Incomplete pictures with genuine information gaps are a positive human marker. Artificially complete arguments with no visible knowledge limits are a negative marker.

### 2.3 Personal Investment Asymmetry

Humans care more about some aspects of a situation than others, based on their particular stake in the outcome. This asymmetry of attention — spending more words, more precision, more emotional weight on what the sender has personal exposure to — is a signature of genuine authorship.

Synthetic persuasion typically produces balanced coverage across all relevant aspects, because it is optimised for the reader's experience rather than shaped by the sender's genuine concerns.

**Detection signal:** Uneven attention distribution correlated with likely sender stakes is a positive human marker. Evenly distributed attention across all topics is a negative marker.

### 2.4 Blind Spots from Personal Experience

Humans overlook what is obvious to them. An expert communicating with a non-expert will inadvertently omit steps that feel too basic to mention. These blind spots produce characteristic incompleteness — information omitted not to deceive, but because the sender could not see the gap.

Malicious synthetic reasoning tends to close all gaps strategically.

**Detection signal:** Accidental omissions that align with expertise assumptions are a positive human marker. Strategic omissions that align with persuasion goals are a negative marker.

### 2.5 Reasoning Texture

Human thinking is nonlinear. Writers backtrack, add qualifications mid-sentence, start a point and shift direction. This reasoning texture — the visible trace of a mind working through a problem — is difficult to replicate synthetically.

Well-engineered synthetic persuasion is smooth. The logic flows cleanly, examples are perfectly chosen, qualifications appear in the ideal position.

**Detection signal:** Structural imperfections in reasoning-heavy messages are a positive human marker. Engineered smoothness in contexts that would produce human strain is a negative marker.

---

## 3. Enterprise Context Profiles

### 3.1 Financial Services — Collections, Lending, Fraud Operations

**Context:** Communications from financial institutions regarding account status, repayment obligations, debt recovery, or fraud investigations. Staff constrained by regulation (ASIC, APRA, NCCP Act, Privacy Act) and institutional tone guidelines.

| Property | Expected baseline signature | Calibration note |
|---|---|---|
| Conviction cost | Strong on regulatory facts; hedged on customer circumstances | Asymmetry is legal protection |
| Epistemic humility | Explicit requests for confirmation; "our records show" rather than assertions | Regulatory language produces genuine limits |
| Investment asymmetry | Disproportionate attention to repayment terms and compliance obligations | Institutional stake is in recovery |
| Blind spots | Assumes customer knows account history and standard banking procedures | Expertise blind spot |
| Reasoning texture | Template-constrained with personalised insertions; awkwardness at template seams | Template use does not erase texture |

**Must not be flagged:** Urgency mirroring regulatory deadlines; formal institutional tone without warmth; repeated procedural references; third-party references to legal team or credit reporting bodies.

**Synthetic departure signature:** Regulatory-sounding urgency combined with non-institutional contact method; perfect formality with no template awkwardness; uniform confidence; closed argument with no genuine information requests.

### 3.2 Legal Correspondence

**Context:** Demand letters, settlement correspondence, regulatory submissions, disclosure notices. Written with awareness the document may be reviewed adversarially.

| Property | Expected baseline signature | Calibration note |
|---|---|---|
| Conviction cost | Carefully stratified: legal assertions as fact; factual assertions about other party hedged with "alleged" | Legal training produces deliberate stratification |
| Epistemic humility | Explicit limits on knowledge of other party's internal state; reservations about matters pending evidence | "Without prejudice" framing is genuine limit acknowledgment |
| Investment asymmetry | Disproportionate precision on matters forming the claimed legal breach | Reflects client instruction priority |
| Blind spots | Assumes legal literacy; visible one-sidedness from client perspective | Adversarial framing creates structural one-sidedness |
| Reasoning texture | Arguments revisit premises; qualifications are nested; occasional over-qualification | Complexity is not synthetic smoothness |

**Must not be flagged:** Threatening language; one-sided presentation of facts; repetition of legal claims; formal Latin phrases or citations.

**Synthetic departure signature:** Imitates legal formality but lacks deliberate epistemic stratification. All claims asserted with equal certainty. Urgency attached to relief a genuine legal proceeding would not require within the stated timeframe.

### 3.3 Internal Organisational Communications

**Context:** Manager-to-employee requests, executive directives, HR communications, IT security notices, policy updates. Brief, written with assumed shared context, shaped by social hierarchies.

| Property | Expected baseline signature | Calibration note |
|---|---|---|
| Conviction cost | Highly variable by hierarchy; senior communications may be directive without hedge | Hierarchy shapes confidence register |
| Epistemic humility | Frequent: "let me know if you have questions", "I'll confirm with [name]" | Internal communications assume incomplete information |
| Investment asymmetry | Brief high-pressure requests focus intensely on the specific action required | Brevity amplifies asymmetry visibility |
| Blind spots | Heavy assumption of shared context — systems, processes, names, recent events | Context-dense blind spot is strong human marker |
| Reasoning texture | Often minimal; when reasoning is given it reflects genuine uncertainty about a novel situation | Absence of reasoning is normal in brief messages |

**Must not be flagged:** Urgent requests with no explanation; gift card or wire transfer requests from known senior names (flagged only with abnormal contact method or secrecy instruction); IT security notices with action urgency; brief impersonal register from senior leadership.

**Synthetic departure signature:** Correct name and role used, but critical shared context omitted. Unusual contact channel, secrecy instruction, and action urgency bypassing normal process are the highest-value composite signals.

### 3.4 Professional Advisory

**Context:** Financial advisors, accountants, consultants, medical specialists. Explicit knowledge asymmetry and professional obligations of disclosure and honesty.

| Property | Expected baseline signature | Calibration note |
|---|---|---|
| Conviction cost | High confidence in domain expertise; genuine uncertainty outside direct knowledge; conditional recommendations | Expert confidence has visible domain limits |
| Epistemic humility | Regulatory disclosure obligations make limits explicit: "based on the information provided", "subject to final review" | Disclosure requirements produce genuine limit statements |
| Investment asymmetry | Precision on core advisory matter; defensive precision at liability points | Liability exposure shapes attention distribution |
| Blind spots | Expert-level communication; assumes client understands technical terms | Expertise blind spot is strong human marker |
| Reasoning texture | Recommendations show genuine working; visible weighing of alternatives; acknowledges different facts would produce different recommendation | Genuine deliberation is visible in reasoning trace |

**Must not be flagged:** Investment urgency language for time-limited opportunities; strong directional recommendations anchored in disclosed reasoning; imprecise language outside core domain; multiple conditional statements.

**Synthetic departure signature:** Expert register used correctly but without reasoning texture of genuine deliberation. Conclusion reached too efficiently — no visible weighing, no alternative considered, no acknowledged uncertainty within the domain.

---

## 4. Cross-Context Invariants

### 4.1 Information requests signal genuine uncertainty
A message that contains no genuine information request — that proceeds as if all necessary information is already assembled — is more likely to have been engineered than authored.

### 4.2 Specificity is asymmetric
Genuine authors are more specific about things they directly know. A uniform level of specificity across all claims is a synthetic marker.

### 4.3 Stakes produce emotional residue
A high-stakes message with no apparent stakes awareness — no careful word choice, no hedging where exposure is greatest — is a negative marker.

### 4.4 Authentic messages have an intended reader
Genuine human authors write for a specific person. Synthetic persuasion optimises for a general reader. Universality — lack of specific targeting artefacts — is a calibration signal.

---

## 5. Calibration Anti-Patterns

| Anti-pattern | Why it resembles synthetic content | How to distinguish |
|---|---|---|
| Template use | Smooth, consistent structure; little reasoning texture | Templates have personalised insertions with texture at seams; fully smooth text with no seams is synthetic |
| Regulatory urgency | Urgent time pressure language | Legitimate urgency references regulatory deadlines with traceable basis |
| Brief internal requests | Lack of reasoning; high action pressure; minimal context | Legitimate brevity references shared context implicitly |
| Expert confidence | Strong confident assertions without hedging | Expert confidence is domain-limited; genuine experts hedge outside their direct knowledge |
| Marketing optimisation | Persuasion-oriented language; call-to-action urgency | Marketing targets a generic action; fraud targets a specific non-standard action |
| Non-native English | Grammatical irregularities; unusual phrasing | Non-native irregularities are consistent with the author's linguistic background |

---

## 6. Architectural Implications

| Detector family | Calibration dependency | Positive human markers to encode | Calibration risk without this document |
|---|---|---|---|
| INT — Intent Extraction | §3 context profiles | Genuine information requests; conditional framing | Legitimate collections intent flagged as extraction |
| TRUST — Trust Hijack | §3.1, §3.2 | Institutional authority citation as regulatory compliance | All authority citation treated as hijack |
| PRESS — Pressure/Urgency | §3 all contexts; §5 | Regulatory-deadline urgency with traceable basis | Legal deadlines flagged as pressure |
| DIST — Reasoning Distortion | §4; §2.2 | One-sided argument in adversarial context; genuine knowledge gaps | Legitimate legal arguments flagged as distortion |
| AUTH — Authenticity Gap | §2; §4 | Accidental omissions aligned with expertise blind spots; stakes residue | Expert-level communication flagged as synthetic smoothness |

---

## 7. Calibration Corpus Requirements

Minimum corpus coverage:
- Financial services: 40 examples minimum
- Legal correspondence: 30 examples minimum
- Internal organisational: 40 examples minimum
- Professional advisory: 30 examples minimum
- Anti-pattern coverage: 10 examples each of template-generated, regulatory urgency, and expert-confidence writing

The corpus must not be supplemented with general-purpose human writing. The enterprise baseline is distinct from a general human-writing baseline.

---

## 8. Version Notes

Version 1.0 — 30 March 2026. Four enterprise contexts covered. Pending: healthcare and government contexts (post-pilot).

*Owlume Pty Ltd — Confidential*