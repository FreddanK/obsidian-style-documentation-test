This vault is published as a static website so that anyone in the organisation can read the documentation without installing [[Obsidian]] or setting up [[Git]].

## Goals

- Zero-friction read access for all contributors, regardless of technical background.
- Full wikilink navigation preserved as clickable hyperlinks.
- Search across all notes.
- Automatic tag index pages as a maintenance-free complement to [[Maps Of Content]].

## Implementation

The site is built with [[Quartz]] from a separate Git repository. See [[Quartz]] for the architecture and publishing workflow.

## URL structure

Each note in `Notes/` becomes a page at `/<note-name>/`. The note filename (without `.md`) becomes the URL slug, with spaces converted to hyphens.

## Access

- **Internal team**: accessible at `<internal URL>` — no login required on the internal network.
- **Public**: TBD — decide whether this documentation is public or private.

## Relationship to the vault

This repo contains **only** documentation source files. It knows nothing about Quartz, deployment, or hosting. That separation keeps this repo simple and makes it straightforward to change the publishing technology in future. See [[Quartz]] and [[Docusaurus]].
