---
name: notification-strategy
description: Разработать стратегию push, SMS и email уведомлений для удержания пользователей и снижения спама.
argument-hint: [цели продукта по рассылкам и список событий]
allowed-tools: Read, Write
preset: telecom
lifecycle: any
business-model: any
domain: saas
stage: any
output-artifact: document
---

# Стратегия уведомлений (notification-strategy)

Спроектировать матрицу триггерных уведомлений (Push/SMS/Email) для стимулирования возврата пользователей в продукт при сохранении баланса вовлечения и защиты от отписок (opt-out).

## Процесс
1. **Составь матрицу событий.**
2. **Определи каналы доставки.** SMS — для критических (транзакции), Push — для контекстных, Email — для длинных дайджестов.
3. **Задай правила ограничения частоты (Frequency Capping).** Не более N пушей в день на пользователя.
4. **Сохрани вывод** в текущей рабочей директории как `notification-strategy-[контекст].md`.

## Формат вывода
```
## Матрица уведомлений: [Продукт]

### 1. Правила доставки (Notification Matrix)
| Событие | Канал по умолчанию | Защитный интервал | Текст сообщения |
|---|---|---|---|
| **Регистрация сделки** | SMS + Push | Мгновенно | «Сделка зарегистрирована в Росреестре. Ожидайте раскрытия счетов» |
| **Брошенная корзина** | Push | 2 часа | «Продукты ждут в корзине. Завершите заказ» |
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
