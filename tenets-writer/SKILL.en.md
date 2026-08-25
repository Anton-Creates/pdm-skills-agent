---
name: tenets-writer
description: Formulate product tenets — decision-making principles that protect the essence of the product during growth, scaling, and trade-offs. The output is a table of principles, risks of violation, checks, and guardrail metrics.
argument-hint: [description of the product, values, risks, and controversial decisions]
allowed-tools: Read, Write
preset: strategy
lifecycle: strategy,operations
business-model: any
domain: any
stage: idea,mvp,pre-pmf,pmf,scale
output-artifact: product-tenets
---

# Product Tenets Writer

Formulate not slogans, but practical principles by which the team will make difficult decisions.

## Output Format

```md
## Product Tenets: [Product]

| Principle | Why critical | Where risk of violation | How to check | Guardrail |
|---|---|---|---|---|
| | | | | |
```

## Rules

- Tenet should help in choosing between two good options.
- Every principle should have a check and a guardrail.
- Don't write abstractions like 'customer at the center' if it's unclear what decision this changes.
- Write in English.

## Metrics

### Universal Metric Rule
If you are suggesting a metric, answer 5 questions:
1. **Who owns this metric?**
2. **How often do we watch it?**
3. **Which events consider her?**
4. **What is the decision threshold?**
5. **How can it be spoiled or manipulated?**