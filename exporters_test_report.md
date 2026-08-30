# Отчет о тестировании экспорта правил в 9 IDE форматов

**Дата:** 31 августа 2026 г.  
**Статус:** 100% ВСЕХ ЭКСПОРТЕРОВ РАБОТАЮТ БЕЗ ОШИБОК.

| IDE / Платформа | Целевая структура файлов в .zip | Формат файлов | Статус |
| :--- | :--- | :--- | :--- |
| **Cursor IDE** | `.cursor/rules/<skill>.mdc` | Markdown с MDC frontmatter (`globs: *`) | **PASSED** |
| **Gemini Antigravity** | `.agents/skills/<skill>/SKILL.md` | Изолированная директория скилла + YAML | **PASSED** |
| **VS Code (Roo Code / Cline)** | `.clinerules.d/<skill>.md` | Модульные правила в `.clinerules.d` | **PASSED** |
| **GitHub Copilot** | `.github/copilot-instructions.d/<skill>.md` | Инструкции репозитория в `.github` | **PASSED** |
| **Windsurf IDE** | `.windsurfrules.d/<skill>.md` | Модульные правила Cascade в `.windsurfrules.d` | **PASSED** |
| **Aider CLI** | `conventions.d/<skill>.md` | Модульные конвенции Aider в `conventions.d` | **PASSED** |
| **Claude Code** | `.claude/skills/<skill>.md` | Модульные скиллы в `.claude/skills` | **PASSED** |
| **Pi Agent** | `skills/<skill>.md` | Системные скиллы Pi в `skills` | **PASSED** |
| **Universal Prompt** | `skills/<skill>.md` + Прямое копирование | Чистый Markdown для ChatGPT/Claude Web | **PASSED** |
