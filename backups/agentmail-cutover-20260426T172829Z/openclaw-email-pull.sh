#!/usr/bin/env bash
set -euo pipefail

GOG_ACCOUNT="alfred.opclaw@gmail.com"
CHAT_ID="7764426016"
OUT_JSON="/tmp/openclaw-email-pull.json"
REPORT="/tmp/openclaw-email-pull-report.json"

if ! command -v gog >/dev/null 2>&1; then
  echo "Email pull failed: gog CLI not found."
  exit 1
fi

# Pull unread inbox messages (threads)
if ! gog gmail messages search "in:inbox is:unread newer_than:2d" --max 50 --json --account "$GOG_ACCOUNT" > "$OUT_JSON"; then
  echo "Email pull failed for $GOG_ACCOUNT."
  exit 1
fi

python3 - <<'PY'
import json, re, os, subprocess, base64
from pathlib import Path
from datetime import datetime, timezone

ACCOUNT='alfred.opclaw@gmail.com'
OUT_JSON=Path('/tmp/openclaw-email-pull.json')
REPORT=Path('/tmp/openclaw-email-pull-report.json')

work_dir=Path('/mnt/obsidian/00_Alfred/20_Diversys_Email')
personal_dir=Path('/mnt/obsidian/01_Elliot/10_Personal_Email')
clients_root=Path('/mnt/obsidian/00_Alfred/10_Diversys/Clients')
action_register=Path('/mnt/obsidian/05_Action_Items/Action Register.md')

work_dir.mkdir(parents=True, exist_ok=True)
personal_dir.mkdir(parents=True, exist_ok=True)

client_domain_map={
    'returnit.ca':'ENCORP',
    'oneturfpro':'Tarkett',
    'ekocircles.com':'Ekocircles',
    'calrecycle.ca.gov':'CalRecycle',
    'aramco.com':'Aramco'
}

stats={
    'unread':0,
    'notes_created':0,
    'client_notes':0,
    'actions_added':0,
    'drafts_created':0,
    'marked_read':0,
    'skipped_empty':0
}

# simple client match

def match_client(email):
    for dom, name in client_domain_map.items():
        if dom in email:
            return name
    return None

# parse date from forwarded content if present

def parse_forwarded_date(body):
    m=re.search(r'^Date:\s*(.*)$', body, re.M)
    if not m:
        return None
    try:
        return datetime.strptime(m.group(1)[:25], '%a, %d %b %Y %H:%M:%S')
    except Exception:
        return None

# decide triage

def triage(body):
    b=body.lower()
    requires_action=bool(re.search(r'\b(please|need|action|required|asap|by\s+\w+|request|follow up)\b', b))
    requires_response=bool(re.search(r'\b(reply|respond|response|can you|could you|please advise|let me know)\b', b) or '?' in body)
    if requires_action or requires_response:
        return 'Requires Action' if requires_action else 'Requires Response', requires_action, requires_response
    return 'Info Only', False, False

# update action register

def normalize_action_register():
    """Renumber actions per section/subsection and keep readable copy in sync."""
    if not action_register.exists():
        return
    text = action_register.read_text()
    lines = text.splitlines()
    section = None
    subsection = None
    counters = {}
    new_lines = []

    for line in lines:
        stripped = line.strip()
        if stripped.startswith('## '):
            section = stripped
            new_lines.append(line)
            continue
        if stripped.startswith('### '):
            subsection = stripped
            new_lines.append(line)
            counters[(section, subsection)] = 0
            continue
        if stripped.startswith('- [#'):
            key = (section, subsection)
            if key not in counters:
                counters[key] = 0
            counters[key] += 1
            num = counters[key]
            line = re.sub(r"- \[#\d+\]", f"- [#{num}]", line)
            new_lines.append(line)
        else:
            new_lines.append(line)

    new_text = "\n".join(new_lines)
    action_register.write_text(new_text)

    # Keep readable copy in sync
    readable = Path('/mnt/obsidian/05_Action_Items/Action_Register_Readable.md')
    try:
        readable.write_text(new_text)
    except Exception:
        pass


