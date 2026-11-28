---
title: "Declaración de Conformidad de Accesibilidad e ISO 14289-1 (PDF/UA-1)"
date: 2026-11-28T09:00:00-07:00
description: "Registro público de verificación de doble compuerta en alanpruitt.com: WCAG 2.2 Nivel AA (Contraste 9:1) e ISO 14289-1:2014 (PDF/UA-1 mediante veraPDF 106/106 reglas, 0 errores)."
layout: "single"
---

<style>
  .ap-ci-banner {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: space-between;
    gap: 0.75rem;
    background-color: #0B192C;
    color: #FAFBF7;
    border-radius: 0.75rem;
    padding: 0.95rem 1.15rem;
    margin: 0.75rem 0 1.25rem 0;
  }
  .ap-ci-pill {
    display: inline-flex;
    align-items: center;
    background-color: #FAFBF7;
    color: #0B192C;
    font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
    font-size: 0.76rem;
    font-weight: 800;
    padding: 0.3rem 0.65rem;
    border-radius: 0.375rem;
  }
  .ap-ledger-wrapper {
    overflow: auto;
    max-inline-size: 100%;
    container-type: inline-size;
    margin: 1rem 0 1.5rem 0;
    border: 1.5px solid #0B192C;
    border-radius: 0.75rem;
    background-color: #FFFFFF;
  }
  table.ap-ledger-table {
    width: 100%;
    border-collapse: separate;
    border-spacing: 0;
    font-size: 0.85rem;
    background-color: #FFFFFF;
    color: #0B192C;
    margin: 0;
  }
  table.ap-ledger-table caption {
    text-align: left;
    font-weight: 800;
    font-size: 0.86rem;
    background-color: #0B192C;
    color: #FAFBF7;
    padding: 0.75rem 1rem;
  }
  table.ap-ledger-table thead {
    position: sticky;
    inset-block-start: 0;
    z-index: 1;
  }
  table.ap-ledger-table th,
  table.ap-ledger-table td {
    padding: 0.65rem 0.85rem;
    text-align: left;
    vertical-align: top;
    border-block-end: 1px solid #CBD5E1;
    line-height: 1.4;
    background-color: #FFFFFF;
    color: #0B192C;
  }
  table.ap-ledger-table thead th {
    background-color: #E8EEF5;
    color: #0B192C;
    font-weight: 800;
    border-block-end: 2px solid #0B192C;
  }
  table.ap-ledger-table tbody th {
    position: sticky;
    inset-inline-start: 0;
    background-color: #FFFFFF;
    color: #0B192C;
    font-weight: 800;
  }
  .ap-pass-pill {
    display: inline-block;
    background-color: #0B192C;
    color: #FAFBF7;
    font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
    font-size: 0.74rem;
    font-weight: 800;
    padding: 0.15rem 0.5rem;
    border-radius: 0.25rem;
    white-space: nowrap;
  }
  .ap-dl-btn {
    display: inline-flex;
    align-items: center;
    min-block-size: 44px;
    min-inline-size: 44px;
    padding: 0.35rem 0.7rem;
    border: 1.5px solid #0B192C;
    border-radius: 0.45rem;
    background-color: #FAFBF7;
    color: #0B192C;
    font-weight: 700;
    text-decoration: underline;
    text-underline-offset: 2px;
  }
  .ap-dl-btn:hover {
    background-color: #E8EEF5;
    color: #0B192C;
  }
  @container (width < 600px) {
    table.ap-ledger-table,
    table.ap-ledger-table thead,
    table.ap-ledger-table tbody,
    table.ap-ledger-table tr,
    table.ap-ledger-table th,
    table.ap-ledger-table td {
      display: block;
    }
    table.ap-ledger-table thead {
      display: none;
    }
    table.ap-ledger-table tr {
      margin-block-end: 0.75rem;
      border-block-end: 2px solid #0B192C;
    }
    table.ap-ledger-table tbody th {
      position: sticky;
      inset-block-start: 0;
      z-index: 2;
      background-color: #E8EEF5;
    }
    table.ap-ledger-table td:nth-child(2)::before {
      content: var(--label-2) ": ";
      font-weight: 800;
    }
    table.ap-ledger-table td:nth-child(3)::before {
      content: var(--label-3) ": ";
      font-weight: 800;
    }
  }
</style>

<div class="ap-ci-banner">
  <div>
    <strong>Integración Continua de Accesibilidad (Pre-Push CI): ACTIVA</strong><br>
    <span style="font-size: 0.8rem;">Compuerta 1: <code>pour_audit.py</code> (WCAG 2.2 AA &bull; 9:1) &nbsp;|&nbsp; Compuerta 2: <code>pdfua_audit.py</code> + <code>veraPDF 1.30.4</code> (ISO 14289-1 PDF/UA-1)</span>
  </div>
  <span class="ap-ci-pill">APROBADO &bull; 10/10 PDFs &bull; 106/106 REGLAS &bull; 0 ERRORES</span>
