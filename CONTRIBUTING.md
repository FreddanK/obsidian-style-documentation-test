# Contributing to this documentation vault

There are three ways to contribute, depending on how often you write docs and how comfortable you are with developer tooling.

---

## Path 1 — Read only (browser)

No setup required. Visit the published site at `<URL>` to browse and search all documentation.

---

## Path 2 — Occasional contributor (GitHub web editor)

For small edits, new notes, or fixing a typo without installing anything locally.

1. Go to the repository on GitHub.
2. Navigate to `Notes/`.
3. Click an existing file to edit it, or click **Add file → Create new file** to create a new note.
4. Write in plain [Markdown](Notes/Markdown.md). Use `[[Note name]]` for internal links.
5. Commit directly to a new branch and open a pull request.

---

## Path 3 — Regular contributor (Obsidian + Git)

Full local setup with the Obsidian knowledge graph, graph view, and plugin support.

### Prerequisites

- [Git](https://git-scm.com/)
- [Python 3.10+](https://www.python.org/)
- [Obsidian](https://obsidian.md/) (free)

### Setup

```bash
# 1. Clone the repository
git clone <repo-url>
cd <repo-name>

# 2. Apply shared settings (merges .obsidian.shared/ into .obsidian/)
- For Linux: `./apply_shared_settings.sh`
- For Windows: Click apply_shared_settings.bat

# 3. Open Obsidian → Open folder as vault → select this folder
```

### After pulling changes

If `.obsidian.shared/` has changed since your last pull, re-run the sync script:

- For Linux: `./apply_shared_settings.sh`
- For Windows: Click apply_shared_settings.bat

### Committing and pushing

Use the **obsidian-git** plugin (sidebar icon or command palette → *Git: Create backup*). Write a short, descriptive commit message — the default is intentionally blank to force you to write one.

---

## Note conventions

See [Obsidian best practices](Notes/Obsidian%20best%20practices.md) for the full style guide. Key points:

- All notes go in `Notes/`. No sub-folders.
- All images and drawings go in `Attachments/`. No sub-folders.
- Use `[[wikilinks]]` for internal links. Link a term the first time it appears; not again.
- Add `last_reviewed` and `owner` frontmatter to [MOC pages](Notes/Maps%20Of%20Content.md).

---

## Automation

| What | When | Script |
|------|------|--------|
| Broken wikilink check | Every PR + weekly | `scripts/check_links.py` |
| Shared settings validation | Every PR touching `.obsidian.shared/` | `scripts/validate_shared_settings.py` |
| MOC suggestions | Every push to `main` + weekly | `scripts/update_mocs.py` |
| Status report | Weekly (posted to CI summary) | `scripts/status_report.py` |

Run any script locally before pushing:

```bash
python3 scripts/check_links.py
python3 scripts/update_mocs.py --dry-run
python3 scripts/validate_shared_settings.py
python3 scripts/status_report.py
```

## Migrating content from Confluence

See [Migration guide](Notes/Migration%20guide.md) for the full workflow and decision rules.
See [Migration backlog](Notes/Migration%20backlog.md) to find and claim a topic to work on.
