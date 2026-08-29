---
title: "Accessibility Conformance Statement"
date: 2026-08-28T19:40:00-07:00
description: "Formal accessibility statement, WCAG 2.2 Level AA conformance status, and feedback mechanism for alanpruitt.com."
layout: "single"
---

## Commitment to Digital Accessibility

Alan Pruitt is dedicated to ensuring digital accessibility for all users, including individuals with disabilities. We continuously audit and refactor this platform to conform with **WCAG 2.2 Level AA** standards and the federal **Americans with Disabilities Act (ADA) Title II Final Rule (28 CFR Part 35)**.

---

### Conformance Status

* **Standard:** Web Content Accessibility Guidelines (WCAG) 2.2 Level AA.
* **Current Status:** Fully Conforming. All primary user journeys, long-form essays, interactive calculators, and media assets meet or exceed Level AA requirements.
* **Continuous Integration Testing:** Our platform utilizes an automated testing pipeline incorporating **Axe-core** and **Playwright** headless browser test runners to prevent regressions prior to deployment.

---

### Architectural Accessibility Measures

* **Semantic HTML Hierarchy:** Section templates strictly reserve `<h1>` for page-level titles and cascade down starting at `<h2>` with zero skipped levels.
* **High-Contrast Typography:** Text elements meet a minimum 4.5:1 contrast ratio for normal text and 3:1 for large text across light and dark modes.
* **Interactive Controls:** All buttons, filters, and links maintain minimum $44 \times 44\text{px}$ touch targets with visible `:focus-visible` outlines for non-mouse and screen reader navigation.
* **Non-Text Content Alternatives:** High-density visual diagrams (including the Curriculum-as-Code architecture infographic) are paired with semantic DOM text transcripts.
* **Screen Reader Announcers:** Dynamic calculation tools implement debounced `aria-live="polite"` status regions to announce recalculations without stealing focus.

---

### Institutional Independence Notice

The accessibility frameworks, audits, and essays on this site reflect independent research and engineering by Alan Pruitt. They do not constitute official legal advice or formal representations of Arizona Western College or The University of Arizona.

---

### Feedback & Barrier Reporting

We welcome feedback on the accessibility of this platform. If you encounter any digital barrier, please contact us with the URL and a brief description:

**Alan Pruitt**  
Email: `alan.pruitt@gmail.com`  
Subject: `Accessibility Feedback - alanpruitt.com`
