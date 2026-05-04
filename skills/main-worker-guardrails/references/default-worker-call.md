# Default worker call

Use this as the baseline call pattern, then adjust it to the task.

```text
Task: <one clear job>
Source: <document, notes, email, or other material>
Allowed scope: <what the worker may and may not do>
Output schema: <paste the agreed schema>
Rules:
- Do not guess.
- Use evidence for substantive claims.
- Mark uncertainty explicitly.
- If the task is incomplete or unclear, return needs_review.
- Follow the schema exactly.
```

## Flexibility rules

Adjust the call when the task demands it:

- For document work, require quotes or line references.
- For meeting notes, require decisions, actions, risks, and open questions.
- For email triage, require classification and reason.
- For analysis tasks, require facts, assumptions, recommendation, and confidence.
- For high-stakes work, tighten the scope and lower the acceptance threshold.
- For simple extraction, keep the call short and the schema minimal.

## Main behavior

Main should keep the same two-pass workflow, but the prompt details should vary by task.
The guardrails stay fixed; the task instructions should flex to the situation.
