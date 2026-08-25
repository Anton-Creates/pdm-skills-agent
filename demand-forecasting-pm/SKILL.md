---
name: demand-forecasting-pm
description: Разработать продуктовые требования к системе прогнозирования спроса (Demand Forecasting) в ритейле.
argument-hint: [категории товаров и структура данных ритейлера для прогнозирования спроса]
allowed-tools: Read, Write
preset: ecom-retail
lifecycle: any
business-model: any
domain: ecom-retail
stage: any
output-artifact: document
---

# Прогнозирование спроса в ритейле (demand-forecasting-pm)

Сформировать требования к ML-системе прогнозирования спроса для оптимизации товарных запасов на складах и предотвращения дефицита (out-of-stock) или избытка (overstock).

## Процесс
1. **Определи входные признаки (Features) для модели.** История продаж, промо-акции, сезонность, праздничные дни, погода.
2. **Установи метрики точности прогноза (Forecast Accuracy).** MAPE (Mean Absolute Percentage Error), WAPE.
3. **Опиши логику автозаказа (Replenishment).** Как прогноз спроса трансформируется в автоматический заказ поставщикам.
4. **Сохрани вывод** в текущей рабочей директории как `demand-forecasting-pm-[контекст].md`.

## Формат вывода
```
## Спецификация системы прогнозирования спроса
- **Входные данные модели:** продажи за 3 года по дням, календарь промо-механик, остатки товаров.
- **Целевая метрика точности (WAPE):** < 15% для сухой бакалеи, < 25% для категории фреш (скоропортящиеся товары).
- **Сценарий отката (Fallback):** при сбое ML-модели заказ формируется по средним продажам за последние 4 недели.
```

## Метрики (E-commerce / Retail)

### Outcome metric
**contribution margin per order, repeat purchase, paid orders.** Главный результат и ценность.

### Input metrics
**checkout conversion, add-to-cart, availability, delivery promise accuracy, promo conversion.** Управляемые рычаги outcome.

### Guardrails
**gross margin after returns, refund rate, return abuse, stockout, payment failure.** Что нельзя ухудшить.

### Diagnostic metrics
**funnel drop-off, category, device, payment method, delivery slot, promo dependency.** Где искать причину.

### Instrumentation
**cart_id, order_id, SKU, inventory, payment events, return/refund reason.** Какие данные нужны.

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
