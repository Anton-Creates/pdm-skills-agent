---
name: intranet-product
description: Design a corporate intranet portal: navigation, search and information architecture.
argument-hint: [concept of a corporate portal or company intranet]
allowed-tools: Read, Write
preset: enterprise-gov
lifecycle: any
business-model: any
domain: generic
stage: any
output-artifact: document
---

# Corporate intranet (intranet-product)

Design the architecture and services of a corporate intranet portal for company employees (search for contacts, ordering certificates, internal news).

## Process
1. **Design a global search (Enterprise Search).** Search for colleagues by name, department, skills or internal documents.
2. **Describe the structure of self-service services.** Ordering 2-NDFL certificates, coordinating vacations, booking meeting rooms.
3. **Define metrics.** Portal DAU/MAU, service satisfaction (CSAT).
4. **Save the output** in the current working directory as `intranet-product-[context].md`.

## Output Format
```
## Intranet portal specification: [Name]
- **Global search:** integration with Active Directory (AD) to automatically update your contact database.
- **Self-service service:** automated sending of a vacation request to 1C: ZUP.
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