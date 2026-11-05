#!/usr/bin/env bash
### Automated Local Verification Runner for WCAG 3.0 Atomic Linter
set -eo pipefail

echo "========================================================"
echo " Running Local WCAG 3.0 Atomic Linter Verification Suite "
echo "========================================================"

REPORT_FILE="wcag3_test_report.json"

# Execute linter across both test fixtures
python3 .github/scripts/wcag3_linter.py \
  --json-out "$REPORT_FILE" \
  tests/fixtures/test_suite_failing.html \
  tests/fixtures/test_suite_failing.md || LINTER_EXIT_CODE=$?

echo ""
echo "--------------------------------------------------------"
echo " Linter Process Exited with Code: ${LINTER_EXIT_CODE:-0}"
echo "--------------------------------------------------------"

# Verify that report was generated
if [[ ! -f "$REPORT_FILE" ]]; then
  echo "[-] FAILURE: Report file $REPORT_FILE was not generated!"
  exit 1
fi

# Audit failure counts using Python one-liner
python3 -c "
import json
with open('$REPORT_FILE') as f:
    data = json.load(f)
failures = data['summary']['failures']
print(f'[+] Detected Blocking Failures: {failures}')
assert failures >= 9, f'Expected at least 9 failures, found {failures}'
print('[+] Test Suite PASSED: All atomic violations successfully intercepted.')
"
