"""
humantrace_behavioural_signals.py
Behavioural signal library for HumanTrace — version 1.0

Signal framework derived from intelligence and interrogation tradecraft.
Measures three primary signal categories:

  1. Micro-variation absence
     Genuine human communication contains natural irregularities.
     Over-controlled text is statistically smooth in ways that are
     detectable and diagnostically significant.

  2. Limbic leakage
     Genuine human communication leaks emotional content that was
     not consciously intended. Synthetic text has no limbic system
     and therefore produces no leakage.

  3. Investment asymmetry
     Genuine need creates a specific investment signature.
     The emotional weight of a message should be proportionate
     to the size and stakes of the ask. Mismatches are diagnostic.

Two further categories (precision asymmetry, structural smoothness)
are specified and reserved for version 2.

Contract:
  analyse(text, context) -> SignalLibraryResult
  Every signal module in trace_signals/ must implement this interface.

Internal vocabulary stays internal.
User-facing findings use layman language only.
Output kind: SIGNAL — not advice, not instruction.
"""

from __future__ import annotations

import re
import math
from dataclasses import dataclass, field
from typing import Optional


# ── Result contract ───────────────────────────────────────────────────────────

@dataclass
class SignalLibraryResult:
    """
    Standard result shape for all trace_signals modules.
    Every module must return this structure.
    """
    module_name:      str
    human_score:      float        # 0.0 (no human signals) — 1.0 (strong human signals)
    synthetic_score:  float        # 0.0 (no synthetic signals) — 1.0 (strong synthetic signals)
    signals_fired:    list[str]    # internal signal names — not shown to users
    findings:         list[str]    # user-facing strings in layman language
    raw_data:         dict         # internal measurements — never shown to users


# ── Signal 1: Micro-variation ─────────────────────────────────────────────────

# Self-interruption markers — genuine humans course-correct mid-thought
SELF_INTERRUPTION = [
    r"\b(actually|wait|i mean|or rather|that is|that's to say|no wait|"
    r"let me rephrase|what i mean is|to be more precise|scratch that)\b",
]

# Topic drift markers — genuine humans elaborate beyond purpose
TOPIC_DRIFT = [
    r"\b(by the way|speaking of which|this reminds me|oh and|also|"
    r"unrelated but|on another note|while i'm at it|incidentally)\b",
]

# Register shift markers — formal→casual or casual→formal within message
CASUAL_MARKERS = [
    r"\b(yeah|yep|nope|gonna|wanna|kinda|sorta|dunno|gotta|"
    r"hey|ok|okay|cool|great|awesome|honestly|basically|literally)\b",
]
FORMAL_MARKERS = [
    r"\b(furthermore|moreover|therefore|consequently|pursuant|"
    r"notwithstanding|henceforth|herein|aforementioned|accordingly)\b",
]


def _sentence_lengths(text: str) -> list[int]:
    """Split into sentences and return word counts."""
    sentences = re.split(r"(?<=[.!?])\s+", text.strip())
    return [len(s.split()) for s in sentences if len(s.split()) >= 2]


def _coefficient_of_variation(values: list[float]) -> float:
    """CV = std/mean — measures relative variability."""
    if len(values) < 2:
        return 0.0
    mean = sum(values) / len(values)
    if mean == 0:
        return 0.0
    variance = sum((v - mean) ** 2 for v in values) / len(values)
    return round(math.sqrt(variance) / mean, 4)


