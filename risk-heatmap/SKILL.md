---
name: risk-heatmap
description: Построить risk heat map для продукта, инициативы или бизнес-модели: market, operational, financial, tech, regulatory, brand risks; probability × impact; trigger signals; mitigations; owners.
argument-hint: [описание инициативы, продукта или запуска]
allowed-tools: Read, Write
preset: fintech
lifecycle: strategy,operations,measure
business-model: any
domain: any
stage: idea,mvp,pre-pmf,pmf,scale
output-artifact: risk-heatmap
---

# Risk Heat Map

Системно разложить риски продукта и превратить их в управляемые trigger signals, mitigations и owners.

## Формат вывода

```md
## Risk Heat Map: [Инициатива]

### 1. Summary
- Красная зона:
- Оранжевая зона:
- Главный early warning signal:

### 2. Risk Register
| Риск | Категория | Вероятность | Влияние | Trigger signal | Mitigation | Owner |
|---|---|---|---|---|---|---|

### 3. Priority Actions
1. Critical:
2. High:
3. Watch:

### 4. Review Cadence
```

## Правила

- Не ограничивайся списком рисков. Обязательно добавляй trigger signal и owner.
- Риск без mitigation — просто тревога.
- Пиши на русском языке.

## Метрики

### Универсальное правило метрики
Если вы предлагаете метрику, ответьте на 5 вопросов:
1. **Кто владеет этой метрикой?**
2. **Как часто её смотрим?**
3. **Какие события её считают?**
4. **Какой порог решения?**
5. **Как её можно испортить или накрутить?**