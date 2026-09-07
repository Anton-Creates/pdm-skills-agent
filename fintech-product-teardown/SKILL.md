---
name: fintech-product-teardown
description: Провести глубокий разбор финтех-продукта (FinTech Product Teardown) с учетом регуляторных рамок и монетизации.
argument-hint: [название финтех-продукта или сервиса для разбора]
allowed-tools: Read, Write
preset: fintech
lifecycle: any
business-model: any
domain: fintech
stage: any
output-artifact: document
---

# Разбор финтех-продукта (fintech-product-teardown)

Провести детальный разбор финтех-решения, анализируя его регуляторные рамки (ЦБ РФ, лицензирование), архитектуру движения денег и модель рисков.

## Процесс
1. **Анализ движения денег (Money Flow).** Откуда поступают средства, где хранятся (номинальные счета, эскроу), как списываются комиссии.
2. **Регуляторный комплаенс.** Лицензии (ЦБ, НКО, банк), соблюдение 115-ФЗ (ПОД/ФТ).
3. **Модель рисков.** Кредитный риск, операционный риск, фрод.
4. **Сохрани вывод** в текущей рабочей директории как `fintech-product-teardown-[контекст].md`.

## Формат вывода
```
## Финтех-разбор продукта: [Название]
- **Тип лицензии:** [Банковская / НКО / Агент]
- **Архитектура движения денег:** [номинальные счета, шлюзы эквайринга]
- **Соблюдение 115-ФЗ:** автоматический скоринг операций на подозрительность.
```

## Метрики (Fintech / Lending)

### Outcome metric
**risk-adjusted profit, approved good customers, portfolio margin.** Главный результат и ценность.

### Input metrics
**KYC pass rate, approval rate by risk bucket, time-to-decision, utilization.** Управляемые рычаги outcome.

### Guardrails
**NPL 30/60/90, fraud loss, complaints, regulatory breaches, manual review overload.** Что нельзя ухудшить.

### Diagnostic metrics
**vintage analysis, PD/LGD, funnel by segment, false positives/negatives, channel quality.** Где искать причину.

### Instrumentation
**application_id, risk bucket, decision, KYC steps, repayment/vintage data, fraud flags.** Какие данные нужны.

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
