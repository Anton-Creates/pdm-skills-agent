# PdM Skills Agent

[Читать на русском (Russian README)](README.ru.md)

![Skills](https://img.shields.io/badge/Skills-130-blue) ![Catalog](https://img.shields.io/badge/Web_Catalog-Live-green) ![E2E Tested](https://img.shields.io/badge/E2E-100%25_Tested-success) ![License](https://img.shields.io/badge/License-MIT-green) ![Antigravity](https://img.shields.io/badge/Antigravity-Ready-purple) ![Cursor](https://img.shields.io/badge/Cursor-Ready-emerald) ![Claude Code](https://img.shields.io/badge/Claude_Code-Plugin-orange)

**A production-ready library of 130 structured Product Management skills and frameworks for AI Coding Agents (Antigravity, Cursor, Windsurf, Codex, Claude Code).**

🌐 **[Open Interactive Web Catalog & Rule Builder](https://anton-creates.github.io/pdm-skills-agent/)**

Transforms your AI assistant into a **Senior Product Manager Co-Pilot**, equipped to produce CPO-grade PRDs, Customer Journey Maps, business cases, unit economics, hypothesis trees, and strategic roadmaps with zero fluff.

---

## Quick Start

### 1. Antigravity
Native agent configuration is included in `.agents/`. Simply clone the repository and open it in Antigravity:
```bash
git clone https://github.com/Anton-Creates/pdm-skills-agent.git
```

### 2. Cursor / Windsurf / Roo Code
Open the repository in your IDE. `.cursorrules` automatically loads the Senior PM Co-Pilot role and grants access to all 130 skills in `skills/`.

### 3. Codex (OpenAI)
1. Clone the repository.
2. Copy `.agents/AGENTS.md` to root as `AGENTS.md` (Codex reads it automatically as system context).
3. Launch Codex in the project directory.

### 4. Claude Code (CLI)
Install the native plugin via terminal:
```bash
/plugin marketplace add Anton-Creates/pdm-skills-agent
/plugin install pdm-skills-agent@pdm-skills-agent
```

### 5. Claude.ai (Web App)
1. Create a **Project** in Claude.ai.
2. Add the contents of `.agents/AGENTS.md` to **Project Custom Instructions**.
3. Upload target `SKILL.md` files from `skills/` to **Project Knowledge**.

---

## 130 Product Skills Taxonomy

| Domain | Description | Example Skills |
|---|---|---|
| **Discovery & Strategy** | User research, hypothesis validation, JTBD, market sizing | `discovery-sprint`, `jobs-to-be-done`, `user-interview-prep`, `hypothesis-tree` |
| **Product Specs & PRD** | Requirements, PRD, BDD scenarios, AI/Data specifications | `prd`, `user-stories`, `ai-feature-spec`, `data-product-spec` |
| **Growth & Analytics** | Funnels, metric trees, onboarding audits, CRO audits | `funnel-analysis`, `metrics-tree`, `onboarding-audit`, `cro-audit` |
| **Fintech & Banking** | Credit products, scoring funnels, financial marketplaces | `fintech-product-teardown`, `credit-product-spec`, `finmarket-spec` |
| **E-commerce & Retail** | PDP, PLP filters, dark store operations, checkout splits | `pdp-spec`, `plp-filters-spec`, `dark-store-ops`, `ecom-checkout-split` |
| **B2B & Enterprise** | Procurement, enterprise discovery, rollout, ROI cases | `enterprise-discovery`, `enterprise-rollout`, `internal-roi`, `rfp-response` |
| **Roadmap & OKRs** | Strategic horizons, OKR trees, RICE/ICE/WSJF prioritization | `roadmap`, `okr-writer`, `prioritize` |

---

## Security & License

- **License:** [MIT License](LICENSE) — Free personal and commercial usage.
- **Security:** See [SECURITY.md](SECURITY.md) for vulnerability reporting.
- **Contributing:** See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on contributing new skills.
