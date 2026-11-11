---
title: "Curriculum-as-Code (CaC): Historia de Origen, Genealogía (2018–2026) y Arquitectura de Referencia S-A-R v2.2"
date: 2026-11-11T08:45:00-07:00
lastmod: 2026-11-11T09:00:00-07:00
description: "Documento técnico canónico de origen sobre Curriculum-as-Code (Plan de Estudios como Código): su evolución desde los contenedores de NRE Labs en 2018 hasta S-A-R v2.2 con DOM GraphRAG, procedencia W3C PROV-O, cumplimiento ADA Título II (9:1) e IA soberana local."
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
  - "Plan de Estudios como Código"
  - "Historia de Curriculum-as-Code"
  - "Estándar S-A-R"
  - "DOM GraphRAG"
  - "W3C PROV-O"
  - "ADA Título II"
  - "Alan Pruitt"
  - "Webcognita LLC"
---

<section aria-label="Definición Canónica y Descarga del Documento Técnico" style="background-color: #FFFFFF; color: #0B192C; border: 2px solid #0B192C; border-left: 6px solid #940925; border-radius: 0.75rem; padding: 1.25rem 1.5rem; margin-bottom: 1.75rem;">
  <p style="margin: 0 0 0.65rem 0; font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 0.78rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.05em; color: #940925; background-color: #FFFFFF;">
    Definición Canónica &bull; Documento de Origen (S-A-R v2.2)
  </p>
  <p style="margin: 0 0 0.85rem 0; font-size: 1.05rem; line-height: 1.65; color: #0B192C; background-color: #FFFFFF;">
    <dfn id="definition" style="font-style: normal; font-weight: 800; color: #0B192C; background-color: #FFFFFF;">Curriculum-as-Code (CaC)</dfn> (Plan de Estudios como Código) es una disciplina de ingeniería instruccional que trata los programas de estudio, lecturas, simulaciones clínicas, rúbricas de competencia y reglas de accesibilidad como código fuente en texto plano bajo control de versiones Git, compilado mediante compuertas automatizadas de integración continua (CI/CD) hacia sistemas LMS y repositorios educativos abiertos.
  </p>
  <p style="margin: 0 0 1rem 0; font-size: 0.95rem; line-height: 1.6; color: #18181b; background-color: #FFFFFF;">
    <strong>En Palabras Sencillas:</strong> Es como armar una casa con planos firmados en lugar de improvisar cuarto por cuarto: cada lectura, rúbrica y regla de accesibilidad vive en archivos limpios que se revisan solos antes de publicarse. Si los términos técnicos se ponen pesados, concéntrate primero en cómo separar el contenido académico de las plataformas cerradas protege a nuestros estudiantes fronterizos con materiales gratuitos y 100% accesibles.
  </p>
  <div style="display: flex; flex-wrap: wrap; gap: 0.75rem; align-items: center;">
    <a href="/docs/Curriculum-as-Code-Origin-and-Evolution-Whitepaper.pdf" download style="display: inline-flex; min-height: 44px; align-items: center; padding: 0.55rem 1rem; border-radius: 0.5rem; background-color: #0B192C; color: #FFFFFF; font-size: 0.85rem; font-weight: 700; text-decoration: none; border: 1.5px solid #0B192C;">
      Descargar Whitepaper Original (PDF en inglés &bull; 2 Páginas &bull; 525 KB) &rarr;
    </a>
    <a href="#citacion-academica" style="display: inline-flex; min-height: 44px; align-items: center; padding: 0.55rem 1rem; border-radius: 0.5rem; background-color: #FFFFFF; color: #0B192C; font-size: 0.85rem; font-weight: 700; text-decoration: underline; border: 1.5px solid #0B192C;">
      Citar Documento (APA 7 y BibTeX)
    </a>
    <a href="https://alanpruitt.substack.com/p/what-if-i-didnt-trace-the-lineage" target="_blank" rel="noopener noreferrer" style="display: inline-flex; min-height: 44px; align-items: center; padding: 0.55rem 1rem; border-radius: 0.5rem; background-color: #FFFFFF; color: #0B192C; font-size: 0.85rem; font-weight: 700; text-decoration: underline; border: 1.5px solid #0B192C;">
      Substack (EN): &ldquo;What If I Didn&rsquo;t Trace the Lineage?&rdquo; &rarr;
    </a>
    <a href="https://www.linkedin.com/feed/update/urn:li:activity:7526393204666077184/" target="_blank" rel="noopener noreferrer" style="display: inline-flex; min-height: 44px; align-items: center; padding: 0.55rem 1rem; border-radius: 0.5rem; background-color: #FFFFFF; color: #0B192C; font-size: 0.85rem; font-weight: 700; text-decoration: underline; border: 1.5px solid #0B192C;">
      Debate y Carrusel en LinkedIn &rarr;
    </a>
    <a href="https://me.developers.google.com/u/alanpruitt" target="_blank" rel="noopener noreferrer" style="display: inline-flex; min-height: 44px; align-items: center; padding: 0.55rem 1rem; border-radius: 0.5rem; background-color: #FFFFFF; color: #0B192C; font-size: 0.85rem; font-weight: 700; text-decoration: underline; border: 1.5px solid #0B192C;">
      Autor Verificado: g.dev/alanpruitt &rarr;
    </a>
  </div>
