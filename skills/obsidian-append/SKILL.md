---
name: obsidian-append
description: Append text to an existing Obsidian note by relative path.
user-invocable: true
---

# Obsidian Append

Append text to an existing note using:
`/home/duane/.local/bin/openclaw-obsidian-append.sh`

## Input format
User will call the slash command with:

`Relative/Path.md | Text to append`

Example:
`00_Inbox/2026-02-27_195124__OpenClaw test note.md | Add this line`

## Behavior
- Split on the first `|` into path and text (trim whitespace).
- Call the append script with path and text as arguments.
- Use exec tool to run:
  `/home/duane/.local/bin/openclaw-obsidian-append.sh "<Relative/Path.md>" "<Text>"`

Return a short confirmation including the file path from stdout.
