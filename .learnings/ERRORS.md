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
