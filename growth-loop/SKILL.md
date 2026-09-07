---
name: growth-loop
description: Спроектировать петли роста продукта (Growth Loops): виральные, контентные и платные циклы.
argument-hint: [описание продукта для проектирования петель роста]
allowed-tools: Read, Write
preset: growth
lifecycle: any
business-model: any
domain: saas
stage: any
output-artifact: document
---

# Проектирование петель роста (growth-loop)

Заменить линейные каналы привлечения цикличными петлями роста (Growth Loops), где действия пользователя приводят к привлечению новых пользователей.

## Процесс
1. **Определи тип петли:**
   - *Виральная (Viral Loop):* пользователь приглашает друга в процессе совместной работы (соавторство, шаринг сметы).
   - *Контентная (Content Loop):* пользователь генерирует контент -> он индексируется в SEO -> новые пользователи находят его и регистрируются.
2. **Спроектируй шаг реинвестирования (Reinvestment step).**
3. **Сохрани вывод** в текущей рабочей директории как `growth-loop-[контекст].md`.

## Формат вывода
```
## Спецификация петель роста: [Продукт]

### 1. Виральная петля (B2B Viral Loop)
- **Акт создания:** Застройщик создает смету в личном кабинете.
- **Действие:** Он отправляет ссылку на смету подрядчику для согласования.
- **Активация:** Подрядчик регистрируется в системе, чтобы отредактировать смету. Цикл замыкается (подрядчик может создать свой проект).
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
