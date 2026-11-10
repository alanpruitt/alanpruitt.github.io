---
layout: post
title: "Essay 26: Navigating Compliance Upstream – The Curriculum-as-Code POUR-Audit Framework"
permalink: /essay-26/
id: "26"
slug: "26-curriculum-as-code-pour-audit-framework"
translationKey: "essay-26"
title_es: "Ensayo 26: Navegando el Cumplimiento Aguas Arriba – El Marco de Auditoría POUR en Currículum como Código"
date: "2026-08-19"
publishDate: "2026-08-19"
draft: false
author: "Alan Pruitt"
course: "EXW101"
term: "Fall 2026"
ssot: "Active Verification Telemetry & Integrity Protocol"
tags:
  - "Curriculum-as-Code"
  - "ADA Title II"
  - "WCAG 2.2 AA"
  - "Accessibility"
  - "POUR"
description: "How I operationalize the W3C POUR accessibility principles (Perceivable, Operable, Understandable, Robust) as automated pre-commit and CI/CD verification checks inside a Curriculum-as-Code repository."
summary: "How I operationalize the W3C POUR accessibility principles (Perceivable, Operable, Understandable, Robust) as automated pre-commit and CI/CD verification checks inside a Curriculum-as-Code repository."
summary_es: "Cómo operacionalizo los cuatro principios de accesibilidad POUR (Perceptible, Operable, Comprensible y Robusto) mediante verificaciones automatizadas en Git y CI/CD."
lang_default: "en"
categories:
  - "ada-title-ii"
  - "Curriculum-as-Code"
aliases:
  - "/essays/essay-26/"
  - "/essays/26/"
  - "/essays/essay26/"
  - "/essays/navigating-compliance-upstream/"
substack_url: "https://alanpruitt.substack.com/p/navigating-compliance-upstream-the"
---

## Moving Accessibility Upstream Before Content Touches the LMS

When the U.S. Department of Justice codified technical digital accessibility standards under **ADA Title II** for public higher education institutions, it signaled the end of reactive, page-by-page patching inside Learning Management System (LMS) rich-text editors. Manually repairing broken heading structures, missing image `alt` descriptions, and low-contrast inline CSS across hundreds of course pages is an unsustainable administrative trap.

To achieve permanent, scalable conformance across my `EXW` course fleet, I moved accessibility validation upstream into a version-controlled software engineering workflow: **Curriculum-as-Code (CaC)**. By managing course modules in plain-text Markdown governed by automated Git pre-commit and CI/CD linters, I enforce my **POUR-Audit Framework** before a single line of HTML ever reaches Canvas LMS.

---

## Operationalizing the Four W3C POUR Pillars as Executable Code

### 1. Perceivable: Automated Asset & High-Contrast Verification

Digital equity requires every visual diagram, clinical table, and text callout to be unambiguously perceivable across viewports and assistive technologies:

* **Context-Specific `alt` Enforcement:** My repository scanners inspect every `<img>` and Markdown image reference, rejecting missing `alt` attributes, empty placeholders on informative charts, or raw filenames (such as `.png` or `.svg`), while enforcing concise `<= 120`-character clinical descriptions.
* **Universal High-Contrast Assurance (`9:1` Double-Contrast Guard):** Automated style checks verify explicit foreground and background hex pairs—such as Deep Navy (`#002147`) and Matador Red (`#940925`) on crisp `#FFFFFF`—exceeding **WCAG 2.2 Level AA** minimums across desktop and mobile displays.

### 2. Operable: Predictable Keyboard Navigation & Zero Focus Traps

Every interactive simulation, collapsible rubric, and external toolkit widget must remain 100% operable via keyboard navigation and switch devices:

* **Visible Focus Indicators & Touch Targets:** Automated audits verify visible `:focus-visible` rings, `44x44px` minimum mobile tap targets, and logical tab order across custom interactive components.
* **Screen-Reader Signal Clarity:** Stripping decorative Unicode emojis and non-semantic visual clutter eliminates disruptive audio noise for students navigating on mobile screen readers.

### 3. Understandable: Deterministic Structure & SSoT Terminology Hygiene

Cognitive predictability reduces extraneous load so students can focus on clinical reasoning rather than deciphering inconsistent page layouts:

* **Sequential Heading Nesting:** Continuous integration scripts enforce a strict `<h2>` -> `<h3>` -> `<h4>` outline (reserving `<h1>` strictly for the Canvas Page Title) so every module follows an identical structural rhythm.
* **Legacy Pattern & Terminology Deprecation:** My linters automatically flag deprecated module numbering patterns and legacy rubric terms, keeping every course aligned with current federal Single Sources of Truth (**PAGA 2018**, **2025–2030 DGA**, **ACSM 12th Ed.**, and **NASM OPT**) and plain-language **WCAG 3.0** scaffolding.

### 4. Robust: Standards-Compliant Semantic Landmarks

A robust curriculum compiles into clean, parser-safe HTML5 landmarks (`<table>` with descriptive `<caption>` and `<th scope="col">`, semantic `<ul>`/`<ol>` lists, and explicit `lang="es"` attributes on bilingual blocks) that current and future assistive technologies parse without ambiguity.

---

## The Sovereign Auditor Model

Under my **Curriculum-as-Code** architecture, accessibility conformance is no longer an exhausting end-of-semester audit event—it is a continuous, automated baseline enforced on every `git commit`. When federal guidelines or LMS accessibility rules evolve, updating a single linter rule and compiler pass refactors an entire multi-section course fleet in seconds rather than weeks.

* **Read the Substack Edition:** [Navigating Compliance Upstream: The Curriculum-as-Code POUR-Audit Framework (Substack)](https://alanpruitt.substack.com/p/navigating-compliance-upstream-the)

---

> **Disclaimer:** The Curriculum-as-Code architecture, S-A-R Standard, and open-source software tools described in this essay represent my independent faculty engineering and research through Webcognita LLC and do not represent official policy or endorsement by Arizona Western College or The University of Arizona.
