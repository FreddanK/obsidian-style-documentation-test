This repository is a test to investigate if it would be feasible to keep the internal documentation of a medium size software organization in an [[Obsidian]] vault following [[Obsidian best practices]].

## Folder structure

Flat folder structure, only one level of folders to keep the top level of the repository clean:
- notes/
	- Contains all the [[Markdown]] files and only Markdown files. Does not have any sub folders.
- assets/
	- Contains all non markdown files, like images, [[Excalidraw]] drawings, pdf files, etc. Does not have any sub folders.
- index.md
	- This is the note that will be the start page for the [[Website for this documentation]]
- README.md
	- This note.

There are also hidden folders and files like:
- .obsidian
- .git
- .gitignore

A later extension will be files for [[AI Agents]].

## Wikilinks

Wikilinks will be the heart of this system. Take inspiration from Wikipedia where searching and links is the only way to navigate.

A good rule of thumb is that the first time something is mentioned in a note you create a link to it. Subsequent mentions should not be made into links.

It is okay to leave broken links, that is part of the Obsidian way of working. That way, if someone else links to the same thing and does create the note. All other notes with links to that thing will now be connected.

The usage of [[MOC]] pages, [[Maps Of Content]], will be central to create structure and ways to easily find and discover notes. A MOC is simply a note that contains links to other notes.

## Note naming

The file name of the note will also be used as the heading. So spaces in filenames will be necessary. And most notes will probably start with an upper case letters. The rule of thumb is to prioritize a nice heading over a nice file name.

## Version control

The vault is version controlled with [[Git]].

## Published website

The vault will be published as a website using [[Quartz]], which is a static website generator. The website will be in a separate git repository. This repository shall only contain the documentation and not anything that is related to publishing. This separation makes it easy to easily replace Quartz with another static website generator like [[Docusaurus]], for example.