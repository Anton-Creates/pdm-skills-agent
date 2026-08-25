---
name: c2c-dynamics
description: Спроектировать баланс C2C-ликвидности, рейтинги и локальные сетевые эффекты.
argument-hint: [описание C2C платформы и проблемы ликвидности в регионах]
allowed-tools: Read, Write
preset: marketplace
lifecycle: any
business-model: any
domain: marketplace
stage: any
output-artifact: document
---

# Динамика C2C платформ (c2c-dynamics)

Оптимизировать баланс спроса и предложения на пиринговых (C2C) платформах с учетом локальных сетевых эффектов.

## Процесс
1. **Определи критическую массу ликвидности (Liquidity Threshold).** Какое число объявлений/исполнителей нужно в гео-зоне, чтобы покупатель нашел услугу.
2. **Спроектируй систему рейтингов и отзывов.** Защита от накруток, сглаживание оценок новых пользователей.
3. **Сохрани вывод** в текущей рабочей директории как `c2c-dynamics-[контекст].md`.

## Формат вывода
```
## Анализ C2C ликвидности: [Сервис]
- **Критический радиус доступности:** [например, 5 км для шеринга самокатов].
- **Механика стимулирования ликвидности:** повышенные бонусы для продавцов в дефицитных зонах.
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