def _score_micro_variation(text: str) -> tuple[float, float, list[str], list[str], dict]:
    """
    Score micro-variation presence/absence.
    Returns: (human_score, synthetic_score, signals_fired, findings, raw_data)
    """
    t = text.lower()
    word_count = len(text.split())
    human_score = 0.0
    synthetic_score = 0.0
    signals_fired = []
    findings = []

    # Self-interruption
    interruptions = []
    for pattern in SELF_INTERRUPTION:
        interruptions.extend(re.findall(pattern, t, re.IGNORECASE))
    if interruptions:
        human_score += 0.25
        signals_fired.append("self_interruption_present")
        findings.append("Natural self-correction present — consistent with genuine human communication")
    elif word_count > 40:
        synthetic_score += 0.15
        signals_fired.append("self_interruption_absent")

    # Topic drift
    drift_hits = []
    for pattern in TOPIC_DRIFT:
        drift_hits.extend(re.findall(pattern, t, re.IGNORECASE))
    if drift_hits:
        human_score += 0.20
        signals_fired.append("topic_drift_present")
        findings.append("Off-purpose elaboration present — genuine humans drift beyond their stated goal")
    elif word_count > 60:
        synthetic_score += 0.10
        signals_fired.append("topic_drift_absent")

    # Register shift — both casual and formal markers in same message
    casual_hits = any(re.search(p, t, re.IGNORECASE) for p in CASUAL_MARKERS)
    formal_hits = any(re.search(p, t, re.IGNORECASE) for p in FORMAL_MARKERS)
    if casual_hits and formal_hits:
        human_score += 0.20
        signals_fired.append("register_shift_present")
        findings.append("Register shift detected — natural mixing of formal and informal tone")
    elif not casual_hits and not formal_hits and word_count > 50:
        # Neither formal nor casual — flat, toneless register
        synthetic_score += 0.10
        signals_fired.append("flat_register")

    # Sentence length variance
    lengths = _sentence_lengths(text)
    if len(lengths) >= 3:
        cv = _coefficient_of_variation([float(l) for l in lengths])
        if cv >= 0.40:
            human_score += 0.20
            signals_fired.append("high_sentence_variance")
            findings.append("Natural sentence length variation — consistent with human writing rhythm")
        elif cv < 0.20:
            synthetic_score += 0.20
            signals_fired.append("low_sentence_variance")
            findings.append("Unusually uniform sentence lengths — synthetic text tends toward statistical smoothness")

    raw_data = {
        "word_count": word_count,
        "interruption_count": len(interruptions),
        "drift_count": len(drift_hits),
        "casual_register": casual_hits,
        "formal_register": formal_hits,
        "sentence_lengths": lengths,
        "sentence_cv": _coefficient_of_variation([float(l) for l in lengths]) if len(lengths) >= 3 else None,
    }

    return (
        round(min(human_score, 1.0), 3),
        round(min(synthetic_score, 1.0), 3),
        signals_fired,
        findings,
        raw_data,
    )


# ── Signal 2: Limbic leakage ──────────────────────────────────────────────────

# Unexpected emotional vocabulary — genuine humans leak affect

EMOTIONAL_LEAKAGE = [
    r"\b(honestly|truthfully|between you and me)\b",
    r"\b(this is hard to say|this is hard to write|this is hard to admit)\b",
    r"\b(i am (embarrassed|nervous|worried|scared|relieved|frustrated|exhausted|overwhelmed|excited|grateful))\b",
    r"\b(sorry to (say|tell|inform|bother|ask))\b",
    r"\b(i hate (asking|bothering|to ask|to bother))\b",
    r"\b(i feel (bad|terrible|awful) (asking|about|for))\b",
]

OVER_QUALIFICATION = [
    r"\b(i think maybe|possibly perhaps|might possibly|could perhaps)\b",
    r"\b(not sure (what|how|if|whether))\b",
    r"\b(i suppose|i guess|sort of|kind of|more or less)\b",
    r"\b(i hope this|maybe possibly)\b",
]

UNDER_QUALIFICATION = [
    r"\b(this will definitely|guaranteed to|absolutely certain)\b",
    r"\b(there is no doubt|without question|one hundred percent)\b",
    r"\b(i promise you|trust me on this|i can assure you)\b",
]

SELF_DISCLOSURE = [
    r"\b(in my (experience|opinion|view|life|case))\b",
    r"\b(when i (was|had|did|went|tried|found|learned))\b",
    r"\b(i remember (when|how|that)|i used to)\b",
    r"\b(i have (found|noticed|learned|discovered|realised|realized))\b",
    r"\b(i recently|i personally|i always|i never|i sometimes)\b",
]

