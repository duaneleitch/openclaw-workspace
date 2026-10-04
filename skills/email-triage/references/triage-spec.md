# Email triage spec

Allowed senders:
- duane.leitch@diversys.com
- duane.leitch@gmail.com

Classification flags:
- info_only
- requires_action
- requires_response

Routing:
- Write the inbox note in the email folder for the sender.
- Create a topic note in the most appropriate folder or subfolder.
- If confidence is low, ask where it should live.

Actions:
- Duane-owned actions go to My Actions.
- Others-owned actions go to Others Actions.
- Update both Action Register files.

Response:
- Research first.
- Draft only.
- Never send.

## Conditional Context Retrieval

Hindsight autoRecall is disabled. Retrieve Hindsight only if prior context could materially change email interpretation: follow-up status, prior promise or disposition, changed date/deadline/owner/scope/commitment, contradiction, unresolved request, or active project/client/person context. Do not retrieve for ordinary extraction, classification, summarization, sender identification, or obvious standalone requests.

When Hindsight points to canonical Obsidian knowledge needed for detail, follow the vault-relative pointer. Do not treat the memory as the canonical document. Active Memory and Codex are excluded from this path.
