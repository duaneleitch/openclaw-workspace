# Humanizer v2 Audit

This document records the weaknesses found in v2 that shaped v3.

## Weaknesses found

### 1. Overloaded SKILL.md
The v2 file is ~300 lines, mixing everything into one file. In practice, that bloats the context window with pattern details, statistical signals, and vocabulary lists that the agent rarely needs all at once.

Fix in v3: Progressive disclosure. SKILL.md stays lean (~140 lines). Pattern library moved to references/pattern-signals.md. Output recipes moved to references/output-recipes.md.

### 2. Binary mode system (Conservative vs Expressive)
Conservative and Expressive are too coarse. A lot of writing falls between them, and users often want something in between without asking explicitly.

Fix in v3: Four graduated strengths: Tighten, Naturalize, Humanize, Voice-match. This gives the agent and user a more precise dial.

### 3. No clear workflow
v2 lists principles but does not give the agent a sequence of decisions. The result is inconsistent application across different tasks.

Fix in v3: Explicit 6-step workflow: identify task type, infer risk level, detect target voice, scan for signals, revise at the right strength, verify fidelity.

### 4. Statistical signals section
Burstiness, vocabulary diversity, trigram repetition — these are interesting but rarely actionable in practice and eat context window space.

Fix in v3: Removed. The agent detects rhythm issues by reading the text, not by counting metrics.

### 5. Vocabulary blacklist (Tier 1 / Tier 2)
A static word list is too brittle. Words like leverage or robust are fine in their natural contexts. A blacklist encourages mechanical replacement without judgment.

Fix in v3: Replaced with pattern-based scanning (inflated claims, generic praise, consultant abstractions). The agent decides per context instead of per word.

### 6. Missing guidance for ambiguous requests
v2 assumes the user always gives clear instructions. In practice, many requests are vague: "make this better" or "fix this."

Fix in v3: Added "Ask when needed" section. One concise question if audience, tone, or rewrite strength is missing and materially changes the result.

### 7. Redundant sections
- What not to do duplicates hard rules
- Tool permissions are not needed in OpenClaw
- Installation notes belong in deployment docs, not the skill
- Examples in the skill file add length without adding value

Fix in v3: Removed all of these. Safety rules are stated once and enforced. Examples live in output-recipes.md if needed.

### 8. No risk-specific output guidance
v2 treats all output the same regardless of text risk level. Legal text needs a different return format than a marketing draft.

Fix in v3: Three risk tiers (high, normal, low) with different output structures. High risk gets conservative rewrite + optional stronger variant + precision note. Normal gets rewrite + change summary. Analysis-only gets diagnosis.

### 9. No voice-matching guidance
v2 lists voice types but does not explain how to match a sample or target role.

Fix in v3: Added Voice-match strength with clear instructions on mirroring cadence, directness, and formality without mimicry.

### 10. Final check too vague
The v2 final check is a set of open questions that are hard to operationalize.

Fix in v3: Quality bar is a 5-item checklist before returning. Each item is a yes/no verification.
