# useful-agents

A collection of useful AI agent personas, ready to drop into GitHub Copilot, Claude Code, Cursor, OpenCode and other AI tools.

It currently has 21 personas across engineering, creative and business, each with a matching GitHub Copilot custom agent.

## Repository structure

```
.
├── .github/
│   ├── agents/                 # Native path for GitHub Copilot custom agents
│   │   ├── senior-dev.agent.md
│   │   ├── ui-ux-designer.agent.md
│   │   ├── technical-writer.agent.md
│   │   ├── seo-specialist.agent.md
│   │   ├── backend-architect.agent.md
│   │   ├── qa-engineer.agent.md
│   │   ├── copywriter.agent.md
│   │   ├── product-manager.agent.md
│   │   ├── scrum-master.agent.md
│   │   ├── data-analyst.agent.md
│   │   ├── legal-compliance-advisor.agent.md
│   │   ├── devops-engineer.agent.md
│   │   ├── frontend-developer.agent.md
│   │   ├── customer-support-specialist.agent.md
│   │   ├── security-engineer.agent.md
│   │   ├── mobile-developer.agent.md
│   │   ├── machine-learning-engineer.agent.md
│   │   ├── data-engineer.agent.md
│   │   ├── site-reliability-engineer.agent.md
│   │   ├── accessibility-specialist.agent.md
│   │   └── ux-researcher.agent.md
│   └── workflows/
│       └── validate-personas.yml   # CI check for persona and agent frontmatter
├── personas/                   # General, cross-platform personas (Claude Code, Cursor, OpenCode, etc.)
│   ├── engineering/
│   │   ├── backend-architect.md
│   │   ├── QA-engineer.md
│   │   ├── technical-writer.md
│   │   ├── devops-engineer.md
│   │   ├── frontend-developer.md
│   │   ├── security-engineer.md
│   │   ├── mobile-developer.md
│   │   ├── machine-learning-engineer.md
│   │   ├── senior-dev.md
│   │   ├── data-engineer.md
│   │   ├── site-reliability-engineer.md
│   │   └── accessibility-specialist.md
│   ├── creative/
│   │   ├── copywriter.md
│   │   ├── ui-ux-designer.md
│   │   └── ux-researcher.md
│   └── business/
│       ├── product-manager.md
│       ├── seo-specialist.md
│       ├── scrum-master.md
│       ├── data-analyst.md
│       ├── legal-compliance-advisor.md
│       └── customer-support-specialist.md
├── scripts/                    # Scripts to transpile or validate frontmatter format
│   ├── transpile-personas.py
│   └── validate-frontmatter.py
├── Persona-Template.md         # Starting point for new personas
├── README.md                   # Repository documentation & directory
└── LICENSE
```

## Agents

### GitHub Copilot custom agents (`.github/agents/`)

