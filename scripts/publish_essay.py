#!/usr/bin/env python3
"""
Single-command publishing engine for alanpruitt.com
Automates bilingual frontmatter generation, local verification,
POUR-Audit linting, and Git CI/CD deployment.
"""

import sys
import os
import subprocess
from datetime import datetime
import zoneinfo

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/publish_essay.py <essay_number>")
        print("Example: python3 scripts/publish_essay.py 29")
        sys.exit(1)

    essay_num = f"{int(sys.argv[1]):02d}"
    slug = f"essay-{int(sys.argv[1])}"

    # Get local timestamp in MST/PDT with strict ISO-8601 formatting
    tz = zoneinfo.ZoneInfo("America/Phoenix")
    now_iso = datetime.now(tz).strftime("%Y-%m-%dT%H:%M:%S%z")
    # Format offset to include colon (e.g. -07:00)
    formatted_date = f"{now_iso[:-2]}:{now_iso[-2:]}"

    en_path = f"content/en/essays/essay-{int(sys.argv[1])}.md"
    es_path = f"content/es/essays/essay-{int(sys.argv[1])}.md"

    print(f"\n🚀 Initializing Essay {essay_num} ({slug})...")

    # Prompt for metadata if files don't already exist
    if not os.path.exists(en_path):
        title_en = input("English Title: ").strip()
        desc_en = input("English Description: ").strip()

        en_template = f"""---
title: "Essay {int(sys.argv[1])}: {title_en}"
date: {formatted_date}
publishDate: {formatted_date}
draft: false
slug: "{slug}"
description: "{desc_en}"
categories: ["Curriculum-as-Code", "Accessibility", "Higher Education Governance", "ADA Title II"]
layout: "single"
---

## Overview

Draft content here...
"""
        os.makedirs(os.path.dirname(en_path), exist_ok=True)
        with open(en_path, "w", encoding="utf-8") as f:
            f.write(en_template)
        print(f"  ✓ Created: {en_path}")
    else:
        print(f"  ℹ Existing file found: {en_path}")

    if not os.path.exists(es_path):
        title_es = input("Spanish Title: ").strip()
        desc_es = input("Spanish Description: ").strip()

        es_template = f"""---
title: "Ensayo {int(sys.argv[1])}: {title_es}"
date: {formatted_date}
publishDate: {formatted_date}
draft: false
slug: "{slug}"
description: "{desc_es}"
categories: ["Curriculum-as-Code", "Accesibilidad", "Gobernanza en Educación Superior", "Título II de la ADA"]
layout: "single"
---

## Resumen

Borrador de contenido aquí...
"""
        os.makedirs(os.path.dirname(es_path), exist_ok=True)
        with open(es_path, "w", encoding="utf-8") as f:
            f.write(es_template)
        print(f"  ✓ Created: {es_path}")
    else:
        print(f"  ℹ Existing file found: {es_path}")

    # Step 2: Clean build & test
    print("\n🔨 Rebuilding static site with Hugo...")
    subprocess.run(["rm", "-rf", "public", "resources"], check=True)
    build_result = subprocess.run(["hugo", "-D"], capture_output=True, text=True)
    
    if build_result.returncode != 0:
        print(f"❌ Hugo build failed:\n{build_result.stderr}")
        sys.exit(1)
    print("  ✓ Hugo build compiled successfully.")

    # Step 3: Verify card rendering in compiled public output
    print("\n🔍 Auditing card presence in compiled HTML...")
    with open("public/index.html", "r", encoding="utf-8") as f:
        home_en = f.read()
    
    if slug in home_en:
        print(f"  ✓ Verified: {slug} is rendering on English homepage (public/index.html)")
    else:
        print(f"  ⚠️ Warning: {slug} not found in public/index.html")

    # Step 4: Run local accessibility suite if configured
    if os.path.exists("package.json"):
        print("\n🧪 Running local accessibility test runner...")
        subprocess.run(["npm", "run", "audit:local"], check=False)

    # Step 5: Git deployment confirmation
    deploy = input(f"\n📦 Deploy Essay {int(sys.argv[1])} to GitHub? (y/N): ").strip().lower()
    if deploy == "y":
        subprocess.run(["git", "add", en_path, es_path], check=True)
        commit_msg = f"feat(essays): publish bilingual Essay {int(sys.argv[1])} and sync metadata"
        subprocess.run(["git", "commit", "-m", commit_msg], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("\n🎉 Deployment pushed to origin main! CI/CD pipeline triggered.")
    else:
        print("\n⏸️ Deployment aborted. Files saved locally for editing.")

if __name__ == "__main__":
    main()
