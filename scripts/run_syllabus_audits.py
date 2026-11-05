#!/usr/bin/env python3
import json
import os
import sys
import urllib.request

COURSES = ["EXW101", "EXW150", "EXW245", "EXW265"]
AUDIT_DIR = "audits"
os.makedirs(AUDIT_DIR, exist_ok=True)

OLLAMA_URL = "http://localhost:11434/api/generate"

def audit_syllabus(course: str):
    file_path = f"content/courses/{course}/syllabus.md"
    out_path = f"{AUDIT_DIR}/{course}-syllabus-audit.txt"

    if not os.path.exists(file_path):
        print(f"[-] Syllabus file not found for {course}: {file_path}")
        return

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    print(f"[+] Auditing Syllabus for {course} ({len(content)} bytes)...")

    prompt = f"""### Audit this Course Syllabus for {course}. Verify that:
1. Heading hierarchies start strictly at h2 (reserving h1 for Canvas).
2. Administrative policies and expectations use clear, plain language while maintaining appropriate rigor ({course} level).
3. Formatting leverages scannable bullet points and structured sections to minimize student cognitive overload. ###

### SYLLABUS CONTENT TO AUDIT:
{content}
"""

    payload = {
        "model": "gemma4:e2b",
        "prompt": prompt,
        "stream": False,
        "options": {
            "num_ctx": 16384,
            "num_predict": 2048,
            "temperature": 0.2
        }
    }

    req = urllib.request.Request(
        OLLAMA_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )

    try:
        with urllib.request.urlopen(req, timeout=300) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            response_text = data.get("response", "").strip()
            eval_count = data.get("eval_count", 0)
            done_reason = data.get("done_reason", "unknown")
            print(f"    Done {course}: {eval_count} tokens generated (reason: {done_reason})")
            
            with open(out_path, "w", encoding="utf-8") as out:
                out.write(response_text + "\n")
            print(f"    Saved: {out_path}")
    except Exception as e:
        print(f"[-] Error auditing syllabus for {course}: {e}")

def main():
    target = sys.argv[1] if len(sys.argv) > 1 else None
    courses = [target] if target else COURSES
    for c in courses:
        audit_syllabus(c)

if __name__ == "__main__":
    main()
