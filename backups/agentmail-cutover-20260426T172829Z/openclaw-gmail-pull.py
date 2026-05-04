#!/usr/bin/env python3
import json, os, re, subprocess, time, textwrap, shlex

ACCOUNT = "alfred.opclaw@gmail.com"
LABEL = "OpenClaw-Processed"
DEFAULT_DIR = "/mnt/obsidian/01_Elliot/10_Personal_Email"
DIVERSYS_DIR = "/mnt/obsidian/00_Alfred/20_Diversys_Email"
ACTION_DIR = "/mnt/obsidian/05_Action_Items"
ACTION_REGISTER = "/mnt/obsidian/05_Action_Items/Action Register.md"
PRODUCT_TRAINING_DIR = "/mnt/obsidian/00_Alfred/10_Diversys/Product/Training"
PRODUCT_API_DIR = "/mnt/obsidian/00_Alfred/10_Diversys/Product/API_Knowledge"
PERSONAL_TRANSCRIPTS_DIR = "/mnt/obsidian/01_Elliot/20_Personal_Knowledge/Videos_Transcripts"
PERSONAL_TRANSCRIPTS_INDEX = "/mnt/obsidian/01_Elliot/20_Personal_Knowledge/Transcripts_Index.md"
CLIENT_FOLDERS = {
    "abcrc": "/mnt/obsidian/00_Alfred/10_Diversys/Clients/ABCRC/ABCRC_Email",
    "encorp": "/mnt/obsidian/00_Alfred/10_Diversys/Clients/ENCORP/ENCORP_Email",
    "calrecycle": "/mnt/obsidian/00_Alfred/10_Diversys/Clients/CalRecycle/CalRecycle_Email",
    "tarkett": "/mnt/obsidian/00_Alfred/10_Diversys/Clients/Tarkett/Tarkett_Email",
    "ekocircles": "/mnt/obsidian/00_Alfred/10_Diversys/Clients/EkoCircles/EkoCircles_Email",
    "aramco": "/mnt/obsidian/00_Alfred/10_Diversys/Clients/Aramco/Aramco_Email",
}
CLIENT_ALIASES = {
    "return-it": "encorp",
    "returnit": "encorp",
    "returnit.ca": "encorp",
    "one turf pro": "tarkett",
    "oneturfpro": "tarkett",
}
QUERY = f"newer_than:2d -label:{LABEL}"
MAX_RESULTS = "20"

OPENCLAW_BIN = "/home/duane/.npm-global/bin/openclaw"
GOG_BIN = "gog"

os.environ["GOG_KEYRING_PASSWORD"] = ""

os.makedirs(DEFAULT_DIR, exist_ok=True)

SUPPORT_INFO_PROMPTS = [
    "Which user/account were you using?",
    "Exact endpoint and environment (prod/sandbox)?",
    "Timestamp and timezone of the request?",
    "Request method and full URL?",
    "Request payload/body and headers?",
    "Response payload and HTTP status code?",
    "Is this reproducible? If yes, steps to reproduce?",
    "Any recent changes before the issue?",
    "Screenshots/logs if available?"
]

SUPPORT_KEYWORDS = ["api", "endpoint", "error", "issue", "bug", "failed", "failure", "exception", "response code", "status code"]
TRAINING_KEYWORDS = ["training", "session", "workshop", "enablement", "configuration", "admin portal", "web platform"]
API_KEYWORDS = ["api", "endpoint", "swagger", "postman", "payload", "response"]
MARKETING_KEYWORDS = ["campaign", "marketing", "webinar", "newsletter", "press", "launch", "brand", "positioning"]
DELIVERY_KEYWORDS = ["implementation", "project", "timeline", "milestone", "deployment", "rollout"]
PRODUCT_KEYWORDS = ["feature", "roadmap", "product", "bug", "enhancement", "release"]
PERSONAL_TRANSCRIPT_KEYWORDS = ["transcript", "youtube", "podcast", "talk", "keynote", "course"]


def run(cmd, input_text=None):
    return subprocess.check_output(cmd, text=True, input=input_text)

# Ensure label exists
try:
    run([GOG_BIN,"gmail","labels","create","--account",ACCOUNT, LABEL])
