# src/humantrace_scanner.py
# HumanTrace — Human Reasoning Presence Scanner
# Powered by Owlume / Elenx Engine
#
# Purpose:
#   Detect whether genuine human reasoning is present behind
#   an external communication (email, SMS, message, document).
#
# Architecture note:
#   This module does NOT modify elenx_engine.py, judgment_gate.py,
#   block_runtime.py, or aggregator.py. It reorients them as
#   infrastructure for external message analysis rather than
#   self-reflection.
#
# Governance alignment:
#   - Output kind is "SIGNAL" — not ACTION, ADVICE, or INSTRUCTIONS.
#   - Stage 14 BLOCK does not apply to SIGNAL output by design.
#   - Narrow interpretation: prefer false negatives over false positives.
#   - Never accuse. Always surface signal + confidence + explanation.
#   - Human analyst makes the final judgment.
#
# Signal thresholds (governance-fixed, non-tunable):
#   RED    >= 0.75  → Low human reasoning presence detected
#   YELLOW  0.45–0.74 → Uncertain — insufficient signal
#   GREEN  >= 0.80  → Human reasoning presence detected
#   NOTE: Gap between RED and GREEN is intentional.
#         HumanTrace defaults to YELLOW under uncertainty.
#         A false GREEN is the catastrophic failure mode.

from __future__ import annotations

import re
import uuid
import json
import datetime as dt
from dataclasses import dataclass, field, asdict
from typing import Dict, List, Optional, Any, Tuple


# ── Signal constants (governance-fixed) ──────────────────────────────────────

RED_THRESHOLD    = 0.75   # Synthetic signal confidence floor
GREEN_THRESHOLD  = 0.80   # Human signal confidence floor
YELLOW_LOW       = 0.45   # Below this = insufficient data, still YELLOW


# ── Synthetic fraud pattern library ──────────────────────────────────────────
# Each pattern targets a reasoning-level signal, not stylistic surface.
# Organised by fraud category for longitudinal BSE tracking.

SYNTHETIC_PATTERNS = {
    "manufactured_urgency": [
        r"\b(act now|immediately|urgent|expires? (today|tonight|in \d+ hours?)|limited time|don'?t delay|time is running out|last chance)\b",
        r"\b(within \d+ (hours?|minutes?|days?))\b",
        r"\b(before it'?s too late|once in a lifetime|now or never)\b",
    ],
    "authority_impersonation": [
        r"\b(irs|hmrc|ato|fbi|interpol|microsoft|apple|amazon|paypal|your bank|government)\b.{0,40}\b(contact|verify|confirm|suspended|frozen|action required)\b",
        r"\b(official notice|final warning|account (suspended|frozen|compromised|flagged))\b",
        r"\b(we have detected|unusual activity|security alert|verify your identity)\b",
    ],
    "investment_fraud": [
        r"\b(guaranteed (returns?|profit|income)|risk[- ]free|no risk)\b",
        r"\b(\d+%\s*(return|profit|gain|interest) (per|a) (day|week|month|year))\b",
        r"\b(secret (method|system|strategy)|exclusive (opportunity|access|offer))\b",
        r"\b(crypto|bitcoin|forex|trading (bot|platform|signal))\b.{0,60}\b(profit|return|earn|income)\b",
    ],
    "romance_scam": [
        r"\b(i (love|adore|miss|need) you).{0,80}\b(money|send|transfer|wallet|gift card)\b",
        r"\b(stuck (in|at)|stranded|emergency|accident|hospital).{0,60}\b(send|transfer|wire|money)\b",
        r"\b(western union|moneygram|gift card|itunes|google play|wire transfer)\b",
    ],
    "phishing": [
        r"\b(click (here|the link|below)|verify (your|the) (account|email|identity|information))\b",
        r"\b(update (your|billing|payment|account) (information|details|method))\b",
        r"\b(your (account|password|card) (will be|has been|is) (suspended|expired|compromised|locked))\b",
    ],
    "purpose_pure_construction": [
        # Messages with zero off-topic human noise — purely instrumental
        # This is detected by absence (see _detect_absence_signals)
    ],
}

