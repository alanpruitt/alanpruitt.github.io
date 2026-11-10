---
title: "Essay 32: From Retrofit to Architecture – Operationalizing ADA Title II Compliance Before the Deadline"
slug: "essay-32-from-retrofit-to-architecture"
date: 2026-09-10T12:00:00-07:00
publishDate: 2026-09-10T12:00:00-07:00
draft: false
author: "Alan Pruitt"
categories:
  - "Curriculum-as-Code"
  - "ADA Title II"
  - "Accessibility"
tags:
  - "ADA Title II"
  - "WCAG 2.2 AA"
  - "9:1 Double-Contrast Guard"
  - "Continuous Integration"
  - "S-A-R Standard"
description: "Why treating ADA Title II digital accessibility as a post-production LMS retrofit fails at scale, and how my Curriculum-as-Code CI/CD pipeline bakes WCAG 2.2 AA compliance directly into the source repository."
summary: "Why treating ADA Title II digital accessibility as a post-production LMS retrofit fails at scale, and how my Curriculum-as-Code CI/CD pipeline bakes WCAG 2.2 AA compliance directly into the source repository."
aliases:
  - "/essays/32/"
  - "/essays/essay-32/"
  - "/essays/essay32/"
  - "/essays/from-retrofit-to-architecture/"
substack_url: "https://alanpruitt.substack.com/p/from-retrofit-to-architecture-operationalizing"
---

## Moving Beyond the Post-Production Scramble

For decades, higher education has treated digital accessibility as an afterthought—a frantic, post-production scramble executed weeks before a semester launch to inject missing `alt` attributes, repair skipped heading tags, and patch low-contrast inline styles inside LMS rich-text editors. Under the federal enforcement timelines of **ADA Title II (`28 CFR Part 35`)**, that reactive model is no longer merely inefficient; it is a structural institutional liability.

When I treat compliance as an upstream architectural invariant rather than a downstream cosmetic retrofit, courses stop breaking between semesters, faculty burnout drops, and students using assistive technologies gain predictable, barrier-free access from day one.

---

## The Fallacy of the Downstream Retrofit

Relying on end-of-semester manual course audits creates a fragile instructional ecosystem. Whenever content is authored directly inside proprietary word processors or WYSIWYG LMS text boxes without deterministic guardrails, every routine edit introduces a fresh regression risk:

> *"Trying to fix accessibility at the end of a content lifecycle is like trying to install seatbelts after a crash test. True safety must be baked into the chassis."*

In my audits of legacy LMS workflows, three recurring failure modes dominate retroactive remediation:

* **Inconsistent Color Contrast:** Visual rich-text editors routinely emit non-compliant hex pairings or omit explicit `background-color` declarations, failing **WCAG 2.2 Level AA** contrast minimums (and falling far short of my **`9:1` Double-Contrast Guard**).
* **Skipped Heading Hierarchies:** Jumping visually from `<h2>` directly to `<h4>` breaks the document outline that screen reader users rely on to navigate clinical instructions.
* **Orphaned Media & Unscoped Tables:** Uncaptioned media assets and layout tables lacking `<caption>` and `<th scope="col">` declarations create recurring deployment bottlenecks right before classes open.

---

## Upstream Conformance: Baking Standards into Code

The foundational premise of my **Curriculum-as-Code (CaC)** architecture is that instructional content is software. By maintaining master course modules in plain-text Markdown under Git version control, I enforce strict typographic, structural, and clinical constraints at the source:

* **High-Contrast Brand Tokens (`9:1` Double-Contrast Guard):** Instead of relying on memory when styling callouts, my compiler pairs explicit foreground and background hex values—such as Deep Navy (`#002147`) or Matador Red (`#940925`) against crisp `#FFFFFF`—guaranteeing **9:1+** contrast ratios and `0 Open Issues` in the Canvas Course Accessibility Checker.
* **Deterministic Semantic Headings:** Every module body starts strictly at `<h2>` (reserving `<h1>` exclusively for the Canvas Page Title) and nests sequentially (`<h2>` -> `<h3>` -> `<h4>`) with heading lengths capped at `<= 120` characters.
* **Delimiter-Isolated Clinical Case Data:** Wrapping clinical case inputs inside triple-hash (`###`) delimiter blocks keeps patient scenarios cleanly separated from instructional prose for both screen readers and student prompt engineering:

```text
###
Clinical Case Input: Client presents with Stage 2 hypertension and progressive exertional fatigue in Yuma afternoon heat.
Compliance Audit: Verify exercise prescription and safety stop-gates strictly against PAGA 2018 (2nd Ed.) benchmarks.
###
```

---

## The Automated Safety Net: Continuous Integration Linting

Manual checklists inevitably lose to human fatigue during busy academic terms. By wiring automated accessibility linters directly into my Git pre-commit hooks and GitHub Actions CI/CD workflows, I turned my publishing pipeline into a self-auditing gatekeeper:

1. **Pre-Commit Structural & Contrast Scanning:** Before any Markdown module compiles into Canvas RCE HTML, automated Python linters verify image `alt` descriptions, table `<caption>` and `scope` attributes, list semantics, decorative-emoji removal, and `9:1` hex contrast pairings.
2. **Zero-Regression Builds:** Any commit that introduces a skipped heading level or contrast violation fails the build locally before it can ever reach a live student shell.
3. **Sovereign Human Verification:** Rather than outsourcing judgment to black-box cloud detectors, I pair deterministic linters with human clinical verification anchored in federal Single Sources of Truth such as the **Physical Activity Guidelines for Americans (2nd Ed., 2018)**.

---

## Engineering for Longevity

**ADA Title II** conformance is fundamentally an systems-engineering challenge, not a one-time paperwork exercise. By treating curriculum as version-controlled code, enforcing automated CI gates, and designing born-accessible templates upstream, I eliminate the panic of the retrofit cycle and deliver equitable, `$0 ZTC` learning environments that scale cleanly across semesters.

* **Read the Substack Edition:** [From Retrofit to Architecture: Operationalizing ADA Title II Compliance (Substack)](https://alanpruitt.substack.com/p/from-retrofit-to-architecture-operationalizing)
* **Explore My Live Compliance Architecture:** [alanpruitt.com/institutional-infrastructure/](https://alanpruitt.com/institutional-infrastructure/)

---

> **Disclaimer:** The Curriculum-as-Code architecture, S-A-R Standard, and open-source software tools described in this essay represent my independent faculty engineering and research through Webcognita LLC and do not represent official policy or endorsement by Arizona Western College or The University of Arizona.
