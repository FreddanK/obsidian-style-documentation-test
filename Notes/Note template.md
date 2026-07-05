This note describes the standard template for new notes in this vault. It is used as the starting point for all migrated and newly written content.

## How to use it

In Obsidian, the built-in Templates plugin is enabled. To start a new note from this template:

1. Create a new note (`Ctrl/Cmd + N`).
2. Open the command palette (`Ctrl/Cmd + P`) → *Templates: Insert template*.
3. Select **Note template**.

The template is stored at `Notes/Note template.md` (this file). Obsidian's template engine will insert the template body, not this wrapper note, when invoked.

## Template

```markdown
---
status: draft
tags: []
owner: 
migrated_from: 
last_reviewed: 
---

One or two sentences defining the topic. This text appears in hover previews
and search results, so make it self-contained and specific.

## Section

Content here.
```

## Frontmatter fields

| Field | Required | Values | Notes |
|-------|----------|--------|-------|
| `status` | Yes | `draft` · `review` · `stable` | See [[Migration guide]] for definitions |
| `tags` | Yes | See [[Obsidian best practices]] | Keep to the controlled tag list |
| `owner` | Recommended | Team or person name | Who keeps this accurate |
| `migrated_from` | If applicable | Confluence page title or URL | Traceability back to the source |
| `last_reviewed` | Required on MOCs | `YYYY-MM` | When the content was last verified |

## Status values

**`draft`** — being written; may be incomplete or unverified. Readers should treat it with caution.

**`review`** — writer considers it complete; waiting for a second pair of eyes before being marked stable.

**`stable`** — accurate, complete, and reviewed. The default expectation for published content.

## See also

- [[Migration guide]] — full workflow for migrating content from Confluence.
- [[Obsidian best practices]] — style and linking conventions.
- [[Migration backlog]] — the list of topics to migrate.
