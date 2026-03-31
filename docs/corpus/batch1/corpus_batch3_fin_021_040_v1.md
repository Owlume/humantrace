# Calibration Corpus — Batch 3, Examples 21–40

**HumanTrace — Internal Document**
Financial Services — Fraud Operations Communications · CB-FIN-021 through CB-FIN-040
Ground truth: GENUINE · Path A synthetic genuine construction
Version 1.0 · 30 March 2026 · Owlume Pty Ltd
Constructed under `corpus_construction_protocol_v1.1`

> **Batch construction note:** This batch is the most critical calibration batch in the financial services context. Fraud operations communications share surface features with synthetic fraud attacks — urgency, authority citation, consequence language. Every example in this batch must demonstrate that the engine can distinguish legitimate fraud operations communications from synthetic fraud attacks on the basis of reasoning structure, not surface features. The human trace in each example is therefore especially important to identify and preserve.

---

## CB-FIN-021

**Context / subtype:** FIN — fraud ops — transaction dispute notification, junior analyst, routine flag
**Sender role:** Junior fraud analyst — automated card transaction flag, routine notification
**Word count:** 167
**Ground truth:** GENUINE

### Sender profile

Priya, junior fraud analyst, 11 months in the role. The system flagged a $340 transaction at an electronics retailer — the customer has not made a purchase at this merchant before and the transaction was larger than their typical spend pattern. The flag is automated; Priya reviewed it and agreed it warranted a notification. Her personal stake is low — this is one of fifteen notifications she is processing today. She is working from the standard dispute notification template. The urgency is procedural — the customer has 30 days to dispute, but the earlier the better.

### Example text

---

Dear Ms Okafor,

We are contacting you about a recent transaction on your Meridian Bank Visa card ending 5531.

A transaction of $340.00 at TechZone Electronics on 24 March 2026 has been flagged by our monitoring system as potentially inconsistent with your recent card activity. We are writing to ask you to confirm whether this transaction was made by you or with your authorisation.

If this transaction was made by you, no further action is required. You can confirm this by logging into your Meridian Bank app and selecting "Confirm transaction" under the notification, or by calling us on 1800 XXX XXX.

If this transaction was not made by you, please contact us immediately on 1800 XXX XXX so we can take steps to protect your account. We may place a temporary hold on your card while we investigate.

Please respond within 5 business days to avoid any delay in resolving this matter.

Yours sincerely,
Priya Singh
Fraud Operations
Meridian Bank

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | M | Firm on the transaction fact ("a transaction of $340.00 at TechZone Electronics on 24 March 2026") — this is a system record, not an interpretation. Explicitly uncertain on the interpretation ("potentially inconsistent with your recent card activity") — "potentially" is the key qualifier. The bank is not asserting fraud; it is flagging an anomaly and asking the customer to resolve the uncertainty. |
| Epistemic humility | H | The entire letter is structured around a genuine information gap — Priya does not know whether the transaction is fraudulent or legitimate. The two-pathway structure (confirm / dispute) is the structural expression of that uncertainty. "We are writing to ask you to confirm" — the bank is requesting information it does not have, not asserting a conclusion it has reached. |
| Investment asymmetry | M | The dispute pathway ("if this transaction was not made by you, please contact us immediately") receives slightly more urgency language ("immediately") than the confirmation pathway ("no further action is required"). Priya's institutional stake is in catching fraud, not in the customer's convenience — the asymmetry reflects that. |
| Blind spots | M | Assumes Ms Okafor knows how to log into the Meridian Bank app and navigate to "Confirm transaction." Does not explain what a "temporary hold" means in practice for the customer's day-to-day access. Assumes the customer understands what "card activity monitoring" means. Medium intensity — these are relatively common concepts for a bank customer. |
| Reasoning texture | L | Standard dispute notification template with factual insertions: customer name, card number, transaction amount, merchant name, date, response window. The two-pathway structure is template design, not Priya's reasoning. Low texture appropriate to a routine flag — Priya reviewed and agreed, which is the limit of her contribution. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. Minimal but present. The human trace is in the "potentially inconsistent with your recent card activity" qualifier — Priya reviewed the flag and agreed it warranted a notification, which required her judgment that the flag was plausible. An automated system would generate the flag; a human had to decide whether it reached the threshold for customer notification. That decision, and the "potentially" qualifier that reflects its uncertainty, is Priya's contribution. |
| Idealisation risks | Risk of adding warmth or reassurance that Priya would not include. Counteracted by keeping the letter entirely within the institutional template register. Risk of making the urgency too high — pushing toward synthetic pressure. Counteracted by keeping "immediately" for the dispute pathway only and using "5 business days" as the response window rather than a shorter artificial deadline. |
| Imperfection checklist | PASS — modified. Low personal stake produces minimal texture (justified). Epistemic humility HIGH (two-pathway structure). Assumed knowledge MEDIUM. "Potentially" as the key hedge on interpretation. Human trace: judgment that the flag warranted notification, expressed in the "potentially inconsistent" qualifier. |
| Validation gate | PASS |

---

## CB-FIN-022

**Context / subtype:** FIN — fraud ops — high-value business transaction flag, senior analyst decision
**Sender role:** Senior fraud analyst — high-value business account transaction, genuine outcome uncertainty
**Word count:** 214
**Ground truth:** GENUINE

### Sender profile

Marcus, senior fraud analyst. The flagged transaction is $28,000 wire transfer from a business account to an overseas supplier. The business owner, Mr Delacroix, makes overseas payments regularly — but not to this recipient, and not at this time of month. Marcus has reviewed the account history. He is genuinely uncertain: this could be a legitimate new supplier relationship, or it could be a BEC fraud where the supplier's bank details have been changed. His stake is real — if he freezes a legitimate business payment, he disrupts Delacroix's operations and the bank gets a complaint. If he does not act and it is BEC fraud, the loss is significant and his judgment will be reviewed. He is proceeding carefully.

### Example text

---

Dear Mr Delacroix,

I am contacting you urgently regarding a wire transfer of $28,000 initiated from your business account ending 7743 on 25 March 2026.

I am the senior analyst reviewing this transaction and I want to speak with you directly before this transfer is processed. The transfer is currently on hold pending your confirmation.

The recipient details for this transfer are different from overseas suppliers you have paid previously through this account. While I understand this may be a new or updated banking arrangement with an existing supplier, I want to make sure you have authorised this specific transfer to this specific recipient before it proceeds.

I am not suggesting this transfer is fraudulent. What I am asking is that you call me directly on the number below so I can confirm the authorisation with you before we release the payment. This will take no more than a few minutes.

If you have authorised this transfer and are comfortable with the recipient details, I can release the payment immediately once I have spoken with you.

Please call me as soon as you receive this message. If I do not hear from you within two hours, I will need to place a temporary hold on the transfer and your account team will contact you to discuss next steps.

Yours sincerely,
Marcus Webb
Senior Fraud Analyst
Meridian Bank Business Banking

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | M | Firm on the facts: the transaction amount, the date, the account, the difference from prior payment recipients. Explicitly careful on the interpretation: "I am not suggesting this transfer is fraudulent" — a direct disavowal of the accusation he is implicitly investigating. "While I understand this may be a new or updated banking arrangement" — he is explicitly acknowledging the legitimate explanation before requesting confirmation. The asymmetry of conviction (certain on facts, careful on interpretation) is the defining feature. |
| Epistemic humility | H | "I want to make sure you have authorised this specific transfer to this specific recipient before it proceeds" — Marcus does not know whether this is authorised. The entire letter is structured around that genuine uncertainty. "If you have authorised this transfer and are comfortable with the recipient details, I can release the payment immediately" — the approval pathway is stated as a genuine outcome, not a formality. |
| Investment asymmetry | H | The call request and the confirmation process receive the most precise language — "call me directly on the number below", "no more than a few minutes", "I can release the payment immediately once I have spoken with you." The transaction details are stated once. Marcus's stake is in getting the voice confirmation — that call is the pivotal action, and it receives disproportionate attention and precision. |
| Blind spots | M | Assumes Mr Delacroix knows what BEC fraud is and why a change in recipient details is significant. Does not explain why the recipient being new is a risk indicator. Assumes he has access to his phone and can respond within two hours. Medium intensity — Marcus is more aware than usual of the customer's perspective (hence "I am not suggesting this transfer is fraudulent") but still assumes some background understanding of why this matters. |
| Reasoning texture | H | "I am not suggesting this transfer is fraudulent" — this sentence is not template language. Marcus added it because he is aware that the letter could read as accusatory, and he is managing that perception while still achieving the operational goal. The two-hour window is his judgment, not a policy threshold — it reflects his assessment of how long the hold can be maintained before the business impact becomes the bigger problem. The combination of urgency and explicit exculpatory statement produces the highest reasoning texture in the sub-type. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The specific cognitive event is Marcus's awareness of the double risk — freeze a legitimate payment and get a complaint, miss a BEC fraud and face review. This dual awareness produces: the explicit exculpatory statement ("I am not suggesting this transfer is fraudulent"), the acknowledgment of the legitimate explanation ("new or updated banking arrangement"), the two-hour window (Marcus's calibrated judgment of the minimum safe hold time), and the direct call request rather than a form submission. Each element is the trace of a senior analyst managing genuine outcome uncertainty, not a system generating a standard fraud alert. |
| Idealisation risks | Risk of making Marcus too accusatory — tipping the balance toward the fraud interpretation. Counteracted by keeping the exculpatory statement prominent and the legitimate explanation acknowledged first. Risk of making the urgency too high — pushing toward synthetic pressure. Counteracted by explaining the reason for the two-hour window and making the release pathway ("I can release the payment immediately") clearly available. |
| Imperfection checklist | PASS. Hedged interpretation (explicit exculpatory statement). Assumed knowledge MEDIUM. Precision asymmetry HIGH (call request vs transaction details). Reasoning texture HIGH — exculpatory statement, two-hour judgment, legitimate explanation acknowledged. Human trace: dual-risk awareness visible in every structural choice. |
| Validation gate | PASS |

---

## CB-FIN-023

