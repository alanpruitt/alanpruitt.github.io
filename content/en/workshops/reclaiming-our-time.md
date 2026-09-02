---
title: "Reclaiming Our Time: Secure and Practical GenAI Workflows for Faculty and Staff"
description: "Interactive professional development workshop covering GenAI governance, FERPA compliance, administrative relief workflows, and SSoT syllabus auditing."
date: 2026-08-15
type: "workshop"
translationKey: "reclaiming-our-time"
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

---

## Module 1: Policy Foundations & Enterprise Authentication

- **Institutional Posture:** Adoption of legally sound, academically rigorous GenAI practices to achieve meaningful administrative relief.
- **Enterprise Authentication Boundary:** Avoid consumer, unauthenticated AI interfaces where inputs may be ingested to train public models. Always log in through institutional SSO credentials:
  - **Google Gemini Enterprise**
  - **Microsoft Copilot Enterprise**
- **Data Privacy Assurance:** Enterprise licensing guarantees that uploaded files, meeting minutes, and draft syllabi are isolated from public model training datasets.

---

## Module 2: Live Administrative Relief Demonstrations

Practical, high-yield workflows demonstrated live to reduce administrative burden:

1. **Syllabus Compliance Auditing:** Ingesting draft syllabi alongside departmental rubrics, institutional policies, and ADA Title II accessibility requirements.
2. **Committee Synthesis & Action Items:** Processing raw meeting transcripts into executive summaries and structured accountability matrices.
3. **Rubric Scaling & Formative Feedback:** Streamlining evaluation rubrics and generating targeted feedback criteria while maintaining complete instructor oversight.

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

## Module 3: Hands-on Micro-Lab: Prompt Architecture & Boundary Enforcement

Isolating task instructions from institutional data inputs is essential for deterministic, hallucination-free outputs.

- **The Delimiter Protocol:** Wrapping all variable institutional data in explicit triple-hash (`###`) fences establishes a hard prompt boundary.
- **Zero Data Retention Instructions:** Enforcing explicit negative constraints ensures the model operates strictly as an ephemeral parser rather than a knowledge repository.

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

---

## Module 4: FERPA Compliance & Secure Routing

Safeguarding student records and directory information in accordance with federal law:

- **Zero PII Transmission:** Never paste student names, ID numbers, grades, or sensitive demographic data into any AI prompt interface.
- **De-identification Standards:** Anonymize and redact all student case work or peer discussions prior to analysis.
- **Human-in-the-Loop Imperative:** Automated outputs serve as initial drafts; final grading, curriculum design, and administrative sign-offs remain strictly human responsibilities.

---

## Module 5: Synthesis, Resources & Institutional Support

### Enterprise Tools & Official University Routing

- **Primary Responsible AI Portal:** Access authorized tools, request enterprise accounts, and review official guidelines via the [University of Arizona Responsible Artificial Intelligence Start Here Portal](https://responsibleai.arizona.edu/tools-support/start-here).
- **Institutional GenAI Support & Intake:** Submit departmental inquiries, review privacy and security evaluations, and access sanctioned generative AI resources directly through the Responsible AI support desk.
- **Data Governance & FERPA Inquiries:** Consult University Information Security and privacy policies through the Responsible AI portal before uploading or processing institutional materials.
