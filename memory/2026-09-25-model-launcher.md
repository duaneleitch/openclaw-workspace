# Session: 2026-09-25 — Model launcher and Claude Code defaults

## What happened

Duane asked why `minimax-m3:cloud` was timing out during this session, and why we were
using it instead of `kimi-k3:cloud`. The two questions turned out to share a single
root cause.

## Root cause

This Claude Code session was launched on Sep 24 with:

```
ollama launch claude --model minimax-m3:cloud
```

That `--model` flag causes Claude Code to export the following env vars into its
own process tree (verified live via `env | grep minimax`):

```
CLAUDE_CODE_SUBAGENT_MODEL=minimax-m3:cloud
ANTHROPIC_DEFAULT_SONNET_MODEL=minimax-m3:cloud
ANTHROPIC_DEFAULT_OPUS_MODEL=minimax-m3:cloud
ANTHROPIC_DEFAULT_HAIKU_MODEL=minimax-m3:cloud
```

Every subagent and subprocess spawned from this Claude Code inherits those defaults.
When the `minimax-m3:cloud` endpoint returned slowly or 5xx'd, the result was the
"minimax-m3:cloud is temporarily unavailable (timed out)" errors seen on Bash,
Write, and the auto-mode classifier.

The OpenClaw config (`/home/duane/.openclaw/openclaw.json`) is **not** the source.
It correctly lists `ollama-cloud-custom/kimi-k3:cloud` as primary on every agent
entry. Claude Code's internal model selection and OpenClaw's primary-model ladder
are separate runtime layers.

The env vars are not stored in any file. They are process-scoped to the Claude
Code tree started on Sep 24 (PID 1199471). When that session ends, they go away
with it. They are also visible inside this same Claude Code process, which is how
my earlier `env | grep minimax` returned them.

## How to relaunch Claude Code with the correct default

In a fresh terminal (not inside the running Claude Code session), run one of:

```
# Option 1: Kimi as the Claude Code model (matches OpenClaw primary)
ollama launch claude --model kimi-k3:cloud

# Option 2: Real Anthropic Sonnet, with OpenClaw fallback chain on outage
ollama launch claude --model sonnet

# Option 3: Clear inherited env, then launch Kimi (most explicit)
unset ANTHROPIC_DEFAULT_SONNET_MODEL ANTHROPIC_DEFAULT_OPUS_MODEL ANTHROPIC_DEFAULT_HAIKU_MODEL CLAUDE_CODE_SUBAGENT_MODEL
ollama launch claude --model kimi-k3:cloud
```

Recommended: Option 1 or 3. Option 2 is cleanest but means paying for real
Anthropic calls instead of routing through the Ollama Cloud alias.

## Things that are now also fixed in this session

- Auto mode is now persistently off. `~/.claude/settings.json` contains
  `{"theme": "dark", "disableAutoMode": "disable"}`. The first attempt used
  `permissionMode: "manual"` which Claude Code's settings.json schema rejects;
  the correct key is `disableAutoMode` with value `"disable"`.
- The Codex execution timeout fix from Sep 24 is still in place: the Codex
  runtime binding was removed from `gpt-5.6-terra` and
  `agents.defaults.timeoutSeconds` is at 600s.

## Why this matters

- The `ollama launch claude --model <X>` flag is sticky for the lifetime of
  that Claude Code session. If you want a different default, relaunch.
- The minimax drift was invisible because Claude Code handles its own internal
  model selection separately from OpenClaw's. Check the launch command, not
  OpenClaw config, when subagents or defaults look wrong.
- "Why is X the default" almost always traces back to either the launch flag
  or the explicit `ANTHROPIC_DEFAULT_*_MODEL` env vars. Both are checked first.

## Related

- `2026-09-24-1838.md` — Codex execution timeout fix session
- `2026-09-24-1711.md` — earlier Codex timeout diagnosis (prior session)
- `/home/duane/.openclaw/openclaw.json` — OpenClaw agent model bindings
- `~/.claude/settings.json` — Claude Code user settings (now disables auto mode)
