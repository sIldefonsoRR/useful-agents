#!/usr/bin/env python3
"""Validate the YAML frontmatter of agent and persona files.

Checks every Markdown file under personas/ and .github/agents/ for a
frontmatter block containing the required keys, and checks that every
persona has a matching GitHub Copilot agent at
.github/agents/<name>.agent.md. Exits non-zero on failure.

Usage: python3 scripts/validate-frontmatter.py
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
AGENTS = ROOT / ".github/agents"

RULES = {
    "personas": {"glob": "**/*.md", "required": ["name", "description", "category"]},
    ".github/agents": {"glob": "*.agent.md", "required": ["name", "description"]},
}

FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
KEY = re.compile(r"^([A-Za-z_][\w-]*):\s*(.*)$")


def parse_keys(text):
    match = FRONTMATTER.match(text)
    if not match:
        return None
    keys = {}
    for line in match.group(1).splitlines():
        m = KEY.match(line)
        if m:
            keys[m.group(1)] = unquote(m.group(2).strip())
    return keys


def unquote(value):
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    return value


def main():
    errors = []
    checked = 0
    for directory, rule in RULES.items():
        for path in sorted((ROOT / directory).glob(rule["glob"])):
            checked += 1
            rel = path.relative_to(ROOT)
            keys = parse_keys(path.read_text(encoding="utf-8"))
            if keys is None:
                errors.append(f"{rel}: missing frontmatter block")
                continue
            for key in rule["required"]:
                if not keys.get(key):
                    errors.append(f"{rel}: missing or empty '{key}'")
            if directory == "personas" and keys.get("name"):
                agent = AGENTS / f"{keys['name']}.agent.md"
                if not agent.is_file():
                    errors.append(f"{rel}: no matching Copilot agent at {agent.relative_to(ROOT)}")

    for error in errors:
        print(error, file=sys.stderr)
    print(f"Checked {checked} file(s), {len(errors)} error(s).")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
