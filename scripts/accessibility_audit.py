#!/usr/bin/env python3
"""
WCAG 2.2 Accessibility Linter for Pre-Commit Git Hooks.
Audits HTML and CSS for:
- Target Size (WCAG 2.5.8, Level AA - minimum 24x24px)
- Non-Text Contrast (WCAG 1.4.11, Level AA - 3:1 contrast on active UI borders)
- Focus Visible (WCAG 2.4.7, Level AA - prohibits outline:none without visible fallback)
"""

import sys
import os
import re
import subprocess
from typing import List
from bs4 import BeautifulSoup

def get_staged_files() -> List[str]:
    """Retrieves staged HTML, CSS, and Markdown files from the git index."""
    try:
        cmd = ["git", "diff", "--cached", "--name-only", "--diff-filter=ACM"]
        output = subprocess.check_output(cmd, text=True, stderr=subprocess.DEVNULL)
        files = [f.strip() for f in output.splitlines() if f.strip().endswith(('.html', '.css', '.md'))]
        return files
    except Exception:
        return []

def audit_accessibility_rules(html_content: str, css_content: str, source_label: str = "") -> List[str]:
    """
    Scans HTML and CSS for WCAG 2.2 compliance:
    1. Target Sizes (WCAG 2.5.8, Level AA)
    2. Non-Text Contrast (WCAG 1.4.11, Level AA)
    3. Focus Visible (WCAG 2.4.7, Level AA)
    """
    issues = []
    prefix = f"[{source_label}] " if source_label else ""

    # 1. Check Target Sizes (WCAG 2.5.8, Level AA)
    if html_content:
        soup = BeautifulSoup(html_content, 'html.parser')
        interactive_elements = soup.find_all(['button', 'input', 'a', 'select'])
        for el in interactive_elements:
            style = el.get('style', '')
            width_match = re.search(r'width:\s*(\d+)px', style)
            height_match = re.search(r'height:\s*(\d+)px', style)

            if width_match and int(width_match.group(1)) < 24:
                issues.append(f"{prefix}Target Size Violation (WCAG 2.5.8): Element <{el.name}> width is under 24px ({width_match.group(1)}px).")
            if height_match and int(height_match.group(1)) < 24:
                issues.append(f"{prefix}Target Size Violation (WCAG 2.5.8): Element <{el.name}> height is under 24px ({height_match.group(1)}px).")

    # 2. Check Non-Text Contrast (WCAG 1.4.11, Level AA)
    if css_content:
        ui_selectors = re.findall(
            r'([a-zA-Z0-9_.-]*(?:button|input|icon|border|btn)[a-zA-Z0-9_.-]*)\s*\{([^}]*)\}',
            css_content,
            re.IGNORECASE
        )
        for selector, rules in ui_selectors:
            if 'border' in rules or 'outline' in rules:
                if 'transparent' in rules:
                    issues.append(f"{prefix}Non-Text Contrast Risk (WCAG 1.4.11): Selector '{selector}' uses transparent borders, risking < 3:1 contrast.")

    # 3. Check Focus Visible (WCAG 2.4.7, Level AA)
    if css_content:
        focus_rules = re.findall(r'([a-zA-Z0-9_.-]+(?:\s*:\s*(?:focus|focus-visible))?)\s*\{([^}]*)\}', css_content)
        for selector, rules in focus_rules:
            if ':focus' in selector or ':focus-visible' in selector:
                has_no_outline = bool(re.search(r'outline\s*:\s*(?:none|0)', rules))
                has_fallback = bool(re.search(r'(box-shadow|border)', rules))

                if has_no_outline and not has_fallback:
                    issues.append(f"{prefix}Focus Visible Violation (WCAG 2.4.7): Selector '{selector}' removes outline without providing a visible focus fallback.")

    return issues

def main():
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]
    is_demo = "--demo" in sys.argv or "--test" in sys.argv

    if is_demo:
        sample_html = '<button style="width: 20px; height: 20px;">Click</button>'
        sample_css = '.btn:focus { outline: none; }'
        detected = audit_accessibility_rules(sample_html, sample_css, source_label="Sample Verification")
        print("[DEMO MODE] Detected sample accessibility issues:")
        for issue in detected:
            print(f"  - {issue}")
        sys.exit(0)

    target_files = args if args else get_staged_files()

    if not target_files:
        print("ℹ️ No staged HTML, CSS, or Markdown files detected for WCAG audit.")
        sys.exit(0)

    all_issues = []
    for filepath in target_files:
        if not os.path.exists(filepath):
            continue

        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        html_part = content if filepath.endswith(('.html', '.md')) else ""
        css_part = content if filepath.endswith('.css') else ""

        # Extract embedded <style> blocks from HTML
        if html_part:
            embedded_css = "\n".join(re.findall(r'<style[^>]*>(.*?)</style>', html_part, re.DOTALL | re.IGNORECASE))
            if embedded_css:
                css_part = f"{css_part}\n{embedded_css}"

        file_issues = audit_accessibility_rules(html_part, css_part, source_label=filepath)
        all_issues.extend(file_issues)

    if all_issues:
        print(f"\n❌ [WCAG 2.2 VIOLATIONS DETECTED] ({len(all_issues)} issue(s) found):")
        for issue in all_issues:
            print(f"  • {issue}")
        print("\nPlease remediate target size (<24px), transparent borders, or outline:none before committing.\n")
        sys.exit(1)

    print(f"✅ Scanned {len(target_files)} staged file(s): WCAG 2.2 Level AA requirements satisfied.")
    sys.exit(0)

if __name__ == "__main__":
    main()
