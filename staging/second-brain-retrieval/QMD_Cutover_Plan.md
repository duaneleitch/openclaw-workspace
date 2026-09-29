# QMD Cutover Plan

## Current State

- Seven collections are stale, ranging from 162 to 209 days since update.
- `workspace-memory` is nested inside `workspace-root`, causing overlap.
- `diversys-email` and `diversys-email-2` represent duplicated email locations.
- No collection context is configured.
- Default QMD retrieval must not include the `Obsidian/` mirror or archives.

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

## Cutover Sequence

1. Export and document the current collection configuration.
2. Add human-written collection context for each target collection.
3. Create the target collections without deleting legacy collections.
4. Run representative retrieval tests for actions, Diversys product knowledge, a source transcript, and a shared governance rule.
5. Compare quality, duplication, and canonical-note ranking.
6. Retire overlapping legacy collections only after tests pass and a rollback record exists.
7. Establish a controlled refresh cadence appropriate for the two-core VPS.

## Guardrail

No global reindex or collection removal occurs until the duplicate mirror path map and email-location decision are complete.
