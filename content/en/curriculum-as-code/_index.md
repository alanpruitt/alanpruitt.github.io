---
title: "Curriculum-as-Code (CaC): Origin Story, Historical Genealogy (2018–2026) & S-A-R v2.2 Reference Architecture"
date: 2026-11-11T08:45:00-07:00
lastmod: 2026-11-11T09:00:00-07:00
description: "Canonical origin whitepaper and reference hub for Curriculum-as-Code (CaC): tracing its evolution from 2018 NRE Labs container emulation to 2021 GitHub AI Co-Pilot SSoTs and 2026 S-A-R v2.2 neuro-symbolic DOM GraphRAG, W3C PROV-O provenance, ADA Title II (9:1) Compliance-as-Code, and air-gapped Sovereign Edge AI."
layout: "single"
outputs: ["HTML"]
draft: false
is_cac_pillar: true
scholar_title: "From Infrastructure Automation to Clinical Pedagogy: The Origin and Evolution of Curriculum-as-Code (2018-2026)"
scholar_date: "2026/11/11"
scholar_pdf_url: "https://alanpruitt.com/docs/Curriculum-as-Code-Origin-and-Evolution-Whitepaper.pdf"
sitemap:
  priority: 1.0
  changefreq: "weekly"
keywords:
  - "Curriculum-as-Code"
  - "Curriculum as Code"
  - "What is Curriculum-as-Code"
  - "History of Curriculum-as-Code"
  - "NRE Labs Curriculum-as-Code"
  - "S-A-R Standard"
  - "DOM GraphRAG"
  - "W3C PROV-O"
  - "ADA Title II Compliance as Code"
  - "Alan Pruitt"
  - "Webcognita LLC"
---

<section aria-label="Canonical Definition and Whitepaper Download" style="background-color: #FFFFFF; color: #0B192C; border: 2px solid #0B192C; border-left: 6px solid #940925; border-radius: 0.75rem; padding: 1.25rem 1.5rem; margin-bottom: 1.75rem;">
  <p style="margin: 0 0 0.65rem 0; font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 0.78rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.05em; color: #940925; background-color: #FFFFFF;">
    Canonical Definition &bull; Origin Whitepaper (S-A-R v2.2)
  </p>
  <p style="margin: 0 0 0.85rem 0; font-size: 1.05rem; line-height: 1.65; color: #0B192C; background-color: #FFFFFF;">
    <dfn id="definition" style="font-style: normal; font-weight: 800; color: #0B192C; background-color: #FFFFFF;">Curriculum-as-Code (CaC)</dfn> is an instructional engineering discipline that treats syllabi, readings, clinical simulations, competency rubrics, and accessibility governance as plain-text, Git-versioned source code compiled through automated Continuous Integration (CI/CD) verification gates into Learning Management Systems (LMS) and open-access educational datasets.
  </p>
  <p style="margin: 0 0 1rem 0; font-size: 0.95rem; line-height: 1.6; color: #18181b; background-color: #FFFFFF;">
    <strong>In Plain English:</strong> Before you read the technical architecture below, here is the short version: <strong>Curriculum-as-Code builds college courses the same way software engineers build reliable apps.</strong> Instead of trapping lessons inside fragile website editors or expensive textbooks, every reading, rubric, and accessibility check lives in clean text files that automatically test themselves before reaching students.
  </p>
  <div style="display: flex; flex-wrap: wrap; gap: 0.75rem; align-items: center;">
    <a href="/docs/Curriculum-as-Code-Origin-and-Evolution-Whitepaper.pdf" download style="display: inline-flex; min-height: 44px; align-items: center; padding: 0.55rem 1rem; border-radius: 0.5rem; background-color: #0B192C; color: #FFFFFF; font-size: 0.85rem; font-weight: 700; text-decoration: none; border: 1.5px solid #0B192C;">
      Download Origin Whitepaper (PDF &bull; 2 Pages &bull; 525 KB) &rarr;
    </a>
    <a href="#academic-citation" style="display: inline-flex; min-height: 44px; align-items: center; padding: 0.55rem 1rem; border-radius: 0.5rem; background-color: #FFFFFF; color: #0B192C; font-size: 0.85rem; font-weight: 700; text-decoration: underline; border: 1.5px solid #0B192C;">
      Cite Paper (APA 7 &amp; BibTeX)
    </a>
    <a href="https://alanpruitt.substack.com/p/what-if-i-didnt-trace-the-lineage" target="_blank" rel="noopener noreferrer" style="display: inline-flex; min-height: 44px; align-items: center; padding: 0.55rem 1rem; border-radius: 0.5rem; background-color: #FFFFFF; color: #0B192C; font-size: 0.85rem; font-weight: 700; text-decoration: underline; border: 1.5px solid #0B192C;">
      Substack Dispatch: &ldquo;What If I Didn&rsquo;t Trace the Lineage?&rdquo; &rarr;
    </a>
    <a href="https://www.linkedin.com/feed/update/urn:li:activity:7526393204666077184/" target="_blank" rel="noopener noreferrer" style="display: inline-flex; min-height: 44px; align-items: center; padding: 0.55rem 1rem; border-radius: 0.5rem; background-color: #FFFFFF; color: #0B192C; font-size: 0.85rem; font-weight: 700; text-decoration: underline; border: 1.5px solid #0B192C;">
      LinkedIn Discussion &amp; Carousel &rarr;
    </a>
    <a href="https://me.developers.google.com/u/alanpruitt" target="_blank" rel="noopener noreferrer" style="display: inline-flex; min-height: 44px; align-items: center; padding: 0.55rem 1rem; border-radius: 0.5rem; background-color: #FFFFFF; color: #0B192C; font-size: 0.85rem; font-weight: 700; text-decoration: underline; border: 1.5px solid #0B192C;">
      Verified Author: g.dev/alanpruitt &rarr;
    </a>
  </div>
