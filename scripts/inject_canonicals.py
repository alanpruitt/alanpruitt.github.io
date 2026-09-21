#!/usr/bin/env python3
import argparse
import re
import sys
from pathlib import Path

# Configuration
DEFAULT_SITE_DIR = "./public"
DEFAULT_BASE_URL = "https://alanpruitt.com"

# Regex matching: rel="canonical", rel='canonical', or minified rel=canonical
CANONICAL_PATTERN = re.compile(r"rel\s*=\s*['\"]?canonical['\"]?", re.IGNORECASE)
HEAD_TAG_PATTERN = re.compile(r"(<head\b[^>]*>)", re.IGNORECASE)


def process_html_files(
    site_dir: str = DEFAULT_SITE_DIR,
    base_url: str = DEFAULT_BASE_URL,
    dry_run: bool = False,
):
    site_path = Path(site_dir)
    if not site_path.exists():
        print(f"Error: Directory '{site_dir}' not found.")
        sys.exit(1)

    clean_base_url = base_url.rstrip("/")
    html_files = sorted(site_path.rglob("*.html"))
    updated_count = 0
    skipped_existing = 0

    for file_path in html_files:
        # Exclude 404 and error pages from receiving canonical tags
        if file_path.name in ("404.html", "50x.html"):
            continue

        content = file_path.read_text(encoding="utf-8", errors="ignore")

        # Skip partial fragments or non-full documents
        if "<head" not in content.lower() or "</body>" not in content.lower():
            continue

        # Check if canonical tag already exists (quoted or minified)
        if CANONICAL_PATTERN.search(content):
            skipped_existing += 1
            continue

        # Construct clean canonical URL
        rel_path = file_path.relative_to(site_path)
        if rel_path.name == "index.html":
            if rel_path.parent == Path("."):
                canonical_url = f"{clean_base_url}/"
            else:
                canonical_url = f"{clean_base_url}/{rel_path.parent.as_posix()}/"
        else:
            canonical_url = f"{clean_base_url}/{rel_path.as_posix()}"

        canonical_tag = f'<link rel="canonical" href="{canonical_url}">'

        if dry_run:
            print(f"[Dry Run - Would Add] {rel_path} -> {canonical_url}")
        else:
            # Inject immediately after opening <head ...> tag
            updated_content = HEAD_TAG_PATTERN.sub(
                rf"\1\n    {canonical_tag}", content, count=1
            )
            file_path.write_text(updated_content, encoding="utf-8")
            print(f"[Added] {canonical_url}")

        updated_count += 1

    mode_label = "[DRY RUN] " if dry_run else ""
    print(f"\n{mode_label}Scan complete for '{site_dir}':")
    print(f"  - Existing canonicals verified: {skipped_existing}")
    print(f"  - Canonical tags injected:     {updated_count}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Inject missing canonical tags into compiled or static HTML files."
    )
    parser.add_argument(
        "--dir",
        default=DEFAULT_SITE_DIR,
        help=f"Target directory to scan (default: {DEFAULT_SITE_DIR})",
    )
    parser.add_argument(
        "--base-url",
        default=DEFAULT_BASE_URL,
        help=f"Base URL for canonical links (default: {DEFAULT_BASE_URL})",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without modifying files",
    )

    args = parser.parse_args()
    process_html_files(
        site_dir=args.dir, base_url=args.base_url, dry_run=args.dry_run
    )
