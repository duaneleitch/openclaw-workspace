---
name: obsidian-recent
description: List recent notes in Obsidian 00_Inbox.
user-invocable: true
---

# Obsidian Recent

List recent notes in the Obsidian inbox using:
`/home/duane/.local/bin/openclaw-obsidian-recent.sh`

## Input format
User may pass an optional number (count). Example:

`5`

## Behavior
- If a number is provided, use it as count; default to 10.
- Call the recent script with count as a single argument.
- Use exec tool to run:
  `/home/duane/.local/bin/openclaw-obsidian-recent.sh <count>`

Return a short list of filenames.
