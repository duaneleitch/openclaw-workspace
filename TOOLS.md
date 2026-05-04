# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

Add whatever helps you do your job. This is your cheat sheet.

## Security Notes
- `openclaw.json` contains live tokens and secrets (Discord, Telegram, gateway, hooks). Never share or commit this file to any public repo or gist.
- **heartbeat-llama / ollama/llama3.2:3b:** If using a small local model (<=300B params) for the heartbeat agent, you MUST set `tools.deny = ["web_search", "web_fetch", "browser"]` on that agent. Small models are vulnerable to prompt injection from untrusted web content. This model should never appear in the global fallback chain — keep it scoped to heartbeat only.

## OpenClaw CLI — Verified Command Syntax

### cron
- List jobs: `openclaw cron list`
- Delete job: `openclaw cron delete <uuid>` (positional, no --id)
- Edit job: `openclaw cron edit <uuid> --cron "expr"` (positional id, use --cron not --schedule)
- Run history: `openclaw cron runs --id <uuid>` (requires --id flag)

### message
- Send to Discord channel: `openclaw message send --channel discord --target channel:<channel-id> --message "text"`
- alfred-main channel id: 1478436599074258954
- alfred-ops channel id: 1478436598453375017

### config
- Read value: `openclaw config get <key>`
- Set scalar: `openclaw config set <key> value`
- Set array: `openclaw config set <key> '["/path1", "/path2"]'`

### gateway
- Restart: `openclaw gateway restart`
- Status: `openclaw gateway status`

### General Rule
When unsure of a subcommand's flags, run `openclaw <command> --help` before providing syntax.

### Channel Logging Rules
- Health & wellness channels (e.g., Discord #health-and-wellness) must never receive internal tooling notices (e.g., `Ran /home...`, cron status, exec logs, or script-trigger messages like `Breakfast health check triggered via /home/...`).
- All operational / internal tooling chatter belongs only in the ops channel (Discord alfred-ops, id: 1478436598453375017), not in #health-and-wellness.
- Health & wellness channels should only see: check-in prompts, your logged inputs, and any brief health feedback you explicitly request.

## openclaw cron edit — Available Options
Key options for `openclaw cron edit <uuid>`:
- `--channel <channel>` — Delivery channel (e.g. discord)
- `--to <dest>` — Delivery destination (Discord channel: `channel:<id>`, user id, Telegram chatId, E.164)
- `--cron <expr>` — Set cron expression
- `--every <duration>` — Set interval (e.g. 10m, 1h)
- `--at <when>` — One-shot time (ISO or duration like 20m)
- `--name <name>` — Rename the job
- `--message <text>` — Set agent turn payload
- `--model <model>` — Model override
- `--session <target>` — Session target (main|isolated)
- `--session-key <key>` — Route to specific session
- `--tz <iana>` — Timezone for cron expressions
- `--enable` / `--disable` — Enable or disable job
- `--timeout-seconds <n>` — Timeout for agent jobs
- `--announce` — Announce summary to chat (subagent-style)
- `--thinking <level>` — Thinking level for agent jobs
- `--light-context` — Lightweight bootstrap context
- `--delete-after-run` — Delete one-shot job after success

## Obsidian Vault Mount (VPS → Mac mini)
- Mount path on VPS: `/mnt/obsidian`
- Source: `duaneleitch@100.70.184.4:/Volumes/AI-Storage/Obsidian` (Mac mini external drive via Tailscale)
- Protocol: **SSHFS** (NFS and SMB failed on macOS Tahoe — NFS exports not registered, SMB forces read-only on external volumes for remote Linux clients)
- SSH key: `/home/duane/.ssh/id_ed25519` (generated on VPS, public key added to Mac mini `~/.ssh/authorized_keys`)
- Systemd unit: `/etc/systemd/system/mnt-obsidian.mount` (enabled, TimeoutSec=120)
- If mount drops after reboot: `fusermount3 -u /mnt/obsidian && sshfs duaneleitch@100.70.184.4:/Volumes/AI-Storage/Obsidian /mnt/obsidian -o uid=1001,gid=1001,reconnect,ServerAliveInterval=30`
- Mac mini must be on and Tailscale connected for mount to work
- Mac mini Tailscale IP: `100.70.184.4`
- Remote Login (SSH) must be enabled on Mac mini: System Settings → General → Sharing → Remote Login: On

## OpenClaw Docs Location
All tool docs: `/home/duane/.npm-global/lib/node_modules/openclaw/docs/tools/`

Key docs available:
- exec.md — shell execution, host/security/ask config
- browser.md — browser automation
- web.md — web search/fetch
- subagents.md — multi-agent orchestration
- skills.md — skill system
- llm-task.md — LLM subtasks
- pdf.md — PDF handling
- apply-patch.md — structured file edits
- loop-detection.md — loop prevention
- agent-send.md — cross-agent messaging

## Exec Tool Config (Applied Fix)
- tools.exec.host = gateway (not sandbox — sandboxing is off by default, sandbox fails closed)
- tools.exec.security = full
- tools.exec.ask = off
- channels.discord.capabilities = ["exec"]