</section>

## Abstract

This flagship origin paper establishes the historical genealogy and architectural evolution of **Curriculum-as-Code (CaC)** from 2018 network reliability engineering (`NetOps`) to 2026 neuro-symbolic higher-education pedagogy. In November 2018, the NRE Labs community (`nre-learning/nrelabs-curriculum` and the Antidote platform) coined *Curriculum-as-Code* to orchestrate Kubernetes virtual routers and browser terminals via declarative YAML (`syringe.yaml`). Because Generation 1 coupled educational materials permanently to heavy container clusters, NRE Labs ultimately shut down under runtime maintenance overhead. Generation 2 (`2021–2026`) decoupled prose into plain-text Git repositories—demonstrated early by Alan Pruitt's **August 2021 NADO Aliceann Wohlbruck Impact Award** for compiling a regional Comprehensive Economic Development Strategy (`CEDS`) manual via an open-source GitHub AI Co-Pilot, and echoed later by 2026 STEM LaTeX/Beamer slide scripts (`arXiv:2608.07364`)—yet flat file pipelines remained blind to semantic pedagogy, LMS accessibility checkers, and cryptographic auditability.

Generation 3 (**Sovereign Neuro-Symbolic Curriculum-as-Code**, `S-A-R v2.2` — *Scalable / Auditable / Repeatable*) resolves those structural gaps across a live 5-course, 11-shell higher-education fleet (`EXW 101`, `150`, `210`, `245`, `265` and national `KIN` / `HLTH` Open Educational Resource packages). By uniting **The Centaur Protocol**, **The Clinical Framing Protocol (`Pattern / Rule / Solve`)**, federal Single Sources of Truth (**PAGA 2018**, **DGA 2025–2030**, **ACSM 12th Ed.**, **NASM OPT**, and **U.S. DOL ETA TEN No. 07-25**), automated **ADA Title II / WCAG 2.2 AA (`9:1` Double-Contrast Guard) & WCAG 3.0** CI/CD linters, a **`3,265`-node DOM GraphRAG** knowledge graph, **W3C PROV-O** SHA-256 provenance receipts, **W3C SKOS** Norteño-Spanish clinical ontologies, and air-gapped Apple Silicon Edge AI (**Google Gemini Carbon 4** and **Gemma 4**), `S-A-R v2.2` guarantees institutional data sovereignty, clinical rigor, and `$0 ZTC` open-access syndication.