def add_action(action_text, source_title, owner='Duane'):
    """Add a new Open action under My Actions and normalize numbering."""
    if not action_register.exists():
        return
    text = action_register.read_text()
    today = datetime.now().strftime('%Y-%m-%d')
    line = (
        f"- [#0] Open Date: {today} | Owner: {owner} | Status: Open | Close Date:  | "
        f"Source: {source_title} | Action: {action_text}"
    )

    # Insert just before My Actions → Pending Actions header
    pattern = "### Pending Actions"
    if pattern in text:
        text = text.replace(pattern, line + '\n\n' + pattern, 1)
    else:
        # Fallback: append at end of file
        if not text.endswith('\n'):
            text += '\n'
        text += '\n' + line + '\n'

    action_register.write_text(text)
    normalize_action_register()

# write note

def write_note(folder, subject, meta, body):
    safe=re.sub(r'[^A-Za-z0-9 _-]','', subject).strip().replace(' ','_')
    if not safe:
        safe='email'
    name=f"{meta['date']}_{safe}.md"
    path=folder/name
    content=f"# {subject}\n\n- From: {meta['from']}\n- To: {meta['to']}\n- Date: {meta['date']}\n- Triage: {meta['triage']}\n\n## Body\n\n{body}\n"
    path.write_text(content)
    return path

# mark read helper (thread)

def mark_thread_processed(thread_id):
    """Mark Gmail thread as processed: read, archived, and labeled."""
    try:
        subprocess.run([
            'gog','gmail','threads','modify',thread_id,
            '--remove-labels','UNREAD,INBOX',
            '--add-labels','OpenClaw-Processed',
            '--account',ACCOUNT
        ], check=True)
        return True
    except Exception:
        return False

# decode body from Gmail message payload

def decode_body(payload):
    if not payload:
        return ''
    body=payload.get('body',{})
    data=body.get('data')
    if data:
        return base64.urlsafe_b64decode(data + '===').decode('utf-8', errors='ignore')
    # walk parts
    parts=payload.get('parts',[])
    for p in parts:
        mime=p.get('mimeType','')
        if mime=='text/plain':
            data=p.get('body',{}).get('data')
            if data:
                return base64.urlsafe_b64decode(data + '===').decode('utf-8', errors='ignore')
        # recurse
        if p.get('parts'):
            b=decode_body(p)
            if b:
                return b
    return ''

# get full thread

def get_thread(thread_id):
    try:
        raw=subprocess.check_output(['gog','gmail','threads','get',thread_id,'--json','--account',ACCOUNT])
        return json.loads(raw)
    except Exception:
        return None

# load messages
if OUT_JSON.exists():
    data=json.loads(OUT_JSON.read_text())
else:
    data={'messages':[]}

msgs=data.get('messages',[])
stats['unread']=len(msgs)

