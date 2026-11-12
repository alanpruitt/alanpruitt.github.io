#!/usr/bin/env python3
"""
S-A-R v2.2 Hybrid Distilled Q&A Index Compiler for alanpruitt.com
Unites:
  1. Downloadable Architecture Briefs & White Papers (01-07)
  2. Distilled DOM GraphRAG Executive Q&A Nodes (US DOL TEN 07-25, Course 42051, PWAs, Food Informatics)
  3. Master Research Log (All 90 Longitudinal Entries from MASTER_RESEARCH_LOG_CAC_CAAS.md)
  4. Curriculum-as-Code Essays (Essays 01-40)
Outputs:
  - /Users/alanpruitt/alanpruitt.github.io/static/data/sovereign-qa-index.json
  - /Users/alanpruitt/alanpruitt.github.io/data/sovereign-qa-index.json
"""

import hashlib
import json
import re
from pathlib import Path

SITE_ROOT = Path("/Users/alanpruitt/alanpruitt.github.io")
EXW_ROOT = Path("/Users/alanpruitt/EXW-MASTER-LIBRARY")
RESEARCH_LOG_MD = EXW_ROOT / "00_GOVERNANCE" / "MASTER_RESEARCH_LOG_CAC_CAAS.md"
LLMS_TXT = SITE_ROOT / "static" / "llms.txt"


def sha12(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]


