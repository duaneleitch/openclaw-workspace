# Errors

---

## [ERR-20260426-001] agentmail-pull-draft-fallback

**Logged**: 2026-04-26T17:37:43.236341+00:00
**Priority**: high
**Status**: pending
**Area**: config

### Summary
Parallel AgentMail pull script failed on live email processing because it assumed the `execpen` agent existed and the exception fallback referenced an undefined variable.

### Error
Unknown agent id "execpen" plus NameError on fallback path in `openclaw-agentmail-pull.py`.

### Context
- Operation: live AgentMail pull test after cutover
- Effect: message listing worked, but processing aborted when draft generation path triggered
- Fix direction: use a known available agent or non-agent fallback, and keep exception fallback self-contained

### Suggested Fix
Replace the unavailable agent dependency with a safer available path and return a static fallback string on exception.

---
# [ERR-20260924-001] claude_code_noninteractive_unknown_model

**Logged**: 2026-09-24T18:09:00Z
**Priority**: medium
**Status**: pending
**Area**: infra

### Summary
Claude Code launched via Ollama Cloud stalled in non-interactive print mode when using `minimax-m3:cloud`.

### Error
```
[claude-code:unrecognized_model] {"model":"minimax-m3:cloud","query_source":"sdk"}
```

### Context
- Command attempted: `ollama launch claude --model minimax-m3:cloud -- -p <read-only review prompt>`
- Interactive Claude Code launch works and `/status` verifies the Ollama endpoint and selected model.
- The non-interactive process produced no report after the unknown-model notice and was stopped without changes.

### Suggested Fix
Test the documented unknown-model compatibility environment setting before using non-interactive Claude Code runs, or use a supported model catalog mapping.

### Metadata
- Reproducible: unknown
- Related Files: .learnings/ERRORS.md

---

