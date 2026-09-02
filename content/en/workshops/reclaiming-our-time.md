---
title: "Reclaiming Our Time: Secure and Practical GenAI Workflows for Faculty and Staff"
description: "Interactive professional development workshop covering GenAI governance, FERPA compliance, administrative relief workflows, and SSoT syllabus auditing."
date: 2026-08-15
type: "workshop"
deck_url: "/decks/reclaiming-our-time/"
video_url: "/videos/reclaiming-our-time.mp4"
institutional_alignment_url: "/governance/institutional-alignment/"
contact: "Alan Pruitt"
aliases:
  - /workshops/reclaiming-our-time/
---

## Reclaiming Our Time: Secure and Practical GenAI Workflows for Faculty and Staff

This interactive workshop equips faculty and staff to harness generative artificial intelligence safely, with strict FERPA compliance and direct alignment to institutional Single Source of Truth (SSoT) standards.

---

## Workshop Video Overview

{{< workshop-video src="/videos/reclaiming-our-time.mp4" vtt="/videos/reclaiming-our-time.vtt" >}}

---

## Executive Presentation Deck

Use arrow keys or onscreen controls to navigate slides. Press **L** to toggle the institutional Navy Blue laser pointer.

{{< workshop-carousel >}}

---

## Executive Visual Summary & Workflow Map

The Sovereign Auditor model ensures that no generative AI output is accepted without verification against predefined institutional standards.

### Core Operating Framework: The Mission Loop

The **Mission Loop (Pattern / Rule / Solve)** framework structures the interaction:

1. **Pattern:** Identify the structure and patterns of the case or administrative task.
2. **Rule:** Apply authorized federal, institutional, or clinical standards.
3. **Solve:** Generate a verified solution with zero data retention.

### Module 1: Instant Syllabus Compliance Audit

Rapid alignment of course syllabi against departmental rubrics and academic integrity policies.

### Prompt Architecture: Delimiter Isolation Protocol

{{< prompt-card title="Delimited Prompt Architecture / Protocolo de Aislamiento" subtitle="Focus: Zero-retention data isolation and strict boundary enforcement using triple-hash (###) delimiters." badge="PROMPT TEMPLATE" badgeClass="DELIMITER PROTOCOL" >}}
    ###
    [ROLE & CONTEXT]:
    Act as an Expert Sovereign Auditor and Curriculum Specialist. Your task is to evaluate and align institutional course content against authoritative Single Source of Truth (SSoT) standards without retaining user data.

    [OPERATIONAL RULES]:
    1. Operate strictly within the provided delimited boundaries.
    2. Cross-reference the input text exclusively against the provided policy standards.
    3. Highlight compliance gaps, missing accessibility vectors, and alignment discrepancies.
    4. Output findings in a structured, actionable Markdown table.

    [INPUT DATA / TEXT TO AUDIT]:
    ###
    [INSERT UNSTRUCTURED SYLLABUS, RUBRIC, OR MEETING TRANSCRIPT HERE]
    ###

    [AUDIT DIRECTIVE]:
    Generate the audit matrix identifying:
    - Finding / Gap
    - Authoritative Rule Reference
    - Remediation Action Item
    ###
{{< /prompt-card >}}

### Prompt Template: Meeting Action Matrix

{{< prompt-card title="Administrative Relief / Matriz de Acciones de Reunión" subtitle="Focus: Extracting deterministic action items, task owners, and deliverables from raw committee transcripts." badge="MEETING MATRIX PROMPT" badgeClass="ADMIN RELIEF" >}}
    ###
    [ROLE & CONTEXT]:
    Act as an Executive Administrative Assistant. Transform the unstructured committee or faculty meeting notes into an actionable, prioritized execution matrix.

    [EXTRACTION RULES]:
    1. Isolate explicit deliverables, appointed task leads, and milestone deadlines.
    2. Group items by operational domain (Curriculum, Compliance, Operations, Technology).
    3. Identify unassigned decisions requiring leadership follow-up.
    4. Do not invent details; flag ambiguity explicitly.

    [RAW MEETING NOTES]:
    ###
    [INSERT RAW MEETING NOTES, TRANSCRIPTS, OR COMMITTEE BULLETS HERE]
    ###

    [OUTPUT FORMAT]:
    Provide a Markdown table with columns:
    | Item # | Action Item / Deliverable | Responsible Lead | Target Completion | Priority (High/Med/Low) |
    ###
{{< /prompt-card >}}

---

## Module 4: FERPA Compliance & Secure Routing

Safeguarding student records in accordance with federal regulations and institutional IT guidelines.

### Workshop Summary & Resource Index

- **Quick Start Guide:** Accessible OER audit templates and rubrics.
- **Support Channel:** Strategic consulting for curriculum committees and instructional design.
