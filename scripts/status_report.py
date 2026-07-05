#!/usr/bin/env python3
"""
status_report.py

Reports the status of all notes in Notes/ — how many are draft, review,
or stable — and lists any notes with no status field at all.

Useful for tracking migration progress. Run locally or in CI.

Usage:
    python3 scripts/status_report.py [--report]

Flags:
    --report    Output Markdown-formatted report (for GitHub Actions summaries).
"""

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
NOTES_DIR = REPO_ROOT / "Notes"

STATUS_RE = re.compile(r"^---\s*\n.*?^status:\s*(\S+).*?^---", re.DOTALL | re.MULTILINE)
MIGRATED_RE = re.compile(r"^migrated_from:", re.MULTILINE)

VALID_STATUSES = {"draft", "review", "stable"}


def get_status(content: str) -> str | None:
    m = STATUS_RE.search(content)
    return m.group(1).strip() if m else None


def main() -> int:
    report_mode = "--report" in sys.argv

    by_status: dict[str, list[str]] = {"draft": [], "review": [], "stable": [], "missing": []}

    for md_file in sorted(NOTES_DIR.glob("*.md")):
        content = md_file.read_text(encoding="utf-8")
        status = get_status(content)
        if status is None:
            by_status["missing"].append(md_file.name)
        elif status in VALID_STATUSES:
            by_status[status].append(md_file.name)
        else:
            by_status["missing"].append(f"{md_file.name} (unknown status: {status})")

    total = sum(len(v) for v in by_status.values())

    if report_mode:
        print("## 📊 Documentation Status Report\n")
        print(f"| Status | Count | % |")
        print(f"|--------|-------|---|")
        for s in ("stable", "review", "draft", "missing"):
            count = len(by_status[s])
            pct = round(count / total * 100) if total else 0
            emoji = {"stable": "✅", "review": "🔍", "draft": "✏️", "missing": "❓"}[s]
            print(f"| {emoji} {s.capitalize()} | {count} | {pct}% |")
        print()
        for s in ("review", "draft", "missing"):
            if by_status[s]:
                label = {"review": "🔍 Awaiting review", "draft": "✏️ In progress", "missing": "❓ No status set"}[s]
                print(f"### {label}\n")
                for name in by_status[s]:
                    print(f"- `{name}`")
                print()
    else:
        print(f"Documentation status ({total} notes total):\n")
        for s in ("stable", "review", "draft", "missing"):
            count = len(by_status[s])
            label = s.capitalize().ljust(8)
            bar = "█" * count
            print(f"  {label} {count:3d}  {bar}")
        print()
        for s in ("review", "draft", "missing"):
            if by_status[s]:
                print(f"{s.upper()}:")
                for name in by_status[s]:
                    print(f"  - {name}")
                print()

    return 0


if __name__ == "__main__":
    sys.exit(main())
