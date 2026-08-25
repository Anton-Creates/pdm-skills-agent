---
name: trust-safety
description: Разработать стратегию безопасности и доверия (Trust & Safety) для C2C маркетплейса или шеринг-платформы.
argument-hint: [описание C2C платформы и ключевых рисков мошенничества]
allowed-tools: Read, Write
preset: marketplace
lifecycle: any
business-model: any
domain: marketplace
stage: any
output-artifact: document
---

# Безопасность и Доверие C2C (trust-safety)

Спроектировать комплекс мер по защите пользователей от мошенничества, обмана и кражи данных на C2C-платформе (аренда жилья, продажа б/у вещей, поиск исполнителей).

## Процесс
1. **Определи векторы атак и фрода.** Обход платежной системы (увод в мессенджеры), фейковые объявления, подмена аккаунтов.
2. **Спроектируй систему верификации пользователей (KYC).** Интеграция с Госуслугами/ЕСИА, проверка по паспорту/селфи.
3. **Разработай безопасную сделку (Escrow).** Холдирование средств, арбитраж споров.
4. **Сохрани вывод** в текущей рабочей директории как `trust-safety-[контекст].md`.

## Формат вывода
```
## Trust & Safety спецификация: [Название платформы]

### 1. Векторы фрода и механики защиты
- **Риск:** увод покупателя в Telegram и отправка фишинговой ссылки.
  - *Защита:* автоблокировка номеров телефонов и ссылок в чате платформы, баннер-предупреждение при детекции слов «ватсап, телеграм, перейди».

### 2. Механика Безопасной Сделки
- Деньги покупателя замораживаются банком-эскроу.
- Выплата продавцу происходит только после подтверждения ПВЗ или покупателем в течение 24 часов.
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
