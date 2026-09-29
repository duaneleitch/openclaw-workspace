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

