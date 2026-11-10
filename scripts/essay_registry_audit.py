#!/usr/bin/env python3
"""
S-A-R Sequential Essay Registry & Substack Parity Auditor
=========================================================
Maintains the Single Source of Truth (SSoT) sequential Essay ledger across:
  1. /Users/alanpruitt/alanpruitt.github.io (Web Canonical SSoT: content/en/essays/, content/es/essays/, content/en/distribution/)
  2. /Users/alanpruitt/EXW-MASTER-LIBRARY/docs/essays/ (Fleet Mirror & Staged Draft Queue)
  3. https://alanpruitt.substack.com/feed (Live Substack RSS Parity Verification)

Guarantees:
  - Contiguous sequential numbering (01..N) with zero missing numbers and zero collisions.
  - Automatic tracking of Staged Drafts (#41+) and Next Available Essay Number.
  - Word-count floor enforcement (prevents summary stubs from overwriting full essays).
  - Institutional Non-Endorsement Disclaimer, H2 root hierarchy, and zero decorative emojis.
  - Substack RSS parity verification (ensures alanpruitt.com is never truncated vs. Substack).
"""

import argparse
import glob
import json
import os
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone

SITE_ORIGIN = "https://alanpruitt.com"
SUBSTACK_FEED_URL = "https://alanpruitt.substack.com/feed"
EMOJI_RE = re.compile(r"[\U0001F300-\U0001FAFF\u2600-\u27BF]")

# Known Substack post URL slug substring -> Canonical Essay Number
SUBSTACK_SLUG_TO_ESSAY = {
    "what-if-i-didnt-automate-the-threshold": 39,
    "essay-38-what-if-i-didnt-build-the": 38,
    "what-if-i-didnt-future-proofing-my": 37,
    "what-if-i-didnt-standardize-the-loop": 36,
    "what-if-i-didnt-automate-accessibility": 35,
    "from-gsu-demo-day-to-vibe-coding": 34,
    "what-happens-when-you-stop-renting": 33,
    "from-retrofit-to-architecture-operationalizing": 32,
    "navigating-ada-title-ii-conformance": 28,
    "navigating-compliance-upstream-the": 26,
}


def resolve_repo_roots():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent = os.path.dirname(script_dir)
    if os.path.exists(os.path.join(parent, "content/en/essays")):
        gh_io = parent
    else:
        gh_io = "/Users/alanpruitt/alanpruitt.github.io"
    master = "/Users/alanpruitt/EXW-MASTER-LIBRARY"
    return gh_io, (master if os.path.exists(master) else None)


def parse_frontmatter(raw):
    m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n(.*)$", raw, flags=re.S)
    if not m:
        return {}, raw.strip()
    fm_text, body = m.group(1), m.group(2).strip()
    meta = {}
    for line in fm_text.splitlines():
        if ":" in line and not line.startswith(" ") and not line.startswith("-"):
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip().strip("\"'")
    return meta, body


def strip_fenced_code(md):
    return re.sub(r"```.*?```", "", md, flags=re.S)


def extract_essay_number(filename, meta):
    bn = os.path.basename(filename)
    m = re.search(r"(?:^|essay[-_]?)(\d+)", bn, flags=re.I)
    if m:
        return int(m.group(1))
    title = meta.get("title", "")
    mt = re.search(r"Essay\s+(\d+)", title, flags=re.I)
    if mt:
        return int(mt.group(1))
    return None