| Agent | Description |
| --- | --- |
| [senior-dev](.github/agents/senior-dev.agent.md) | Senior software engineer who writes clean, tested, maintainable code and explains trade-offs. |
| [ui-ux-designer](.github/agents/ui-ux-designer.agent.md) | Turns user flows into wireframes, maintains the design system and reviews visual fidelity. |
| [technical-writer](.github/agents/technical-writer.agent.md) | Writes developer docs and SDK guides from the repository's API code and architecture. |
| [seo-specialist](.github/agents/seo-specialist.agent.md) | Audits copy and recommends keyword, meta tag and structure improvements. |
| [backend-architect](.github/agents/backend-architect.agent.md) | Designs backend systems, APIs and data models, and documents the decisions. |
| [qa-engineer](.github/agents/qa-engineer.agent.md) | Plans, writes and runs tests, and reports reproducible bugs. |
| [copywriter](.github/agents/copywriter.agent.md) | Writes and edits copy for a specific audience and brand voice. |
| [product-manager](.github/agents/product-manager.agent.md) | Turns problems into prioritized, well-scoped requirements. |
| [scrum-master](.github/agents/scrum-master.agent.md) | Removes sprint bottlenecks and writes ready-to-execute GitHub or Jira issues. |
| [data-analyst](.github/agents/data-analyst.agent.md) | Analyzes user behavior and product metrics for data-backed feature insights. |
| [legal-compliance-advisor](.github/agents/legal-compliance-advisor.agent.md) | Reviews requirements, code and copy for GDPR, CCPA and AI-governance risks. |
| [devops-engineer](.github/agents/devops-engineer.agent.md) | Builds and maintains CI/CD pipelines, infrastructure as code and observability. |
| [frontend-developer](.github/agents/frontend-developer.agent.md) | Builds accessible, responsive and performant UIs that match the design system. |
| [customer-support-specialist](.github/agents/customer-support-specialist.agent.md) | Investigates customer issues, drafts replies and writes bug reports and help content. |
| [security-engineer](.github/agents/security-engineer.agent.md) | Reviews code for vulnerabilities (read-only), or threat-models, hardens and fixes them. |
| [mobile-developer](.github/agents/mobile-developer.agent.md) | Builds fast, reliable and accessible iOS and Android features. |
| [machine-learning-engineer](.github/agents/machine-learning-engineer.agent.md) | Builds, evaluates and prepares ML models and LLM features for production. |
| [data-engineer](.github/agents/data-engineer.agent.md) | Builds and tests data pipelines, transformation models and warehouse schemas. |
| [site-reliability-engineer](.github/agents/site-reliability-engineer.agent.md) | Defines SLOs and alerts, writes runbooks and postmortems, and improves service resilience. |
| [accessibility-specialist](.github/agents/accessibility-specialist.agent.md) | Audits UI code against WCAG 2.2 AA (read-only), or fixes accessibility barriers. |
| [ux-researcher](.github/agents/ux-researcher.agent.md) | Writes research plans and test guides, and synthesizes findings into recommendations. |

### Cross-platform personas (`personas/`)

| Persona | Category | Description |
| --- | --- | --- |
| [backend-architect](personas/engineering/backend-architect.md) | Engineering | Designs scalable, reliable backend systems, APIs and data models. |
| [qa-engineer](personas/engineering/QA-engineer.md) | Engineering | Plans and writes tests, hunts edge cases and verifies features. |
| [technical-writer](personas/engineering/technical-writer.md) | Engineering | Turns backend API code and architecture into developer docs and SDK guides. |
| [devops-engineer](personas/engineering/devops-engineer.md) | Engineering | Builds CI/CD pipelines, infrastructure as code and observability for safe, frequent releases. |
| [frontend-developer](personas/engineering/frontend-developer.md) | Engineering | Builds accessible, responsive and performant user interfaces. |
| [security-engineer](personas/engineering/security-engineer.md) | Engineering | Reviews code for vulnerabilities and builds security in through threat modeling, hardening and remediation. |
| [mobile-developer](personas/engineering/mobile-developer.md) | Engineering | Builds fast, reliable and accessible iOS and Android apps, native or cross-platform. |
| [machine-learning-engineer](personas/engineering/machine-learning-engineer.md) | Engineering | Builds, evaluates and deploys ML models and LLM features that hold up in production. |
| [senior-dev](personas/engineering/senior-dev.md) | Engineering | Writes clean, tested, maintainable code that fits the existing codebase. |
| [data-engineer](personas/engineering/data-engineer.md) | Engineering | Builds reliable, well-tested data pipelines, models and warehouses. |
| [site-reliability-engineer](personas/engineering/site-reliability-engineer.md) | Engineering | Keeps production reliable through SLOs, incident response, postmortems and capacity planning. |
| [accessibility-specialist](personas/engineering/accessibility-specialist.md) | Engineering | Audits interfaces against WCAG 2.2 and fixes barriers for assistive technology users. |
| [copywriter](personas/creative/copywriter.md) | Creative | Writes clear, persuasive copy for a specific audience and voice. |
| [ui-ux-designer](personas/creative/ui-ux-designer.md) | Creative | Turns user flows into wireframes, builds design systems and reviews visual fidelity. |
| [ux-researcher](personas/creative/ux-researcher.md) | Creative | Plans and runs user research and turns findings into evidence-backed decisions. |
| [product-manager](personas/business/product-manager.md) | Business | Turns problems into prioritized, well-scoped requirements. |
| [seo-specialist](personas/business/seo-specialist.md) | Business | Audits copy and optimizes keywords, meta tags and structure for search. |
| [scrum-master](personas/business/scrum-master.md) | Business | Improves team flow, removes sprint bottlenecks and writes ready-to-execute issues. |
| [data-analyst](personas/business/data-analyst.md) | Business | Turns user behavior and product metrics into data-backed feature insights. |
| [legal-compliance-advisor](personas/business/legal-compliance-advisor.md) | Business | Reviews requirements and copy for GDPR, CCPA and AI-governance risks before launch. |
| [customer-support-specialist](personas/business/customer-support-specialist.md) | Business | Resolves customer issues with empathetic replies and turns recurring problems into bug reports and help content. |

