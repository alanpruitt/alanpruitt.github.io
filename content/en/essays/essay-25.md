---
title: "Essay 25: The Accessibility Checker Parity Illusion: Schema Divergence & CaC"
date: 2026-08-27T08:00:00-07:00
publishDate: 2026-08-27T08:00:00-07:00
draft: false
slug: "essay-25"
description: "Why proprietary LMS accessibility checkers create false confidence, how schema divergence masks non-compliance, and how Curriculum-as-Code restores audit parity."
categories: ["Curriculum-as-Code", "Accessibility", "Higher Education Governance", "ADA Title II"]
layout: "single"
---

## The Illusion of the Green Checkmark

In modern higher education IT, institutions invest heavily in automated Learning Management System (LMS) accessibility checkers. These tools present faculty and administrators with simplified dashboards, color-coded dials, and green checkmarks indicating high compliance scores.

This is the **Accessibility Checker Parity Illusion**.

A passing score on a native LMS scanner frequently masks fundamental non-conformance with **WCAG 2.2 Level AA** and federal **ADA Title II (28 CFR Part 35)** mandates. The failure stems not from malicious intent, but from **schema divergence**—the structural gap between the underlying DOM rendered by the browser and the limited AST parsed by the LMS plugin.

---

## The Mechanics of Schema Divergence

The failure of automated checkers originates in the structural divergence of their underlying schemas:

| System & Engine | Schema Architecture | Heading Hierarchy Handling | Table Structure Support | Mobile & Viewport Reflow |
| :--- | :--- | :--- | :--- | :--- |
| **Canvas RCE Checker** | HTML5 Web DOM via TinyMCE | Audits sequential tags; often fails to enforce `<h2>` root under page title | Checks basic `<th>` presence; lacks complex scope validation | Fluid and responsive if HTML remains clean |
| **Microsoft Office Checker** | OpenXML Schema (`.docx`, `.pptx`) | Audits visual Word styles; decouples from export tag mappings | Validates "Header Row" flag; loses explicit cell mapping on export | Responsive within Office applications only |
| **Adobe Acrobat Pro** | PostScript Stream + `/StructTreeRoot` Tag Tree | Audits structural tags (`/H1`–`/H6`); requires manual tree remediation | Requires manual tagging for `/Table`, `/TR`, `/TH`, `/TD`, and span attributes | Rigid print layout; fails mobile reflow without complex tagging |

---

## The Multi-Step Export Translation Debt

The legacy instructional workflow—*Word &rarr; PDF &rarr; Canvas*—introduces compounding structural degradation at each transformation boundary:

1. **Heading Flattening:** Exporting from OpenXML to PDF or pasting into the Canvas RCE often converts semantic subheadings (`<h3>`, `<h4>`) into unanchored bold styling (`<strong>` or `/Span`).
2. **List Fragmentation:** Nested lists lose parent-child relationship tokens, preventing screen readers from calculating total list length or hierarchy depth.
3. **Table Scope Destruction:** Export filters strip `scope="col"` and `scope="row"` attributes, leaving screen readers unable to announce contextual coordinates to non-sighted students.
4. **Reflow & Mobile Disruption:** PDF documents lock content into fixed-coordinate visual boxes, forcing mobile learners into continuous horizontal scrolling.

---

## Regulatory Benchmarks: WCAG 2.2 AA & ADA Title II

Under the Department of Justice ADA Title II digital accessibility mandate, public institutions must ensure all digital course content strictly adheres to WCAG Level AA criteria:

* **WCAG 1.3.1 (Info and Relationships):** Semantic structures must be programmatically determinable, not merely visually implied.
* **WCAG 2.4.6 (Headings and Labels):** Headings must describe topic or purpose and maintain an unbroken hierarchy starting at `<h2>`.
* **WCAG 2.4.11 (Focus Appearance):** Interactive elements must retain high-contrast, discernible focus states.
* **WCAG 2.5.8 (Target Size - Minimum):** Touch targets must maintain adequate spacing on mobile viewports.

---

## Curriculum-as-Code: Deterministic Accessibility

Curriculum-as-Code eliminates document translation debt by utilizing Markdown as the immutable Single Source of Truth (SSoT).

* **Deterministic Compilation:** Plain text compiles directly into standardized HTML5 elements (`<h2>`, `<h3>`, `<p>`, `<table>`, `<ul>`), preventing proprietary WYSIWYG tag bloat.
* **Automated CI/CD Verification:** Master repositories run automated linters (`markdownlint`, `axe-core`) on every commit to block non-compliant syntax before deployment.
* **OER & Device Equity:** Plain-text Markdown generates lightweight, zero-cost, screen-reader-optimized instructional files that load instantly across all devices and bandwidth levels.

---

## Concluding Synthesis

Automated GUI checkers act as superficial linters for visual styles, but they cannot engineer structural accessibility. Achieving authentic accessibility and federal compliance requires structural rigor at the source. Adopting Markdown and Curriculum-as-Code replaces subjective checker validation with deterministic, accessible, and future-proof course architecture.
