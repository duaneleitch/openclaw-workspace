#!/usr/bin/env python3
import json, os, re, subprocess, time, textwrap, shlex

ACCOUNT = "alfred.opclaw@gmail.com"
LABEL = "OpenClaw-Processed"
DEFAULT_DIR = "/mnt/obsidian/06_Google Email"
DIVERSYS_DIR = "/mnt/obsidian/07_Diversys_Email"
CLIENT_FOLDERS = {
    "abcrc": "/mnt/obsidian/05_Diversys/Clients/ABCRC/ABCRC_Email",
    "encorp": "/mnt/obsidian/05_Diversys/Clients/ENCORP/ENCORP_Email",
    "calrecycle": "/mnt/obsidian/05_Diversys/Clients/CalRecycle/CalRecycle_Email",
    "tarkett": "/mnt/obsidian/05_Diversys/Clients/Tarkett/Tarkett_Email",
    "ekocircles": "/mnt/obsidian/05_Diversys/Clients/EkoCircles/EkoCircles_Email",
    "aramco": "/mnt/obsidian/05_Diversys/Clients/Aramco/Aramco_Email",
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


def run(cmd, input_text=None):
    return subprocess.check_output(cmd, text=True, input=input_text)

# Ensure label exists
try:
    run([GOG_BIN,"gmail","labels","create","--account",ACCOUNT, LABEL])
except Exception:
    pass


def select_folder(sender, body):
    combo = (sender + "\n" + body).lower()
    for key, path in CLIENT_FOLDERS.items():
        if key in combo:
            return path
    if "@diversys.com" in combo:
        return DIVERSYS_DIR
    return DEFAULT_DIR


def is_support(subject, body):
    combo = (subject + "\n" + body).lower()
    return any(k in combo for k in SUPPORT_KEYWORDS)


def ai_triage(subject, sender, date, body):
    prompt = textwrap.dedent(f"""
    You are triaging an inbound email for a busy executive.
    Return ONLY valid JSON with these keys:
    response_required (yes/no/maybe),
    intent_type (info/action/response),
    summary (2-3 sentences),
    action_items (array of strings),
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


def obsidian_search_snippets(query):
    try:
        cmd = ["bash","-lc", f"grep -RIn --max-count=5 --include='*.md' {shlex.quote(query)} /mnt/obsidian 2>/dev/null || true"]
        out = run(cmd)
        return out.strip()
    except Exception:
        return ""


def ai_draft(subject, sender, date, body, triage, missing_info, obsidian_hits):
    prompt = textwrap.dedent(f"""
    Draft a concise, professional, human-sounding reply.
    If missing_info is non-empty, the response must ask for those details first
    and should NOT claim investigation has started.
    Use only dashes (-) for lists. Do not use asterisks.

    Triage:
    {json.dumps(triage, ensure_ascii=False)}

    Missing info:
    {json.dumps(missing_info, ensure_ascii=False)}

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

    triage = ai_triage(subject, sender, date, body) or {
        "response_required":"maybe",
        "intent_type":"response",
        "summary":"",
        "action_items":[],
        "missing_info":[]
    }

    # ensure missing info list for support cases
    missing = triage.get("missing_info", []) or []
    if is_support(subject, body) and not missing:
        missing = SUPPORT_INFO_PROMPTS

    keywords = " ".join(subject.split()[:3])
    obsidian_hits = obsidian_search_snippets(keywords) if keywords else ""

    draft = ""
    if triage.get("response_required","maybe") in ["yes","maybe"]:
        draft = ai_draft(subject, sender, date, body, triage, missing, obsidian_hits)

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
    content.append(f"- Response Required: {triage.get('response_required','maybe')}")
    content.append(f"- Intent: {triage.get('intent_type','response')}")
    content.append(f"- Summary: {triage.get('summary','')}")
    content.append("")

    content.append("## Action Items")
    actions = triage.get("action_items", []) or [""]
    for a in actions:
        content.append(f"- {a}")
    content.append("")

    content.append("## Missing Info")
    for m in (missing or [""]):
        content.append(f"- {m}")
    content.append("")

    if is_support(subject, body):
        content.append("## Info Needed for Dev Team")
        for q in SUPPORT_INFO_PROMPTS:
            content.append(f"- {q}")
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

    if triage.get("response_required","maybe") in ["yes","maybe"] and draft:
        subj = subject if subject.lower().startswith("re:") else f"Re: {subject}"
        run([
            GOG_BIN,"gmail","draft","create",
            "--account",ACCOUNT,
            "--to", sender,
            "--subject", subj,
            "--body", draft,
            "--reply-to-message-id", msg_id
        ])

    run([GOG_BIN,"gmail","labels","modify","--account",ACCOUNT,"--add",LABEL, thread_id])
