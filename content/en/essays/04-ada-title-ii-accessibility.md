---
title: "Architecting Born-Accessible Higher Ed: ADA Title II & Curriculum-as-Code"
description: "Under Title II of the ADA and Section 508 of the Rehabilitation Act, digital accessibility is a strict legal mandate for every content author. Here is how Curriculum-as-Code paradigms replace reactive remediation with automated compliance."
essay_number: "04"
date: "2026-07-30"
author: "Alan Pruitt"
slug: "04-ada-title-ii-accessibility"
categories: ["ada-title-ii"]
aliases:
  - "/essays/04/"
  - "/essays/essay-04/"
  - "/essays/essay04/"
---

## Architecting Born-Accessible Higher Ed: ADA Title II & Curriculum-as-Code

Under Title II of the Americans with Disabilities Act (ADA) and Section 508 of the Rehabilitation Act, public colleges and universities are legally bound to ensure that all digital content—from course syllabi to web applications—is fully accessible. Accessibility is no longer an optional task delegated to disability support offices; it is the immediate responsibility of every faculty member, instructional designer, and content creator across the institution.

However, the traditional higher education approach to compliance relies heavily on *reactive remediation*: scanning unstructured PDFs, manually adding alt text to WYSIWYG editors, or re-formatting course shells right before a semester begins. This approach fails at scale. To achieve true compliance, higher education must move to a **born-accessible** engineering model powered by **Curriculum-as-Code (CaC)**.

## The Failure of Reactive PDF and LMS Workflows

For decades, the standard method for distributing course materials has involved converting desktop documents to PDFs or typing content into closed Learning Management System (LMS) rich-text containers.

* **PDF Inaccessibility:** Exported PDFs frequently drop logical reading order, strip out proper heading tags (`H1`-`H3`), and generate unlabelled form fields, making them unusable for screen reader users.
* **WYSIWYG Fragmentation:** Rich-text LMS editors permit inconsistent heading hierarchies, arbitrary color choices that fail WCAG contrast ratios, and inline layout hacks that break responsive reflow.

> Retrofitting accessibility onto proprietary binary files or fragmented rich-text editors is expensive and prone to failure. True compliance requires generating accessible outputs automatically from a clean source.

## How Curriculum-as-Code Enforces WCAG 2.1 AA Standards

Curriculum-as-Code decouples instructional content from display formatting by maintaining all educational assets in plain-text Markdown single sources of truth (SSoT). Plain-text Markdown enforces semantic structure by default:

* **Semantic Structure Enforcement:** Markdown inherently requires strict document hierarchy (`#`, `##`, `###`), forcing authors to build proper heading trees that screen readers rely on for navigation.
* **Automated Alt-Text Auditing:** CI/CD build pipelines analyze image references in real time. If an author attempts to merge a lab manual without specifying meaningful image alt text, the build fails automatically.
* **Born-Accessible HTML Output:** During automated compilation, the Markdown SSoT compiles into clean, semantic HTML5 containing proper ARIA landmarks, WCAG 2.1 AA compliant color contrast ratios, and responsive text reflow without horizontal scrolling.

## Institutional Scale and Continuous Audit Trails

When instructional content is managed as source code in Git repositories, compliance officers and department chairs gain something previously impossible in traditional LMS environments: **continuous, automated audit trails**.

Every revision to a course syllabus or lab guide generates a version-controlled commit. Automated linting scripts audit the entire institutional curriculum for accessibility compliance continuously on every push. By shifting from manual retroactive checks to automated Curriculum-as-Code pipelines, institutions eliminate legal exposure under ADA Title II while guaranteeing equal access for all learners.

---

> **Disclaimer:** The Curriculum-as-Code architecture, S-A-R Standard, and open-source software tools described in this essay represent my independent faculty engineering and research through Webcognita LLC and do not represent official policy or endorsement by Arizona Western College or The University of Arizona.
