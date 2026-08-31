# PdM Skills Agent (RU)

[English README](README.md)

![Skills](https://img.shields.io/badge/Скиллы-130-blue) ![Веб-Каталог](https://img.shields.io/badge/Веб_Каталог-Live-green) ![E2E Tested](https://img.shields.io/badge/E2E-100%25_Тестов-success) ![License](https://img.shields.io/badge/Лицензия-MIT-green) ![Antigravity](https://img.shields.io/badge/Antigravity-Ready-purple) ![Cursor](https://img.shields.io/badge/Cursor-Ready-emerald) ![Claude Code](https://img.shields.io/badge/Claude_Code-Plugin-orange)

Библиотека из **130 структурных продуктовых скиллов (фреймворков)** для AI-агентов кодинга (**Antigravity, Cursor, Windsurf, Codex, Claude Code**). 

🌐 **[Интерактивный веб-каталог и конструктор правил](https://anton-creates.github.io/pdm-skills-agent/)**

Превращает вашего AI-помощника в **Senior Product Manager Co-Pilot**, готового разрабатывать PRD, карты CJM, бизнес-кейсы, юнит-экономику, деревья гипотез и роадмапы без «нейрослопа» и общих слов.

---

## Быстрый старт

### 1. Antigravity
Конфигурация уже встроена в `.agents/`. Просто клонируйте репозиторий и откройте в Antigravity:
```bash
git clone https://github.com/Anton-Creates/pdm-skills-agent.git
```

### 2. Cursor / Windsurf / Roo Code
Откройте склонированный проект в редакторе — `.cursorrules` автоматически подгрузит роль Senior PM Co-Pilot и даст доступ ко всем 130 скиллам в папке `skills/`.

### 3. Codex (OpenAI)
1. Клонируйте репозиторий.
2. Скопируйте `.agents/AGENTS.md` в корень проекта как `AGENTS.md` — Codex читает его автоматически как системный промпт.
3. Запустите Codex в папке проекта — агент получит доступ к скиллам через контекст рабочей директории.

### 4. Claude Code (CLI)
```bash
/plugin marketplace add Anton-Creates/pdm-skills-agent
/plugin install pdm-skills-agent@pdm-skills-agent
```

### 5. Claude.ai (Веб-версия)
1. Создайте Project в Claude.ai.
2. В «Custom Instructions» вставьте содержимое `.agents/AGENTS.md`.
3. Загрузите нужные `SKILL.md` файлы в базу знаний проекта.

---

## Категории скиллов (130 фреймворков)

| Домен | Описание | Примеры скиллов |
|---|---|---|
| **Discovery & Strategy** | Исследования, валидация гипотез, JTBD | `discovery-sprint`, `jobs-to-be-done`, `user-interview-prep`, `hypothesis-tree` |
| **Product Specs & PRD** | Требования, спецификации, BDD-сценарии | `prd`, `user-stories`, `ai-feature-spec`, `data-product-spec` |
| **Growth & Analytics** | Воронки, метрики, онбординг, CRO | `funnel-analysis`, `metrics-tree`, `onboarding-audit`, `cro-audit` |
| **Fintech & Banking** | Финтех-продукты, скоринг, маркетплейсы | `fintech-product-teardown`, `credit-product-spec`, `finmarket-spec` |
| **E-commerce & Retail** | Карточки, листинги, логистика, дарксторы | `pdp-spec`, `plp-filters-spec`, `dark-store-ops`, `ecom-checkout-split` |
| **B2B & Enterprise** | Закупки, внедрение, интеграции, ROI | `enterprise-discovery`, `enterprise-rollout`, `internal-roi`, `rfp-response` |
| **Roadmap & OKR** | Планирование, цели, приоритизация | `roadmap`, `okr-writer`, `prioritize` (RICE/ICE/WSJF) |

---

## Безопасность и Лицензия

- **Лицензия:** [MIT License](LICENSE) — свободное личное и коммерческое использование.
- **Безопасность:** См. [SECURITY.md](SECURITY.md) для репортов об уязвимостях.
- **Вклад в проект:** См. [CONTRIBUTING.md](CONTRIBUTING.md) для правил добавления новых скиллов.