def build_curated_executive_nodes():
    return [
        # --- 1. U.S. DOL ETA ADVISORY TEN NO. 07-25 ---
        {
            "id": "qa-dol-ten-07-25-overview",
            "category": "dol-ten-07-25",
            "badge": "US DOL TEN No. 07-25 • Voluntary Framework",
            "dom_path": "Sovereign Spine > Mandate / System / Proof > TEN 07-25 Crosswalk",
            "title_en": "How does Alan Pruitt operationalize U.S. DOL ETA Advisory TEN No. 07-25 (Feb 13, 2026)?",
            "title_es": "¿Cómo operacionaliza Alan Pruitt el Aviso U.S. DOL ETA TEN No. 07-25 (13 de feb. de 2026)?",
            "answer_en": (
                "In plain English: U.S. Department of Labor (DOL) Employment and Training Administration (ETA) "
                "Training and Employment Notice (TEN) No. 07-25 (issued February 13, 2026) is a voluntary federal "
                "workforce and community college AI Literacy Framework—not a punitive statutory mandate. Across all "
                "10 EXW courses at Arizona Western College, we proactively map all 5 Foundational Content Areas "
                "(1. Understand AI Principles, 2. Explore AI Uses, 3. Direct AI Effectively, 4. Evaluate Outputs, "
                "5. Use AI Responsibly) and all 7 Community College Delivery Design Principles (1. Experiential Learning, "
                "2. Embedded Context, 3. Complementary Human Skills, 4. $0 ZTC Prerequisite & Equitable Access, "
                "5. Continued Learning Pathways, 6. Enabling Faculty Roles, 7. Agile Design) directly into Sovereign CaC's "
                "Sovereign Spine (Mandate -> System -> Proof) and the Four-Part Submission Standard."
            ),
            "answer_es": (
                "En palabras sencillas: El aviso U.S. Department of Labor (DOL) ETA TEN No. 07-25 (emitido el 13 de "
                "febrero de 2026) es un marco federal voluntario para colegios comunitarios y desarrollo laboral. En "
                "los 10 cursos de la flota EXW en AWC, integramos de forma proactiva sus 5 Áreas de Contenido Fundamental "
                "y sus 7 Principios de Diseño de Entrega dentro del arquitectura soberana de tres etapas (Mandato -> Sistema -> Evidencia) "
                "y el estándar de evaluación clínica de 4 partes."
            ),
            "keywords": "dol ten 07-25 07 25 department of labor eta training and employment notice ai literacy framework voluntary 5 foundational content areas 7 delivery principles community college wioa workforce",
            "links": [
                {"label_en": "Live EXW-Demo TEN 07-25 Crosswalk (Course 42051)", "label_es": "Cruce en Vivo EXW-Demo (Curso 42051)", "url": "https://azwestern.instructure.com/courses/42051/pages/exw-demo-coach-alan-the-exw-ai-landscape-institutional-alignment-and-literacy"},
                {"label_en": "Official U.S. DOL Advisory TEN 07-25 (.gov)", "label_es": "Aviso Oficial U.S. DOL TEN 07-25 (.gov)", "url": "https://www.dol.gov/agencies/eta/advisories/ten-07-25"},
                {"label_en": "Bento Architecture Card (#dol-ten-07-25-framework)", "label_es": "Tarjeta de Arquitectura (#dol-ten-07-25-framework)", "url": "/#dol-ten-07-25-framework"},
            ],
        },
        # --- 2. DOWNLOADABLE BRIEFS & WHITE PAPERS (01-07) ---
        {
            "id": "brief-01-dom-graphrag-prov-o",
            "category": "briefs",
            "badge": "BRIEF 01 • PDF White Paper (91 KB)",
            "dom_path": "Architecture Briefs > Brief 01 > DOM GraphRAG & W3C PROV-O",
            "title_en": "Brief 01: Sovereign Clinical AI, DOM GraphRAG & W3C PROV-O Architecture Brief (S-A-R v2.2)",
            "title_es": "Informe 01: Arquitectura de IA Clínica Soberana, DOM GraphRAG y W3C PROV-O (S-A-R v2.2)",
            "answer_en": (
                "In plain English: Brief 01 explains how Curriculum-as-Code transcends flat Docs-as-Code by indexing "
                "3,265 pedagogical graph nodes (3,151 curriculum vectors + 114 platform/governance nodes) enriched with "
                "DOM hierarchy paths (h2 > h3), clinical_framing_role (Pattern / Rule / Solve), CLO outcome mappings, "
                "W3C SKOS bilingual Norteño-Spanish clinical concepts, and cryptographic W3C PROV-O JSON-LD audit receipts "
                "generated locally on Apple Silicon M1/M2 hardware."
            ),
            "answer_es": (
                "En palabras sencillas: El Informe 01 detalla cómo Currículo-como-Código supera a Docs-as-Code mediante "
                "3,265 nodos en un grafo de conocimiento DOM GraphRAG enriquecido con rutas jerárquicas (h2 > h3), "
                "encuadre clínico (Patrón / Regla / Solución), ontologías bilingües W3C SKOS y recibos criptográficos "
                "W3C PROV-O ejecutados localmente en Apple Silicon M1/M2."
            ),
            "keywords": "brief 01 white paper dom graphrag w3c prov-o prov-o cryptographic provenance receipts 3265 3151 vectors s-a-r v2.2 rag knowledge graph",
            "links": [
                {"label_en": "Download Brief 01 (PDF)", "label_es": "Descargar Informe 01 (PDF)", "url": "/docs/EXW_S_A_R_v2_2_DOM_GraphRAG_and_PROV_O_Architecture_Brief.pdf"},
                {"label_en": "Read Essay 38 (DOM GraphRAG & W3C PROV-O)", "label_es": "Leer Ensayo 38 (DOM GraphRAG y W3C PROV-O)", "url": "/essays/essay-38-dom-graphrag-and-prov-o-curriculum-as-code/"},
            ],
        },
        {
            "id": "brief-02-lab-manual",
            "category": "briefs",
            "badge": "MANUAL 02 • PDF Lab Manual (121 KB)",
            "dom_path": "Architecture Briefs > Manual 02 > EXW Course Fleet Laboratory Manual",
            "title_en": "Manual 02: EXW Course Fleet Laboratory Manual (v2.2 — Pattern / Rule / Solve & exwtoolkit.com)",
            "title_es": "Manual 02: Manual de Laboratorio de la Flota de Cursos EXW (v2.2 — Patrón / Regla / Solución)",
            "answer_en": (
                "In plain English: Manual 02 is the applied field and laboratory methods manual across EXW 101, 150, 210, "
                "245, and 265. It operationalizes the 9-Box exwtoolkit.com Clinical Biometrics & Desert Heat-Stress Workbench, "
                "the Pattern / Rule / Solve Clinical Framing Protocol, triple-hash (###) case delimiter protocols, and the "
                "Four-Part Submission Standard graded on the 10-7-0 Mastery Scale."
            ),
            "answer_es": (
                "En palabras sencillas: El Manual 02 documenta los métodos de laboratorio aplicados en EXW 101, 150, 210, "
                "245 y 265 utilizando exwtoolkit.com, el protocolo Patrón / Regla / Solución, delimitadores (###) y la "
                "escala de dominio 10-7-0."
            ),
            "keywords": "manual 02 laboratory manual exwtoolkit.com 9-box clinical biometrics desert heat stress yuma pattern rule solve 10-7-0 mastery scale",
            "links": [
                {"label_en": "Download Manual 02 (PDF)", "label_es": "Descargar Manual 02 (PDF)", "url": "/docs/EXW_Course_Fleet_Laboratory_Manual_v2_2.pdf"},
                {"label_en": "Launch exwtoolkit.com", "label_es": "Abrir exwtoolkit.com", "url": "https://exwtoolkit.com"},
            ],
        },
        {
            "id": "brief-03-novel-100-level-portfolio",
            "category": "briefs",
            "badge": "PORTFOLIO 03 • PDF Proposals (90 KB)",
            "dom_path": "Architecture Briefs > Portfolio 03 > AWC WPE Novel 100-Level OER Courses",
            "title_en": "Portfolio 03: AWC WPE Novel 100-Level Curriculum Proposal Portfolio ($0 ZTC OER)",
            "title_es": "Portafolio 03: Propuestas Curriculares Nivel 100 para AWC WPE ($0 ZTC OER)",
            "answer_en": (
                "In plain English: Portfolio 03 contains complete ACRES institutional forms and 16-Module Curriculum-as-Code "
                "blueprints for 5 zero-prerequisite, $0 ZTC OER transfer courses designed for Arizona Western College: "
                "EXW 110 (Foundations of Tactical & Occupational Readiness), EXW 120 (Desert Heat Physiology & Hydration), "
                "EXW 130 (Movement Longevity & Healthy Aging), EXW 140 (Culinary Medicine & Real-Food Performance), and "
                "EXW 160 (AI Literacy & Digital Biometrics in Health)."
            ),
            "answer_es": (
                "En palabras sencillas: El Portafolio 03 presenta propuestas completas ACRES y planes de 16 módulos ($0 ZTC OER) "
                "para 5 nuevos cursos transferibles de nivel 100 en AWC (EXW 110, EXW 120, EXW 130, EXW 140 y EXW 160)."
            ),
            "keywords": "portfolio 03 novel 100-level curriculum proposal acres exw 110 120 130 140 160 ztc oer transfer courses arizona western college",
            "links": [
                {"label_en": "Download Portfolio 03 (PDF)", "label_es": "Descargar Portafolio 03 (PDF)", "url": "/docs/AWC_WPE_Novel_100_Level_Curriculum_Proposal_Portfolio.pdf"},
            ],
        },
        {
            "id": "brief-04-project-horizon-grant",
            "category": "briefs",
            "badge": "BRIEF 04 • Executive Grant Brief (92 KB)",
            "dom_path": "Architecture Briefs > Brief 04 > Project Horizon Innovation Fund Grant",
            "title_en": "Brief 04: Project Horizon — 2026 AWC Innovation Fund Executive Grant Brief ($8,850 One-Time / $0 Recurring)",
            "title_es": "Informe 04: Proyecto Horizon — Propuesta Ejecutiva Fondo de Innovación AWC 2026 ($8,850)",
            "answer_en": (
                "In plain English: Brief 04 is the executive grant proposal ($8,850 one-time hardware investment, $0.00 "
                "recurring SaaS cost) and 100-Point Rubric Matrix establishing an air-gapped ADA Title II, WCAG 2.2 AA (9:1), "
                "and WCAG 3.0 APCA optical telemetry testbed at Arizona Western College."
            ),
            "answer_es": (
                "En palabras sencillas: El Informe 04 es la propuesta ejecutiva ($8,850 de inversión única y $0 en costos "
                "recurrentes SaaS) para establecer un laboratorio aislado (air-gapped) de pruebas ópticas ADA Título II y "
                "WCAG 3.0 APCA en AWC."
            ),
            "keywords": "brief 04 project horizon innovation fund grant 8850 ada title ii wcag 3.0 apca testbed zero recurring saas",
            "links": [
                {"label_en": "Download Brief 04 (PDF)", "label_es": "Descargar Informe 04 (PDF)", "url": "/docs/AWC_2026_Innovation_Fund_Project_Horizon_Executive_Memo.pdf"},
            ],
        },
        {
            "id": "brief-05-wcag3-apca-norteno",
            "category": "briefs",
            "badge": "WHITE PAPER 05 • Optical & Screen-Reader R&D (78 KB)",
            "dom_path": "Architecture Briefs > White Paper 05 > WCAG 3.0 APCA & Norteño Phonetics",
            "title_en": "White Paper 05: WCAG 3.0 APCA (100,000+ Lux Desert Sunlight) & Norteño-Spanish Screen-Reader Linting",
            "title_es": "Documento Técnico 05: WCAG 3.0 APCA (100,000+ Lux) y Lector de Pantalla en Español Norteño",
            "answer_en": (
                "In plain English: White Paper 05 details the optical and linguistic R&D methodology benchmarking "
                "Bronze/Silver/Gold WCAG 3.0 APCA perceptual contrast (Lc >= 90) and our 9:1 Double-Contrast Guard under "
                "100,000+ lux Yuma desert sunlight, alongside W3C SKOS Norteño-Spanish .imscc screen-reader phonetic linting "
                "(preventing English TTS engines from mangling Spanish clinical terminology)."
            ),
            "answer_es": (
                "En palabras sencillas: El Documento Técnico 05 presenta la metodología óptica y lingüística que valida "
                "el contraste perceptual WCAG 3.0 APCA y la guardia 9:1 bajo 100,000+ lux de sol en el desierto de Yuma, "
                "junto con la verificación fonética para lectores de pantalla en español norteño."
            ),
            "keywords": "white paper 05 wcag 3.0 apca 100000 lux desert sunlight norteno spanish screen reader linting w3c skos",
            "links": [
                {"label_en": "Download White Paper 05 (PDF)", "label_es": "Descargar Documento 05 (PDF)", "url": "/docs/Project_Horizon_WCAG3_APCA_and_Norteno_ScreenReader_White_Paper.pdf"},
                {"label_en": "Read Essay 37 (WCAG 3.0 Cognitive Accessibility)", "label_es": "Leer Ensayo 37 (Accesibilidad Cognitiva WCAG 3.0)", "url": "/essays/essay-37-wcag-3-cognitive-accessibility/"},
            ],
        },
        {
            "id": "brief-06-edge-testbed-specs",
            "category": "briefs",
            "badge": "SPEC 06 • Hardware & Telemetry Spec (90 KB)",
            "dom_path": "Architecture Briefs > Spec 06 > Air-Gapped Edge Testbed",
            "title_en": "Spec 06: Air-Gapped Edge Testbed & Optical Telemetry Hardware Specifications",
            "title_es": "Especificación 06: Banco de Pruebas Air-Gapped y Telemetría Óptica",
            "answer_en": (
                "In plain English: Spec 06 provides vendor-agnostic engineering specifications for the 16-Core / 64GB DDR5 / "
                "16GB VRAM air-gapped workstation, dual factory-calibrated 27-inch 4K reference displays, multi-tier mobile "
                "viewport sandbox, and 100,000+ lux digital photometer."
            ),
            "answer_es": (
                "En palabras sencillas: La Especificación 06 define el hardware agnóstico de proveedor para la estación de "
                "trabajo aislada (air-gapped), monitores de referencia 4K calibrados y fotómetro de 100,000+ lux."
            ),
            "keywords": "spec 06 hardware specifications air-gapped edge testbed photometer 4k reference display",
            "links": [
                {"label_en": "Download Spec 06 (PDF)", "label_es": "Descargar Especificación 06 (PDF)", "url": "/docs/Project_Horizon_Vendor-agnostic_Technical_Specs.pdf"},
            ],
        },
        {
            "id": "brief-07-master-research-log-compendium",
            "category": "briefs",
            "badge": "COMPENDIUM 07 • Live Observatory + PDF (1.28 MB)",
            "dom_path": "Architecture Briefs > Compendium 07 > Master Research Log (90 Entries)",
            "title_en": "Compendium 07: Master Research Log — Curriculum as Code (CaC), CaaS & Compliance as Code (May–Nov 2026)",
            "title_es": "Compendio 07: Bitácora Maestra de Investigación — CaC, CaaS y Compliance as Code (Mayo–Nov 2026)",
            "answer_en": (
                "In plain English: Compendium 07 is Alan Pruitt's continuous longitudinal engineering dataset containing "
                "90 dated technical analyses, 35+ ASCII dataflow pipelines, and 32 Instructional Design Role Evolution "
                "archetypes tracking Google Workspace (Gemini 3.5, NotebookLM, Workspace Studio, Google Vids), Instructure "
                "Canvas LMS (GraphQL /api/graphql, New Quizzes Jan 2027 Mandate, LTI 1.3), U.S. DOL TEN No. 07-25, and "
                "sovereign Compliance-as-Code verification."
            ),
            "answer_es": (
                "En palabras sencillas: El Compendio 07 reúne 90 análisis técnicos fechados (mayo a noviembre de 2026), "
                "más de 35 diagramas de arquitectura y 32 arquetipos de evolución del diseño instruccional sobre Google "
                "Workspace, Canvas LMS GraphQL, U.S. DOL TEN No. 07-25 y cumplimiento como código."
            ),
            "keywords": "compendium 07 master research log 90 entries 89 entries 91 entries longitudinal dataset google workspace gemini canvas graphql new quizzes",
            "links": [
                {"label_en": "Launch Live Research Log Observatory", "label_es": "Abrir Observatorio en Vivo de la Bitácora", "url": "/research-log/"},
                {"label_en": "Download Compendium 07 (PDF)", "label_es": "Descargar Compendio 07 (PDF)", "url": "/docs/CaC_and_CaaS_Master_Research_Log_2026_Compendium.pdf"},
            ],
        },
        # --- 3. DISTILLED DOM GRAPHRAG & ARCHITECTURE Q&A NODES ---
        {
            "id": "qa-golden-circle-clinical-framing",
            "category": "dom-graphrag",
            "badge": "DOM GraphRAG • Sovereign Spine & Pedagogy",
            "dom_path": "Course 42051 > Sovereign Spine (Mandate -> System -> Proof) > Pattern / Rule / Solve",
            "title_en": "How do Sovereign Three-Stage Architecture (Mandate -> System -> Proof) and Pattern / Rule / Solve work together?",
            "title_es": "¿Cómo funcionan juntos el arquitectura soberana de tres etapas (Mandato -> Sistema -> Evidencia) y Patrón / Regla / Solución?",
            "answer_en": (
                "In plain English: Every module across the 10-course EXW fleet is sequenced from the inside out using "
                "Simon Sovereign Three-Stage Sequencing: (1) THE WHY establishes purpose, civil-rights equity ($0 ZTC, WCAG 2.2 AA 9:1), "
                "and clinical foundations; (2) THE HOW equips students with the Clinical Framing Protocol (Pattern: diagnose "
                "the client & Yuma environmental stressors -> Rule: apply federal SSoT benchmarks like PAGA 2018, DGA 2025-2030, "
                "ACSM 12th Ed., or NASM OPT -> Solve: prescribe & audit the intervention); and (3) THE WHAT executes the "
                "Four-Part Submission Standard, exwtoolkit.com simulation tokens, and 256 10/10 Exemplar Solves."
            ),
            "answer_es": (
                "En palabras sencillas: Cada módulo de la flota EXW se secuencia de adentro hacia afuera con el Círculo "
                "Dorado de Sovereign CaC (Mandato -> Sistema -> Evidencia) y el Protocolo de Encuadre Clínico (Patrón / Regla / Solución), "
                "entrenando al estudiante como Arquitecto Clínico y a la IA como calculadora subordinada."
            ),
            "keywords": "sovereign spine mandate system proof institutional pattern rule solve patron regla solucion clinical framing protocol centaur",
            "links": [
                {"label_en": "Inspect EXW-Demo Sovereign 3-Stage Spine Modules (Course 42051)", "label_es": "Inspeccionar Módulos del Arquitectura Soberana (Curso 42051)", "url": "https://azwestern.instructure.com/courses/42051/modules"},
                {"label_en": "Workshops & 4-Stop Tour", "label_es": "Portal de Talleres y Recorrido en 4 Puntos", "url": "/workshops/"},
            ],
        },
        {
            "id": "qa-air-gapped-m1-m2-ferpa",
            "category": "dom-graphrag",
            "badge": "DOM GraphRAG • Sovereign Edge AI",
            "dom_path": "Course 42051 > Ring 2: THE HOW > Local Apple Silicon M1/M2 & Carbon 4",
            "title_en": "What does Air-Gapped Apple Silicon M1/M2 Ollama (Carbon 4) mean for FERPA privacy and $0 ZTC cost?",
            "title_es": "¿Qué significa el sistema aislado (Air-Gapped) Apple Silicon M1/M2 con Carbon 4 para FERPA y costo $0?",
            "answer_en": (
                "In plain English: Instead of sending student submissions or curriculum data to commercial cloud AI APIs, "
                "our instructional grading and auditing pipeline runs offline on local Apple Silicon hardware (M1 Interactive "
                "Antigravity IDE Cockpit + M2 Unattended 7:00 AM MST Daemon running 9.5 GB open-weight Ollama models "
                "exw-carbon4-cac:latest and exw-gemma4:latest). Student PII never leaves the local machine, guaranteeing "
                "100% FERPA compliance with $0 SaaS fees and $0 token costs."
            ),
            "answer_es": (
                "En palabras sencillas: En lugar de enviar datos estudiantiles a la nube, ejecutamos los modelos abiertos "
                "Google Gemini Carbon 4 localmente en estaciones Apple Silicon M1 y M2 aisladas de internet. Los datos nunca "
                "tocan servidores externos, garantizando privacidad FERPA al 100% y cero costos de suscripción o tokens."
            ),
            "keywords": "air-gapped air gapped apple silicon m1 m2 ollama argon 4 gemma ferpa privacy zero trust $0 ztc local ai",
            "links": [
                {"label_en": "Explore Workshops & Air-Gapped Architecture", "label_es": "Explorar Talleres y Arquitectura Air-Gapped", "url": "/workshops/"},
                {"label_en": "Inspect Local AI Governance in EXW-Demo", "label_es": "Inspeccionar Gobernanza de IA Local en EXW-Demo", "url": "https://azwestern.instructure.com/courses/42051/pages/exw-demo-coach-alan-local-ai-governance-ollama-modelfiles-and-yaml-frontmatter-architecture"},
            ],
        },
        {
            "id": "qa-ada-title-ii-wcag-9-1",
            "category": "dom-graphrag",
            "badge": "DOM GraphRAG • Accessibility & Civil Rights",
            "dom_path": "Course 42051 > Ring 1: THE WHY > WCAG 2.2 AA (9:1) & ADA Title II",
            "title_en": "How does the 9:1 Double-Contrast Guard enforce ADA Title II, WCAG 2.2 AA, and WCAG 3.0 Cognitive Accessibility?",
            "title_es": "¿Cómo garantiza la Guardia de Doble Contraste 9:1 el cumplimiento del Título II de la ADA, WCAG 2.2 AA y WCAG 3.0?",
            "answer_en": (
                "In plain English: While standard WCAG 2.2 AA requires a 4.5:1 contrast ratio, our Compliance-as-Code "
                "pipeline enforces a minimum 9:1 Double-Contrast Guard (#0B192C on #FAFBF7 = 16.8:1) across every Canvas page "
                "and web application so content remains readable under 100,000+ lux Yuma desert sunlight. Pre-commit and "
                "pre-push CI/CD linters also enforce sequential H2->H3 hierarchies, strip decorative emojis that break screen "
                "readers, and embed bilingual In Plain English / Norteño-Spanish cognitive scaffolding."
            ),
            "answer_es": (
                "En palabras sencillas: Mientras que WCAG 2.2 AA exige 4.5:1, nuestra tubería de Cumplimiento-como-Código "
                "impone un contraste mínimo de 9:1 (16.8:1 en producción), jerarquía estricta H2->H3, cero emojis decorativos "
                "y resúmenes bilingües en lenguaje sencillo para cumplir con el Título II de la ADA."
            ),
            "keywords": "ada title ii wcag 2.2 aa 9:1 double-contrast guard wcag 3.0 apca cognitive accessibility in plain english screen reader emoji stripper",
            "links": [
                {"label_en": "Inspect WCAG 2.2 AA & ADA Title II Standards in EXW-Demo", "label_es": "Inspeccionar Estándares WCAG 2.2 AA en EXW-Demo", "url": "https://azwestern.instructure.com/courses/42051/pages/exw-demo-coach-alan-wcag-2-dot-2-aa-ada-title-ii-and-section-508-verification-standards"},
                {"label_en": "Read Essay 35 (Automating Accessibility in CI/CD)", "label_es": "Leer Ensayo 35 (Automatización de Accesibilidad)", "url": "/essays/essay-35-automating-accessibility/"},
            ],
        },
        {
            "id": "qa-food-informatics-pwa-library",
            "category": "dom-graphrag",
            "badge": "DOM GraphRAG • Food Informatics & 9 PWAs",
            "dom_path": "Production Applications > Food Informatics & 9-App Lovable PWA Library",
            "title_en": "What are Food Informatics Consulting ('Measure Twice, Cut Once') and the 9 Production PWAs?",
            "title_es": "¿Qué son la Consultoría en Informática de Alimentos ('Medir Dos Veces, Cortar Una') y las 9 PWAs en producción?",
            "answer_en": (
                "In plain English: Grounded in Krupitzer & Stein (2021, Foods, 10(11), 2889), Food Informatics Consulting "
                "uses on-device machine vision and structured Markdown handoffs to convert restaurant menus into gram-level "
                "dish reformulation proposals (T2DM, GLP-1 Supportive, DASH, Prenatal, Celiac/Gluten-Free). It is part of our "
                "9-app production PWA suite: exwtoolkit.com, paga2018.dev, exwdemo.dev, culinarycompass.dev, flavorarchitect.dev, "
                "arquitectodelsabor.dev, mdtodocs.app, prompt-mile-hero, and agflow-roi-dash."
            ),
            "answer_es": (
                "En palabras sencillas: Basada en Krupitzer y Stein (2021), la Consultoría en Informática de Alimentos "
                "convierte menús de restaurantes en datos estructurados en Markdown y propuestas de reformulación en gramos, "
                "integrada dentro de nuestra biblioteca de 9 aplicaciones web progresivas (PWAs) en vivo."
            ),
            "keywords": "food informatics consulting measure twice cut once krupitzer stein 2021 flavorarchitect culinarycompass exwtoolkit paga2018 exwdemo mdtodocs pwa",
            "links": [
                {"label_en": "Launch Food Informatics Hub (flavorarchitect.dev)", "label_es": "Abrir Hub de Informática de Alimentos", "url": "https://flavorarchitect.dev/food-informatics"},
                {"label_en": "Explore All 9 Production PWAs", "label_es": "Explorar las 9 Aplicaciones PWA", "url": "/#applications"},
                {"label_en": "Webcognita LLC Capabilities Statement", "label_es": "Declaración de Capacidades de Webcognita LLC", "url": "https://www.webcognita.com/"},
            ],
        },
    ]


