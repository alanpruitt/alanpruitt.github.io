---
title: "Continuous Integration for Pedagogy: Writing Automated Unit Tests for Learning Outcomes"
title_es: "Integración Continua para la Pedagogía: Escritura de Pruebas Unitarias Automatizadas para Resultados de Aprendizaje"
description: "How applying CI pipeline linting, AST mapping, and automated prerequisite graph validation guarantees instructional integrity before code hits production."
description_es: "Cómo la aplicación de validaciones CI, mapeo AST y verificación automatizada de grafos de prerequisitos garantiza la integridad instruccional antes de llegar a producción."
essay_number: "07"
date: "2026-08-04"
author: "Alan Pruitt"
read_time: "8 min read"
source_type: "Markdown SSoT"
tags:
  - "Continuous Integration"
  - "Curriculum-as-Code"
  - "Pedagogical Testing"
  - "AST Linting"
  - "Instructional Engineering"
lang_default: "en"
canonical_url: "https://alanpruitt.com/articles/07-continuous-integration-pedagogy.html"
---

<!-- =========================================================================
  LANG: ENGLISH
  ========================================================================= -->
<div data-lang="en">

# Continuous Integration for Pedagogy: Writing Automated Unit Tests for Learning Outcomes

In software engineering, continuous integration (CI) pipelines run automated test suites on every commit to ensure system contracts remain unbroken. In traditional instructional design, however, curriculum changes are committed without automated verification—resulting in broken prerequisites, unmapped learning outcomes, and silent accessibility regressions that go unnoticed until students encounter them.

**Continuous Integration for Pedagogy** shifts quality assurance from a manual pre-semester review to an automated background process running on every Git commit.

## 1. The Anatomy of a Pedagogical Unit Test

Just as a software unit test validates that an function returns expected outputs for given inputs, a pedagogical unit test validates that instructional source code satisfies core educational requirements before compilation:

* **Bloom's Taxonomy Regex/AST Audits:** Automated linters scan Markdown headings and learning objectives to ensure action verbs match target cognitive depth.
* **Outcome Coverage Mapping:** Pre-commit hooks parse course modules to verify that every lesson maps directly to at least one accredited institutional outcome.
* **Accessibility Linting:** Build checks audit contrast ratios, header hierarchy depth (`#` through `###`), and alt-text completeness across all visual media.

## 2. Directed Acyclic Graphs (DAGs) for Prerequisite Verification

When course modules are reordered or updated across multiple semesters, prerequisite dependencies frequently break. By representing course progression as a Directed Acyclic Graph (DAG), CI build scripts run topological sorting tests to detect dependency failures instantly:

1. **Node Validation:** Every module node must define explicit entry competencies and exit outcomes.
2. **Cycle Detection:** Automated graph traversal verifies that circular prerequisite loops cannot occur.
3. **Orphaned Content Warnings:** Build passes flag any module or lab assignment disconnected from the primary progression tree.

> "If a broken code commit shouldn't make it to main, a broken learning outcome shouldn't make it to the LMS."

## 3. Shifting Quality Assurance Left

By integrating pedagogical linters into local pre-commit hooks and remote GitHub Actions workflows, instructional architects achieve **zero-regression curriculum delivery**. Quality assurance is no longer a stressful audit completed days before a term starts; it is a continuously passing test suite.

</div>

<!-- =========================================================================
  LANG: SPANISH
  ========================================================================= -->
<div data-lang="es" class="hidden-lang">

# Integración Continua para la Pedagogía: Escritura de Pruebas Unitarias Automatizadas para Resultados de Aprendizaje

En la ingeniería de software, las tuberías de integración continua (CI) ejecutan suites de pruebas automatizadas en cada commit para garantizar que las funciones del sistema permanezcan intactas. En el diseño instruccional tradicional, sin embargo, los cambios curriculares se aplican sin verificación automatizada, lo que resulta en prerrequisitos rotos, resultados de aprendizaje desalineados y regresiones de accesibilidad no detectadas hasta que el estudiante las enfrenta.

La **Integración Continua para la Pedagogía** traslada la garantía de calidad desde una revisión manual previa al semestre hacia un proceso automatizado en segundo plano que se ejecuta en cada actualización de Git.

## 1. La Anatomía de una Prueba Unitaria Pedagógica

Así como una prueba unitaria de software valida que una función devuelva los resultados esperados, una prueba unitaria pedagógica valida que el código fuente instruccional cumpla con los requisitos educativos fundamentales antes de su compilación:

* **Auditorías AST/Regex de la Taxonomía de Bloom:** Validadores automatizados analizan los encabezados y objetivos en Markdown para asegurar que los verbos de acción coincidan con la profundidad cognitiva esperada.
* **Mapeo de Cobertura de Resultados:** Hooks de pre-commit analizan los módulos para verificar que cada lección esté vinculada a un resultado de aprendizaje acreditado.
* **Verificación Automatizada de Accesibilidad:** Las pruebas de compilación auditan contrastes, jerarquías de encabezados y etiquetas de texto alternativo en todos los medios visuales.

## 2. Grafos Acíclicos Dirigidos (DAGs) para Verificación de Prerrequisitos

Cuando los módulos de un curso se reordenan o actualizan entre semestres, las dependencias de prerrequisitos suelen romperse. Al representar la progresión académica como un Grafo Acíclico Dirigido (DAG), los scripts de CI ejecutan pruebas de ordenamiento topológico para detectar fallos de dependencia al instante:

1. **Validación de Nodos:** Cada nodo del módulo debe definir competencias de entrada y resultados de salida explícitos.
2. **Detección de Ciclos:** El recorrido automatizado del grafo verifica que no existan bucles circulares de prerrequisitos.
3. **Advertencias de Contenido Huérfano:** El sistema señala cualquier lección o laboratorio desconectado del árbol de progresión principal.

> "Si una actualización de código defectuosa no debe llegar a la rama principal, un resultado de aprendizaje roto tampoco debe llegar al LMS."

## 3. Desplazando la Garantía de Calidad a la Izquierda

Al integrar validadores pedagógicos en hooks locales de pre-commit y flujos de GitHub Actions, los arquitectos instruccionales logran una **entrega curricular libre de regresiones**. La garantía de calidad deja de ser una auditoría estresante días antes del semestre para convertirse en una suite de pruebas en ejecución continua.

</div>
