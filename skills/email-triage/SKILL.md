---
name: email-triage
description: Gmail triage workflow for Duane. Classifies inbound mail into info_only, requires_action, requires_response, routes by topic, updates the Action Register, and drafts replies without sending them.
metadata: { "openclaw": { "emoji": "📧" } }
---

# Email triage

Use this skill to process inbound email from the allowed sender list.

## Scope

Only process mail from:

- `duane.leitch@diversys.com`
- `duane.leitch@gmail.com`

## Required outputs

For every qualifying email:

1. Create an email note in the correct inbox folder.
2. Classify it with three independent flags:
   - `info_only`
   - `requires_action`
   - `requires_response`
3. Route the topic note to the most appropriate folder or subfolder.
4. If `requires_action`, create Action Register entries.
5. If `requires_response`, research answers and draft a reply.
6. Never send mail.

## Classification schema

Return JSON with:

- `info_only`: boolean
- `requires_action`: boolean
- `requires_response`: boolean
- `summary`: string
- `topic`: string
- `topic_confidence`: `high` | `medium` | `low`
- `routed_folder`: string or null
- `needs_user_folder_choice`: boolean
- `action_items`: array of objects with `owner`, `action`, `due`, `priority`
- `questions`: array of strings
- `draft_response`: string
- `research_notes`: array of strings
- `missing_info`: array of strings

## Processing rules

### 1. Info only
- Create the email note.
- Route the topic note.
- No Action Register changes.
- No draft.

### 2. Requires action
- Do everything in case 1.
- Add Action Register items.
- Put Duane-owned actions in My Actions.
- Put others’ actions in Others Actions.

### 3. Requires response
- Do everything in case 1.
- Research using available internal and external sources.
- Draft a response.
- Never send.

### 2 and 3
- Do both Action Register updates and draft response.

## Routing

If topic confidence is low, ask Duane where the routed note should live instead of guessing.

## Important

Do not mark Gmail as processed until the Gog keyring/passphrase issue is fixed.