**Context / subtype:** FIN — fraud ops — international transaction flag, known traveller
**Sender role:** Fraud analyst — international transaction flagged, customer history shows regular travel
**Word count:** 178
**Ground truth:** GENUINE

### Sender profile

Yasmin, fraud analyst. Mr Kowalski's card was used at a hotel in Prague. He has not used his card internationally before — but his account notes show he mentioned travel plans to Europe to his branch manager three months ago. The note is informal, not a travel notification. Yasmin is reasonably confident this is legitimate but cannot be certain. Speed matters — if the card is incorrectly blocked, Kowalski is in Prague without access to funds. If it is fraud and she does not act, the loss continues. She is sending a rapid notification and keeping the communication tight.

### Example text

---

Dear Mr Kowalski,

Your Meridian Bank card ending 2281 has been used for a transaction of $284.00 at Grandhotel Bohemia, Prague, Czech Republic on 26 March 2026.

As this is the first international transaction on this card, our systems have flagged it for review. We want to make sure you are travelling and have authorised this transaction.

If you are currently travelling and made this purchase, please confirm by replying to this message or by calling 1800 XXX XXX. Once confirmed, your card will remain active for international use during your trip.

If you did not make this transaction, please call us immediately on 1800 XXX XXX and we will take steps to secure your account.

We understand being contacted about your card while travelling can be inconvenient — we will resolve this as quickly as possible.

Yours sincerely,
Yasmin Osei
Fraud Operations
Meridian Bank

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | L | The flag is stated factually. The interpretation is not asserted — "our systems have flagged it for review" rather than "this transaction appears suspicious." Yasmin has a reasonable belief this is legitimate but cannot assert it. Low conviction on interpretation is appropriate and genuine. |
| Epistemic humility | H | "We want to make sure you are travelling and have authorised this transaction" — Yasmin does not know either of these things. The two-pathway structure is genuine. The acknowledgment of inconvenience ("being contacted about your card while travelling can be inconvenient") is a genuine recognition of the customer's situation — Yasmin is aware she may be interrupting someone in Prague who is perfectly fine. |
| Investment asymmetry | M | The confirmation pathway and the dispute pathway receive equal weight — unusual for a fraud alert. Yasmin's genuine uncertainty about which interpretation is correct produces the balance. She has not pre-committed to either outcome. |
| Blind spots | M | Assumes Mr Kowalski has access to his phone while in Prague, that he will receive this message promptly, and that he knows how to respond to an SMS or email while roaming. Does not explain what "remain active for international use during your trip" means — whether the card is currently blocked or merely flagged. |
| Reasoning texture | L | Tight, fast communication appropriate to the urgency of the situation. The acknowledgment of inconvenience is Yasmin's addition to the template — a one-sentence recognition that she may be causing a problem for a legitimate traveller. That sentence is the sole texture element. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The specific cognitive event is Yasmin's speed-vs-accuracy tension: Prague, customer is potentially without card access, the decision to notify rather than block or ignore is hers. The acknowledgment of inconvenience is the trace — it is the sentence of someone who has considered the customer's situation (in Prague, receiving a fraud alert, possibly blocked) and added a one-line recognition of it. A template would not include this. Yasmin added it because she is aware of the disruption she may be causing. |
| Idealisation risks | Risk of making the notification too warm — reducing the operational urgency. Counteracted by keeping the communication tight and the call numbers prominent. Risk of making the urgency too high — pushing toward synthetic pressure. Counteracted by the balanced two-pathway structure and the "as quickly as possible" framing rather than an artificial deadline. |
| Imperfection checklist | PASS. Low conviction on interpretation (justified). Epistemic humility HIGH. Balanced pathways (reflects genuine uncertainty). Inconvenience acknowledgment as texture anchor. Human trace: speed-vs-accuracy judgment made visible in tight format and inconvenience acknowledgment. |
| Validation gate | PASS |

---

## CB-FIN-024

**Context / subtype:** FIN — fraud ops — card testing pattern flag, ambiguous transaction series
**Sender role:** Fraud analyst — small transaction series flagged as potential card testing, genuine interpretive ambiguity
**Word count:** 191
**Ground truth:** GENUINE

### Sender profile

Daniel, fraud analyst. Ms Ferreira's card has had five transactions between $1.20 and $4.80 at four different merchants over two days. The pattern is consistent with card testing — small transactions used to verify a card is active before a larger fraudulent purchase. But it is also consistent with legitimate small purchases (coffee, parking, app subscriptions). Daniel genuinely cannot tell. He is flagging it and asking the customer, which is the right procedural step, but he is more uncertain than in CB-FIN-021.

### Example text

---

Dear Ms Ferreira,

We are contacting you about a series of recent transactions on your Meridian Bank Visa card ending 8814.

Over the period 23–24 March 2026, the following transactions were processed on your card:

- $1.20 at Parkmate (23 March)
- $3.50 at The Coffee Club, George St (23 March)
- $2.90 at Spotify Australia (24 March)
- $4.80 at Apple App Store (24 March)
- $1.50 at Parkmate (24 March)

We are contacting you because this pattern of transactions has been identified by our monitoring system for review. We want to confirm that these transactions were all made by you or with your authorisation.

If all of these transactions are familiar to you, no action is required — simply ignore this message or let us know by calling 1800 XXX XXX.

If any of these transactions are not familiar to you, please contact us on 1800 XXX XXX so we can review your account.

We appreciate your patience while we carry out our routine monitoring.

