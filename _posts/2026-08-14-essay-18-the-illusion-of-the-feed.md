---
title: "Essay 18: The Illusion of the Feed: Upstream SSoT and Feed Link Rot Governance"
date: 2026-08-14
author: "Coach Alan"
category: "Instructional Design & AI Architecture"
tags:
  - Curriculum-as-Code
  - Link Rot
  - Web Standards
  - CI/CD
  - Canvas LMS
---

> **TL;DR:** Relying on live external web links and dynamic social media widgets inside an LMS creates an illusion of real-time engagement while introducing a compounding vulnerability of link rot. Upstream Single Source of Truth (SSoT) governance resolves this at the source by managing links, references, and credentials as config-controlled variables in centralized manifests, which are validated by automated link-auditing pipelines.

---

## The Illusion of the Feed

In contemporary web-based education, courses often incorporate dynamic components such as real-time social media widgets, live discussion feeds, and external resource embeds. These widgets create the "illusion of the feed"—the impression that course content is current, interactive, and continuously updated.

However, this reliance on live-state web resources introduces a major system vulnerability: **Link Rot**. Research shows that a substantial percentage of external hyperlinks in web pages rot within a few years due to URL restructurings, server decommissions, and platform access updates. In an LMS environment, link rot degrades instructional quality, interrupts student learning flows, and compromises accessibility standards.

---

## Upstream SSoT Governance

Curriculum-as-Code (C-a-C) resolves the issue of link rot by establishing an upstream Single Source of Truth (SSoT) for all external resources. Instead of allowing instructors to hardcode URLs directly into individual pages or assignments, URLs are stored in central configurations:

```json
{
  "external_resources": {
    "paga_2018_guidelines": "https://health.gov/sites/default/files/2019-09/Physical_Activity_Guidelines_2nd_edition.pdf",
    "acsm_testing_standards": "https://www.acsm.org/education-resources/guidelines-exercise-testing-prescription",
    "yuma_heat_safety_protocol": "https://www.yumaaz.gov/government/emergency-management/heat-safety"
  }
}
```

By separating content from configuration, instructional engineers can audit and update link destinations globally. If a government website restructures its URL path, the fix is made once in the configuration file, and the CI/CD compilation pipeline automatically regenerates and deploys the updated references to the Canvas LMS.

---

## The Centaur Protocol & High-Friction Pedagogy

In alignment with the **Centaur Protocol**, course designs should position the student as the **Pilot/Architect** (exhibiting critical clinical judgment) and the AI as the **Engine/Calculator** (processing computations and drafting templates).

To prevent cognitive offloading, we implement **High-Friction Pedagogy**:
* **High-Friction Assessments:** Rather than completing passive, one-and-done multiple-choice tests, residents must perform active clinical audits.
* **Offline-First Resilience:** In regional institutions like Arizona Western College (AWC), a Hispanic-Serving Institution (HSI), students often study in high-heat environments (e.g., Yuma County desert glare exceeding $115^\circ\text{F}$) where mobile connectivity drops.
* **Semantic Security:** Instructors wrap clinical case data, client profiles, and medical inputs in triple-hashes (`###`). This keeps parsing errors from leaking information into public AI models.

---

## CI/CD Link Rot Audits

Our automated validation pipeline includes pre-commit link checkers that audit the integrity of the SSoT file before code is staged. This ensures that:
1. All referenced URLs return `HTTP 200 OK`.
2. Anchor tags contain descriptive labels matching WCAG 2.1 AA screen reader standards.
3. Every external link opens in a new tab with proper security parameters (`rel="noopener noreferrer"`).

This programmatic approach ensures that the course remains functional, secure, and accessible throughout the academic year.
