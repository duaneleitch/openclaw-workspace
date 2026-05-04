# Task selection decision tree

Use this to decide whether Main should answer directly, use the quick call, or use the default worker call.

## Step 1: Can Main answer directly?

Answer directly if the task is:
- simple
- fully self-contained
- low risk
- not dependent on a document or external source
- not likely to benefit from delegation

## Step 2: If delegating, is it simple and low risk?

Use the quick call if the task is:
- narrow
- routine
- easy to validate
- likely to produce a short output
- low risk if slightly imperfect

Examples:
- simple extraction
- basic classification
- short summary

## Step 3: Otherwise use the default worker call

Use the default worker call when the task is:
- moderately complex
- document-based
- multi-part
- evidence-sensitive
- likely to need richer structure
- more important than a trivial helper task

## Step 4: Escalate beyond the worker if needed

Use a stronger model or tighter review when the task is:
- customer-facing
- strategic
- ambiguous
- high stakes
- legally, financially, or operationally sensitive
- likely to fail without stronger reasoning

## Default rule

When unsure, prefer the default worker call over the quick call.
The quick call is only for clearly simple and low-risk tasks.
