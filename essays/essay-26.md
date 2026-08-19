---
layout: post
title: "Essay 26"
permalink: /essay-26/
id: "26"
slug: "26-curriculum-as-code-pour-audit-framework"
title_es: "Currículum como Código y el Marco de Auditoría POUR"
date: "2026-08-19"
course: "EXW101"
term: "Fall 2026"
ssot: "The Einstein Protocol"
tags: ["AI", "CurriculumAsCode", "EdTech", "LMS", "Accessibility", "OpenSource", "POUR"]
summary: "An analysis of the POUR-Audit framework within Curriculum-as-Code paradigms, highlighting automated verification checks for heading hierarchies, image alt-text, and legacy reference deprecation."
summary_es: "Un análisis del marco de auditoría POUR dentro de los paradigmas de Currículum como Código, destacando la verificación automatizada de accesibilidad."
lang_default: "en"
canonical_url: "https://alanpruitt.com/articles/26-curriculum-as-code-pour-audit-framework.html"
---

## The POUR-Audit Framework in Curriculum-as-Code

Treating educational content as software—known as *Curriculum-as-Code* (CaC)—enables the integration of automated verification pipelines to enforce instructional quality, semantic hierarchy, and digital accessibility. The **POUR-Audit framework** operationalizes Web Content Accessibility Guidelines (WCAG) into testable, programmatically audited standards directly inside git workflows.

### 1. Robust: Semantic Structure and Hierarchy

A robust curriculum is built on standard HTML5 landmarks that assistive technologies can parse reliably. The audit checks heading structures to confirm strict semantic progression:

* **Entry Constraints:** The content body must start with a `##` (H2) heading level. H1 is reserved exclusively for the Canvas LMS Page Title.
* **Structural Parity:** Audits scan header trees programmatically, ensuring no skipped heading levels (e.g. from H2 to H4) exist, which disorients screen readers.

### 2. Perceivable: Asset Alt-Text Enforcement

Digital equity requires that all instructional media is perceivable. Programmatic scans analyze `<img ...>` tags in the course fleet:

* **Descriptive Text:** Every image tag must contain a descriptive `alt` attribute.
* **Prohibited Placeholders:** Empty placeholders (`alt=""` or `alt=''`) are flagged as failures to prevent decorative bypass of active educational charts.

### 3. Understandable: Legacy Term Deprecation

To maintain clear and accurate instructional pathways, the audit monitors prohibited legacy terms and references:

* **Legacy Patterns:** References containing deprecated structural patterns (such as `"8.#"`-style module references) are checked and flagged.
* **Unified Terminology:** Ensures course fleet documentation aligns with current academic sources of truth (SSoT).
