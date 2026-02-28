---
name: obsidian-capture
description: Capture a new note into Obsidian 00_Inbox via OpenClaw.
user-invocable: true
---

# Obsidian Capture

You capture a new note into the Obsidian vault inbox using:
`/home/duane/.local/bin/openclaw-obsidian-capture.sh`

## Input format
User will call the slash command with either:

1) `Title | Body text`
2) `Body text` (no separator)

## Behavior
- If input contains `|`, split into Title and Body (trim whitespace).
- If no `|`, use Title = "Quick Capture" and Body = full input.
- Call the capture script with Title and Body as separate arguments.
- Use exec tool to run:
  `/home/duane/.local/bin/openclaw-obsidian-capture.sh "<Title>" "<Body>"`

Return a short confirmation including the file path from stdout.
