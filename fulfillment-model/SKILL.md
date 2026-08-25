---
name: fulfillment-model
description: Разработать стратегию логистики маркетплейса: сравнение и выбор моделей FBO, FBS, DBS.
argument-hint: [параметры товаров, ограничения по доставке и цели маркетплейса]
allowed-tools: Read, Write
preset: marketplace
lifecycle: any
business-model: any
domain: marketplace
stage: any
output-artifact: document
---

# Логистические модели маркетплейса (fulfillment-model)

Сравнить и спроектировать оптимальный микс логистических моделей (FBO - продажи со склада маркетплейса, FBS - склад продавца + доставка маркетплейса, DBS - доставка силами продавца).

## Процесс
1. **Проанализируй категории товаров.** Вес, габариты, оборачиваемость, температурный режим.
2. **Сделай финансовое сравнение моделей.** Влияние скорости доставки на конверсию карточки товара.
3. **Сформулируй правила выбора модели для продавцов.**
4. **Сохрани вывод** в текущей рабочей директории как `fulfillment-model-[контекст].md`.

## Формат вывода
```
## Спецификация логистической модели: [Продукт]
- **Модель FBO (склад платформы):** для высокооборотистых товаров (топ-20% SKU).
- **Модель FBS (склад продавца):** для низкооборотистых и крупногабаритных товаров.
- **Влияние на конверсию:** доставка со склада платформы (FBO) повышает конверсию карточки на 15-20% за счет быстрой доставки.
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
