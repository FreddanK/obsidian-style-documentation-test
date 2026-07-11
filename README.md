This repository is a test to investigate if it would be feasible to keep the internal documentation of a medium size software organization in an [Obsidian](Notes/Obsidian.md) vault following [Obsidian best practices](Notes/Obsidian%20best%20practices.md) 

## Getting Started

1. Clone this repository
2. Optional but recommended, run this command to ignore local changes to some settings:
	1. `git update-index --skip-worktree .obsidian/app.json`
	(To undo this, do `git update-index --no-skip-worktree .obsidian/app.json`)

## Contributing to this documentation vault

There are three ways to contribute, depending on how often you write docs and how comfortable you are with developer tooling.

---

### Path 1 — Read only (browser)

No setup required. Visit the published site at `<URL>` to browse and search all documentation.

---

### Path 2 — Occasional contributor (GitHub web editor)

For small edits, new notes, or fixing a typo without installing anything locally.

1. Go to the repository on GitHub.
2. Navigate to `Notes/`.
3. Click an existing file to edit it, or click **Add file → Create new file** to create a new note.
4. Write in plain Markdown. Use `[[Note name]]` for internal links.
5. Commit directly to a new branch and open a pull request.

---

### Path 3 — Regular contributor (Obsidian + Git)

Full local setup with the Obsidian knowledge graph, graph view, and plugin support.

### Prerequisites

- [Git](https://git-scm.com/)
- [Obsidian](https://obsidian.md/) (free)

### Committing and pushing

Write a short, descriptive commit message — the default is intentionally blank to force you to write one.

---

## Note conventions

See [Obsidian best practices](Notes/Obsidian%20best%20practices.md)for the full style guide. Key points:

- All notes go in `Notes/`. No sub-folders.
- All images and drawings go in `Attachments/`. No sub-folders.
- Use `[[wikilinks]]` for internal links. Link a term the first time it appears; not again.
- Add `last_reviewed` and `owner` frontmatter to [MOC pages](Notes/Maps%20Of%20Content.md).
## Folder structure

Flat folder structure, only one level of folders to keep the top level of the repository clean:
- Notes/
	- Contains all the [Markdown](Notes/Markdown.md) files and only Markdown files. Does not have any sub folders.
- Attachments/
	- Contains all non markdown files, like images, [Excalidraw](Notes/Excalidraw.md) drawings, pdf files, etc. Does not have any sub folders.
- index.md
	- This is the note that will be the start page for the [Website for this documentation](Notes/Website%20for%20this%20documentation.md)
- README.md
	- This note.

There are also hidden folders and files like:
- .obsidian
- .git
- .gitignore
- .obsidian.shared/
	- [[Obsidian shared settings]] that all contributors sync into their local `.obsidian/` folder.
- .scripts/
	- Automation scripts (see below).

There might also be a dedicated folder containing things related to [[AI Agents]] when we get to that point.

## Wikilinks

[Wikilinks](Notes/Wikilinks.md) will be the heart of this system. Take inspiration from Wikipedia where searching and links is the only way to navigate. The one exception is this README file, which uses normal markdown links in order to make them work in the bitbucket rendered README.

A good rule of thumb is that the first time something is mentioned in a note you create a link to it. Subsequent mentions should not be made into links.

It is okay to leave broken links — that is part of the Obsidian way of working. When someone else creates the target note, all existing links to it become connected automatically. Broken links are tracked by the [[Link health check]] workflow, which reports them weekly so they do not accumulate silently.

The usage of [MOC](Notes/MOC.md) pages, [Maps Of Content](Notes/Maps%20Of%20Content.md), will be central to create structure and ways to easily find and discover notes. A MOC is simply a note that contains links to other notes.

## Note naming

The file name of the note will also be used as the heading. So spaces in filenames will be necessary. And most notes will probably start with an upper case letters. The rule of thumb is to prioritize a nice heading over a nice file name.

## Version control

The vault is version controlled with [Git](Notes/Git.md).

Git will ensure that line endings are consistently using Linux style LF endings and not Windows style CRLF.

## Published website

The vault will be published as a website using [Quartz](Notes/Quartz.md), which is a static website generator. The website will be in a separate git repository. This repository shall only contain the documentation and not anything that is related to publishing. This separation makes it easy to replace Quartz with another static website generator like [Docusaurus](Notes/Docusaurus.md), for example.
