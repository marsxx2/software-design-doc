#!/usr/bin/env python3
"""Validate plugin structure: manifests, skill frontmatter, README coverage."""
import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
errors = []


def err(msg):
    errors.append(msg)


# --- manifests -------------------------------------------------------------
for rel in (".claude-plugin/plugin.json", ".claude-plugin/marketplace.json"):
    p = ROOT / rel
    try:
        data = json.loads(p.read_text())
    except Exception as e:  # noqa: BLE001
        err(f"{rel}: invalid or missing JSON ({e})")
        continue
    if rel.endswith("plugin.json"):
        for key in ("name", "version", "description"):
            if not data.get(key):
                err(f"{rel}: missing '{key}'")
        if not re.fullmatch(r"\d+\.\d+\.\d+", str(data.get("version", ""))):
            err(f"{rel}: version must look like 1.2.3")

# --- skills ----------------------------------------------------------------
skills_dir = ROOT / "skills"
readme = (ROOT / "README.md").read_text() if (ROOT / "README.md").exists() else ""
names = []
for skill_md in sorted(skills_dir.glob("*/SKILL.md")):
    folder = skill_md.parent.name
    text = skill_md.read_text()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        err(f"{folder}: missing YAML frontmatter")
        continue
    try:
        fm = yaml.safe_load(m.group(1))
    except yaml.YAMLError as e:
        err(f"{folder}: invalid YAML frontmatter ({e})")
        continue
    if fm.get("name") != folder:
        err(f"{folder}: frontmatter name '{fm.get('name')}' != folder name")
    desc = fm.get("description", "")
    if not desc or len(desc) < 40:
        err(f"{folder}: description missing or too short")
    if len(desc) > 1024:
        err(f"{folder}: description exceeds 1024 characters")
    if len(text.splitlines()) > 500:
        err(f"{folder}: SKILL.md exceeds 500 lines")
    if f"`{folder}`" not in readme:
        err(f"{folder}: not listed in README.md")
    names.append(folder)

if not names:
    err("no skills found under skills/")

if errors:
    print("Validation failed:")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)
print(f"OK: {len(names)} skills validated")
