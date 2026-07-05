---
tags: [meta]
last_reviewed: 2026-07
owner: Documentation Team
---

A Map of Content (MOC) is a note whose primary purpose is to link to other notes on a related topic. MOCs provide curated, human-maintained navigation on top of the flat [[Obsidian]] vault structure.

Think of them as the equivalent of a Wikipedia category page or a table of contents — not a container, but a signpost.

## Why MOCs instead of folders

Folders force a note into exactly one place. A note about "database migrations in production" belongs equally under *Databases*, *Runbooks*, and *Backend*. With MOCs a note can appear in as many index pages as makes sense, without duplication.

## MOC conventions

- Every MOC must have a `last_reviewed` frontmatter date (format: `YYYY-MM`).
- Every MOC must have an `owner` frontmatter field.
- The [[MOC update script]] automatically appends a *Suggested additions* section listing notes that link to the MOC but are not yet listed in it. A human decides what to promote.

## MOC pages in this vault

- [[MOC]] — abbreviation reference

## Creating a new MOC

1. Create a note with a descriptive name, e.g. `Backend.md`.
2. Add frontmatter with `last_reviewed` and `owner`.
3. Add a short description of what belongs here.
4. Start linking to relevant notes.
5. Link to this note (`[[Maps Of Content]]`) so the MOC update script can discover it.
