# Substack Distribution Package: Essay 38

- **Title:** Essay 38: What If I Didn't Build the Graph? – Why Curriculum-as-Code Transcends Flat Docs-as-Code with DOM GraphRAG & W3C PROV-O
- **Subtitle:** How I engineered DOM GraphRAG, W3C PROV-O cryptographic receipts, Born-Accessible 9:1 XAI scorecards, and W3C SKOS Norteño-Spanish ontologies on air-gapped Apple Silicon.
- **Canonical URL:** `https://alanpruitt.com/essays/essay-38-dom-graphrag-and-prov-o-curriculum-as-code/`
- **Architecture Briefs Shelf:** `https://alanpruitt.com/#architecture-briefs`

---

When I first engineered a **Git-versioned Markdown repository** with **automated CI/CD workflows** to manage my multi-course exercise science and clinical nutrition fleet (`EXW 101`, `EXW 150`, `EXW 210`, `EXW 245`, and `EXW 265`), I could have stopped at standard *Docs-as-Code*.

I already had clean Markdown source files, automated **Canvas GraphQL** synchronization, and a local vector index over **3,151 curriculum chunks**. By conventional software documentation standards, my pipeline was finished.

Every time a system I build reaches baseline maturity, however, I pressure-test it against the same guiding counterfactual:

**What if I didn't build the graph?**

What if I treated a clinical kinesiology and nutrition curriculum like a flat software manual—slicing pages into isolated 500-token chunks, retrieving them by raw cosine similarity, returning opaque AI confidence numbers to students, and assuming English-only terminology would magically serve the bilingual **Hispanic-Serving Institution (HSI)** students I teach along the **Yuma, AZ / Imperial Valley, CA** borderland?

The answer is clear: flat *Docs-as-Code* without structural pedagogy and cryptographic provenance eventually collapses back into probabilistic guesswork.

---

### Anatomy of the Flat-Vector Trap

Higher education—especially clinical exercise physiology and nutrition governed by non-negotiable **Federal Single Sources of Truth** (**PAGA 2nd Ed. 2018**, **2025–2030 Dietary Guidelines for Americans**, **ACSM 12th Ed.**, and the **NASM OPT Model**)—operates under strict safety gates. Leaving a Retrieval-Augmented Generation (RAG) pipeline flat creates four structural fault lines:

1. **Context-Blind Retrieval (Orphaned Clinical Rules):** When I slice a Markdown module into flat chunks, a contraindication table loses its relationship to the Module's **Course Learning Outcomes (CLOs)**, its Required Reading foundation, and its parent phase inside **The Clinical Framing Protocol (`Pattern / Rule / Solve`)**.
2. **Unverifiable AI Synthesis (Zero Lineage):** Without a machine-readable provenance graph, neither the student nor an auditor can prove *which* exact Federal SSoT revision, Git commit, or local model produced the recommendation.
3. **The Black-Box Score Fallacy:** Handing a student a single opaque similarity percentage (`84% Match`) tells them nothing about *why* their clinical reasoning succeeded or where their safety gate failed.
4. **The Bilingual Vocabulary Gap:** When a first-generation student in Yuma or San Luis Río Colorado describes heat exhaustion in authentic **Norteño-Spanish** (*"se le bajó la presión y anda bien mareado en el calorón de Yuma"*), a flat English vector index misses the exact clinical mapping to **exertional heat illness**, **orthostatic hypotension**, and **WBGT > 82°F fluid replacement gates**.

---

### Engineering the Upgrade: Four Pillars of S-A-R v2.2

Drawing on my experience as an **Adjunct Faculty member of Exercise Science & Wellness at Arizona Western College**, a **Generative AI Strategist at The University of Arizona**, and **Principal of Webcognita LLC (VOSB)**, I independently designed the **S-A-R Standard (Scalable / Auditable / Repeatable)** so that I can close every architectural gap deterministically across my **scalable $0 ZTC Open Educational Resource (OER) course fleet**.

