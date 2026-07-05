The MOC update script semi-automates the maintenance of [[Maps Of Content]] pages.

## What it does

1. Detects [[Maps Of Content|MOC]] pages in the vault (by name pattern and link density heuristic).
2. For each MOC, finds notes that **link to the MOC** but are **not yet listed in the MOC**.
3. Appends a *Suggested additions* section to the MOC with the unlisted notes.
4. Flags MOC pages whose `last_reviewed` date is older than 90 days.

A human reviews the suggestions and decides which ones to promote into the main body of the MOC.

## Intentional design choices

The script **suggests**, it does not auto-promote. This keeps humans in control of the curated structure while automating the discovery work.

## Running locally

```bash
# Preview what would change without writing anything
python3 scripts/update_mocs.py --dry-run

# Apply suggestions
python3 scripts/update_mocs.py
```

## Running in CI

The [[GitHub Actions]] `moc-suggestions` workflow runs this script automatically on every push to `main` and on a weekly schedule. Changes are committed back to `main` with the message `docs: auto-update MOC suggestion sections [skip ci]`.

## Staleness warnings

MOC pages should include a `last_reviewed` frontmatter field:

```yaml
---
last_reviewed: 2026-07
owner: Backend Team
---
```

The script will warn if a MOC has no `last_reviewed` date or if the date is more than 90 days in the past.

## See also

- [[Maps Of Content]] — what MOCs are and how to use them.
- [[GitHub Actions]] — the CI workflow that runs this script.
- [[Obsidian best practices]] — frontmatter conventions including `last_reviewed` and `owner`.
