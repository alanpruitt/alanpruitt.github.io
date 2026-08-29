---
title: "Reclaiming Our Time: Secure and Practical GenAI Workflows for Faculty and Staff"
date: 2026-08-29T10:00:00-07:00
publishDate: 2026-08-29T10:00:00-07:00
draft: false
slug: "reclaiming-our-time"
description: "A 60-minute interactive professional development blueprint and reference portal for secure enterprise GenAI workflows, prompt delimiter architecture, and FERPA/HIPAA compliance."
categories: ["Generative AI", "Higher Education Governance", "Workshops", "Faculty Development"]
layout: "workshop-single"
facilitator: "Alan Pruitt"
facilitator_title: "Designated Campus Colleague (DCC - Yuma) & Generative AI Strategist"
facilitator_email: "alanpruitt@arizona.edu"
institutional_alignment: "Office of Responsible AI, Information Security Office (ISO), and U of A Enterprise AI Infrastructure"
duration: "60 Minutes"
---

## Workshop Video Overview

{{< workshop-video src="/videos/reclaiming-our-time.mp4" vtt="/videos/reclaiming-our-time.vtt" >}}

---

## Session Architecture & Timing

<div class="timing-grid">
  <div class="timing-card">
    <span class="timing-span">00:00 - 00:10</span>
    <div class="timing-title">Module 1: Enterprise Ecosystem</div>
  </div>
  <div class="timing-card">
    <span class="timing-span">00:10 - 00:30</span>
    <div class="timing-title">Module 2: Live Workflows</div>
  </div>
  <div class="timing-card">
    <span class="timing-span">00:30 - 00:45</span>
    <div class="timing-title">Module 3: Prompt Micro-Lab</div>
  </div>
  <div class="timing-card">
    <span class="timing-span">00:45 - 00:55</span>
    <div class="timing-title">Module 4: FERPA & Routing</div>
  </div>
  <div class="timing-card">
    <span class="timing-span">00:55 - 01:00</span>
    <div class="timing-title">Synthesis & Reference</div>
  </div>
</div>

---

## Module 1: Policy Grounding & The Enterprise Ecosystem (10 mins)

* **Institutional Stance:** The University of Arizona supports legally sound, academically rigorous AI integration to deliver meaningful administrative and pedagogical relief.
* **Enterprise Authentication Boundary:** Avoid unauthenticated consumer AI interfaces where prompts may be harvested for model training. Always authenticate via NetID into institutional instances:
  * **Google Gemini Enterprise**
  * **U of A GenAI**
  * **Microsoft Copilot Enterprise**
* **Data Privacy Assurance:** Enterprise licensing agreements guarantee that inputs and uploaded documents are not ingested into public foundation models, providing a secure perimeter for course design and drafting.

---

## Module 2: Live Demonstration of Administrative Relief (20 mins)

Three live demonstrations executed during the active workshop session:

1. **Instant Syllabus Compliance Auditing:** Ingesting a draft course syllabus alongside institutional policy checklists to audit grading scales, ADA Title II accessibility statements, and required institutional disclosures.
2. **Transcript Synthesis & Action Items:** Ingesting raw departmental or committee meeting transcripts to automatically generate executive summaries, chronological decision logs, and accountability matrices.
3. **Rubric Scaling & Formative Feedback:** Processing assignment prompts, evaluation rubrics, and de-identified student drafts to generate high-quality formative feedback while maintaining instructor authority.

---

## Module 3: Hands-On Micro-Lab: Prompt Vault & Delimiters (15 mins)

### Prompt Architecture Protocol

Wrap all variable data (course outlines, meeting notes, rubrics) in explicit triple-hash (`###`) delimiter blocks to isolate context from instructions, eliminating model drift and hallucination.

```plaintext
### ROLE & OBJECTIVE ###
You are an expert curriculum designer and higher-education administrator.

### CONTEXT ###
[Insert sanitized course outline, meeting notes, or assignment prompt here]

### TASK & CONSTRAINTS ###
Audit the context against departmental standards. Enforce a professional tone, tabular output, and zero hallucination.
```

### The Importance of Delimiters

Without explicit delimiters, LLMs frequently merge user instructions with context data. This causes "instruction leakage" or "prompt injection," where raw input data containing commands mistakenly overrides the system's objective. Delimiting content ensures strict boundary compliance and deterministic processing.

---

## Module 4: FERPA Compliance & Secure Routing (10 mins)

* **The Student Privacy Boundary (FERPA):** Federal law protects student education records. Never paste student names, emails, ID numbers, grades, GPAs, or disciplinary histories into any AI prompt interface, whether enterprise or consumer-grade.
* **Sanitization Workflow:** Always sanitise content before running evaluations:
  1. Remove all names, replacing them with standard identifiers (e.g. `Student A`, `Student B`).
  2. Strip out all explicit IDs, email addresses, and phone numbers.
  3. Redact any local descriptive narrative that could inadvertently identify a specific individual.
* **Enterprise Security is Not a FERPA Bypass:** While enterprise systems keep your inputs private within the U of A cloud tenancy, exposing student records still constitutes an unauthorized access risk under federal and institutional policies. Clean all inputs before processing.

---

## Synthesis & Reference Portal (5 mins)

### Quick-Start Faculty Checklist

1. **Am I authenticated?** Double-check that your Gemini or Copilot window indicates active enterprise NetID login.
2. **Is the input sanitised?** Ensure no personal student details are embedded in the prompt.
3. **Are delimiters active?** Confirm that all variables are enclosed in `###` blocks.
4. **Is the output audited?** Read the generated content carefully for accuracy.
5. **Am I in control?** Remember that the AI acts as your clinical processor, but the faculty member remains the pilot.

> *"AI Disclosure: This content was synthesized using Google Gemini. Residents must audit all clinical claims against the Source of Truth. AI can make mistakes."*
