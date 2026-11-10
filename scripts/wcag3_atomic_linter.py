#!/usr/bin/env python3
"""
WCAG 3.0 Atomic Linter Engine with Line-Level Annotation & Automated Suggestion Support
Evaluates HTML/Markdown DOM nodes and formats output for GitHub Actions.
"""

import sys
import os
import re
import json
import argparse
from typing import List, Dict, Any, Set, Tuple

class WCAG3AtomicAuditor:
    def __init__(self, content: str, filepath: str = ""):
        self.raw_content = content
        self.lines = content.splitlines()
        self.filepath = filepath
        self.violations: List[Dict[str, Any]] = []

    def _get_line_number(self, index: int) -> int:
        """Calculates 1-based line number from a character index."""
        return self.raw_content.count('\n', 0, index) + 1

    def _get_line_text(self, line_no: int) -> str:
        """Safely gets text of 1-based line number."""
        if 1 <= line_no <= len(self.lines):
            return self.lines[line_no - 1]
        return ""

    def audit_heading_progression(self) -> None:
        """Outcome: Structured Headings - Enforces h2 start and linear hierarchy across HTML and Markdown."""
        levels: List[Tuple[int, int]] = []
        in_fence = False

        for line_idx, line in enumerate(self.lines):
            line_no = line_idx + 1
            stripped = line.strip()

            if stripped.startswith("```") or stripped.startswith("~~~"):
                in_fence = not in_fence
                continue
            if in_fence:
                continue

            # Ignore structural Centaur/prompt delimiters, table rows, and protocol bounds
            if (
                stripped in ["###", "> ###"]
                or stripped.startswith("### STRUCTURAL_DELIMITER")
                or stripped.startswith("### |")
                or (stripped.startswith("###") and stripped.endswith("###"))
                or re.match(r"^[\s>]*###[\s>]*$", line)
            ):
                continue

            line_no_inline_code = re.sub(r"`[^`]*`", "", line)
            h_html = re.search(r"<h([1-6])\b[^>]*>", line_no_inline_code, re.IGNORECASE)
            h_md = re.match(r"^(#{1,6})\s+\S+", line_no_inline_code)

            level = None
            if h_html:
                level = int(h_html.group(1))
            elif h_md:
                level = len(h_md.group(1))

            if level is not None:
                levels.append((level, line_no))

        if not levels:
            return

        # Check for reserved <h1>
        for level, line_no in levels:
            if level == 1:
                line_text = self._get_line_text(line_no)
                sugg = re.sub(r'<h1\b', '<h2', line_text, flags=re.IGNORECASE)
                sugg = re.sub(r'</h1>', '</h2>', sugg, flags=re.IGNORECASE)
                if sugg == line_text and line_text.lstrip().startswith('# '):
                    sugg = re.sub(r'^(\s*)# ', r'\1## ', line_text)
                self.violations.append({
                    "rule": "RULE_HEAD_ROOT",
                    "severity": "FAIL",
                    "line": line_no,
                    "col": 1,
                    "outcome": "Structure: Heading Hierarchy",
                    "message": "Found <h1> tag. Embedded content must begin at <h2> to preserve platform title hierarchy.",
                    "suggestion": sugg if sugg != line_text else None
                })

        # Check first heading is <h2>
        first_level, first_line = levels[0]
        if first_level != 2:
            line_text = self._get_line_text(first_line)
            sugg = re.sub(rf'<h{first_level}\b', '<h2', line_text, flags=re.IGNORECASE)
            sugg = re.sub(rf'</h{first_level}>', '</h2>', sugg, flags=re.IGNORECASE)
            if sugg == line_text and line_text.lstrip().startswith('#'):
                sugg = re.sub(r'^(\s*)#{1,6}\s+', r'\1## ', line_text)
            self.violations.append({
                "rule": "RULE_HEAD_START",
                "severity": "FAIL",
                "line": first_line,
                "col": 1,
                "outcome": "Structure: Heading Hierarchy",
                "message": f"First heading is <h{first_level}>. Expected <h2>.",
                "suggestion": sugg if sugg != line_text else None
            })

        # Check linear progression (no skipped levels)
        for i in range(len(levels) - 1):
            curr_lvl, _ = levels[i]
            next_lvl, next_line = levels[i + 1]
            if next_lvl > curr_lvl + 1:
                target_lvl = curr_lvl + 1
                line_text = self._get_line_text(next_line)
                sugg = re.sub(rf'<h{next_lvl}\b', f'<h{target_lvl}', line_text, flags=re.IGNORECASE)
                sugg = re.sub(rf'</h{next_lvl}>', f'</h{target_lvl}>', sugg, flags=re.IGNORECASE)
                if sugg == line_text and line_text.lstrip().startswith('#'):
                    sugg = re.sub(r'^(\s*)#{1,6}\s+', rf'\1{"#" * target_lvl} ', line_text)
                self.violations.append({
                    "rule": "RULE_HEAD_NO_SKIP",
                    "severity": "FAIL",
                    "line": next_line,
                    "col": 1,
                    "outcome": "Structure: Heading Progression",
                    "message": f"Heading hierarchy skipped from <h{curr_lvl}> to <h{next_lvl}>.",
                    "suggestion": sugg if sugg != line_text else None
                })

    def audit_image_alternatives(self) -> None:
        """Outcome: Text Alternatives - Presence and character budget across HTML and Markdown."""
        img_pattern = re.compile(r'<img\s+([^>]+)>', re.IGNORECASE)
        for match in img_pattern.finditer(self.raw_content):
            tag_attrs = match.group(1)
            line_no = self._get_line_number(match.start())
            alt_match = re.search(r'alt=["\'](.*?)["\']', tag_attrs, re.IGNORECASE)

            if not alt_match:
                line_text = self._get_line_text(line_no)
                sugg = re.sub(r'<img\b', '<img alt="Descriptive image summary"', line_text, count=1, flags=re.IGNORECASE)
                self.violations.append({
                    "rule": "RULE_ALT_EXISTS",
                    "severity": "FAIL",
                    "line": line_no,
                    "col": 1,
                    "outcome": "Alternative Text: Presence",
                    "message": "Missing alt attribute on <img> element.",
                    "suggestion": sugg if sugg != line_text else None
                })
            else:
                alt_text = alt_match.group(1).strip()
                if len(alt_text) > 120:
                    self.violations.append({
                        "rule": "RULE_ALT_LENGTH_120",
                        "severity": "WARNING",
                        "line": line_no,
                        "col": 1,
                        "outcome": "Alternative Text: Density Budget",
                        "message": f"Alt text exceeds 120-character limit ({len(alt_text)} chars): '{alt_text[:25]}...'"
                    })

        # Markdown image syntax: ![alt](url)
        md_img_pattern = re.compile(r'!\[(.*?)\]\((.*?)\)')
        for line_idx, line in enumerate(self.lines):
            line_no = line_idx + 1
            for match in md_img_pattern.finditer(line):
                alt_text = match.group(1).strip()
                if not alt_text:
                    line_text = self._get_line_text(line_no)
                    sugg = line_text.replace("![](", '![Descriptive image summary](')
                    self.violations.append({
                        "rule": "RULE_ALT_EXISTS",
                        "severity": "FAIL",
                        "line": line_no,
                        "col": 1,
                        "outcome": "Alternative Text: Presence",
                        "message": "Empty alt-text detected in Markdown image.",
                        "suggestion": sugg if sugg != line_text else None
                    })
                elif len(alt_text) > 120:
                    self.violations.append({
                        "rule": "RULE_ALT_LENGTH_120",
                        "severity": "WARNING",
                        "line": line_no,
                        "col": 1,
                        "outcome": "Alternative Text: Density Budget",
                        "message": f"Markdown alt-text exceeds 120 characters ({len(alt_text)} chars): '{alt_text[:25]}...'"
                    })

    def audit_tabular_semantics(self) -> None:
        """Outcome: Tabular Grid Semantics - Caption and explicit scope validation."""
        table_pattern = re.compile(r'<table\b[^>]*>(.*?)</table>', re.IGNORECASE | re.DOTALL)
        for table_match in table_pattern.finditer(self.raw_content):
            table_body = table_match.group(1)
            table_line = self._get_line_number(table_match.start())

            # Caption verification
            caption_match = re.search(r'<caption\b[^>]*>(.*?)</caption>', table_body, re.IGNORECASE | re.DOTALL)
            if not caption_match or not caption_match.group(1).strip():
                line_text = self._get_line_text(table_line)
                indent = len(line_text) - len(line_text.lstrip())
                indent_str = line_text[:indent]
                sugg = f"{line_text}\n{indent_str}  <caption>Accessible Table Description</caption>"
                self.violations.append({
                    "rule": "RULE_TABLE_CAPTION",
                    "severity": "FAIL",
                    "line": table_line,
                    "col": 1,
                    "outcome": "Tabular Semantics: Accessible Name",
                    "message": "Table missing an accessible, non-empty <caption> element.",
                    "suggestion": sugg
                })

            # Explicit th scope verification
            th_pattern = re.compile(r'<th\b([^>]*)>', re.IGNORECASE)
            for th_match in th_pattern.finditer(table_body):
                attrs = th_match.group(1)
                th_line = self._get_line_number(table_match.start(1) + th_match.start())
                scope_match = re.search(r'scope=["\'](col|row|colgroup|rowgroup)["\']', attrs, re.IGNORECASE)
                if not scope_match:
                    line_text = self._get_line_text(th_line)
                    sugg = re.sub(r'<th\b(?![^>]*\bscope=)', '<th scope="col"', line_text, count=1, flags=re.IGNORECASE)
                    self.violations.append({
                        "rule": "RULE_TABLE_TH_SCOPE",
                        "severity": "FAIL",
                        "line": th_line,
                        "col": 1,
                        "outcome": "Tabular Semantics: Header Scope",
                        "message": "<th> tag missing valid scope attribute ('col' or 'row').",
                        "suggestion": sugg if sugg != line_text else None
                    })

    def audit_form_control_bindings(self) -> None:
        """Outcome: Form Control Binding - Explicit for/id link or parent wrapping."""
        label_for_targets = set(re.findall(r'<label\b[^>]*\bfor=["\']([^"\']+)["\']', self.raw_content, re.IGNORECASE))
        interactive_pattern = re.compile(r'<(input|select|textarea)\b([^>]*)>', re.IGNORECASE)
        
        seen_ids: Set[str] = set()

        for match in interactive_pattern.finditer(self.raw_content):
            tag_name = match.group(1).lower()
            attrs = match.group(2)
            line_no = self._get_line_number(match.start())

            type_match = re.search(r'type=["\']([^"\']+)["\']', attrs, re.IGNORECASE)
            input_type = type_match.group(1).lower() if type_match else "text"
            if input_type in {"hidden", "submit", "reset", "button"}:
                continue

            id_match = re.search(r'id=["\']([^"\']+)["\']', attrs, re.IGNORECASE)
            ctrl_id = id_match.group(1) if id_match else None

            # Duplicate ID validation
            if ctrl_id:
                if ctrl_id in seen_ids:
                    self.violations.append({
                        "rule": "RULE_FORM_ID_COLLISION",
                        "severity": "FAIL",
                        "line": line_no,
                        "col": 1,
                        "outcome": "Form Semantics: Identity Uniqueness",
                        "message": f"Duplicate form control id='{ctrl_id}' detected."
                    })
                seen_ids.add(ctrl_id)

            # Association test
            is_bound_explicitly = ctrl_id and (ctrl_id in label_for_targets)
            control_snippet = match.group(0)
            is_bound_implicitly = bool(re.search(
                rf'<label\b[^>]*>(?:(?!</label>).)*?{re.escape(control_snippet)}.*?</label>',
                self.raw_content,
                re.IGNORECASE | re.DOTALL
            ))

            if not (is_bound_explicitly or is_bound_implicitly):
                label_target = f"id='{ctrl_id}'" if ctrl_id else f"<{tag_name}>"
                line_text = self._get_line_text(line_no)
                sugg = None
                if ctrl_id:
                    indent = len(line_text) - len(line_text.lstrip())
                    indent_str = line_text[:indent]
                    sugg = f"{indent_str}<label for=\"{ctrl_id}\">Label:</label>\n{line_text}"
                self.violations.append({
                    "rule": "RULE_FORM_EXPLICIT_LABEL",
                    "severity": "FAIL",
                    "line": line_no,
                    "col": 1,
                    "outcome": "Form Semantics: Label Association",
                    "message": f"Form control ({label_target}) lacks an associated <label> via 'for' link or nesting.",
                    "suggestion": sugg
                })

    def run_suite(self) -> List[Dict[str, Any]]:
        self.audit_heading_progression()
        self.audit_image_alternatives()
        self.audit_tabular_semantics()
        self.audit_form_control_bindings()
        return self.violations

