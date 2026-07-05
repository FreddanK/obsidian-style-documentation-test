The link health check is an automated [[GitHub Actions]] workflow that finds broken [[Wikilinks]] in the vault and reports them.

## What counts as a broken link

A [[Wikilinks|wikilink]] is broken if no file with the linked name exists in `Notes/`. For example, `[[Database migrations]]` is broken if `Notes/Database migrations.md` does not exist.

## How it runs

- **On every push or PR** that touches `Notes/` — broken links introduced by the change are reported immediately.
- **Weekly** (Monday 08:00 UTC) — a full scan of the vault is run and results are posted to a GitHub Issue.

## What happens when links are broken

- On a **pull request**: a comment is posted listing all broken links in the changed files.
- On a **scheduled run**: a GitHub Issue is opened (or an existing one is updated) with the full broken-links table.
- The workflow **fails** (exit code 1) if any broken links are found, making this visible in the PR status checks.

## Fixing a broken link

Two options:

1. **Create the missing note.** Add `Notes/<name>.md` with at least a one-sentence description. This is the preferred option.
2. **Correct the link.** If the link target was simply misspelled or renamed, fix the `[[wikilink]]` text.

## Script

The underlying script is `scripts/check_links.py`. Run it locally to check links before pushing:

```bash
python3 scripts/check_links.py
```

Use `--report` for the full Markdown-formatted output:

```bash
python3 scripts/check_links.py --report
```

## See also

- [[Wikilinks]] — link syntax and conventions.
- [[GitHub Actions]] — all automation workflows.
- [[Obsidian best practices]] — stub note convention for intentional broken links.
