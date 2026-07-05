Git is the version control system used to manage this documentation vault.

## Why Git for documentation

- Full history of every change, with author and timestamp.
- Pull requests enable peer review of documentation changes before they are merged.
- Plain [[Markdown]] files mean every standard Git tool (diff, blame, bisect) works without modification.
- No vendor lock-in — the content is always portable.

## Line endings

Git is configured (via `.gitattributes` or global config) to normalise all line endings to Unix LF. This prevents noise in diffs when contributors work on different operating systems.

## Workflow for contributors

Regular contributors use the **obsidian-git** plugin (see [[Obsidian shared settings]]) to commit and push from inside Obsidian. The plugin is configured to:
- Require a manual, intentional commit message (no auto-generated defaults).
- Use **rebase** as the default merge/pull strategy to keep history linear.

Occasional contributors can edit files directly in the GitHub web UI without any local setup — see [[CONTRIBUTING]].

## Commit message conventions

Use short imperative-mood messages that describe *what changed*, not *why*:

```
docs: add runbook for database migrations
docs: fix broken links in Backend MOC
docs: update Quartz publishing instructions
```

Prefix with `docs:` to distinguish documentation commits from code commits in repositories where both live together.

## Branch strategy

- `main` is the published branch. Direct pushes are discouraged.
- Create a feature branch for any non-trivial change, then open a pull request.
- The [[link health check]] and [[GitHub Actions|shared settings validation]] run automatically on every pull request.
