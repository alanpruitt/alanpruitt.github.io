---
title: "Essay 38: What If I Didn't Build the Graph? – Why Curriculum-as-Code Transcends Flat Docs-as-Code with DOM GraphRAG & W3C PROV-O"
date: 2026-11-01T10:00:00-07:00
draft: false
tags: ["Curriculum-as-Code", "DOM GraphRAG", "W3C PROV-O", "W3C SKOS", "Sovereign AI", "WCAG 3.0", "ADA Title II", "Higher Ed"]
categories: ["Essays"]
description: "A counterfactual examination of why flat vector RAG fails clinical higher education—and how DOM GraphRAG, W3C PROV-O provenance receipts, Born-Accessible 9:1 XAI scorecards, and W3C SKOS bilingual ontologies protect academic sovereignty."
translationKey: "essay-38"
slug: "essay-38-dom-graphrag-and-prov-o-curriculum-as-code"
aliases:
  - /essays/essay-38/
  - /essays/38/
  - /essays/essay38/
---

When I first engineered a **Git-versioned Markdown repository** with **automated CI/CD workflows** to manage a multi-course exercise science and clinical nutrition fleet (`EXW 101`, `EXW 150`, `EXW 210`, `EXW 245`, and `EXW 265`), I could have stopped at standard *Docs-as-Code*.

I already had clean Markdown source files, automated **Canvas GraphQL** synchronization, and a local vector index over **3,151 curriculum chunks**. By conventional software documentation standards, the pipeline was finished.

Every time a system reaches baseline maturity, however, I pressure-test it against the same guiding counterfactual:

**What if I didn't build the graph?**

What if I treated a clinical kinesiology and nutrition curriculum like a flat software manual—slicing pages into isolated 500-token chunks, retrieving them by raw cosine similarity, returning opaque AI confidence numbers to students, and assuming English-only terminology would magically serve a bilingual **Hispanic-Serving Institution (HSI)** along the **Yuma, AZ / Imperial Valley, CA** borderland?

The answer is clear: flat *Docs-as-Code* without structural pedagogy and cryptographic provenance eventually collapses back into probabilistic guesswork.

---

## Anatomy of the Flat-Vector Trap

In enterprise software documentation, *Docs-as-Code* treats pages as independent reference articles. If a developer searches for an API parameter, any matching paragraph will suffice.

Higher education—especially clinical exercise physiology and nutrition governed by non-negotiable **Federal Single Sources of Truth** (**PAGA 2nd Ed. 2018**, **2025–2030 Dietary Guidelines for Americans**, **ACSM 12th Ed.**, and the **NASM OPT Model**)—operates under far stricter constraints. Leaving a Retrieval-Augmented Generation (RAG) pipeline flat creates four structural fault lines:

1. **Context-Blind Retrieval (Orphaned Clinical Rules):**
   When a Markdown module is sliced into flat chunks, a contraindication table or safety gate loses its relationship to the Module's **Course Learning Outcomes (CLOs)**, its Required Reading foundation, and its parent phase inside **The Clinical Framing Protocol (`Pattern / Rule / Solve`)**.
2. **Unverifiable AI Synthesis (Zero Lineage):**
   If an AI tutor or clinical auditor synthesizes feedback without a machine-readable provenance graph, neither the student nor an accreditation committee can prove *which* exact Federal SSoT revision, Git commit, or local model produced the recommendation.
3. **The Black-Box Score Fallacy:**
   Handing a student a single opaque similarity percentage (`84% Match`) tells them nothing about *why* their clinical reasoning succeeded or where their safety gate failed.
4. **The Bilingual Vocabulary Gap:**
   When a first-generation resident in Yuma or San Luis describes heat exhaustion in authentic **Norteño-Spanish** (*"se le bajó la presión y anda bien mareado en el calorón de Yuma"*), a flat English vector index misses the exact clinical mapping to **exertional heat illness**, **orthostatic hypotension**, and **WBGT > 82°F fluid replacement gates**.

---

## Engineering the Upgrade: Four Pillars of S-A-R v2.2

As an **Adjunct Faculty of Exercise Science & Wellness at Arizona Western College**, **Generative AI Strategist at The University of Arizona**, and **Principal of Webcognita LLC (VOSB)**, I designed the **S-A-R Standard (Scalable / Auditable / Repeatable)** so that every architectural gap is closed deterministically across the entire **scalable $0 ZTC Open Educational Resource (OER) course fleet**.

Instead of settling for flat *Docs-as-Code*, we upgraded the **EXW Master Library (`v2.2`)** with four open-standard semantic layers running on **air-gapped Google Gemini Argon 4 models locally on Apple Silicon (M1/M2) for 100% FERPA privacy**:

```text
+-----------------------------------------------------------------------------+
|            CURRICULUM-AS-CODE (S-A-R v2.2) SEMANTIC GRAPH ENGINE            |
|                                                                             |
|  [1. W3C SKOS Ontology]  ->  Bilingual Norteño-Spanish <-> Clinical SSoT    |
|  [2. DOM GraphRAG]       ->  3,151 Nodes Linked by CLOs & Pattern/Rule/Solve|
|  [3. Born-Accessible XAI]->  9:1 Contrast 4D Radar (Pattern/Rule/Solve/Ver.)|
|  [4. W3C PROV-O Receipt] ->  Cryptographic SHA-256 Lineage (SSoT -> Argon4) |
+-----------------------------------------------------------------------------+
```

