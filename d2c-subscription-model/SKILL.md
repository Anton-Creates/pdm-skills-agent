---
name: d2c-subscription-model
description: Спроектировать D2C-подписку для физического продукта: food box, beauty box, premium goods, фермерская корзина или регулярная доставка. На выходе — выбор модели, тарифы, unit economics, retention loop, fulfillment risks, supplier economics, метрики подписки и go/no-go решение.
argument-hint: [описание продукта, аудитории, цены, частоты покупки и логистики]
allowed-tools: Read, Write
preset: d2c
lifecycle: strategy,growth,measure
business-model: d2c,subscription,ecommerce
domain: retail,food-d2c
stage: idea,mvp,pre-pmf,pmf,scale
output-artifact: d2c-subscription-business-case
---

# D2C-подписка для физического продукта

Спроектировать бизнес-модель прямых продаж по подписке для физического продукта, где ценность создаётся не только цифровым интерфейсом, но и регулярной поставкой, качеством, доверием, брендом и операционной дисциплиной.

## Когда использовать

- Фермерская/food подписка, premium goods, beauty box, pet food, wellness, регулярная доставка расходников.
- Бренд хочет уйти от разовых продаж к recurring revenue.
- Есть дорогой CAC и нужна модель, где удержание важнее постоянного перепривлечения.
- Нужно выбрать между интернет-магазином, чужим маркетплейсом и собственной подпиской.

## Когда НЕ использовать

- Покупка нерегулярная и нет естественной частоты потребления.
- Логистика съедает маржу, а поднять чек нельзя.
- Пользователь не готов к повторной поставке или хочет каждый раз выбирать вручную.
- Нет контроля качества поставки, упаковки и возвратов.

## Процесс

1. **Определи recurring job.** Какая регулярная потребность делает подписку естественной?
2. **Сравни модели.** Разовая e-commerce покупка, чужой marketplace, D2C-подписка, retail/офлайн.
3. **Сформируй тарифы.** Частота, состав, цена, пауза, пропуск, отмена, апселл.
4. **Посчитай unit economics.** AOV, ARPU, gross margin, delivery cost, CAC, LTV, payback, break-even.
5. **Спроектируй retention loop.** Что заставляет ждать следующую поставку?
6. **Спроектируй fulfillment.** SLA, свежесть, упаковка, маршруты, замены, возвраты.
7. **Опиши supplier economics.** Доля партнёра, минимальные объёмы, качество, надёжность.
8. **Построй growth loop.** Referral, content, community, brand, gift mechanics.
9. **Собери risk heat map.** Логистика, CAC, churn, качество, поставщики, сезонность, репутация.
10. **Дай go/no-go решение.** Pilot / narrow wedge / build / partner / kill.
11. **Сохрани вывод** в текущей рабочей директории как `d2c-subscription-model-[контекст].md`.

## Формат вывода

```md
## D2C Subscription Model: [Название]

### 1. Контекст и recurring job
- **Пользователь:** [сегмент]
- **Регулярная потребность:** [что повторяется]
- **Почему подписка естественна:** [частота/удобство/доверие/экономия усилий]

### 2. Выбор модели
| Модель | Плюсы | Минусы | Вывод |
|---|---|---|---|
| Разовый интернет-магазин | | | |
| Чужой marketplace | | | |
| D2C-подписка | | | |

### 3. Тарифы и UX подписки
| Тариф | Цена | Частота | Для кого | Маржа | Риски |
|---|---:|---|---|---:|---|

- **Пауза:** [как работает]
- **Пропуск:** [как работает]
- **Отмена:** [без dark patterns]
- **Замены:** [если товара нет]

### 4. Unit economics
| Метрика | Значение | Комментарий |
|---|---:|---|
| AOV | | |
| Deliveries/month | | |
| ARPU | | |
| Gross Margin | | |
| Delivery Cost | | |
| CAC | | |
| Monthly Churn | | |
| LTV | | |
| LTV/CAC | | |
| CAC Payback | | |
| Break-even subscribers | | |

### 5. Метрики подписки
- **Outcome:** active subscribers, MRR, contribution margin.
- **Input:** activation, first delivery success, delivery SLA, referral rate.
- **Retention:** monthly churn, pause rate, pause return rate, repeat delivery success.
- **Guardrails:** complaint rate, refund rate, late delivery rate, supplier margin, quality incidents.
- **Diagnostics:** churn reasons, cohort retention, CAC by channel, NPS by delivery cohort, stockout rate.

### 6. Fulfillment и SLA
| Этап | SLA | Риск | Guardrail |
|---|---|---|---|
| Сборка | | | |
| Упаковка | | | |
| Доставка | | | |
| Замены/возвраты | | | |

### 7. Supplier economics
- **Партнёры/поставщики:** [кто]
- **Доля поставщика:** [%]
- **Минимальный объём:** [значение]
- **Quality control:** [как проверяем]
- **Backup supply:** [2-3 поставщика на критичный компонент]

### 8. Growth / Retention Loop
1. Acquisition: [brand/content/referral/paid]
2. First order: [первый момент доверия]
3. Delivery value: [почему пользователь доволен]
4. Retention content: [что поддерживает привычку]
5. Referral/community: [как пользователь приводит других]

### 9. Risk Heat Map
| Риск | Вероятность | Влияние | Trigger signal | Mitigation |
|---|---|---|---|---|

### 10. Решение
**Рекомендация:** [pilot / build / narrow / partner / kill]
**Первый пилот:** [сегмент, гео, число клиентов, длительность]
**Exit criteria:** [метрики успеха/провала]
```

## Правила

- Не проектируй подписку без честной паузы, пропуска и отмены. Удержание должно строиться на ценности, а не на ловушках.
- Не считай LTV от выручки. Используй маржу после товара, доставки, упаковки и возвратов.
- Проверяй, что частота поставки совпадает с реальным потреблением, иначе будет churn и накопление ненужного товара.
- Если доставка/свежесть — часть ценности, SLA должен быть guardrail, а не операционная деталь.
- Всегда показывай чувствительность экономики к churn, CAC и delivery cost.
- Пиши на русском языке.

## Метрики (Subscription / D2C)

### Outcome metric
**active subscribers, MRR, contribution margin.** Главный результат и ценность.

### Input metrics
**first order success, delivery SLA, referral rate, content engagement, pause return rate.** Управляемые рычаги outcome.

### Guardrails
**monthly churn, refund rate, late delivery rate, complaint rate, supplier margin, quality incidents.** Что нельзя ухудшить.

### Diagnostic metrics
**churn reason, cohort retention, CAC by channel, NPS by delivery cohort, stockout/substitution rate.** Где искать причину.

### Instrumentation
**subscription_id, delivery_id, pause/cancel events, SKU availability, channel, refund reason.** Какие данные нужны.

### Decision rules
- Ship / Iterate / Kill

### Универсальное правило метрики
Если вы предлагаете метрику, ответьте на 5 вопросов:
1. **Кто владеет этой метрикой?**
2. **Как часто её смотрим?**
3. **Какие события её считают?**
4. **Какой порог решения?**
5. **Как её можно испортить или накрутить?**
