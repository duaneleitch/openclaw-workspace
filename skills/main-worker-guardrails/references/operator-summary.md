# Operator summary

## Purpose
Make Main the single entry point for delegated work and keep worker output safe, structured, and useful.

## Default flow
1. Receive the user request.
2. Decide direct answer vs delegation.
3. If delegating, choose quick call or default worker call.
4. Send the worker a bounded task with the right schema and rules.
5. Validate the worker output.
6. Re-run, repair, escalate, or ask for clarification if needed.
7. Return only validated results to the user.

## Default choices
- **Direct answer**: trivial, self-contained, low risk
- **Quick call**: simple, narrow, low-risk delegated work
- **Default worker call**: most normal delegated work
- **Escalate**: ambiguous, messy, customer-facing, strategic, or high-risk work

## Non-negotiables
- Do not let the worker guess.
- Require evidence for substantive claims.
- Require confidence and missing-info reporting.
- Validate before the user sees anything.

## Rule of thumb
Keep the guardrails fixed and flex the task details.