def _score_limbic_leakage(text: str) -> tuple[float, float, list[str], list[str], dict]:
    t = text.lower()
    word_count = len(text.split())
    human_score = 0.0
    synthetic_score = 0.0
    signals_fired = []
    findings = []

    # Emotional leakage
    leakage_hits = []
    for pattern in EMOTIONAL_LEAKAGE:
        leakage_hits.extend(re.findall(pattern, t, re.IGNORECASE))
    if leakage_hits:
        human_score += 0.30
        signals_fired.append("emotional_leakage_present")
        findings.append("Unguarded emotional content present — genuine human affect signal")

    # Over-qualification (genuine uncertainty)
    over_q = any(re.search(p, t, re.IGNORECASE) for p in OVER_QUALIFICATION)
    if over_q:
        human_score += 0.15
        signals_fired.append("over_qualification_present")
        findings.append("Genuine uncertainty markers present — authentic hedging detected")

    # Under-qualification (suspicious perfect confidence)
    under_q = any(re.search(p, t, re.IGNORECASE) for p in UNDER_QUALIFICATION)
    if under_q:
        synthetic_score += 0.25
        signals_fired.append("under_qualification_present")
        findings.append("Costless certainty detected — claims made without appropriate hedging")

    # Investment/stakes mismatch — high certainty on unverifiable claims
    if under_q and not over_q and word_count > 30:
        synthetic_score += 0.15
        signals_fired.append("certainty_stakes_mismatch")

    # Spontaneous self-disclosure
    disclosure_hits = []
    for pattern in SELF_DISCLOSURE:
        disclosure_hits.extend(re.findall(pattern, t, re.IGNORECASE))
    disclosure_count = len(set(disclosure_hits))
    if disclosure_count >= 2:
        human_score += 0.25
        signals_fired.append("self_disclosure_present")
        findings.append("Spontaneous personal disclosure — genuine humans volunteer context beyond their stated purpose")
    elif disclosure_count == 1:
        human_score += 0.10
        signals_fired.append("minimal_self_disclosure")

    raw_data = {
        "leakage_hits": len(leakage_hits),
        "over_qualification": over_q,
        "under_qualification": under_q,
        "disclosure_count": disclosure_count,
    }

    return (
        round(min(human_score, 1.0), 3),
        round(min(synthetic_score, 1.0), 3),
        signals_fired,
        findings,
        raw_data,
    )


# ── Signal 3: Investment asymmetry ───────────────────────────────────────────

# High-stakes ask markers — messages requesting significant action
HIGH_STAKES_ASK = [
    r"\b(send|transfer|pay|wire|click|verify|confirm|update|provide|"
    r"urgent|immediately|right away|as soon as possible|asap|"
    r"deadline|expires?|limited time|act now)\b",
]

# Appropriate investment for high-stakes — genuine humans show cost
APPROPRIATE_INVESTMENT = [
    r"\b(i hate (asking|bothering|to ask|to bother))\b",
    r"\b(i feel (bad|terrible|awful) (asking|about|for))\b",
    r"\b(i know this is (a lot|much|big|hard|difficult))\b",
    r"\b(i would not ask (if|unless)|i would not normally ask)\b",
    r"\b(i am only asking because|i realise this is|i understand if you)\b",
    r"\b(sorry to ask|hate to ask|awkward to ask|hard to ask)\b",
]



def _score_investment_asymmetry(text: str) -> tuple[float, float, list[str], list[str], dict]:
    t = text.lower()
    human_score = 0.0
    synthetic_score = 0.0
    signals_fired = []
    findings = []

    # Detect stakes level
    stakes_hits = []
    for pattern in HIGH_STAKES_ASK:
        stakes_hits.extend(re.findall(pattern, t, re.IGNORECASE))
    high_stakes = len(stakes_hits) >= 2

    # Detect investment level
    investment_hits = []
    for pattern in APPROPRIATE_INVESTMENT:
        investment_hits.extend(re.findall(pattern, t, re.IGNORECASE))
    shows_investment = len(investment_hits) >= 1

    if high_stakes and shows_investment:
        # High stakes + appropriate investment = genuine human signal
        human_score += 0.30
        signals_fired.append("appropriate_investment_present")
        findings.append("Appropriate hesitation present for the size of the request — genuine human signal")
    elif high_stakes and not shows_investment:
        # High stakes + no investment = synthetic fraud signal
        synthetic_score += 0.35
        signals_fired.append("investment_absent_high_stakes")
        findings.append("High-stakes request made without appropriate hesitation — costless ask detected")
    elif not high_stakes and shows_investment:
        # Low stakes + moderate investment = normal human behaviour, not suspicious
        # Only flag if investment is dramatically over the top (handled in v2)
        signals_fired.append("investment_neutral")
    else:
        # Low stakes, no investment — neutral
        signals_fired.append("investment_neutral")

    raw_data = {
        "stakes_hits": len(stakes_hits),
        "high_stakes": high_stakes,
        "investment_hits": len(investment_hits),
        "shows_investment": shows_investment,
    }

    return (
        round(min(human_score, 1.0), 3),
        round(min(synthetic_score, 1.0), 3),
        signals_fired,
        findings,
        raw_data,
    )


