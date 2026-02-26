# Restore Guide - OpenClaw Workspace

This document explains how to recover your workspace quickly if something goes wrong.

## What this restores
- Workspace files from GitHub (`openclaw-workspace` repo)
- Agent definitions and templates in the repo
- OpenClaw config file if you committed it in this repo copy

## What this does NOT restore automatically
- OAuth/API credentials stored outside the repo
- Running sessions/transcripts not committed to git
- External service state (Telegram bot settings, etc.)

---

## Scenario A: Fast rollback to last good commit (same VPS)
Use this when a recent change broke behavior.

1) Go to repo
```bash
cd /home/duane/.openclaw/workspace
```

2) Check recent commits
```bash
git log --oneline -n 20
```

3) Choose a known good commit hash (example: `abc1234`) and hard reset
```bash
git reset --hard abc1234
```

4) Restart gateway
```bash
openclaw gateway restart
openclaw gateway status
```

---

## Scenario B: Restore latest from GitHub on the same VPS
Use this if local files drifted and you want the remote state.

1) Go to repo
```bash
cd /home/duane/.openclaw/workspace
```

2) Fetch latest
```bash
git fetch origin
```

3) Reset local branch to remote
```bash
git checkout main
git reset --hard origin/main
```

4) Restart gateway
```bash
openclaw gateway restart
openclaw gateway status
```

---

## Scenario C: Full restore on a new server/VPS
1) Install OpenClaw and Git
2) Clone repo
```bash
git clone https://github.com/duaneleitch/openclaw-workspace.git /home/duane/.openclaw/workspace
```

3) Confirm files
```bash
ls -la /home/duane/.openclaw/workspace
```

4) Reconnect auth (required)
- Re-auth OpenClaw providers (OpenAI/Anthropic/etc.)
- Reconnect channels as needed (Telegram, etc.)

5) Start gateway
```bash
openclaw gateway start
openclaw gateway status
```

---

## Scenario D: Recover a deleted file from Git history
Example for `AGENTS.md`:

```bash
cd /home/duane/.openclaw/workspace
git log -- AGENTS.md
# pick a commit hash, then:
git checkout <commit_hash> -- AGENTS.md
git commit -m "Restore AGENTS.md from history"
git push
```

---

## Safety checklist after any restore
Run these checks:

```bash
openclaw gateway status
openclaw status
git -C /home/duane/.openclaw/workspace status
```

Expected:
- gateway status is healthy
- no invalid config errors
- git status is clean (or only expected local edits)

---

## Suggested backup habit
After meaningful changes:

```bash
cd /home/duane/.openclaw/workspace
git add .
git commit -m "Describe change"
git push
```

If you are unsure, create a checkpoint first:

```bash
git tag checkpoint-$(date +%Y%m%d-%H%M)
git push --tags
```
