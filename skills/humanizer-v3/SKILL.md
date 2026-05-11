---
name: humanizer-v3
description: Refine writing so it sounds natural, specific, and human without changing the author's meaning. Use when the user asks to humanize writing, remove AI-sounding phrasing, smooth tone, improve rhythm or clarity, preserve voice while rewriting, compare rewrite options, or analyze why a draft feels synthetic across emails, memos, reports, docs, posts, and other prose.
---

# Humanizer v3

Refine text so it reads like a capable person wrote it, not a template engine.
Preserve facts, intent, register, and constraints. Improve only what actually needs help.

## Default posture

Default to a conservative rewrite.
Make the smallest edit that removes stiffness, filler, hype, or mechanical rhythm.
If a stronger rewrite would materially shift tone, emphasis, or meaning, either label it as a stronger option or ask first.

## Workflow

1. Identify the task type:
   - rewrite
   - analysis only
   - compare options
   - voice match
2. Infer the text's risk level:
   - high risk: legal, financial, medical, policy, compliance, technical, contract, executive messaging with sensitive claims
   - normal risk: most business writing, emails, memos, updates, decks, summaries
   - low risk: marketing drafts, bios, speeches, personal writing, creative copy
3. Infer the target voice from the source unless the user specifies one.
4. Detect the biggest synthetic signals.
5. Revise at the lowest strength that solves the problem.
6. Check factual fidelity before returning.

## Rewrite strengths

### 1. Tighten
Use for already-human drafts that mainly need cleanup.
Actions:
- cut filler
- simplify padded phrasing
- fix clunky transitions
- preserve structure

### 2. Naturalize
Use as the default for most business writing.
Actions:
- vary rhythm lightly
- replace inflated or generic wording
- reduce template-like phrasing
- preserve register and structure unless structure is part of the problem

### 3. Humanize
Use when the user explicitly wants stronger rewriting.
Actions:
- allow bigger sentence rewrites
- improve flow and emphasis
- keep facts and intent fixed
- do not invent personality, evidence, or specificity

### 4. Voice-match
Use when the user wants the text to sound more like a known audience, role, or prior sample.
Actions:
- mirror sentence length, directness, warmth, and level of formality
- stay within one notch of the provided voice
- if no sample exists, infer voice cautiously from the source

## Hard rules

- Do not add facts, examples, sources, names, dates, or numbers.
- Do not make a claim more certain than the source supports.
- Do not remove qualifiers that carry meaning.
- Do not turn precise technical wording into vague plain English.
- Do not force casual tone onto professional writing.
- Do not flatten distinctive human voice in the name of cleanup.
- Honor explicit style constraints, including forbidden punctuation or formatting choices.

## What to scan for

Read `references/pattern-signals.md` when you need a fuller pattern library.
Focus on the signals that most affect this draft, not every possible issue.

Common signals:
- inflated claims without substance
- generic praise or hype words
- repetitive sentence cadence
- stock transitions and throat-clearing
- consultant-sounding abstractions
- chatbot closers and sycophantic framing
- list-heavy rhythm with little emphasis hierarchy
- obvious synonym cycling around the same noun or idea

## Risk handling

### High risk text
Return:
1. conservative rewrite
2. optional stronger version only for lines where style can move safely
3. brief note on what precision was protected

### Normal risk text
Return:
1. revised text
2. 2 to 5 bullets on what changed

### Analysis-only requests
Return:
- top synthetic signals
- tone and voice assessment
- risk notes
- recommended rewrite strength

## Ask when needed

Ask one concise question if any of these are missing and materially change the result:
- target audience
- intended tone
- whether brevity or warmth matters more
- whether the user wants cleanup or a stronger rewrite

Otherwise, proceed with the best conservative assumption.

## Quality bar

Before returning, verify:
- meaning stayed intact
- no new facts appeared
- rhythm improved
- the draft sounds less templated
- the result still sounds plausible for the original writer

## Output patterns

Read `references/output-recipes.md` when you need examples for:
- standard rewrite output
- high-risk output
- option sets
- voice-match handling
