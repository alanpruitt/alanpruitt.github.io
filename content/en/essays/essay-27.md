---
title: "Essay 27: Curriculum-as-Code, ADA Title II Compliance, and Fleet-Wide Accessibility Refactoring"
date: 2026-08-25T16:53:00-07:00
publishDate: 2026-08-25T16:53:00-07:00
draft: false
author: "Alan Pruitt"
tags:
  - "ADA Title II"
  - "WCAG 2.2 AA"
  - "Canvas LMS"
  - "CI/CD"
  - "POUR-Audit"
categories:
  - "ada-title-ii"
  - "Curriculum-as-Code"
description: "How engineering course architectures in plain Markdown with automated CI/CD linters solves ADA Title II compliance and enables rapid, fleet-wide accessibility refactoring across live Canvas shells."
summary: "How engineering course architectures in plain Markdown with automated CI/CD linters solves ADA Title II compliance and enables rapid, fleet-wide accessibility refactoring across live Canvas shells."
translationKey: "essay-27"
slug: "essay-27"
aliases:
  - "/essays/27-ada-title-ii-fleet-refactor/"
  - "/essays/27/"
  - "/essays/essay27/"
---

## The Federal Mandate: Ending the Era of Manual Patchwork

For public higher education institutions, the federal **ADA Title II (`28 CFR Part 35`)** digital accessibility mandate leaves zero margin for reactive guesswork: every live LMS page, syllabus, assignment table, and digital learning asset must conform to **WCAG 2.2 Level AA** standards.

For more than a decade, the conventional institutional response has relied on an expensive, fragile cycle:

* Hiring temporary remediation teams to click through hundreds of pages by hand inside the LMS rich-text editor.
* Relying on commercial dashboard overlays that flag symptoms after publication without fixing the underlying source templates.
* Watching remediated courses silently regress the next semester as soon as shells are cloned or edited without structural guardrails.

Manual click-by-click remediation inside a browser interface simply does not scale across a multi-course department fleet.

---

## The Thesis: Eliminating Technical Debt with Curriculum-as-Code (CaC)

In my Exercise Science & Wellness (`EXW 101`, `150`, `210`, `245`, and `265`) engineering work, I solve accessibility drift by treating instructional materials with the same version-control and continuous-integration discipline used for production software: **Curriculum-as-Code (CaC)**.

> When curriculum lives as clean, structured Markdown in a Git Single Source of Truth (SSoT) governed by deterministic pre-commit linters, accessibility stops being a post-production chore and becomes a born-accessible structural property.

---

## My 4-Phase Fleet Refactoring Roadmap

To refactor an active multi-course fleet without disrupting ongoing instruction, I execute accessibility modernization in four deterministic phases:

### 1. Baseline Telemetry & Technical Debt Mapping (Phase 1)

Before modifying a single page, I run automated API scans across the target Canvas shells to establish an exact empirical baseline:

* Exporting raw WikiPage, Assignment, Discussion, and Syllabus HTML payloads with full local backups.
* Running programmatic checks (`pour_audit.py` and Canvas Accessibility Checker rules) to catalog skipped heading levels (`<h1>` collisions or `<h2>` -> `<h4>` jumps), unscoped tables, missing image `alt` descriptions, and low-contrast inline CSS.
* Generating an auditable JSON/Markdown remediation manifest before any write operation occurs.

### 2. Single Source of Truth (SSoT) Standardization (Phase 2)

Next, I decouple authoring from the browser WYSIWYG editor and establish the local Git repository as the authoritative source:

* Normalizing every module reading, lab, discussion, and coaching sprint into clean Markdown (`.md`) files.
* Enforcing sequential semantic hierarchy where body content always begins at `<h2>` beneath the Canvas `<h1>` Page Title.
* Replacing fragile inline styling with explicit, high-contrast foreground/background hex pairs (`9:1` Double-Contrast Guard) and responsive table structures (`<caption>` + `<th scope="col">`).

### 3. Automated Pre-Commit & CI/CD Quality Gates (Phase 3)

Compliance no longer depends on human memory during late-night course updates:

* Integrating `markdownlint`, `pour_audit.py`, and Canvas RCE accessibility validators directly into local Git pre-commit/pre-push hooks and GitHub Actions.
* Automatically blocking any commit that introduces empty or filename-based `alt` attributes, ambiguous link text, fake typed list bullets, or contrast ratios below threshold.

### 4. Deterministic API Synchronization & Re-Fetch Verification (Phase 4)

Finally, my synchronization scripts compile validated Markdown into clean semantic HTML, run a `DRY_RUN` diff, update exact Canvas page URLs via API, and re-fetch the rendered live payloads to verify **`0 Open Issues`**.

---

## Live Production Edge Case: Fleet-Wide Emoji Stripping for Screen-Reader Clarity

A concrete example of **Curriculum-as-Code** agility occurred during an active rollout in `EXW 150`. Screen readers announce decorative Unicode emojis and pictographs inline as disruptive verbal clutter (for example, reading *"rocket"* or *"check mark button"* mid-heading), creating unnecessary cognitive load for blind, low-vision, and neurodivergent students.

Rather than manually editing hundreds of Canvas pages one by one, I resolved the issue across the entire repository as a single infrastructure refactor:

1. **Deterministic Sanitization Utility:** I built a recursive Python sanitizer (`scripts/emoji_cleaner.py`) that strips decorative Unicode pictographs while preserving Spanish accents (`á, é, í, ó, ú, ñ, ¿, ¡`) and clinical math/unit symbols (`≥, °, ×, ±`).
2. **Pre-Commit Enforcement:** I wired the check directly into my pre-commit linter alongside my **Clinical Framing Protocol (`Pattern / Rule / Solve`)** templates so decorative icons can never re-enter the codebase.
3. **Fleet-Wide Sync:** A single audited commit and sync updated every affected page cleanly with zero downtime and full Git rollback provenance.

---

## Accessible by Architecture, Not by Patchwork

Attempting to satisfy **ADA Title II** through manual browser edits drains faculty energy every semester. Engineering courses through **Curriculum-as-Code** protects the institution with timestamped Git provenance, gives faculty deterministic control over their curriculum, and guarantees every student—whether on a screen reader or a mobile phone in rural Yuma County—a fast, clear, born-accessible learning experience.

---

> **Disclaimer:** The Curriculum-as-Code architecture, S-A-R Standard, and open-source software tools described in this essay represent my independent faculty engineering and research through Webcognita LLC and do not represent official policy or endorsement by Arizona Western College or The University of Arizona.
