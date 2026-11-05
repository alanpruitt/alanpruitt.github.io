#!/usr/bin/env bash
set -eo pipefail

COURSES=("EXW101" "EXW150" "EXW245" "EXW265")
AUDIT_DIR="audits"
mkdir -p "$AUDIT_DIR"

echo "========================================================"
echo " Starting Automated Welcome Page Audits (gemma4:e2b)    "
echo "========================================================"

for course in "${COURSES[@]}"; do
  file="content/courses/${course}/home.md"
  output_file="${AUDIT_DIR}/${course}-home-audit.txt"
  
  if [ -f "$file" ]; then
    echo "[+] Auditing Welcome Page for ${course}..."
    cat "$file" | ollama run gemma4:e2b "### Audit this Welcome (Home Page) for ${course}. Verify that:
    1. Heading hierarchies start strictly at h2 (reserving h1 for Canvas).
    2. Tone is welcoming, clear, and appropriately calibrated (${course} introductory vs. transfer rigor).
    3. Formatting uses scannable bullet points and avoids dense text walls. ###" \
    > "$output_file"
    echo "    Completed ${course} -> ${output_file} ($(wc -l < "$output_file") lines)"
  else
    echo "[-] File not found for ${course}: $file"
  fi
done

echo "========================================================"
echo " All Welcome Page Audits Completed Successfully!        "
echo "========================================================"
