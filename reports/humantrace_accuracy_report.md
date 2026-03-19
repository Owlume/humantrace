# HumanTrace Accuracy Validation Report
*Generated: 2026-03-19T23:49:18.442743Z*

## Summary

| Metric | Result | Target | Status |
|--------|--------|--------|--------|
| Overall accuracy | 78.3% | — | — |
| Synthetic fraud detection | 85.0% | ≥80% | ✅ |
| False positive rate | 6.7% | <15% | ✅ |
| Mixed content detection | 90.0% | ≥70% | ✅ |

## By Category

| Category | Total | Correct | Accuracy |
|----------|-------|---------|----------|
| synthetic_fraud | 20 | 17 | 85.0% |
| genuine_human | 20 | 20 | 100.0% |
| mixed_content | 10 | 2 | 20.0% |
| edge_case | 10 | 8 | 80.0% |

## False Positives

- EC002 (confidence: 0.70)
- EC007 (confidence: 0.80)

## Missed Fraud

- SF006 predicted yellow (confidence: 0.57)
- SF008 predicted yellow (confidence: 0.57)
- SF013 predicted yellow (confidence: 0.57)

---
*HumanTrace — Powered by Owlume*
