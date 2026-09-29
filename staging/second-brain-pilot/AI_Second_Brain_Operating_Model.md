---
type: knowledge
status: pilot_reviewed
topic: agentic_second_brain
sources:
  - [[2026-09-28_how-to-build-the-ultimate-ai-second-brain-for-hermes-agent]]
---

# AI Second Brain Operating Model

## Purpose

Provide agents with a governed context layer that is faster to retrieve than raw evidence alone, while preserving the ability to verify any material claim against its source.

## Operating Model

1. **Capture:** collect new material with minimal interpretation.
2. **Archive:** retain immutable originals, metadata, captions, and transcripts in `10_Raw`.
3. **Source note:** record provenance, processing status, and links to the raw evidence.
4. **Digest:** extract reviewable insights, relationships, decisions, risks, and candidate actions.
5. **Wiki:** publish concise, reusable knowledge notes in `20_Knowledge` that link back to evidence.
6. **Retrieval:** search canonical knowledge first, then source notes and raw evidence when depth or verification is required.

## Shared-Agent Requirements

- A common router and context rules prevent every agent from searching the entire vault.
- Ownership rules prevent capture workflows, digest workflows, and action workflows from overwriting one another.
- Raw sources remain immutable. Generated summaries never replace the evidence.
- New action items require Duane's explicit request.
- Archives and mirrored content remain out of default retrieval until classified.

## Controlled Automation

The desired future state is a scoped overnight digest followed by a concise Toronto-time morning brief. Automation must begin only after pilot batches meet the quality gates in [[00_System/Digest_Runbook]].

## Evidence

- [[2026-09-28_how-to-build-the-ultimate-ai-second-brain-for-hermes-agent]]
- [[10_Raw/Video/2026-09-28_120551_https-youtu-be-wvyauhfjro0/transcript.txt]]