except Exception:
    pass


def select_folder(sender, body):
    combo = (sender + "\n" + body).lower()

    # client-specific routing (highest priority)
    for key, path in CLIENT_FOLDERS.items():
        if key in combo:
            return path

    # alias routing
    for alias, target in CLIENT_ALIASES.items():
        if alias in combo and target in CLIENT_FOLDERS:
            return CLIENT_FOLDERS[target]

    # forwarded routing based on forwarding sender
    if "duane.leitch@diversys.com" in combo:
        return DIVERSYS_DIR
    if "duane.leitch@gmail.com" in combo:
        return DEFAULT_DIR

    # general diversys routing
    if "@diversys.com" in combo:
        return DIVERSYS_DIR

    return DEFAULT_DIR


def is_support(subject, body):
    combo = (subject + "\n" + body).lower()
    return any(k in combo for k in SUPPORT_KEYWORDS)


def detect_secondary(subject, body, attachments):
    combo = (subject + "\n" + body + "\n" + "\n".join(attachments)).lower()
    flags = []
    if any(k in combo for k in TRAINING_KEYWORDS):
        flags.append("training")
    if any(k in combo for k in API_KEYWORDS):
        flags.append("api")
    if any(k in combo for k in PERSONAL_TRANSCRIPT_KEYWORDS):
        flags.append("personal_transcript")
    return flags


def confidence_score(subject, body, attachments):
    combo = (subject + "\n" + body + "\n" + "\n".join(attachments)).lower()
    hits = 0
    hits += sum(1 for k in TRAINING_KEYWORDS if k in combo)
    hits += sum(1 for k in API_KEYWORDS if k in combo)
    hits += sum(1 for k in SUPPORT_KEYWORDS if k in combo)
    hits += sum(1 for k in PERSONAL_TRANSCRIPT_KEYWORDS if k in combo)
    if hits >= 3:
        return "high"
    if hits == 2:
        return "med"
    return "low"


def ai_triage(subject, sender, date, body):
    prompt = textwrap.dedent(f"""
    You are triaging an inbound email for a busy executive.
    Return ONLY valid JSON with these keys:
    info_only (yes/no)
    action_required (yes/no)
    response_required (yes/no/maybe)
    priority (low/med/high)
    due (now/today/this_week/none)
    summary (2-3 sentences)
    my_actions (array of strings)
    other_actions (array of objects: {{owner, action}})
    missing_info (array of strings)

    Email metadata:
    From: {sender}
    Date: {date}
    Subject: {subject}

    Email body:
    {body}
    """).strip()

    raw = run([OPENCLAW_BIN,"agent","--agent","analyst","--message", prompt, "--json"])
    data = json.loads(raw)
    text = data.get("result", {}).get("payloads", [{}])[0].get("text", "")
    m = re.search(r"\{.*\}", text, re.S)
    if not m:
        return None
    try:
        return json.loads(m.group(0))
    except Exception:
        return None


def route_agents(subject, body):
    combo=(subject+"\n"+body).lower()
    agents=[]
    if any(k in combo for k in MARKETING_KEYWORDS):
        agents += ["sales_marketing_manager","marketing_specialist"]
    if any(k in combo for k in DELIVERY_KEYWORDS):
        agents += ["services_support_manager","project_manager"]
    if any(k in combo for k in PRODUCT_KEYWORDS):
        agents += ["product_dev_manager","product_manager"]
    if is_support(subject, body):
        agents += ["tech_expert","support_lead"]
    # dedupe
    return list(dict.fromkeys(agents))


def collect_agent_notes(subject, sender, date, body, agents):
    notes=[]
    for agent in agents:
        prompt=textwrap.dedent(f"""
        Provide 3-5 bullet insights relevant to this email. Focus on actionable analysis.
        Email metadata:\nFrom: {sender}\nDate: {date}\nSubject: {subject}\n\nEmail body:\n{body}\n
        Return only bullets.
        """).strip()
        raw = run([OPENCLAW_BIN,"agent","--agent",agent,"--message",prompt,"--json"])
        data = json.loads(raw)
        text = data.get("result", {}).get("payloads", [{}])[0].get("text", "")
        notes.append(f"## {agent}\n{text}\n")
    return "\n".join(notes)


