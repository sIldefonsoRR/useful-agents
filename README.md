# useful-agents

A collection of useful AI agent personas, ready to drop into GitHub Copilot, Claude, Cursor and other AI tools.

## Repository structure

```
.
├── .github/
│   ├── agents/                 # Native path for GitHub Copilot custom agents
│   │   ├── senior-dev.agent.md
│   │   ├── security-reviewer.agent.md
│   │   ├── ui-ux-designer.agent.md
│   │   ├── technical-writer.agent.md
│   │   ├── seo-specialist.agent.md
│   │   ├── backend-architect.agent.md
│   │   ├── qa-engineer.agent.md
│   │   ├── copywriter.agent.md
│   │   └── product-manager.agent.md
│   └── workflows/
│       └── validate-personas.yml   # CI check for persona and agent frontmatter
├── personas/                   # General, cross-platform personas (Claude, Cursor, etc.)
│   ├── engineering/
│   │   ├── backend-architect.md
│   │   ├── QA-engineer.md
│   │   └── technical-writer.md
│   ├── creative/
│   │   ├── copywriter.md
│   │   └── ui-ux-designer.md
│   └── business/
│       ├── product-manager.md
│       └── seo-specialist.md
├── scripts/                    # Scripts to transpile or validate frontmatter format
├── Persona-Template.md         # Starting point for new personas
├── README.md                   # Repository documentation & directory
└── LICENSE
```

## Agents

### GitHub Copilot custom agents (`.github/agents/`)

| Agent | Description |
| --- | --- |
| [senior-dev](.github/agents/senior-dev.agent.md) | Senior software engineer who writes clean, tested, maintainable code. |
| [security-reviewer](.github/agents/security-reviewer.agent.md) | Audits code changes for vulnerabilities and insecure patterns. |
| [ui-ux-designer](.github/agents/ui-ux-designer.agent.md) | Turns user flows into wireframes, maintains the design system and reviews visual fidelity. |
| [technical-writer](.github/agents/technical-writer.agent.md) | Writes developer docs and SDK guides from the repository's API code and architecture. |
| [seo-specialist](.github/agents/seo-specialist.agent.md) | Audits copy and recommends keyword, meta tag and structure improvements. |
| [backend-architect](.github/agents/backend-architect.agent.md) | Designs backend systems, APIs and data models, and documents the decisions. |
| [qa-engineer](.github/agents/qa-engineer.agent.md) | Plans, writes and runs tests, and reports reproducible bugs. |
| [copywriter](.github/agents/copywriter.agent.md) | Writes and edits copy for a specific audience and brand voice. |
| [product-manager](.github/agents/product-manager.agent.md) | Turns problems into prioritized, well-scoped requirements. |

### Cross-platform personas (`personas/`)

| Persona | Category | Description |
| --- | --- | --- |
| [backend-architect](personas/engineering/backend-architect.md) | Engineering | Designs scalable, reliable backend systems, APIs and data models. |
| [qa-engineer](personas/engineering/QA-engineer.md) | Engineering | Plans and writes tests, hunts edge cases and verifies features. |
| [technical-writer](personas/engineering/technical-writer.md) | Engineering | Turns backend API code and architecture into developer docs and SDK guides. |
| [copywriter](personas/creative/copywriter.md) | Creative | Writes clear, persuasive copy for a specific audience and voice. |
| [ui-ux-designer](personas/creative/ui-ux-designer.md) | Creative | Turns user flows into wireframes, builds design systems and reviews visual fidelity. |
| [product-manager](personas/business/product-manager.md) | Business | Turns problems into prioritized, well-scoped requirements. |
| [seo-specialist](personas/business/seo-specialist.md) | Business | Audits copy and optimizes keywords, meta tags and structure for search. |

## Usage

- **GitHub Copilot**: files in `.github/agents/` are picked up automatically as custom agents in this repository. Copy them into another repository's `.github/agents/` to use them there.
- **Claude, Cursor and others**: use the body of a persona file as a system prompt, or copy it into your tool's agent or rules configuration.

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

It checks every file under `personas/` and `.github/agents/` for the required keys and exits with a non-zero status if any are missing or empty. `Persona-Template.md` lives at the repository root, so it is not checked.

### Validate personas workflow

The [Validate personas](.github/workflows/validate-personas.yml) GitHub Actions workflow runs the same script automatically:

- on pull requests that change `personas/`, `.github/agents/`, the validator script or the workflow itself;
- on pushes to `main` that touch the same paths;
- manually, from the **Actions** tab (`workflow_dispatch`).

A pull request that adds a persona with missing frontmatter fails this check.

## Contributing

1. Copy `Persona-Template.md` into the matching `personas/<category>/` folder (or add a Copilot agent under `.github/agents/` with the `.agent.md` suffix).
2. Run `python3 scripts/validate-frontmatter.py` and fix any errors.
3. Add the persona to the tables above.
4. Open a pull request. The **Validate personas** check must pass before it is merged.
