---
name: monetization-audit
description: Провести аудит текущей модели монетизации и выявить упущенную выгоду.
argument-hint: [описание бизнес-модели, цен и текущих доходов]
allowed-tools: Read, Write
preset: growth
lifecycle: any
business-model: any
domain: saas
stage: any
output-artifact: document
---

# Аудит монетизации (monetization-audit)

Провести аудит финансовой эффективности продукта, найти зоны утечки выручки (revenue leakage) и определить возможности для внедрения новых моделей (add-ons, комиссии, подписки).

## Процесс
1. **Опиши текущие потоки выручки (Revenue Streams).**
2. **Выяви немонетизируемую ценность.** За какие ценные фичи пользователи активно пользуются, но не платят?
3. **Предложи 3 гипотезы оптимизации цен/пакетов.**
4. **Сохрани вывод** в текущей рабочей директории как `monetization-audit-[контекст].md`.

## Формат вывода
```
## Аудит монетизации: [Название]
- **Текущая модель:** [описание]
- **Зоны потерь ценности:** [где отдаем бесплатно то, за что готовы платить]
- **Гипотезы по росту LTV:** [новые аддоны, комиссии за транзакции].
```

## Метрики (SaaS)

### Outcome metric
**NRR, retained ARR/MRR, active paying accounts.** Главный результат и ценность.

### Input metrics
**activation rate, time-to-value, feature adoption, seats used, integrations connected.** Управляемые рычаги outcome.

### Guardrails
**GRR, logo churn, support load, gross margin, implementation time.** Что нельзя ухудшить.

### Diagnostic metrics
**cohort retention by segment, churn reasons, expansion/contraction bridge, account health score.** Где искать причину.

### Instrumentation
**account_id, plan, seats, feature events, billing events, CRM segment.** Какие данные нужны.

### Decision rules
- Ship / Iterate / Kill

### Универсальное правило метрики
Если вы предлагаете метрику, ответьте на 5 вопросов:
1. **Кто владеет этой метрикой?**
2. **Как часто её смотрим?**
3. **Какие события её считают?**
4. **Какой порог решения?**
5. **Как её можно испортить или накрутить?**

## Правила

- Пиши на русском языке.