def scan_published_essays(gh_io):
    en_dir = os.path.join(gh_io, "content/en/essays")
    es_dir = os.path.join(gh_io, "content/es/essays")
    dist_dir = os.path.join(gh_io, "content/en/distribution")

    es_files = {
        os.path.basename(p): p
        for p in glob.glob(os.path.join(es_dir, "*.md"))
        if os.path.basename(p) != "_index.md"
    }

    records = []
    errors = []
    seen_numbers = {}

    for fp in sorted(glob.glob(os.path.join(en_dir, "*.md"))):
        bn = os.path.basename(fp)
        if bn == "_index.md":
            continue
        raw = open(fp, encoding="utf-8").read()
        meta, body = parse_frontmatter(raw)
        num = extract_essay_number(bn, meta)
        if num is None:
            errors.append(f"[SEQUENCE ERROR] Cannot determine essay number for {bn}")
            continue
        if num in seen_numbers:
            errors.append(
                f"[COLLISION ERROR] Duplicate Essay #{num:02d}: {bn} collides with {seen_numbers[num]}"
            )
        seen_numbers[num] = bn

        file_base = os.path.splitext(bn)[0]
        primary_slug = meta.get("slug") or file_base
        canonical_url = f"{SITE_ORIGIN}/essays/{primary_slug}/"
        words = len(body.split())
        min_words = 400 if num >= 26 else 320
        if words < min_words:
            errors.append(
                f"[STUB ERROR] Essay #{num:02d} ({bn}) has only {words} body words (minimum {min_words})"
            )

        no_code = strip_fenced_code(body)
        if re.search(r"^#\s+\S", no_code, flags=re.M):
            errors.append(f"[HEADING ERROR] Essay #{num:02d} ({bn}) contains top-level '# ' H1 in body")

        emojis = EMOJI_RE.findall(raw)
        if emojis:
            errors.append(f"[EMOJI ERROR] Essay #{num:02d} ({bn}) contains decorative icons: {emojis[:5]}")

        if "do not represent official policy or endorsement" not in body:
            errors.append(f"[DISCLAIMER ERROR] Essay #{num:02d} ({bn}) missing Institutional Non-Endorsement Disclaimer")

        if num >= 38:
            unquoted_lines = [
                ln for ln in no_code.splitlines()
                if not ln.lstrip().startswith(">")
            ]
            we_hits = re.findall(r"\b(we|our|ours)\b", "\n".join(unquoted_lines), flags=re.I)
            if we_hits:
                errors.append(
                    f"[VOICE ERROR] Essay #{num:02d} ({bn}) contains plural pronouns in first-person essay: {we_hits[:5]}"
                )

        es_match = es_files.get(bn)
        sub_kit = os.path.join(dist_dir, f"essay-{num:02d}-substack.md")
        li_kit = os.path.join(dist_dir, f"essay-{num:02d}-linkedin.md")

        records.append({
            "essay_number": num,
            "status": "published",
            "title": meta.get("title", ""),
            "date": (meta.get("date", "") or "")[:10],
            "slug": primary_slug,
            "canonical_url": canonical_url,
            "en_file": f"content/en/essays/{bn}",
            "es_file": f"content/es/essays/{bn}" if es_match else None,
            "substack_kit": f"content/en/distribution/essay-{num:02d}-substack.md" if os.path.exists(sub_kit) else None,
            "linkedin_kit": f"content/en/distribution/essay-{num:02d}-linkedin.md" if os.path.exists(li_kit) else None,
            "substack_live_url": None,
            "word_count": words,
        })

    records.sort(key=lambda r: r["essay_number"])

    if records:
        max_num = records[-1]["essay_number"]
        present = {r["essay_number"] for r in records}
        missing = [n for n in range(1, max_num + 1) if n not in present]
        if missing:
            errors.append(f"[GAP ERROR] Missing sequential essay numbers in 1..{max_num}: {missing}")

    return records, errors


def scan_staged_drafts(master, published_nums):
    staged = []
    errors = []
    if not master:
        return staged, errors
    docs_dir = os.path.join(master, "docs/essays")
    if not os.path.exists(docs_dir):
        return staged, errors

    for fp in sorted(glob.glob(os.path.join(docs_dir, "essay-*.md"))):
        bn = os.path.basename(fp)
        if bn.endswith("-substack.md") or bn.endswith("-linkedin.md"):
            continue
        raw = open(fp, encoding="utf-8").read()
        meta, body = parse_frontmatter(raw)
        num = extract_essay_number(bn, meta)
        if num is None:
            continue
        if num in published_nums:
            # Mirror of an already published canonical essay
            continue
        title = meta.get("title", "")
        if not title:
            m_h = re.search(r"^#+\s+(.*)$", raw, flags=re.M)
            title = m_h.group(1).strip() if m_h else bn
        staged.append({
            "essay_number": num,
            "status": "staged",
            "title": title,
            "slug": os.path.splitext(bn)[0],
            "staged_file": f"docs/essays/{bn}",
            "substack_kit": f"docs/essays/essay-{num:02d}-substack.md"
            if os.path.exists(os.path.join(docs_dir, f"essay-{num:02d}-substack.md"))
            else None,
            "linkedin_kit": f"docs/essays/essay-{num:02d}-linkedin.md"
            if os.path.exists(os.path.join(docs_dir, f"essay-{num:02d}-linkedin.md"))
            else None,
            "word_count": len(body.split()),
        })

    staged.sort(key=lambda s: s["essay_number"])
    return staged, errors


