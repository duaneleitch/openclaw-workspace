# Examples

## Example 1: Document extraction

User request:
- Extract action items from the attached meeting notes.

Main sends:
- One clear task
- The document text
- The default schema
- Rules not to guess and to cite evidence

Worker returns:
- Structured JSON with actions, owners, evidence, confidence, and missing info

Main checks:
- Are all action items supported by the notes?
- Are owners and due dates present where stated?
- Is anything guessed?

## Example 2: Email triage

User request:
- Triage this email and tell me if it needs action.

Main sends:
- The email body
- The default schema
- Rules to classify conservatively when ambiguous

Worker returns:
- Classification, reason, evidence, confidence, and missing info

Main checks:
- Is the sender intent supported?
- Is it action, response, or info-only?
- Does the worker avoid over-claiming?

## Example 3: Summary with risk flags

User request:
- Summarize this customer update and call out risks.

Main sends:
- The source text
- The default schema
- Rules to separate facts, assumptions, and recommendations

Worker returns:
- Summary, findings, risks, confidence, and evidence

Main checks:
- Are risks directly supported?
- Is the output suitable for the intended audience?
- Should it be escalated to a stronger model?
