#!/usr/bin/env python3
"""
Canvas Common Cartridge (.imscc) & Facilitator Bundle Generator
Builds a standards-compliant IMS CC 1.1 package containing Modules 0-5,
the Capstone SpeedGrader Assignment, the Community Exchange Discussion,
and native Canvas Rubric JSON/CSV exports.
"""
import os
import zipfile
import json
import csv
import io

OUTPUT_DIR = "static/docs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 1. IMS Manifest definition
manifest_xml = """<?xml version="1.0" encoding="UTF-8"?>
<manifest identifier="MANIFEST_RECLAIMING_OUR_TIME_2026"
          xmlns="http://www.imsglobal.org/xsd/imsccv1p1/imscp_v1p1"
          xmlns:lom="http://ltsc.ieee.org/xsd/imsccv1p1/LOM/resource"
          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xsi:schemaLocation="http://www.imsglobal.org/xsd/imsccv1p1/imscp_v1p1 http://www.imsglobal.org/profile/cc/ccv1p1/ccv1p1_imscp_v1p1.xsd">
  <metadata>
    <schema>IMS Common Cartridge</schema>
    <schemaversion>1.1.0</schemaversion>
    <lom:lom>
      <lom:general>
        <lom:title>
          <lom:string language="en">Reclaiming Our Time: Secure and Practical GenAI Workflows for Faculty and Staff</lom:string>
        </lom:title>
        <lom:description>
          <lom:string language="en">Canvas v3.0 Exemplar Course Cartridge. Includes Modules 00-05, SpeedGrader Rubric, and FERPA-compliant prompt architectures.</lom:string>
        </lom:description>
      </lom:general>
    </lom:lom>
  </metadata>
  <organizations>
    <organization identifier="ORG_ROT_2026" structure="rooted-hierarchy">
      <item identifier="ITEM_M00">
        <title>Module 00: Technical Pre-Flight Gate &amp; FERPA Privacy Shield</title>
        <item identifier="RES_M00_PAGE" identifierref="RES_PAGE_M00">
          <title>Module 00: Access Gate &amp; Data Hygiene</title>
        </item>
        <item identifier="RES_M00_DISC" identifierref="RES_DISC_COMMUNITY">
          <title>Discussion: Community Exchange - Reclaiming Our Time Check-In</title>
        </item>
      </item>
      <item identifier="ITEM_M01">
        <title>Module 01: Institutional Governance &amp; Syllabus Policy Tiers</title>
        <item identifier="RES_M01_PAGE" identifierref="RES_PAGE_M01">
          <title>Module 01: Tiered Syllabus Governance (Tiers 1-3)</title>
        </item>
      </item>
      <item identifier="ITEM_M02">
        <title>Module 02: Administrative Triage &amp; Committee Minutes Extraction</title>
        <item identifier="RES_M02_PAGE" identifierref="RES_PAGE_M02">
          <title>Module 02: Committee Meeting Notes Extraction Matrix</title>
        </item>
      </item>
      <item identifier="ITEM_M03">
        <title>Module 03: Syntax Lab: Delimited Prompt Architecture</title>
        <item identifier="RES_M03_PAGE" identifierref="RES_PAGE_M03">
          <title>Module 03: Converting Notes to SpeedGrader Rubrics</title>
        </item>
      </item>
      <item identifier="ITEM_M04">
        <title>Module 04: The Safety Auditor: Hallucination Interception</title>
        <item identifier="RES_M04_PAGE" identifierref="RES_PAGE_M04">
          <title>Module 04: Clinical &amp; SSoT Hallucination Audits</title>
        </item>
      </item>
      <item identifier="ITEM_M05">
        <title>Module 05: Sovereign Auditor Capstone Matrix &amp; Reflection</title>
        <item identifier="RES_M05_ASSIGN" identifierref="RES_ASSIGN_CAPSTONE">
          <title>Summative Capstone: Sovereign Auditor Deliverable Matrix</title>
        </item>
      </item>
    </organization>
  </organizations>
  <resources>
    <resource identifier="RES_PAGE_M00" type="webcontent" href="wiki_content/module-00.html">
      <file href="wiki_content/module-00.html"/>
    </resource>
    <resource identifier="RES_DISC_COMMUNITY" type="imsdt_xmlv1p1" href="discussions/community-checkin.xml">
      <file href="discussions/community-checkin.xml"/>
    </resource>
    <resource identifier="RES_PAGE_M01" type="webcontent" href="wiki_content/module-01.html">
      <file href="wiki_content/module-01.html"/>
    </resource>
    <resource identifier="RES_PAGE_M02" type="webcontent" href="wiki_content/module-02.html">
      <file href="wiki_content/module-02.html"/>
    </resource>
    <resource identifier="RES_PAGE_M03" type="webcontent" href="wiki_content/module-03.html">
      <file href="wiki_content/module-03.html"/>
    </resource>
    <resource identifier="RES_PAGE_M04" type="webcontent" href="wiki_content/module-04.html">
      <file href="wiki_content/module-04.html"/>
    </resource>
    <resource identifier="RES_ASSIGN_CAPSTONE" type="associatedcontent/imscc_xmlv1p1/learning-application-resource" href="assignments/capstone-matrix.xml">
      <file href="assignments/capstone-matrix.xml"/>
    </resource>
  </resources>
</manifest>
"""

