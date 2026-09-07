---
name: kill-or-scale-decision
description: Принять решение по инициативе после пилота или MVP: масштабировать, сузить, итерировать, пивотить или закрыть. На выходе — evidence review, decision criteria, recommendation и next steps.
argument-hint: [результаты пилота/MVP, метрики, качественные выводы, ограничения]
allowed-tools: Read, Write
preset: strategy
lifecycle: measure,strategy
business-model: any
domain: any
stage: mvp,pre-pmf,pmf,scale
output-artifact: kill-or-scale-decision
---

# Kill or Scale Decision

Помочь команде не застрять в бесконечном “ещё чуть-чуть поитерируем”: собрать доказательства и принять явное решение.

## Формат вывода

```md
## Kill / Scale Decision: [Инициатива]

### 1. Decision
**Рекомендация:** Scale / Iterate / Narrow / Pivot / Kill

### 2. Pre-agreed Criteria
| Критерий | План | Факт | Статус |
|---|---:|---:|---|

### 3. Evidence Review
- Quantitative evidence:
- Qualitative evidence:
- Risks:
- Missing evidence:

### 4. Interpretation
### 5. Next Steps
### 6. Revisit Date
```

## Правила

- Не меняй критерии успеха после получения результата.
- Если данные inconclusive, рекомендуй минимальный следующий тест, а не бесконечную разработку.
- Пиши на русском языке.

## Метрики

### Универсальное правило метрики
Если вы предлагаете метрику, ответьте на 5 вопросов:
1. **Кто владеет этой метрикой?**
2. **Как часто её смотрим?**
3. **Какие события её считают?**
4. **Какой порог решения?**
5. **Как её можно испортить или накрутить?**