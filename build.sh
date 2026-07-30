#!/usr/bin/env bash
# Local Curriculum-as-Code Build & Validation Script for alanpruitt.com

set -e

echo "=== Running alanpruitt.com Local Build Checks ==="

# 1. Ensure required directories exist
mkdir -p src/articles
mkdir -p articles

# 2. Check for raw Markdown sources
MD_COUNT=$(find src/articles -name "*.md" | wc -l | tr -d ' ')
echo "[✓] Found ${MD_COUNT} raw Markdown source files in src/articles/"

# 3. List compiled production HTML files
HTML_COUNT=$(find articles -name "*.html" | wc -l | tr -d ' ')
echo "[✓] Found ${HTML_COUNT} production HTML files in articles/"

echo "=== Build Check Complete: Ready for Git Commit ==="
