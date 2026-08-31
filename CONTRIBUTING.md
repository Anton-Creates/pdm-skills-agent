# Contributing to PdM Skills Agent

We welcome contributions from Product Managers, Engineers, and AI Researchers!

## How to Add or Improve a PM Skill

Every skill in `skills/<skill-name>/` must follow the **Grade-A E2E Tested Standard**:

1. **Folder Structure**:
   ```
   skills/<skill-name>/
   └── SKILL.md
   ```
2. **SKILL.md Requirements**:
   - YAML Frontmatter with `name` and `description` (Russian or English).
   - Clear input expectations (Context & Problem statement).
   - Strict markdown output schema (Artifact sections).
   - Embedded **BDD Scenarios** (`Given ... When ... Then ...`) ensuring deterministic model output.
   - Professional PM terminology (LTV, CAC, Retention, Unit Economics, MoSCoW/RICE, etc.).

## Contribution Workflow

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/new-growth-skill`.
3. Add or update your `SKILL.md` under `skills/<skill-name>/`.
4. Validate that output formatting is crisp and without generic filler text ("neuro-slop").
5. Open a Pull Request with a clear summary of the PM methodology used.

Thank you for helping make Product Management smarter with AI!
