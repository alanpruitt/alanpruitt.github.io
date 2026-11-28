---
title: "Accessibility & ISO 14289-1 (PDF/UA-1) Conformance Statement"
date: 2026-11-28T09:00:00-07:00
description: "Live Dual-Gate Accessibility Conformance Ledger for alanpruitt.com: WCAG 2.2 Level AA (9:1 Double-Contrast Guard via pour_audit.py) and strict ISO 14289-1:2014 (PDF/UA-1 via veraPDF 106/106 rules, 0 errors)."
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
    <strong>Dual-Gate Pre-Push Accessibility CI: ACTIVE</strong><br>
    <span style="font-size: 0.8rem;">Gate 1: <code>pour_audit.py</code> (WCAG 2.2 AA &bull; 9:1) &nbsp;|&nbsp; Gate 2: <code>pdfua_audit.py</code> + <code>veraPDF 1.30.4</code> (ISO 14289-1 PDF/UA-1)</span>
  </div>
  <span class="ap-ci-pill">PASS &bull; 10/10 PDFs &bull; 106/106 RULES &bull; 0 ERRORS</span>
</div>

## Commitment to Dual-Gate Digital Accessibility

Alan Pruitt ("Coach Alan") engineers `alanpruitt.com`, its 42 bilingual essays, 11 companion Progressive Web Apps, 419 Canvas LMS HTML course files, and all 10 published research PDFs to satisfy **both** web and document civil-rights standards deterministically prior to deployment:

* **DOJ ADA Title II Final Rule (`28 CFR Part 35`) & Revised Federal Section 508 (`36 CFR Part 1194`)**
* **WCAG 2.2 Level AA (`9:1 Double-Contrast Guard`) & WCAG 3.0 APCA / Cognitive Accessibility** (*In Plain English* / Norteño-Spanish parity)
* **Strict `ISO 14289-1:2014 (PDF/UA-1)` Universal Accessibility** verified via **`veraPDF 1.30.4`** (the exact validation engine inside **PAC 2024**) with **`0` failed rules and `0` failed checks**

---

<h2 id="pdfua-ledger">Live Dual-Gate Verification Ledger (Don&rsquo;t Trust &mdash; Verify)</h2>

Conventional "Tagged PDF" exports routinely pass Adobe Acrobat's 32-item heuristic check while leaving hundreds of untagged decorative vectors, unmapped PDF 2.0 `<Strong>`/`<Em>` roles, skipped headings, broken `<LI>/<LBody>` lists, or unlabeled hyperlinks. Every authored PDF on `alanpruitt.com` passes our `pikepdf` + **`veraPDF 1.30.4 (-f ua1)`** pre-push gate (`106/106` rules, `0` errors) before `git push` is permitted.

