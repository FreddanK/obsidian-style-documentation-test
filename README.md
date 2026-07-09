This repository is a test to investigate if it would be feasible to keep the internal documentation of a medium size software organization in an [[Obsidian]] vault following [[Obsidian best practices]]. 

## Getting Started

See [[CONTRIBUTING]]

## Folder structure

Flat folder structure, only one level of folders to keep the top level of the repository clean:
- Notes/
	- Contains all the [[Markdown]] files and only Markdown files. Does not have any sub folders.
- Attachments/
	- Contains all non markdown files, like images, [[Excalidraw]] drawings, pdf files, etc. Does not have any sub folders.
- index.md
	- This is the note that will be the start page for the [[Website for this documentation]]
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

[[Wikilinks]] will be the heart of this system. Take inspiration from Wikipedia where searching and links is the only way to navigate.

A good rule of thumb is that the first time something is mentioned in a note you create a link to it. Subsequent mentions should not be made into links.

It is okay to leave broken links — that is part of the Obsidian way of working. When someone else creates the target note, all existing links to it become connected automatically. Broken links are tracked by the [[Link health check]] workflow, which reports them weekly so they do not accumulate silently.

The usage of [[MOC]] pages, [[Maps Of Content]], will be central to create structure and ways to easily find and discover notes. A MOC is simply a note that contains links to other notes.

## Note naming

The file name of the note will also be used as the heading. So spaces in filenames will be necessary. And most notes will probably start with an upper case letters. The rule of thumb is to prioritize a nice heading over a nice file name.

## Version control

The vault is version controlled with [[Git]].

Git will ensure that line endings are consistently using Linux style LF endings and not Windows style CRLF.

## Published website

The vault will be published as a website using [[Quartz]], which is a static website generator. The website will be in a separate git repository. This repository shall only contain the documentation and not anything that is related to publishing. This separation makes it easy to replace Quartz with another static website generator like [[Docusaurus]], for example.

## Contributor guide

See [[CONTRIBUTING]] for step-by-step instructions for readers, occasional editors, and regular contributors.
