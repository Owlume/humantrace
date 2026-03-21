# HumanTrace

**Tells you if a real human sent that message — before you respond.**

HumanTrace verifies whether genuine human reasoning is present behind a written communication. It is not a style detector. It does not look for "AI-sounding" language. It measures structural signals that are difficult for synthetic text to replicate — and returns a single verdict: 🔴 RED / 🟡 YELLOW / 🟢 GREEN.

---

## What problem it solves

AI-generated messages, documents, and loan applications are now indistinguishable from genuine ones by style alone. Traditional fraud detection looks for inconsistencies in data. HumanTrace looks at the reasoning behind the words.

The fraud risk is not that AI writes imperfect English. The risk is that AI writes perfect English with no human behind it.

---

## How it works

HumanTrace analyses five layers of reasoning signal:

| Layer | What it measures |
|-------|-----------------|
| Structural coherence | Whether sentence structure is consistent with a single author |
| Conviction cost | Whether the author demonstrates personal stakes in the outcome |
| Contextual plausibility | Whether named entities are specific and internally consistent |
| Pattern library | Whether phrasing matches known synthetic patterns |
| Absence signals | What is missing — hedging, contradiction, idiosyncratic detail |

For institutional use (loan applications, document batches), HumanTrace adds:

- **Cross-document consistency scoring** — five dimensions across all documents in a single application
- **Cross-application BSE matching** — detecting the same reasoning fingerprint appearing under different identities across multiple applications

---

## Product lines

| Product | User | Use case |
|---------|------|----------|
| HumanTrace Consumer | Individual | Single suspicious message — paste, screenshot, or URL |
| HumanTrace Institutional | Loan manager / fraud analyst | Document batch + cross-application cluster detection |

---

## Governance

HumanTrace returns signals only. It never makes decisions.

Every output carries the acknowledgment: *"Human judgment required. HumanTrace did not decide."*

The audit trail records the analyst as the decision-maker. Output kind: `SIGNAL` — not advice, not instruction, not recommendation.

---

## Status

Currently in private pilot. Validated accuracy on a 60-message labelled dataset:

| Metric | Result | Target |
|--------|--------|--------|
| Synthetic fraud detection | 85% | ≥80% ✅ |
| False positive rate | 6.7% | <15% ✅ |
| Mixed content detection | 90% | ≥70% ✅ |
| Genuine human accuracy | 100% | — ✅ |

---

## Powered by

**Owlume** — reasoning clarity infrastructure.

Owlume is the engine. HumanTrace is the product.

---

## Contact

[humantrace.au](https://humantrace.au)

---

*This repository is private. Code, architecture, and signal weights are proprietary.*