</div>

## Compromiso con la Accesibilidad Digital de Doble Compuerta

Alan Pruitt ("Coach Alan") audita y compila `alanpruitt.com`, sus 42 ensayos bilingües, 11 aplicaciones PWA, 419 páginas HTML en Canvas LMS y las 10 publicaciones técnicas en PDF bajo validación automatizada previa a cada despliegue:

* **Título II de la ADA (`28 CFR Parte 35`) y Sección 508 Federal (`36 CFR Parte 1194`)**
* **WCAG 2.2 Nivel AA (`Guardia de Doble Contraste 9:1`) y Accesibilidad Cognitiva WCAG 3.0** (*En palabras sencillas* / paridad Norteño-Español)
* **Estándar Internacional `ISO 14289-1:2014 (PDF/UA-1)`** verificado mediante **`veraPDF 1.30.4`** (el motor exacto de **PAC 2024**) con **`106/106` reglas aprobadas y `0` errores**

---

<h2 id="pdfua-ledger">Registro Público de Verificación en Vivo (veraPDF 106/106)</h2>

<div tabindex="0" role="region" aria-labelledby="pdfua-ledger-caption-ap-es" class="ap-ledger-wrapper">
  <table class="ap-ledger-table" style="--label-2: 'Puntaje y SHA-256'; --label-3: 'Descargar PDF/UA-1 Verificado';">
    <caption id="pdfua-ledger-caption-ap-es">Registro de Verificación Dual WCAG 2.2 AA (9:1) e ISO 14289-1 (PDF/UA-1) — alanpruitt.com (2026-11-28)</caption>
    <thead>
      <tr>
        <th scope="col">Publicación / Recurso</th>
        <th scope="col">Puntaje y SHA-256</th>
        <th scope="col">Descargar PDF/UA-1 Verificado</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <th scope="row">42 Ensayos Bilingües, 11 PWAs y 419 Páginas HTML EXW</th>
        <td><span class="ap-pass-pill">APROBADO &bull; 0 ERRORES</span><br><code>pour_audit.py</code> (WCAG 2.2 AA &bull; &ge;9:1)</td>
        <td><a href="/es/essays/" class="ap-dl-btn">Explorar 42 Ensayos HTML</a></td>
      </tr>
      <tr>
        <th scope="row">White Paper 00: Origen y Evolución de Curriculum-as-Code</th>
        <td><span class="ap-pass-pill">APROBADO &bull; 106/106 &bull; 0 ERRORES</span><br><code>sha256:9b3497815afc</code></td>
        <td><a href="/docs/Curriculum-as-Code-Origin-and-Evolution-Whitepaper.pdf" download="Curriculum-as-Code-Origin-and-Evolution-Whitepaper_PDFUA1.pdf" class="ap-dl-btn">Descargar Whitepaper 00 PDF/UA-1</a></td>
      </tr>
      <tr>
        <th scope="row">Informe 01: IA Clínica Soberana, DOM GraphRAG y W3C PROV-O</th>
        <td><span class="ap-pass-pill">APROBADO &bull; 106/106 &bull; 0 ERRORES</span><br><code>sha256:447c29f4ae17</code></td>
        <td><a href="/docs/EXW_S_A_R_v2_2_DOM_GraphRAG_and_PROV_O_Architecture_Brief.pdf" download="EXW_S_A_R_v2_2_DOM_GraphRAG_and_PROV_O_Architecture_Brief_PDFUA1.pdf" class="ap-dl-btn">Descargar Informe 01 PDF/UA-1</a></td>
      </tr>
      <tr>
        <th scope="row">Manual 02: Manual de Laboratorio Flota EXW (v2.2)</th>
        <td><span class="ap-pass-pill">APROBADO &bull; 106/106 &bull; 0 ERRORES</span><br><code>sha256:df8ada6e15be</code></td>
        <td><a href="/docs/EXW_Course_Fleet_Laboratory_Manual_v2_2.pdf" download="EXW_Course_Fleet_Laboratory_Manual_v2_2_PDFUA1.pdf" class="ap-dl-btn">Descargar Manual 02 PDF/UA-1</a></td>
      </tr>
      <tr>
        <th scope="row">Portafolio 03: Propuesta Curricular AWC WPE Nivel 100</th>
        <td><span class="ap-pass-pill">APROBADO &bull; 106/106 &bull; 0 ERRORES</span><br><code>sha256:bd270246a734</code></td>
        <td><a href="/docs/AWC_WPE_Novel_100_Level_Curriculum_Proposal_Portfolio.pdf" download="AWC_WPE_Novel_100_Level_Curriculum_Proposal_Portfolio_PDFUA1.pdf" class="ap-dl-btn">Descargar Portafolio 03 PDF/UA-1</a></td>
      </tr>
      <tr>
        <th scope="row">Informe 04: Project Horizon Fondo de Innovación AWC 2026</th>
        <td><span class="ap-pass-pill">APROBADO &bull; 106/106 &bull; 0 ERRORES</span><br><code>sha256:3f2281117063</code></td>
        <td><a href="/docs/AWC_2026_Innovation_Fund_Project_Horizon_Executive_Memo.pdf" download="AWC_2026_Innovation_Fund_Project_Horizon_Executive_Memo_PDFUA1.pdf" class="ap-dl-btn">Descargar Informe 04 PDF/UA-1</a></td>
      </tr>
      <tr>
        <th scope="row">White Paper 05: WCAG 3.0 APCA (100k+ Lux) y Norteño Linting</th>
        <td><span class="ap-pass-pill">APROBADO &bull; 106/106 &bull; 0 ERRORES</span><br><code>sha256:ddbf8b0611b4</code></td>
        <td><a href="/docs/Project_Horizon_WCAG3_APCA_and_Norteno_ScreenReader_White_Paper.pdf" download="Project_Horizon_WCAG3_APCA_and_Norteno_ScreenReader_White_Paper_PDFUA1.pdf" class="ap-dl-btn">Descargar White Paper 05 PDF/UA-1</a></td>
      </tr>
      <tr>
        <th scope="row">Especificación 06: Banco de Pruebas Edge Aislado</th>
        <td><span class="ap-pass-pill">APROBADO &bull; 106/106 &bull; 0 ERRORES</span><br><code>sha256:41e5b6b18d84</code></td>
        <td><a href="/docs/Project_Horizon_Vendor-agnostic_Technical_Specs.pdf" download="Project_Horizon_Vendor-agnostic_Technical_Specs_PDFUA1.pdf" class="ap-dl-btn">Descargar Especificación 06 PDF/UA-1</a></td>
      </tr>
      <tr>
        <th scope="row">Compendio 07: Bitácora Maestra de Investigación 2026 (36 págs.)</th>
        <td><span class="ap-pass-pill">APROBADO &bull; 106/106 &bull; 0 ERRORES</span><br><code>sha256:9f5f8ab880ce</code></td>
        <td><a href="/docs/CaC_and_CaaS_Master_Research_Log_2026_Compendium.pdf" download="CaC_and_CaaS_Master_Research_Log_2026_Compendium_PDFUA1.pdf" class="ap-dl-btn">Descargar Compendio 07 PDF/UA-1</a></td>
      </tr>
      <tr>
        <th scope="row">Informe Dataset 08: Impacto Schema.org Argon 4</th>
        <td><span class="ap-pass-pill">APROBADO &bull; 106/106 &bull; 0 ERRORES</span><br><code>sha256:1526d59bdc3c</code></td>
        <td><a href="/docs/Argon4_SchemaOrg_Dataset_Impact_on_CaC_and_EXW_Fleet_Report_2026-11-03.pdf" download="Argon4_SchemaOrg_Dataset_Impact_Report_PDFUA1.pdf" class="ap-dl-btn">Descargar Informe 08 PDF/UA-1</a></td>
      </tr>
      <tr>
        <th scope="row">Guía 09: Guía para Evaluadores Reclaiming Our Time</th>
        <td><span class="ap-pass-pill">APROBADO &bull; 106/106 &bull; 0 ERRORES</span><br><code>sha256:dc5d6379f52b</code></td>
        <td><a href="/docs/reclaiming-our-time-evaluator-guide.pdf" download="reclaiming-our-time-evaluator-guide_PDFUA1.pdf" class="ap-dl-btn">Descargar Guía 09 PDF/UA-1</a></td>
      </tr>
    </tbody>
  </table>
</div>

*Los anexos corporativos de contratación federal y estatal (Declaración de Capacidades, CV Principal y Memorando CMMC Nivel 1) están igualmente verificados con `106/106` reglas `veraPDF` (`0` errores) en el [Registro Dual de Accesibilidad de Webcognita LLC](https://www.webcognita.com/accessibility.html#pdfua-ledger).*

---

### Aviso de Independencia Institucional y Retroalimentación

Los marcos y auditorías publicados aquí corresponden a la investigación independiente de Alan Pruitt y no representan posturas oficiales de Arizona Western College ni de The University of Arizona. Para reportar cualquier barrera digital:

**Alan Pruitt**  
Correo electrónico: `alan.pruitt@gmail.com` • Asunto: `Retroalimentación de Accesibilidad - alanpruitt.com`
