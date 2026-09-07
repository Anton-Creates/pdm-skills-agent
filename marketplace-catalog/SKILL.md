---
name: marketplace-catalog
description: Разработать стратегию управления каталогом и таксономией маркетплейса.
argument-hint: [описание структуры товаров/услуг маркетплейса]
allowed-tools: Read, Write
preset: marketplace
lifecycle: any
business-model: any
domain: marketplace
stage: any
output-artifact: document
---

# Управление каталогом маркетплейса (marketplace-catalog)

Спроектировать таксономию категорий товаров/услуг, структуру карточек товаров и правила модерации контента для маркетплейса.

## Процесс
1. **Разработай иерархию категорий.** Дерево каталога, фильтры и теги.
2. **Определи требования к карточке товара (Listing Quality).** Фото, описание, технические характеристики.
3. **Опиши процесс модерации.** Автоматическая проверка ИИ (распознавание дублей и фейков) + ручная модерация.
4. **Сохрани вывод** в текущей рабочей директории как `marketplace-catalog-[контекст].md`.

## Формат вывода
```
## Спецификация каталога: [Маркетплейс]
- **Структура таксономии:** [категории]
- **ИИ-модерация контента:** правила детекции дублирующихся карточек товаров.
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