# 2. Capstone Assignment XML with Canvas SpeedGrader configuration
assignment_xml = """<?xml version="1.0" encoding="UTF-8"?>
<assignment identifier="RES_ASSIGN_CAPSTONE" xmlns="http://canvas.instructure.com/xsd/cccv1p0">
  <title>Summative Capstone: Sovereign Auditor Deliverable Matrix</title>
  <description>&lt;div style="background-color: #FFFFFF; border: 1px solid #CBD5E1; border-left: 5px solid #003366; padding: 18px 20px; border-radius: 4px;"&gt;
    &lt;h2 style="color: #002147; font-size: 1.15rem; margin-top: 0;"&gt;Sovereign Auditor Capstone Submission&lt;/h2&gt;
    &lt;p&gt;Submit your completed 5-point Sovereign Auditor Deliverable Matrix. Fencing of raw inputs inside triple-hashes (&lt;code&gt;###&lt;/code&gt;) and documentation of at least 2 human audits is required.&lt;/p&gt;
    &lt;pre style="background-color: #F8F6F0; padding: 12px; border: 1px solid #CBD5E1; font-family: monospace;"&gt;### SOVEREIGN_AUDITOR_MATRIX / MATRIZ_DEL_AUDITOR_SOBERANO
1. Selected Workflow: [Meeting Minutes / Rubric / Syllabus Policy]
2. Estimated Time Reclaimed: [e.g., 45 minutes]
3. Delimited Prompt Input:
###
[Paste triple-hash fenced input here]
###
4. Human Verification &amp; SSoT Cross-Check (Min. 2 documented edits):
   - Correction 1: [Curricular/SSoT accuracy check]
   - Correction 2: [Institutional tone/formatting precision]
5. Auditor Attestation: Confirmed verified via human judgment.&lt;/pre&gt;
  &lt;/div&gt;</description>
  <points_possible>20.0</points_possible>
  <grading_type>points</grading_type>
  <submission_types>
    <submission_type>online_text_entry</submission_type>
    <submission_type>online_upload</submission_type>
  </submission_types>
  <allowed_attempts>3</allowed_attempts>
  <workflow_state>published</workflow_state>
</assignment>
"""

# 3. Community Discussion Topic XML
discussion_xml = """<?xml version="1.0" encoding="UTF-8"?>
<topic identifier="RES_DISC_COMMUNITY" xmlns="http://canvas.instructure.com/xsd/cccv1p0">
  <title>Community Exchange: Reclaiming Our Time Check-In</title>
  <text>&lt;div style="background-color: #FFFFFF; border: 1px solid #CBD5E1; border-left: 5px solid #003366; padding: 18px 20px; border-radius: 4px;"&gt;
    &lt;h3 style="color: #002147; margin-top: 0;"&gt;Welcome to the Workshop Cohort Exchange&lt;/h3&gt;
    &lt;p&gt;Introduce yourself to colleagues across divisions by addressing three concise prompts:&lt;/p&gt;
    &lt;ol&gt;
      &lt;li&gt;&lt;strong&gt;Administrative Bottleneck:&lt;/strong&gt; What routine academic task consumes the most uncompensated time in your week?&lt;/li&gt;
      &lt;li&gt;&lt;strong&gt;The Human Firewall:&lt;/strong&gt; What instructional area must remain strictly under your direct personal judgment?&lt;/li&gt;
      &lt;li&gt;&lt;strong&gt;Colleague Exchange:&lt;/strong&gt; Respond to at least one peer with a shared insight or workflow tip.&lt;/li&gt;
    &lt;/ol&gt;
  &lt;/div&gt;</text>
  <discussion_type>threaded</discussion_type>
  <workflow_state>published</workflow_state>
</topic>
"""