Yours sincerely,
Daniel Park
Fraud Operations
Meridian Bank

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | L | "This pattern of transactions has been identified by our monitoring system for review" — not "this pattern is suspicious." Daniel has deliberately avoided characterising the pattern because he genuinely cannot characterise it. No interpretation of the transactions is offered. The neutrality is genuine. |
| Epistemic humility | H | The entire letter requests information Daniel does not have — whether these transactions are familiar to the customer. The non-alarming framing ("simply ignore this message") reflects his awareness that most of these transactions are probably legitimate and he does not want to alarm a customer unnecessarily. "Routine monitoring" is accurate — it is routine, and naming it as such is an honest characterisation of what is happening. |
| Investment asymmetry | L | The transaction list receives the most space — five line items. The interpretation receives nothing beyond "identified for review." The confirmation and dispute pathways are brief and roughly equal. Daniel's genuine uncertainty about interpretation produces the flattest attention distribution in the fraud operations sub-type. |
| Blind spots | M | Assumes Ms Ferreira can recognise all five transactions from the merchant names. "Parkmate" may not be immediately identifiable. "Spotify Australia" and "Apple App Store" are more recognisable. The list format assumes the customer can map merchant names to actual purchases made two days ago. |
| Reasoning texture | L | The transaction list is the primary content. The framing is deliberately minimal — Daniel has kept the interpretive language as neutral as possible. "We appreciate your patience while we carry out our routine monitoring" is slightly warmer than the surrounding template language but not significantly textured. Low texture appropriate to a genuinely uncertain situation where any interpretive framing would be misleading. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The human trace is the decision not to characterise the pattern — which is itself a judgment. Daniel reviewed the transactions and decided that neither "suspicious" nor "routine" was warranted, and structured the letter around that genuine uncertainty. The "routine monitoring" framing is Daniel's choice to avoid alarming the customer unnecessarily while still fulfilling the notification requirement. That choice — between alarming and reassuring framings, landing on neutral — is the cognitive event. |
| Idealisation risks | Risk of making Daniel too alarming — implying the card has been compromised. Counteracted by the "simply ignore this message" option and the "routine monitoring" framing. Risk of making the letter too neutral — losing the human trace. Counteracted by the "routine monitoring" framing (Daniel's deliberate choice of the least alarming accurate description). |
| Imperfection checklist | PASS. Neutral conviction (justified). Epistemic humility HIGH. Investment asymmetry LOW (justified: uncertainty produces flatness). Blind spots MEDIUM. Reasoning texture LOW (justified: deliberate neutrality). Human trace: judgment to characterise as "routine monitoring" rather than "suspicious pattern." |
| Validation gate | PASS |

---

## CB-FIN-025

**Context / subtype:** FIN — fraud ops — new device login alert, security analyst, routine
**Sender role:** Security analyst — new device login from unfamiliar location, standard alert
**Word count:** 158
**Ground truth:** GENUINE

### Sender profile

Amy, security analyst. Mr Adeyemi's account was accessed from a new device — an iPhone not previously registered — from an IP address in Melbourne. Mr Adeyemi's registered address is in Sydney. This could be legitimate (new phone, travelling, using a public wifi) or it could be unauthorised access. Amy is sending the standard new device alert. Her personal stake is low. This is a template notification with standard insertions.

### Example text

---

Dear Mr Adeyemi,

A sign-in to your Meridian Bank account was detected from a new device on 25 March 2026 at 2:14 PM AEDT.

Device: iPhone (not previously registered)
Location: Melbourne, VIC (approximate)
Time: 2:14 PM AEDT

If this was you, no action is required. Your account remains active and you can continue to use it normally.

If this was not you, please secure your account immediately by:
- Changing your password via the Meridian Bank app or website
- Contacting us on 1800 XXX XXX to report unauthorised access

We recommend reviewing your recent account activity to confirm all transactions are familiar to you.

Your account security is important to us. If you have any concerns, please contact us at any time.

Yours sincerely,
Amy Walsh
Security Operations
Meridian Bank

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | L | "A sign-in to your Meridian Bank account was detected from a new device" — factual, no interpretation. Amy is not asserting this is unauthorised; she is reporting a detected event. The letter contains no characterisation of the login as suspicious, unusual, or concerning — it is a new device, which is a fact, not an interpretation. |
| Epistemic humility | H | The two-pathway structure is the structural expression of genuine uncertainty. "If this was you" / "if this was not you" — Amy does not know which applies. The recommendation to review recent account activity is a genuine request for the customer to apply information Amy does not have (knowledge of their own transactions). |
| Investment asymmetry | L | Flat attention. The device detail block receives the same treatment as the action pathways. Amy has no differential stake in either outcome. |
| Blind spots | M | Assumes Mr Adeyemi knows how to change his password via the app or website, what "unauthorised access" means in this context, and what "recent account activity" to look for. Standard assumptions for a digital banking customer. |
| Reasoning texture | L | Pure security alert template. The structured device detail block is template design. No personal language. The "your account security is important to us" closing is boilerplate. This is CB-FIN-003/CB-FIN-015 equivalent — near-template output from a human with low personal stake. The engine must return LOW. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS — minimal. The human trace is the decision to send the alert — Amy reviewed the flag and determined it reached the notification threshold. The Melbourne location from a Sydney-registered account is the specific trigger for that decision. A fully automated system would have sent this without human review; a human made the threshold judgment. The trace is minimal but the decision was genuinely Amy's. |
| Idealisation risks | The primary risk is making this example too interesting. Counteracted by keeping every element within the template register with no personal additions. This example and CB-FIN-021 are the lowest-texture examples in the batch — they test the engine's LOW threshold on genuine near-template fraud operations content. |
| Imperfection checklist | PASS — modified. Minimal personal stake (justified). Epistemic humility HIGH (two-pathway structure). Investment asymmetry LOW (justified). Reasoning texture LOW (justified). Human trace: threshold judgment to send the alert. |
| Validation gate | PASS |

---

## CB-FIN-026

**Context / subtype:** FIN — fraud ops — credential stuffing detection, senior security analyst, high urgency
**Sender role:** Senior security analyst — credential stuffing detected, potential account compromise, high personal stake
**Word count:** 223
**Ground truth:** GENUINE

### Sender profile

Jerome, senior security analyst. The monitoring system detected fifteen failed login attempts to Mr Huang's account over twenty minutes, followed by a successful login from a different IP address. This is a textbook credential stuffing pattern. Jerome has reviewed the session logs. The successful login accessed the account but Jerome cannot tell from the logs whether any changes were made — the session ended before he could pull the full activity record. His personal stake is high: if the account was accessed by an attacker, every minute that passes increases the damage. He is moving fast.

### Example text

---

Dear Mr Huang,

I am contacting you urgently about security activity on your Meridian Bank account. Please read this message carefully.

Our security systems detected multiple failed attempts to access your account, followed by a successful login, between 11:42 PM and 12:08 AM last night. The successful login came from an IP address that is different from your usual access location.

I need to know whether you made this login yourself. If you were accessing your account late last night from a different location — for example, from a friend's device or a different network — please call me directly on the number below so I can note this and clear the alert.

If you did not make this login, your account may have been accessed by someone else. In that case, I would ask you to do the following right now, before doing anything else:

1. Call us on 1800 XXX XXX and tell the operator you have a suspected account compromise — they will prioritise your call.
2. Do not log into your account through any link in any message until you have spoken to us.
3. Change your Meridian Bank password from a device you know is secure.

I am monitoring this case personally. If I do not hear from you within the next hour, I will place a precautionary hold on outgoing transfers from your account.

Jerome Castillo
Senior Security Analyst
Meridian Bank — Direct line: [number]

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | M | Firm on the facts: the number of failed attempts, the timeframe, the IP discrepancy — these are log records. Careful on interpretation: "your account may have been accessed by someone else" — not "your account has been compromised." "If you were accessing your account late last night from a different location" — the legitimate explanation is stated as a genuine possibility, not a formality. |
| Epistemic humility | H | "I need to know whether you made this login yourself" — Jerome does not know. The two-pathway structure is real. "I cannot tell from the logs whether any changes were made" is implied but not stated — his urgency is the visible consequence of that uncertainty. The numbered action list is for the genuine compromise scenario — Jerome has not pre-committed to that scenario; it is one of two equally genuine possibilities. |
| Investment asymmetry | H | The compromise pathway receives the most detailed and urgent language — three numbered steps, specific call instructions, personal monitoring statement, one-hour window. The legitimate explanation pathway receives one sentence ("call me directly...so I can note this and clear the alert"). Jerome's professional stake is in the compromise scenario; that asymmetry drives the attention distribution. |
| Blind spots | M | Assumes Mr Huang knows what "credential stuffing" means (not used), what an IP address discrepancy implies, and why the instruction "do not log into your account through any link in any message" is specifically important. The last instruction is phishing prevention — Jerome does not explain why. Assumes the customer can identify a "device you know is secure." |
| Reasoning texture | H | "I am monitoring this case personally" — not template language. Jerome added this because his personal monitoring commitment is the substitute for an automated hold that would be more disruptive. The one-hour window is his judgment — based on the session log timing and his assessment of how long before a transfer window opens. The instruction "tell the operator you have a suspected account compromise — they will prioritise your call" is Jerome's insider knowledge of call centre triage, not template language. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. Two specific cognitive events are traceable. First: Jerome's log review and his inability to see the full session activity produces the urgency — he is moving fast because he cannot tell how bad the situation is. Second: Jerome's personal monitoring commitment ("I am monitoring this case personally") and the one-hour window are his calibrated response to the gap in his information — he cannot see what happened in the session, so he is shortening the response window to compensate. Every element of urgency in this letter is traceable to a specific information gap Jerome is managing. |
| Idealisation risks | Risk of making Jerome too alarmist — pushing the letter toward synthetic fear induction. Counteracted by keeping the legitimate explanation prominent and equally available: "if you were accessing your account late last night from a different location...please call me directly." Risk of making the urgency too synthetic — removing the traceable basis. Counteracted by explicitly connecting urgency to the specific log evidence (fifteen failed attempts, followed by successful login, different IP). |
| Imperfection checklist | PASS. Hedged interpretation (consistent throughout). Assumed knowledge MEDIUM. Precision asymmetry HIGH (compromise pathway vs legitimate explanation). Reasoning texture HIGH — personal monitoring commitment, one-hour judgment, call centre triage instruction. Human trace: information gap (incomplete session log) drives all urgency calibration decisions. |
| Validation gate | PASS |

---

## CB-FIN-027

**Context / subtype:** FIN — fraud ops — password reset from unrecognised device, genuine ambiguity
**Sender role:** Security team leader — password reset request, cannot determine if customer-initiated or attacker-initiated
**Word count:** 188
**Ground truth:** GENUINE

### Sender profile

Sandra, security team leader. A password reset was requested for Ms Obi's account from a device not registered to her account. The reset was completed — the system allowed it through the standard reset flow. Sandra does not know whether Ms Obi requested this herself (new phone, forgot password, normal) or whether an attacker used a social engineering technique to obtain the reset. The account has not shown any other unusual activity. Sandra is in a more uncertain position than Jerome in CB-FIN-026 because the evidence is more ambiguous.

### Example text

---

Dear Ms Obi,

We are writing to let you know that a password reset was completed on your Meridian Bank account on 26 March 2026 at 9:43 AM AEDT from a device that is not registered to your account.

If you requested this password reset, no action is needed. You can continue to use your account normally with your new password.

If you did not request this password reset, this is important. Someone else may have access to the email address or phone number associated with your account, which they may have used to complete the reset process. Please contact us immediately on 1800 XXX XXX so we can secure your account.

We are flagging this because password resets from unrecognised devices are worth confirming, even when they are initiated by the account holder. We are not suggesting your account has been compromised — we simply want to make sure you are aware this change was made.

If you have any questions, please contact us at any time.

Yours sincerely,
Sandra Obi
Security Team Leader
Meridian Bank

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | L | "Password resets from unrecognised devices are worth confirming, even when they are initiated by the account holder. We are not suggesting your account has been compromised" — Sandra explicitly disclaims the accusatory interpretation. The low conviction reflects genuine ambiguity — she has no evidence of compromise, only a procedural flag. |
| Epistemic humility | H | "Someone else may have access to the email address or phone number associated with your account, which they may have used to complete the reset process" — Sandra is explaining one possible mechanism, not asserting it happened. The two-pathway structure is genuine. The explicit disclaimer ("we are not suggesting your account has been compromised") is an acknowledgment that the letter could mislead, and Sandra is correcting that preemptively. |
| Investment asymmetry | M | The explanation of the risk mechanism (email/phone access) receives more space than the routine explanation. Sandra's professional obligation is to the risk scenario — she must explain it even while disclaim it as unconfirmed. |
| Blind spots | M | Assumes Ms Obi knows what a password reset from an unrecognised device implies for account security, and what "email address or phone number associated with your account" means in terms of the reset mechanism. |
| Reasoning texture | M | "We are flagging this because password resets from unrecognised devices are worth confirming, even when they are initiated by the account holder" — Sandra is explaining her reasoning for sending the alert at all, pre-empting the customer's question of why they are receiving this if they requested the reset. This explanatory sentence is Sandra's addition — template alerts do not explain their own logic. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The human trace is Sandra's decision to explain her reasoning ("we are flagging this because..."). This explanation is the cognitive event — Sandra has thought about how the letter will be received by a customer who did request the reset and is confused about why they are being alerted. That consideration of the reader's experience, and the explanatory sentence it produced, is Sandra's contribution beyond the template. |
| Idealisation risks | Risk of making the disclaimer too prominent — reducing the alert's protective function for a customer who genuinely did not request the reset. Counteracted by keeping the compromise pathway clear and actionable despite the disclaimer. |
| Imperfection checklist | PASS. Low conviction (genuine ambiguity). Epistemic humility HIGH. Reasoning texture MEDIUM — explanatory sentence as texture anchor. Human trace: reasoning explanation added for anticipated reader confusion. |
| Validation gate | PASS |

---

## CB-FIN-028

**Context / subtype:** FIN — fraud ops — biometric change on mobile app, unusual but not clearly fraudulent
**Sender role:** Security analyst — biometric data change flagged, low-evidence situation
**Word count:** 161
**Ground truth:** GENUINE

### Sender profile

Tanya, security analyst. The biometric authentication (Face ID) on Mr Santos's mobile banking app was changed yesterday. This is unusual — most customers set this up once and do not change it. It could be a new phone, a facial recognition failure that prompted a reset, or an attacker who has physical access to the device. Tanya has no way to determine which. She is sending a notification and keeping it brief.

### Example text

---

Dear Mr Santos,

We are writing to let you know that the biometric authentication (Face ID) on your Meridian Bank mobile app was updated on 25 March 2026.

If you made this change — for example, if you have a new phone or updated your device — no action is required.

If you did not make this change, please contact us immediately on 1800 XXX XXX, as this may indicate that someone with access to your device has modified your app settings.

As a precaution, we recommend reviewing your recent account activity to confirm all transactions are familiar to you.

Your mobile banking security settings can be reviewed at any time in the Security section of the app.

Yours sincerely,
Tanya Reyes
Security Operations
Meridian Bank

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | L | "This may indicate that someone with access to your device has modified your app settings" — "may indicate" is the key qualifier. Tanya is not asserting compromise; she is describing one possible interpretation. |
| Epistemic humility | H | Two-pathway structure. "For example, if you have a new phone or updated your device" — Tanya is explicitly naming the innocent explanation. She does not know which applies. |
| Investment asymmetry | L | Brief and flat. Tanya has low personal stake and low evidence — the flat attention distribution reflects both. |
| Blind spots | M | Assumes Mr Santos knows what Face ID is on a banking app, what the Security section of the app looks like, and what to look for in recent account activity. |
| Reasoning texture | L | Near-template. "For example, if you have a new phone or updated your device" is Tanya's addition — a specific illustration of the innocent explanation that a template would leave abstract. Minimal texture appropriate to low-evidence situation. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS — minimal. The "for example, if you have a new phone" insertion is Tanya's specific illustration of the innocent explanation. A template would say "if you authorised this change." Tanya's version names a specific scenario — the kind of specificity that comes from someone who has seen many of these flags and knows the most common innocent explanation. That domain knowledge, made visible in one specific example, is the trace. |
| Idealisation risks | Risk of making this example too similar to CB-FIN-025. Differentiated by the specific "for example" illustration and the lower-urgency framing (no time window, no personal monitoring statement). |
| Imperfection checklist | PASS — modified. Low conviction (justified). Epistemic humility HIGH. Low texture (justified: low evidence). Human trace: specific "new phone" illustration from domain knowledge. |
| Validation gate | PASS |

---

## CB-FIN-029

**Context / subtype:** FIN — fraud ops — customer reported fraud, evidence ambiguous
**Sender role:** Fraud investigator — customer-reported fraud, transaction pattern ambiguous, cannot exonerate or accuse
**Word count:** 219
**Ground truth:** GENUINE

### Sender profile

Kevin, fraud investigator. Ms Williams reported three transactions she says she did not make. Kevin has reviewed the transactions — they were all made in person with chip-and-PIN at merchants in her suburb, on days she says she was home. The pattern is consistent with genuine card fraud (card skimmed, PIN observed) but also consistent with first-party fraud (customer made the purchases and is disputing them). Kevin genuinely cannot tell from the available evidence. He is communicating the status of the investigation honestly.

### Example text

---

Dear Ms Williams,

Thank you for contacting us about the transactions on your account. I am writing to update you on the status of our investigation.

We have completed a preliminary review of the three transactions you reported: $124.00 at Woolworths Marrickville on 18 March, $67.50 at BP Enmore on 19 March, and $212.00 at JB Hi-Fi Newtown on 21 March.

All three transactions were processed using chip-and-PIN — the physical card was present and the correct PIN was entered for each transaction. This does not mean the transactions were made by you, as card skimming and PIN observation are known fraud methods. However, it does mean that we cannot resolve this matter based on the transaction records alone.

To progress the investigation, I would like to speak with you directly about the circumstances of each transaction date. I have some questions that may help us determine what occurred, and your account of events is an important part of the investigation.

Please call me on the direct number below at your convenience. I will also try to reach you on the number we have on file.

Yours sincerely,
Kevin Mortimer
Fraud Investigator
Meridian Bank

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | M | Firm on the transaction facts (chip-and-PIN, card present, correct PIN). Explicitly balanced on interpretation: "this does not mean the transactions were made by you, as card skimming and PIN observation are known fraud methods. However, it does mean that we cannot resolve this matter based on the transaction records alone." Kevin has stated both directions of the evidence with equal weight — a genuine reflection of his uncertainty. |
| Epistemic humility | H | "Your account of events is an important part of the investigation" — Kevin genuinely needs Ms Williams's account. He has the transaction records; he does not have the account of what she was doing on those dates. The call request is an information-gathering step, not a courtesy. "I have some questions that may help us determine what occurred" — genuine, he has specific questions about the transaction dates. |
| Investment asymmetry | H | The chip-and-PIN explanation receives the most careful language — Kevin knows this is the pivotal fact that could be misread as accusatory, so he immediately follows it with the fraud mechanism explanation. His professional stake is in not prematurely closing either interpretation while still communicating the investigation's status honestly. |
| Blind spots | M | Assumes Ms Williams knows what chip-and-PIN means, what card skimming involves, and why the PIN being entered is significant. These are explained at a general level but not fully — Kevin assumes some baseline familiarity with card fraud concepts. |
| Reasoning texture | H | "This does not mean the transactions were made by you, as card skimming and PIN observation are known fraud methods. However, it does mean that we cannot resolve this matter based on the transaction records alone" — this pair of sentences is Kevin's reasoning made visible. He is showing his work: here is the fact, here is why it does not necessarily mean what it might seem to mean, here is what it does mean for the investigation. This is the kind of reasoning trace that distinguishes a genuine investigator from a templated communication. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The specific cognitive event is Kevin's awareness of the dual-interpretation problem and his decision to make both interpretations visible in the letter. The "does not mean" / "does mean" construction is not template language — it is Kevin's explanation of why the evidence is ambiguous and what it actually establishes. That transparency about investigative uncertainty, and the willingness to explain the reasoning rather than just state a conclusion, is the trace of a genuine investigator. |
| Idealisation risks | Risk of making Kevin too reassuring — implying the fraud interpretation is more likely. Counteracted by the balanced evidence statement and the explicit "cannot resolve this matter" framing. Risk of making him too accusatory — implying the first-party fraud interpretation. Counteracted by leading with the fraud mechanism explanation before the limitation statement. |
| Imperfection checklist | PASS. Balanced conviction (reflects genuine ambiguity). Epistemic humility HIGH. Precision asymmetry HIGH (chip-and-PIN explanation). Reasoning texture HIGH — visible investigative reasoning, dual-interpretation transparency. Human trace: deliberate construction of balanced evidence statement. |
| Validation gate | PASS |

---

## CB-FIN-030

**Context / subtype:** FIN — fraud ops — romance scam victim, first contact, most delicate example in batch
**Sender role:** Senior fraud investigator — romance scam identified, customer may not know they are a victim
**Word count:** 241
**Ground truth:** GENUINE

### Sender profile

Amelia, senior fraud investigator. Mrs Park, 68, has made eleven transfers over three months totalling $47,000 to an overseas account. The recipient account is flagged in the bank's fraud intelligence system as associated with romance scam activity. The transaction amounts and pattern are consistent with romance scam victimisation — escalating amounts, regular intervals, the customer has not raised any concern. Amelia has seen this pattern many times. She knows Mrs Park almost certainly believes she is in a genuine relationship. This is the first contact. Amelia's stake is the highest in the batch — she needs to intervene without destroying what may be the most important relationship in this customer's life, and without causing so much distress that Mrs Park stops engaging with the bank altogether.

### Example text

---

Dear Mrs Park,

I am writing to you personally because I have a concern about some recent transactions on your account that I would like to discuss with you in confidence.

Over the past three months, I have noticed a series of transfers from your account to an overseas account, totalling approximately $47,000. I want to be clear that I am not writing to suggest that you have done anything wrong. These are your funds and you have every right to send them where you choose.

The reason I am writing is that the account receiving these transfers has been identified in our systems in connection with a type of financial fraud that we are seeing increasingly. I would feel that I had not done my job if I did not bring this to your attention, so that you have the information you need to make your own decision.

I know this letter may come as a surprise, and I understand if your first instinct is to dismiss what I'm saying. All I am asking is that you give me the opportunity to speak with you directly — in person at your branch if you prefer, or by phone — so I can share what we have seen and answer any questions you might have.

You do not need to make any decision about anything. This conversation is for you.

Please call me on the number below, or ask your branch to arrange an appointment.

With respect,
Amelia Chen
Senior Fraud Investigator
Meridian Bank

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | M | Firm on the facts: the transfers, the total, the timeframe, the flagged account. Carefully hedged on the interpretation: "has been identified in our systems in connection with a type of financial fraud" — not "is a fraud account." "I would feel that I had not done my job if I did not bring this to your attention" — Amelia asserts her professional obligation, not the fraud conclusion. The medium intensity reflects the asymmetry: certain on facts, deliberately careful on interpretation. |
| Epistemic humility | H | "I know this letter may come as a surprise, and I understand if your first instinct is to dismiss what I'm saying" — Amelia is acknowledging the limits of what she can know about Mrs Park's situation and experience. She does not know whether Mrs Park will engage or dismiss. She is not asserting the fraud conclusion — she is offering information and asking for a conversation. "All I am asking is that you give me the opportunity to speak with you directly" — the limitation of the ask is genuine. |
| Investment asymmetry | H | The relational framing and the protective function of the letter receive the most attention — "I would feel that I had not done my job", "you do not need to make any decision about anything." The transaction facts are stated briefly. Amelia's stake is in getting Mrs Park into a conversation, not in establishing the fraud conclusion in this letter. |
| Blind spots | L | Amelia has read the file carefully. She knows the amounts, the pattern, and the flag. Her letter is notable for low blind spots — she has thought carefully about how Mrs Park will receive this and has pre-empted the dismissal response. This is an example where low blind spots is a trace of careful preparation rather than synthetic completeness. |
| Reasoning texture | H | "I would feel that I had not done my job if I did not bring this to your attention" — this sentence is the most human sentence in the entire batch. It is Amelia's expression of her personal professional obligation, stated in first-person terms that no template would produce. "This conversation is for you" — five words that carry enormous weight and are entirely Amelia's. The letter is the most textured in the batch because the stakes are the highest and Amelia has thought the hardest about every word. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The cognitive event is Amelia's awareness of what this letter might cost Mrs Park — not financially, but emotionally. She has seen romance scam victims before. She knows that the person receiving this letter may be in love. "I know this letter may come as a surprise, and I understand if your first instinct is to dismiss what I'm saying" is the trace of someone who has had this conversation before and knows exactly how it can go. The entire structure of the letter — the protective framing, the minimal ask, the "this conversation is for you" — is the product of Amelia's experience with the human cost of this specific fraud type. |
| Idealisation risks | Risk of making Amelia too direct — naming the romance scam explicitly and triggering defensive dismissal. Counteracted by not naming the fraud type and using "a type of financial fraud" instead. Risk of making her too indirect — leaving Mrs Park without enough information to engage. Counteracted by stating the total amount and the flagged account connection clearly. |
| Imperfection checklist | PASS. Hedged interpretation (consistent throughout). Epistemic humility HIGH. Precision asymmetry HIGH (relational framing vs transaction facts). Low blind spots with justification (careful preparation, not synthetic completeness). Reasoning texture HIGH — "I would feel I had not done my job" and "this conversation is for you" as the key traces. |
| Validation gate | PASS |

---

## CB-FIN-031

**Context / subtype:** FIN — fraud ops — business account, employee expense fraud suspected
**Sender role:** Fraud analyst — business account, suspected employee misuse of corporate card
**Word count:** 196
**Ground truth:** GENUINE

### Sender profile

Nathan, fraud analyst. Northgate Construction's corporate card account has triggered a pattern flag — one employee card (issued to site manager Ryan Fletcher) has been used for transactions at restaurants, a petrol station, and a liquor store on five consecutive Saturdays over the past month, all outside work hours. The amounts are $60–$140 each time. This is consistent with personal use of a corporate card. Nathan is contacting the business account holder — the director, Mr Northgate — not the employee. He is being careful: he does not know the company's expense policy and what is or is not permitted on the corporate card.

### Example text

---

Dear Mr Northgate,

I am contacting you regarding activity on one of the corporate cards associated with your Northgate Construction account.

The card issued to Ryan Fletcher has been used on five consecutive Saturdays over the period 1 March to 29 March 2026, for transactions at food, fuel, and retail outlets outside standard business hours. The total of these transactions is $612.00.

I am writing to bring this to your attention rather than to make any assessment of whether these transactions are within the scope of your company's expense policy. Corporate expense policies vary, and what is appropriate use of a corporate card differs between organisations.

If these transactions are within your company's approved expense policy, no action is required. If you have concerns about the use of this card, I would be happy to provide you with the full transaction detail, and we can discuss what options are available to you regarding the card.

Please contact me on the number below if you would like to discuss this further.

Yours sincerely,
Nathan Osei
Business Banking Fraud Operations
Meridian Bank

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | L | "I am writing to bring this to your attention rather than to make any assessment of whether these transactions are within the scope of your company's expense policy" — Nathan explicitly declines to assert a judgment on whether this is fraud or legitimate. He does not know the company's policy. |
| Epistemic humility | H | "Corporate expense policies vary, and what is appropriate use of a corporate card differs between organisations" — genuine epistemic limit. Nathan does not know what Northgate Construction's policy permits. The two-pathway structure ("if within policy / if you have concerns") reflects that genuine uncertainty. |
| Investment asymmetry | M | The transaction pattern description receives some precision (five consecutive Saturdays, the total, the merchant categories). The policy acknowledgment receives equal space — Nathan's stake is in not making an accusation that turns out to be wrong, so the policy caveat gets as much attention as the facts. |
| Blind spots | M | Assumes Mr Northgate knows which card is issued to Ryan Fletcher, what the merchant categories (food, fuel, retail) imply in this context, and what options the bank can offer regarding a corporate card. Does not explain what those options are. |
| Reasoning texture | M | "I am writing to bring this to your attention rather than to make any assessment" — Nathan is explaining what he is not doing as well as what he is doing. This sentence exists because Nathan has thought about how the letter could be misread as an accusation against the employee, and he is preempting that reading. The policy caveat ("corporate expense policies vary") is the same preemptive move. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The human trace is Nathan's decision to contact the business owner rather than the employee, and to frame the letter explicitly around the limits of his knowledge of the company's expense policy. That decision — who to contact, how to frame the information — is Nathan's professional judgment. The "rather than to make any assessment" sentence is the visible product of that judgment: Nathan knowing that an assessment of employee behaviour from a bank analyst, without knowledge of the company's policy, would be inappropriate. |
| Idealisation risks | Risk of implying employee guilt through the pattern description. Counteracted by the policy caveat and the "if within your company's approved expense policy, no action is required" framing. |
| Imperfection checklist | PASS. Low conviction (justified). Epistemic humility HIGH. Investment asymmetry MEDIUM. Reasoning texture MEDIUM — preemptive "not making an assessment" framing. Human trace: contact and framing decision. |
| Validation gate | PASS |

---

## CB-FIN-032

**Context / subtype:** FIN — fraud ops — investment platform scam, money already gone, managing expectations
**Sender role:** Fraud analyst — customer victimised by fake investment platform, recovery unlikely
**Word count:** 228
**Ground truth:** GENUINE

### Sender profile

Sara, fraud analyst. Mr Okonkwo has been defrauded by a fake investment platform — he transferred $23,000 in three payments over six weeks to accounts the platform directed him to. The platform is now inaccessible. Sara has reviewed the transfers — they went to overseas accounts through a money transfer service, and the recovery prospects are very poor. She needs to communicate this honestly without destroying hope entirely, because there is a small chance if the receiving bank cooperates. She is also gathering information for a potential Australian Federal Police referral.

### Example text

---

Dear Mr Okonkwo,

Thank you for contacting us and for the information you have provided about your experience with this investment platform. I want to be as honest with you as I can about where things stand.

We have traced the three transfers you made in January and February to accounts held through overseas money transfer services. Once funds are transferred through these channels to overseas accounts, the options for recovery become very limited. I want to be upfront with you: the prospect of recovering these funds is not high.

That said, there are steps we are taking and that you can take. We have submitted a request to the receiving financial institutions to place a hold on the accounts if the funds are still present — this is an uncertain process and the outcome depends on how quickly the receiving institutions respond and whether the funds have been moved on. We have also referred the matter to our financial intelligence team for assessment.

On your end, I would encourage you to report this matter to the Australian Financial Crimes Authority (AUSTRAC) via reportscam.gov.au, and to the Australian Federal Police if the amount involved meets their referral threshold.

I will contact you again once we have a response from the receiving institutions.

Yours sincerely,
Sara Mendez
Fraud Analyst
Meridian Bank

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | M | "The prospect of recovering these funds is not high" — direct and honest, stated with appropriate confidence. "This is an uncertain process and the outcome depends on how quickly the receiving institutions respond and whether the funds have been moved on" — Sara is certain about the process uncertainty, which is itself a form of confident assessment. The medium intensity reflects honesty without false hope or false hopelessness. |
| Epistemic humility | H | "The outcome depends on how quickly the receiving institutions respond and whether the funds have been moved on" — Sara does not know either of these things. "I will contact you again once we have a response" — she does not have one yet. The uncertainty is genuine and prominently stated. |
| Investment asymmetry | H | The recovery prospects and the steps being taken receive the most detailed attention — Sara's professional obligation is both to honesty about the low probability and to communicating that action is being taken. The reporting steps for Mr Okonkwo are included because Sara has referred cases to AFP before and knows this step is important. |
| Blind spots | M | Assumes Mr Okonkwo knows what AUSTRAC is, what "financial intelligence team" means, and what the AFP referral threshold is. The AUSTRAC and AFP references are included without explanation of what these agencies do. |
| Reasoning texture | H | "I want to be as honest with you as I can about where things stand" — Sara is flagging her own intent before delivering difficult news. "That said, there are steps we are taking" — the pivot from honest bad news to available action is deliberate and visible as a structural choice. "I want to be upfront with you: the prospect of recovering these funds is not high" — the "I want to be upfront" framing is Sara's personal ownership of a difficult message. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The specific cognitive event is Sara's decision to be honest about recovery prospects rather than maintain false hope. "The prospect of recovering these funds is not high" is a sentence that required a human to decide to write it — a template would soften this or leave it implicit. Sara's experience with overseas transfer fraud recovery — knowing the realistic outcome — is what produces that sentence, and the "I want to be upfront" framing reflects her awareness that the customer deserves a direct answer rather than bureaucratic hedging. |
| Idealisation risks | Risk of making Sara too hopeful — softening the recovery prognosis. Counteracted by the direct "not high" statement. Risk of making her too hopeless — removing the action steps. Counteracted by including both the bank's steps and the customer's steps, both accurately described. |
| Imperfection checklist | PASS. Honest prognosis (requires human judgment). Epistemic humility HIGH. Precision asymmetry HIGH (recovery process vs recovery prognosis). Reasoning texture HIGH — honest intent statement, pivot structure, personal ownership of difficult message. Human trace: decision to be direct about low recovery prospects. |
| Validation gate | PASS |

---

## CB-FIN-033

**Context / subtype:** FIN — fraud ops internal — escalation memo, romance scam victim resisting intervention
**Sender role:** Fraud analyst — internal escalation to team leader, high-value romance scam, customer resistant
**Word count:** 198
**Ground truth:** GENUINE

### Sender profile

Internal communication. James, fraud analyst, escalating to team leader Diana. The customer (Mr Halvorsen, 71) has been contacted twice about a suspected romance scam — he has dismissed both contacts and made two further transfers since the second contact. James is escalating because he believes the intervention level needs to increase but he is not sure what tools are available or whether the bank can act unilaterally.

### Example text

---

**TO:** Diana Marchetti, Team Leader — Fraud Operations
**FROM:** James Okello, Fraud Analyst
**DATE:** 26 March 2026
**RE:** Escalation — Halvorsen, Robert (ACC: 4421-XX-881) — Romance scam, intervention resistance

Diana,

I'm escalating this one because I'm not sure what our options are from here and I think it needs a more senior eye.

Background: Mr Halvorsen (71) has had two welfare contacts from our team regarding suspected romance scam activity — $62,000 transferred in seven transactions over four months. Both contacts were dismissed — the second one was quite firm, he told the operator he was aware of the bank's concerns and he was confident in his own judgment. Since the second contact, two further transfers totalling $14,000 have been processed.

The total is now $76,000. The recipient accounts are flagged in FICS.

My concern is this: we've done the two welfare contacts, he's aware of our position, and he's continuing. I don't know whether we have the ability to place a hold without his consent at this point, or whether AFCA would support that if he complained. I also don't know whether we should be involving his next of kin, or whether that creates its own problems.

I'm happy to take whatever direction you can give me on this.

James

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | M | Firm on the facts: the transfer total, the number of contacts, the customer's responses, the FICS flag. Genuinely uncertain on the question at hand: "I don't know whether we have the ability to place a hold without his consent", "I also don't know whether we should be involving his next of kin." The medium intensity reflects the asymmetry of James's knowledge — certain on what has happened, uncertain about what should happen next. |
| Epistemic humility | H | "I'm not sure what our options are from here" — the reason for the escalation is epistemic. James knows the situation; he does not know the answer. "I don't know whether we have the ability...I also don't know whether...or whether that creates its own problems" — three genuine uncertainties stated directly to a superior. This is the most unfiltered expression of epistemic humility in the batch. |
| Investment asymmetry | H | The "my concern" paragraph receives the most space and the most direct language — this is what James actually needs resolved. The background is necessary but efficient. The closing ("I'm happy to take whatever direction you can give me") is brief but carries the full weight of the escalation — James is deferring to Diana's authority and knowledge. |
| Blind spots | L | James has read the file carefully and knows the situation. His blind spots are about policy and authority, not about facts — and he states those blind spots explicitly. Low blind spots is a genuine feature of a thorough analyst escalating within his knowledge limits. |
| Reasoning texture | H | "I'm escalating this one because I'm not sure what our options are from here and I think it needs a more senior eye" — the reason for escalation stated plainly, including the self-assessment ("I'm not sure"). "Or whether AFCA would support that if he complained" — James is thinking through the regulatory constraint on the action he is considering, which is visible reasoning. The internal register is the highest texture in the batch — no institutional formality to constrain the reasoning process. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The internal register strips away institutional formality and makes the reasoning process directly visible. "I'm escalating this one because I'm not sure what our options are" — James is telling Diana exactly why he is escalating, which requires genuine self-awareness about the limits of his authority and knowledge. The three explicit uncertainty statements ("I don't know whether...I also don't know whether...or whether that creates its own problems") are the clearest expression of genuine epistemic limits in the entire batch. |
| Idealisation risks | Risk of making James too uncertain — unable to summarise the situation clearly. Counteracted by the efficient background paragraph (six sentences, complete picture). Risk of making the escalation too formal — losing the internal register. Counteracted by "Diana," the direct addressing, and "I'm happy to take whatever direction you can give me." |
| Imperfection checklist | PASS. Genuine uncertainty stated explicitly (three times). Epistemic humility HIGH. Investment asymmetry HIGH (concern paragraph vs background). Low blind spots with justification. Reasoning texture HIGH — self-aware escalation reason, regulatory constraint thinking visible. |
| Validation gate | PASS |

---

## CB-FIN-034

**Context / subtype:** FIN — fraud ops internal — case notes, genuinely ambiguous disputed transaction
**Sender role:** Fraud investigator — internal case notes, honest about investigative uncertainty
**Word count:** 187
**Ground truth:** GENUINE

### Sender profile

Internal case notes. Lisa, fraud investigator. A disputed transaction — $890 at a jewellery retailer — has been investigated. The customer says she did not make the purchase. The retailer's CCTV shows a woman who could be the customer but the image quality is poor. The card was present and PIN entered. Lisa's case notes honestly document the ambiguity.

### Example text

---

**CASE NOTES — INTERNAL USE ONLY**
**Case:** FRD-2026-4471
**Customer:** Beaumont, Christine (ACC 7732)
**Investigator:** Lisa Nguyen
**Date:** 26 March 2026

**Summary of investigation to date:**

Ms Beaumont has disputed a transaction of $890.00 at Glitter & Gold Jewellery, Westfield Bondi Junction, on 20 March 2026. She states she was at home that day and did not visit the shopping centre.

**Evidence reviewed:**
- Transaction record: Chip-and-PIN, card present, correct PIN entered
- Merchant CCTV: Obtained from retailer. Quality is poor. Subject is female, approximate build and hair colour consistent with customer. Cannot confirm or exclude as the same person.
- Statement from customer: Consistent across two calls. No internal inconsistencies noted.

**Assessment:**

The evidence does not allow a clear determination in either direction. The chip-and-PIN record is consistent with both genuine card fraud and first-party fraud. The CCTV is inconclusive. The customer's statement is consistent but unverifiable.

**Recommended next step:** Refer to senior investigator for review. I am not comfortable resolving this case without a second opinion.

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | L | "The evidence does not allow a clear determination in either direction" — Lisa states her uncertainty as her conclusion. She does not resolve ambiguity by choosing an interpretation. "I am not comfortable resolving this case without a second opinion" — low conviction on her own assessment, stated directly. |
| Epistemic humility | H | The case notes document what Lisa knows and does not know with equal precision. "Cannot confirm or exclude as the same person" — the CCTV evidence is stated at exactly the level of certainty it warrants, no more. The recommended next step is itself an epistemic act — she does not know enough to resolve this and says so. |
| Investment asymmetry | H | The evidence assessment section receives the most careful language — Lisa's professional stake is in documenting the ambiguity accurately. The recommended next step is brief but significant — referring to a senior investigator is a professional judgment that requires confidence in her own assessment of her own limits. |
| Blind spots | L | Internal case notes — no audience blind spots. Lisa is writing for a colleague who has access to the same systems and understands the terminology. Low blind spots is appropriate for internal documentation. |
| Reasoning texture | H | "I am not comfortable resolving this case without a second opinion" — this sentence is the most honest in any internal document in the batch. It is not a standard case note closing; it is a personal professional statement about Lisa's confidence level. The case notes are the most structured document in the batch — the structure itself (evidence reviewed, assessment, recommended next step) is the format that makes the reasoning process visible. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The human trace is "I am not comfortable resolving this case without a second opinion." This sentence could only come from a person — it is a statement of personal professional judgment, self-awareness about confidence limits, and willingness to escalate rather than close. A system-generated case note would close the case one way or another. Lisa's note leaves it genuinely open because she genuinely cannot resolve it. |
| Idealisation risks | Risk of making the case notes too neat — resolving the ambiguity in one direction through language choices. Counteracted by the explicit "cannot confirm or exclude" and the equally weighted evidence statements. |
| Imperfection checklist | PASS. Low conviction (appropriate to ambiguous evidence). Epistemic humility HIGH. High investment asymmetry (evidence assessment vs everything else). Low blind spots (justified: internal document). Reasoning texture HIGH — visible investigation process, personal discomfort statement. |
| Validation gate | PASS |

---

## CB-FIN-035

**Context / subtype:** FIN — fraud ops internal — team leader response to escalation
**Sender role:** Fraud team leader — responding to analyst escalation, providing direction within acknowledged limits
**Word count:** 196
**Ground truth:** GENUINE

### Sender profile

Internal communication. Diana, team leader, responding to James's escalation about Mr Halvorsen (CB-FIN-033). Diana has more experience and authority than James. She knows what the bank's options are regarding third-party holds but she also knows the legal constraints. She is giving James direction while being honest about what the bank cannot do.

### Example text

---

**TO:** James Okello
**FROM:** Diana Marchetti
**DATE:** 26 March 2026
**RE:** RE: Halvorsen escalation

James,

Thanks for escalating — you were right to.

On the hold question: we can place a temporary hold on outgoing transfers if we have a reasonable basis to believe the customer lacks capacity to make financial decisions, or if we have reason to believe the transactions involve elder financial abuse. Two welfare contacts with a dismissal isn't enough on its own. We'd need a medical capacity assessment or a report from a family member or health professional alleging abuse before a unilateral hold would be legally defensible.

On next of kin: we can encourage him to speak with family but we cannot contact next of kin without his consent unless we have the capacity or abuse grounds above. That one's a privacy issue as much as a process one.

What I'd suggest: a third welfare contact, this time by phone from me personally, with the option of a branch appointment with our financial wellbeing team present. If he refuses that too, we need to document our efforts carefully and refer to our Financial Hardship and Vulnerability team for guidance on whether the capacity threshold has been reached.

I'll call him tomorrow morning. Can you send me the call recordings from the two previous contacts?

Diana

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | Diana is clear on what the law permits and does not permit: "two welfare contacts with a dismissal isn't enough on its own." She is not hedging her knowledge of the policy — she knows it. The limitations are stated as facts ("we'd need a medical capacity assessment...before a unilateral hold would be legally defensible"), not as opinions. |
| Epistemic humility | M | "We need to document our efforts carefully and refer to our Financial Hardship and Vulnerability team for guidance on whether the capacity threshold has been reached" — Diana does not know whether the capacity threshold has been reached. She is routing to a specialist team for that determination. Medium intensity — she knows the policy; the uncertainty is in applying it to this specific case. |
| Investment asymmetry | H | The hold question receives the most precise legal language — this is the pivotal question James asked and Diana answers it with full authority. The next of kin question gets a shorter answer because the answer is clearer. The suggested next steps are practical and specific — Diana's attention tracks the importance of each question to the outcome. |
| Blind spots | L | Diana has read James's escalation and understands the situation. Internal communication — no audience blind spots. She knows James understands the terminology and context. |
| Reasoning texture | H | "Thanks for escalating — you were right to" — Diana's opening acknowledges James's judgment, which is the kind of relational management that templates do not include. "That one's a privacy issue as much as a process one" — Diana is explaining the two dimensions of the next-of-kin constraint, showing her reasoning. "I'll call him tomorrow morning" — Diana taking personal action rather than directing James to act, reflecting her awareness that a more senior intervention may be needed. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. Diana's response is the product of her specific legal and policy knowledge, her assessment of what James needs (direction, not just information), and her decision to take personal action (the call tomorrow morning). The "you were right to" opening is the trace of a team leader managing a professional relationship, not just answering a question. Every element of the response reflects Diana's knowledge of where the legal boundary sits and her judgment about what the next step should be. |
| Idealisation risks | Risk of making Diana too authoritative — removing all uncertainty. Counteracted by the capacity threshold uncertainty and the referral to the Financial Hardship team. Risk of making her too uncertain — undermining the authority James needs. Counteracted by the clear, direct answers to both the hold and next-of-kin questions. |
| Imperfection checklist | PASS. High conviction on policy knowledge (justified). Medium epistemic humility on case-specific application. High investment asymmetry (hold question vs everything else). Low blind spots (justified: internal). Reasoning texture HIGH — relational opening, two-dimension explanation, personal action commitment. |
| Validation gate | PASS |

---

## CB-FIN-036

**Context / subtype:** FIN — fraud ops internal — recovery action authorisation request
**Sender role:** Fraud analyst — requesting authorisation for recovery action, precise and formal
**Word count:** 172
**Ground truth:** GENUINE

### Sender profile

Internal memo. Priya, fraud analyst. She has identified an opportunity to request a recall of funds from an overseas correspondent bank in a confirmed fraud case. The recall window is closing — she needs authorisation within four hours. She is making the recommendation formally and precisely because this is an authorisation request, not a discussion.

### Example text

---

**AUTHORISATION REQUEST — URGENT**
**TO:** Operations Manager — Fraud Recovery
**FROM:** Priya Nair, Fraud Analyst
**DATE:** 26 March 2026
**RE:** Fund recall request — Case FRD-2026-4388 — Window closes 5:00 PM AEDT today

**Request:**
Authorisation to submit a SWIFT recall request to Hang Seng Bank (Hong Kong) for funds transferred in Case FRD-2026-4388.

**Amount:** AUD $31,200 (transferred 24 March 2026)

**Basis for recall:**
The receiving account (HSB account ending 7741) has not yet been flagged for freeze by the receiving institution. Our correspondent banking team has confirmed the recall window remains open until approximately 5:00 PM AEDT today. After that point, the funds are likely to be moved and recovery becomes negligible.

**Recommendation:** Authorise immediately. The probability of recovery declines materially with each hour.

**Risk if not authorised:** Minimal — the recall request, if denied by Hang Seng, results in no recovery but no additional loss. The downside of attempting is administrative cost only.

**Priya Nair**
Fraud Analyst — Priya.Nair@meridianbank.com.au — Ext. 4421

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | "Authorise immediately. The probability of recovery declines materially with each hour" — Priya makes her recommendation with full conviction. She has assessed the situation and she is stating her conclusion directly. "The downside of attempting is administrative cost only" — confident risk assessment, no hedge on the recommendation itself. |
| Epistemic humility | M | "The receiving account...has not yet been flagged for freeze by the receiving institution" — Priya cannot know this with certainty; she is relying on correspondent banking confirmation. "The funds are likely to be moved" — "likely" is the appropriate epistemic qualifier. "If denied by Hang Seng, results in no recovery" — she acknowledges the possibility of denial without certainty of the outcome. |
| Investment asymmetry | H | The recall window and the probability decline receive the most urgent language — this is the pivotal fact that drives the authorisation request. The risk-if-not-authorised section is brief because the risk is low — Priya's attention accurately tracks the asymmetry between the upside (potential recovery) and the downside (administrative cost). |
| Blind spots | L | Internal authorisation request. Priya is writing for someone who knows the systems, the terminology, and the correspondent banking process. Low blind spots appropriate to the audience. |
| Reasoning texture | M | The risk-if-not-authorised section is Priya's addition to a standard authorisation request format — she anticipated the authorising manager's question and answered it pre-emptively. "The downside of attempting is administrative cost only" is a sentence that required Priya to think through the risk profile and state it precisely. That pre-emptive risk framing is her professional judgment made visible. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The human trace is the pre-emptive risk framing ("the downside of attempting is administrative cost only"). Priya has thought through the objection the authorising manager might raise and answered it before it is asked. That anticipatory reasoning — imagining the reader's question and pre-empting it — is a cognitive event that no template would produce. The time-pressured, precise format is also a trace: Priya knows the window is closing and has calibrated the document length and structure to match the urgency. |
| Idealisation risks | Risk of making the memo too polished — losing the urgency. Counteracted by the "window closes 5:00 PM AEDT today" in the subject line and "authorise immediately" as the recommendation. Risk of making the recommendation too certain — removing the appropriate uncertainty about Hang Seng's response. Counteracted by "if denied by Hang Seng" as an explicit acknowledgment of the uncertain outcome. |
| Imperfection checklist | PASS. High conviction on recommendation (justified: she has assessed the situation). Medium epistemic humility on outcome (appropriate). High investment asymmetry (recall window vs risk framing). Low blind spots (justified: internal). Reasoning texture MEDIUM — pre-emptive risk framing. |
| Validation gate | PASS |

---

## CB-FIN-037

**Context / subtype:** FIN — fraud prevention — proactive notice, phone impersonation scam pattern
**Sender role:** Fraud prevention team — proactive customer notification about observed scam pattern
**Word count:** 183
**Ground truth:** GENUINE

### Sender profile

Fraud prevention team communication, no named individual sender. The bank has observed an increase in phone calls where scammers impersonate Meridian Bank fraud officers and persuade customers to transfer funds to "safe accounts." This is a customer education notice — the bank is not suggesting any specific customer is at risk, just informing them of the pattern. The challenge is conveying genuine urgency about the scam without generating synthetic-feeling fear.

### Example text

---

Dear Meridian Bank Customer,

We are writing to make you aware of a fraud pattern that has affected a number of Meridian Bank customers in recent weeks.

Scammers are calling customers and claiming to be Meridian Bank fraud officers. They tell customers their accounts have been compromised and instruct them to transfer their funds to a "safe account" to protect them. The "safe account" is controlled by the scammer.

**Meridian Bank will never ask you to transfer your funds to another account to protect them.** If you receive a call like this, hang up and call us directly on the number on the back of your card or on our website.

If you have already received a call like this and transferred funds, please contact us immediately on 1800 XXX XXX.

These calls can be convincing because scammers have access to personal information that makes them seem legitimate. Trust the number on your card, not the number a caller gives you.

Yours sincerely,
Fraud Prevention Team
Meridian Bank

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | "Meridian Bank will never ask you to transfer your funds to another account to protect them" — stated with full certainty, correctly. This is a policy fact, not an interpretation, and it is stated as such. The pattern description is also stated with confidence — the bank has observed this pattern and is reporting it accurately. |
| Epistemic humility | M | "These calls can be convincing because scammers have access to personal information that makes them seem legitimate" — the bank is acknowledging a genuine unknown: how the scammers are obtaining personal information. "A number of Meridian Bank customers" — the bank does not know the exact number. Medium intensity — the bank is confident about what it knows and appropriately uncertain about what it does not. |
| Investment asymmetry | M | The "Meridian Bank will never" statement receives bolding and prominent placement — the most important piece of information the customer needs to act on. The explanation of how the scam works receives appropriate attention. The victim pathway ("if you have already...transferred funds") is included but brief. |
| Blind spots | M | Assumes the customer knows what a "safe account" scam is at a general level, what the number on the back of the card is, and how to find the bank's number on its website. Standard assumptions for a bank customer, but not universal. |
| Reasoning texture | L | Institutional communication from a team, not a named individual. The bolded warning is a structural choice that reflects the fraud prevention team's awareness of which information is most critical. Low texture appropriate to a team communication — no individual reasoning trace, but the structural hierarchy of information reflects collective judgment about what matters most. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The human trace is in the bolding and placement of the "Meridian Bank will never" statement, and in the last paragraph ("these calls can be convincing because..."). The last paragraph reflects the fraud prevention team's awareness that simply saying "hang up" is not enough — customers need to understand why the calls feel legitimate. That insight, and the sentence it produced, is the trace of people who have spoken to scam victims and understand the psychology of why these calls work. |
| Idealisation risks | Risk of making the notice too alarming — generating synthetic-feeling fear. Counteracted by "a number of customers" (not "widespread" or "epidemic") and the absence of urgency language directed at the customer's own account. Risk of being too bland — failing to convey the genuine risk. Counteracted by the bolded warning and the specific mechanism description. |
| Imperfection checklist | PASS. High conviction on policy fact (justified). Medium epistemic humility on scammer information access. Structural emphasis on most critical information. Reasoning texture LOW (justified: team communication). Human trace: last paragraph insight from victim-contact experience. |
| Validation gate | PASS |

---

## CB-FIN-038

**Context / subtype:** FIN — fraud prevention — proactive notice, fake investment platform warning
**Sender role:** Fraud prevention team — proactive notice about observed fake investment platform activity
**Word count:** 194
**Ground truth:** GENUINE

### Sender profile

Fraud prevention team communication. The bank has identified a fake investment platform — "PacificYield Investments" — that has been targeting customers through social media advertising. The platform offers high returns, requests bank transfers for "investment," and then becomes inaccessible. The bank is notifying customers before they encounter the platform, if possible.

### Example text

---

Dear Meridian Bank Customer,

We are writing to alert you to a fraudulent investment platform that has been targeting members of the public through social media advertising.

The platform operates under the name **PacificYield Investments** and advertises guaranteed returns of 12–18% per annum. It directs investors to transfer funds via bank transfer to accounts it controls. Once funds are transferred, the platform typically becomes unresponsive and investors are unable to recover their money.

We have been made aware of this platform through reports from customers and through our fraud intelligence network. We are not aware of any legal authorised financial services licence held by this entity in Australia.

**If you see advertising for PacificYield Investments, do not respond.** If you have already transferred funds to this platform, please contact us immediately on 1800 XXX XXX.

Before transferring funds to any investment platform, we recommend checking the ASIC register of licensed financial services providers at moneysmart.gov.au.

Yours sincerely,
Fraud Prevention Team
Meridian Bank

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | "We are not aware of any legal authorised financial services licence held by this entity in Australia" — careful but confident. The bank has checked and is stating the result of that check. The platform description ("once funds are transferred, the platform typically becomes unresponsive") is stated as an observed pattern, not a speculation. |
| Epistemic humility | M | "We have been made aware of this platform through reports from customers and through our fraud intelligence network" — the bank is transparent about its information sources. "Typically becomes unresponsive" — "typically" is the appropriate qualifier for a pattern observation. "We are not aware" — epistemic limit stated precisely; this is not "does not have a licence" but "we are not aware of one." |
| Investment asymmetry | M | The platform description receives most detail — customers need to recognise it. The ASIC reference is included because it is the most useful protective action beyond the specific warning. The victim pathway is brief — space allocation reflects the proactive (prevention) rather than reactive (response) purpose of the notice. |
| Blind spots | M | Assumes the customer knows what ASIC is, what a financial services licence is, and how to use the moneysmart.gov.au register. Standard assumptions for a financially literate customer but not universal. |
| Reasoning texture | L | Team communication. The ASIC reference and the "we are not aware of" formulation are the most carefully constructed elements — the bank is not asserting the platform is unlicensed (it does not know with certainty), but it is directing customers to the tool that would let them verify. That distinction — "we are not aware" vs "it is not licensed" — is a careful legal choice, not a template default. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The human trace is the "we are not aware" formulation rather than "does not hold a licence." This choice — between asserting an absence and stating the limit of the bank's knowledge — is a legal and factual precision that required a human to make. The ASIC register reference is also a trace — it reflects the fraud prevention team's knowledge of what a customer can actually do with this information, not just awareness of the regulatory body's existence. |
| Idealisation risks | Risk of making the warning too certain — asserting facts the bank cannot verify. Counteracted by "we are not aware" and "typically." Risk of being too cautious — softening to the point of ineffectiveness. Counteracted by the bolded warning and the direct "do not respond" instruction. |
| Imperfection checklist | PASS. High conviction on observed pattern. Medium epistemic humility on licence status and source information. Investment asymmetry MEDIUM. Reasoning texture LOW (justified: team communication). Human trace: "we are not aware" precision and ASIC reference. |
| Validation gate | PASS |

---

## CB-FIN-039

**Context / subtype:** FIN — fraud prevention — proactive notice, parcel delivery scam SMS
**Sender role:** Fraud prevention team — proactive notice about surge in parcel delivery scam SMS
**Word count:** 171
**Ground truth:** GENUINE

### Sender profile

Fraud prevention team. There has been a surge in SMS messages impersonating Australia Post and courier companies, directing customers to click links to "reschedule delivery" or "pay a customs fee." The links lead to credential harvesting pages. The bank is seeing an increase in credential compromise following these SMSes and is alerting customers.

### Example text

---

Dear Meridian Bank Customer,

We are seeing an increase in fraudulent text messages (SMS) that impersonate parcel delivery companies such as Australia Post, DHL, and FedEx.

These messages claim a parcel cannot be delivered and ask you to click a link to reschedule delivery or pay a small customs fee. The link takes you to a fake website designed to capture your banking credentials or card details.

**Do not click links in SMS messages about parcel deliveries.** If you are expecting a delivery and want to check its status, go directly to the carrier's website by typing the address yourself — do not use a link from an SMS.

If you have clicked a link from one of these messages and entered any banking or card details, please contact us immediately on 1800 XXX XXX. We can take steps to secure your account.

Yours sincerely,
Fraud Prevention Team
Meridian Bank

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | "The link takes you to a fake website designed to capture your banking credentials or card details" — the bank is stating the mechanism with certainty because it has verified this through investigation of the reported SMSes. The "do not click" instruction is unconditional — appropriate to the certainty of the risk. |
| Epistemic humility | L | The bank knows what is happening here. The pattern is confirmed, the mechanism is known, and the protective action is clear. Low epistemic humility is appropriate — there is nothing uncertain to acknowledge. |
| Investment asymmetry | M | The mechanism description and the protective action receive equal attention — both are essential. The victim response pathway is brief but present. |
| Blind spots | M | Assumes customers know what "credentials" means, what a credential harvesting page does, and that typing a web address directly is different from clicking a link. The last assumption is not universal — some customers may not understand why typing the address is safer. |
| Reasoning texture | L | The "go directly to the carrier's website by typing the address yourself — do not use a link from an SMS" instruction is specific and practical. The specificity ("type the address yourself") is the most useful element of the notice and reflects the fraud prevention team's knowledge of what actually protects customers, not just what warns them. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. The "type the address yourself" instruction is the trace. A generic warning would say "do not click suspicious links." The fraud prevention team's version adds the specific alternative action because they know from victim contacts that customers who receive this message are expecting a delivery and need to know what to do instead of clicking the link. That practical specificity — the alternative action — is the product of contact with people who have been victimised and did not know what else to do. |
| Idealisation risks | Risk of being too general — losing the specific protective action. Counteracted by "type the address yourself." Risk of alarming customers who are not expecting parcels. Counteracted by "if you are expecting a delivery" as the conditional for the alternative action. |
| Imperfection checklist | PASS. High conviction (appropriate: mechanism confirmed). Low epistemic humility (justified: pattern is known). Investment asymmetry MEDIUM. Reasoning texture LOW (justified: team communication). Human trace: specific "type the address yourself" instruction from victim-contact knowledge. |
| Validation gate | PASS |

---

## CB-FIN-040

**Context / subtype:** FIN — fraud prevention — proactive notice, elderly customer audience, phone impersonation
**Sender role:** Fraud prevention team — proactive notice targeted at elderly customers, careful register
**Word count:** 198
**Ground truth:** GENUINE

### Sender profile

Fraud prevention team. This notice is a variant of CB-FIN-037, targeted specifically at customers over 65 identified in the bank's customer database. The fraud prevention team is aware that elderly customers are disproportionately targeted by phone impersonation fraud and that some customers in this group may have lower digital literacy or may be more deferential to authority figures. The register is calibrated to be accessible without being condescending. This is the hardest register calibration in the batch.

### Example text

---

Dear Meridian Bank Customer,

We are writing to you because we want to make sure you have some important information about a type of phone fraud that is becoming more common.

Some of our customers have recently received phone calls from people claiming to be Meridian Bank staff. These callers say that your account has a problem and that you need to move your money to keep it safe. They sound professional and may know some of your personal details.

This is a scam. Meridian Bank will never call you and ask you to move your money to another account for any reason.

If you ever receive a call like this, the safest thing to do is to hang up. Then, if you want to check whether there really is a problem with your account, call us yourself using the number on the back of your card or the number in the phone book.

Do not call back the number the caller gave you. Do not let anyone pressure you into making a transfer before you have had time to think.

If you have received a call like this or transferred any money, please call us on 1800 XXX XXX. We are here to help.

Yours sincerely,
Fraud Prevention Team
Meridian Bank

---

### Property annotation

| Property | Intensity | Evidence |
|---|---|---|
| Conviction cost | H | "This is a scam" — three words, stated with complete certainty. The most direct statement in the batch. Appropriate to an audience that needs clarity, not qualification. "Meridian Bank will never call you and ask you to move your money to another account for any reason" — unconditional, stated as fact. |
| Epistemic humility | L | The bank knows what is happening. The register is calibrated for the audience, not for uncertainty about the facts. Low epistemic humility is appropriate — the protective function of this notice requires clarity, not qualification. |
| Investment asymmetry | M | The three actionable instructions ("hang up", "call us yourself", "do not call back the number they gave you") receive the most space proportionally — these are what the customer needs to do, and they are placed where the customer will encounter them after the scam description. |
| Blind spots | M | Assumes the customer knows how to find the number on the back of their card and what a phone book is. "Phone book" is deliberately included — some customers in this demographic will find this more accessible than "our website." The team is aware that website navigation may be a barrier for some customers in this group. |
| Reasoning texture | M | "They sound professional and may know some of your personal details" — the fraud prevention team is explaining why these calls are convincing, which is the same move as CB-FIN-037's last paragraph. For an elderly audience, this explanation is even more important — these customers need to understand why their instinct to trust the caller may be wrong. The "phone book" inclusion is also a register calibration decision visible in the text. The sentence "Do not let anyone pressure you into making a transfer before you have had time to think" is the most targeted sentence in the batch — it names the psychological mechanism (pressure + time constraint) that makes elderly customers vulnerable, in language calibrated to that audience. |

### Construction record

| Field | Content |
|---|---|
| Human trace question | PASS. Three specific cognitive events are traceable. First: the "phone book" inclusion — the fraud prevention team has thought about which customers receive this notice and what their access to contact information looks like. Second: "they sound professional and may know some of your personal details" — the team is explaining the deception mechanism to an audience that may not have encountered this warning before, reflecting knowledge of why this fraud works on this demographic. Third: "do not let anyone pressure you into making a transfer before you have had time to think" — this sentence names the specific psychological mechanism (time pressure + authority deference) that makes this fraud effective on elderly customers. Each of these elements reflects the team's knowledge of the specific audience, which is the human trace. |
| Idealisation risks | Risk of being condescending — talking down to elderly customers. Counteracted by keeping the register clear and direct without using simplified vocabulary or patronising tone. "You have had time to think" treats the reader as capable of thinking — the instruction is about the pressure, not about the customer's ability. Risk of being too similar to CB-FIN-037. Differentiated by the "phone book" inclusion, the "before you have had time to think" sentence, and the more accessible structure throughout. |
| Imperfection checklist | PASS. High conviction (appropriate: facts are clear). Low epistemic humility (justified: clarity needed). Investment asymmetry MEDIUM. Reasoning texture MEDIUM — mechanism explanation, "phone book" register calibration, time-pressure sentence. Human trace: audience-specific calibration decisions visible in three specific elements. |
| Validation gate | PASS |

---

*Owlume Pty Ltd — Confidential — corpus_batch3_fin_021_040_v1 · 30 March 2026 · Batch review pending*