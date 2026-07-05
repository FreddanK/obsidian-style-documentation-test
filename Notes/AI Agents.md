AI Agents are an planned extension to this documentation vault, designed to reduce the manual overhead of maintaining a large knowledge base and to make the vault more useful to contributors.

## Planned capabilities

### Level 1 — Vault Q&A (RAG)

A retrieval-augmented generation pipeline over `Notes/`. Contributors can ask natural-language questions and get answers grounded in the actual documentation.

**Implementation approach:**
1. Embed all notes using an embeddings API (e.g. OpenAI `text-embedding-3-small`).
2. Store embeddings in a local vector store (e.g. Chroma, Qdrant, or a simple FAISS index).
3. On a query, retrieve the top-k most relevant notes and pass them as context to an LLM.
4. Surface via a CLI script, a simple web UI, or the [Obsidian Copilot plugin](https://github.com/logancyang/obsidian-copilot).

Re-embed on every push to `main` via a [[GitHub Actions]] workflow.

### Level 2 — Stale content detection

An agent that reads every note, infers its topic from the content, and cross-checks against:
- The note's `last_reviewed` frontmatter date.
- Recent Git commit messages in the linked code repositories.
- Contradictions with other notes in the vault.

Flags are posted as a weekly GitHub Issue (similar to the [[link health check]]).

### Level 3 — Doc stub generation from code

A CI step that runs on pull requests in linked code repositories:
1. Detects new public APIs, services, config flags, or data models.
2. Drafts a stub note in `Notes/` with the name, a one-sentence description, and boilerplate sections.
3. Opens a pull request for humans to review and complete.

This keeps the documentation structurally in sync with the codebase without requiring developers to write prose.

### Level 4 — Conversational editing

A natural-language interface (CLI or chat) through which contributors create or update notes by describing what they want. The agent writes the Markdown, respects [[Obsidian best practices]], and commits the result to [[Git]] automatically. Particularly useful for non-developer contributors who are not comfortable with Obsidian or Git.

## Current status

Levels 1–4 are planned. No implementation exists yet. The [[Glossary]] and [[Obsidian best practices]] notes are prerequisites for Level 1 (they improve retrieval quality). Level 3 requires identifying which code repositories are "linked" to this vault.

## See also

- [[Obsidian best practices]] — conventions the agent must respect when writing notes.
- [[GitHub Actions]] — where the CI-based agents will run.
- [[Glossary]] — controlled vocabulary that improves embedding quality.