<div tabindex="0" role="region" aria-labelledby="pdfua-ledger-caption-ap" class="ap-ledger-wrapper">
  <table class="ap-ledger-table" style="--label-2: 'Audit Score &amp; SHA-256'; --label-3: 'Download Verified PDF/UA-1';">
    <caption id="pdfua-ledger-caption-ap">alanpruitt.com Dual-Gate WCAG 2.2 AA (9:1) &amp; ISO 14289-1 (PDF/UA-1) Verification Ledger (Verified 2026-11-28)</caption>
    <thead>
      <tr>
        <th scope="col">Publication / Corpus Asset</th>
        <th scope="col">Audit Score &amp; SHA-256</th>
        <th scope="col">Download Verified PDF/UA-1</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <th scope="row">42 Bilingual Essays, 11 PWAs &amp; 419 EXW Canvas HTML Pages</th>
        <td><span class="ap-pass-pill">PASS &bull; 0 VIOLATIONS</span><br><code>pour_audit.py</code> (WCAG 2.2 AA &bull; &ge;9:1)</td>
        <td><a href="/essays/" class="ap-dl-btn">Browse 42-Essay HTML Archive</a></td>
      </tr>
      <tr>
        <th scope="row">Origin White Paper 00: Origin &amp; Evolution of Curriculum-as-Code</th>
        <td><span class="ap-pass-pill">PASS &bull; 106/106 &bull; 0 ERRORS</span><br><code>sha256:9b3497815afc</code></td>
        <td><a href="/docs/Curriculum-as-Code-Origin-and-Evolution-Whitepaper.pdf" download="Curriculum-as-Code-Origin-and-Evolution-Whitepaper_PDFUA1.pdf" class="ap-dl-btn">Download Whitepaper 00 PDF/UA-1</a></td>
      </tr>
      <tr>
        <th scope="row">Brief 01: Sovereign Clinical AI, DOM GraphRAG &amp; W3C PROV-O</th>
        <td><span class="ap-pass-pill">PASS &bull; 106/106 &bull; 0 ERRORS</span><br><code>sha256:447c29f4ae17</code></td>
        <td><a href="/docs/EXW_S_A_R_v2_2_DOM_GraphRAG_and_PROV_O_Architecture_Brief.pdf" download="EXW_S_A_R_v2_2_DOM_GraphRAG_and_PROV_O_Architecture_Brief_PDFUA1.pdf" class="ap-dl-btn">Download Brief 01 PDF/UA-1</a></td>
      </tr>
      <tr>
        <th scope="row">Manual 02: EXW Course Fleet Laboratory Manual (v2.2)</th>
        <td><span class="ap-pass-pill">PASS &bull; 106/106 &bull; 0 ERRORS</span><br><code>sha256:df8ada6e15be</code></td>
        <td><a href="/docs/EXW_Course_Fleet_Laboratory_Manual_v2_2.pdf" download="EXW_Course_Fleet_Laboratory_Manual_v2_2_PDFUA1.pdf" class="ap-dl-btn">Download Lab Manual 02 PDF/UA-1</a></td>
      </tr>
      <tr>
        <th scope="row">Portfolio 03: AWC WPE Novel 100-Level Curriculum Portfolio</th>
        <td><span class="ap-pass-pill">PASS &bull; 106/106 &bull; 0 ERRORS</span><br><code>sha256:bd270246a734</code></td>
        <td><a href="/docs/AWC_WPE_Novel_100_Level_Curriculum_Proposal_Portfolio.pdf" download="AWC_WPE_Novel_100_Level_Curriculum_Proposal_Portfolio_PDFUA1.pdf" class="ap-dl-btn">Download Portfolio 03 PDF/UA-1</a></td>
      </tr>
      <tr>
        <th scope="row">Brief 04: Project Horizon 2026 AWC Innovation Fund Memo</th>
        <td><span class="ap-pass-pill">PASS &bull; 106/106 &bull; 0 ERRORS</span><br><code>sha256:3f2281117063</code></td>
        <td><a href="/docs/AWC_2026_Innovation_Fund_Project_Horizon_Executive_Memo.pdf" download="AWC_2026_Innovation_Fund_Project_Horizon_Executive_Memo_PDFUA1.pdf" class="ap-dl-btn">Download Brief 04 PDF/UA-1</a></td>
      </tr>
      <tr>
        <th scope="row">White Paper 05: WCAG 3.0 APCA (100k+ Lux) &amp; Norte&ntilde;o Linting</th>
        <td><span class="ap-pass-pill">PASS &bull; 106/106 &bull; 0 ERRORS</span><br><code>sha256:ddbf8b0611b4</code></td>
        <td><a href="/docs/Project_Horizon_WCAG3_APCA_and_Norteno_ScreenReader_White_Paper.pdf" download="Project_Horizon_WCAG3_APCA_and_Norteno_ScreenReader_White_Paper_PDFUA1.pdf" class="ap-dl-btn">Download White Paper 05 PDF/UA-1</a></td>
      </tr>
      <tr>
        <th scope="row">Spec 06: Air-Gapped Edge Testbed &amp; Optical Telemetry Specs</th>
        <td><span class="ap-pass-pill">PASS &bull; 106/106 &bull; 0 ERRORS</span><br><code>sha256:41e5b6b18d84</code></td>
        <td><a href="/docs/Project_Horizon_Vendor-agnostic_Technical_Specs.pdf" download="Project_Horizon_Vendor-agnostic_Technical_Specs_PDFUA1.pdf" class="ap-dl-btn">Download Spec 06 PDF/UA-1</a></td>
      </tr>
      <tr>
        <th scope="row">Compendium 07: Master Research Log 2026 Compendium (36 pp.)</th>
        <td><span class="ap-pass-pill">PASS &bull; 106/106 &bull; 0 ERRORS</span><br><code>sha256:9f5f8ab880ce</code></td>
        <td><a href="/docs/CaC_and_CaaS_Master_Research_Log_2026_Compendium.pdf" download="CaC_and_CaaS_Master_Research_Log_2026_Compendium_PDFUA1.pdf" class="ap-dl-btn">Download Compendium 07 PDF/UA-1</a></td>
      </tr>
      <tr>
        <th scope="row">Dataset Brief 08: Argon 4 Schema.org Dataset Impact Report</th>
        <td><span class="ap-pass-pill">PASS &bull; 106/106 &bull; 0 ERRORS</span><br><code>sha256:1526d59bdc3c</code></td>
        <td><a href="/docs/Argon4_SchemaOrg_Dataset_Impact_on_CaC_and_EXW_Fleet_Report_2026-11-03.pdf" download="Argon4_SchemaOrg_Dataset_Impact_Report_PDFUA1.pdf" class="ap-dl-btn">Download Dataset Brief 08 PDF/UA-1</a></td>
      </tr>
      <tr>
        <th scope="row">Guide 09: Reclaiming Our Time Evaluator Guide</th>
        <td><span class="ap-pass-pill">PASS &bull; 106/106 &bull; 0 ERRORS</span><br><code>sha256:dc5d6379f52b</code></td>
        <td><a href="/docs/reclaiming-our-time-evaluator-guide.pdf" download="reclaiming-our-time-evaluator-guide_PDFUA1.pdf" class="ap-dl-btn">Download Evaluator Guide PDF/UA-1</a></td>
      </tr>
    </tbody>
  </table>
