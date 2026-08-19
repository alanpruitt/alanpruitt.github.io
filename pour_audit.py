#!/usr/bin/env python3
"""
POUR Accessibility Audit Script for EXW Course Fleet
Audits Markdown and HTML files against Perceivable, Operable, Understandable, and Robust standards.
"""

import os
import re
import sys

def audit_file(filepath):
    print(f"Auditing [POUR]: {filepath}")
    errors = []
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # 1. ROBUST AUDIT: Check heading hierarchy (must start at h2, no skipped levels)
    headings = re.findall(r'(<h([2-6])>|^(#{1,6})\s+)', content, re.MULTILINE)
    last_level = 1 # Canvas page title is h1, content starts at h2
    
    for h in headings:
        if h[1]:
            level = int(h[1])
        elif h[2]:
            level = len(h[2])
        else:
            continue
            
        if last_level == 1 and level != 2:
            errors.append(f"[Robust] Structure Violation: First content heading must be <h2>, found <h{level}>.")
        elif level > last_level + 1:
            errors.append(f"[Robust] Hierarchy Violation: Skipped heading level from <h{last_level}> to <h{level}>.")
        last_level = level

    # 2. PERCEIVABLE AUDIT: Check for missing or empty alt text in images
    img_tags = re.findall(r'<img\s+[^>]*>', content, re.IGNORECASE)
    for img in img_tags:
        if 'alt=' not in img or 'alt=""' in img or "alt='''" in img:
            errors.append(f"[Perceivable] Image missing descriptive alt text -> {img}")

    # 3. UNDERSTANDABLE AUDIT: Check for deprecated or non-standard structural tags/terms
    if "8.#" in content:
        errors.append("[Understandable] Legacy Reference: Found prohibited '8.#'-style reference.")

    return errors

def run_pour_audit(directory):
    total_errors = 0
    scanned_files = 0
    
    for root, _, files in os.walk(directory):
        # Skip hidden directories like .git or node_modules
        if '.git' in root or 'node_modules' in root:
            continue
            
        for file in files:
            if file.endswith(('.md', '.html')):
                filepath = os.path.join(root, file)
                scanned_files += 1
                errors = audit_file(filepath)
                if errors:
                    total_errors += len(errors)
                    print(f"  [FAIL] {file}:")
                    for err in errors:
                        print(f"    - {err}")
                else:
                    print(f"  [PASS] {file}")
                    
    print(f"\n--- POUR Audit Summary ---")
    print(f"Files scanned: {scanned_files}")
    print(f"Total violations found: {total_errors}")
    
    if total_errors > 0:
        sys.exit(1)
    else:
        print("All files passed the POUR-Audit successfully!")
        sys.exit(0)

if __name__ == "__main__":
    target_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    run_pour_audit(target_dir)
