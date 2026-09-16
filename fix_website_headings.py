#!/usr/bin/env python3
"""
Script: fix_website_headings.py
Description: Fixes top-level headings (# -> ##) and heading hierarchy across Hugo content files in alanpruitt.github.io.
"""

import os
import re
from pathlib import Path

TARGET_DIR = Path("/Users/alanpruitt/alanpruitt.github.io/content")

def fix_file(filepath: Path):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.splitlines(keepends=True)
    in_frontmatter = False
    frontmatter_count = 0
    first_heading_fixed = False
    modified = False

    for i in range(len(lines)):
        line = lines[i]
        stripped = line.strip()

        if stripped == "---":
            frontmatter_count += 1
            if frontmatter_count <= 2:
                in_frontmatter = (frontmatter_count % 2 != 0)
                continue

        if in_frontmatter:
            continue

        # Ignore structural delimiter lines
        if stripped in ["###", "> ###"] or stripped.startswith("### STRUCTURAL") or stripped.startswith("### |"):
            continue

        # Match `# Heading`
        heading_match = re.match(r'^(#)\s+(.*)', line)
        if heading_match:
            title = heading_match.group(2)
            lines[i] = f"## {title}\n"
            modified = True
            first_heading_fixed = True
            print(f"  [FIX] {filepath.name} (Line {i+1}): Changed '# {title}' -> '## {title}'")

    if modified:
        with open(filepath, "w", encoding="utf-8") as f:
            f.writelines(lines)

def main():
    print(f"🛠️ Fixing headings in {TARGET_DIR}...")
    for ext in ["*.md", "*.markdown"]:
        for filepath in TARGET_DIR.rglob(ext):
            fix_file(filepath)
    print("✅ Heading fixes complete!")

if __name__ == "__main__":
    main()
