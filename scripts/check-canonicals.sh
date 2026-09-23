#!/bin/bash
# Pre-push Canonical Integrity Check
# Scans built HTML files for canonical tags referencing index.html

echo "🔍 Auditing HTML files for trailing index.html canonicals..."

# Match <link ...> elements with rel=canonical (quoted or minified) referencing index.html
CANONICAL_PATTERN='<link[^>]+(rel=["'"'"']?canonical["'"'"']?[^>]*index\.html|index\.html[^>]*rel=["'"'"']?canonical)'

BAD_CANONICALS=$(find . -name "*.html" -type f \
    -not -path "*/node_modules/*" \
    -not -path "*/.git/*" \
    -exec grep -E -i -l "$CANONICAL_PATTERN" {} +)

if [ -n "$BAD_CANONICALS" ]; then
    echo "❌ ERROR: Found canonical tags pointing to index.html:"
    echo "$BAD_CANONICALS"
    echo "💡 Fix: Strip 'index.html' from your canonical URLs to maintain clean directory paths."
    exit 1
else
    echo "✅ Success: All canonical tags adhere to clean directory best practices."
    exit 0
fi
