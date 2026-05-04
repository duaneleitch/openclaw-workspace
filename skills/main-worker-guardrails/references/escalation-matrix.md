# Escalation matrix

## Accept
Use the worker output as-is when:

- schema is complete
- evidence supports the claims
- confidence is high
- the task is narrow and low risk

## Repair
Revise the worker output inside Main when:

- the schema is mostly right but needs cleanup
- one or two fields are missing
- the answer is usable but needs formatting or tightening

## Re-run
Send a tighter prompt back to the worker when:

- the schema is malformed
- evidence is missing
- the worker drifted off scope
- the worker guessed instead of stating uncertainty

## Escalate
Use a stronger model when:

- the source is ambiguous or messy
- the task is customer-facing
- the task is strategic, policy-related, or high risk
- the worker confidence is low
- the output will be used without further human review

## Ask the user
Ask for clarification only when:

- the source material is insufficient
- the objective is genuinely ambiguous
- no safe or accurate completion is possible yet
