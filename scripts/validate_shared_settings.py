#!/usr/bin/env python3
"""
validate_shared_settings.py

CI check: verifies that every JSON file in .obsidian.shared/ is valid JSON
and that the required plugins are listed in community-plugins.json.
Exits with code 1 on any failure.

Usage:
    python3 scripts/validate_shared_settings.py
"""

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SHARED_DIR = REPO_ROOT / ".obsidian.shared"
REQUIRED_PLUGINS = ["obsidian-excalidraw-plugin", "obsidian-git"]

errors: list[str] = []


def check_json_files():
    for path in sorted(SHARED_DIR.rglob("*.json")):
        relative = path.relative_to(REPO_ROOT)
        try:
            with open(path, encoding="utf-8") as f:
                json.load(f)
            print(f"  ✓ Valid JSON : {relative}")
        except json.JSONDecodeError as e:
            errors.append(f"Invalid JSON in {relative}: {e}")
            print(f"  ✗ Invalid    : {relative} — {e}")


def check_required_plugins():
    plugins_file = SHARED_DIR / "community-plugins.json"
    if not plugins_file.exists():
        errors.append("community-plugins.json missing from .obsidian.shared/")
        return
    with open(plugins_file, encoding="utf-8") as f:
        plugins = json.load(f)
    for plugin in REQUIRED_PLUGINS:
        if plugin in plugins:
            print(f"  ✓ Plugin present : {plugin}")
        else:
            msg = f"Required plugin missing from community-plugins.json: {plugin}"
            errors.append(msg)
            print(f"  ✗ {msg}")


def check_plugin_versions():
    """Ensure each plugin folder in .obsidian.shared has a manifest.json with a version."""
    plugins_dir = SHARED_DIR / "plugins"
    if not plugins_dir.exists():
        return
    for plugin_dir in sorted(plugins_dir.iterdir()):
        manifest = plugin_dir / "manifest.json"
        if not manifest.exists():
            errors.append(f"Plugin {plugin_dir.name} has no manifest.json")
            continue
        with open(manifest, encoding="utf-8") as f:
            data = json.load(f)
        version = data.get("version")
        if version:
            print(f"  ✓ Plugin {plugin_dir.name} pinned at version {version}")
        else:
            errors.append(f"Plugin {plugin_dir.name} manifest.json has no version field")


def main() -> int:
    print("=== Validating .obsidian.shared/ ===\n")
    check_json_files()
    print()
    check_required_plugins()
    print()
    check_plugin_versions()
    print()

    if errors:
        print(f"FAILED with {len(errors)} error(s):")
        for e in errors:
            print(f"  - {e}")
        return 1

    print("All checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
