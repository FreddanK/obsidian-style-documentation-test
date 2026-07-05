In [[Obsidian]] there is no built-in way to share settings among multiple contributors while allowing some personal settings to differ. This vault solves the problem with a `.obsidian.shared/` folder and a sync script.

## How it works

The `.obsidian.shared/` folder is committed to the repository and contains the settings and plugin files that every contributor must have identical. Running the sync script merges those shared settings into the contributor's local `.obsidian/` folder, which is **git-ignored**.

Key properties of the merge:

- **JSON config files** — shared keys override local values; personal-only keys (hotkeys, themes) are preserved.
- **Plugin code files** (`.js`, `.css`) — always overwritten so plugin versions stay in sync.
- **Personal files** (`appearance.json`, `graph.json`, `workspace.json`) — always skipped.

## Setup for new contributors

```bash
# 1. Clone the repo
git clone <repo-url>
cd <repo-name>

# 2. Apply shared settings
python3 scripts/apply_shared_settings.py

# 3. Open the vault root in Obsidian
```

Re-run `apply_shared_settings.py` after pulling whenever `.obsidian.shared/` has changed.

## Shared settings reference

### app.json

| Setting | Value | Reason |
|---------|-------|--------|
| New notes location | `Notes/` | Keeps the flat folder structure |
| New attachments location | `Attachments/` | Keeps the flat folder structure |

### Plugins

Both plugins below are required. Do **not** upgrade them without updating the pinned version in `.obsidian.shared/plugins/<plugin>/manifest.json` and testing.

| Plugin | ID | Pinned version |
|--------|----|----------------|
| Git | `obsidian-git` | See manifest |
| Excalidraw | `obsidian-excalidraw-plugin` | See manifest |

**obsidian-git** changed settings:
- Empty default commit message (forces intentional commit messages).
- Rebase as the default merge strategy.

**obsidian-excalidraw-plugin** changed settings:
- Date/time suffix disabled on new drawing filenames.
- New drawings saved to `Attachments/`.

## CI validation

Every pull request that modifies `.obsidian.shared/` automatically runs `scripts/validate_shared_settings.py`, which checks that all JSON is valid and that all required plugins are present. See [[GitHub Actions]].

## Personal settings

Settings **not** managed here — left entirely to individual preference:
- Theme and colour scheme (`appearance.json`)
- Graph view layout (`graph.json`)
- Hotkeys
- Font size
- Vim mode
