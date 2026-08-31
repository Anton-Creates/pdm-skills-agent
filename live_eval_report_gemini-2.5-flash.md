# Live E2E Evaluation Report (Gemini API)

**Дата:** 2026-08-31 12:55
**Модель:** gemini-2.5-flash
**Итог:** 0/2 тестов пройдено

---

## Скилл: `prioritize`

### Realistic Input — FAILED

**Запрос:** Приоритизируй 4 фичи для мобильного приложения доставки: 1. Оплата через СБП, 2. Темная тема, 3. Отслеживание курьера на карте онлайн, 4. Анимированные стикеры.

**Время ответа:** ?s

**Ответ модели:**
```markdown
[API ERROR 429]: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-a
```

---

### Vague Input (guardrail test) — FAILED

**Запрос:** Расставь мне приоритеты в продукте.

**Время ответа:** ?s

**Ответ модели:**
```markdown
[API ERROR 429]: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-a
```

---

