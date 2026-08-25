---
name: loyalty-program
description: Спроектировать экосистемную программу лояльности на основе балльного кэшбэка.
argument-hint: [параметры экосистемы или холдинга для программы лояльности]
allowed-tools: Read, Write
preset: ecom-retail
lifecycle: any
business-model: any
domain: ecom-retail
stage: any
output-artifact: document
---

# Экосистемные программы лояльности (loyalty-program)

Спроектировать экономику и правила работы кросс-продуктовой программы лояльности (например, Яндекс Плюс, СберСпасибо, МТС Cashback) для удержания клиентов внутри холдинга.

## Процесс
1. **Спроектируй коалиционные правила начисления.** За какие действия в сервисе А начисляются баллы, которые можно потратить в сервисе Б.
2. **Определи экономические лимиты (Funding Pool).** Из чьей маржинальности финансируются баллы.
3. **Опиши метрики.** Redemption Rate, Churn Rate участников программы лояльности по сравнению с обычными пользователями.
4. **Сохрани вывод** в текущей рабочей директории как `loyalty-program-[контекст].md`.

## Формат вывода
```
## Концепт экосистемной лояльности: [Название]
- **Балльный баланс:** единый счет баллов во всех приложениях экосистемы.
- **Funding Pool:** 70% финансирования баллов идет за счет маржи сервиса-донора, 30% — из рекламных бюджетов партнеров.
- **Redemption Rate цель:** > 75% в течение первого года.
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