</div>

*Corporate Federal & SLED Procurement PDFs (Capabilities Statement, Principal CV, and CMMC Level 1 MFR) are similarly verified at `106/106` `veraPDF` rules (`0` errors) on the [Webcognita LLC Dual-Gate Accessibility Ledger](https://www.webcognita.com/accessibility.html#pdfua-ledger).*

---

### Architectural Accessibility Measures

* **Semantic HTML & ISO 32000-1 Tag Trees:** Section templates reserve `<h1>` for page-level titles with zero skipped heading levels; PDFs normalize headings sequentially (`H1` first), wrap list items in `<Lbl>` + `<LBody>`, map PDF 2.0 inline tags in `/RoleMap`, label every hyperlink's `/Contents` dictionary, and mark decorative borders/QR squares as `/Artifact`.
* **9:1 Double-Contrast Guard:** Doubling WCAG 2.2 AA's 4.5:1 baseline, primary text and interactive controls enforce a minimum **9:1 contrast ratio** and zero decorative Unicode emojis.
* **Interactive Controls & Announcers:** All buttons, filters, and links maintain minimum `44 × 44px` touch targets with visible `:focus-visible` outlines and debounced `aria-live="polite"` status regions.

---

### Institutional Independence & Feedback

The accessibility frameworks, audits, and essays on this site reflect independent research and engineering by Alan Pruitt and do not constitute official legal representations of Arizona Western College or The University of Arizona. To report any digital barrier:

**Alan Pruitt**  
Email: `alan.pruitt@gmail.com` • Subject: `Accessibility Feedback - alanpruitt.com`