for msg in msgs:
    thread_id=msg.get('threadId')
    message_id=msg.get('id')
    thread=get_thread(thread_id) if thread_id else None
    # select last message in thread
    thread_msgs=thread.get('messages',[]) if thread else []
    last=thread_msgs[-1] if thread_msgs else msg

    headers={}
    for h in last.get('payload',{}).get('headers',[]):
        headers[h.get('name')]=h.get('value')
    sender=headers.get('From','')
    to=headers.get('To','')
    subject=headers.get('Subject','(no subject)')

    internal=last.get('internalDate') or msg.get('internalDate')
    if internal:
        dt=datetime.fromtimestamp(int(internal)/1000, tz=timezone.utc)
    else:
        dt=datetime.now(timezone.utc)

    body=decode_body(last.get('payload',{})) or last.get('snippet','') or msg.get('snippet','')

    fwd_date=parse_forwarded_date(body)
    if fwd_date and (fwd_date.year < 2025 or (fwd_date.year==2025 and fwd_date.month < 12)):
        if thread_id and mark_thread_processed(thread_id):
            stats['marked_read']+=1
        continue

    if (not sender and not to and (subject=='(no subject)') and not body.strip()):
        stats['skipped_empty']+=1
        if thread_id and mark_thread_processed(thread_id):
            stats['marked_read']+=1
        continue

    triage_label, req_action, req_response = triage(body)

    sender_dom=sender.lower()
    is_personal='@gmail.com' in sender_dom
    folder=personal_dir if is_personal else work_dir

    meta={
        'from': sender,
        'to': to,
        'date': dt.astimezone().strftime('%Y-%m-%d_%H%M%S'),
        'triage': triage_label
    }

    note_path=write_note(folder, subject, meta, body)
    stats['notes_created'] += 1

    client=match_client(sender_dom)
    if client:
        client_folder=clients_root/client
        if client_folder.exists():
            client_note=client_folder/f"{meta['date']}__{subject.replace(' ','_')}.md"
            client_note.write_text(note_path.read_text())
            stats['client_notes'] += 1
        else:
            # Log missing client folder so it can be surfaced elsewhere
            missing_log = clients_root / '_Missing_Client_Folders.md'
            msg = f"- {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | Missing client folder for {client} (email from: {sender})"
            if missing_log.exists():
                existing = missing_log.read_text()
                missing_log.write_text(existing + "\n" + msg)
            else:
                missing_log.write_text("# Missing Client Folders\n\n" + msg + "\n")

    if req_action:
        add_action(f"Review and act on email: {subject}", subject)
        stats['actions_added'] += 1

    if req_response:
        draft=(folder/f"{meta['date']}__Response_{subject.replace(' ','_')}.md")
        draft.write_text(f"# Response: {subject}\n\nDraft response needed.\n")
        stats['drafts_created'] += 1

    if thread_id and mark_thread_processed(thread_id):
        stats['marked_read']+=1

REPORT.write_text(json.dumps(stats))
PY

# Build summary message
if [ -f "$REPORT" ]; then
  unread=$(python3 - <<'PY'
import json
from pathlib import Path
print(json.loads(Path('/tmp/openclaw-email-pull-report.json').read_text()).get('unread',0))
PY
)
  notes=$(python3 - <<'PY'
import json
from pathlib import Path
print(json.loads(Path('/tmp/openclaw-email-pull-report.json').read_text()).get('notes_created',0))
PY
)
  client_notes=$(python3 - <<'PY'
import json
from pathlib import Path
print(json.loads(Path('/tmp/openclaw-email-pull-report.json').read_text()).get('client_notes',0))
PY
)
  actions=$(python3 - <<'PY'
import json
from pathlib import Path
print(json.loads(Path('/tmp/openclaw-email-pull-report.json').read_text()).get('actions_added',0))
PY
)
  drafts=$(python3 - <<'PY'
import json
from pathlib import Path
print(json.loads(Path('/tmp/openclaw-email-pull-report.json').read_text()).get('drafts_created',0))
PY
)
  marked=$(python3 - <<'PY'
import json
from pathlib import Path
print(json.loads(Path('/tmp/openclaw-email-pull-report.json').read_text()).get('marked_read',0))
PY
)
  skipped=$(python3 - <<'PY'
import json
from pathlib import Path
print(json.loads(Path('/tmp/openclaw-email-pull-report.json').read_text()).get('skipped_empty',0))
PY
)

  if [ "$unread" -eq 0 ] && [ "$notes" -eq 0 ] && [ "$actions" -eq 0 ] && [ "$drafts" -eq 0 ]; then
    exit 0
  fi

  MSG="Email pull completed.\nActions taken:\n- Unread messages: ${unread}\n- Notes created: ${notes}\n- Client notes created: ${client_notes}\n- Actions added: ${actions}\n- Draft responses created: ${drafts}\n- Messages marked read: ${marked}\n- Empty messages skipped: ${skipped}"
else
  MSG="Email pull completed. No report was produced."
fi

echo "$MSG"
