#!/usr/bin/env python3
"""Render the canonical Action Items register for the daily reminder."""
from pathlib import Path
import re

REGISTER = Path('/mnt/obsidian/20_Knowledge/Wiki/Tasks/Action-Items.md')
REGISTER_LINK = 'obsidian://open?vault=Obsidian&file=20_Knowledge%2FWiki%2FTasks%2FAction-Items'


def clean(value):
    value = re.sub(r'`([^`]+)`', r'\1', value)
    return re.sub(r'\s+', ' ', value).strip()


def table_rows(text, heading, next_heading):
    section = text.split(heading, 1)[1].split(next_heading, 1)[0]
    return [[clean(cell) for cell in line.strip().strip('|').split('|')]
            for line in section.splitlines() if line.startswith('| A-')]


text = REGISTER.read_text(encoding='utf-8')
open_rows = table_rows(text, '## Open Actions', '## Pending Actions')
pending_rows = table_rows(text, '## Pending Actions', '## Completion Archive')

print('**Daily Action Items Reminder**')
print(f'[Open Action Items]({REGISTER_LINK})')
print(f'\nActive items: {len(open_rows)} open, {len(pending_rows)} pending.')

if open_rows:
    print('\n**Open Actions**')
    for row in open_rows:
        action_id, action, priority, due, next_step, reviewed, notes = row[:7]
        print(f'- **{action_id}** ({priority}, due: {due or "No due date"})')
        print(f'  Summary: {action}')
        print(f'  Next step: {next_step or "Not specified"}')

if pending_rows:
    print('\n**Pending Actions**')
    for row in pending_rows:
        action_id, action, dependency, review, reviewed, notes = row[:6]
        print(f'- **{action_id}** (next review: {review or "Not specified"})')
        print(f'  Summary: {action}')
        print(f'  Waiting on: {dependency or "Not specified"}')

if not open_rows and not pending_rows:
    print('\nNo active action items.')
else:
    print('\nReply with an action ID and update, for example: `A-002: complete`.')
