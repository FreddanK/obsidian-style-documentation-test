GitHub Actions is the CI/CD platform used to automate documentation quality checks in this vault.

## Workflows

### Validate shared settings

**File:** `.github/workflows/validate-shared-settings.yml`
**Triggers:** push or PR that modifies `.obsidian.shared/`

Runs `scripts/validate_shared_settings.py`, which checks:
- All JSON files in `.obsidian.shared/` are valid JSON.
- All required plugins (`obsidian-git`, `obsidian-excalidraw-plugin`) are listed in `community-plugins.json`.
- Each plugin folder has a `manifest.json` with a pinned version.

### Link health check

**File:** `.github/workflows/link-health.yml`
**Triggers:** push or PR touching `Notes/`; weekly schedule (Monday 08:00 UTC)

Runs `scripts/check_links.py` to find [[Wikilinks]] with no corresponding file.
- On a PR: posts a comment listing broken links.
- On a schedule: opens or updates a GitHub Issue.
- Fails the workflow if any broken links are found.

### MOC suggestions

**File:** `.github/workflows/moc-suggestions.yml`
**Triggers:** push to `main` touching `Notes/`; weekly schedule (Monday 08:05 UTC)

Runs `scripts/update_mocs.py`, which appends a *Suggested additions* section to any [[Maps Of Content|MOC]] that has notes linking to it but not yet listed in it. Commits the result with `[skip ci]` to avoid a loop.

## Scripts

All automation scripts live in `scripts/`:

| Script | Purpose |
|--------|---------|
| `apply_shared_settings.py` | Merge `.obsidian.shared/` into `.obsidian/` (run locally) |
| `validate_shared_settings.py` | CI check for shared settings validity |
| `check_links.py` | Find broken wikilinks |
| `update_mocs.py` | Suggest unlisted notes to MOC pages |

## Permissions

The MOC suggestions workflow pushes commits to `main`. If branch protection rules require PRs, change the workflow to open a pull request instead of committing directly. The `GITHUB_TOKEN` is sufficient for commits; use a PAT for cross-repo operations (needed for [[AI Agents]] Level 3).
