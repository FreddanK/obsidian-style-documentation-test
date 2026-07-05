---
tags: [meta]
last_reviewed: 2026-07
owner: Documentation Team
---

The Glossary is an authoritative list of defined terms and concepts used across this vault. It serves two purposes:

1. **Quality gate** — if a concept is not defined here and does not have its own note, it should not be [[Wikilinks|wikilinked]] yet.
2. **Embedding quality** — a well-defined vocabulary improves the [[AI Agents|RAG system]]'s ability to retrieve the right notes for a given query.

## Terms

| Term | Definition | Note |
|------|------------|------|
| MOC | Map of Content — a curated index note that links to other notes on a topic | [[Maps Of Content]] |
| Wikilink | `[[double bracket]]` internal link syntax in Obsidian | [[Wikilinks]] |
| Stub | A note that exists but contains only a one-line description of what it should eventually contain | [[Obsidian best practices]] |
| Vault | The root folder of an Obsidian project, containing all notes and settings | [[Obsidian]] |
| RAG | Retrieval-Augmented Generation — an AI pattern that grounds LLM answers in a document corpus | [[AI Agents]] |
| ADR | Architecture Decision Record — a note documenting a significant technical decision and its rationale | — |
| Runbook | A step-by-step operational procedure for a specific task or incident | — |
| status | Frontmatter field indicating a note's maturity: `draft`, `review`, or `stable` | [[Note template]] |
| migrated_from | Frontmatter field recording the Confluence source page(s) a note was based on | [[Migration guide]] |

## Adding a term

Add a row to the table above. If the term deserves its own note, create it in `Notes/` and link to it in the *Note* column.