def parse_research_log_entries():
    entries = []
    if not RESEARCH_LOG_MD.exists():
        return entries
    text = RESEARCH_LOG_MD.read_text(encoding="utf-8")
    # Match ### **Month Day, Year — Title**
    pattern = re.compile(
        r"^###\s+\*\*([A-Za-z]+\s+\d{1,2},\s+\d{4}(?:\s+\([^)]+\))?)\s+—\s+(.+?)\*\*\s*$([\s\S]*?)(?=^###\s+|\n##\s+|\Z)",
        re.MULTILINE,
    )
    for idx, m in enumerate(pattern.finditer(text), start=1):
        date_str, title, body = (
            m.group(1).strip(),
            m.group(2).strip(),
            m.group(3).strip(),
        )
        title_clean = re.sub(r"`([^`]+)`", r"\1", title)
        # Extract first narrative paragraph as concise answer
        clean_lines = []
        for line in body.splitlines():
            s = line.strip()
            if not s or s.startswith("```") or s.startswith("|") or s.startswith("+-") or s.startswith("* **"):
                continue
            s_clean = re.sub(r"\*\*([^*]+)\*\*", r"\1", s)
            s_clean = re.sub(r"`([^`]+)`", r"\1", s_clean)
            s_clean = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s_clean)
            s_clean = re.sub(r"^[-*]\s*", "", s_clean)
            if len(s_clean) > 35:
                clean_lines.append(s_clean)
            if len(" ".join(clean_lines)) > 360:
                break
        summary = " ".join(clean_lines)[:440].strip()
        if not summary:
            summary = f"Longitudinal Research Log Entry ({date_str}) analyzing {title_clean}."
        entries.append(
            {
                "id": f"rlog-{idx:02d}-{sha12(date_str + title_clean)[:6]}",
                "category": "research-log",
                "badge": f"Research Log #{idx:02d} • {date_str}",
                "dom_path": f"Master Research Log > {date_str}",
                "title_en": f"[{date_str}] {title_clean}",
                "title_es": f"[{date_str}] {title_clean}",
                "answer_en": f"In plain English ({date_str}): {summary}",
                "answer_es": f"En palabras sencillas ({date_str}): {summary}",
                "keywords": f"{date_str.lower()} {title_clean.lower()} research log bitacora compendium 07",
                "links": [
                    {
                        "label_en": "Open in Live Research Log Observatory",
                        "label_es": "Abrir en el Observatorio de la Bitácora",
                        "url": "/research-log/",
                    },
                    {
                        "label_en": "Download Compendium 07 (PDF)",
                        "label_es": "Descargar Compendio 07 (PDF)",
                        "url": "/docs/CaC_and_CaaS_Master_Research_Log_2026_Compendium.pdf",
                    },
                ],
            }
        )
    return entries


