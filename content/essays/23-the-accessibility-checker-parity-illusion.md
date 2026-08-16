---
id: "23"
slug: "23-the-accessibility-checker-parity-illusion"
title: "The Accessibility Checker Parity Illusion and the Curriculum-as-Code Imperative"
date: "2026-08-21"
course: "EXW101"
term: "Fall 2026"
ssot: "ADA Title II / WCAG 2.2 Level AA"
tags: ["Accessibility", "WCAG", "CurriculumAsCode", "ADATitleII", "Compliance", "OER"]
summary: "How proprietary accessibility checkers in Canvas LMS, Microsoft Office, and Adobe Acrobat introduce silent structural compliance failures, and why Curriculum-as-Code resolves accessibility translation debt at the source."
---

## The Accessibility Checker Parity Illusion and the Curriculum-as-Code Imperative

### Executive Summary

Automated accessibility checkers in Canvas LMS, Microsoft Office 365, and Adobe Acrobat Pro operate on fundamentally incompatible, proprietary schema architectures. A document certified "accessible" in one system routinely introduces severe structural barriers in another.

To achieve verifiable compliance under ADA Title II and WCAG 2.2 Level AA, higher education institutions must discard multi-tier export pipelines in favor of **Curriculum-as-Code (CaC)**: authoring in semantic, mobile-first Markdown as the Single Source of Truth (SSoT) and compiling deterministically to pristine HTML5.

### 1. The Tri-Engine Illusion: The False Sense of Parity

Higher education instructional workflows often assume that clicking "Check Accessibility" in Microsoft Word, running the Canvas Rich Content Editor (RCE) checker, and executing the Adobe Acrobat Pro Action Wizard are interchangeable checkpoints.

They are not. These engines do not share a common schema, validation logic, or Document Object Model (DOM).

When faculty author in Microsoft Word and export to PDF or copy-paste into Canvas, they inherit a cascade of silent structural failures. This checker-parity illusion creates institutional compliance risks under Title II of the Americans with Disabilities Act and presents students who rely on assistive technologies with broken reading orders, fragmented lists, and unassociated table cells.

### 2. Architectural Comparison of Accessibility Engines

The failure of automated checkers originates in the structural divergence of their underlying schemas:

| System & Engine | Schema Architecture | Heading Hierarchy Handling | Table Structure Support | Mobile & Viewport Reflow |
| :--- | :--- | :--- | :--- | :--- |
| **Canvas RCE Checker** | HTML5 Web DOM via TinyMCE | Audits sequential tags; often fails to enforce `<h2>` root under page title | Checks basic `<th>` presence; lacks complex scope validation | Fluid and responsive if HTML remains clean |
| **Microsoft Office Checker** | OpenXML Schema (`.docx`, `.pptx`) | Audits visual Word styles; decouples from export tag mappings | Validates "Header Row" flag; loses explicit cell mapping on export | Responsive within Office applications only |
| **Adobe Acrobat Pro** | PostScript Stream + `/StructTreeRoot` Tag Tree | Audits structural tags (`/H1`–`/H6`); requires manual tree remediation | Requires manual tagging for `/Table`, `/TR`, `/TH`, `/TD`, and span attributes | Rigid print layout; fails mobile reflow without complex tagging |

### 3. The Multi-Step Export Translation Debt

The legacy instructional workflow—$Word \rightarrow PDF \rightarrow Canvas$—introduces compounding structural degradation at each transformation boundary:

1. **Heading Flattening:** Exporting from OpenXML to PDF or pasting into the Canvas RCE often converts semantic subheadings (`<h3>`, `<h4>`) into unanchored bold styling (`<strong>` or `/Span`).
2. **List Fragmentation:** Nested lists lose parent-child relationship tokens, preventing screen readers from calculating total list length or hierarchy depth.
3. **Table Scope Destruction:** Export filters strip `scope="col"` and `scope="row"` attributes, leaving screen readers unable to announce contextual coordinates to non-sighted students.
4. **Reflow & Mobile Disruption:** PDF documents lock content into fixed-coordinate visual boxes, forcing mobile learners into continuous horizontal scrolling.

### 4. Regulatory Benchmarks: WCAG 2.2 AA & ADA Title II

Under the Department of Justice ADA Title II digital accessibility mandate, public institutions must ensure all digital course content strictly adheres to WCAG Level AA criteria:

* **WCAG 1.3.1 (Info and Relationships):** Semantic structures must be programmatically determinable, not merely visually implied.
* **WCAG 2.4.6 (Headings and Labels):** Headings must describe topic or purpose and maintain an unbroken hierarchy starting at `<h2>`.
* **WCAG 2.4.11 (Focus Appearance):** Interactive elements must retain high-contrast, discernible focus states.
* **WCAG 2.5.8 (Target Size - Minimum):** Touch targets must maintain adequate spacing on mobile viewports.

### 5. Curriculum-as-Code: Deterministic Accessibility

Curriculum-as-Code eliminates document translation debt by utilizing Markdown as the immutable Single Source of Truth (SSoT).

* **Deterministic Compilation:** Plain text compiles directly into standardized HTML5 elements (`<h2>`, `<h3>`, `<p>`, `<table>`, `<ul>`), preventing proprietary WYSIWYG tag bloat.
* **Automated CI/CD Verification:** Master repositories run automated linters (`markdownlint`, `axe-core`) on every commit to block non-compliant syntax before deployment.
* **OER & Device Equity:** Plain-text Markdown generates lightweight, zero-cost, screen-reader-optimized instructional files that load instantly across all devices and bandwidth levels.

### Concluding Synthesis

Automated GUI checkers act as superficial linters for visual styles, but they cannot engineer structural accessibility. Achieving authentic accessibility and federal compliance requires structural rigor at the source. Adopting Markdown and Curriculum-as-Code replaces subjective checker validation with deterministic, accessible, and future-proof course architecture.

### Academic Citation & Attribution

```bibtex
@article{pruitt2026accessibilitycheckerparity,
  author    = {Alan Pruitt},
  title     = {The Accessibility Checker Parity Illusion and the Curriculum-as-Code Imperative},
  journal   = {Curriculum-as-Code Publication Series},
  year      = {2026},
  month     = {aug},
  number    = {23},
  url       = {https://alanpruitt.com/articles/23-the-accessibility-checker-parity-illusion.html},
  publisher = {Webcognita LLC}
}
```
