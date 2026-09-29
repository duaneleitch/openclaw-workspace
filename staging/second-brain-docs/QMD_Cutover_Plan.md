# QMD Cutover Plan

## Current State

- Canonical cutover completed on 2026-09-28.
- The seven legacy overlapping collections have been retired from the active index.
- Nine scoped canonical collections are active, each with a human-written retrieval context.
- Default QMD retrieval excludes the `Obsidian/` mirror and `90_Archive/`.
- BM25 `qmd search` is the supported retrieval path on this CPU-only VPS.

## Target Non-Overlapping Collections

1. **agent-memory:** OpenClaw daily and curated memory only.
2. **diversys-current:** `00_Alfred/10_Diversys/`.
3. **actions-current:** `05_Action_Items/`.
4. **general-methods:** `02_General_Info/`.
5. **knowledge-wiki:** `20_Knowledge/`.
6. **operations-current:** `30_Operations/`.
7. **raw-evidence:** `10_Raw/`, searched only when source evidence or transcript detail is needed.

## Explicit Exclusions

- `Obsidian/` mirror until duplicate resolution is complete.
- `90_Archive/` unless historical material is explicitly requested.
- `40_Agent_Workspaces/` except when a draft is requested.
- Legacy duplicated email folders until one canonical email location is selected.
- Broad workspace-root indexing, because it subsumes agent memory and produces duplicate results.

## Completed Cutover Sequence

1. Exported and documented the legacy collection configuration.
2. Added human-written collection context for every canonical target collection.
3. Created the canonical collection set and validated representative BM25 retrieval.
4. Restricted action retrieval to the live action register only.
5. Retired legacy overlapping collections from the active index.
6. Added `operations-current` and indexed the first controlled digest.
7. Established a 3:05 AM Toronto digest and 7:05 AM Toronto brief cadence.

## Guardrails

- Do not run global `qmd update`, `qmd query`, or broad `qmd embed` on this VPS until the Node/SQLite shutdown defect is resolved.
- Use `qmd search` for current retrieval validation.
- Preserve the mirror and archive exclusions unless an explicit historical search is required.
- Do not automatically modify source notes, create action items, or generate semantic wiki notes from scheduled automation.
