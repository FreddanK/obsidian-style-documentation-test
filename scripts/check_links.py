#!/usr/bin/env python3
"""
check_links.py

Scans all Markdown files in Notes/ for [[wikilinks]] and reports any that
have no corresponding file. Exits with code 1 if broken links are found
(suitable for use in CI).

Usage:
    python3 scripts/check_links.py [--report]

Flags:
    --report    Print a full Markdown-formatted report instead of plain text.
                Used by the GitHub Actions workflow to post issue comments.
"""

import os
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
NOTES_DIR = REPO_ROOT / "Notes"

# Matches [[Link]], [[Link|Alias]], [[Link#heading]], [[Link#heading|Alias]]
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:[#|][^\]]*)?\]\]")


def collect_note_names() -> set[str]:
    """Return the set of all note names (lowercased, without extension)."""
    names = set()
    for md_file in NOTES_DIR.glob("*.md"):
        names.add(md_file.stem.lower())
    return names


def find_broken_links(note_names: set[str]) -> dict[str, list[str]]:
    """
    Returns a dict mapping filename → list of broken link targets found in it.
    """
    broken: dict[str, list[str]] = {}
    for md_file in sorted(NOTES_DIR.glob("*.md")):
        content = md_file.read_text(encoding="utf-8")
        file_broken = []
        for match in WIKILINK_RE.finditer(content):
            target = match.group(1).strip()
            if target.lower() not in note_names:
                file_broken.append(target)
        if file_broken:
            broken[md_file.name] = file_broken
    return broken


def print_plain(broken: dict[str, list[str]]) -> None:
    if not broken:
        print("All wikilinks are healthy.")
        return
    total = sum(len(v) for v in broken.values())
    print(f"Found {total} broken wikilink(s) across {len(broken)} file(s):\n")
    for filename, targets in broken.items():
        print(f"  {filename}")
        for t in targets:
            print(f"    - [[{t}]]")


def print_report(broken: dict[str, list[str]]) -> None:
    if not broken:
        print("## ✅ Wikilink Health Check\n\nAll wikilinks are healthy.")
        return
    total = sum(len(v) for v in broken.values())
    print("## ⚠️ Broken Wikilinks Report\n")
    print(f"Found **{total}** broken wikilink(s) across **{len(broken)}** note(s).\n")
    print("A broken link means no file with that name exists in `Notes/`.")
    print("Fix by creating a stub note or correcting the link.\n")
    print("| Note | Broken Link |")
    print("|------|-------------|")
    for filename, targets in broken.items():
        for t in targets:
            print(f"| `{filename}` | `[[{t}]]` |")
    print()
    print("> To create a stub for a missing note, add a file `Notes/<name>.md`")
    print("> with a one-line description of what the note should eventually contain.")


def main() -> int:
    report_mode = "--report" in sys.argv
    note_names = collect_note_names()
    broken = find_broken_links(note_names)

    if report_mode:
        print_report(broken)
    else:
        print_plain(broken)

    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
