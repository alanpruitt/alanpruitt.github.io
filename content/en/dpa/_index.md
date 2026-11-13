---
title: "Data Processing Addendum (DPA)"
date: 2026-11-10T08:00:00-07:00
draft: false
layout: "single"
description: "Data Processing Addendum (DPA), FERPA compliance rider, ADA Title II accessibility guarantee, and AI data governance terms for Webcognita LLC institutional contracts."
---

## Institutional Compliance & AI Governance Rider

* **Effective Date:** November 10, 2026
* **Entity:** Webcognita LLC (a Veteran-Owned Small Business) and Alan Pruitt ("Provider," "we," or "our")
* **Applicable To:** All educational institutions, community colleges, universities, public workforce agencies, and government contracting bodies ("Customer" or "Institution") entering into a Master Services Agreement, Statement of Work (SOW), Purchase Order, or digital product licensing agreement with Webcognita LLC.

---

### 1. Purpose, Scope, and Order of Precedence

This Data Processing Addendum ("DPA") supplements the [Webcognita LLC Terms of Service](/terms/), [Privacy Policy](/privacy/), and [IP & OER Licensing Rider](/ip-oer/) as well as any governing institutional contract, Purchase Order, or Statement of Work (SOW). This DPA ensures strict compliance with statutory data privacy, accessibility, and AI governance mandates, including the **Family Educational Rights and Privacy Act (FERPA, 20 U.S.C. § 1232g; 34 CFR Part 99)**, **DOJ ADA Title II (28 CFR Part 35)**, state-level student and public data privacy statutes, and institutional IT security policies. In the event of any conflict between the terms of this DPA and the general Terms of Service, the terms of this DPA shall govern.

---

### 2. FERPA Compliance & Educational Records

1. **Default Zero-PII Architecture by Design:** Webcognita LLC engineers its Curriculum-as-Code frameworks, static web infrastructure, and client-side browser simulators (`exwtoolkit.com`) to operate without collecting, transmitting, or storing student personally identifiable information (PII). Unless explicitly required by a written Statement of Work, the Institution does not need to provision student PII to Webcognita LLC.
2. **School Official Designation (`34 CFR § 99.31(a)(1)(i)(B)`):** To the extent that Webcognita LLC receives, accesses, or maintains education records (as defined under FERPA, `34 CFR Part 99`) on behalf of the Institution under a specific Statement of Work, Provider acknowledges that it acts as a "School Official" with a legitimate educational interest and operates under the direct control of the Institution with respect to the use, maintenance, and handling of such education records.
3. **Prohibition on Unauthorized Disclosure & Re-Disclosure (`34 CFR § 99.33`):** Webcognita LLC shall not use, disclose, or re-disclose any education records or personally identifiable information (PII) derived from student records for any purpose other than fulfilling the specific contractual deliverables outlined in the governing Statement of Work.
4. **Strict Data Minimization:** Provider shall collect and process only the absolute minimum institutional or faculty data necessary to execute consulting, training, accessibility auditing, or software integration services.

---

### 3. AI Data Governance, Air-Gapped Sovereignty, and Zero-Retention Mandates

1. **Strict Prohibition on Foundation Model Training:** Webcognita LLC explicitly certifies that **no Customer data, user inputs, uploaded documents, prompts, source code, or institutional content processed via Webcognita LLC systems or associated AI workflows shall ever be used to train, fine-tune, or improve public or third-party foundational machine learning models**.
2. **Air-Gapped Local Inference & Zero-Retention Enterprise APIs:** Any artificial intelligence models or automated auditing tools deployed by Webcognita LLC in connection with institutional contracts operate exclusively via either: (a) **air-gapped local hardware inference (`Zero Cloud Egress`)** where all computation remains on local encrypted workstations, or (b) **enterprise-grade, zero-retention API endpoints** where input and output payloads are processed ephemerally and purged immediately following query resolution.
3. **Federal AI Literacy & Risk Alignment:** All AI governance workflows and instructional deliverables align with the **NIST AI Risk Management Framework (AI RMF 1.0)** and the **U.S. Department of Labor (DOL) Employment and Training Administration (ETA) Training and Employment Notice (TEN) No. 07-25 (*Artificial Intelligence Literacy Framework*)**.
4. **No Third-Party Monetization:** Institutional data and intellectual property assets shall never be monetized, aggregated for commercial profiling, or shared with unauthorized third-party entities.

