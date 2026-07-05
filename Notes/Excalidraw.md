Excalidraw is a tool for creating hand-drawn-style diagrams and sketches. Diagrams are stored as `.excalidraw.md` files in `Attachments/` and can be embedded directly in notes.

## Embedding a drawing

```markdown
![[Drawing.excalidraw]]
```

Example:

![[Drawing.excalidraw]]

## Creating a new drawing

In Obsidian: open the command palette → *Excalidraw: Create new drawing*. The file will be saved to `Attachments/` automatically (configured in [[Obsidian shared settings]]).

The date/time suffix is disabled so that drawing filenames stay clean and stable for embedding.

## Tips

- Give each drawing a descriptive filename that matches the context of the note it belongs to (e.g. `auth-flow.excalidraw`).
- Excalidraw files are plain JSON wrapped in Markdown frontmatter — they diff cleanly in [[Git]].
- Keep diagrams focused on one concept. Link to the note rather than duplicating the diagram if the same drawing is relevant in multiple places.

## See also

- [[Obsidian shared settings]] — plugin configuration for Excalidraw.
- [[Attachments]] — where all non-Markdown files live.
