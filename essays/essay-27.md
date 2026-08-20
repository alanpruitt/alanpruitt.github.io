---
layout: post
title: "Essay 27"
permalink: /essay-27/
id: "27"
slug: "27-ada-title-ii-fleet-refactor"
title_es: "Título II de la ADA y la Reestructuración de la Flota"
date: "2026-08-20"
course: "EXW101"
term: "Fall 2026"
ssot: "The Einstein Protocol"
tags: ["AI", "CurriculumAsCode", "EdTech", "LMS", "Accessibility", "OpenSource", "ADA"]
summary: "A case study of the fleet-wide emoji stripping sweep, detailing the regex patterns and pre-commit hooks that catch spacing errors and ensure strict compliance."
summary_es: "Un caso de estudio de la limpieza de emojis en toda la flota, detallando los patrones de regex y los ganchos de pre-commit."
lang_default: "en"
canonical_url: "https://alanpruitt.com/articles/27-ada-title-ii-fleet-refactor.html"
---

## ADA Title II and the Fleet-Wide Refactor

Meeting the federal ADA Title II compliance deadlines requires absolute uniformity in structural content across learning management systems. When executing massive, fleet-wide content transformations—such as removing decorative emojis and non-standard unicode characters—automated scripts must be governed by strict syntax validation gates.

### 1. The Decorative Emojis Clean Sweep

Decorative characters and emoticons introduce screen reader friction, resulting in poor perceivability. Programmatic regex patterns are deployed recursively across Markdown and HTML course content to purge these symbols:

* **Emoji Ranges:** Scanning and matching standard Unicode emoji groups, transport icons, transport symbols, emoticons, and geometric flags.
* **Content Preservation:** Ensure actual alphanumeric characters and code block layouts are left intact.

### 2. Spacing Violations in Automated Substitution

Automated replacement pipelines are highly efficient but prone to introducing subtle syntax regressions:

* **Hash Spacing:** Stripping an emoji immediately following header hashes (e.g., `## 🎯 Learning Objectives`) leaves behind a duplicate space (`##  Learning Objectives`).
* **ATX Heading Rules:** Duplicate spacing after ATX header hashes violates standard Markdown rules (`MD019`), creating rendering conflicts for content parsing engines.

### 3. Pre-Commit Gates as Safe Release Pipelines

A key lesson from the fleet-wide sweep is the vital role of pre-commit validation hook check points:

* **Early Detection:** When automated scripts introduce double-space regressions, pre-commit lint gates programmatically reject the commit.
* **Auto-Correction Integration:** Developers must combine regex cleansers with automatic syntax formatters (`markdownlint --fix`) to reconcile spacing issues before pushing changes to remote tracking branches.