### 1. DOM GraphRAG (Structural Pedagogical Graph)

Rather than indexing isolated text fragments, our indexer (`scripts/index_corpus.py`) parses the semantic Document Object Model (DOM) of every curriculum file. Every one of our **3,151 curriculum vectors** is enriched with a `dom_graph_node` payload containing:
- Its exact `dom_path` (`h2 > h3` semantic hierarchy),
- Its governing role inside **The Clinical Framing Protocol (`Pattern / Rule / Solve`)**,
- Its explicit **Course Learning Outcome (`CLO`)** alignment, and
- Directed `graph_edges` (`parent_module`, `requires_reading`, `grounds_lab`, `grounds_discussion`, and `governed_by_ssot`).

When a student audits a lab inside Canvas, the engine retrieves not just a matching paragraph, but the complete pedagogical subgraph linking the reading, the lab rubric, and the federal guideline.

### 2. W3C PROV-O Cryptographic Provenance Receipts

Every live **Sovereign AI Auditing** response returned by our local API (`scripts/canvas_rag_api.py`) now emits a formal **W3C PROV-O (`http://www.w3.org/ns/prov#`)** JSON-LD provenance graph (`prov_o_receipt`) alongside a deterministic SHA-256 `receipt_id`:
- **`prov:Entity` (`exw:SSoTCorpus`):** The exact federal guideline (`PAGA 2018`, `DGA 2025-2030`, `ACSM 12th Ed.`, or `NASM OPT`) and the Git-versioned curriculum chunks retrieved.
- **`prov:Activity` (`exw:ClinicalAuditSynthesis`):** The timestamped execution of the local RAG + Clinical Framing audit.
- **`prov:Agent` (`exw:SovereignArgon4Auditor`):** Our air-gapped local **Google Gemini Argon 4** engine running on Apple Silicon (`M1/M2`) with zero external cloud telemetry.

### 3. Born-Accessible (`9:1` Contrast) 4-Dimensional XAI Radar Scorecard

Under our **ADA Title II & Atomic WCAG 2.2 AA / 3.0 Higher Ed Architecture**, explainability must be born accessible. Inside the live Canvas Clinical Auditor Modal, we replaced single-number confidence scores with a **4-Dimensional Explainable AI (XAI) Radar Scorecard** engineered to our strict **9:1 Double-Contrast Guard** (`#FFFFFF` on `#090D16` = `19.3:1`; `#38BDF8` sky cyan = `9.82:1`; `#34D399` mint = `10.45:1`; `#FBBF24` amber = `11.85:1`):
- **Pattern (`Context & Telemetry` — 25%):** Client vitals, biometrics, and regional **Yuma / Imperial Valley** heat stressors.
- **Rule (`Federal SSoT Citation` — 25%):** Explicit quantitative anchors from PAGA, DGA, ACSM, or NASM.
- **Solve (`Clinical Intervention` — 25%):** Concrete FITT-VP or "Real Food" prescription with safety gates.
- **Active Verification (`150-Word Defense` — 25%):** Authentic human justification in the student's own voice.

### 4. W3C SKOS / Schema.org Bilingual Clinical Controlled Vocabulary

To honor our mission of delivering **bilingual "In Plain English" OER across borderland HSI communities**, we authored a formal **W3C SKOS (`Simple Knowledge Organization System`)** and **Schema.org (`MedicalEntity`)** controlled vocabulary (`01_INFRASTRUCTURE/skos_bilingual_clinical_taxonomy.json`).

Colloquial **Norteño-Spanish** clinical expressions (`skos:altLabel @es-MX-Norteno`) map deterministically to English and Spanish clinical terms (`skos:prefLabel`) and federal SSoT rules (`skos:definition`). When a resident queries our RAG pipeline in Norteño-Spanish, the SKOS layer automatically expands the vector query across languages—lifting top clinical retrieval similarity from `0.7743` to **`0.8236`** without requiring the student to abandon their community's authentic voice.

---

## Slow is Smooth, Smooth is Fast

*What if I didn't build the graph?*

Without **DOM GraphRAG**, **W3C PROV-O**, **Born-Accessible 9:1 XAI**, and **W3C SKOS bilingual ontologies**, a course repository is just a static folder of text waiting to be summarized by commercial chatbots.

By binding every paragraph, bilingual clinical term, and AI audit receipt into an auditable semantic graph, we prove that **Curriculum-as-Code** can simultaneously defend academic rigor, guarantee **100% FERPA privacy**, and expand equitable access for every student in our borderland classrooms.

---

### Explore the Architecture Briefs & White Papers

All six formal architecture briefs and technical white papers—including the **EXW S-A-R v2.2 DOM GraphRAG & W3C PROV-O Architecture Brief** and the **AWC 2026 Innovation Fund "Project Horizon" White Papers**—are available for direct download in the [**Architecture Briefs & Grant White Papers shelf on alanpruitt.com**](/#architecture-briefs).
