## Substack Distribution Package: Origin Whitepaper 00 (`Tech. Report S-A-R-v2.2-ORIGIN`)

- **Title:** From Infrastructure Automation to Clinical Pedagogy: The Origin and Evolution of Curriculum-as-Code (2018–2026)
- **Subtitle:** Tracing the three-generation genealogy of Curriculum-as-Code—from 2018 Kubernetes network labs and my 2021 GitHub AI Co-Pilot CEDS award to a neuro-symbolic S-A-R v2.2 academic operating system.
- **Suggested Substack Custom URL Slug:** `origin-and-evolution-of-curriculum-as-code`
- **Canonical Hub URL (Primary SERP Target):** `https://alanpruitt.com/curriculum-as-code/`
- **2-Page Archival Whitepaper PDF:** `https://alanpruitt.com/docs/Curriculum-as-Code-Origin-and-Evolution-Whitepaper.pdf`
- **Spanish Canonical Hub:** `https://alanpruitt.com/es/curriculum-as-code/`

---

> **Canonical Reference & 2-Page Archival PDF:** This Substack dispatch is the executive companion to **Webcognita LLC Technical Report `S-A-R-v2.2-ORIGIN`**. Read the full interactive reference specification (with complete comparative architecture tables, BibTeX citation, and bilingual Spanish mirror) at **[Curriculum-as-Code (CaC) Canonical Origin Hub (`alanpruitt.com/curriculum-as-code/`)](https://alanpruitt.com/curriculum-as-code/)** or download the **[2-Page Archival Whitepaper PDF](https://alanpruitt.com/docs/Curriculum-as-Code-Origin-and-Evolution-Whitepaper.pdf)**.

---

Whenever an engineering discipline crosses into mainstream vocabulary, its historical lineage tends to blur.

Over the past year, **"Curriculum-as-Code" (`CaC`)** has begun appearing in academic preprints, instructional design workshops, and workforce policy discussions. Yet almost none of those conversations connect how the term actually originated in cloud-native infrastructure engineering—or why early container-based and slide-compilation experiments stalled before reaching everyday community college and allied-health classrooms.

Today, I am publishing **[From Infrastructure Automation to Clinical Pedagogy: The Origin and Evolution of Curriculum-as-Code (2018–2026)](https://alanpruitt.com/curriculum-as-code/)** (`Technical Report S-A-R-v2.2-ORIGIN`) to establish a single, auditable historical genealogy and reference architecture across all three generations of the discipline.

---

### Generation 1 (2018–2020): Ephemeral Infrastructure Emulation (`NRE Labs` & Project Antidote)

The earliest explicit industrial formulation of **"Curriculum-as-Code"** emerged in **October 2018** through **Network Reliability Engineering (`NRE`) Labs** (`nrelabs-curriculum`), spearheaded by **Matt Oswalt** and cloud-native infrastructure engineers alongside **Project Antidote** ([`github.com/nre-learning/nrelabs-curriculum`](https://github.com/nre-learning/nrelabs-curriculum)).

At the time, network engineers were transitioning from manual command-line router configuration to Infrastructure-as-Code (`IaC`). Oswalt and his collaborators recognized that technical training suffered from the exact same configuration drift as data centers. Their breakthrough was storing lesson definitions, terminal verification scripts, and network topologies as plain-text code inside Git so Kubernetes could spin up live, browser-accessible virtual sandboxes on demand.

Generation 1 proved that educational environments could be version-controlled and peer-reviewed via pull requests. However, because every lesson spun up heavyweight virtual machines and Kubernetes pods, hosting costs were prohibitive and the paradigm remained confined to DevOps and network engineering bootcamps.

---

### Generation 2 (2021–2025): Plain-Text SSoTs, Pre-ChatGPT AI Co-Pilots & Flat Document Pipelines

Between 2021 and 2025, a second wave adapted Docs-as-Code pipelines (`Markdown`, `YAML`, `LaTeX`, `Pandoc`, and GitHub Actions) to compile static syllabi, lecture notes, and slide decks without Kubernetes overhead:

1. **August 2021 — Pre-ChatGPT GitHub AI Co-Pilot Governance:** More than a year before ChatGPT's public debut, during my 15-year executive tenure directing regional planning for the **Western Arizona Economic Development District (`WAEDD`, 2007–2022)**, I engineered a multi-county **Comprehensive Economic Development Strategy (`CEDS`)** manual using an early-stage open-source AI Co-Pilot model from a GitHub repository—earning the national **2021 NADO Aliceann Wohlbruck Impact Award**. That project proved that public-sector compliance and instructional manuals could be governed as modular, Git-tracked Single Sources of Truth (`SSoTs`).
2. **2023–August 2026 — Academic STEM Slide & Syllabus Compilers:** University Computer Science and STEM faculty—culminating in formal academic preprints such as Paiva's August 2026 *Curriculum-as-Code* (`arXiv:2608.07364`)—demonstrated `YAML` + `LaTeX/Beamer` pipelines that eliminated copy-paste drift between course syllabi and lecture slides.

Yet Generation 2 remained **structurally flat**. Compiling Markdown or LaTeX into PDF slides does not build a semantic knowledge graph, does not enforce federal civil-rights accessibility inside a live Learning Management System (`LMS`), does not protect first-generation students from unverified AI hallucinations, and does not respect FERPA privacy when cloud chatbots ingest student work.

---

### Generation 3 (2026–Present): `S-A-R v2.2` Neuro-Symbolic Pedagogy & Sovereign Edge AI

To cross the chasm from static document compilation to live higher-education execution, I independently engineered **Generation 3 (`S-A-R v2.2` — Scalable / Auditable / Repeatable)** through **Webcognita LLC (`SDVOSB`)**, field-tested across my five-course Exercise Science & Wellness (`EXW`) fleet (`EXW 101`, `EXW 150`, `EXW 210`, `EXW 245`, and `EXW 265`) at **Arizona Western College** and R1 applied Edge AI research at **The University of Arizona (School of Nutritional Sciences and Wellness — Yuma Campus)**.

Context dictates architecture. Arizona Western College is a rural borderland **Hispanic-Serving Institution (`HSI`)** where **77% of students are Latino** (`3.08x` the 25% federal Title V HSI threshold) and **62% are first-generation college students** (*"At AWC, 77% of students are Latino, and 62% are first-generation students. We serve this beautiful community, but challenge is everywhere,"* AWC President Dr. Reetika Dhawan, as quoted in *The Yuma Sun*, November 11, 2026).

In a community where structural financial, linguistic, shift-work, and connectivity barriers are everyday realities, commercial `$180` textbook access codes, `$20/month` cloud AI subscriptions, and post-production accessibility retrofits fail on arrival. Generation 3 solves six problems that Generation 1 and Generation 2 never addressed:

1. **Neuro-Symbolic `DOM GraphRAG` & `W3C PROV-O` Provenance:** Instead of flat Markdown files, my compiler parses all five courses into a **3,265-node Document Object Model (`DOM`) Knowledge Graph** paired with **`W3C PROV-O` SHA-256 cryptographic provenance receipts**, syncing deterministically to Instructure Canvas via a **Canvas GraphQL-first (`POST /api/graphql`)** pipeline (`Write Once -> Push Many`).
2. **Compliance-as-Code (`ADA Title II`, `9:1` Double-Contrast Guard & `WCAG 3.0`):** Pre-commit and pre-push linters programmatically enforce all **8 Canvas Course Accessibility Checker rules** (`0 Open Issues` across 419+ HTML files), a strict **`9:1` contrast ratio** (doubling WCAG 2.2 AA's `4.5:1` baseline for `100,000+ lux` Sonoran Desert glare), and **WCAG 3.0** *In Plain English* + **`W3C SKOS` Norteño-Spanish** callouts.
3. **U.S. DOL ETA Advisory TEN No. 07-25 & The Clinical Framing Protocol (`Pattern / Rule / Solve`):** Every module operationalizes all **5 Foundational AI Content Areas** and **7 Community College Delivery Design Principles** of **U.S. DOL TEN No. 07-25** (February 13, 2026). Under **The Centaur Protocol**, students act as **Clinical Architects / Problem Framers** using structured `P-T-C-F` prompts with triple-hash (`###`) case-data isolation, auditing AI outputs against federal Single Sources of Truth (**PAGA 2018 2nd Ed.**, **2025–2030 Dietary Guidelines for Americans ["Real Food" Focus]**, **ACSM 12th Ed.**, and **NASM OPT**), calibrating browser-native simulators on [`exwtoolkit.com`](https://exwtoolkit.com) and [`paga2018.dev`](https://paga2018.dev), and defending clinical priorities in a **150-word Active Verification** in their own voice on the **10-7-0 Mastery Scale**.
4. **Air-Gapped Sovereign Edge AI (`AI-AWARE` -> `AI-READY`):** Rather than routing student data to commercial clouds, instructional auditing runs locally on air-gapped **Apple Silicon (`M1` / `M2`)** workstations via Ollama (`exw-carbon4-cac:latest` / open-weight **Google Gemini Carbon 4** and **Gemma 4**), guaranteeing `100%` FERPA, HIPAA, and OPSEC sovereignty at `$0.00` recurring token cost.
5. **Dual-Namespace (`EXW -> KIN / HLTH`) `$0 ZTC` OER & K–16 Dual-Enrollment Syndication:** A single JSON standards registry ([`educational_alignment_registry.json`](https://alanpruitt.com/institutional-infrastructure/)) compiles SHA-256 checksummed OER packages (`KIN-101`, `HLTH-150`, `KIN-210`, `KIN-245`, `KIN-265`) with 4-Tier `Schema.org/Dataset` and `LRMI educationalAlignment` metadata—bridging K–12 Dual-Enrollment (`CCSS` / `WA.ELA`) and HLC collegiate transfer syllabi with zero accreditation collision.
6. **Non-Competing 50-State Enabling Resource (`NSF TechAccess: AI-Ready America`):** Through **Webcognita LLC** (`SDVOSB / VOSB` • `SAM.gov UEI: EZ34U9KNJA17` • `CAGE: 4ZCN6` • `Primary NAICS: 541511`), I never compete against community colleges, universities, or state consortia for primary NSF grant awards—serving strictly as a turnkey open reference architecture and subaward implementation partner across all 50 states.

---

### Read & Cite the Canonical Origin Whitepaper

- **Interactive Canonical Reference Hub (`EN`):** [Curriculum-as-Code (CaC): Origin Story, Historical Genealogy (2018–2026) & S-A-R v2.2 Reference Architecture (`alanpruitt.com/curriculum-as-code/`)](https://alanpruitt.com/curriculum-as-code/)
- **Download the 2-Page Archival PDF (`533.8 KB`):** [Curriculum-as-Code-Origin-and-Evolution-Whitepaper.pdf](https://alanpruitt.com/docs/Curriculum-as-Code-Origin-and-Evolution-Whitepaper.pdf)
- **Spanish Canonical Hub (`ES`):** [Currículo-como-Código (CaC): Historia de Origen y Arquitectura S-A-R v2.2 (`alanpruitt.com/es/curriculum-as-code/`)](https://alanpruitt.com/es/curriculum-as-code/)
- **Live Master Research Log Observatory (`92` Entries):** [alanpruitt.com/research-log/](https://alanpruitt.com/research-log/)
- **Federal Capabilities Statement (`Webcognita LLC`):** [webcognita.com/capabilities-statement.html](https://www.webcognita.com/capabilities-statement.html)

**APA 7th Citation:**  
Pruitt, A. (2026). *From infrastructure automation to clinical pedagogy: The origin and evolution of Curriculum-as-Code (2018–2026)* (S-A-R Architecture Whitepaper v2.2, Tech. Report S-A-R-v2.2-ORIGIN). Webcognita LLC. [https://alanpruitt.com/curriculum-as-code/](https://alanpruitt.com/curriculum-as-code/)

---

### How I Made This

- **Concept & Historical Genealogy:** Synthesized from primary open-source repository commits (`nrelabs-curriculum`, 2018), NADO award records (August 2021), STEM CaC preprints (2026), and multi-semester production telemetry across the EXW Master Library (`S-A-R v2.2`).
- **Drafting & Compilation:** Authored in deterministic Markdown and compiled simultaneously to Hugo HTML (`JSON-LD DefinedTerm + TechArticle + Google Scholar Highwire tags`) and a 2-page print-calibrated PDF.
- **Verification:** Local AI tools assisted with syntax linting and accessibility checks (`0` POUR / WCAG 2.2 AA `9:1` / Markdownlint errors). Every historical citation, demographic statistic, and architectural claim was manually verified by a human author prior to publication.

> **Disclaimer:** The Curriculum-as-Code architecture, S-A-R Standard, Clinical Framing Protocol, and open-source software tools described in this publication represent my independent faculty engineering and research through Webcognita LLC and do not represent official policy or endorsement by Arizona Western College or The University of Arizona.
