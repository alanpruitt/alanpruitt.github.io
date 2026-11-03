#!/usr/bin/env python3
"""
S-A-R v2.2 EXW Clinical SSoT DOM GraphRAG Index Compiler
Distills /Users/alanpruitt/EXW-MASTER-LIBRARY/reports/rag_index/corpus_vector_index.json
into a browser-ready EXW SSoT Q&A JSON index for Canvas LMS course modules:
  - /Users/alanpruitt/alanpruitt.github.io/static/data/exw-ssot-rag-index.json
  - /Users/alanpruitt/alanpruitt.github.io/data/exw-ssot-rag-index.json
"""

import json
import re
from collections import Counter
from pathlib import Path

EXW_ROOT = Path("/Users/alanpruitt/EXW-MASTER-LIBRARY")
CORPUS_INDEX = EXW_ROOT / "reports" / "rag_index" / "corpus_vector_index.json"
SITE_ROOT = Path("/Users/alanpruitt/alanpruitt.github.io")

ROLE_LABELS = {
    "Plain_English_Callout": "In Plain English Callout",
    "Clinical_Case_Pattern": "Pattern (Clinical Case & Yuma Context)",
    "SSoT_Rule_Constraint": "Rule (SSoT Benchmark & Safety Gate)",
    "Instructional_Core_Solve": "Solve (Instructional Core & Prescription)",
    "Active_Verification": "Active Verification (150-Word Defense)",
    "Exemplar_10_10": "10/10 Student Exemplar",
}

COURSE_LINKS = {
    "EXW101": {
        "label": "Inspect EXW 101 Exemplar & PAGA 2018 Hub (Course 42051)",
        "url": "https://azwestern.instructure.com/courses/42051/pages/ex-exw101-exemplar-solves-catalog",
        "toolkit_label": "Open paga2018.dev OER Toolkit",
        "toolkit_url": "https://paga2018.dev",
    },
    "EXW150": {
        "label": "Inspect EXW 150 Exemplar & DGA 2025–2030 Hub (Course 42051)",
        "url": "https://azwestern.instructure.com/courses/42051/pages/ex-exw150-exemplar-solves-catalog",
        "toolkit_label": "Open EXW150 Sweat-Rate & Hydration Simulator",
        "toolkit_url": "https://azwestern.instructure.com/courses/42051/pages/exw-demo-coach-alan-exw150-desert-sweat-rate-and-fluid-deficit-simulator-embed-code-plus-rubric",
    },
    "EXW210": {
        "label": "Inspect EXW 210 Personal Fitness Training Syllabus & Modules (Course 42051)",
        "url": "https://azwestern.instructure.com/courses/42051/pages/exw210-syllabus-spring2027",
        "toolkit_label": "Launch exwtoolkit.com Clinical Workbench",
        "toolkit_url": "https://exwtoolkit.com",
    },
    "EXW245": {
        "label": "Inspect EXW 245 ACSM 12th Ed. Physiology Lab Guide (Course 42051)",
        "url": "https://azwestern.instructure.com/courses/42051/pages/exw245-module-01-lab-guide",
        "toolkit_label": "Launch exwtoolkit.com Ergometry Workbench",
        "toolkit_url": "https://exwtoolkit.com",
    },
    "EXW265": {
        "label": "Inspect EXW 265 Special Populations Exemplar Hub (Course 42051)",
        "url": "https://azwestern.instructure.com/courses/42051/pages/ex-exw265-exemplar-solves-catalog",
        "toolkit_label": "Open EXW265 Older Adult Fall-Risk Auditor",
        "toolkit_url": "https://azwestern.instructure.com/courses/42051/pages/exw-demo-coach-alan-exw265-older-adult-fall-risk-and-multicomponent-auditor-embed-code-plus-rubric",
    },
    "STANDARDS": {
        "label": "Inspect Vehicle 1 & 2: Clinical Framing Protocol & Federal SSoT Hierarchy",
        "url": "https://azwestern.instructure.com/courses/42051/pages/exw-demo-coach-alan-vehicle-1-and-2-the-clinical-framing-protocol-and-federal-ssot-hierarchy",
        "toolkit_label": "Inspect US DOL TEN No. 07-25 Crosswalk (Course 42051)",
        "toolkit_url": "https://azwestern.instructure.com/courses/42051/pages/exw-demo-coach-alan-the-exw-ai-landscape-institutional-alignment-and-literacy",
    },
}


