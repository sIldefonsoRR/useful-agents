#!/usr/bin/env python3
"""Transpile personas into Claude Code subagents, Cursor rules and OpenCode agents.

Reads every Markdown file under personas/ and writes:

  <out>/.claude/agents/<name>.md     Claude Code subagent (name, description)
  <out>/.cursor/rules/<name>.mdc     Cursor project rule (description, globs, alwaysApply)
  <out>/.opencode/agents/<name>.md   OpenCode subagent (description, mode)

The persona body is copied unchanged. Template-only metadata (category, role,
vibe, emoji, color) is dropped because none of these tools use it.

Usage:
  python3 scripts/transpile-personas.py                      # into this repository
  python3 scripts/transpile-personas.py --out ~/my-project   # into another project
  python3 scripts/transpile-personas.py --out ~ --target claude   # user-level Claude Code agents
"""

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PERSONAS = ROOT / "personas"

FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n(.*)\Z", re.DOTALL)
KEY = re.compile(r"^([A-Za-z_][\w-]*):\s*(.*)$")
NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def unquote(value):
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    return value


def parse(path):
    match = FRONTMATTER.match(path.read_text(encoding="utf-8"))
    if not match:
        raise ValueError("missing frontmatter block")
    meta = {}
    for line in match.group(1).splitlines():
        m = KEY.match(line)
        if m:
            meta[m.group(1)] = unquote(m.group(2).strip())
    for key in ("name", "description"):
        if not meta.get(key):
            raise ValueError(f"missing or empty '{key}'")
    if not NAME.match(meta["name"]):
        raise ValueError(f"name '{meta['name']}' must be lowercase letters, digits and hyphens")
    return meta, match.group(2).lstrip("\n")


def quote(value):
    # A JSON string is a valid double-quoted YAML scalar.
    return json.dumps(value, ensure_ascii=False)


def claude_agent(meta, body):
    return (
        "---\n"
        f"name: {meta['name']}\n"
        f"description: {quote(meta['description'])}\n"
        "---\n\n"
        f"{body}"
    )


def cursor_rule(meta, body):
    return (
        "---\n"
        f"description: {quote(meta['description'])}\n"
        "globs:\n"
        "alwaysApply: false\n"
        "---\n\n"
        f"{body}"
    )


def opencode_agent(meta, body):
    # OpenCode names the agent after the file; without mode it defaults to primary.
    return (
        "---\n"
        f"description: {quote(meta['description'])}\n"
        "mode: subagent\n"
        "---\n\n"
        f"{body}"
    )


TARGETS = {
    "claude": (Path(".claude/agents"), ".md", claude_agent),
    "cursor": (Path(".cursor/rules"), ".mdc", cursor_rule),
    "opencode": (Path(".opencode/agents"), ".md", opencode_agent),
}


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--out", type=Path, default=ROOT,
                        help="directory to write .claude/ and .cursor/ into (default: repository root)")
    parser.add_argument("--target", choices=["all", *TARGETS], default="all",
                        help="which format to generate (default: all)")
    args = parser.parse_args()

    out = args.out.expanduser().resolve()
    targets = TARGETS if args.target == "all" else {args.target: TARGETS[args.target]}

    personas, errors = [], []
    for path in sorted(PERSONAS.glob("**/*.md")):
        try:
            personas.append(parse(path))
        except ValueError as error:
            errors.append(f"{path.relative_to(ROOT)}: {error}")

    names = [meta["name"] for meta, _ in personas]
    errors += [f"duplicate persona name '{n}'" for n in sorted(set(names)) if names.count(n) > 1]

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    for target, (subdir, suffix, render) in targets.items():
        directory = out / subdir
        directory.mkdir(parents=True, exist_ok=True)
        for meta, body in personas:
            (directory / f"{meta['name']}{suffix}").write_text(render(meta, body), encoding="utf-8")
        print(f"Wrote {len(personas)} {target} file(s) to {directory}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