## Usage

- **GitHub Copilot**: files in `.github/agents/` are picked up automatically as custom agents in this repository. Copy them into another repository's `.github/agents/` to use them there.
- **Claude Code, Cursor and OpenCode**: generate ready-to-use files with the transpiler below, or copy personas by hand.
- **Other tools**: use the body of a persona file as a system prompt, or copy it into your tool's agent or rules configuration.

### Transpile personas

[`scripts/transpile-personas.py`](scripts/transpile-personas.py) converts every persona in `personas/` into each tool's format:

| Output | Format |
| --- | --- |
| `.claude/agents/<name>.md` | Claude Code subagent with `name` and `description` frontmatter |
| `.cursor/rules/<name>.mdc` | Cursor rule with `description`, `globs` and `alwaysApply: false` frontmatter |
| `.opencode/agents/<name>.md` | OpenCode subagent with `description` and `mode: subagent` frontmatter |

The persona body is copied unchanged. Template-only fields (`category`, `role`, `vibe`, `emoji`, `color`) are dropped because none of these tools use them.

```sh
# Into another project (Claude Code agents, Cursor rules and OpenCode agents)
python3 scripts/transpile-personas.py --out ~/code/my-project

# Claude Code user-level agents, available in all your projects
python3 scripts/transpile-personas.py --out ~ --target claude

# Into this repository (the generated folders are git-ignored)
python3 scripts/transpile-personas.py
```

`--target` accepts `all` (default), `claude`, `cursor` or `opencode`. Existing files with the same name are overwritten. The script stops without writing anything if a persona is missing `name` or `description`, has a `name` that is not lowercase letters, digits and hyphens, or shares a `name` with another persona.

### Claude Code

Claude Code loads subagents from Markdown files with `name` and `description` frontmatter, which every persona already has.

```sh
# Project-level: available only in that project
mkdir -p .claude/agents
cp personas/engineering/backend-architect.md .claude/agents/

# User-level: available in all your projects
mkdir -p ~/.claude/agents
cp personas/engineering/backend-architect.md ~/.claude/agents/
```

To install every persona at once:

```sh
mkdir -p ~/.claude/agents
cp personas/*/*.md ~/.claude/agents/
```

Run `/agents` in Claude Code to confirm they are loaded. Claude delegates to a subagent automatically when a task matches its `description`, or you can ask for one by name, for example "use the backend-architect agent to design this API".

### Cursor

Cursor loads project rules from `.mdc` files in `.cursor/rules/`. Copy a persona there with the `.mdc` extension:

```sh
mkdir -p .cursor/rules
cp personas/creative/copywriter.md .cursor/rules/copywriter.mdc
```

To install every persona at once:

```sh
mkdir -p .cursor/rules
for f in personas/*/*.md; do cp "$f" ".cursor/rules/$(basename "$f" .md).mdc"; done
```