Instead of settling for flat *Docs-as-Code*, I upgraded my **EXW Master Library (`v2.2`)** with four open-standard semantic layers running on **air-gapped Google Gemini Argon 4 models locally on my Apple Silicon (M1/M2) workstations for 100% FERPA privacy**:

1. **DOM GraphRAG (Structural Pedagogical Graph):** I enriched every one of my **3,151 curriculum vectors** with a `dom_graph_node` payload containing its `dom_path` (`h2 > h3` hierarchy), its governing role inside **The Clinical Framing Protocol (`Pattern / Rule / Solve`)**, its **Course Learning Outcome (`CLO`)** alignment, and directed `graph_edges` (`parent_module`, `requires_reading`, `grounds_lab`, `grounds_discussion`, and `governed_by_ssot`).
2. **W3C PROV-O Cryptographic Provenance Receipts:** Every live **Sovereign AI Auditing** response returned by my local API emits a formal **W3C PROV-O (`http://www.w3.org/ns/prov#`)** JSON-LD provenance graph (`prov_o_receipt`) alongside a deterministic SHA-256 `receipt_id` linking `prov:Entity` (Federal SSoT), `prov:Activity` (Clinical Audit Synthesis), and `prov:Agent` (Local Apple Silicon Argon 4 Auditor).
3. **Born-Accessible (`9:1` Contrast) 4-Dimensional XAI Radar Scorecard:** Under my **ADA Title II & Atomic WCAG 2.2 AA / 3.0 Higher Ed Architecture**, I replaced single-number confidence scores inside the live Canvas Clinical Auditor Modal with a **4-Dimensional Explainable AI (XAI) Radar Scorecard** (`Pattern 25%` / `Rule 25%` / `Solve 25%` / `Active Verification 25%`) engineered to my strict **9:1 Double-Contrast Guard**.
4. **W3C SKOS / Schema.org Bilingual Clinical Controlled Vocabulary:** To deliver **bilingual "In Plain English" OER across borderland HSI communities**, my **W3C SKOS** and **Schema.org (`MedicalEntity`)** ontology maps colloquial **Norteño-Spanish** clinical expressions (`skos:altLabel @es-MX-Norteno`) to English and Spanish clinical terms (`skos:prefLabel`) and federal SSoT rules—lifting top clinical RAG retrieval similarity from `0.7743` to **`0.8236`**.

---

### Slow is Smooth, Smooth is Fast

*What if I didn't build the graph?*

Without **DOM GraphRAG**, **W3C PROV-O**, **Born-Accessible 9:1 XAI**, and **W3C SKOS bilingual ontologies**, a course repository is just a static folder of text waiting to be summarized by commercial chatbots. By binding every paragraph, bilingual clinical term, and AI audit receipt into an auditable semantic graph, my **Curriculum-as-Code** architecture simultaneously defends academic rigor, guarantees **100% FERPA privacy**, and expands equitable access across my borderland classrooms.

*(Disclaimer: The Curriculum-as-Code architecture, S-A-R Standard, and open-source software tools described in this article represent my independent faculty engineering and research through Webcognita LLC and do not represent official policy or endorsement by Arizona Western College or The University of Arizona.)*

- **Read the canonical essay on alanpruitt.com:** [Essay 38: What If I Didn't Build the Graph?](https://alanpruitt.com/essays/essay-38-dom-graphrag-and-prov-o-curriculum-as-code/)
- **Download my 6-Publication Architecture Briefs & Project Horizon White Papers:** [alanpruitt.com/#architecture-briefs](https://alanpruitt.com/#architecture-briefs)

---

### How I Made This
- **Concept & Framework:** Researched and structured as part of the Curriculum-as-Code initiative, anchored in authoritative federal and clinical Single Sources of Truth.
- **Drafting & Execution:** Built using local Markdown source files and static site generators.
- **Verification:** Local AI tools assisted with syntax formatting and linting. A human expert manually audited and verified every claim and pedagogical framework before publication.
