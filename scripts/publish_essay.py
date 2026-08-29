#!/usr/bin/env python3
"""
Advanced publishing and syndication engine for alanpruitt.com
Automates bilingual frontmatter generation, automated changelog entries,
LinkedIn executive brief generation, POUR-Audit testing, and Git CI/CD deployment.
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

    essay_num = int(sys.argv[1])
    essay_str = f"{essay_num:02d}"
    slug = f"essay-{essay_num}"

    # Strict Arizona Timezone (MST/PDT)
    tz = zoneinfo.ZoneInfo("America/Phoenix")
    now = datetime.now(tz)
    now_iso = now.strftime("%Y-%m-%dT%H:%M:%S%z")
    formatted_date = f"{now_iso[:-2]}:{now_iso[-2:]}"
    display_date = now.strftime("%B %d, %Y")
    display_date_es = now.strftime("%d de %B de %Y")

    en_path = f"content/en/essays/essay-{essay_num}.md"
    es_path = f"content/es/essays/essay-{essay_num}.md"
    os.makedirs("dist/syndication", exist_ok=True)
    linkedin_path = f"dist/syndication/essay-{essay_num}-linkedin.md"

    print(f"\n🚀 Initializing Publishing Pipeline for Essay {essay_num} ({slug})...")

    # Metadata capture
    title_en = ""
    desc_en = ""
    title_es = ""
    desc_es = ""

    if not os.path.exists(en_path):
        title_en = input("English Title: ").strip()
        desc_en = input("English Description: ").strip()

        en_template = f"""---
title: "Essay {essay_num}: {title_en}"
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
        print(f"  ℹ Existing English file found: {en_path}")
        with open(en_path, "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith("title:"):
                    title_en = line.replace("title:", "").strip().strip('"').replace(f"Essay {essay_num}: ", "")
                if line.startswith("description:"):
                    desc_en = line.replace("description:", "").strip().strip('"')

    if not os.path.exists(es_path):
        title_es = input("Spanish Title: ").strip()
        desc_es = input("Spanish Description: ").strip()

        es_template = f"""---
title: "Ensayo {essay_num}: {title_es}"
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
        print(f"  ℹ Existing Spanish file found: {es_path}")

    # Step 2: Generate LinkedIn Executive Brief Template
    linkedin_template = f"""# LinkedIn Syndicate Brief: Essay {essay_num}
**Target URL:** https://alanpruitt.com/essays/{slug}/
**Date:** {display_date}

---

### Executive Copy

{desc_en}

Under the DOJ's ADA Title II Final Rule (28 CFR Part 35), higher education institutions face strict WCAG 2.2 AA technical standards. In Essay {essay_num}, I examine how Curriculum-as-Code transforms compliance from reactive remediation into automated, CI/CD-governed software pipelines.

Key takeaways:
• Eliminating manual configuration drift across Canvas LMS course shells.
• Deterministic testing with Axe-core and Playwright prior to deployment.
• Establishing institutional sovereignty over academic digital assets.

Read the full analysis:
👉 https://alanpruitt.com/essays/{slug}/

#HigherEducation #Accessibility #ADATitleII #CurriculumAsCode #EdTech #HigherEdLeadership
"""
    with open(linkedin_path, "w", encoding="utf-8") as f:
        f.write(linkedin_template)
    print(f"  ✓ Generated LinkedIn brief: {linkedin_path}")

    # Step 3: Rebuild with Hugo
    print("\n🔨 Rebuilding static site with Hugo...")
    subprocess.run(["rm", "-rf", "public", "resources"], check=True)
    build_result = subprocess.run(["hugo", "-D"], capture_output=True, text=True)
    if build_result.returncode != 0:
        print(f"❌ Hugo build failed:\n{build_result.stderr}")
        sys.exit(1)
    print("  ✓ Hugo compiled cleanly.")

    # Step 4: Verify Card Rendering
    with open("public/index.html", "r", encoding="utf-8") as f:
        home_en = f.read()
    if slug in home_en:
        print(f"  ✓ Verified: {slug} is rendering on English homepage.")
    else:
        print(f"  ⚠️ Warning: {slug} not detected in public/index.html")

    # Step 5: Test runner
    if os.path.exists("package.json"):
        print("\n🧪 Running local accessibility test suite...")
        subprocess.run(["npm", "run", "audit:local"], check=False)

    # Step 6: Git deployment confirmation
    deploy = input(f"\n📦 Deploy Essay {essay_num} to GitHub production? (y/N): ").strip().lower()
    if deploy == "y":
        subprocess.run(["git", "add", en_path, es_path, linkedin_path], check=True)
        commit_msg = f"feat(essays): publish bilingual Essay {essay_num} and generate syndication brief"
        subprocess.run(["git", "commit", "-m", commit_msg], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("\n🎉 Deployed to origin main! CI/CD pipeline triggered.")
        print(f"📄 LinkedIn copy ready in: {linkedin_path}")
    else:
        print("\n⏸️ Build saved locally. You can edit the markdown and run again anytime.")

if __name__ == "__main__":
    main()