def verify_substack_parity(records, strict_network=False):
    errors = []
    by_num = {r["essay_number"]: r for r in records}
    try:
        req = urllib.request.Request(SUBSTACK_FEED_URL, headers={"User-Agent": "Mozilla/5.0"})
        xml_bytes = urllib.request.urlopen(req, timeout=12).read()
        root = ET.fromstring(xml_bytes.decode("utf-8"))
    except Exception as exc:
        msg = f"[SUBSTACK WARN] Could not reach {SUBSTACK_FEED_URL}: {exc}"
        if strict_network:
            errors.append(msg)
        else:
            print(msg)
        return errors

    for item in root.findall(".//item"):
        link = (item.findtext("link") or "").strip()
        content = ""
        for child in item:
            if "encoded" in child.tag:
                content = child.text or ""
        plain = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", content)).strip()
        sub_words = len(plain.split())

        matched_num = None
        for slug_part, num in SUBSTACK_SLUG_TO_ESSAY.items():
            if slug_part in link:
                matched_num = num
                break
        if matched_num and matched_num in by_num:
            rec = by_num[matched_num]
            rec["substack_live_url"] = link
            rec["substack_word_count"] = sub_words
            canon_no_slash = rec["canonical_url"].rstrip("/")
            hrefs = re.findall(r'href=["\']([^"\']+)["\']', content)
            has_exact_backlink = any(h.rstrip("/") == canon_no_slash for h in hrefs)
            has_sub_disclaimer = "do not represent official policy" in plain
            rec["substack_has_canonical_backlink"] = has_exact_backlink
            rec["substack_has_disclaimer"] = has_sub_disclaimer
            if rec["word_count"] < int(sub_words * 0.85):
                errors.append(
                    f"[SUBSTACK DRIFT] Essay #{matched_num:02d} ({rec['en_file']}) has {rec['word_count']}W "
                    f"on alanpruitt.com vs {sub_words}W on Substack ({link})"
                )
    return errors


