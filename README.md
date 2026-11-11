# useful-agents

A collection of useful AI agent personas, ready to drop into GitHub Copilot, Claude, Cursor and other AI tools.

## Repository structure

```
.
├── .github/
│   └── agents/                 # Native path for GitHub Copilot custom agents
│       ├── senior-dev.agent.md
│       └── security-reviewer.agent.md
├── personas/                   # General, cross-platform personas (Claude, Cursor, etc.)
│   ├── engineering/
│   │   ├── backend-architect.md
│   │   └── QA-engineer.md
│   ├── creative/
│   │   └── copywriter.md
│   └── business/
│       └── product-manager.md
├── scripts/                    # Scripts to transpile or validate frontmatter format
├── README.md                   # Repository documentation & directory
└── LICENSE
```

## Agents

### GitHub Copilot custom agents (`.github/agents/`)

| Agent | Description |
| --- | --- |
| [senior-dev](.github/agents/senior-dev.agent.md) | Senior software engineer who writes clean, tested, maintainable code. |
| [security-reviewer](.github/agents/security-reviewer.agent.md) | Audits code changes for vulnerabilities and insecure patterns. |

### Cross-platform personas (`personas/`)

| Persona | Category | Description |
| --- | --- | --- |
| [backend-architect](personas/engineering/backend-architect.md) | Engineering | Designs scalable, reliable backend systems, APIs and data models. |
| [qa-engineer](personas/engineering/QA-engineer.md) | Engineering | Plans and writes tests, hunts edge cases and verifies features. |
| [copywriter](personas/creative/copywriter.md) | Creative | Writes clear, persuasive copy for a specific audience and voice. |
| [product-manager](personas/business/product-manager.md) | Business | Turns problems into prioritized, well-scoped requirements. |

## Usage

- **GitHub Copilot**: files in `.github/agents/` are picked up automatically as custom agents in this repository. Copy them into another repository's `.github/agents/` to use them there.
- **Claude, Cursor and others**: use the body of a persona file as a system prompt, or copy it into your tool's agent or rules configuration.

## File format

Every file starts with YAML frontmatter:

```yaml
---
name: backend-architect
description: One-line summary of what the agent does.
category: engineering   # personas only
---
```

Validate all files with:

```sh
python3 scripts/validate-frontmatter.py
```

## Contributing

Add a persona under the matching `personas/<category>/` folder (or a Copilot agent under `.github/agents/` with the `.agent.md` suffix), run the validator, add it to the tables above and open a pull request.
