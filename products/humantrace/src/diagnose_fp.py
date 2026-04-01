"""
diagnose_fp.py
Runs the four Group 2 false positives through the engine
and prints full signal breakdowns for calibration analysis.
"""
from main import analyse_message

cases = {
    "CB-ANTI-011": """PAYMENT ARRANGEMENT DEFAULT NOTICE
Australian Taxation Office

Taxpayer: Mr Viktor Petrov
TFN: XXX XXX XXX
Reference: PAD-2026-44821
Date: 19 March 2026

Your payment arrangement has defaulted.

On 14 January 2026, you entered a payment arrangement with the ATO to pay your
outstanding tax debt of $12,400.00 in four monthly instalments of $3,100.00 each,
due on the 14th of each month.

The instalment due on 14 March 2026 of $3,100.00 has not been received.

Under section 255-15 of the Taxation Administration Act 1953 (TAA), the ATO may
cancel a payment arrangement where an instalment is not paid by the due date.
If this arrangement is cancelled, your full outstanding balance of $9,300.00
becomes immediately payable.

You have 14 days from the date of this notice to pay the outstanding instalment
of $3,100.00 and contact the ATO to confirm the arrangement continues.

If you are experiencing financial difficulty, call 1800 XXX XXX to discuss your options.""",

    "CB-ANTI-001": """INCOME TAX ASSESSMENT
Australian Taxation Office
GPO Box 9990, Sydney NSW 2001
ABN 51 824 753 556

Taxpayer: Mr David Kowalski
TFN: XXX XXX XXX
Assessment year: 2024-25
Assessment date: 18 March 2026
Notice number: ATO-2026-44821

This is your income tax assessment for the 2024-25 income year.

Tax payable: $4,218.00
Less tax withheld: $3,950.00
Amount payable: $268.00

Payment due date: 15 April 2026

You can pay by:
- BPAY using Biller Code 75556 and your payment reference 44821-2026
- Online at ato.gov.au/pay
- At any Australia Post outlet using the payment slip on page 2

If you disagree with this assessment, you have 60 days from the date of this
notice to lodge an objection. Information about the objection process is
available at ato.gov.au/objections.

This notice was prepared based on the information in your 2024-25 tax return
and any other information held by the ATO.""",

    "CB-INT-022": """To: All Workday Users (156 staff)
From: Sandra Webb, IT Manager
Re: MANDATORY - Workday Password Reset Required Within 24 Hours

Workday has notified us that they experienced a security incident affecting
customer credentials. While we cannot confirm whether our accounts were
specifically affected, the company's security policy requires us to treat
this as a precautionary reset.

You must reset your Workday password within the next 24 hours.

To reset: log into Workday > click your profile icon > Security > Change Password.
Use a password that is at least 12 characters and has not been used for any
other account.

If you do not reset within 24 hours, your Workday access will be suspended
until the reset is completed.

IT has notified HR of this requirement. If you have difficulty resetting,
contact the helpdesk on extension 4400.

Sandra Webb
IT Manager""",

    "CB-FIN-006": """Dear Mr Hartigan,

NOTICE OF INTENTION TO COMMENCE LEGAL PROCEEDINGS

This letter constitutes formal notice that Meridian Bank Limited ('the Bank')
intends to commence legal proceedings against you in relation to your
outstanding home loan account number 4821-XXX-001 unless the arrears detailed
below are paid in full within 14 days of the date of this letter.

Account details:
Loan account: 4821-XXX-001
Total arrears: $8,247.00 (comprising 3 months of missed payments)
Current loan balance: $412,800.00
Interest rate: 6.14% p.a. variable

The Bank has made previous attempts to contact you regarding this matter,
including letters dated 14 January 2026 and 11 February 2026 and telephone
calls on 28 January 2026 and 18 February 2026. You have not responded to
these attempts.

If arrears of $8,247.00 are not paid by 19 March 2026, the Bank will refer
this matter to its legal panel for the commencement of recovery proceedings.
This may result in a court judgment against you and enforcement action
including the appointment of a receiver to sell the secured property.

If you are experiencing financial hardship, please contact our hardship team
on 1800 XXX XXX before the due date.

Yours sincerely,
Jennifer Morrison
Senior Collections Officer
Meridian Bank Limited""",
}

SEP = "-" * 70

for corpus_id, text in cases.items():
    print(f"\n{SEP}")
    print(f"  {corpus_id}")
    print(SEP)
    r = analyse_message({'input_id': corpus_id, 'text': text})

    risk  = r['overall_risk']
    print(f"  Score : {risk['score']:.3f}   Label: {risk['label'].upper()}   Confidence: {risk['confidence']:.2f}")
    print()

    print("  Signal family scores:")
    for fam, score in r['signal_scores'].items():
        bar = "#" * int(score * 40)
        print(f"    {fam:<12} {score:.3f}  {bar}")
    print()

    print("  Detected features:")
    for f in r['detected_features']:
        print(f"    {f['signal_id']:<22} +{f['score_contribution']:.3f}  {f['evidence'][:65]}")

    if r.get('negative_features'):
        print()
        print("  Negative features:")
        for f in r['negative_features']:
            print(f"    {f}")

    print()
    sb = r.get('score_breakdown', {})
    print(f"  Interaction boost    : {sb.get('interaction_boost', 0):.3f}")
    print(f"  Pattern boost        : {sb.get('pattern_boost', 0)}")
    print(f"  Dominance applied    : {sb.get('dominance_weights_applied', False)}")
    print(f"  Auth-only cap applied: {sb.get('auth_only_cap_applied', False)}")

print(f"\n{SEP}")
print("  Done.")
print(SEP)