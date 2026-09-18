---
title: "Essay 35: Automating Accessibility - Curriculum-as-Code & Continuous Integration"
date: 2026-09-18T10:40:00-07:00
draft: false
tags: ["Accessibility", "Instructional Design", "Curriculum-as-Code", "GitHub Actions", "ADA Title II", "WCAG 2.1 AA"]
categories: ["Essays"]
description: "How automated GitHub Actions linters and Curriculum-as-Code turn ADA Title II and WCAG 2.1 AA accessibility compliance into a continuous integration baseline."
translationKey: "essay-35"
slug: "essay-35"
---

When public higher education institutions faced the Department of Justice's mandate for **ADA Title II (WCAG 2.1/2.2 Level AA)** compliance, traditional instructional design hit an operational wall. Manually auditing hundreds of Canvas pages, inspecting heading tags in rich text editors, and manually verifying image alt-text lengths across multi-section course fleets is unsustainable.

Sustainable accessibility requires a fundamental paradigm shift: **Curriculum-as-Code**.

---

## 🛠️ The Shift-Left Accessibility Architecture

In software engineering, "Shift-Left" means catching defects early in the development lifecycle rather than in production. Applying this to course design transforms instructional assets into plain, version-controlled Markdown files audited by automated CI/CD pipelines before deployment.

```
+------------------+     +-------------------------------+     +-----------------------+
| Plain Markdown   | --> | GitHub Actions CI Pipeline    | --> | Production Canvas LMS |
| Course Shells    |     | (Heading & Alt-Text Linters)  |     | Deployment            |
+------------------+     +-------------------------------+     +-----------------------+
```

---

## 🔒 Core Audit Guardrails

Our custom **Curriculum-as-Code Accessibility Linter** enforces deterministic rules across the entire course fleet:

1. **Deterministic Heading Hierarchy (WCAG 1.3.1)**:
   - Canvas LMS reserves `<h1>` for page titles. All document content must begin at `<h2>`.
   - Strict sequential progression prevents skipping heading levels (e.g., jumping directly from `<h2>` to `<h4>`).
   - Mixed HTML (`<h1-h6>`) and Markdown (`#{1,6}`) headers are parsed seamlessly.

2. **Concise Image Alt-Text (WCAG 1.1.1)**:
   - All visual elements must include non-empty, descriptive alt text.
   - Restricts alt-text length to $\le 120$ characters to maintain efficient screen reader output without cognitive overload.

3. **Structural Delimiter Immunity**:
   - Structural prompt fences (`###`, `### STRUCTURAL_DELIMITER`) used in clinical AI prompt engineering are safely isolated, preventing false-positive heading skips.

---

## 🚀 Continuous Integration via GitHub Actions

By embedding the linter into `.github/workflows/accessibility-audit.yml`, every `git push` or pull request automatically validates 100% of course Markdown assets:

```yaml
name: Curriculum-as-Code Accessibility Audit

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  accessibility-audit:
    name: WCAG 2.1 AA & ADA Title II Compliance Check
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - name: Run Accessibility Linter
        run: python3 scripts/curriculum_accessibility_linter.py .
```

---

## 💡 Summary: Immutable Accessibility Baselines

Treating curriculum as code converts accessibility compliance from an administrative chore into a permanent, automated build baseline. When federal regulations or institutional standards update, automated scripts audit and refactor entire course fleets in seconds—guaranteeing universal access for every resident student.
