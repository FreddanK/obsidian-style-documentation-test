Wikilinks are the `[[double bracket]]` link syntax used in [[Obsidian]] to link between notes. They are the primary navigation mechanism in this vault.

## Syntax

```markdown
[[Note name]]                 ← link to a note by its filename (without .md)
[[Note name|Display text]]    ← link with a custom label
[[Note name#Heading]]         ← link to a specific heading within a note
```

## Conventions

- Link a term the **first time** it appears in a note. Do not repeat the link on subsequent mentions in the same note.
- It is fine to link to a note that does not exist yet. The [[link health check]] will surface it, and another contributor may create it later.
- If you intentionally leave a link target empty, add at least a one-sentence stub file so others know the gap is acknowledged.

## Broken links

A broken wikilink is one that points to a filename that does not exist in `Notes/`. Broken links are:
- Visible in Obsidian (shown in a muted colour in the graph view).
- Reported weekly by the [[link health check]] GitHub Actions workflow.
- Fine to leave intentionally — they signal a concept that deserves a note.

## See also

- [[Maps Of Content]] — curated index pages that complement wikilink navigation.
- [[Obsidian best practices]] — full linking conventions.