def parse_essays():
    essays = [
        {
            "id": "essay-40",
            "category": "essays",
            "badge": "ESSAY 40 • US DOL TEN 07-25 & Sovereign 3-Stage Spine OER",
            "dom_path": "Curriculum-as-Code Essays > Essay 40",
            "title_en": "Essay 40: What If I Didn't Map the Federal Blueprint? – Operationalizing U.S. DOL TEN No. 07-25 AI Literacy Inside a Sovereign 3-Stage Spine OER Fleet",
            "title_es": "Ensayo 40: ¿Y si no hubiera mapeado el marco federal? – U.S. DOL TEN No. 07-25 y el Arquitectura Soberana OER",
            "answer_en": "In plain English: Essay 40 demonstrates how to translate the voluntary U.S. Department of Labor (DOL) ETA Advisory TEN No. 07-25 (5 Foundational Content Areas + 7 Community College Delivery Design Principles) into Sovereign Three-Stage Architecture (Mandate -> System -> Proof) and $0 ZTC Open Educational Resources.",
            "answer_es": "En palabras sencillas: El Ensayo 40 muestra cómo operacionalizar el marco federal voluntario U.S. DOL ETA TEN No. 07-25 (5 Áreas + 7 Principios) dentro del Arquitectura Soberana de Sovereign CaC y recursos educativos abiertos ($0 ZTC).",
            "keywords": "essay 40 us dol eta ten 07-25 ai literacy framework sovereign spine mandate system proof oer community college",
            "links": [
                {"label_en": "Inspect Live Crosswalk in EXW-Demo (Course 42051)", "label_es": "Inspeccionar Cruce en Vivo en EXW-Demo", "url": "https://azwestern.instructure.com/courses/42051/pages/exw-demo-coach-alan-the-exw-ai-landscape-institutional-alignment-and-literacy"},
                {"label_en": "View All Essays", "label_es": "Ver Todos los Ensayos", "url": "/essays/"},
            ],
        },
        {
            "id": "essay-39",
            "category": "essays",
            "badge": "ESSAY 39 • Compliance as Code & Longitudinal Telemetry",
            "dom_path": "Curriculum-as-Code Essays > Essay 39",
            "title_en": "Essay 39: What If I Didn't Log the Telemetry? – Compliance as Code & 6 Months of Continuous Curriculum-as-Code Intelligence",
            "title_es": "Ensayo 39: ¿Y si no hubiera registrado la telemetría? – Compliance as Code y 6 meses de inteligencia continua",
            "answer_en": "In plain English: Essay 39 examines how maintaining a continuous 90-entry Master Research Log transforms daily EdTech release notes (Google Workspace, Canvas GraphQL, W3C standards) into deterministic Compliance-as-Code pre-commit gates.",
            "answer_es": "En palabras sencillas: El Ensayo 39 analiza cómo una bitácora longitudinal de 90 entradas convierte las actualizaciones de Google Workspace y Canvas GraphQL en compuertas deterministas de Cumplimiento-como-Código.",
            "keywords": "essay 39 compliance as code master research log telemetry longitudinal",
            "links": [
                {"label_en": "Launch Live Research Log Observatory", "label_es": "Abrir Observatorio de la Bitácora", "url": "/research-log/"},
                {"label_en": "View All Essays", "label_es": "Ver Todos los Ensayos", "url": "/essays/"},
            ],
        },
    ]
    if not LLMS_TXT.exists():
        return essays

    text = LLMS_TXT.read_text(encoding="utf-8")
    pattern = re.compile(r"^-\s+\[(Essay\s+\d+:[^\]]+)\]\(([^)]+)\):\s+(.+)$", re.MULTILINE)
    for m in pattern.finditer(text):
        title, url, desc = m.group(1).strip(), m.group(2).strip(), m.group(3).strip()
        num_m = re.search(r"Essay\s+(\d+)", title)
        num_str = num_m.group(1) if num_m else "00"
        rel_url = url.replace("https://alanpruitt.com", "")
        essays.append(
            {
                "id": f"essay-{num_str}",
                "category": "essays",
                "badge": f"ESSAY {num_str} • Canonical Archive",
                "dom_path": f"Curriculum-as-Code Essays > Essay {num_str}",
                "title_en": title,
                "title_es": title,
                "answer_en": f"In plain English: {desc}",
                "answer_es": f"En palabras sencillas: {desc}",
                "keywords": f"essay {num_str} {title.lower()} {desc.lower()}",
                "links": [
                    {"label_en": f"Read Essay {num_str}", "label_es": f"Leer Ensayo {num_str}", "url": rel_url},
                    {"label_en": "All Essays Archive", "label_es": "Archivo Completo de Ensayos", "url": "/essays/"},
                ],
            }
        )
    return essays


