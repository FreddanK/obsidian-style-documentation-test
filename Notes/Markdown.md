Markdown is the plain-text format used for all notes in this vault.

## Why Markdown

- Human-readable without any special tooling.
- Renders in GitHub, Obsidian, VS Code, and every static site generator.
- Diffable in Git — changes are visible at the character level.
- No vendor lock-in: files can be imported into any wiki, CMS, or documentation platform.

## Syntax quick reference

```markdown
# Heading 1
## Heading 2
### Heading 3

**bold**   _italic_   `inline code`

- bullet list
1. numbered list

[[Wikilink]]               ← Obsidian internal link
[label](https://url.com)   ← external link

![[image.png]]             ← embedded attachment

```python
code block
```

> blockquote

| Column A | Column B |
|----------|----------|
| value    | value    |
```

## Frontmatter

Notes may include a YAML frontmatter block at the very top:

```yaml
---
tags: [architecture]
last_reviewed: 2026-07
owner: Platform Team
---
```

See [[Obsidian best practices]] for the full list of supported frontmatter fields and when to use them.

## Conventions for this vault

- Use `##` as the top-level heading inside a note (the filename already serves as the `#` title in Obsidian and [[Quartz]]).
- One blank line between paragraphs and between sections.
- Prefer tables over bullet lists when comparing multiple things.
- Keep lines unwrapped — let the editor handle visual line wrapping.
