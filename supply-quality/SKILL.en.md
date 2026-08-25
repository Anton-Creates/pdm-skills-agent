---
name: supply-quality
description: Design a system for controlling the quality of offerings (Supply Quality) and verification on the marketplace.
argument-hint: [type of marketplace and description of the problem with product/service quality]
allowed-tools: Read, Write
preset: marketplace
lifecycle: any
business-model: any
domain: marketplace
stage: any
output-artifact: document
---

# Quality of the offer on the marketplace (supply-quality)

Design a system for merchant/partner verification and quality control of the product or service catalog on a two-sided marketplace.

## Process
1. **Design onboarding compliance (KYC/KYB).** Verification of legal entities, licenses, brand originality.
2. **Define seller quality metrics.** Listing Quality Score, shipping speed, return rate, review rating.
3. **Develop a system of fines and boosting.** Promotion in the ranking of quality sellers and demotion/blocking of violators.
4. **Save the output** in the current working directory as `supply-quality-[context].md`.

## Output Format
```
## Supply Quality Specification: [Marketplace Name]

### 1. Seller Verification Rules (KYB/KYC)
- Documents for the start: OGRN, INN, certificates of conformity for brands.
- Automatic verification against the Federal Tax Service registers.

### 2. Seller Quality Score (SQS) Specification
How the seller quality rating is calculated:
- **SQS Rating (0-100%):** `0.4 * Rating + 0.3 * SLA_Shipment + 0.3 * (1 - Return_Rate)`.
- *Pessimization:* a 20% decrease in impressions when SQS < 70%.
- *Locking:* disabling the cabinet when SQS < 50%.
```

## Metrics (Marketplace / Classifieds)

### Outcome metric
**successful transactions/matches, GMV with healthy take rate, liquidity.** The main result and value.

### Input metrics
**supply coverage, demand coverage, search success, time-to-first-match, reply rate.** Managed levers of outcome.

### Guardrails
**seller margin, dispute rate, cancellation rate, fraud rate, leakage/disintermediation.** What cannot be worsened.

### Diagnostic metrics
**liquidity by geo/category/price/time, supply quality, buyer conversion, seller activation.** Where to look for the cause.

### Instrumentation
**buyer_id, seller_id, listing_id, category, geo, search_id, contact/match/transaction events.** What data is needed.

### Decision rules
- Ship / Iterate / Kill

### Universal Metric Rule
If you are suggesting a metric, answer 5 questions:
1. **Who owns this metric?**
2. **How often do we watch it?**
3. **Which events consider her?**
4. **What is the decision threshold?**
5. **How can it be spoiled or manipulated?**

## Rules

- Write in English.