# ── Main entry point ──────────────────────────────────────────────────────────

def analyse(
    text: str,
    context: Optional[str] = None,
) -> SignalLibraryResult:
    """
    Main entry point. Analyses text across all three signal categories
    and returns a combined SignalLibraryResult.

    Args:
        text:    The message or document to analyse
        context: Optional context hint (e.g. "authored_document", "bank_officer")

    Returns:
        SignalLibraryResult with combined scores and findings
    """
    # Run all three signal categories
    mv_human, mv_synth, mv_signals, mv_findings, mv_raw = _score_micro_variation(text)
    ll_human, ll_synth, ll_signals, ll_findings, ll_raw = _score_limbic_leakage(text)
    ia_human, ia_synth, ia_signals, ia_findings, ia_raw = _score_investment_asymmetry(text)

    # Combine scores — weighted average
    # Micro-variation: 0.35 weight
    # Limbic leakage:  0.40 weight (most diagnostic per Hughes)
    # Investment:      0.25 weight
    human_score = round(
        (mv_human * 0.35) + (ll_human * 0.40) + (ia_human * 0.25), 3
    )
    synthetic_score = round(
        (mv_synth * 0.35) + (ll_synth * 0.40) + (ia_synth * 0.25), 3
    )

    all_signals = mv_signals + ll_signals + ia_signals
    all_findings = mv_findings + ll_findings + ia_findings
    raw_data = {
        "micro_variation": mv_raw,
        "limbic_leakage":  ll_raw,
        "investment":      ia_raw,
        "context":         context,
    }

    return SignalLibraryResult(
        module_name     = "behavioural_signals_v1",
        human_score     = human_score,
        synthetic_score = synthetic_score,
        signals_fired   = all_signals,
        findings        = all_findings,
        raw_data        = raw_data,
    )


# ── Smoke test ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    TEST_CASES = [
        {
            "label": "Genuine personal message",
            "text": (
                "Hey, I know this is awkward to ask but I'm actually in a bit of a "
                "situation. I hate bothering you with this — and honestly I wasn't "
                "going to say anything — but my car broke down yesterday and I'm "
                "not sure what to do. I think maybe I could ask my brother but "
                "he's been going through a lot lately. Anyway, sorry for rambling."
            ),
        },
        {
            "label": "Sophisticated fraud (short, intellectual)",
            "text": (
                "The opportunity I am presenting to you is time-sensitive and "
                "guaranteed to yield significant returns. You must act within "
                "48 hours to secure your position. This will definitely work "
                "and I can assure you there is no risk involved whatsoever."
            ),
        },
        {
            "label": "Book passage (authored document)",
            "text": (
                "The success of Upper Confidence Bound algorithms offers a formal "
                "justification for the benefit of the doubt. Following the advice "
                "of these algorithms, you should be excited to meet new people and "
                "try new things — to assume the best about them, in the absence of "
                "evidence to the contrary. In the long run, optimism is the best "
                "prevention of regret."
            ),
        },
        {
            "label": "Phishing email",
            "text": (
                "Dear valued customer, we have detected unusual activity on your "
                "account. You must verify your identity immediately by clicking "
                "the link below. Failure to act within 24 hours will result in "
                "your account being suspended. This is an urgent security alert."
            ),
        },
    ]

    print(f"\n{'='*65}")
    print("HUMANTRACE BEHAVIOURAL SIGNALS — Smoke Test")
    print(f"{'='*65}")

    for case in TEST_CASES:
        result = analyse(case["text"])
        print(f"\n{case['label']}")
        print(f"  Human score:     {result.human_score:.3f}")
        print(f"  Synthetic score: {result.synthetic_score:.3f}")
        print(f"  Signals fired:   {result.signals_fired}")
        print(f"  Findings:")
        for f in result.findings:
            print(f"    · {f}")