def obsidian_search_snippets(query):
    try:
        cmd = ["bash","-lc", f"grep -RIn --max-count=5 --include='*.md' {shlex.quote(query)} /mnt/obsidian 2>/dev/null || true"]
        out = run(cmd)
        return out.strip()
    except Exception:
        return ""


def ai_draft(subject, sender, date, body, triage, missing_info, obsidian_hits, agent_notes):
    prompt = textwrap.dedent(f"""
    Draft a concise, professional, human-sounding reply.
    If missing_info is non-empty, the response must ask for those details first
    and should NOT claim investigation has started.
    Use only dashes (-) for lists. Do not use asterisks.

    Triage:
    {json.dumps(triage, ensure_ascii=False)}

    Missing info:
    {json.dumps(missing_info, ensure_ascii=False)}

    Agent notes:
    {agent_notes if agent_notes else '(none)'}

    Obsidian hits:
    {obsidian_hits if obsidian_hits else '(none)'}

    Email metadata:
    From: {sender}
    Date: {date}
    Subject: {subject}

    Email body:
    {body}

    Return ONLY the draft body (no preamble).
    """).strip()

    raw = run([OPENCLAW_BIN,"agent","--agent","execpen","--message", prompt, "--json"])
    data = json.loads(raw)
    return data.get("result", {}).get("payloads", [{}])[0].get("text", "").strip()


def append_backlink(master_path, link_path, label):
    with open(master_path, "a", encoding="utf-8") as f:
        f.write(f"\n## Secondary Notes\n- {label}: [[{os.path.relpath(link_path, '/mnt/obsidian')}]]\n")


def append_action_register(subject, triage, master_rel):
    os.makedirs(ACTION_DIR, exist_ok=True)
    if not os.path.exists(ACTION_REGISTER):
        with open(ACTION_REGISTER, "w", encoding="utf-8") as f:
            f.write("# Action Register\n\n")
    with open(ACTION_REGISTER, "a", encoding="utf-8") as f:
        f.write(f"## {time.strftime('%Y-%m-%d')} — {subject}\n")
        f.write(f"- Master note: [[{master_rel}]]\n")
        for a in (triage.get('my_actions') or []):
            f.write(f"- My action: {a}\n")
        for oa in (triage.get('other_actions') or []):
            f.write(f"- Other action ({oa.get('owner','')}): {oa.get('action','')}\n")
        f.write("\n")


def update_transcript_index(note_rel):
    os.makedirs(PERSONAL_TRANSCRIPTS_DIR, exist_ok=True)
    if not os.path.exists(PERSONAL_TRANSCRIPTS_INDEX):
        with open(PERSONAL_TRANSCRIPTS_INDEX, "w", encoding="utf-8") as f:
            f.write("# Transcripts Index\n\n")
    with open(PERSONAL_TRANSCRIPTS_INDEX, "a", encoding="utf-8") as f:
        f.write(f"- [[{note_rel}]]\n")


def action_due_tag(due):
    return {
        "now": "#action/now",
        "today": "#action/today",
        "this_week": "#action/this_week",
        "none": "#action/unscheduled"
    }.get(due, "#action/unscheduled")


# Search recent unprocessed threads
out = run([GOG_BIN,"gmail","search","--account",ACCOUNT,"--max",MAX_RESULTS,"--json","--results-only", QUERY])
items = json.loads(out)
if not items:
    raise SystemExit(0)

