---
name: product-operating-model
description: Спроектировать operating model продуктовой организации: роли, decision rights, ритуалы, метрики, cadence, governance и связь стратегии с delivery. На выходе — модель управления продуктом для команды/направления.
argument-hint: [описание продуктовой организации, команд, проблем управления]
allowed-tools: Read, Write
preset: strategy
lifecycle: operations,strategy
business-model: any
domain: any
stage: scale,mature,turnaround
output-artifact: product-operating-model
---

# Product Operating Model

Спроектировать, как продуктовая организация принимает решения, связывает стратегию с roadmap, управляет метриками и эскалирует trade-offs.

## Формат вывода

```md
## Product Operating Model: [Организация]

### 1. Текущая проблема управления
### 2. Product Principles
### 3. Roles and Decision Rights
| Решение | Owner | Contributors | Approver | Cadence |
|---|---|---|---|---|

### 4. Rituals and Cadence
### 5. Metrics Governance
### 6. Portfolio / Roadmap Governance
### 7. Escalation Rules
### 8. Implementation Plan
```

## Правила

- Не проектируй ритуалы без decision rights.
- Если непонятно, кто принимает решение, operating model не работает.
- Пиши на русском языке.

## Метрики

### Универсальное правило метрики
Если вы предлагаете метрику, ответьте на 5 вопросов:
1. **Кто владеет этой метрикой?**
2. **Как часто её смотрим?**
3. **Какие события её считают?**
4. **Какой порог решения?**
5. **Как её можно испортить или накрутить?**