# Genuine human communication markers — signals that synthetic messages
# almost never produce because they serve no persuasive purpose.
HUMAN_MARKERS = {
    "genuine_uncertainty": [
        r"\b(i (think|believe|guess|suppose|wonder)|not sure (if|whether|about)|maybe|perhaps|probably)\b",
        r"\b(i might be wrong|correct me if|let me know if (i'?m|that'?s))\b",
    ],
    "self_correction": [
        r"\b(actually|wait|never mind|scratch that|i mean|what i meant|to clarify)\b",
        r"\*?(correction|edit|update)\*?",
    ],
    "irrelevant_human_noise": [
        r"\b(anyway|by the way|oh|hmm|sorry for the rambling|hope (you'?re|this finds you))\b",
        r"\b(just wanted to|quick question|random thought|totally unrelated)\b",
    ],
    "asymmetric_emphasis": [
        # Human overweights certain concerns — detectable as disproportionate focus
        r"\b(the (main|biggest|real|only) (thing|issue|concern|problem|reason) is)\b",
        r"\b(what (really|actually) (bothers|concerns|worries) me)\b",
    ],
    "cost_of_conclusion": [
        r"\b(it'?s (hard|difficult|painful) to (admit|say|accept)|i (hate|regret|wish) (that|i))\b",
        r"\b(even though (i|this)|despite (the fact|knowing|my))\b",
        r"\b(i'?m (conflicted|torn|not comfortable|hesitant))\b",
    ],
}

# Contextual plausibility rules — does reasoning match claimed context?
CONTEXT_PLAUSIBILITY = {
    "bank_officer": {
        "never_says": [
            r"\b(gift card|itunes|google play|wire (to|me)|send (cash|money) to)\b",
            r"\b(keep this (secret|confidential|between us)|don'?t tell (anyone|your family))\b",
            r"\b(personal (wallet|account)|my (account|address))\b",
        ],
        "confidence_penalty": 0.30,
    },
    "friend_in_distress": {
        "suspicious_if": [
            r"\b(wire transfer|western union|moneygram|bitcoin|crypto wallet)\b",
            r"\b(don'?t (call|contact) (me|my family|the police))\b",
        ],
        "confidence_penalty": 0.20,
    },
    "investment_opportunity": {
        "suspicious_if": [
            r"\b(guaranteed|no risk|risk[- ]free|can'?t lose)\b",
            r"\b(secret|exclusive|only (a few|limited) (spots?|people|access))\b",
        ],
        "confidence_penalty": 0.25,
    },
}


# ── Data structures ───────────────────────────────────────────────────────────

@dataclass
class LayerResult:
    """Result from a single detection layer."""
    layer: str
    signal: str          # "synthetic" | "human" | "uncertain" | "absent"
    confidence: float    # 0.0 – 1.0
    findings: List[str]  # Human-readable findings for this layer
    patterns_hit: List[str] = field(default_factory=list)


@dataclass
class ScanResult:
    """
    Full HumanTrace scan result.

    Output kind: SIGNAL — not ACTION, ADVICE, or INSTRUCTIONS.
    Stage 14 BLOCK does not apply.
    Human analyst makes the final judgment.
    """
    scan_id: str
    timestamp: str
    signal: str              # "red" | "yellow" | "green"
    confidence: float        # 0.0 – 1.0
    first_contact: bool      # No longitudinal BSE data available
    layers: List[LayerResult]
    fraud_category: Optional[str]    # Detected fraud type if any
    plain_english: str               # One sentence for ordinary person
    recommended_action: str          # Non-prescriptive guidance
    analyst_questions: List[str]     # Questions for human analyst follow-up
    meta: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        d["layers"] = [asdict(l) for l in self.layers]
        return d

    def to_json(self, indent: int = 2) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=indent)


# ── Core scanner ─────────────────────────────────────────────────────────────

