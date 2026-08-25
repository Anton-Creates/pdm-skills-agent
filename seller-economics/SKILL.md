---
name: seller-economics
description: Разработать калькулятор юнит-экономики и прибыльности продавца (Seller Economics) на маркетплейсе.
argument-hint: [структура комиссий маркетплейса, логистика и реклама]
allowed-tools: Read, Write
preset: marketplace
lifecycle: any
business-model: any
domain: marketplace
stage: any
output-artifact: document
---

# Экономика продавца маркетплейса (seller-economics)

Спроектировать калькулятор затрат и прибыльности продавца (Seller Economics) для оценки его маржинальности с учетом всех комиссий платформы.

## Процесс
1. **Опиши структуру комиссий.** Комиссия за продажу по категориям (take rate), плата за хранение (storage fee), доставка до клиента (last mile), обработка возвратов.
2. **Рассчитай чистую маржу продавца.**
3. **Сохрани вывод** в текущей рабочей директории как `seller-economics-[контекст].md`.

## Формат вывода
```
## Калькулятор экономики продавца: [Категория товара]
- **Розничная цена:** 1000 руб.
- **Комиссия платформы (15%):** 150 руб.
- **Логистика (доставка + хранение):** 120 руб.
- **Чистая выручка продавца (Net Payout):** 730 руб.
```

## Метрики (Marketplace / Classifieds)

### Outcome metric
**successful transactions/matches, GMV with healthy take rate, liquidity.** Главный результат и ценность.

### Input metrics
**supply coverage, demand coverage, search success, time-to-first-match, reply rate.** Управляемые рычаги outcome.

### Guardrails
**seller margin, dispute rate, cancellation rate, fraud rate, leakage/disintermediation.** Что нельзя ухудшить.

### Diagnostic metrics
**liquidity by geo/category/price/time, supply quality, buyer conversion, seller activation.** Где искать причину.

### Instrumentation
**buyer_id, seller_id, listing_id, category, geo, search_id, contact/match/transaction events.** Какие данные нужны.

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