for item in items:
    msg_id = item.get("id")
    if not msg_id:
        continue
    detail = json.loads(run([GOG_BIN,"gmail","get","--account",ACCOUNT,"--format","full","--json", msg_id]))
    headers = detail.get("headers", {})
    body = detail.get("body", "").strip()
    subject = headers.get("subject","(no subject)")
    sender = headers.get("from","(unknown)")
    date = headers.get("date","")
    thread_id = detail.get("message",{}).get("threadId", msg_id)
    attachments = [a.get('filename','') for a in detail.get('attachments', [])]

    triage = ai_triage(subject, sender, date, body) or {
        "info_only":"no",
        "action_required":"yes",
        "response_required":"maybe",
        "priority":"med",
        "due":"this_week",
        "summary":"",
        "my_actions":[],
        "other_actions":[],
        "missing_info":[]
    }

    missing = triage.get("missing_info", []) or []
    if is_support(subject, body) and not missing:
        missing = SUPPORT_INFO_PROMPTS

    agents = route_agents(subject, body)
    agent_notes = collect_agent_notes(subject, sender, date, body, agents) if agents else ""

    keywords = " ".join(subject.split()[:3])
    obsidian_hits = obsidian_search_snippets(keywords) if keywords else ""

    draft = ""
    if triage.get("response_required","maybe") in ["yes","maybe"]:
        draft = ai_draft(subject, sender, date, body, triage, missing, obsidian_hits, agent_notes)

    safe = re.sub(r"[^A-Za-z0-9 _-]+","", subject).strip() or "email"
    ts = time.strftime("%Y-%m-%d_%H%M%S")
    filename = f"{ts}__{safe}.md"
    target_dir = select_folder(sender, body)
    os.makedirs(target_dir, exist_ok=True)
    path = os.path.join(target_dir, filename)

    content = []
    content.append(f"# {subject}")
    content.append("")
    content.append("## Summary")
    content.append(f"- From: {sender}")
    content.append(f"- Date: {date}")
    content.append(f"- Info Only: {triage.get('info_only','no')}")
    content.append(f"- Action Required: {triage.get('action_required','yes')}")
    content.append(f"- Response Required: {triage.get('response_required','maybe')}")
    content.append(f"- Priority: {triage.get('priority','med')}")
    content.append(f"- Due: {triage.get('due','this_week')}")
    content.append(f"- Summary: {triage.get('summary','')}")
    content.append("")

    content.append("## My Actions")
    my_actions = triage.get("my_actions", []) or [""]
    for a in my_actions:
        content.append(f"- {a}")
    content.append("")

    content.append("## Others' Actions")
    other_actions = triage.get("other_actions", []) or []
    if not other_actions:
        content.append("- ")
    else:
        for oa in other_actions:
            owner = oa.get("owner","")
            action = oa.get("action","")
            content.append(f"- {owner}: {action}")
    content.append("")

    content.append("## Missing Info")
    for m in (missing or [""]):
        content.append(f"- {m}")
    content.append("")

    if agent_notes:
        content.append("## Agent Insights")
        content.append(agent_notes)
        content.append("")

    content.append("## Draft Response")
    content.append(draft if draft else "-")
    content.append("")

    if obsidian_hits:
        content.append("## Obsidian Context (hits)")
        content.append(obsidian_hits)
        content.append("")

    content.append("## Full Email")
    content.append(body if body else "(no body)")
    content.append("")

    with open(path,"w",encoding="utf-8") as f:
        f.write("\n".join(content))

    master_rel = os.path.relpath(path, '/mnt/obsidian')

    # Secondary notes (only if confidence is high/med; otherwise ask)
    conf = confidence_score(subject, body, attachments)
    secondary = detect_secondary(subject, body, attachments) if conf in ["high","med"] else []

    # Action items note + register
    if (triage.get("my_actions") or triage.get("other_actions")):
        os.makedirs(ACTION_DIR, exist_ok=True)
        apath = os.path.join(ACTION_DIR, f"{ts}__{safe}_actions.md")
        with open(apath, "w", encoding="utf-8") as f:
            f.write(f"# Action Items: {subject}\n\n")
            f.write(f"- Master note: [[{master_rel}]]\n")
            f.write(f"\n{action_due_tag(triage.get('due','this_week'))}\n\n")
            f.write("## My Actions\n")
            for a in (triage.get("my_actions") or [""]):
                f.write(f"- {a}\n")
            f.write("\n## Others' Actions\n")
            if triage.get("other_actions"):
                for oa in triage.get("other_actions"):
                    f.write(f"- {oa.get('owner','')}: {oa.get('action','')}\n")
            else:
                f.write("- \n")
        append_backlink(path, apath, "Action Items")
        append_action_register(subject, triage, master_rel)

    # Training / API notes
    if "training" in secondary:
        os.makedirs(PRODUCT_TRAINING_DIR, exist_ok=True)
        tpath = os.path.join(PRODUCT_TRAINING_DIR, f"{ts}__{safe}_training.md")
        with open(tpath, "w", encoding="utf-8") as f:
            f.write(f"# Training: {subject}\n")
            f.write("\n## Metadata\n")
            f.write(f"- Source: Email\n- Date: {date}\n- Attachments: {', '.join(attachments) if attachments else 'None'}\n")
            f.write(f"\n- Master note: [[{master_rel}]]\n")
            f.write("\n## Summary\n- \n")
        append_backlink(path, tpath, "Training")
    if "api" in secondary:
        os.makedirs(PRODUCT_API_DIR, exist_ok=True)
        apipath = os.path.join(PRODUCT_API_DIR, f"{ts}__{safe}_api.md")
        with open(apipath, "w", encoding="utf-8") as f:
            f.write(f"# API Knowledge: {subject}\n\n")
            f.write(f"- Master note: [[{master_rel}]]\n")
            f.write("\n## Summary\n- \n")
        append_backlink(path, apipath, "API Knowledge")

    # Personal transcript notes
    if "personal_transcript" in secondary and ("duane.leitch@gmail.com" in (sender+body).lower()):
        os.makedirs(PERSONAL_TRANSCRIPTS_DIR, exist_ok=True)
        tpath = os.path.join(PERSONAL_TRANSCRIPTS_DIR, f"{ts}__{safe}_transcript.md")
        with open(tpath, "w", encoding="utf-8") as f:
            f.write(f"# Transcript: {subject}\n")
            f.write("\n## Metadata\n")
            f.write(f"- Source: Email\n- Date: {date}\n- Attachments: {', '.join(attachments) if attachments else 'None'}\n")
            f.write(f"\n- Master note: [[{master_rel}]]\n")
            f.write("\n## Summary\n- \n")
        append_backlink(path, tpath, "Transcript")
        update_transcript_index(os.path.relpath(tpath, '/mnt/obsidian'))

    # Follow-up reminder note for response required
    if triage.get("response_required","maybe") in ["yes","maybe"]:
        os.makedirs(ACTION_DIR, exist_ok=True)
        rpath = os.path.join(ACTION_DIR, f"{ts}__{safe}_response.md")
        with open(rpath, "w", encoding="utf-8") as f:
            f.write(f"# Response Reminder: {subject}\n\n")
            f.write(f"- Master note: [[{master_rel}]]\n")
            f.write(f"- Due: {triage.get('due','this_week')}\n")
            f.write(f"\n{action_due_tag(triage.get('due','this_week'))}\n")
        append_backlink(path, rpath, "Response Reminder")

    # Draft creation
    if triage.get("response_required","maybe") in ["yes","maybe"] and draft and not (date and date.startswith('Sun,') and date[8:12]<'2025'):
        tag = "info needed" if missing else "next steps"
        subj = subject if subject.lower().startswith("re:") else f"Re: {subject}"
        subj = f"{subj} — {tag}"
        run([
            GOG_BIN,"gmail","draft","create",
            "--account",ACCOUNT,
            "--to", sender,
            "--subject", subj,
            "--body", draft,
            "--reply-to-message-id", msg_id
        ])

    # Label thread as processed
    run([GOG_BIN,"gmail","labels","modify","--account",ACCOUNT,"--add",LABEL, thread_id])

    # Summary message to Duane (simple high-level)
    summary_msg = textwrap.dedent(f"""
    Email triaged: {subject}
    From: {sender}
    Summary: {triage.get('summary','')}
    Action required: {triage.get('action_required','yes')} | Response required: {triage.get('response_required','maybe')} | Priority: {triage.get('priority','med')} | Due: {triage.get('due','this_week')}
    My actions: {', '.join(triage.get('my_actions', [])) or 'None'}
    Others' actions: {', '.join([f"{oa.get('owner','')}: {oa.get('action','')}" for oa in triage.get('other_actions', [])]) or 'None'}
    Master note: {master_rel}
    """).strip()
    run([OPENCLAW_BIN,"message","send","--channel","telegram","--target","7764426016","--message",summary_msg])

