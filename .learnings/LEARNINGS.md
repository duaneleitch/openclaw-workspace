# Learnings

---

## [LEARN-20260426-humanizer-email-enforcement]

**Logged**: 2026-04-26T19:42:53.875399+00:00
**Category**: correction
**Priority**: high

### Learning
For generated email responses, a generic second-pass rewrite is not enough to count as Humanizer application. The workflow must enforce the user's style constraints explicitly, including a hard ban on em dashes, and record that the response was humanized in note metadata.

### Trigger
User reported that the last generated email still contained em dashes, proving the Humanizer requirement was not being applied adequately.

### Action
Strengthen the response-generation prompt to explicitly forbid em dashes and add visible `Humanized: yes` metadata to response notes.

---

## [LRN-20260428-001] correction

**Logged**: 2026-04-28T11:24:00Z
**Priority**: high
**Status**: pending
**Area**: docs

### Summary
For contact-add requests, default to Duane's Obsidian contacts list in General Info when the request is framed as personal contact management.

### Details
I initially interpreted "add to my contacts" as an external contacts system and asked for confirmation for an external write. Duane clarified that there is an existing contacts list in Obsidian under General Info and that this is where contacts are supposed to be added.

### Suggested Action
Use /mnt/obsidian/02_General_Info/Contacts as the default destination for personal contact additions unless Duane explicitly asks for Google Contacts or another external address book.

### Metadata
- Source: user_feedback
- Related Files: /mnt/obsidian/02_General_Info/Contacts
- Tags: contacts, obsidian, correction

---
## [LRN-20260503-001] correction

**Logged**: 2026-05-03T01:34:26.004397+00:00
**Priority**: high
**Status**: pending
**Area**: config

### Summary
Do not add per-model contextWindow/maxTokens overrides under agents.defaults.models or a models block under the heartbeat-llama agent in OpenClaw 2026.4.15.

### Details
I attempted to fix local Ollama cron execution by inserting contextWindow/maxTokens keys under agents.defaults.models for ollama/llama3.2:3b and by adding a models block to the heartbeat-llama agent entry. Duane had to manually repair ~/.openclaw/openclaw.json with ChatGPT's help because those locations are not accepted by this OpenClaw version and broke behavior.

### Suggested Action
When adjusting model sizing for OpenClaw 2026.4.15, inspect the current JSON schema first and only edit supported provider/agent fields. Validate JSON structure after every change and avoid guessing unsupported nested keys.

### Metadata
- Source: user_feedback
- Related Files: /home/duane/.openclaw/openclaw.json
- Tags: openclaw, config, ollama, cron

---

## [LRN-20260716-001] correction

**Logged**: 2026-07-16T11:52:00Z
**Priority**: high
**Status**: pending
**Area**: docs

### Summary
When Duane shares transcripts, full processing must always happen, not just memory capture.

### Details
I only partially processed a transcript by extracting durable notes into daily memory. Duane corrected that transcript handling must always include the full processing workflow.

### Suggested Action
For every transcript batch, always complete the full workflow: read, summarize, extract actions/risks/decisions, save processed notes to the appropriate Obsidian location, and only then report completion.

### Metadata
- Source: user_feedback
- Related Files: /home/duane/.openclaw/workspace/AGENTS.md, /home/duane/.openclaw/workspace/MEMORY.md
- Tags: transcripts, processing, obsidian, correction

---

## [LRN-20260816-001] correction

**Logged**: 2026-08-16T23:16:22.294288+00:00
**Priority**: high
**Status**: pending
**Area**: docs

### Summary
Do not assume resent image batches are duplicates without checking filenames against the target Obsidian topic folder.

### Details
I incorrectly labeled at least one resent Social_Media_Insights batch as a duplicate. A later filename check showed the files were missing from the library and needed to be processed. For this workflow, duplicate detection should be based on actual filename/path existence checks before replying, not on conversational proximity or visual similarity assumptions.

### Suggested Action
Before calling any incoming image batch a duplicate, check whether each filename already exists in the target topic Images folder and only then suppress re-processing.

### Metadata
- Source: user_feedback
- Related Files: .learnings/LEARNINGS.md
- Tags: duplicate-detection, image-library, obsidian, correction

---
