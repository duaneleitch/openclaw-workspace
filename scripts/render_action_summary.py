#!/usr/bin/env python3
"""Render the Open Actions table from Duane's canonical readable register."""
from pathlib import Path
import re

REGISTER = Path('/mnt/obsidian/05_Action_Items/Action_Register_Readable.md')
text = REGISTER.read_text(encoding='utf-8')
section = text.split('## Open Actions', 1)[1].split('## Pending Actions', 1)[0]
rows = [line.strip() for line in section.splitlines() if line.startswith('| A-')]
items = []
for row in rows:
    cells = [cell.strip() for cell in row.strip('|').split('|')]
    if len(cells) >= 7:
        action = re.sub(r'`([^`]+)`', r'\1', cells[1])
        action = re.sub(r'\s+', ' ', action)
        items.append((cells[0], cells[2], cells[3] or 'No due date', action))

print('**Morning Action Items Summary**')
print('[Open the Action Register](obsidian://open?vault=Obsidian&file=05_Action_Items%2FAction_Register_Readable)')
if not items:
    print('\nNo open actions.')
else:
    print(f'\n{len(items)} open action' + ('' if len(items) == 1 else 's') + ':')
    for action_id, priority, due, action in items:
        print(f'- **{action_id}** · {priority} · {due}: {action}')
    print('\nReply with the action ID and an update, for example: `A-001: complete`.')