# 4. Canvas SpeedGrader 4-Criterion Rubric (JSON)
rubric_data = {
    "rubric": {
        "title": "Sovereign Auditor Capstone Evaluation Rubric",
        "points_possible": 20,
        "criteria": [
            {
                "id": "crit_ssot_alignment",
                "description": "1. SSoT & Regulatory Alignment",
                "long_description": "Grounds evaluation strictly in governing federal/clinical standards (PAGA 2018 2nd Ed, ADA Title II, Faculty Senate Code). Zero points for unverified external trends.",
                "points": 5,
                "ratings": [
                    {"description": "Exemplary: Complete text citations & explicit standards alignment", "points": 5},
                    {"description": "Competent: Cites standards correctly with minor omissions", "points": 4},
                    {"description": "Developing: Vague mention of standards without specific metrics", "points": 2},
                    {"description": "Inadequate: No SSoT citation or relies on unverified web trends", "points": 0}
                ]
            },
            {
                "id": "crit_delimiter_isolation",
                "description": "2. Delimiter Isolation Protocol",
                "long_description": "Applies strict triple-hash (###) fencing to isolate system instructions from variable user inputs and clinical data.",
                "points": 5,
                "ratings": [
                    {"description": "Exemplary: Flawless triple-hash isolation; zero syntax leakage", "points": 5},
                    {"description": "Competent: Delimiters used with slight structural inconsistency", "points": 4},
                    {"description": "Developing: Incomplete fencing; inputs mix with instructions", "points": 2},
                    {"description": "Inadequate: No delimiter protocol applied", "points": 0}
                ]
            },
            {
                "id": "crit_practicality",
                "description": "3. Curricular Practicality & Intervention",
                "long_description": "Produces actionable, equitable, zero-barrier instructional artifacts (ZTC/OER-friendly, clear action items, accountable owners).",
                "points": 5,
                "ratings": [
                    {"description": "Exemplary: Highly practical, mobile-responsive, zero cost barrier", "points": 5},
                    {"description": "Competent: Practical deliverable with minor logistical hurdles", "points": 4},
                    {"description": "Developing: Deliverable difficult to execute or high resource load", "points": 2},
                    {"description": "Inadequate: Impractical, non-inclusive, or cost-prohibitive", "points": 0}
                ]
            },
            {
                "id": "crit_human_audit",
                "description": "4. Human Verification & Sovereign Audit",
                "long_description": "Documents at least two verifiable human-in-the-loop audits correcting arithmetic, clinical safety, or institutional policy.",
                "points": 5,
                "ratings": [
                    {"description": "Exemplary: >=2 explicit human audits with mathematical/clinical proofs", "points": 5},
                    {"description": "Competent: 1 thorough human audit with source reference", "points": 4},
                    {"description": "Developing: Superficial audit without documented correction", "points": 2},
                    {"description": "Inadequate: Raw AI output accepted without human verification", "points": 0}
                ]
            }
        ]
    }
}

# 5. SpeedGrader CSV Rubric
csv_buffer = io.StringIO()
csv_writer = csv.writer(csv_buffer)
csv_writer.writerow(["Criterion Description", "Points", "Rating Description", "Rating Points"])
for crit in rubric_data["rubric"]["criteria"]:
    for rating in crit["ratings"]:
        csv_writer.writerow([crit["description"], crit["points"], rating["description"], rating["points"]])
csv_content = csv_buffer.getvalue()

# 6. HTML Content Pages for Modules 00-05
def make_page(title, body_content):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{title}</title>
</head>
<body style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; color: #0C2340; background-color: #FFFFFF; padding: 24px; line-height: 1.6;">
  <h2 style="color: #002147; border-bottom: 2px solid #003366; padding-bottom: 8px;">{title}</h2>
  {body_content}
