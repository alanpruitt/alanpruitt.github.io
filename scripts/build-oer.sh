#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="/Users/alanpruitt/alanpruitt.github.io"
BUILD_DIR="${ROOT_DIR}/dist/curriculum-as-code-health-sciences-oer"
ZIP_NAME="curriculum-as-code-health-sciences-v1.0.zip"

echo "==> Creating clean OER distribution structure..."
rm -rf "${BUILD_DIR}" "${ROOT_DIR}/dist/${ZIP_NAME}"
mkdir -p "${BUILD_DIR}/01-framework"
mkdir -p "${BUILD_DIR}/02-course-modules/EXW101-foundational-human-movement"
mkdir -p "${BUILD_DIR}/02-course-modules/EXW150-sports-nutrition"
mkdir -p "${BUILD_DIR}/02-course-modules/EXW245-exercise-testing-prescription"
mkdir -p "${BUILD_DIR}/02-course-modules/EXW265-special-populations"

echo "==> Copying essay sources to module targets..."
cp "${ROOT_DIR}/content/essays/22-foundational-human-movement-in-the-algorithmic-age.md" \
   "${BUILD_DIR}/02-course-modules/EXW101-foundational-human-movement/essay-22-source.md"

cp "${ROOT_DIR}/content/essays/21-evidence-based-nutrition-vs-feed.md" \
   "${BUILD_DIR}/02-course-modules/EXW150-sports-nutrition/essay-21-source.md"

cp "${ROOT_DIR}/content/essays/19-hybrid-ergometer-scaffold.md" \
   "${BUILD_DIR}/02-course-modules/EXW245-exercise-testing-prescription/essay-19-source.md"

cp "${ROOT_DIR}/content/essays/20-deterministic-clinical-guardrails.md" \
   "${BUILD_DIR}/02-course-modules/EXW265-special-populations/essay-20-source.md"

echo "==> Generating OER metadata.json..."
cat << 'EOF' > "${BUILD_DIR}/metadata.json"
{
  "title": "Curriculum-as-Code: Deterministic AI Guardrails, SSoT Governance, and Accessible Lab Scaffolding in Health Sciences",
  "author": "Alan Pruitt (Coach Alan)",
  "publisher": "Webcognita LLC / Arizona Western College",
  "version": "1.0.0",
  "publicationDate": "2026-08-21",
  "license": "CC-BY-4.0",
  "canonicalUrl": "https://alanpruitt.com/articles/",
  "repository": "https://github.com/alanpruitt/alanpruitt.github.io",
  "subjects": ["Education", "Applied Science", "Life Science", "Career and Technical Education"],
  "tags": [
    "Artificial Intelligence in Education",
    "Curriculum-as-Code",
    "Generative AI Pedagogy",
    "Instructional Design",
    "Prompt Engineering",
    "PAGA 2018 SSoT",
    "Kinesiology",
    "WCAG 2.2 AA",
    "OER"
  ]
}
EOF

echo "==> Generating LICENSE.md..."
cat << 'EOF' > "${BUILD_DIR}/LICENSE.md"
# Open License Agreement

## Content & Pedagogical Frameworks
All text, rubrics, case study schemas, and instructional frameworks are licensed under the **Creative Commons Attribution 4.0 International License (CC BY 4.0)**.
To view a copy of this license, visit: https://creativecommons.org/licenses/by/4.0/

**Attribution:**  
Pruitt, A. (2026). *Curriculum-as-Code: Deterministic AI Guardrails, SSoT Governance, and Accessible Lab Scaffolding in Health Sciences*. Webcognita LLC / Arizona Western College. https://alanpruitt.com/articles/

## Code, Prompts & Scripts
All system prompt templates, GitHub Actions workflows, and automated linter configurations are licensed under the **MIT License**.
EOF

echo "==> Generating Master OER Adoption Guide (README.md)..."
cat << 'EOF' > "${BUILD_DIR}/README.md"
# Curriculum-as-Code: Deterministic AI Guardrails, SSoT Governance, and Accessible Lab Scaffolding in Health Sciences

**Author:** Alan Pruitt (Coach Alan) — Founder & Chief Curriculum Architect, Webcognita LLC  
**Institution:** Arizona Western College / University of Arizona Yuma Campus  
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)  
**Canonical Hub:** [alanpruitt.com/articles](https://alanpruitt.com/articles/)

---

## What is this OER Package?
This repository contains a production-ready, open-access instructional suite for higher education faculty, curriculum architects, and instructional designers. Built on **Curriculum-as-Code (CaC)** principles, it provides a replicable architecture for integrating Generative AI into applied health sciences, kinesiology, and lab-based courses without clinical hallucination drift, student data privacy leaks, or commercial paywalls.

## Included Course Modules:
1. **EXW101 (Foundational Human Movement):** Community physical inactivity interventions, sociological problem framing, and PAGA 2018 SSoT alignment.
2. **EXW150 (Sports Nutrition):** Energy availability, REDs prevention, and synthetic delimited nutritional audits versus social media diet fads.
3. **EXW245 (Exercise Testing & Prescription):** 2-part hybrid ergometer scaffolding decoupling AI cognitive pre-flight simulations from physical Lode Corival cycle execution.
4. **EXW265 (Special Populations):** Deterministic clinical guardrails, triple-hash (###) delimiter prompt sandboxes, and 3-tier clinical evaluation rubrics.

## How to Import into Canvas LMS / Blackboard / Moodle:
* Each module folder contains raw, mobile-first Markdown files pre-formatted with strict WCAG 2.2 AA semantic heading hierarchies (starting at `<h2>`).
* AI prompt templates can be pasted directly into institutional custom GPTs, Gemini Gems, or Canvas LMS AI system instructions.
EOF

echo "==> Packaging release zip archive..."
cd "${ROOT_DIR}/dist"
zip -r "${ZIP_NAME}" "curriculum-as-code-health-sciences-oer" -x "*.DS_Store"

echo "==> OER Bundle ready: ${ROOT_DIR}/dist/${ZIP_NAME}"
