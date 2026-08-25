---
name: hrtech-spec
description: Develop a specification for an HRtech product taking into account the requirements of labor law and personal data protection.
argument-hint: [description of HRtech solution (onboarding, reviews, evaluation)]
allowed-tools: Read, Write
preset: enterprise-gov
lifecycle: any
business-model: any
domain: generic
stage: any
output-artifact: document
---

# HRtech products (hrtech-spec)

Design a specification for an IT solution in the field of personnel management (HRtech), taking into account the compliance requirements of the Labor Code of the Russian Federation and 152-FZ.

## Process
1. **Describe the roles of the participants.** Employee, HR manager, Manager.
2. **Comply with regulatory compliance.** Signing consents for personal data processing, integration with HR electronic document management.
3. **Develop an onboarding or assessment funnel.**
4. **Save the output** in the current working directory as `hrtech-spec-[context].md`.

## Output Format
```
## HRtech module specification: [Name]
- **Legal compliance:** signing non-disclosure documents (NDA) and consents to process personal data through KEDO State Services.
- **Role model:** differentiation of the access rights of managers to the assessments of subordinates.
```


## Rules

- Write in English.
## Metrics

### Universal Metric Rule
If you propose a metric, answer these 5 questions:
1. **Who owns this metric?**
2. **How often do we track it?**
3. **What events calculate it?**
4. **What is the decision threshold?**
5. **How can it be gamed or corrupted?