Cursor uses the `description` to decide when to apply a rule. You can also attach one manually in chat by typing `@` followed by the rule name, for example `@copywriter`.

### OpenCode

OpenCode loads agents from Markdown files and names each agent after its file. The body becomes the agent's system prompt. Personas need different frontmatter for OpenCode: `description`, plus `mode: subagent` so the persona runs as a helper instead of replacing the main agent. Custom agents default to `primary`. Use the transpiler rather than copying persona files directly.

```sh
# Project-level: .opencode/agents/ in that project
python3 scripts/transpile-personas.py --out ~/code/my-project --target opencode

# Global: available in all your projects
python3 scripts/transpile-personas.py --out /tmp/personas --target opencode
mkdir -p ~/.config/opencode/agents
cp /tmp/personas/.opencode/agents/*.md ~/.config/opencode/agents/
```

Each generated file looks like this:

```md
---
description: "Plans and writes tests, hunts edge cases and verifies features against requirements."
mode: subagent
---

# Identity & Core Mission
...
```

To use one, ask the main agent to delegate to it by name, for example "use the qa-engineer subagent to write tests for this module". OpenCode uses the `description` to decide which subagent fits a task. To restrict what an agent can do, add OpenCode's `permissions` rules to its frontmatter after generating it; see the [OpenCode agents documentation](https://opencode.ai/docs/agents/).

## File format

Every file starts with YAML frontmatter:

```yaml
---
name: backend-architect
description: One-line summary of what the agent does.
category: engineering   # personas only
---
```

Required keys:

| Location | Required keys |
| --- | --- |
| `personas/**/*.md` | `name`, `description`, `category` |
| `.github/agents/*.agent.md` | `name`, `description` |

Extra keys are allowed.

### Persona template

[`Persona-Template.md`](Persona-Template.md) is the standard starting point for a new persona. Besides the required keys, it adds optional metadata (`role`, `vibe`, `emoji`, `color`) and a body with these sections:

- **Identity & Core Mission**: who the persona is and what it is for.
- **Core Capabilities**: the main things it does.
- **Specialized Skills**: specific tools, languages or techniques.
- **Decision Framework & Logic**: how it prioritizes and makes calls.
- **Boundaries & Constraints**: what it must never do.

To create a persona from it:

```sh
cp Persona-Template.md personas/<category>/<persona-name>.md
```

Then replace the example Security Reviewer content with your own.

## Validation

Validate all files locally with:

```sh
python3 scripts/validate-frontmatter.py
```

It checks that:

- every file under `personas/` and `.github/agents/` has the required keys, and none of them is missing or empty;
- every persona has a matching GitHub Copilot agent at `.github/agents/<name>.agent.md`, where `<name>` is the persona's `name`.

It exits with a non-zero status if any check fails. `Persona-Template.md` lives at the repository root, so it is not checked. Copilot agents without a matching persona are allowed.

### Validate personas workflow

The [Validate personas](.github/workflows/validate-personas.yml) GitHub Actions workflow runs the validator, then runs the transpiler into a temporary folder to make sure every persona converts cleanly. It runs:

- on every pull request, whatever it changes, because it is a required check for merging into `main`;
- on pushes to `main` that change `personas/`, `.github/agents/`, `scripts/` or the workflow itself;
- manually, from the **Actions** tab (`workflow_dispatch`).

A pull request that adds a persona with missing frontmatter, without a matching Copilot agent, or that cannot be transpiled, fails this check.

## Contributing

1. Copy `Persona-Template.md` into the matching `personas/<category>/` folder (or add a Copilot agent under `.github/agents/` with the `.agent.md` suffix).
2. Run `python3 scripts/validate-frontmatter.py` and fix any errors.
3. Add a matching Copilot agent in `.github/agents/<name>.agent.md` (the validator fails without one), and add both to the tables above.
4. Open a pull request. The **Validate personas** check must pass before it is merged.
