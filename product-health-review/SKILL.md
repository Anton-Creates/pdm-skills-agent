---
name: product-health-review
description: Провести CPO-level диагностику здоровья продукта по пользователям, метрикам, экономике, delivery, рискам и стратегии. На выходе — health scorecard, красные зоны, root causes и план действий на 30/60/90 дней.
argument-hint: [описание продукта, стадия, ключевые метрики и проблемы]
allowed-tools: Read, Write
preset: strategy
lifecycle: measure,strategy,operations
business-model: any
domain: any
stage: mvp,pre-pmf,pmf,scale,mature,turnaround
output-artifact: product-health-review
---

# Product Health Review

Провести диагностику продукта не по одной метрике, а как системы: пользовательская ценность, retention, экономика, качество delivery, операционные риски, команда и стратегический фокус.

## Процесс

1. Определи стадию продукта и бизнес-модель.
2. Собери outcome/input/guardrail метрики.
3. Проверь retention и повторное поведение.
4. Проверь unit economics и каналы роста.
5. Проверь качество продукта: reliability, support, UX, complaints.
6. Найди root causes красных зон.
7. Сформируй 30/60/90 day action plan.
8. **Сохрани вывод** в текущей рабочей директории как `product-health-review-[контекст].md`.

## Формат вывода

```md
## Product Health Review: [Продукт]

### 1. Executive Summary
- **Общий статус:** Healthy / Watch / Critical
- **Главная красная зона:**
- **Главная рекомендация:**

### 2. Health Scorecard
| Область | Статус | Метрики | Вывод |
|---|---|---|---|
| User Value | Green/Yellow/Red | | |
| Activation | | | |
| Retention | | | |
| Monetization | | | |
| Unit Economics | | | |
| Growth | | | |
| Reliability/Ops | | | |
| Strategy Fit | | | |

### 3. Root Causes
### 4. Риски
### 5. План 30/60/90
### 6. Решения, которые нужны от руководства
```

## Правила

- Не объявляй продукт здоровым только из-за роста выручки. Рост может быть куплен CAC при дырявом retention.
- Разделяй симптомы и root causes.
- Если данных нет, явно перечисли missing instrumentation.
- Пиши на русском языке.

## Метрики

### Универсальное правило метрики
Если вы предлагаете метрику, ответьте на 5 вопросов:
1. **Кто владеет этой метрикой?**
2. **Как часто её смотрим?**
3. **Какие события её считают?**
4. **Какой порог решения?**
5. **Как её можно испортить или накрутить?**