def clean_markdown_text(raw: str) -> str:
    s = re.sub(r"```[\s\S]*?```", " ", raw)
    s = re.sub(r"^#+\s*", "", s, flags=re.MULTILINE)
    s = re.sub(r"\*\*([^*]+)\*\*", r"\1", s)
    s = re.sub(r"`([^`]+)`", r"\1", s)
    s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)
    s = re.sub(r"###+", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def main():
    with open(CORPUS_INDEX, "r", encoding="utf-8") as f:
        chunks = json.load(f)

    seen_keys = Counter()
    seen_exact = set()
    nodes = []

    # Add top-priority curated SSoT reference anchors first
    curated_ssot_nodes = [
        {
            "id": "ssot-paga-2018-master",
            "course": "EXW101",
            "module": "Module 01–16 SSoT",
            "ssot": "Physical Activity Guidelines for Americans (PAGA), 2nd Edition (2018)",
            "role": "SSoT_Rule_Constraint",
            "role_label": ROLE_LABELS["SSoT_Rule_Constraint"],
            "dom_path": "PAGA 2018 (2nd Ed.) > Aerobic, Muscle-Strengthening & Multicomponent Benchmarks",
            "clo": "EXW101-CLO1 / EXW265-CLO1",
            "sha": "paga2018ssot",
            "section": "PAGA 2018 Core Benchmarks (EXW 101, EXW 210 & EXW 265)",
            "source": "02_COURSES/EXW101/README.md",
            "text": (
                "In plain English: The Physical Activity Guidelines for Americans (PAGA), 2nd Edition (2018) is the "
                "Academic Source of Truth for EXW 101 and EXW 265 (and foundational movement in EXW 210). Key rules: "
                "(1) Adults need 150 to 300 minutes/week of moderate-intensity aerobic activity (3.0–5.9 METs) OR "
                "75 to 150 minutes/week of vigorous-intensity aerobic activity (>=6.0 METs), plus muscle-strengthening "
                "activities targeting all major muscle groups on >=2 days/week; (2) Youth (ages 6–17) require >=60 minutes/day "
                "of moderate-to-vigorous physical activity (including bone- and muscle-strengthening >=3 days/week); "
                "(3) Older adults (>=65 years) require multicomponent physical activity combining balance training, "
                "aerobic, and muscle-strengthening to prevent falls; (4) Every minute counts (the legacy 10-minute bout "
                "rule was eliminated in the 2nd Edition)."
            ),
            "links": COURSE_LINKS["EXW101"],
        },
        {
            "id": "ssot-dga-2025-2030-master",
            "course": "EXW150",
            "module": "Module 01–16 SSoT",
            "ssot": "2025-2030 Dietary Guidelines for Americans (\"Real Food\" Focus)",
            "role": "SSoT_Rule_Constraint",
            "role_label": ROLE_LABELS["SSoT_Rule_Constraint"],
            "dom_path": "DGA 2025–2030 > Real Food Focus, Macronutrient AMDRs & Desert Hydration Rules",
            "clo": "EXW150-CLO1 / EXW150-CLO2",
            "sha": "dga20252030s",
            "section": "2025–2030 Dietary Guidelines for Americans ('Real Food' Focus — EXW 150)",
            "source": "02_COURSES/EXW150/README.md",
            "text": (
                "In plain English: The 2025–2030 Dietary Guidelines for Americans ('Real Food' Focus) is the Academic "
                "Source of Truth for EXW 150 (Nutrition for Exercise & Sport). Key rules: (1) Prioritize whole, minimally "
                "processed nutrient-dense 'Real Foods' over ultra-processed supplements and proprietary blends; (2) Limit "
                "added sugars to <10% of total daily kcal and saturated fat to <10% of total daily kcal, with sodium "
                "<2,300 mg/day (adjusted clinically for documented high-heat sweat sodium losses in Yuma >110°F environments); "
                "(3) Acceptable Macronutrient Distribution Ranges (AMDR): Carbohydrates 45–65% (3–10 g/kg/day scaled to "
                "training volume), Protein 10–35% (1.2–2.0 g/kg/day for strength/endurance athletes), Fat 20–35%; "
                "(4) Fluid replacement: 125–150% of acute body-mass fluid deficit (~16–24 oz per lb of sweat lost) with "
                "whole-food electrolytes."
            ),
            "links": COURSE_LINKS["EXW150"],
        },
        {
            "id": "ssot-acsm-12th-ed-master",
            "course": "EXW245",
            "module": "Module 01–16 SSoT",
            "ssot": "ACSM's Guidelines for Exercise Testing and Prescription, 12th Edition (Effective July 10, 2025)",
            "role": "SSoT_Rule_Constraint",
            "role_label": ROLE_LABELS["SSoT_Rule_Constraint"],
            "dom_path": "ACSM 12th Ed. (2025) > Preparticipation Screening, FITT-VP & Cycle Ergometry",
            "clo": "EXW245-CLO1 / EXW210-CLO2",
            "sha": "acsm12thed25",
            "section": "ACSM's Guidelines for Exercise Testing and Prescription, 12th Edition (EXW 245 & EXW 210)",
            "source": "02_COURSES/EXW245/README.md",
            "text": (
                "In plain English: ACSM's Guidelines for Exercise Testing and Prescription, 12th Edition (effective July 10, "
                "2025) is the Academic Source of Truth for EXW 245 (Exercise Testing & Prescription) and clinical testing in "
                "EXW 210. Key rules: (1) Apply the ACSMPreparticipation Screening algorithm (current activity level + "
                "known CV/metabolic/renal disease + signs/symptoms + desired intensity) before any graded exercise test (GXT); "
                "(2) FITT-VP principle (Frequency, Intensity, Time, Type, Volume, Progression) using Karvonen Heart Rate "
                "Reserve (Target HR = [(HRmax - HRrest) x %Intensity] + HRrest) and VO2R / MET metabolic equations; "
                "(3) Enforce absolute and relative test termination criteria (e.g., drop in SBP >=10 mmHg with increasing "
                "workload, SBP >250 mmHg or DBP >115 mmHg, onset of angina, ataxia/dizziness) and post-exercise thermal "
                "safety in Yuma desert conditions."
            ),
            "links": COURSE_LINKS["EXW245"],
        },
        {
            "id": "ssot-nasm-opt-exw210-master",
            "course": "EXW210",
            "module": "Module 01–16 SSoT",
            "ssot": "PAGA 2018 (2nd Ed.); ACSM 12th Ed. (2025); and NASM Optimum Performance Training (OPT) Model",
            "role": "SSoT_Rule_Constraint",
            "role_label": ROLE_LABELS["SSoT_Rule_Constraint"],
            "dom_path": "NASM OPT Model > Stabilization, Strength & Power Phases (EXW 210)",
            "clo": "EXW210-CLO1 / EXW210-CLO3",
            "sha": "nasmopt210ss",
            "section": "NASM Optimum Performance Training (OPT) Model & Tri-SSoT Integration (EXW 210)",
            "source": "02_COURSES/EXW210/README.md",
            "text": (
                "In plain English: EXW 210 (Essentials of Personal Fitness Training) integrates three Academic Sources of "
                "Truth: PAGA 2018 (2nd Ed.), ACSM 12th Ed. (2025), and the National Academy of Sports Medicine (NASM) "
                "Optimum Performance Training (OPT) Model. Key OPT rules: (1) Level 1 — Stabilization Endurance (Phase 1: "
                "12–20 reps, 50–70% 1RM, slow 4-2-1-1 tempo, proprioceptive/core stability before heavy loading); "
                "(2) Level 2 — Strength (Phase 2 Strength Endurance supersets, Phase 3 Muscular Development 6–12 reps at "
                "75–85% 1RM, Phase 4 Maximal Strength 1–5 reps at 85–100% 1RM); (3) Level 3 — Power (Phase 5 Power supersetting "
                "85–100% 1RM strength with 30–45% 1RM or 10% body-weight explosive speed-strength). Always correct Overhead "
                "Squat Assessment (OHSA) movement compensations (overactive vs. underactive muscles) first."
            ),
            "links": COURSE_LINKS["EXW210"],
        },
        {
            "id": "ssot-dol-ten-07-25-master",
            "course": "STANDARDS",
            "module": "Fleet-Wide SSoT",
            "ssot": "U.S. DOL ETA Advisory TEN No. 07-25: Artificial Intelligence Literacy Framework (Feb 13, 2026)",
            "role": "SSoT_Rule_Constraint",
            "role_label": ROLE_LABELS["SSoT_Rule_Constraint"],
            "dom_path": "US DOL ETA TEN No. 07-25 > 5 Foundational Content Areas & 7 Community College Delivery Principles",
            "clo": "FLEET-ILO1 (Workforce AI Literacy & Clinical Problem Framing)",
            "sha": "dolten0725ss",
            "section": "Workforce AI Literacy SSoT: U.S. DOL ETA Advisory TEN No. 07-25 (All EXW Courses)",
            "source": "GEMINI.md",
            "text": (
                "In plain English: Across EXW 101, 150, 210, 245, and 265, our Workforce AI Literacy Source of Truth is "
                "the voluntary U.S. Department of Labor (DOL) Employment and Training Administration (ETA) Training and "
                "Employment Notice (TEN) No. 07-25 (issued February 13, 2026). Every Four-Part Submission operationalizes "
                "its 5 Foundational Content Areas: (1) Understand AI Principles (Centaur Protocol: Student as Clinical "
                "Architect, AI as Probabilistic Engine); (2) Explore AI Uses (case synthesis & bilingual patient education); "
                "(3) Direct AI Effectively (Part 1: P-T-C-F Prompt + ### delimiters); (4) Evaluate Outputs (Part 2: 150-Word "
                "Clinical SSoT Audit); and (5) Use AI Responsibly (Part 3: 150-Word Verbatim Active Verification Defense + "
                "FERPA zero-PII hygiene) alongside its 7 Community College Delivery Design Principles ($0 ZTC OER, Yuma "
                "context, experiential exwtoolkit.com simulation, and Golden Circle WHY -> HOW -> WHAT navigation)."
            ),
            "links": COURSE_LINKS["STANDARDS"],
        },
    ]

    nodes.extend(curated_ssot_nodes)

    for c in chunks:
        src = c.get("source", "")
        if "EXW101_001_Spring2027_Accelerated" in src or src.startswith("03_COURSES/"):
            continue
        course = c.get("course", "STANDARDS")
        module = c.get("module", "General")
        dg = c.get("dom_graph_node", {})
        role = dg.get("clinical_framing_role", "Instructional_Core_Solve")
        section = c.get("section", "")

        txt = clean_markdown_text(c.get("content", ""))
        if len(txt) < 45:
            continue

        dedup_sig = (course, module, role, txt[:100])
        if dedup_sig in seen_exact:
            continue
        seen_exact.add(dedup_sig)

        key_bucket = (course, module, role)
        if seen_keys[key_bucket] >= 2 and course != "STANDARDS":
            continue
        seen_keys[key_bucket] += 1

        nodes.append(
            {
                "id": c.get("id"),
                "course": course,
                "module": module,
                "ssot": c.get("ssot", ""),
                "role": role,
                "role_label": ROLE_LABELS.get(role, role),
                "dom_path": dg.get("dom_path", ""),
                "clo": (dg.get("clo_alignment") or [""])[0],
                "sha": (c.get("sha256") or "")[:12],
                "section": section,
                "source": src,
                "text": txt[:560],
                "links": COURSE_LINKS.get(course, COURSE_LINKS["STANDARDS"]),
            }
        )

    counts_by_course = Counter(n["course"] for n in nodes)
    counts_by_role = Counter(n["role"] for n in nodes)

    payload = {
        "meta": {
            "version": "S-A-R v2.2 EXW Clinical SSoT DOM GraphRAG",
            "generated_at": "2026-11-02",
            "source_vectors": len(chunks),
            "distilled_nodes": len(nodes),
            "counts_by_course": dict(counts_by_course),
            "counts_by_role": dict(counts_by_role),
        },
        "suggested_queries": [
            {"label_en": "PAGA 2018 (150–300 min/wk & METs)", "label_es": "PAGA 2018 (150–300 min/sem y METs)", "query": "PAGA 2018 150 300 minutes METs"},
            {"label_en": "DGA 2025–2030 ('Real Food' & <10% Added Sugar)", "label_es": "DGA 2025–2030 (Comida Real y Azúcares <10%)", "query": "2025-2030 Dietary Guidelines Real Food sugar"},
            {"label_en": "ACSM 12th Ed. (VO2max, HRR & Cycle Ergometry)", "label_es": "ACSM 12.ª Ed. (VO2max, FC Reserva y Ergometría)", "query": "ACSM 12th Edition HRR VO2 ergometer"},
            {"label_en": "NASM OPT Model (Stabilization, Strength, Power)", "label_es": "Modelo NASM OPT (Estabilización, Fuerza, Potencia)", "query": "NASM OPT Stabilization Strength Power OHSA"},
            {"label_en": "Yuma Heat Stress (>110°F), Sweat Rate & Hydration", "label_es": "Estrés Térmico en Yuma (>110°F) e Hidratación", "query": "Yuma heat sweat rate hydration electrolytes"},
            {"label_en": "Special Populations (Fall Risk, T2DM, Hypertension)", "label_es": "Poblaciones Especiales (Riesgo de Caídas, DM2, HTA)", "query": "EXW265 fall risk balance diabetes hypertension"},
            {"label_en": "Pattern / Rule / Solve & 10-7-0 Mastery Scale", "label_es": "Patrón / Regla / Solución y Escala 10-7-0", "query": "Pattern Rule Solve P-T-C-F Active Verification"},
            {"label_en": "US DOL TEN No. 07-25 (5 Areas + 7 Principles)", "label_es": "US DOL TEN N.º 07-25 (5 Áreas + 7 Principios)", "query": "DOL TEN 07-25 5 Foundational Content Areas"},
        ],
        "items": nodes,
    }

    for out_dir in [SITE_ROOT / "static" / "data", SITE_ROOT / "data"]:
        out_dir.mkdir(parents=True, exist_ok=True)
        out_file = out_dir / "exw-ssot-rag-index.json"
        out_file.write_text(json.dumps(payload, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
        print(f"[✓] Wrote {out_file} ({out_file.stat().st_size / 1024:.1f} KB, {len(nodes)} EXW SSoT nodes)")


if __name__ == "__main__":
    main()
