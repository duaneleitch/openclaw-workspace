# Worker schema and templates

## Default worker schema

Use this structure for most delegated tasks:

```json
{
  "status": "ok|needs_review|failed",
  "task": "",
  "summary": "",
  "findings": [],
  "evidence": [],
  "assumptions": [],
  "missing_info": [],
  "risks": [],
  "confidence": "high|medium|low",
  "recommendation": ""
}
```

## Validation checklist for Main

Reject or rework the result if any of the following are true:

- a required field is missing
- the schema is malformed
- claims are not supported by evidence
- the worker guessed instead of stating uncertainty
- the output contradicts the source material
- the result is too vague to use
- confidence is too low for the task
- the task is customer-facing, strategic, or otherwise high stakes

## Main prompt template

Use this pattern when delegating:

```text
Task: <one clear job>
Source: <document, notes, or text>
Allowed scope: <what the worker may and may not do>
Output schema: <paste schema>
Rules:
- Do not guess.
- Cite evidence for substantive claims.
- If something is missing or unclear, report it.
- If you cannot complete the task safely, return needs_review.
- Follow the schema exactly.
```

## Routing policy

Use the worker only when the task is narrow and reviewable.

### Good fits for worker models

- extraction
- classification
- summarization
- first-pass analysis
- chunk-level review
- evidence gathering
- draft options

### Escalate to a stronger model when

- the task is ambiguous
- the source is messy or incomplete
- the result will be customer-facing
- the task has policy, legal, financial, or operational risk
- confidence is low or evidence is thin

## Automation flow

1. Main receives the request.
2. Main decides direct answer vs delegation.
3. If delegating, Main sends a bounded task with the schema and rules.
4. Worker returns structured output.
5. Main validates the output.
6. Main either accepts, repairs, re-runs, or escalates.
7. Main gives the user only the final validated result.
