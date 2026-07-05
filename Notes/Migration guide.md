---
status: stable
tags: [meta]
owner: Documentation Team
last_reviewed: 2026-07
---

This note records exactly how content is migrated from Confluence into this vault. It is written for contributors picking up migration work after the initial batch of notes has been established. Follow it closely — consistency of judgement across contributors is what makes the vault coherent.

## Core principle

**Rewrite, don't copy.** Confluence content is not pasted in. It is read, understood, and rewritten from scratch. This forces three things: you only write what you actually understand, you automatically leave behind what is outdated, and the result reads like a note rather than a wiki page. The extra effort is the point.

## Workflow for each topic

### 1. Claim it

Find the topic in [[Migration backlog]] and change its status from `to-do` to `in-progress`, adding your name. This prevents two people working on the same note simultaneously.

### 2. Find the Confluence sources

Search Confluence for the topic. There will often be multiple pages — duplicates across spaces, outdated versions, pages that partially overlap. Read all of them. You are synthesising, not transcribing.

### 3. Decide what is still true

For each piece of information, ask:
- Is this still accurate?
- Does anyone actually need to know this?
- Is this documented better somewhere else (e.g. in code comments, a README, an ADR)?

If the answer to all three is no, leave it behind. Do not feel obligated to preserve content just because it existed in Confluence.

### 4. Create the note

Create a new note in `Notes/` using the [[Note template]]. Name it clearly — the filename is the heading. Use natural capitalisation and spaces.

Fill in the frontmatter:

```yaml
---
status: draft
tags: [appropriate-tag]
owner: Your Team
migrated_from: "Confluence page title (Space name)"
last_reviewed: 2026-07
---
```

### 5. Write the content

- Start with one or two sentences that define the topic without assuming prior knowledge.
- Use `##` headings to structure the note. Avoid deep nesting (`####` and beyond).
- [[Wikilinks|Link]] to related notes the first time a concept is mentioned.
- Freely create links to notes that do not exist yet — they become backlog items automatically.
- Keep the note focused. If it grows to cover two clearly distinct topics, split it.

### 6. Mark it for review

When you consider the note complete, change `status: draft` to `status: review` and add it to the relevant [[Maps Of Content|MOC]] pages.

### 7. Mark the backlog item done

In [[Migration backlog]], change the status to `done` and add the date.

---

## Decision rules

These are the judgement calls made during the initial migration. Apply them consistently.

### Duplicates

When multiple Confluence pages cover the same topic: synthesise them into one note. Record all source page titles in `migrated_from` as a list:

```yaml
migrated_from:
  - "Database migrations (Backend space)"
  - "How to run migrations (Onboarding space)"
```

### Outdated content

If a page is outdated but describes something that still exists (e.g. a deprecated service someone might still encounter): write a brief note, mark it with `status: draft` and a clear opening sentence like *"This service was deprecated in 2024. See [[New service]] for the replacement."*

If the page is outdated and describes something entirely gone: do not migrate it.

### Incomplete pages

If a Confluence page is a stub with one paragraph and no useful information: skip it. Create a wikilink to the topic from a related note instead. The broken link signals the gap without creating an empty note.

### Sensitive content

Do not migrate anything that contains:
- Personal data (names + contact details together, salary information, etc.)
- Credentials, tokens, or internal URLs that should not be in version control
- Content that is subject to legal review

When in doubt, leave it out and flag it in [[Migration backlog]] with a note.

### Formatting

- Convert Confluence tables to Markdown tables.
- Convert Confluence code blocks to fenced Markdown code blocks with a language identifier.
- Discard Confluence-specific macros (status lozenges, info panels, etc.) — rewrite the content as plain prose or a note block (`> Note: ...`).
- Discard page metadata (created by, last modified, etc.) — Git history provides this.

---

## Quality bar

The initial batch of notes sets the quality bar for all future contributions. Before marking a note `stable`, check:

- [ ] Opens with a clear, assumption-free definition of the topic.
- [ ] Every concept mentioned that has its own note is wikilinked (first mention only).
- [ ] No broken links that are not intentional stubs.
- [ ] Frontmatter is complete (`status`, `tags`, `owner`, `migrated_from` if applicable).
- [ ] A second person has read it and agrees it is accurate.

---

## See also

- [[Migration backlog]] — the full list of topics and their status.
- [[Note template]] — the frontmatter and structure to start each note from.
- [[Obsidian best practices]] — style and linking conventions.
- [[GitHub Actions]] — automated checks that run on every pull request.
