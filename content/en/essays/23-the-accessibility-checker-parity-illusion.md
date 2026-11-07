---
title: "The Accessibility Checker Parity Illusion: Schema Divergence & Curriculum-as-Code"
description: "Why Canvas LMS, Microsoft Office, and Adobe PDF accessibility checkers lack structural parity, and why Markdown Curriculum-as-Code is the only deterministic path to WCAG 2.2 AA."
essay_number: "23"
date: "2026-08-19"
author: "Alan Pruitt"
slug: "23-the-accessibility-checker-parity-illusion"
categories: ["ada-title-ii"]
aliases:
  - "/essays/23/"
  - "/essays/essay-23/"
  - "/essays/essay23/"
  - "/essays/23-accessibility-checker-parity-illusion/"
---

## Executive Summary

Automated accessibility checkers in Canvas LMS, Microsoft Office 365, and Adobe Acrobat Pro operate on fundamentally incompatible, proprietary schema architectures. A document certified "accessible" in one system routinely introduces severe structural barriers in another.

To achieve verifiable compliance under ADA Title II and WCAG 2.2 Level AA, higher education institutions must discard multi-tier export pipelines in favor of **Curriculum-as-Code (CaC)**: authoring in semantic, mobile-first Markdown as the Single Source of Truth (SSoT) and compiling deterministically to pristine HTML5.

## 1. The Tri-Engine Illusion: The False Sense of Parity

Higher education instructional workflows often assume that clicking "Check Accessibility" in Microsoft Word, running the Canvas Rich Content Editor (RCE) checker, and executing the Adobe Acrobat Pro Action Wizard are interchangeable checkpoints.

They are not. These engines do not share a common schema, validation logic, or Document Object Model (DOM). When faculty author in Microsoft Word and export to PDF or copy-paste into Canvas, they inherit a cascade of silent structural failures.

## 2. Architectural Comparison of Accessibility Engines

## 3. The Multi-Step Export Translation Debt

The legacy instructional workflow— *Word → PDF → Canvas* —introduces compounding structural degradation at each transformation boundary:

* **Heading Flattening:** Exporting from OpenXML to PDF or pasting into the Canvas RCE often converts semantic subheadings (<h3>, <h4>) into unanchored bold styling (<strong> or /Span).
* **List Fragmentation:** Nested lists lose parent-child relationship tokens, preventing screen readers from calculating total list length or hierarchy depth.
* **Table Scope Destruction:** Export filters strip `scope="col"` and `scope="row"` attributes, leaving screen readers unable to announce contextual coordinates to non-sighted students.
* **Reflow & Mobile Disruption:** PDF documents lock content into fixed-coordinate visual boxes, forcing mobile learners into continuous horizontal scrolling.

## 4. Regulatory Benchmarks: WCAG 2.2 AA & ADA Title II

Under the Department of Justice ADA Title II digital accessibility mandate, public institutions must ensure all digital course content strictly adheres to WCAG Level AA criteria:

* **WCAG 1.3.1 (Info and Relationships):** Semantic structures must be programmatically determinable, not merely visually implied.
* **WCAG 2.4.6 (Headings and Labels):** Headings must describe topic or purpose and maintain an unbroken hierarchy starting at <h2>.
* **WCAG 2.4.11 (Focus Appearance):** Interactive elements must retain high-contrast, discernible focus states.
* **WCAG 2.5.8 (Target Size - Minimum):** Touch targets must maintain adequate spacing on mobile viewports.

## 5. Curriculum-as-Code: Deterministic Accessibility

Curriculum-as-Code eliminates document translation debt by utilizing Markdown as the immutable Single Source of Truth (SSoT):

* **Deterministic Compilation:** Plain text compiles directly into standardized HTML5 elements (<h2>, <h3>, <p>, <table>, <ul>), preventing proprietary WYSIWYG tag bloat.
* **Automated Gating:** Master repositories run local linters (markdownlint, axe-core) before deployment to block non-compliant syntax.
* **OER & Device Equity:** Plain-text Markdown generates lightweight, zero-cost, screen-reader-optimized instructional files that load instantly across all devices.

## Concluding Synthesis

Automated GUI checkers act as superficial linters for visual styles, but they cannot engineer structural accessibility. Achieving authentic accessibility and federal compliance requires structural rigor at the source. Adopting Markdown and Curriculum-as-Code replaces subjective checker validation with deterministic, accessible, and future-proof course architecture.

---

> **Disclaimer:** The Curriculum-as-Code architecture, S-A-R Standard, and open-source software tools described in this essay represent my independent faculty engineering and research through Webcognita LLC and do not represent official policy or endorsement by Arizona Western College or The University of Arizona.
