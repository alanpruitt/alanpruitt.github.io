#!/usr/bin/env bash
set -eo pipefail

echo "========================================================"
echo " Running Course Syllabus Audits with gemma4:e2b         "
echo "========================================================"

python3 scripts/run_syllabus_audits.py

echo "========================================================"
echo " All Syllabus Audits Completed!                         "
echo "========================================================"