class HumanTraceScanner:
    """
    HumanTrace fraud detection scanner.
    Powered by Owlume reasoning infrastructure.

    Detects whether genuine human reasoning is present behind
    an external communication — or whether it is synthetic.

    Five detection layers:
      L1 — Structural reasoning analysis
      L2 — Contextual plausibility
      L3 — Conviction cost analysis
      L4 — Synthetic pattern library matching
      L5 — Absence signal detection
    """

    def __init__(self, bse_history: Optional[Dict[str, Any]] = None):
        """
        bse_history: optional Bias Signature Engine longitudinal data
                     for this sender. If None, first_contact = True.
        """
        self.bse_history = bse_history or {}
        self.first_contact = not bool(bse_history)

    def scan(self, message: str, context_hint: Optional[str] = None) -> ScanResult:
        """
        Scan a message for human reasoning presence.

        Args:
            message: The suspicious communication text.
            context_hint: Optional claimed context e.g. "bank_officer",
                         "friend_in_distress", "investment_opportunity".
                         Enables Layer 2 contextual plausibility check.

        Returns:
            ScanResult with signal, confidence, layer findings,
            plain English summary, and analyst questions.
        """
        message = (message or "").strip()
        if not message:
            return self._empty_result()

        # Run all five layers
        l1 = self._layer1_structural_reasoning(message)
        l2 = self._layer2_contextual_plausibility(message, context_hint)
        l3 = self._layer3_conviction_cost(message)
        l4 = self._layer4_pattern_library(message)
        l5 = self._layer5_absence_signals(message)

        layers = [l1, l2, l3, l4, l5]

        # Aggregate signal
        signal, confidence, mixed_meta = self._aggregate_signal(layers, l4)

        # Fraud category from L4
        fraud_category = l4.meta.get("category") if hasattr(l4, "meta") else None
        # Extract from patterns_hit
        fraud_category = self._extract_fraud_category(l4)

        # Build output
        plain_english = self._plain_english(signal, confidence, fraud_category, mixed_meta)
        recommended_action = self._recommended_action(signal, confidence)
        analyst_questions = self._analyst_questions(layers, message, context_hint, mixed_meta)

        return ScanResult(
            scan_id=str(uuid.uuid4()),
            timestamp=dt.datetime.utcnow().isoformat() + "Z",
            signal=signal,
            confidence=round(confidence, 3),
            first_contact=self.first_contact,
            layers=layers,
            fraud_category=fraud_category,
            plain_english=plain_english,
            recommended_action=recommended_action,
            analyst_questions=analyst_questions,
            meta={
                "message_length": len(message),
                "context_hint": context_hint,
                "bse_available": not self.first_contact,
                **mixed_meta,
                "governance": {
                    "output_kind": "SIGNAL",
                    "stage14_applies": False,
                    "interpretation": "narrow",
                    "false_green_is_catastrophic": True,
                }
            }
        )

    # ── Layer 1: Structural Reasoning Analysis ────────────────────────────────

    def _layer1_structural_reasoning(self, text: str) -> LayerResult:
        """
        Does the message show signs of genuine reasoning structure?
        Human reasoning is uneven, asymmetric, and shows struggle.
        Synthetic reasoning is complete, balanced, and costlessly confident.
        """
        t = text.lower()
        findings = []
        synthetic_score = 0.0
        human_score = 0.0

        # Check for manufactured urgency (synthetic signal)
        urgency_hits = self._match_any(t, SYNTHETIC_PATTERNS["manufactured_urgency"])
        if urgency_hits:
            synthetic_score += 0.25
            findings.append(f"Urgency appears manufactured rather than earned ({len(urgency_hits)} signal(s))")

        # Check for human uncertainty markers
        uncertainty_hits = self._match_any(t, HUMAN_MARKERS["genuine_uncertainty"])
        if uncertainty_hits:
            human_score += 0.20
            findings.append("Genuine uncertainty markers present")

        # Check for self-correction (strong human signal)
        correction_hits = self._match_any(t, HUMAN_MARKERS["self_correction"])
        if correction_hits:
            human_score += 0.25
            findings.append("Self-correction detected — strong human signal")

        # Check for asymmetric emphasis (human overweights certain concerns)
        emphasis_hits = self._match_any(t, HUMAN_MARKERS["asymmetric_emphasis"])
        if emphasis_hits:
            human_score += 0.15
            findings.append("Asymmetric emphasis detected — consistent with genuine conviction")

        # Sentence uniformity check — synthetic text has suspiciously uniform sentence length
        uniformity_penalty = self._check_sentence_uniformity(text)
        if uniformity_penalty > 0:
            synthetic_score += uniformity_penalty
            findings.append("Sentence structure shows high uniformity — consistent with synthetic generation")

        # Overall structural signal
        net = human_score - synthetic_score
        if net > 0.15:
            signal, conf = "human", min(0.50 + net, 0.75)
        elif net < -0.15:
            signal, conf = "synthetic", min(0.50 + abs(net), 0.80)
        else:
            signal, conf = "uncertain", 0.45
            findings.append("Structural reasoning signal is mixed")

        if not findings:
            findings.append("No strong structural reasoning signals detected")

        return LayerResult(
            layer="structural_reasoning",
            signal=signal,
            confidence=round(conf, 3),
            findings=findings,
        )

    def _check_sentence_uniformity(self, text: str) -> float:
        """
        Synthetic text tends to have suspiciously uniform sentence lengths.
        Returns a penalty score 0.0–0.20.
        """
        sentences = [s.strip() for s in re.split(r'[.!?]+', text) if len(s.strip()) > 10]
        if len(sentences) < 3:
            return 0.0
        lengths = [len(s.split()) for s in sentences]
        mean = sum(lengths) / len(lengths)
        variance = sum((l - mean) ** 2 for l in lengths) / len(lengths)
        std = variance ** 0.5
        # Low std relative to mean = high uniformity = synthetic signal
        cv = std / mean if mean > 0 else 0
        if cv < 0.15:
            return 0.20   # Very uniform
        if cv < 0.25:
            return 0.10   # Moderately uniform
        return 0.0

    # ── Layer 2: Contextual Plausibility ─────────────────────────────────────

    def _layer2_contextual_plausibility(self, text: str, context_hint: Optional[str]) -> LayerResult:
        """
        Does the reasoning make sense for a real person in this claimed context?
        Bank officers do not ask for gift cards.
        Friends in distress do not specify wire transfer methods.
        """
        findings = []
        t = text.lower()

        if not context_hint or context_hint not in CONTEXT_PLAUSIBILITY:
            # Auto-detect context from text
            context_hint = self._auto_detect_context(t)

        if not context_hint:
            return LayerResult(
                layer="contextual_plausibility",
                signal="uncertain",
                confidence=0.45,
                findings=["No context available for plausibility check — first contact"],
            )

        rules = CONTEXT_PLAUSIBILITY[context_hint]
        penalty = 0.0
        never_says = rules.get("never_says", []) + rules.get("suspicious_if", [])

        violations = []
        for pattern in never_says:
            if re.search(pattern, t, re.IGNORECASE):
                violations.append(pattern)
                penalty += rules.get("confidence_penalty", 0.20)

        if violations:
            findings.append(f"Context '{context_hint}': {len(violations)} plausibility violation(s) detected")
            findings.append("Real people in this context do not communicate this way")
            signal = "synthetic"
            conf = min(0.55 + penalty, 0.90)
        else:
            findings.append(f"Context '{context_hint}': No obvious plausibility violations")
            signal = "uncertain"
            conf = 0.45

        return LayerResult(
            layer="contextual_plausibility",
            signal=signal,
            confidence=round(conf, 3),
            findings=findings,
            patterns_hit=violations,
        )

    def _auto_detect_context(self, text: str) -> Optional[str]:
        """Infer likely claimed context from message content."""
        t = text.lower()
        if re.search(r"\b(bank|account|transaction|financial institution)\b", t):
            return "bank_officer"
        if re.search(r"\b(invest|return|profit|trading|opportunity|portfolio)\b", t):
            return "investment_opportunity"
        if re.search(r"\b(love|miss you|together|relationship|met online)\b", t):
            return "friend_in_distress"
        return None

    # ── Layer 3: Conviction Cost Analysis ────────────────────────────────────

    def _layer3_conviction_cost(self, text: str) -> LayerResult:
        """
        Does the sender show evidence of genuine personal cost
        behind this communication?

        Real humans asking for something show:
        - Reluctance to ask
        - Awareness of imposition
        - Genuine emotional exposure
        - Imperfect self-presentation

        Synthetic messages are costlessly confident.
        """
        t = text.lower()
        findings = []
        human_score = 0.0

        cost_hits = self._match_any(t, HUMAN_MARKERS["cost_of_conclusion"])
        if cost_hits:
            human_score += 0.30
            findings.append("Evidence of personal cost behind communication — genuine human signal")

        noise_hits = self._match_any(t, HUMAN_MARKERS["irrelevant_human_noise"])
        if noise_hits:
            human_score += 0.20
            findings.append("Off-topic human noise present — synthetic messages are purpose-pure")

        # Check for costless confidence — no hedging, no reluctance, no doubt
        if not cost_hits and not noise_hits:
            # Look for telltale perfect confidence
            perfect_confidence = re.search(
                r"\b(you will|you must|this will|guaranteed|absolutely|definitely|certainly)\b",
                t, re.IGNORECASE
            )
            if perfect_confidence:
                findings.append("Costless confidence detected — no evidence of personal stakes or doubt")
                signal = "synthetic"
                conf = 0.65
            else:
                findings.append("No conviction cost signals detected — insufficient to determine")
                signal = "uncertain"
                conf = 0.45
        else:
            signal = "human"
            conf = min(0.50 + human_score, 0.75)

        return LayerResult(
            layer="conviction_cost",
            signal=signal,
            confidence=round(conf, 3),
            findings=findings,
        )

    # ── Layer 4: Synthetic Pattern Library ───────────────────────────────────

    def _layer4_pattern_library(self, text: str) -> LayerResult:
        """
        Match against known synthetic fraud reasoning patterns.
        Each category has a reasoning topology that recurs across instances.
        """
        t = text.lower()
        findings = []
        patterns_hit = []
        category_scores: Dict[str, int] = {}

        for category, patterns in SYNTHETIC_PATTERNS.items():
            if category == "purpose_pure_construction":
                continue
            hits = self._match_any(t, patterns)
            if hits:
                category_scores[category] = len(hits)
                patterns_hit.extend(hits)

        if not category_scores:
            findings.append("No known fraud pattern signatures detected")
            return LayerResult(
                layer="pattern_library",
                signal="uncertain",
                confidence=0.45,
                findings=findings,
                patterns_hit=[],
            )

        # Highest scoring category
        top_category = max(category_scores, key=category_scores.get)
        total_hits = sum(category_scores.values())

        findings.append(f"Pattern match: {top_category.replace('_', ' ').title()} ({total_hits} signal(s))")
        if len(category_scores) > 1:
            others = [c.replace('_', ' ').title() for c in category_scores if c != top_category]
            findings.append(f"Secondary patterns: {', '.join(others)}")

        # Confidence scales with hit count
        conf = min(0.60 + (total_hits * 0.05), 0.92)

        result = LayerResult(
            layer="pattern_library",
            signal="synthetic",
            confidence=round(conf, 3),
            findings=findings,
            patterns_hit=patterns_hit[:10],  # cap for readability
        )
        # Attach category for fraud_category extraction
        result.__dict__["_top_category"] = top_category
        return result

    def _extract_fraud_category(self, l4: LayerResult) -> Optional[str]:
        """Extract top fraud category from L4 result."""
        return getattr(l4, "_top_category", None)

    # ── Layer 5: Absence Signal Detection ────────────────────────────────────

    def _layer5_absence_signals(self, text: str) -> LayerResult:
        """
        What is missing that should be present in genuine human communication?

        Real humans leak irrelevant humanity into messages.
        Synthetic messages are purpose-pure — every element serves the goal.

        Purpose-purity is a fraud signal.
        """
        t = text.lower()
        findings = []
        absence_score = 0.0

        # No acknowledgment of recipient's possible doubt
        doubt_acknowledgment = re.search(
            r"\b(i know (this|it) (sounds?|seems?|looks?|might seem)|(you might|i understand if you) (be|are|seem))\b",
            t, re.IGNORECASE
        )
        if not doubt_acknowledgment:
            absence_score += 0.15
            findings.append("No acknowledgment of recipient's possible doubt — unusual in genuine requests")

        # No genuine uncertainty about outcome
        outcome_uncertainty = re.search(
            r"\b(i (hope|think|believe) (this|it|you)|not sure (how|if|what)|might not)\b",
            t, re.IGNORECASE
        )
        if not outcome_uncertainty:
            absence_score += 0.15
            findings.append("No genuine uncertainty about outcome — synthetic messages assume compliance")

        # No off-purpose content whatsoever
        word_count = len(text.split())
        noise_hits = self._match_any(t, HUMAN_MARKERS["irrelevant_human_noise"])
        if word_count > 30 and not noise_hits:
            absence_score += 0.20
            findings.append("Message is purpose-pure — no irrelevant human content across full length")

        # No imperfect self-presentation
        imperfection = re.search(
            r"\b(sorry|apologi[sz]|excuse|forgive|i know i|not great at|bear with)\b",
            t, re.IGNORECASE
        )
        if not imperfection and word_count > 50:
            absence_score += 0.10
            findings.append("No imperfect self-presentation — genuine humans rarely present perfectly")

        if absence_score >= 0.40:
            signal = "synthetic"
            conf = min(0.55 + absence_score, 0.85)
            findings.insert(0, "Multiple absence signals detected")
        elif absence_score >= 0.20:
            signal = "uncertain"
            conf = 0.50
        else:
            signal = "uncertain"
            conf = 0.45
            findings.append("Absence signals insufficient to determine — message may be short")

        return LayerResult(
            layer="absence_signals",
            signal=signal,
            confidence=round(conf, 3),
            findings=findings,
        )

    # ── Signal aggregation ────────────────────────────────────────────────────

    def _aggregate_signal(
        self,
        layers: List[LayerResult],
        l4: LayerResult,
    ) -> Tuple[str, float, Dict[str, Any]]:
        """
        Aggregate five layer signals into final RED/YELLOW/GREEN.

        Governance rule: narrow interpretation.
        - Prefer false negatives (YELLOW) over false positives.
        - A false GREEN is the catastrophic failure mode.
        - Pattern library (L4) has veto power for strong matches.
        - GREEN requires majority human signal AND high confidence.
        - YELLOW with high spread = mixed content warning.
        """
        synthetic_votes = sum(1 for l in layers if l.signal == "synthetic")
        human_votes = sum(1 for l in layers if l.signal == "human")

        # Weighted confidence average (L4 pattern match weighted 2x)
        weights = [1.0, 1.0, 1.0, 2.0, 1.0]
        weighted_conf = sum(
            l.confidence * w for l, w in zip(layers, weights)
        ) / sum(weights)

        # Mixed content detection — high spread between layers signals
        # that some layers fired high and others low — the seam signature
        # of human-edited synthetic content.
        confidences = [l.confidence for l in layers]
        spread = max(confidences) - min(confidences)
        mixed_content_meta: Dict[str, Any] = {}
        if spread >= 0.40:
            mixed_content_meta = {
                "mixed_content_warning": True,
                "mixed_content_note": (
                    "Reasoning signals are internally inconsistent across layers. "
                    "This pattern is consistent with human-edited synthetic content — "
                    "AI scaffolding with human modifications. "
                    "Treat with significant caution."
                ),
                "layer_spread": round(spread, 3),
            }

        # L4 veto: strong pattern match alone can push to RED
        if l4.signal == "synthetic" and l4.confidence >= 0.75:
            if synthetic_votes >= 2:
                return "red", min(weighted_conf * 1.15, 0.95), mixed_content_meta

        # Majority synthetic
        if synthetic_votes >= 3:
            conf = weighted_conf
            if conf >= RED_THRESHOLD:
                return "red", conf, mixed_content_meta
            return "yellow", conf, mixed_content_meta

        # Majority human — requires HIGH confidence for GREEN
        if human_votes >= 3:
            conf = weighted_conf
            if conf >= GREEN_THRESHOLD:
                return "green", conf, mixed_content_meta
            return "yellow", conf, mixed_content_meta

        # Mixed or uncertain — default YELLOW
        # This is the correct behavior: uncertainty resolves to caution
        return "yellow", max(weighted_conf, YELLOW_LOW), mixed_content_meta

    # ── Output builders ───────────────────────────────────────────────────────

    def _plain_english(
        self,
        signal: str,
        confidence: float,
        fraud_category: Optional[str],
        mixed_meta: Optional[Dict[str, Any]] = None,
    ) -> str:
        pct = int(confidence * 100)
        mixed_meta = mixed_meta or {}

        if signal == "red":
            cat = fraud_category.replace("_", " ").title() if fraud_category else "Fraud"
            base = (
                f"No genuine human reasoning detected behind this message "
                f"({pct}% confidence). Pattern consistent with {cat}. "
                f"Treat with extreme caution."
            )
            if mixed_meta.get("mixed_content_warning"):
                base += (
                    " Note: reasoning signals show internal inconsistency — "
                    "this message may contain human-edited synthetic content."
                )
            return base

        if signal == "green":
            return (
                f"Human reasoning presence detected ({pct}% confidence). "
                f"Standard caution still applies — verify sender independently."
            )

        # Yellow
        if mixed_meta.get("mixed_content_warning"):
            return (
                f"Warning: reasoning signals are internally inconsistent ({pct}% confidence). "
                f"This pattern is consistent with human-edited synthetic content — "
                f"AI scaffolding with human modifications. "
                f"Do not respond until sender is independently verified."
            )
        if self.first_contact:
            return (
                f"Reasoning signal is unclear ({pct}% confidence) — "
                f"no prior communication history available for this sender. "
                f"Verify the sender independently before responding."
            )
        return (
            f"Mixed reasoning signals detected ({pct}% confidence). "
            f"Insufficient evidence to confirm human presence. "
            f"Do not act until sender is independently verified."
        )

    def _recommended_action(self, signal: str, confidence: float) -> str:
        """
        Non-prescriptive guidance. Does not tell user what to do —
        surfaces the question they should ask themselves.
        Consistent with Owlume governance: no advice, no instructions.
        """
        if signal == "red":
            return (
                "Before responding: can you verify this sender through an "
                "official channel completely independent of this message?"
            )
        if signal == "green":
            return (
                "Human presence indicators are present. "
                "Standard verification of sender identity still recommended."
            )
        return (
            "Before responding or acting: verify the sender's identity "
            "through a channel you established yourself, not one provided "
            "in this message."
        )

    def _analyst_questions(
        self,
        layers: List[LayerResult],
        message: str,
        context_hint: Optional[str],
        mixed_meta: Optional[Dict[str, Any]] = None,
    ) -> List[str]:
        """
        Generate questions for human analyst follow-up.
        These are the questions a fraud analyst or concerned recipient
        should investigate — not conclusions.
        """
        mixed_meta = mixed_meta or {}
        questions = []

        # Always include the core verification question
        questions.append(
            "Can the sender be verified through an official channel "
            "completely independent of this message?"
        )

        # Mixed content specific question — surfaces the seam
        if mixed_meta.get("mixed_content_warning"):
            questions.append(
                "This message shows signs of being partially written by AI and "
                "partially by a human. Which sections feel genuinely personal — "
                "and which feel templated or too perfectly structured?"
            )

        # Layer-specific questions
        for layer in layers:
            if layer.signal == "synthetic" and layer.confidence >= 0.65:
                if layer.layer == "structural_reasoning":
                    questions.append(
                        "Does the urgency in this message feel earned by the "
                        "circumstances — or was it inserted to prevent careful thinking?"
                    )
                elif layer.layer == "contextual_plausibility":
                    questions.append(
                        f"Would a real {context_hint or 'person'} in this situation "
                        f"actually communicate this way?"
                    )
                elif layer.layer == "conviction_cost":
                    questions.append(
                        "Does the sender show any evidence of personal stakes, "
                        "doubt, or reluctance — or is their confidence completely costless?"
                    )
                elif layer.layer == "pattern_library":
                    questions.append(
                        "Have you seen this type of message before — "
                        "and what happened to people who acted on it?"
                    )
                elif layer.layer == "absence_signals":
                    questions.append(
                        "Does this message contain anything that serves no "
                        "persuasive purpose — or is every element working toward one goal?"
                    )

        # First contact warning
        if self.first_contact:
            questions.append(
                "This is the first communication from this sender. "
                "Why is this person contacting you now, through this channel?"
            )

        return questions[:5]  # Cap at 5 for usability

    # ── Utilities ─────────────────────────────────────────────────────────────

    def _match_any(self, text: str, patterns: List[str]) -> List[str]:
        """Return list of patterns that match in text."""
        return [p for p in patterns if re.search(p, text, re.IGNORECASE)]

    def _empty_result(self) -> ScanResult:
        return ScanResult(
            scan_id=str(uuid.uuid4()),
            timestamp=dt.datetime.utcnow().isoformat() + "Z",
            signal="yellow",
            confidence=0.0,
            first_contact=True,
            layers=[],
            fraud_category=None,
            plain_english="No message provided for analysis.",
            recommended_action="Please provide the suspicious message text.",
            analyst_questions=[],
            meta={"error": "empty_input"},
        )


# ── Convenience function ──────────────────────────────────────────────────────

def scan_message(
    message: str,
    context_hint: Optional[str] = None,
    bse_history: Optional[Dict[str, Any]] = None,
) -> ScanResult:
    """
    Convenience wrapper for single message scanning.

    Args:
        message: The suspicious communication text.
        context_hint: Optional claimed context e.g. "bank_officer".
        bse_history: Optional longitudinal BSE data for this sender.

    Returns:
        ScanResult
    """
    scanner = HumanTraceScanner(bse_history=bse_history)
    return scanner.scan(message, context_hint=context_hint)