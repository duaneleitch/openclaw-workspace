---
name: main-worker-guardrails
description: Enforce a two-pass orchestration pattern where Main sends bounded tasks to worker sub-agents, validates worker output, and only then returns final results. Use when you want automation with llama-based or other lower-cost worker models, strict prompting, schema-based output, evidence requirements, confidence gating, and automatic escalation or rework before the user sees anything.
---

# Main Worker Guardrails

Use this skill to make Main the single entry point and single decision point for delegated work.

## Operating model

1. Accept one user request.
2. Decide whether Main can answer directly or should delegate.
3. If delegating, send one bounded task to a worker.
4. Require structured output with evidence and confidence.
5. Validate the worker output before responding.
6. Escalate, re-run, or ask for clarification if validation fails.

## Use the bundled references

- Read [references/worker-schema.md](references/worker-schema.md) for the default schema, validation checklist, prompt template, routing policy, and automation flow.
- Read [references/task-library.md](references/task-library.md) for reusable prompt patterns by task type.
- Read [references/escalation-matrix.md](references/escalation-matrix.md) for accept, repair, re-run, escalate, and ask-user rules.
- Read [references/examples.md](references/examples.md) for concrete delegation examples.
- Read [references/default-worker-call.md](references/default-worker-call.md) for the baseline worker call pattern and how to flex it by task.
- Read [references/quick-call.md](references/quick-call.md) for a shortened prompt pattern for simple, low-risk tasks.
- Read [references/decision-tree.md](references/decision-tree.md) for choosing direct answer vs quick call vs default call vs escalation.
- Read [references/operator-summary.md](references/operator-summary.md) for a one-page operating summary.

## Worker task rules

- Give the worker one job only.
- State the source material explicitly.
- Require a fixed schema.
- Require evidence for each substantive claim.
- Require an explicit confidence rating.
- Require missing info and uncertainty to be reported, not guessed.
- Define hard fail conditions up front.

## Main response rule

Do not pass worker output to the user until Main has validated it.
If validation fails, Main owns the remediation step.

## Everyday use

Treat this as the default delegation pattern for routine multi-step work.
Use task-specific prompt patterns from the references when the request matches documents, meetings, email, or analysis.
Keep the guardrails fixed and flex the task details as needed.
Use the decision tree to choose between direct answer, quick call, default call, or stronger-model escalation.
Use the operator summary as the quick mental model.
