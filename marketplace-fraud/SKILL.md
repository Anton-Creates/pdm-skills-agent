---
name: marketplace-fraud
description: Спроектировать систему защиты от мошенничества (Anti-Fraud) на маркетплейсе.
argument-hint: [типы мошенничества на маркетплейсе: накрутка отзывов, фейковые продавцы]
allowed-tools: Read, Write
preset: marketplace
lifecycle: any
business-model: any
domain: marketplace
stage: any
output-artifact: document
---

# Борьба с фродом на маркетплейсах (marketplace-fraud)

Спроектировать систему детекции и предотвращения мошеннических действий покупателей и продавцов на двусторонней торговой платформе.

## Процесс
1. **Выяви виды фрода.** Накрутка отзывов (самовыкупы), фейковые трек-номера, подмена оригиналов подделками на ПВЗ.
2. **Разработайте правила детекции.** Ограничения по одному IP/карте, паттерны поведения в приложении.
3. **Сохрани вывод** в текущей рабочей директории как `marketplace-fraud-[контекст].md`.

## Формат вывода
```
## Спецификация маркетплейс-антифрода: [Название]
- **Детекция самовыкупов:** блокировка выплат при аномально высокой конверсии из клика в покупку с одной карты.
- **Контроль отзывов:** отзывы публикуются только после физического подтверждения выдачи товара на ПВЗ.
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