</body>
</html>"""

pages = {
    "module-00.html": make_page(
        "Module 00: Technical Pre-Flight Gate &amp; FERPA Privacy Shield",
        """<div style="background-color: #FFFFFF; border-left: 5px solid #003366; padding: 16px; border: 1px solid #CBD5E1; margin: 16px 0;">
  <h3 style="color: #002147; margin-top: 0;">Enterprise Authentication &amp; Zero Data Retention</h3>
  <p>Before pasting instructional materials or administrative drafts into any GenAI model, verify authentication through your enterprise portal with Single Sign-On (SSO). Never upload unredacted student records protected under FERPA.</p>
</div>"""
    ),
    "module-01.html": make_page(
        "Module 01: Institutional Governance &amp; Syllabus Policy Tiers",
        """<p>Select and customize your course policy tier (Tier 1: Prohibition, Tier 2: Bounded Collaboration, Tier 3: Sovereign Co-Intelligence) to establish transparent expectations.</p>"""
    ),
    "module-02.html": make_page(
        "Module 02: Administrative Triage &amp; Committee Minutes Extraction",
        """<p>Practice extracting actionable matrices (Task, Owner, Deadline) from messy committee transcripts using delimited system prompts.</p>"""
    ),
    "module-03.html": make_page(
        "Module 03: Syntax Lab: Delimited Prompt Architecture",
        """<p>Convert unstructured criteria into calibrated 20-point Canvas SpeedGrader rubrics using triple-hash (###) context fencing.</p>"""
    ),
    "module-04.html": make_page(
        "Module 04: The Safety Auditor: Hallucination Interception",
        """<p>Audit AI outputs against established Single Sources of Truth (SSoT) to identify and correct clinical, mathematical, and policy errors.</p>"""
    )
}

# 7. Build Canvas Common Cartridge (.imscc)
imscc_filename = "reclaiming-our-time-canvas.imscc"
imscc_path = os.path.join(OUTPUT_DIR, imscc_filename)

with zipfile.ZipFile(imscc_path, "w", zipfile.ZIP_DEFLATED) as zf:
    zf.writestr("imsmanifest.xml", manifest_xml)
    zf.writestr("assignments/capstone-matrix.xml", assignment_xml)
    zf.writestr("discussions/community-checkin.xml", discussion_xml)
    for path, content in pages.items():
        zf.writestr(f"wiki_content/{path}", content)
    zf.writestr("course_settings/rubric_speedgrader.json", json.dumps(rubric_data, indent=2))

print(f"Generated Canvas Cartridge: {imscc_path} ({os.path.getsize(imscc_path)} bytes)")

# 8. Build Companion Facilitator Bundle (.zip)
bundle_filename = "reclaiming-our-time-canvas-bundle.zip"
bundle_path = os.path.join(OUTPUT_DIR, bundle_filename)

readme_text = """======================================================================
RECLAIMING OUR TIME: CANVAS LMS INGEST & FACILITATOR PACKAGE
======================================================================
This bundle provides direct ingestion artifacts for Canvas LMS.

PACKAGE CONTENTS:
1. reclaiming-our-time-canvas.imscc
   - Native Canvas Common Cartridge (Modules 00-05, Capstone, Discussion)
2. canvas_speedgrader_rubric.json
   - 4-criterion, 20-point Sovereign Auditor Rubric (Canvas native JSON format)
3. canvas_speedgrader_rubric.csv
   - SpeedGrader Rubric in spreadsheet format for bulk-import tools
4. canvas_assignment_spec.xml
   - SpeedGrader submission definition (allowed attempts, point total)

INSTRUCTIONS FOR CANVAS INGESTION:
1. In your Canvas course shell, go to Settings > Import Course Content.
2. Under "Content Type", select: Common Cartridge 1.x Package.
3. Choose the file: reclaiming-our-time-canvas.imscc.
4. Select "All content" and click "Import".
5. In SpeedGrader, attach the 20-point Sovereign Auditor Rubric directly
   to the Summative Capstone Assignment.
======================================================================
"""

with zipfile.ZipFile(bundle_path, "w", zipfile.ZIP_DEFLATED) as bz:
    bz.writestr(imscc_filename, open(imscc_path, "rb").read())
    bz.writestr("canvas_speedgrader_rubric.json", json.dumps(rubric_data, indent=2))
    bz.writestr("canvas_speedgrader_rubric.csv", csv_content)
    bz.writestr("canvas_assignment_spec.xml", assignment_xml)
    bz.writestr("README_CANVAS_INGEST.txt", readme_text)

print(f"Generated Facilitator Bundle: {bundle_path} ({os.path.getsize(bundle_path)} bytes)")