</section>

## Resumen Ejecutivo

Este documento establece la genealogía histórica completa y la evolución arquitectónica de **Curriculum-as-Code (CaC)** desde la ingeniería de confiabilidad de redes (`NetOps`) en 2018 hasta la pedagogía neuro-simbólica universitaria en 2026. En noviembre de 2018, la comunidad de NRE Labs (`nre-learning/nrelabs-curriculum` y la plataforma Antidote) introdujo el término *Curriculum-as-Code* para orquestar enrutadores virtuales en Kubernetes mediante archivos YAML (`syringe.yaml`). Al acoplar el contenido educativo a clústeres pesados de contenedores, NRE Labs terminó cerrando su plataforma interactiva. La Generación 2 (`2021–2026`) desacopló los textos en repositorios Git—anticipado en agosto de 2021 por el **Premio Nacional NADO Aliceann Wohlbruck** otorgado a Alan Pruitt por compilar un manual regional `CEDS` con un modelo Co-Pilot de código abierto en GitHub, y retomado en 2026 por flujos de diapositivas LaTeX/Beamer (`arXiv:2608.07364`)—pero los archivos planos carecían de grafos pedagógicos, verificación de accesibilidad LMS y trazabilidad criptográfica.

La Generación 3 (**Curriculum-as-Code Neuro-Simbólico y Soberano**, `S-A-R v2.2` — *Escalable / Auditable / Repetible*) cierra esas brechas en una flota universitaria activa de 5 cursos y 11 entornos Canvas (`EXW 101`, `150`, `210`, `245`, `265` y paquetes OER nacionales `KIN` / `HLTH`), integrando **El Protocolo de Encuadre Clínico (`Patrón / Regla / Solución`)**, fuentes federales de verdad (**PAGA 2018**, **DGA 2025–2030**, **ACSM 12.ª Ed.**, **NASM OPT** y **U.S. DOL ETA TEN N.º 07-25**), compuertas CI/CD para **ADA Título II / WCAG 2.2 AA (`9:1`) y WCAG 3.0**, un grafo **DOM GraphRAG de `3,265` nodos**, recibos **W3C PROV-O**, ontologías bilingües **W3C SKOS** en español norteño e IA local aislada (**Google Gemini Carbon 4** y **Gemma 4**).

---

## 1. Raíces Históricas: Las Tres Generaciones de Curriculum-as-Code (2018–2026)

### 1.1 Generación 1 (2018): Emulación de Contenedores NetOps en NRE Labs

