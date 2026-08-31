# PdM Skills Agent

![Skills](https://img.shields.io/badge/Skills-130-blue) ![Antigravity](https://img.shields.io/badge/Antigravity-Ready-purple) ![Cursor](https://img.shields.io/badge/Cursor-Ready-green) ![Claude](https://img.shields.io/badge/Claude-Ready-orange)

Библиотека из 130 структурированных инструкций (скиллов) для AI-агентов, заточенных под задачи продакт-менеджера.

Скачай и подключи к своему AI-редактору — агент начнёт работать как Senior PM: писать PRD, строить Roadmap, делать юнит-экономику, проводить CustDev и многое другое.

> **Каталог с поиском и экспортом:** https://anton-creates.github.io/pdm-skills-builder/

---

## Быстрый старт

### Antigravity

Конфигурация уже встроена в `.agents/`. Просто клонируйте репозиторий и откройте в Antigravity:

```bash
git clone https://github.com/Anton-Creates/pdm-skills-agent.git
```

Агент автоматически загрузит все 130 скиллов и системный промпт. Пишите задачу в чат — агент сам подберёт нужные скиллы.

### Cursor / Windsurf / Roo Code

1. Клонируйте репозиторий.
2. Файл `.cursorrules` уже настроен — просто откройте папку в редакторе.
3. Добавляйте скиллы через `@File` или `@Folder`:

```
@skills/prd @skills/roadmap Подготовь документацию для фичи авторизации.
```

### Claude

1. Создайте новый Project на claude.ai.
2. В «Custom Instructions» вставьте содержимое `.agents/AGENTS.md`.
3. Загрузите нужные `SKILL.md` файлы в базу знаний проекта.

### Codex (OpenAI)

1. Клонируйте репозиторий.
2. Скопируйте `.agents/AGENTS.md` в корень проекта как `AGENTS.md` — Codex читает его автоматически как системный промпт.
3. Запустите Codex в папке проекта — агент получит доступ к скиллам через контекст рабочей директории.

### Copy-paste в любой чат

1. Откройте `skills/<нужный_скилл>/SKILL.md`.
2. Скопируйте и вставьте как системный промпт.
3. Передайте задачу.

---

## Структура

```
pdm-skills-agent/
├── skills/              # 130 скиллов по доменам
│   ├── prd/
│   ├── roadmap/
│   ├── competitor-scan/
│   └── ...
├── .agents/
│   ├── AGENTS.md        # Системный промпт агента
│   └── skills.json      # Реестр скиллов для Antigravity
└── .cursorrules         # Конфигурация для Cursor/Windsurf
```

| Домен | Примеры скиллов |
|---|---|
| Ядро PdM | PRD, Roadmap, User Stories, Prioritize, Launch Checklist |
| Исследования | Persona, CJM, Market Sizing, JTBD, User Interview |
| Рост и воронки | Funnel Analysis, Onboarding Audit, Referral, Retention |
| Стратегия | OKR, Business Model Canvas, Business Case, Competitor Scan |
| SaaS / B2B | Subscription Economics, Pricing Model, Enterprise Discovery |
| Маркетплейсы | Marketplace Model, Seller Economics, Search Ranking, Loyalty |
| Финтех | Credit Product Spec, Fintech Teardown, Finmarket Spec |
| Платформы | Platform Strategy, Data Product, DSP/SSP |
| HR-Tech / Internal | Internal Discovery, Admin UX, HR Portal, Task Tracker |
| GovTech | Public Service Design, Citizen Journey, GovTech Metrics |
| Телеком / EdTech | Telecom Subscriber, B2B EdTech, Dark Store Ops |

---

## Об авторе

[Антон Михайлов](https://www.linkedin.com/in/anton-mikhaylove/) · [Telegram](https://t.me/mikhaylove_anton)

---

> Рабочий репозиторий (сайт, аудит, инструменты разработки): [pdm-skills-builder](https://github.com/Anton-Creates/pdm-skills-builder)