# Alias for backwards-compatibility
WCAG3AtomicAuditorExtended = WCAG3AtomicAuditor

def parse_args():
    parser = argparse.ArgumentParser(description="WCAG 3.0 Atomic Accessibility Linter")
    parser.add_argument("files", nargs="*", help="List of files to audit")
    parser.add_argument("--json-out", dest="json_out", default=None, help="Path to write JSON violation report")
    return parser.parse_args()

def main():
    args = parse_args()
    if not args.files:
        print("No files specified for audit.")
        sys.exit(0)

    all_violations: List[Dict[str, Any]] = []
    total_failures = 0
    total_warnings = 0

    for filepath in args.files:
        if not os.path.exists(filepath):
            continue

        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        auditor = WCAG3AtomicAuditor(content, filepath)
        results = auditor.run_suite()

        for v in results:
            v_record = {
                "file": filepath,
                "line": v["line"],
                "col": v["col"],
                "rule": v["rule"],
                "severity": v["severity"],
                "outcome": v["outcome"],
                "message": v["message"],
                "suggestion": v.get("suggestion")
            }
            all_violations.append(v_record)

            cmd = "error" if v["severity"] == "FAIL" else "warning"
            print(f"::{cmd} file={filepath},line={v['line']},col={v['col']},title={v['rule']} - {v['outcome']}::{v['message']}")

            if v["severity"] == "FAIL":
                total_failures += 1
            else:
                total_warnings += 1

    # Emit JSON payload if requested
    if args.json_out:
        report_data = {
            "summary": {
                "total_files": len(args.files),
                "failures": total_failures,
                "warnings": total_warnings
            },
            "violations": all_violations
        }
        with open(args.json_out, "w", encoding="utf-8") as jf:
            json.dump(report_data, jf, indent=2)

    print(f"\nAudit completed: {total_failures} blocking error(s), {total_warnings} warning(s).")
    
    # Non-zero exit code on failure
    if total_failures > 0:
        sys.exit(1)
    sys.exit(0)

if __name__ == "__main__":
    main()