def main():
    curated = build_curated_executive_nodes()
    rlog = parse_research_log_entries()
    essays = parse_essays()
    all_items = curated + essays + rlog

    payload = {
        "meta": {
            "version": "S-A-R v2.2",
            "generated_at": "2026-11-02",
            "prov_o_agent": "urn:exw:agent:argon4-cac-distiller",
            "total_items": len(all_items),
            "counts": {
                "briefs": sum(1 for x in all_items if x["category"] == "briefs"),
                "dol_ten_07_25": sum(1 for x in all_items if x["category"] == "dol-ten-07-25"),
                "dom_graphrag": sum(1 for x in all_items if x["category"] == "dom-graphrag"),
                "essays": sum(1 for x in all_items if x["category"] == "essays"),
                "research_log": sum(1 for x in all_items if x["category"] == "research-log"),
            },
        },
        "suggested_queries": [
            {
                "label_en": "US DOL TEN No. 07-25 (5 + 7 AI Framework)",
                "label_es": "Marco Federal US DOL TEN No. 07-25 (5 + 7)",
                "query": "US DOL TEN 07-25",
            },
            {
                "label_en": "Downloadable Briefs & White Papers (01–07)",
                "label_es": "Informes Técnicos Descargables (01–07)",
                "query": "Brief 01 02 03 04 05 06 07 PDF",
            },
            {
                "label_en": "DOM GraphRAG (3,265 Nodes) & W3C PROV-O",
                "label_es": "DOM GraphRAG (3,265 Nodos) y W3C PROV-O",
                "query": "DOM GraphRAG W3C PROV-O",
            },
            {
                "label_en": "ADA Title II & 9:1 Double-Contrast Guard",
                "label_es": "Título II ADA y Contraste Mínimo 9:1",
                "query": "ADA Title II WCAG 9:1 APCA",
            },
            {
                "label_en": "Sovereign Spine (Mandate -> System -> Proof) & Pattern / Rule / Solve",
                "label_es": "Arquitectura Soberana (Mandato -> Sistema -> Evidencia)",
                "query": "Mandate System Proof Pattern Rule Solve",
            },
            {
                "label_en": "Air-Gapped Apple Silicon M1/M2 & FERPA",
                "label_es": "Apple Silicon M1/M2 Air-Gapped y FERPA",
                "query": "Air-Gapped Apple Silicon M1 M2 FERPA",
            },
            {
                "label_en": "Food Informatics ('Measure Twice, Cut Once')",
                "label_es": "Informática de Alimentos (Food Informatics)",
                "query": "Food Informatics Krupitzer Stein",
            },
            {
                "label_en": "Master Research Log (90 Entries)",
                "label_es": "Bitácora Maestra (90 Entradas)",
                "query": "Compendium 07 Master Research Log",
            },
        ],
        "items": all_items,
    }

    for out_dir in [SITE_ROOT / "static" / "data", SITE_ROOT / "data"]:
        out_dir.mkdir(parents=True, exist_ok=True)
        out_file = out_dir / "sovereign-qa-index.json"
        out_file.write_text(json.dumps(payload, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
        print(f"[✓] Wrote {out_file} ({out_file.stat().st_size / 1024:.1f} KB, {len(all_items)} items)")


if __name__ == "__main__":
    main()