A finales de 2018, la comunidad de ingeniería de redes presentó **Curriculum-as-Code** mediante NRE Labs, el motor Antidote y el repositorio archivado [nre-learning/nrelabs-curriculum en GitHub](https://github.com/nre-learning/nrelabs-curriculum) *(nota: el portal interactivo de NRE Labs cerró definitivamente)*. Inspirado en *Infrastructure-as-Code*, NRE Labs definió guías (`guide.md`) y topologías (`syringe.yaml`) bajo Git, pero cada lección dependía de contenedores Docker y clústeres Kubernetes (`Minikube`) en vivo, provocando una carga operativa insostenible.

### 1.2 Generación 2 (2021–2026): Texto Plano en Git, Co-Pilots Tempranos y Diapositivas

La segunda etapa trasladó el enfoque hacia repositorios de texto plano como Fuente Única de Verdad (`SSoT`): en agosto de 2021, Alan Pruitt obtuvo el **Premio de Impacto NADO Aliceann Wohlbruck** utilizando un modelo temprano de IA Co-Pilot en GitHub para estructurar un manual estratégico regional (`CEDS`), cinco años antes de los esquemas académicos de generación de diapositivas STEM en LaTeX/Beamer (`arXiv:2608.07364`). No obstante, los archivos planos seguían careciendo de validación automática de accesibilidad LMS, grafos semánticos de competencias y soberanía de datos estudiantiles bajo FERPA.

### 1.3 Generación 3 (2026): Arquitectura Neuro-Simbólica Soberana (S-A-R v2.2)

Desarrollada y validada en aulas reales de **Arizona Western College (HSI)**—donde el **77% del alumnado es latino** (`3.08` veces el umbral federal HSI del 25%) y el **62% son estudiantes universitarios de primera generación** (*"En AWC, el 77% de los estudiantes son latinos y el 62% son estudiantes de primera generación. Servimos a esta hermosa comunidad, pero los desafíos están en todas partes"*, Dra. Reetika Dhawan, Presidenta de AWC, citada en *The Yuma Sun*, 11 de noviembre de 2026)—y en investigación aplicada de IA en el borde en **The University of Arizona (Campus Yuma)** a través de **Webcognita LLC (`SDVOSB`)**, la arquitectura `S-A-R v2.2` compila módulos accesibles, rúbricas clínicas, ontologías bilingües y paquetes abiertos `Schema.org/Dataset` directamente desde Git hacia Canvas GraphQL (`POST /api/graphql`) sin depender de contenedores frágiles ni libros comerciales costosos.

---

## 2. Matriz Comparativa de las Tres Generaciones

<div tabindex="0" role="region" aria-labelledby="cac-matrix-caption-es" style="overflow-x: auto; max-width: 100%; margin: 1.25rem 0 1.75rem 0;">
  <table>
    <caption id="cac-matrix-caption-es">Evolución Arquitectónica de Curriculum-as-Code desde 2018 hasta el Estándar S-A-R v2.2 en 2026</caption>
    <thead>
      <tr>
        <th scope="col">Dimensión Arquitectónica</th>
        <th scope="col">Gen 1: Infraestructura NetOps (NRE Labs, 2018)</th>
        <th scope="col">Gen 2: Documentos Planos y Diapositivas (2021–2026)</th>
        <th scope="col">Gen 3: CaC Neuro-Simbólico Soberano (S-A-R v2.2, 2026)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <th scope="row">Dominio Principal</th>
        <td>Automatización de redes (<code>NetOps</code>), consola CLI y enrutamiento virtual.</td>
        <td>Manuales estratégicos (<code>CEDS 2021</code>), documentación técnica y diapositivas STEM LaTeX/Beamer (<code>arXiv:2608.07364</code>).</td>
        <td>Kinesiología universitaria, nutrición clínica, poblaciones especiales y alfabetización laboral en IA (<code>EXW</code>, <code>KIN</code>, <code>HLTH</code>).</td>
      </tr>
      <tr>
        <th scope="row">Entorno de Ejecución</th>
        <td>Emuladores en Kubernetes (<code>Minikube</code>), Docker y terminales <code>syringe.yaml</code> (plataforma cerrada).</td>
        <td>Repositorios Markdown o LaTeX compilados en PDFs o sitios estáticos planos.</td>
        <td>Markdown SSoT, Git CI/CD, Hugo SSG, tubería <strong>Canvas GraphQL (<code>/api/graphql</code>)</strong> de 3 etapas y simuladores PWA (<code>exwtoolkit.com</code>).</td>
      </tr>
      <tr>
        <th scope="row">Taxonomía Pedagógica</th>
        <td><code>Curso &rarr; Lección &rarr; Etapa</code> centrada en comandos operativos.</td>
        <td>Capítulos o presentaciones lineales sin aristas formales de competencia.</td>
        <td><strong>Protocolo Centauro</strong> y <strong>Protocolo de Encuadre Clínico (<code>Patrón / Regla / Solución</code>)</strong> con escala <code>10-7-0</code>.</td>
      </tr>
      <tr>
        <th scope="row">Fuentes Rectoras (SSoT)</th>
        <td>Sintaxis de red y validación de respuestas API.</td>
        <td>Plantillas de prompts y reglas tipográficas matemáticas.</td>
        <td>Estándares federales públicos: <strong>PAGA 2018 (2.ª Ed.)</strong>, <strong>DGA 2025–2030</strong>, <strong>ACSM 12.ª Ed.</strong>, <strong>NASM OPT</strong> y <strong>U.S. DOL TEN N.º 07-25</strong>.</td>
      </tr>
      <tr>
        <th scope="row">Accesibilidad y Derechos Civiles</th>
        <td>Terminal en navegador sin garantías de contraste ni carga cognitiva.</td>
        <td>Remediación manual posterior; fallos frecuentes en verificadores LMS.</td>
        <td><strong>Cumplimiento como Código</strong> con las <strong>8 reglas del Verificador de Canvas</strong>, <strong>Guardia de Doble Contraste <code>9:1</code></strong> y WCAG 3.0 bilingüe.</td>
      </tr>
      <tr>
        <th scope="row">Grafo Semántico e IA Soberana</th>
        <td>Scripts imperativos previos a los modelos de lenguaje.</td>
        <td>Fragmentos planos de texto con APIs comerciales en la nube.</td>
        <td><strong>DOM GraphRAG de <code>3,265</code> nodos</strong> + <strong>W3C PROV-O</strong> + <strong>W3C SKOS</strong> español norteño + <strong>Gemini Carbon 4 y Gemma 4</strong> locales en Apple Silicon.</td>
      </tr>
    </tbody>
  </table>
</div>

---

## 3. Seis Pilares Fundamentales de S-A-R v2.2

### 3.1 Fuente Única de Verdad (SSoT) en Markdown y Estándares Federales
Elimina el costo de libros comerciales (`$0 ZTC`) en los 5 cursos de la flota (`EXW 101 / KIN-101`, `EXW 150 / HLTH-150`, `EXW 210 / KIN-210`, `EXW 245 / KIN-245`, `EXW 265 / KIN-265`), anclando cada módulo a **PAGA 2018**, **Guías Alimentarias 2025–2030 ("Comida Real")**, **ACSM 12.ª Ed. (2025)**, **NASM OPT** y las **5 áreas de contenido y 7 principios de diseño de U.S. DOL ETA TEN N.º 07-25**.

### 3.2 El Protocolo Centauro y Encuadre Clínico (Patrón / Regla / Solución)
Forma al estudiante como **Arquitecto Clínico** utilizando prompts estructurados `P-T-C-F`, delimitadores triples (`###`), calibración táctil en `exwtoolkit.com`, auditoría clínica de 150 palabras y defensa activa de 150 palabras en su propia voz bajo la escala de dominio **10-7-0** con intentos ilimitados.

### 3.3 Cumplimiento como Código: ADA Título II, Contraste 9:1 y WCAG 3.0
Validadores automatizados en Python (`remediate_canvas_accessibility_checker_exw101.py`, `pour_audit.py`, `achieve_oer_linter.py`) garantizan `0 problemas abiertos` en el Verificador de Accesibilidad de Canvas, contraste mínimo **`9:1`** para lectura móvil bajo el sol del desierto de Yuma (`100,000+ lux`) y bloques bilingües *In Plain English / En Palabras Sencillas*.

### 3.4 Pedagogía Neuro-Simbólica: DOM GraphRAG, W3C PROV-O y W3C SKOS
Conecta **`3,265` nodos DOM** con resultados de aprendizaje (`CLOs`), traduce expresiones clínicas coloquiales del español norteño fronterizo mediante **W3C SKOS** y emite recibos criptográficos **W3C PROV-O** con huella SHA-256.

### 3.5 Sincronización GraphQL y Sindicación OER 21/21
Despliega actualizaciones sin deriva en 11 entornos Canvas vía `POST /api/graphql` y compila `467/467` módulos OER verificados al **`100.0% (21/21)`** bajo las rúbricas Achieve OER + metadatos `Schema.org/Dataset` de 4 niveles.

### 3.6 IA Soberana Aislada y Habilitación Nacional en los 50 Estados
Ejecuta **Google Gemini Carbon 4** y **Gemma 4** localmente en estaciones Apple Silicon (`M1/M2`) con 100% de privacidad FERPA y `$0.00` en tarifas recurrentes, posicionando a **Webcognita LLC (`SDVOSB`, `UEI: EZ34U9KNJA17`, `CAGE: 4ZCN6`)** como socio técnico habilitador no competidor para **NSF TechAccess: AI-Ready America**.

---

## 4. Preguntas Frecuentes sobre Curriculum-as-Code

<section aria-labelledby="faq-heading-es" style="margin: 1rem 0 2rem 0;">
  <h3 id="faq-heading-es" style="margin-bottom: 0.85rem;">Preguntas Clave de Referencia</h3>

  <details name="cac-faq-es" open style="background-color: #FFFFFF; color: #0B192C; border: 1.5px solid #0B192C; border-radius: 0.5rem; padding: 0.85rem 1.1rem; margin-bottom: 0.75rem;">
    <summary style="font-weight: 800; cursor: pointer; color: #0B192C; background-color: #FFFFFF;">¿Qué es Curriculum-as-Code (Plan de Estudios como Código)?</summary>
    <p style="margin-top: 0.65rem; margin-bottom: 0; color: #18181b; background-color: #FFFFFF;">
      Es una disciplina de ingeniería instruccional donde los programas, lecturas, simulaciones clínicas, rúbricas y reglas de accesibilidad se redactan en Markdown bajo control de versiones Git, se auditan automáticamente mediante integración continua (CI/CD) y se compilan sin deriva hacia Canvas LMS y paquetes abiertos OER.
    </p>
  </details>

  <details name="cac-faq-es" style="background-color: #FFFFFF; color: #0B192C; border: 1.5px solid #0B192C; border-radius: 0.5rem; padding: 0.85rem 1.1rem; margin-bottom: 0.75rem;">
    <summary style="font-weight: 800; cursor: pointer; color: #0B192C; background-color: #FFFFFF;">¿Cómo evolucionó desde NRE Labs (2018) hasta S-A-R v2.2 (2026)?</summary>
    <p style="margin-top: 0.65rem; margin-bottom: 0; color: #18181b; background-color: #FFFFFF;">
      NRE Labs introdujo el término en 2018 para laboratorios de redes en contenedores Kubernetes que luego cerraron por costos operativos. Tras los primeros manuales estratégicos en GitHub con IA Co-Pilot (Premio NADO 2021 de Alan Pruitt) y los generadores planos de diapositivas, S-A-R v2.2 consolidó en 2026 una arquitectura universitaria neuro-simbólica con DOM GraphRAG, W3C PROV-O, accesibilidad 9:1 e IA local aislada.
    </p>
  </details>
</section>

---

<h2 id="citacion-academica">5. Citación Académica y Atribución</h2>

**APA 7.ª Edición:**  
Pruitt, A. (2026). *From infrastructure automation to clinical pedagogy: The origin and evolution of Curriculum-as-Code (2018–2026)* (S-A-R Architecture Whitepaper v2.2). Webcognita LLC. [https://alanpruitt.com/curriculum-as-code/](https://alanpruitt.com/curriculum-as-code/)

> **Aviso Legal:** La arquitectura Curriculum-as-Code, el Estándar S-A-R, el Protocolo de Encuadre Clínico y las herramientas de código abierto descritas en este documento representan investigación e ingeniería docente independiente a través de Webcognita LLC y no constituyen política oficial ni respaldo de Arizona Western College ni de The University of Arizona.
