Docusaurus is a React-based static site generator maintained by Meta, and the main alternative to [[Quartz]] for publishing this vault as a website.

## Comparison with Quartz

| Feature | Quartz | Docusaurus |
|---------|--------|------------|
| Designed for Obsidian/Markdown vaults | ✅ Yes | ⚠️ Possible with plugins |
| [[Wikilinks]] support | ✅ Native | ⚠️ Requires a remark plugin |
| Graph view | ✅ Built-in | ❌ Not available |
| Versioned docs | ❌ | ✅ Built-in |
| Custom React components in Markdown | ❌ | ✅ MDX support |
| Search | ✅ Built-in | ✅ Algolia or local |
| Tag index pages | ✅ Auto-generated | ✅ Auto-generated |

## When to switch

Quartz is the current choice because it is purpose-built for Obsidian vaults. Consider switching to Docusaurus if:
- The documentation needs versioning (e.g. for a public API).
- The team wants to embed interactive components (charts, live code) in notes.
- The team is already heavily invested in React.

## Repository separation

Because the publishing layer is kept in a separate repository from the vault content, switching from Quartz to Docusaurus only affects the publisher repo — all notes stay exactly as they are.
