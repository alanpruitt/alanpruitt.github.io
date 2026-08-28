---
title: "Curriculum-as-Code, ADA Title II Compliance, and Fleet-Wide Accessibility Refactoring"
date: 2026-08-25T16:53:00-07:00
draft: false
tags: ["Accessibility", "Instructional Design", "Curriculum-as-Code", "Higher Ed", "ADA Title II"]
categories: ["Essays"]
description: "How engineering course architectures in plain Markdown with automated CI/CD linters solves ADA Title II compliance and enables fleet-wide accessibility refactoring."
---

When the Department of Justice codified WCAG 2.1 AA standards under ADA Title II for public higher education institutions, it ended the era of reactive, page-by-page accessibility audits. Traditional post-publication fixes inside LMS rich text editors fail to scale across multi-section course fleets.

Achieving sustainable compliance requires moving accessibility upstream into a version-controlled engineering workflow: **Curriculum-as-Code**.

---

## The Upstream Accessibility Pipeline

By authoring instructional materials in standardized Markdown and validating them through automated linting pipelines before deployment, entire categories of accessibility errors are eliminated at the source.

* **Deterministic Heading Hierarchies:** Linters enforce strict semantic nesting (starting at `<h2>` and proceeding sequentially to `<h3>` and `<h4>`) to ensure screen reader navigation remains logical.
* **Assistive Tech Optimization:** Stripping non-semantic emojis and decorative artifacts removes cognitive friction for screen reader users.
* **Universal Contrast Assurance:** Standardized CSS templates guarantee WCAG 2.1 AA compliance (minimum 4.5:1 text contrast) across mobile and desktop viewports.

---

## Fleet-Wide Refactoring

The definitive advantage of Curriculum-as-Code is agility during fleet-wide refactoring. When institutional standards, federal guidelines, or accessibility rules change, automated scripts audit and update entire course catalogs in seconds rather than requiring manual edits across hundreds of individual LMS pages.

Treating course architecture as software infrastructure turns accessibility from an administrative bottleneck into a permanent, automated baseline.