---

## 1. Historical Roots: Three Generations of Curriculum-as-Code (2018–2026)

### 1.1 Generation 1 (2018): NetOps Container Emulation at NRE Labs

In late 2018, network reliability engineers introduced the phrase **Curriculum-as-Code** through NRE Labs, the Antidote engine, and the archived [nre-learning/nrelabs-curriculum GitHub repository](https://github.com/nre-learning/nrelabs-curriculum) *(note: the hosted NRE Labs web portal has permanently shut down, and interactive labs are offline)*. Borrowing directly from *Infrastructure-as-Code (IaC)*, NRE Labs codified lesson guides (`guide.md`) and virtual network topologies (`syringe.yaml`) inside Git so contributors could propose updates through pull requests and automated tests.

However, the "code" in 2018 NetOps curricula was fundamentally **infrastructural**. Every lesson spun up live Docker containers, Kubernetes (`Minikube`) pods, and browser-based SSH/CLI terminal proxies to emulate routers, switches, and firewalls. While pioneering for CLI training, coupling every reading and exercise to live Kubernetes cluster orchestration created severe operational fragility—ultimately forcing the hosted NRE Labs platform to shut down.

### 1.2 Generation 2 (2021–2026): Plain-Text SSoTs, GitHub AI Co-Pilots, and Slide Pipelines

As educators and policy architects sought vendor independence without Kubernetes cluster overhead, Generation 2 shifted the locus of code from *virtualized hardware* to *plain-text document compilation*:

* **August–September 2021 Open-Source HTML, Python API & GitHub AI Co-Pilot Precursor:** Five years before 2026 academic slide-generation preprints, Alan Pruitt—serving as Executive Director of the Western Arizona Economic Development District (`2007–2022`)—replaced static print PDFs (*"The Gutenberg Effect"*) with a living, screen-reader-accessible HTML and Python API regional Comprehensive Economic Development Strategy (`CEDS`) engineered using open-source VS Code, automated `U.S. Census` / `BLS` / `BEA` data pipelines, and an early-stage GitHub AI Co-Pilot model, earning the **2021 NADO Aliceann Wohlbruck Impact Award** and an independent feature in the [U.S. EDA-supported StatsAmerica Q3 2021 User Spotlight](https://www.statsamerica.org/newsletter/2021Q3.aspx).
* **2025–2026 Flat Docs-as-Code and STEM Slide Scripts:** Subsequent academic workflows—including 2026 STEM slide-generation frameworks (`arXiv:2608.07364`)—paired generative AI with Python and LaTeX/Beamer to automate lecture slide formatting and technical plots.

While Generation 2 eliminated proprietary word-processor lock-in, flat document and slide pipelines left four institutional failure modes unsolved:
1. **Orphaned Pedagogical Context:** Slicing flat Markdown or LaTeX files into isolated chunks severs safety gates from Course Learning Outcomes (`CLOs`) and competency rubrics.
2. **Downstream Accessibility Drift:** Static Beamer PDFs and unverified HTML fail strict **ADA Title II (`28 CFR Part 35`)** mandates and LMS server-side accessibility scanners.
3. **Monolingual Exclusion:** English-only pipelines fail borderland Hispanic-Serving Institution (`HSI`) cohorts who reason across clinical English and regional Spanish dialects.
4. **Cloud FERPA Exposure:** Routing student work or institutional IP through commercial cloud LLM APIs surrenders data sovereignty.

### 1.3 Generation 3 (2026): Sovereign Neuro-Symbolic Curriculum-as-Code (S-A-R v2.2)

Independently engineered and field-tested by Alan Pruitt across active Exercise Science & Wellness (`EXW`) cohorts at **Arizona Western College**—a borderland Hispanic-Serving Institution (`HSI`) serving a **77% Latino** (`3.08x` the 25% federal Title V HSI threshold) and **62% first-generation** student body (*"At AWC, 77% of students are Latino, and 62% are first-generation students. We serve this beautiful community, but challenge is everywhere,"* AWC President Dr. Reetika Dhawan, as quoted in *The Yuma Sun*, November 11, 2026)—and R1 applied Edge AI research at **The University of Arizona (School of Nutritional Sciences and Wellness — Yuma Campus)** through **Webcognita LLC (`SDVOSB`)**, Generation 3 (**`S-A-R v2.2` — Scalable / Auditable / Repeatable**) decouples instructional logic from both fragile container clusters and static slide decks. Every syllabus, clinical simulation, competency rubric, bilingual ontology node, and accessibility rule is compiled from a single Git repository into Canvas LMS via GraphQL, `$0 ZTC` Progressive Web Apps (`exwtoolkit.com`), OER Commons archives, and Google Dataset Search JSON-LD.

---

## 2. Three-Generation Paradigm Comparison Matrix

<div tabindex="0" role="region" aria-labelledby="cac-matrix-caption" style="overflow-x: auto; max-width: 100%; margin: 1.25rem 0 1.75rem 0;">
  <table>
    <caption id="cac-matrix-caption">Architectural Evolution of Curriculum-as-Code from 2018 Container Emulation to 2026 S-A-R v2.2 Pedagogy</caption>
    <thead>
      <tr>
        <th scope="col">Architectural Dimension</th>
        <th scope="col">Gen 1: NetOps Infrastructure Model (NRE Labs, 2018)</th>
        <th scope="col">Gen 2: Flat Docs and Slide Pipelines (2021–2026)</th>
        <th scope="col">Gen 3: Sovereign Neuro-Symbolic CaC (S-A-R v2.2, 2026)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <th scope="row">Primary Domain</th>
        <td>Network reliability engineering (<code>NetOps</code>), CLI automation, and virtual packet routing.</td>
        <td>Regional economic strategy manuals (<code>2021 CEDS</code>), software docs, and STEM LaTeX/Beamer slides (<code>arXiv:2608.07364</code>).</td>
        <td>Higher-education kinesiology, clinical nutrition, special populations, and workforce AI literacy (<code>EXW</code>, <code>KIN</code>, <code>HLTH</code>).</td>
      </tr>
      <tr>
        <th scope="row">Execution Environment</th>
        <td>Containerized network emulators orchestrated by Kubernetes (<code>Minikube</code>), Docker pods, and <code>syringe.yaml</code> browser terminals (platform shut down).</td>
        <td>Plain-text Markdown or LaTeX repositories compiled into static slide PDFs or flat reference sites.</td>
        <td>Immutable Markdown SSoT, Git CI/CD, Hugo SSG, <strong>Canvas LMS GraphQL (<code>/api/graphql</code>)</strong> 3-Stage Zero-Drift Pipeline, and browser-native PWAs (<code>exwtoolkit.com</code>).</td>
      </tr>
      <tr>
        <th scope="row">Pedagogical Taxonomy</th>
        <td><code>Course &rarr; Lesson &rarr; Lab Stage</code> focused on procedural CLI command execution.</td>
        <td>Linear chapters or lecture decks without machine-typed competency edges.</td>
        <td><code>Course &rarr; Module &rarr; Scaffolded Residency</code> governed by <strong>The Centaur Protocol</strong> and <strong>The Clinical Framing Protocol (<code>Pattern / Rule / Solve</code>)</strong>.</td>
      </tr>
      <tr>
        <th scope="row">Governing Standards &amp; SSoT</th>
        <td>Technical correctness of network scripts, API calls, and packet state.</td>
        <td>Author-defined prompt templates and mathematical typesetting rules.</td>
        <td>Public-domain federal and national clinical SSoTs: <strong>PAGA 2018 (2nd Ed.)</strong>, <strong>DGA 2025–2030</strong>, <strong>ACSM 12th Ed. (2025)</strong>, <strong>NASM OPT</strong>, and <strong>U.S. DOL ETA TEN No. 07-25</strong>.</td>
      </tr>
      <tr>
        <th scope="row">Accessibility &amp; Civil Rights</th>
        <td>Browser terminal UI without formal cognitive or high-contrast compliance gates.</td>
        <td>Downstream manual PDF remediation; frequent LMS accessibility checker parity failures.</td>
        <td>Pre-push <strong>Compliance-as-Code</strong> enforcing all <strong>8 Canvas Course Accessibility Checker rules</strong>, the <strong><code>9:1</code> Double-Contrast Guard</strong>, and <strong>WCAG 3.0</strong> bilingual callouts.</td>
      </tr>
      <tr>
        <th scope="row">Semantic Graph &amp; Provenance</th>
        <td>Imperative container state verification scripts.</td>
        <td>Flat files or context-blind cosine similarity vector chunks.</td>
        <td><strong><code>3,265</code>-node DOM GraphRAG</strong> + <strong>W3C SKOS</strong> Norteño-Spanish ontology + <strong>W3C PROV-O</strong> SHA-256 cryptographic receipts.</td>
      </tr>
      <tr>
        <th scope="row">AI Inference &amp; Sovereignty</th>
        <td>Pre-LLM deterministic shell validation.</td>
        <td>Commercial cloud LLM APIs with external telemetry egress.</td>
        <td><strong>100% Air-Gapped Apple Silicon (<code>M1/M2</code>) Edge AI</strong> running local <strong>Google Gemini Carbon 4</strong> and <strong>Gemma 4</strong> via Ollama (zero FERPA cloud leakage).</td>
      </tr>
      <tr>
        <th scope="row">Open Syndication &amp; Licensing</th>
        <td>Archived GitHub YAML/Markdown repository (<code>Apache-2.0</code>).</td>
        <td>Isolated institutional PDFs or course silos.</td>
        <td><strong>Non-Destructive Dual-Namespace (<code>EXW &rarr; KIN / HLTH</code>)</strong> OER Commons <code>.zip</code> archives (<code>21/21</code> Achieve Rubric score) + 4-Tier <code>Schema.org/Dataset</code> JSON-LD under <strong>CC BY-NC-SA 4.0</strong>.</td>
      </tr>
    </tbody>
  </table>
</div>

---

## 3. Six Core Architectural Pillars of Modern Curriculum-as-Code

### 3.1 Immutable Markdown SSoT and 5-Course Federal Grounding

Commercial textbook paywalls impose financial barriers on community college students while lagging years behind updated federal clinical standards. Modern CaC establishes pure Markdown (`.md`) in Git as the immutable Single Source of Truth across all five fleet courses—bridging local institutional catalog codes to national transfer namespaces:

* **`EXW 101` (`KIN-101` — Concepts of Kinesiology):** Grounded in *Physical Activity Guidelines for Americans (PAGA), 2nd Edition (2018)*.
* **`EXW 150` (`HLTH-150` — Nutrition for Exercise & Sport):** Grounded in *2025–2030 Dietary Guidelines for Americans ("Real Food" Focus)*.
* **`EXW 210` (`KIN-210` — Principles of Strength & Conditioning):** Grounded in *PAGA 2018*, *ACSM's Guidelines for Exercise Testing and Prescription (12th Ed., 2025)*, and the *NASM Optimum Performance Training (OPT) Model*.
* **`EXW 245` (`KIN-245` — Exercise Testing & Prescription):** Grounded in *ACSM 12th Edition (2025)* clinical testing thresholds.
* **`EXW 265` (`KIN-265` — Exercise for Special Populations):** Grounded in *PAGA 2018* chronic-condition safety gates.
* **Fleet-Wide Workforce AI Literacy:** Every module operationalizes all **5 Foundational Content Areas** and **7 Community College Delivery Design Principles** of **U.S. Department of Labor (DOL) ETA Advisory TEN No. 07-25** (Issued February 13, 2026).

### 3.2 The Centaur Protocol and The Clinical Framing Protocol (Pattern / Rule / Solve)

To resist agentic offloading, Curriculum-as-Code trains the student as the **Clinical Architect and Problem Framer** and restricts AI to the **Clinical Calculator**. Every laboratory workflow enforces **The Clinical Framing Protocol** (`Pattern / Rule / Solve` • Spanish: `Patrón / Regla / Solución`):

1. **Pattern (Context):** Students diagnose client biometrics, physiological telemetry, and regional **Yuma, AZ / Imperial Valley, CA** extreme-heat stressors encapsulated inside triple-hash (`###`) case-data delimiters.
2. **Rule (Constraint):** Students audit probabilistic AI outputs against quantitative federal SSoT benchmarks (`PAGA`, `DGA`, `ACSM`, `NASM`).
3. **Solve (Intervention & Active Verification):** Students prescribe safe interventions calibrated on `exwtoolkit.com` and author a mandatory 150-word verbatim clinical defense in their own voice, evaluated on the iterative **10-7-0 Mastery Grading Scale** (`allowed_attempts = -1`).

### 3.3 Born-Accessible Compliance-as-Code (ADA Title II, 9:1 Contrast & WCAG 3.0)

Retrofitting broken LMS pages after publication cannot scale ahead of federal **ADA Title II (`28 CFR Part 35`)** deadlines. Upstream CI/CD Python linters (`remediate_canvas_accessibility_checker_exw101.py`, `pour_audit.py`, and `achieve_oer_linter.py`) enforce:

* **Zero Open Issues in Canvas Course Accessibility Checker:** Programmatic enforcement of all 8 institutional scanner rules—sequential `<h2> → <h3> → <h4>` hierarchy (`<= 120` chars), descriptive image alt text, decorative presentation markers, merged adjacent links, semantic lists, and `<caption>` + `<th scope="col|row">` tables.
* **The `9:1` Double-Contrast Guard:** Doubling WCAG 2.2 AA's `4.5:1` minimum to **`9.0:1+`** with explicit paired hex `color` and `background-color` rules validated for `100,000+ lux` desert glare.
* **WCAG 3.0 Cognitive and Bilingual Equity:** Bespoke **In Plain English / En Palabras Sencillas (Norteño-Spanish)** callouts at the top of every reading and authentic bilingual feedback parity.

### 3.4 Neuro-Symbolic Pedagogy: DOM GraphRAG, W3C PROV-O & W3C SKOS

Rather than slicing lessons into context-blind vector fragments, `S-A-R v2.2` compiles **`3,265` DOM GraphRAG nodes** preserving each section's semantic heading path, Course Learning Outcomes (`CLOs`), and rubric edges. A formal **W3C SKOS** controlled vocabulary maps colloquial Norteño-Spanish expressions to clinical SSoT definitions, while every local AI evaluation emits a **W3C PROV-O** JSON-LD receipt signed with a SHA-256 lineage hash.

### 3.5 GraphQL-First LMS Publishing and 21/21 Achieve OER Dataset Syndication

Through a **3-Stage "Write Once -> Push Many" Zero-Drift Publishing Pipeline** (`Fall 2026 Telemetry → Canonical DEV 0/0 Staging Gate → Spring 2027 Production`) executing over **Canvas GraphQL (`POST /api/graphql`)**, a single Git commit updates 11 Canvas shells while compiling 10 dual-namespace OER Commons `.zip` packages (`467/467` Markdown modules verified at **`21/21 [100.0%]`** on Achieve OER Rubrics + ISKME AI Attribution disclosure) and 4-Tier `Schema.org/Dataset` JSON-LD for Google Dataset Search.

### 3.6 Air-Gapped Edge AI Sovereignty and 50-State NSF AI-Ready Enablement

All local grading telemetry, RAG retrieval, and rubric validation execute on air-gapped Apple Silicon (`M1` and `M2`) workstations running open-weight **Google Gemini Carbon 4** and **Gemma 4** models via Ollama—achieving 100% FERPA student privacy at `$0.00` recurring cloud cost. Through **Webcognita LLC (`SDVOSB`, `SAM.gov UEI: EZ34U9KNJA17`, `CAGE: 4ZCN6`)**, this reference architecture serves as a **non-competing 50-state technical enabling partner** for community colleges, universities, tribal nations, and **NSF TechAccess: AI-Ready America** Coordination Hubs.

---

## 4. Empirical Research Chapters (Hub-and-Spoke Corpus)

This canonical origin paper anchors the longitudinal **40-Essay Curriculum-as-Code Research Series** and **92-Entry Master Research Log Observatory**:

* **[Essay 02 (July 30, 2026): Curriculum-as-Code — Treating Educational Content Like Software Development](/essays/02-curriculum-as-code/)** — Foundational thesis decoupling academic IP from proprietary LMS black boxes.
* **[Essay 26: Navigating Compliance Upstream — The Curriculum-as-Code POUR-Audit Framework](/essays/26-curriculum-as-code-pour-audit-framework/)** — Pre-commit Perceivable, Operable, Understandable, and Robust CI/CD verification.
* **[Essay 32: From Retrofit to Architecture — Operationalizing ADA Title II Compliance Before the Deadline](/essays/essay-32-from-retrofit-to-architecture/)** — Eliminating manual remediation backlogs with upstream `9:1` source linters.
* **[Essay 38: What If I Didn't Build the Graph? — Why Curriculum-as-Code Transcends Flat Docs-as-Code with DOM GraphRAG & W3C PROV-O](/essays/essay-38-dom-graphrag-and-prov-o-curriculum-as-code/)** — Deep dive into the `3,265`-node pedagogical graph, `W3C SKOS` Norteño-Spanish ontology, and cryptographic receipts.
* **[Essay 39: What If I Didn't Automate the Threshold? — Programmatic Canvas Rubric Validation & Edge AI Workflows](/essays/essay-39-automate-the-threshold/)** — Enforcing the `10-7-0` Mastery Grading Scale with air-gapped Apple Silicon inference.
* **[Essay 40: What If I Didn't Operationalize the Framework? — Turning U.S. DOL ETA Advisory TEN No. 07-25 into Born-Accessible Curriculum-as-Code](/essays/essay-40-federal-workforce-ai-literacy/)** — Mapping federal workforce AI literacy into `$0 ZTC` community college residencies.
* **[Live Observatory: Master Research Log (92 Dated Engineering Analyses)](/research-log/)** and **[50-State Institutional Infrastructure Matrix](/institutional-infrastructure/)**.

---

## 5. Frequently Asked Questions About Curriculum-as-Code

<section aria-labelledby="faq-heading" style="margin: 1rem 0 2rem 0;">
  <h3 id="faq-heading" style="margin-bottom: 0.85rem;">Core Reference Questions</h3>

  <details name="cac-faq" open style="background-color: #FFFFFF; color: #0B192C; border: 1.5px solid #0B192C; border-radius: 0.5rem; padding: 0.85rem 1.1rem; margin-bottom: 0.75rem;">
    <summary style="font-weight: 800; cursor: pointer; color: #0B192C; background-color: #FFFFFF;">What is Curriculum-as-Code (CaC)?</summary>
    <p style="margin-top: 0.65rem; margin-bottom: 0; color: #18181b; background-color: #FFFFFF;">
      Curriculum-as-Code (CaC) is an instructional engineering paradigm in which syllabi, readings, clinical simulations, rubrics, and compliance rules are authored in plain-text Markdown, version-controlled in Git, validated automatically by Continuous Integration (CI/CD) accessibility and accuracy linters, and compiled deterministically into Learning Management Systems (such as Canvas LMS via GraphQL) and open educational datasets.
    </p>
  </details>

  <details name="cac-faq" style="background-color: #FFFFFF; color: #0B192C; border: 1.5px solid #0B192C; border-radius: 0.5rem; padding: 0.85rem 1.1rem; margin-bottom: 0.75rem;">
    <summary style="font-weight: 800; cursor: pointer; color: #0B192C; background-color: #FFFFFF;">Who coined Curriculum-as-Code and how did it evolve from 2018 to 2026?</summary>
    <p style="margin-top: 0.65rem; margin-bottom: 0; color: #18181b; background-color: #FFFFFF;">
      The term first appeared in November 2018 at NRE Labs (<code>nre-learning/nrelabs-curriculum</code>) to provision Kubernetes-based network emulation labs, which later shut down due to heavy container runtime costs. Following early GitHub AI Co-Pilot plain-text strategy manuals (Alan Pruitt's August 2021 NADO Impact Award) and flat LaTeX/Markdown pipelines, Curriculum-as-Code evolved in 2026 under Alan Pruitt's <code>S-A-R v2.2</code> architecture into a neuro-symbolic higher-education system uniting DOM GraphRAG, W3C PROV-O provenance, ADA Title II <code>9:1</code> Compliance-as-Code, and air-gapped Sovereign Edge AI.
    </p>
  </details>

  <details name="cac-faq" style="background-color: #FFFFFF; color: #0B192C; border: 1.5px solid #0B192C; border-radius: 0.5rem; padding: 0.85rem 1.1rem; margin-bottom: 0.75rem;">
    <summary style="font-weight: 800; cursor: pointer; color: #0B192C; background-color: #FFFFFF;">How does Curriculum-as-Code differ from Docs-as-Code and STEM slide-generation scripts?</summary>
    <p style="margin-top: 0.65rem; margin-bottom: 0; color: #18181b; background-color: #FFFFFF;">
      Flat Docs-as-Code and LaTeX/Beamer slide scripts generate static reference pages or lecture slides without typed pedagogical relationships, LMS accessibility verification, or cryptographic audit trails. Modern Curriculum-as-Code (<code>S-A-R v2.2</code>) encodes Course Learning Outcomes, federal Single Sources of Truth, competency rubrics, bilingual W3C SKOS ontologies, <code>21/21</code> Achieve OER syndication packages, and W3C PROV-O grading provenance inside a unified semantic graph.
    </p>
  </details>

  <details name="cac-faq" style="background-color: #FFFFFF; color: #0B192C; border: 1.5px solid #0B192C; border-radius: 0.5rem; padding: 0.85rem 1.1rem;">
    <summary style="font-weight: 800; cursor: pointer; color: #0B192C; background-color: #FFFFFF;">How does Curriculum-as-Code enforce ADA Title II, WCAG 2.2 AA, and WCAG 3.0 compliance?</summary>
    <p style="margin-top: 0.65rem; margin-bottom: 0; color: #18181b; background-color: #FFFFFF;">
      Before any module reaches Canvas LMS or public web mirrors, automated pre-push CI/CD gates verify all 8 Canvas Course Accessibility Checker rules, enforce a strict <code>9:1</code> Double-Contrast Guard with explicit paired hex colors, validate table scopes and heading lengths (<code>&lt;= 120</code> characters), and require bilingual <em>In Plain English / En Palabras Sencillas</em> cognitive scaffolding.
    </p>
  </details>
</section>

---

<h2 id="academic-citation">6. Academic Citation &amp; Attribution</h2>

**APA 7th Edition:**  
Pruitt, A. (2026). *From infrastructure automation to clinical pedagogy: The origin and evolution of Curriculum-as-Code (2018–2026)* (S-A-R Architecture Whitepaper v2.2). Webcognita LLC. [https://alanpruitt.com/curriculum-as-code/](https://alanpruitt.com/curriculum-as-code/)

```bibtex
@techreport{pruitt2026cac,
  title       = {From Infrastructure Automation to Clinical Pedagogy: The Origin and Evolution of Curriculum-as-Code (2018--2026)},
  author      = {Pruitt, Alan},
  institution = {Webcognita LLC},
  number      = {S-A-R-v2.2-ORIGIN},
  year        = {2026},
  month       = {nov},
  url         = {https://alanpruitt.com/curriculum-as-code/},
  note        = {PDF: https://alanpruitt.com/docs/Curriculum-as-Code-Origin-and-Evolution-Whitepaper.pdf}
}
```

> **Disclaimer:** The Curriculum-as-Code architecture, S-A-R Standard, Clinical Framing Protocol, and open-source software tools described in this whitepaper represent independent faculty engineering and research through Webcognita LLC and do not represent official policy or endorsement by Arizona Western College or The University of Arizona.
