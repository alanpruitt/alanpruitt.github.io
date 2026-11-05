import re
from bs4 import BeautifulSoup

def audit_accessibility_rules(html_content, css_content):
    """
    Scans HTML and CSS for WCAG 2.2 non-text contrast (3:1), target size (24x24px),
    and focus-visible outline compliance.
    """
    issues = []
    soup = BeautifulSoup(html_content, 'html.parser')

    # 1. Check Target Sizes (WCAG 2.5.8, Level AA)
    interactive_elements = soup.find_all(['button', 'input', 'a', 'select'])
    for el in interactive_elements:
        style = el.get('style', '')
        width_match = re.search(r'width:\s*(\d+)px', style)
        height_match = re.search(r'height:\s*(\d+)px', style)
        
        if width_match and int(width_match.group(1)) < 24:
            issues.append(f"Target Size Violation: Element <{el.name}> width is under 24px.")
        if height_match and int(height_match.group(1)) < 24:
            issues.append(f"Target Size Violation: Element <{el.name}> height is under 24px.")

    # 2. Check Non-Text Contrast (WCAG 1.4.11, Level AA)
    ui_selectors = re.findall(r'(\.[a-zA-Z0-9_-]*(?:button|input|icon|border)[a-zA-Z0-9_-]*)\s*\{([^}]*)\}', css_content)
    for selector, rules in ui_selectors:
        if 'border' in rules or 'outline' in rules:
            if 'transparent' in rules:
                issues.append(f"Non-Text Contrast Risk: Selector '{selector}' uses transparent borders, risking < 3:1 contrast.")

    # 3. Check Focus Visible (WCAG 2.4.7, Level AA)
    # Scans for selectors utilizing ':focus' and flags hazardous 'outline: none' / 'outline: 0' 
    # unless an alternative visual indicator (box-shadow or custom border) is present.
    focus_rules = re.findall(r'([a-zA-Z0-9_.-]+(?:\s*:\s*focus)?)\s*\{([^}]*)\}', css_content)
    for selector, rules in focus_rules:
        if ':focus' in selector:
            has_no_outline = bool(re.search(r'outline\s*:\s*(?:none|0)', rules))
            has_fallback = bool(re.search(r'(box-shadow|border)', rules))
            
            if has_no_outline and not has_fallback:
                issues.append(f"Focus Visible Violation: Selector '{selector}' removes the outline without providing a visible focus fallback.")

    return issues

# Example execution with a focus violation test case
if __name__ == "__main__":
    sample_html = '<button class="btn">Submit</button>'
    sample_css = '.btn:focus { outline: none; }'  # Triggers violation
    
    detected_issues = audit_accessibility_rules(sample_html, sample_css)
    for issue in detected_issues:
        print(f"[LINTER ALERT] {issue}")
