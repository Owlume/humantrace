# Doctrine

This directory contains **non-negotiable doctrinal constraints** that govern Owlume itself.

Files in this directory do **not** describe behavior to be optimized, tuned, learned, or expanded.  
They define **limits** within which Owlume must operate.

Doctrine precedes implementation.

---

## What Doctrine Is

Doctrine defines:
- structural boundaries on judgment,
- classifications that are treated as closed,
- constraints that apply regardless of context, model, or runtime.

Doctrine is **normative**, not empirical.

It does not emerge from usage data, telemetry, or model behavior.
It is not revised through iteration, feedback, or performance metrics.

---

## What Doctrine Is Not

Doctrine is **not**:
- a dataset,
- a heuristic library,
- a prompt strategy,
- a taxonomy for model training,
- or an output classification scheme.

Files here must never contain:
- probabilities,
- weights,
- confidence scores,
- learning hooks,
- or expansion points.

If a concept requires tuning, it does not belong here.

---

## Authority and Precedence

Doctrine files take precedence over:
- runtime behavior,
- configuration files,
- model outputs,
- and learned patterns.

If a conflict arises between:
- a doctrinal definition, and
- any other system component,

**the doctrinal definition prevails.**

---

## Closed Sets

Some doctrinal classifications are explicitly **closed**.

For closed sets:
- no new elements may be added,
- no elements may be removed,
- no elements may be merged or split,
- and no ranking or weighting may be introduced.

Any newly observed phenomenon must be:
- mapped to an existing element, or
- excluded as outside the scope of the doctrine.

---

## Example: Reading Failure Types

The file `reading_failure_types.md` defines a closed set of fourteen reading failure types.

These types:
- are not discovered by Owlume,
- are not inferred from usage,
- and are not adaptable by the system.

Owlume operates **under** these constraints.
It may detect signals related to them and intervene accordingly,
but it may not invent, modify, or prioritize them.

---

## Change Policy

Changes to doctrine require:
- explicit justification at the architectural level,
- review for scope creep and circularity,
- and confirmation that the change does not convert constraint into heuristic.

Absent such justification, doctrine is treated as **stable**.

---

## Design Principle

Doctrine exists to **limit system power**, not to increase it.

By constraining what Owlume is allowed to infer, generate, or optimize,
doctrine preserves:
- interpretability,
- responsibility,
- and human judgment ownership.

---

## Doctrinal Constraints

Some documents under `docs/doctrine/` define **non-negotiable constraints** that govern Owlume itself.

These materials are normative rather than descriptive:
- they are not learned from data,
- not tuned through iteration,
- and not expanded through usage.

Doctrine exists to limit system behavior, not to document features.

---

## Final Note

If you are unsure whether something belongs in this directory, it probably does not.

Doctrine is rare by design.
