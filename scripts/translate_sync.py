#!/usr/bin/env python3
"""
Script: translate_sync.py
Purpose: Validates English/Spanish content alignment and delegates sequential essay
         integrity checks to scripts/essay_registry_audit.py.
"""

import os
import subprocess
import sys

CONTENT_EN = "content/en/essays"
CONTENT_ES = "content/es/essays"


def main():
    en_files = {
        fn for fn in os.listdir(CONTENT_EN)
        if fn.endswith(".md") and fn != "_index.md"
    }
    es_files = {
        fn for fn in os.listdir(CONTENT_ES)
        if fn.endswith(".md") and fn != "_index.md"
    } if os.path.exists(CONTENT_ES) else set()

    orphaned_es = sorted(es_files - en_files)
    if orphaned_es:
        print(f"[FAIL] Orphaned Spanish essay file(s) with no matching English canonical file: {orphaned_es}")
        sys.exit(1)

    print(
        f"[TRANSLATION SYNC] Verified {len(en_files)} English canonical essays and "
        f"{len(es_files)} bilingual Spanish mirrors (0 orphaned routes)."
    )
    res = subprocess.run([sys.executable, "scripts/essay_registry_audit.py", "--ci"])
    sys.exit(res.returncode)


if __name__ == "__main__":
    main()