---

### 4. Sub-Processor Inventory & Supply Chain Transparency

Webcognita LLC maintains a minimal, transparent inventory of authorized infrastructure providers utilized in delivering static web assets, documentation, and billing:

* **Static Hosting & Version Control:** GitHub Pages / GitHub Enterprise (Static asset hosting, version-controlled repositories, and automated CI/CD deployment).
* **Edge DNS & TLS Security Routing:** Cloudflare, Inc. (DNS resolution, DDoS mitigation, and enforced TLS/HTTPS transport encryption).
* **Payment Processing (If Applicable):** Stripe, Inc. (Tokenized PCI-DSS Level 1 compliant financial transaction handling; payment card credentials never touch Webcognita LLC servers).
* **Sub-Processor Obligations:** Webcognita LLC binds all authorized sub-processors to data protection and security standards no less restrictive than those outlined in this DPA. The Institution will be provided written notice prior to the addition of any new sub-processor that processes institutional data.

---

### 5. Data Security, Accessibility Compliance, and Breach Notification

1. **Technical & Administrative Safeguards:** Webcognita LLC implements industry-standard administrative, physical, and technical safeguards, including enforced TLS 1.3 / HTTPS encryption for data in transit, AES-256 encryption for data at rest, hardware-backed multi-factor authentication (MFA) for administrative access, and static architecture designs that eliminate server-side database injection surfaces.
2. **Digital Accessibility Standards (`ADA Title II` • `WCAG 2.2 AA` • `Section 508`):** All digital assets, consulting courseware, and web applications delivered by Webcognita LLC are engineered and continuously audited to comply with **WCAG 2.2 Level AA** (including high-contrast `9:1` visual readability gates), **DOJ ADA Title II (`28 CFR Part 35`)**, and **Section 508 of the Rehabilitation Act (`36 CFR Part 1194`)**.
3. **48-Hour Security Incident Notification:** In the event of a confirmed or reasonably suspected security breach compromising institutional data or education records, Webcognita LLC shall notify the Institution's designated procurement officer and legal counsel without unreasonable delay—and in no event later than **forty-eight (48) hours** following discovery—providing full cooperation and forensic telemetry to mitigate the incident.

---

### 6. Data Return and Certified Permanent Deletion

Upon the expiration, termination, or completion of the governing Statement of Work or contract:

1. **Secure Purging (30-Day Window):** Webcognita LLC shall, within **thirty (30) calendar days** (or sooner if requested in writing by the Institution), securely return, delete, purge, and destroy all institutional data, confidential communication records, and education-related files from its active systems and non-archival backups.
2. **Certificate of Destruction:** Upon written request by the Institution, an authorized principal of Webcognita LLC shall provide formal written certification confirming that all institutional data has been permanently and securely destroyed.

---

### 7. Governing Law and Institutional Jurisdiction

This DPA shall be governed by and construed in accordance with the federal laws of the United States and the state laws of the jurisdiction governing the contracting educational institution or public agency (or the State of Arizona if not otherwise specified by statute), without regard to conflict of law principles.

---

### 8. Authorized Execution

By entering into a Master Services Agreement, Purchase Order, or Statement of Work with Webcognita LLC, the signatory warrants that they are an authorized representative of Webcognita LLC, and that the commitments outlined in this Data Processing Addendum are legally binding upon the organization.

* **Provider:** Webcognita LLC (100% Veteran-Owned, Sole-Member Small Business • VOSB)
* **Principal:** Alan Pruitt
* **Headquarters & Standard Operating Hours:** `1906 S 6th Ave, Yuma, AZ 85364` • `Monday–Friday, 8:00 AM – 5:00 PM MST (Arizona)`
* **Canonical DPA URL:** `https://alanpruitt.com/dpa/`
* **Contact Email:** `alan.pruitt@gmail.com`
