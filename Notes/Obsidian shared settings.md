In [[Obsidian]] there is no built in functionality to share settings among multiple people while allowing some settings to be different and some to be the same.

To solve this problem. This repo has a .obsidian.shared folder that contains the settings that should be the same for all contributors of this repo in order to ensure a smooth workflow.

The shared settings can be synced with the content in the obisidan folder using the script apply_shared_settings.py. There are very few settings that are shared because most defaults work fine.

### Default settings

Place new notes in a folder called Notes/

Place new attachments in a folder called Attachments/

Install and enable the Excalidraw community plugin.
Changed settings:
- Don't append the date and time to the name of new drawings.
- Place new Excalidraw drawings in the Attachments folder.

Install and enabled the Git community plugin.
Changed settings:
- Don't use a default commit message for manual commits.
- Use rebase as the default merge strategy.


- 