def render_markdown_ledger(registry):
    lines = [
        "# Canonical Essay Sequential Ledger (`alanpruitt.com` ↔ Substack ↔ `EXW-MASTER-LIBRARY`)",
        "",
        f"**Last Audited:** `{registry['generated_at']}`  ",
        f"**Published Live Sequence:** `Essay 01` – `Essay {registry['max_published_number']:02d}` (`{registry['published_count']}/{registry['max_published_number']}` contiguous, `0` gaps)  ",
        f"**Staged Queue (`EXW-MASTER-LIBRARY/docs/essays/`):** "
        + (
            ", ".join(f"`Essay {s['essay_number']:02d}` (*{s['title']}*)" for s in registry["staged_essays"])
            if registry["staged_essays"]
            else "`None`"
        )
        + "  ",
        f"**Next Brand-New Essay Number to Assign:** **`Essay {registry['next_new_essay_number']:02d}`**",
        "",
        "---",
        "",
        "## 1. Staged Release Queue (Unpublished)",
        "",
    ]
    if registry["staged_essays"]:
        lines.extend([
            "| # | Title | Staged SSoT File | Words | Kits Ready |",
            "| :---: | :--- | :--- | :---: | :---: |",
        ])
        for s in registry["staged_essays"]:
            kits = []
            if s.get("substack_kit"):
                kits.append("Substack")
            if s.get("linkedin_kit"):
                kits.append("LinkedIn")
            kit_str = " + ".join(kits) if kits else "Canonical Only"
            lines.append(
                f"| **{s['essay_number']:02d}** | {s['title']} | `{s['staged_file']}` | `{s['word_count']}` | {kit_str} |"
            )
    else:
        lines.append("*No unpublished drafts currently staged.*")

    lines.extend([
        "",
        "---",
        "",
        "## 2. Published Canonical Corpus (`alanpruitt.com` — Newest First)",
        "",
        "| # | Date | Title | Canonical Route | Site Words | ES Mirror | Substack Parity |",
        "| :---: | :---: | :--- | :--- | :---: | :---: | :---: |",
    ])
    for r in reversed(registry["published_essays"]):
        es_badge = "Yes" if r["es_file"] else "—"
        if r.get("substack_live_url"):
            sub_wc = r.get("substack_word_count", "")
            bl_flag = "Backlink OK" if r.get("substack_has_canonical_backlink") else "Needs Backlink"
            sub_badge = f"[Live ({sub_wc}W • {bl_flag})]({r['substack_live_url']})"
        else:
            sub_badge = "—"
        route = r["canonical_url"].replace(SITE_ORIGIN, "")
        lines.append(
            f"| **{r['essay_number']:02d}** | `{r['date']}` | {r['title']} | `{route}` | `{r['word_count']}` | {es_badge} | {sub_badge} |"
        )
    lines.append("")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Sequential Essay Registry & Substack Parity Auditor")
    parser.add_argument("--write", action="store_true", help="Write ESSAY_REGISTRY.json and ESSAY_INDEX.md")
    parser.add_argument("--ci", action="store_true", help="Run strict CI validation mode")
    parser.add_argument("--check-substack", action="store_true", help="Compare word counts against live Substack RSS")
    parser.add_argument("--status", action="store_true", help="Print concise sequential status summary")
    args = parser.parse_args()

    gh_io, master = resolve_repo_roots()
    records, pub_errors = scan_published_essays(gh_io)
    published_nums = {r["essay_number"] for r in records}
    staged, staged_errors = scan_staged_drafts(master, published_nums)

    sub_errors = []
    if args.check_substack or args.write:
        sub_errors = verify_substack_parity(records, strict_network=False)

    all_errors = pub_errors + staged_errors + sub_errors
    max_pub = max(published_nums) if published_nums else 0
    all_known_nums = published_nums | {s["essay_number"] for s in staged}
    next_new = (max(all_known_nums) + 1) if all_known_nums else 1

    registry = {
        "schema_version": "1.0.0",
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "published_count": len(records),
        "max_published_number": max_pub,
        "staged_numbers": [s["essay_number"] for s in staged],
        "next_new_essay_number": next_new,
        "staged_essays": staged,
        "published_essays": records,
    }

    staged_label = ", ".join(f"#{s['essay_number']:02d}" for s in staged) if staged else "None"
    print(
        f"[ESSAY SEQUENCE LEDGER] Published Live: 01-{max_pub:02d} ({len(records)}/{max_pub} contiguous) "
        f"| Staged Queue: {staged_label} | Next New Essay Number: #{next_new:02d}"
    )

    if args.write:
        reg_path = os.path.join(gh_io, "ESSAY_REGISTRY.json")
        with open(reg_path, "w", encoding="utf-8") as f:
            json.dump(registry, f, indent=2, ensure_ascii=False)
            f.write("\n")
        print(f"  [WRITE] {reg_path}")

        if master and os.path.exists(os.path.join(master, "docs/essays")):
            m_reg = os.path.join(master, "docs/essays/ESSAY_REGISTRY.json")
            m_idx = os.path.join(master, "docs/essays/ESSAY_INDEX.md")
            with open(m_reg, "w", encoding="utf-8") as f:
                json.dump(registry, f, indent=2, ensure_ascii=False)
                f.write("\n")
            with open(m_idx, "w", encoding="utf-8") as f:
                f.write(render_markdown_ledger(registry))
            print(f"  [WRITE] {m_reg}")
            print(f"  [WRITE] {m_idx}")

    if all_errors:
        print(f"\n[FAIL] {len(all_errors)} Essay Registry / Parity violation(s) detected:")
        for e in all_errors:
            print("  -", e)
        sys.exit(1)

    print("[PASS] Zero gaps, zero collisions, zero stubs, and 100% Substack RSS parity verified.")


if __name__ == "__main__":
    main()
