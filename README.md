# PdM-Skills Builder

### Модульный компилятор системных правил ИИ для продакт-менеджеров

[![Skills](https://img.shields.io/badge/Skills-125%20Модулей-0284c7?style=flat-square)](https://anton-creates.github.io/pdm-skills-builder/)
[![IDE](https://img.shields.io/badge/IDE%20Support-9%20Форматов-16a34a?style=flat-square)](https://anton-creates.github.io/pdm-skills-builder/)
[![Design System](https://img.shields.io/badge/Design%20System-Anti--AI%20Swiss%20Grid-0f172a?style=flat-square)](https://anton-creates.github.io/pdm-skills-builder/)
[![Author](https://img.shields.io/badge/Telegram-@mikhaylove__anton-229ED9?style=flat-square)](https://t.me/mikhaylove_anton)

[Запустить Web-конструктор онлайн (Live App)](https://anton-creates.github.io/pdm-skills-builder/)

---

Модульная библиотека из **125 изолированных системных инструкций** для продакт-менеджмента. Позволяет собирать точечный контекст и правила для ChatGPT, Claude, Cursor, Roo Code, Copilot и Antigravity без перегрузки контекстного окна.

```mermaid
flowchart LR
    A["Выбор роли / Скиллов\n(125 модулей)"] --> B["Компилятор правил\n(Token Estimator & Guardrails)"]
    B --> C["Экспорт в 1 клик\n(Cursor / Claude / Copilot)"]
    C --> D["Результат без воды\n(PRD / Метрики / Аналитика)"]
```

---

## Архитектурные принципы

- **Изолированный контекст:** Вместо перегруженных универсальных промптов на десятки страниц — точечный выбор 3–5 целевых модулей под конкретную задачу.
- **Встроенные Guardrails:**
  - Обязательное правило 5 вопросов для любой предлагаемой метрики (владелец, частота замера, события расчета, порог решения, защита от накрутки).
  - Запрет наводящих вопросов в CustDev-исследованиях (методология Mom Test).
  - Требование проектирования Fallback-сценариев и HITL для всех AI/ML спецификаций.
  - Протокол Root-Cause расследования при падении бизнес-показателей.
- **Realtime Token Estimator:** Подсчет веса сборки правил в токенах и шкала заполнения контекстного окна (128k baseline).
- **Двухрежимный интерфейс:** Поддержка тем Light Editorial и Engineering Dark, переключение между карточной сеткой и табличной матрицей с горизонтальным скроллом.

---

## Поддерживаемые форматы экспорта (9 IDE и Агентов)

Конструктор генерирует чистый архив с изолированными модульными файлами для целевой среды разработки:

| Среда / Инструмент | Формат файлов в архиве | Описание |
| :--- | :--- | :--- |
| **Universal Markdown** | `skills/*.md` | Модульные файлы для ChatGPT, Claude Web, DeepSeek |
| **Cursor IDE** | `.cursor/rules/*.mdc` | Модульные правила с метаданными и глоб-паттернами |
| **VS Code / Roo Code / Cline** | `.clinerules.d/*.md` | Изолированные системные инструкции для кодинг-агентов |
| **GitHub Copilot** | `.github/copilot-instructions.d/*.md` | Модульные инструкции для Copilot |
| **Windsurf IDE** | `.windsurfrules.d/*.md` | Контекстные правила для Cascade Assistant |
| **Aider** | `conventions.d/*.md` | Модульные конвенции для терминального AI-ассистента |
| **Pi Agent** | `skills/*.md` | Дополнительные системные модули |
| **Claude Code** | `.claude/skills/*.md` | Модульные скиллы для CLI Claude Code |
| **Gemini Antigravity** | `.agents/skills/*/SKILL.md` | Исполняемые скиллы для Antigravity 2.0 |

---

## Структура библиотеки (125 Скиллов по 15 Доменам)

<details open>
<summary><b>[01] Ядро PdM / Core Delivery (16 скиллов)</b></summary>

- `/prd` — Продуктовые требования с критериями приемки и нефункциональными требованиями.
- `/user-stories` — Пользовательские истории по Given-When-Then с негативными сценариями.
- `/roadmap` — Таймлайн-роадмап с фазами Now / Next / Later и оценкой рисков.
- `/prioritize` — Приоритизация бэклога по фреймворкам RICE, ICE, WSJF и Kano.
- `/decision-doc` — Архитектурные и продуктовые Decision Records (ADR / PDR) с фиксацией Trade-offs.
- `/metrics-analyzer` — Расследование падений метрик (Root-Cause Analysis), финтех-фильтры и когорты.
- `/metrics-tree` — Дерево метрик от North Star до операционных драйверов.
- `/ab-test-design` — Дизайн A/B-тестов, расчет MDE, выборки, P-peeking защита и Guardrail метрики.
- `/technical-translator` — Перевод технических ограничений архитектуры на язык бизнес-метрик.
- `/launch-checklist` — Чек-лист предрелизного аудита, канареечного раската (Canary) и отката (Rollback).
- `/release-notes` — Пользовательские и технические Release Notes.
- `/product-status-update` — Структурированный статус-отчет по продукту.
- `/stakeholder-update` — Синхронизация с топ-менеджментом и стейкхолдерами.
- `/meeting-prep` — Подготовка повесток и фреймворков встреч без потери времени.
- `/presentation-design` — Сторилайн и структура питч-деков для защиты концепций.
- `/retro-facilitator` — Сценарии и фасилитация ретроспектив команды (Start/Stop/Continue, 4Ls).

</details>

<details>
<summary><b>[02] Исследования и CustDev / Discovery (12 скиллов)</b></summary>

- `/user-interview-prep` — Гайд качественного интервью по фреймворку Mom Test без наводящих вопросов.
- `/customer-journey-map` — CJM полного цикла с точками трения, эмоциями и возможностями.
- `/discovery-sprint` — 2-недельный спринт валидации, Opportunity Solution Tree (OST) и Assumption Mapping.
- `/feedback-analyzer` — Кластеризация обратной связи из саппорта, сторов и NPS.
- `/persona` — Описание целевой персоны (ICP) с триггерами покупки и барьерами.
- `/icp-definition` — Определение Ideal Customer Profile для B2B и B2C продуктов.
- `/survey-design` — Проектирование количественных опросов без когнитивных искажений.
- `/competitor-scan` — Конкурентный анализ и бенчмаркинг продуктовых решений.
- `/market-sizing` — Расчет емкости рынка через PAM / TAM / SAM / SOM.
- `/positioning-statement` — Разработка позиционирования и УТП продукта.
- `/jobs-to-be-done` — Исследование глубинных работ (JTBD) и сил прогресса (Push/Pull/Habit/Anxiety).
- `/hypothesis-tree` — Дерево продуктовых гипотез для структурированной валидации.

</details>

<details>
<summary><b>[03] Рост и Воронки / Growth & Acquisition (6 скиллов)</b></summary>

- `/growth-loop` — Проектирование самоподдерживающихся петель роста (Viral, Content, Paid Loops).
- `/onboarding-audit` — Аудит первых 5 минут в продукте и устранение точек отвала (Activation Drop-offs).
- `/retention-model` — Когортный анализ удержания, построение Retention Curve и поиск Aha-моментов.
- `/funnel-analysis` — Пошаговая декомпозиция воронок и поиск узких мест.
- `/referral-mechanics` — Реферальные программы с двусторонней ценностью.
- `/channel-mix` — Анализ и приоритизация каналов привлечения (Now / Later / Never).

</details>

<details>
<summary><b>[04] SaaS и Подписки / Subscriptions & PLG (7 скиллов)</b></summary>

- `/saas-metrics` — Метрики SaaS (CAC, LTV, Magic Number, Net Revenue Retention).
- `/subscription-economics` — Экономика регулярных подписок (MRR, Churn, Cohorts).
- `/d2c-subscription-model` — Подписочные модели для B2C сервисов и физических товаров.
- `/plg-design` — Product-Led Growth механики: Time-to-Value, виральный шеринг, бесшовный онбординг.
- `/pricing-experiment` — Дизайн ценовых тестов (Van Westendorp, Gabor-Granger, Paywall A/B).
- `/pricing-model` — Разработка моделей тарификации и монетизации.
- `/monetization-audit` — Аудит тарифов, Freemium-ограничений и расчет потенциала ARPU.

</details>

<details>
<summary><b>[05] B2B Продукты и Продажи / Enterprise Sales (5 скиллов)</b></summary>

- `/enterprise-discovery` — Особенности Discovery в Enterprise: закупочные комитеты и лица принимающие решения (ЛПР).
- `/enterprise-rollout` — План раската B2B-софта на корпоративных пользователей.
- `/rfp-response` — Подготовка ответов на тендерные требования и технические задания.
- `/build-buy-partner` — Фреймворк выбора между собственной разработкой, покупкой или партнерством.
- `/adoption-strategy` — Стратегия вовлечения и адаптации сотрудников к новым системам.

</details>

<details>
<summary><b>[06] Внутренние продукты и HR-Tech (8 скиллов)</b></summary>

- `/digital-workspace-superapp` — Корпоративный суперапп и цифровой офис сотрудника (ЦОС, микросервисы, самообслуживание).
- `/hr-portal-growth` — Портал развития сотрудников, Welcome-онбординг 30-60-90, ИПР и Performance Review 360.
- `/corp-communication-suite` — Корпоративные коммуникации (защищенный мессенджер, почта, ВКС и облачная АТС).
- `/internal-task-tracker` — Корпоративный тасктрекер и система управления проектами (доски, воркфлоу, контроль SLA).
- `/internal-recruitment-crm` — Внутренняя HR CRM и ATS для управления воронкой найма и кандидатами.
- `/internal-product-discovery` — Исследование потребностей внутренних пользователей компании.
- `/admin-ux` — Проектирование эргономичных бэк-офисов, массовых действий (Bulk) и журнала аудита (Audit Trail).
- `/service-desk-metrics` — Метрики технической поддержки и Service Desk (SLA, FCR, MTTR).

</details>

<details>
<summary><b>[07] Стратегия и CPO / Leadership (13 скиллов)</b></summary>

- `/product-strategy` — Стратегия продукта на 1–3 года с мостами и фазами роста.
- `/business-case` — Расчет окупаемости и бизнес-обоснование новых инициатив.
- `/investment-memo` — Инвестиционный меморандум для привлечения финансирования.
- `/portfolio-review` — Аудит продуктового портфеля и перераспределение ресурсов.
- `/product-health-review` — Комплексный аудит здоровья продукта и процессов.
- `/kill-or-scale-decision` — Фреймворк принятия решений о масштабировании или закрытии фичи.
- `/product-operating-model` — Операционная модель и оргструктура продуктовой команды.
- `/business-model-canvas` — Бизнес-модель продукта по Остервальдеру.
- `/competitive-moat` — Защитные барьеры и конкурентные рвы (сетевые эффекты, издержки переключения, данные).
- `/gtm-strategy` — Go-to-Market план вывода продукта на рынок.
- `/north-star-metric` — Определение главной путеводной метрики и связка с ценностью.
- `/okr-writer` — Постановка измеримых целей и ключевых результатов (Objectives & Key Results).
- `/tenets-writer` — Продуктовые принципы и догмы для автономного принятия решений командой.

</details>

<details>
<summary><b>[08] Платформы и Архитектура / Tech & Platforms (10 скиллов)</b></summary>

- `/api-product-spec` — Спецификация API как продукта: SLA, Rate Limits (429), версионирование и DX/Sandbox.
- `/ai-feature-spec` — Спецификация AI-фичи: ML-постановка, метрики (Precision/Recall vs Бизнес), Fallback и HITL.
- `/llm-product-design` — Промпт-инжиниринг, защита от инъекций, RAG-архитектура и оценка качества ответов (Evals).
- `/data-product-spec` — Спецификация витрин данных, DWH пайплайнов и SLA обновления аналитики.
- `/platform-strategy` — Платформенная стратегия и построение многосторонних экосистем.
- `/superapp-strategy` — Стратегия супераппа и архитектура мини-приложений.
- `/ecosystem-design` — Дизайн цифровых экосистем и синергии сервисов.
- `/feature-flag-strategy` — Стратегия управления фиче-тогглами и канареечными релизами.
- `/incident-pm-role` — Протокол работы PM во время аварий на проде, статус-пейджи и пост-мортемы.
- `/hw-sw-roadmap` — Роадмап продуктов на стыке софта и аппаратного обеспечения (IoT / Hardware).

</details>

<details>
<summary><b>[09] Финтех и Банкинг (10 скиллов)</b></summary>

- `/fintech-product-teardown` — Декомпозиция банковских сервисов, рисков регуляторики и скоринга.
- `/credit-product-spec` — Спецификация кредитных продуктов, скоринговых карт и условий выдачи.
- `/finmarket-spec` — Спецификация финансовых маркетплейсов и агрегаторов.
- `/unit-economics` — Детальный расчет юнит-экономики на клиента и на транзакцию.
- `/internal-roi` — Оценка окупаемости внутренних проектов автоматизации.
- `/real-estate-tech` — Продуктовые решения в сфере недвижимости, ипотеки и эскроу-счетов.
- `/compliance-checkpoint` — Проверка соответствия регуляторным требованиям ЦБ РФ и 152-ФЗ.
- `/risk-heatmap` — Тепловая карта операционных, регуляторных и кредитных рисков.
- `/trust-safety` — Противодействие фроду, AML/KYC комплаенс и защита от социальной инженерии.
- `/product-teardown` — Детальный анатомический разбор любого цифрового продукта.

</details>

<details>
<summary><b>[10] Маркетплейсы (11 скиллов)</b></summary>

- `/marketplace-model` — Экономическая модель двухстороннего маркетплейса.
- `/marketplace-catalog` — Архитектура товарного каталога, атрибуты, вариации и модерация.
- `/seller-economics` — Юнит-экономика мерчанта, комиссии (Take Rate) и калькуляторы окупаемости.
- `/seller-journey` — Путь селлера: онбординг, загрузка товаров, продажи и выплаты.
- `/supply-quality` — Контроль качества предложения селлеров и работа с дефектами.
- `/matching-algorithm` — Алгоритмы матчинга спроса и предложения в реальном времени.
- `/search-ranking` — Поисковая выдача и ранжирование товаров в маркетплейсе.
- `/c2c-dynamics` — Балансировка спроса и предложения на C2C площадках.
- `/classifieds-model` — Бизнес-модель классифайдов и монетизация платных размещений.
- `/fulfillment-model` — Сравнение схем FBO / FBS / DBS и оптимизация стоимости последней мили.
- `/marketplace-fraud` — Борьба с накрутками отзывов, самовыкупами и фейковыми треками.

</details>

<details>
<summary><b>[11] E-commerce и Ритейл (11 скиллов)</b></summary>

- `/catalog-strategy` — Управление товарной матрицей и категоризацией интернет-магазина.
- `/checkout-audit` — Аудит чекаута, оптимизация шагов оплаты и борьба с брошенными корзинами.
- `/cro-audit` — Аудит конверсии страниц и устранение барьеров покупки.
- `/promo-engine` — Проектирование промо-механик, скидок, купонов и бандлов.
- `/loyalty-program` — Дизайн программ лояльности: баллы, кешбэк, уровни привилегий.
- `/loyalty-crm` — Сегментация базы (RFM-анализ) и триггерные CRM-коммуникации.
- `/returns-management` — Процессы возвратов товаров и минимизация логистических потерь.
- `/demand-forecasting-pm` — Прогнозирование спроса для управления складскими запасами.
- `/retail-supply-chain` — Продуктовая оптимизация цепочек поставок ритейла.
- `/dark-store-ops` — Продуктовое проектирование дарксторов и скорости сборки заказов.
- `/last-mile-product` — Управление курьерской доставкой и клиентским опытом последней мили.

</details>

<details>
<summary><b>[12] Медиа, Стриминг и AdTech (5 скиллов)</b></summary>

- `/ugc-platform` — Механики генерации пользовательского контента (UGC) и модерация.
- `/content-strategy` — Контентная стратегия и дистрибуция в медиапродуктах.
- `/streaming-product` — Специфика видео- и аудио-стриминговых сервисов.
- `/ads-platform-pm` — Проектирование собственной рекламной платформы и кабинета рекламодателя.
- `/dsp-ssp-spec` — Архитектура programmatic-рекламы: DSP, SSP и аукционы RTB.

</details>

<details>
<summary><b>[13] EdTech и Образование (2 скилла)</b></summary>

- `/learning-product` — Проектирование образовательного опыта (LMS) и доходимости курсов (Completion Rate).
- `/b2b-edtech` — Специфика корпоративного обучения и интеграции с HR-системами.

</details>

<details>
<summary><b>[14] Телеком и Инфраструктура (4 скилла)</b></summary>

- `/telecom-subscriber` — Жизненный цикл абонента телеком-оператора и управление оттоком.
- `/vas-product` — Дополнительные услуги оператора (Value Added Services).
- `/b2b-telecom` — Продукты фиксированной и мобильной связи для корпоративных клиентов.
- `/notification-strategy` — Стратегия push-, sms- и email-уведомлений без спама.

</details>

<details>
<summary><b>[15] Госсектор и Граждане / GovTech (5 скиллов)</b></summary>

- `/public-service-design` — Проектирование электронных госуслуг, соответствие 152-ФЗ и ГОСТ.
- `/govtech-metrics` — Метрики эффективности госсервисов (уровень цифровизации, скорость оказания услуг).
- `/citizen-journey` — Клиентский путь гражданина при получении услуг.
- `/mini-app-platform` — Платформа мини-приложений для порталов госуслуг.
- `/localization-strategy` — Стратегия локализации и адаптации сервисов под языки и регионы.

</details>

---

## Локальный запуск

Проект автономен, работает в статическом режиме и не требует серверов или баз данных.

```bash
# Клонировать репозиторий
git clone https://github.com/Anton-Creates/pdm-skills-builder.git

# Перейти в директорию
cd pdm-skills-builder

# Открыть веб-приложение
# Откройте index.html в любом браузере
```

### Добавление нового скилла:
1. Создайте папку `skills/my-new-skill/` с файлом `SKILL.md`.
2. Запустите пересборку базы:
   ```bash
   python manager.py
   ```
3. Новый модуль автоматически появится в каталоге и поиске.

---

## Автор и Контакты

**Антон Михайлов (Anton.Creates)** — Lead Product Manager / Tech Solutions Builder

- Telegram: [@mikhaylove_anton](https://t.me/mikhaylove_anton)
- LinkedIn: [linkedin.com/in/anton-mikhaylove](https://www.linkedin.com/in/anton-mikhaylove/)
- GitHub: [github.com/Anton-Creates](https://github.com/Anton-Creates)

---

## Лицензия

Распространяется под свободной лицензией **MIT License**.
