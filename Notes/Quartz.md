Quartz is the static site generator used to publish this vault as a website.

## What it does

Quartz takes the [[Markdown]] notes in this vault and converts them into a fast, fully-linked static website — including:
- Rendered [[Wikilinks]] as clickable hyperlinks.
- A graph view showing how notes connect.
- Full-text search.
- Tag index pages (automatically generated from frontmatter `tags`).
- Backlinks section on every page.

## Repository separation

The Quartz publishing configuration lives in a **separate Git repository**. This vault contains only documentation. That separation means:
- The publishing layer can be swapped for [[Docusaurus]] or anything else without touching the docs.
- Contributors do not need to understand Quartz to write documentation.

## How publishing works

1. The Quartz repo points at this vault's `Notes/` as its content source (via a Git submodule or a CI copy step).
2. On every push to `main` in *this* repo, a CI workflow triggers a build in the Quartz repo.
3. The built site is deployed to the target hosting platform (GitHub Pages, Vercel, Cloudflare Pages, etc.).

## Local preview

To preview the site locally before pushing:

```bash
# In the Quartz repo (not this one)
npx quartz build --serve
```

## See also

- [[Docusaurus]] — the alternative static site generator considered for this vault.
- [[Website for this documentation]] — decisions and context around the published site.
