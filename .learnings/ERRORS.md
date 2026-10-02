# Errors

---

## [ERR-20260929-005] main_codex_execution_budget_timeout

**Logged**: 2026-09-29T14:00:00Z
**Priority**: high
**Status**: resolved
**Area**: config

### Summary
The main Discord agent reached the Codex app-server's configured 600-second execution budget while work was still pending response delivery.

### Context
- Gateway evidence recorded `elapsedMs=600001`, `timeoutMs=600000`, and `pendingStage=notification_queue`.
- The default model definition no longer bound `openai/gpt-5.6-terra` to Codex, but `agents.entries.main.models` still had a main-agent override forcing `agentRuntime.id=codex`.

### Resolution
Removed the main-agent Codex runtime override, retained the model alias, and raised the outer default timeout to 900 seconds. Durable work should be scheduler-owned rather than held open in an interactive turn.

### Metadata
- Reproducible: yes
- Related Files: /home/duane/.openclaw/openclaw.json
- See Also: memory/2026-09-24-1838.md

---

## [ERR-20260929-004] cron_edit_empty_message

**Logged**: 2026-09-29T13:47:00Z
**Priority**: low
**Status**: resolved
**Area**: config

### Summary
A cron edit attempted to replace an agent payload with an empty shell-expanded message and was rejected by schema validation.

### Resolution
Use a fully populated literal message when updating agent cron payloads; do not rely on command substitution for long policy prompts.

---

## [ERR-20260929-003] sessions_spawn_main_agent_restricted

**Logged**: 2026-09-29T13:43:00Z
**Priority**: low
**Status**: resolved
**Area**: config

### Summary
The OpenClaw subagent launcher does not permit the `main` agent as a child target.

### Resolution
For bounded delegated work, select an allowed specialist agent and apply the requested worker-model override.

---

## [ERR-20260929-002] sqlite_cli_unavailable_on_vps

**Logged**: 2026-09-29T12:43:00Z
**Priority**: low
**Status**: resolved
**Area**: infra

### Summary
The VPS does not include the `sqlite3` CLI, so direct SQLite inspection is unavailable.

### Resolution
Use QMD status, QMD search, and process telemetry for index-health and queue checks. Install SQLite tooling only if a future maintenance task specifically requires direct database queries.

---

## [ERR-20260929-001] mounted_vault_recursive_filename_scan_timeout

**Logged**: 2026-09-29T03:33:00Z
**Priority**: medium
**Status**: resolved
**Area**: infra

### Summary
Recursive filename scans across the SSHFS-mounted Obsidian vault can exceed the short interactive command lifetime.

### Context
- Operation: locating corroborating CE triage sources.
- Effect: read-only `rg --files` did not return before the process limit and was terminated without changing vault state.

### Resolution
Use the local QMD index for broad discovery, then perform targeted reads of selected source files.

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

# [ERR-20260928-001] gog_sheets_keyring_unavailable

**Logged**: 2026-09-28T14:22:00Z
**Priority**: low
**Status**: pending
**Area**: infra

### Summary
Google Sheets creation could not run non-interactively because the local gog keyring backend requires an unavailable TTY password prompt.

### Error
```
read token: no TTY available for keyring file backend password prompt; set GOG_KEYRING_PASSWORD
```

### Context
- Attempted action: create an editable recruiter outreach spreadsheet in the authorized Google Workspace account.
- No credentials, tokens, or secrets were accessed or exposed.

### Suggested Fix
Configure the gog file-keyring password in the Gateway environment or use an authenticated interactive shell. Until then, generate local spreadsheet artifacts.

### Metadata
- Reproducible: yes
- Related Files: .learnings/ERRORS.md

---

# [ERR-20260928-002] agentmail_configured_inbox_not_found

**Logged**: 2026-09-28T14:27:00Z
**Priority**: low
**Status**: pending
**Area**: infra

### Summary
The configured legacy AgentMail inbox identifier returned HTTP 404 when sending an attachment.

### Error
```
HTTP Error 404: Not Found
```

### Context
- Attempted action: send the recruiter outreach tracker attachment through AgentMail.
- The API key was read locally and never exposed.
- No email was sent because the sender inbox could not be found.

### Suggested Fix
List active AgentMail inboxes and update the sender inbox reference before retrying.

### Metadata
- Reproducible: yes
- Related Files: .learnings/ERRORS.md

---

## [ERR-20260928-003] mounted_vault_broad_search_timeout

**Logged**: 2026-09-28T16:09:00Z
**Priority**: low
**Status**: resolved
**Area**: infra

### Summary
A broad recursive search across the SSHFS-mounted Obsidian vault timed out during second-brain review.

### Suggested Fix
Use known paths, targeted reads, and narrowly scoped searches for mounted-vault analysis. Avoid recursive broad scans during interactive work.

### Metadata
- Reproducible: likely
- Related Files: /mnt/obsidian

---

## [ERR-20260928-004] youtube_cookie_rotated_after_ingest

**Logged**: 2026-09-28T16:15:00Z
**Priority**: medium
**Status**: pending
**Area**: infra

### Summary
The manually exported YouTube cookie authenticated the initial ingest but was rejected as rotated on the next capture request.

### Suggested Fix
Treat exported YouTube cookies as short-lived. Refresh from the dedicated browser profile when yt-dlp reports an authentication or bot-check failure. Preserve original media with `--keep-video` on successful future ingests.

### Metadata
- Reproducible: likely
- Related Files: /home/duane/.openclaw/workspace/scripts/youtube_ingest.py

---

## [ERR-20260928-005] qmd_node_sqlite_shutdown_assertion

**Logged**: 2026-09-28T18:59:00Z
**Priority**: high
**Status**: pending
**Area**: retrieval

### Summary
QMD aborts with a Node `RemoveEnvironmentCleanupHook` assertion in the native `better-sqlite3` binding when invoking status or embedding operations on the VPS.

### Context
- `qmd embed --max-docs-per-batch 8 --max-batch-mb 4` aborted before completing its first batch.
- The index passed SQLite `PRAGMA integrity_check` afterward.
- QMD is installed under Node 24 on a two-core CPU-only VPS.

### Safe Interim Rule
Use validated BM25 retrieval (`qmd search`). Do not retry broad embedding, global update, or hybrid query operations until QMD/Node compatibility is repaired in an isolated test index.

---

## [ERR-20261001-001] youtube_video_ingestion

**Logged**: 2026-10-01T02:31:00Z
**Priority**: medium
**Status**: pending
**Area**: infra

### Summary
The standard YouTube ingestion flow is blocked on this VPS when YouTube rejects yt-dlp and Agent Reach lacks a configured transcription provider.

### Context
- yt-dlp rejected video fAhwYrjmQRk with a bot-confirmation requirement.
- `agent-reach transcribe` reported no Groq or OpenAI provider key.
- The configured Hermes/Elliot fallback is not addressable from this session.

### Suggested Fix
Expose the approved Hermes/Elliot relay to Alfred, or configure an Agent Reach transcription provider through the protected credential workflow.

### Metadata
- Reproducible: yes
- Related Files: /mnt/obsidian/00_Alfred/YouTube_Video_Transcription_How-To.md

---
