#!/usr/bin/env python3
"""
apply_shared_settings.py

Syncs .obsidian.shared/ settings into .obsidian/, merging JSON files so that
shared settings take precedence while personal-only settings are preserved.

Usage:
    python3 scripts/apply_shared_settings.py

Strategy:
  - JSON dicts:  shared keys override local; personal-only keys are kept.
  - JSON lists:  union of shared and local (e.g. community-plugins.json).
  - Binary/JS/CSS files: always overwrite (plugin code must stay in sync).
  - Personal-only files (appearance.json, graph.json, workspace.json) are skipped.
"""

import json
import os
import shutil
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SHARED_DIR = REPO_ROOT / ".obsidian.shared"
LOCAL_DIR = REPO_ROOT / ".obsidian"

# These files capture personal state and must never be overwritten by shared settings.
SKIP_FILES = {"appearance.json", "graph.json", "workspace.json"}


def merge_json(local_path: Path, shared_data):
    """
    Merge shared_data into the existing local JSON file.
    - Dicts: shared keys override; personal-only keys are kept.
    - Lists: set union (shared items added if missing from local).
    - Primitives / type mismatch: shared wins.
    """
    if local_path.exists():
        try:
            with open(local_path, encoding="utf-8") as f:
                local_data = json.load(f)
        except json.JSONDecodeError:
            print(f"    WARNING: {local_path} contains invalid JSON — overwriting.")
            local_data = type(shared_data)()
    else:
        local_data = type(shared_data)() if isinstance(shared_data, (dict, list)) else None

    if isinstance(shared_data, dict) and isinstance(local_data, dict):
        merged = {**local_data, **shared_data}
        return merged
    elif isinstance(shared_data, list) and isinstance(local_data, list):
        merged = list(local_data)
        for item in shared_data:
            if item not in merged:
                merged.append(item)
        return merged
    else:
        return shared_data


def apply():
    if not SHARED_DIR.exists():
        print(f"Error: {SHARED_DIR} does not exist.")
        return 1

    LOCAL_DIR.mkdir(exist_ok=True)

    synced = 0
    skipped = 0

    for shared_file in sorted(SHARED_DIR.rglob("*")):
        if not shared_file.is_file():
            continue
        if shared_file.name in SKIP_FILES:
            print(f"  Skipping personal file : {shared_file.relative_to(SHARED_DIR)}")
            skipped += 1
            continue

        relative = shared_file.relative_to(SHARED_DIR)
        target = LOCAL_DIR / relative
        target.parent.mkdir(parents=True, exist_ok=True)

        if shared_file.suffix == ".json":
            with open(shared_file, encoding="utf-8") as f:
                shared_data = json.load(f)
            merged = merge_json(target, shared_data)
            with open(target, "w", encoding="utf-8") as f:
                json.dump(merged, f, indent=2, ensure_ascii=False)
                f.write("\n")
            print(f"  Merged  : {relative}")
        else:
            shutil.copy2(shared_file, target)
            print(f"  Copied  : {relative}")

        synced += 1

    print(f"\nDone. {synced} file(s) synced, {skipped} skipped.")
    return 0


if __name__ == "__main__":
    sys.exit(apply())
