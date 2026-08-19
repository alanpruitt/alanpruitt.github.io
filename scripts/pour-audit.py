import os
import re
import sys

def audit_file(filepath):
    print(f"Auditing: {filepath}")
    errors = []
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Check heading hierarchy (must start at h2, no skipping levels)
    # Finding all HTML/Markdown headers
    headings = re.findall(r'(<h([2-6])>|^(#{1,6})\s+)', content, re.MULTILINE)
    
    last_level = 1 # Canvas page title is h1, so content should start at h2
    for h in headings:
        # Determine level based on html tag or markdown hashes
        if h[1]:
            level = int(h[1])
        elif h[2]:
            level = len(h[2])
        else:
            continue
            
        if last_level == 1 and level != 2:
            errors.append(f"Structure Violation: First content heading must be <h2>, found <h{level}>.")
        elif level > last_level + 1:
            errors.append(f"Hierarchy Violation: Skipped heading level from <h{last_level}> to <h{level}>.")
        last_level = level

    # Check for missing alt text in images
    img_tags = re.findall(r'<img\s+[^>]*>', content, re.IGNORECASE)
    for img in img_tags:
        if 'alt=' not in img or 'alt=""' in img or "alt=''" in img:
            errors.append(f"Perceivable Violation: Image missing descriptive alt text -> {img}")

    return errors

def run_audit(directory):
    total_errors = 0
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(('.md', '.html')):
                filepath = os.path.join(root, file)
                errors = audit_file(filepath)
                if errors:
                    total_errors += len(errors)
                    print(f"  [FAIL] {file}:")
                    for err in errors:
                        print(f"    - {err}")
                else:
                    print(f"  [PASS] {file}")
                    
    if total_errors > 0:
        print(f"\nAudit completed with {total_errors} accessibility violations.")
        sys.exit(1)
    else:
        print("\nAll files passed the POUR structural audit successfully!")
        sys.exit(0)

if __name__ == "__main__":
    target_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    run_audit(target_dir)
