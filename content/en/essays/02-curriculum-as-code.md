---
title: "Curriculum-as-Code: Treating Educational Content Like Software Development"
description: "Why proprietary Learning Management Systems fail modern institutional compliance and how Git version control, plain-text Markdown, and automated CI/CD validation redefine instructional engineering."
essay_number: "02"
date: "2026-07-30"
author: "Alan Pruitt"
slug: "02-curriculum-as-code"
categories: ["curriculum-as-code"]
aliases:
  - "/essays/02/"
  - "/essays/essay-02/"
  - "/essays/essay02/"
---

## Curriculum-as-Code: Treating Educational Content Like Software Development

For decades, educators have been tethered to proprietary Learning Management Systems (LMS) that act as black boxes. These platforms lock valuable instructional assets into rigid databases, make version rollback nearly impossible, and break accessibility standards with every proprietary UI update.

It is time to borrow an established paradigm from software engineering: **Curriculum-as-Code (CaC)**. By treating educational materials as source code, we gain the rigorous verification, portability, and version control required for high-accessibility academic environments.

## The Single Source of Truth (SSoT)

In a CaC framework, every syllabus, lab specification, and assessment rubric is authored in plain-text Markdown. Markdown acts as our Single Source of Truth (SSoT).

> Plain text outlives software vendors. Content stored in Git repositories remains readable, fully portable, and independent of proprietary corporate platforms.

When course material lives in a Git repository rather than a locked LMS course shell, faculty collaboration shifts from tedious email attachments to clean pull requests, branch protection, and transparent peer review.

## Automated Validation and WCAG 2.2 AA Compliance

Software teams use continuous integration (CI/CD) pipelines to catch syntax errors, broken links, and performance bottlenecks before code ships to production. Educational pipelines should do the exact same thing.

* **Lighthouse & Accessibility Audits:** Every build is automatically tested against WCAG 2.2 AA contrast ratios and Lighthouse performance standards.
* **Automated Link Checking:** CI scripts crawl all internal and external references to eliminate 404 errors before students ever access a lab manual.
* **Bilingual Localization Sync:** Translation matrices are validated automatically to ensure English and Spanish text trees remain structurally aligned.

## Sovereignty Over Proprietary Vendor Lock-In

Institutions and independent educators must reclaim ownership of their instructional IP. By decoupling course delivery from corporate walled gardens, Curriculum-as-Code ensures that academic materials remain fast, secure, born-accessible, and entirely under sovereign control.

---

> **Disclaimer:** The Curriculum-as-Code architecture, S-A-R Standard, and open-source software tools described in this essay represent my independent faculty engineering and research through Webcognita LLC and do not represent official policy or endorsement by Arizona Western College or The University of Arizona.
