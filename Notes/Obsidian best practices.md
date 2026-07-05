Conventions for keeping this [[Obsidian]] vault healthy and easy to navigate.

## Note naming

- Use the note's title as its filename, with spaces and natural capitalization.
  Good: `Database migrations.md`. Avoid: `db-migrations.md`.
- Prioritize a readable heading over a tidy filename.
- Most notes start with an upper-case letter.

## Writing style

- Start every note with one or two sentences that define the topic — this text appears in hover previews and search results.
- Use headings (`##`, `###`) to structure longer notes.
- Keep notes focused. If a note grows to cover two clearly separate ideas, split it.

## Wikilinks

- Link a term the **first time** it appears in a note. Do not repeat the link on subsequent mentions.
- It is fine to create a link to a note that does not exist yet. Stub notes will be picked up by the [[Link health check]].
- When you create a link target that is intentionally incomplete, add a one-sentence description of what it should contain — this converts a broken link into a documented gap.

## Frontmatter

Use YAML frontmatter for structured metadata where useful:

```yaml
---
tags: [architecture, backend]
last_reviewed: 2026-07
owner: Backend Team
---
```

- `tags` — use the controlled tag list from [[Glossary]].
- `last_reviewed` — required on [[Maps Of Content]] pages. Format: `YYYY-MM` or `YYYY-MM-DD`.
- `owner` — the team or person responsible for keeping the note accurate.

## Tags

Use a small, controlled set of tags rather than free-form tagging:

| Tag | When to use |
|-----|-------------|
| `#architecture` | System design, ADRs, diagrams |
| `#runbook` | Step-by-step operational procedures |
| `#decision` | Decisions made and their rationale |
| `#team` | People, teams, processes |
| `#onboarding` | Content specifically for new joiners |

Obsidian and [[Quartz]] both generate tag index pages automatically, providing a maintenance-free navigation layer alongside [[Maps Of Content]].

## Maps of Content

- Every major topic area should have a [[Maps Of Content|MOC]].
- Add a `last_reviewed` date and an `owner` to every MOC.
- The [[MOC update script]] will suggest unlisted notes; a human decides what to promote.

## File organisation

- All Markdown notes go in `Notes/` — no sub-folders.
- All non-Markdown assets (images, drawings) go in `Attachments/` — no sub-folders.
- See the [[README]] for the full folder structure rationale.
