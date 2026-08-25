---
name: trust-safety
description: Develop a security and trust strategy (Trust & Safety) for a C2C marketplace or sharing platform.
argument-hint: [description of a C2C platform and key fraud risks]
allowed-tools: Read, Write
preset: marketplace
lifecycle: any
business-model: any
domain: marketplace
stage: any
output-artifact: document
---

# Safety and Trust C2C (trust-safety)

Design a set of measures to protect users from fraud, deception, and data theft on a C2C platform (housing rental, sale of used goods, finding service providers).

## Process
1. **Identify attack and fraud vectors.** Bypassing the payment system (diversion to messengers), fake ads, account takeover.
2. **Design a user verification system (KYC).** Integration with Gosuslugi/ESIA, verification by passport/selfie.
3. **Develop a secure deal (Escrow).** Holding funds, dispute arbitration.
4. **Save the output** in the current working directory as `trust-safety-[context].md`.

## Output Format
```
## Trust & Safety Specification: [Platform Name]

### 1. Fraud Vectors and Defense Mechanisms
- **Risk:** leading the buyer to Telegram and sending a phishing link.
- *Protection:* auto-blocking of phone numbers and links in the platform chat, warning banner when the words 'WhatsApp, Telegram, switch' are detected.

### 2. Mechanics of a Secure Transaction
- The buyer's money is frozen by the escrow bank.
- Payment to the seller occurs only after confirmation by the pickup point or by the buyer within 24 hours.
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