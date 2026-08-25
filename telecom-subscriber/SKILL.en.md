## Metrics

### Universal Metric Rule
If you are suggesting a metric, answer 5 questions:
1. **Who owns this metric?**
2. **How often do we watch it?**
3. **Which events consider her?**
4. **What is the decision threshold?**
5. **How can it be spoiled or manipulated?**
---
name: telecom-subscriber
description: Design a B2C product for a telecom operator — a tariff plan, a convergent bundle (internet+TV+mobile), anti-churn or upsell. Input — segment and operator context, output — product structure, pricing logic, and retention metrics.
argument-hint: [description of the subscriber segment, current tariff/service, problem or goal]
allowed-tools: Read, Write
preset: telecom
lifecycle: any
business-model: subscription
domain: telecom
stage: any
output-artifact: document
---

# B2C products of a telecom operator (telecom-subscriber)

Design a consumer product for a telecom operator: a tariff plan, a convergent service package (internet + TV + mobile), a retention mechanism (anti-churn) or an upsell to a premium package. This skill helps a product manager work with the specifics of the subscriber business: high churn, price sensitivity, the role of the call center, and cross-selling.

## Process

1. **Clarify the context:**
- **Product type:** New tariff / Bundle (convergent package) / Anti-churn / Upsell / Loyalty program.
- **Segment:** Individuals (B2C mass market / premium) or households.
- **Current situation:** What does the subscriber currently have? What is the average ARPU? What is the churn rate?
- **Goal:** Reduce churn / Increase ARPU / Convert to a bundle / Launch a new service.

2. **Design the product logic:**

**For the new tariff/bundle:**
- Determine the anchor service — what is the main thing in the package for the subscriber.
- Calculate the discount on the bundle vs individual services — it should be significant (≥15%).
- Design a “switching costs” trap: the discount is only active if all package services are included.
- Determine the connection conditions: online / call center / dealer network.

**For anti-churn (Anti-Churn):**
- Identify churn triggers (decline in usage, expired contract, support complaints).
- Design a retention offer: personal discount / speed upgrade / free month.
- Determine the cohort for proactive calling (propensity-to-churn scoring).
- Set the request window: 30 days before the contract ends.

**For upsell:**
- Identify the upsell trigger: reaching the speed limit, increased TV usage, purchasing a new device.
- Design an offer: upgrade without service interruption, minimal price difference.
- Choose a channel: push in the personal account / call center / SMS / in-app.

3. **Calculate the unit economics:**
- **ARPU** before and after switching to the new plan.
- **CAC** (cost of acquisition/conversion): call center is expensive (500-2000 rubles), online is cheap (<100 rubles).
- **LTV** = ARPU × average subscriber lifetime — show how the bundle increases LTV.
- **Churn rate** target: a reduction of X% gives Y million rubles of additional revenue.

4. **Define the pilot metrics:**
- Conversion to bundle (% of offered).
- ARPU delta (increase in average check).
- Churn rate after 3/6/12 months following the transition.
- NPS after contacting the call center.
5. **Save the output** in the current working directory as `telecom-subscriber-[context].md`.

## Output Format

```
## Product Specification: [Name of the tariff/bundle/mechanic]

### Product Description
- **Type:** [Bundle / Plan / Anti-churn offer / Upsell]
- **Target Segment:** [description]
- **Anchor service:** [internet / TV / mobile]

### Package Contents
| Service | Parameters | Price separately | Price in bundle |
|--------|-----------|---------------|---------------|
| Internet | 500 Mbps | 800 RUB/month | — |
| TV | 200 channels, 4K | 400 RUB/month | — |
| **Bundle** | All inclusive | 1200 rub./month | **990 rub./month** |

### Unit Economics
- ARPU before: [X] rub. → ARPU after: [Y] rub. (+Z%)
- CAC: [amount] RUB (channel: [online/call center])
- Payback period: [N] months

### Pilot Success Metrics
- Conversion to bundle ≥ [X%]
- Churn in 6 months ≤ [Y%]
- NPS ≥ [Z]
```

## Rules and Restrictions
- The bundle discount versus individual services should be significant — otherwise, there is no motivation to switch.
- The retention offer should not be visible to new subscribers — otherwise, everyone will 'leave' for the discount.
- Anti-churn scoring is more important than mass calling: don't bother loyal customers, don't annoy them.
- Take into account the regulations: prohibition of auto-subscriptions without explicit consent (Federal Law 'On Communications').

## Skill Success Metrics
- The specification contains the calculation of ARPU delta and payback period.
- There is a clear distinction: what the subscriber gets and why it is better than the current plan.
- A retention offer does not create adverse selection (only those who are leaving receive a discount).

## Rules


- Write in English.