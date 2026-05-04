# Task-specific prompt library

Use these patterns when Main delegates to a worker.

## Document extraction

```text
Task: Extract the requested fields from this document.
Source: <paste or attach document text>
Output schema: <schema>
Rules:
- Do not infer missing values.
- Quote the exact text that supports each extracted field.
- If the document is unclear, return needs_review.
```

## Meeting notes summary

```text
Task: Summarize the meeting notes into decisions, actions, risks, and open questions.
Source: <paste notes>
Output schema: <schema>
Rules:
- Separate decisions from discussion.
- Identify action items with owners and due dates if present.
- Mark missing or uncertain information explicitly.
```

## Email triage

```text
Task: Classify this email and identify whether it needs action, response, or info-only handling.
Source: <paste email>
Output schema: <schema>
Rules:
- Do not guess intent if the message is ambiguous.
- Quote the sender or text that supports the classification.
- Escalate when the message appears customer-facing, sensitive, or time-bound.
```

## Analysis task

```text
Task: Analyze the material and produce the key findings and recommendation.
Source: <paste material>
Output schema: <schema>
Rules:
- Limit the response to supported findings.
- Distinguish facts, assumptions, and recommendation.
- If evidence is thin, mark the result needs_review.
```
