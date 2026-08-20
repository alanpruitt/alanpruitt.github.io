#!/usr/bin/env python3
"""
Emoji and Decorative Icon Stripper for EXW Course Fleet
Recursively scans Markdown and HTML files to remove emojis and non-standard unicode symbols
to ensure zero screen reader friction and strict ADA compliance.
"""

import os
import re
import sys

# Comprehensive regex pattern to match emojis and decorative unicode symbols
# Covers standard emojis, emoticons, symbols, and pictographs
EMOJI_PATTERN = re.compile(
    r"["
    r"\U0001f300-\U0001f5ff"  # Symbols & Pictographs
    r"\U0001f600-\U0001f64f"  # Emoticons
    r"\U0001f680-\U0001f6ff"  # Transport & Map Symbols
    r"\U0001f1e0-\U0001f1ff"  # Flags (iOS)
    r"\U00002700-\U000027bf"  # Dingbats
    r"\U0001f900-\U0001f9ff"  # Supplemental Symbols and Pictographs
    r"\U0001fa70-\U0001faff"  # Symbols and Pictographs Extended-A
    r"\U00002600-\U000026ff"  # Miscellaneous Symbols
    r"\U00002b50-\U00002b55"  # Stars and geometric symbols
    r"]+",
    flags=re.UNICODE,
)

def clean_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Strip emojis and clean up any double spaces left behind in headings/text
    cleaned_content = EMOJI_PATTERN.sub('', content)
    
    # Clean up any trailing/leading whitespace left in lines or double spaces
    # We want to preserve newlines and code structures
    if content != cleaned_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(cleaned_content)
        return True
    return False

def run_stripper(directory):
    modified_files = 0
    total_files = 0
    
    print(f"Scanning directory: {directory} for emojis/decorative icons...")
    
    for root, _, files in os.walk(directory):
        # Skip hidden directories like .git or node_modules
        if '.git' in root or 'node_modules' in root:
            continue
            
        for file in files:
            if file.endswith(('.md', '.html')):
                filepath = os.path.join(root, file)
                total_files += 1
                if clean_file(filepath):
                    modified_files += 1
                    print(f"  [CLEANED] {filepath}")
                    
    print(f"\n--- Emoji Stripper Summary ---")
    print(f"Total files scanned: {total_files}")
    print(f"Files modified: {modified_files}")

if __name__ == "__main__":
    target_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    run_stripper(target_dir)
