# Second Brain Migration Log

## 2026-09-28: Preservation Baseline and Additive Foundation

### Preservation

- Source vault Markdown count: 1,692.
- Recovery snapshot: `/Volumes/AI-Storage/Obsidian_Backups/Second_Brain_2026-09-28/markdown`.
- Source manifest: `/Volumes/AI-Storage/Obsidian_Backups/Second_Brain_2026-09-28/markdown-manifest.tsv`.
- Snapshot hashes verified against the source manifest.

### Added, no existing Markdown moved or deleted

- `AGENTS.md`
- `00_System/Context_Rules.md`
- `00_System/Router.md`
- `00_System/Source_Governance.md`
- `00_System/Digest_Runbook.md`
- New additive layer folders: `00_Inbox`, `30_Operations`, `40_Agent_Workspaces`, `50_Governance`, `60_Retrieval`, and `90_Archive`.

### Pilot

- Created one reviewed knowledge note from the ingested second-brain video.
- No legacy content was moved, reclassified, or indexed differently.

## 2026-09-28: Isolated QMD Pilot and Mirror Path Map

### Retrieval validation
- Created isolated QMD index: `secondbrain-pilot`.
- Indexed 4 governance, 2 knowledge-wiki, 0 operations, and 1 raw transcript document; 19 chunks embedded.
- Verified BM25 retrieval for canonical knowledge and raw transcripts.
- Governance collection is indexed and retrievable; hybrid `query` triggers a large reranking model download on this CPU-only VPS, so use `search` (BM25) until that dependency is resolved.
- No live QMD collections were changed.

### Mirror resolution
- `Obsidian/` mirror classification completed: 368 hash-identical duplicates, 24 unique records.
- A source-to-destination path map for the 24 unique records is captured in `Mirror_Classification_2026-09-28`.
- Existing records remain untouched pending explicit approval for the migration batch.

### Next step
- After approval, move the 24 unique records into the mapped canonical destinations with full hash and link verification.
- Once moved, re-index the pilot QMD collection to confirm the canonical notes surface before raw evidence.

## 2026-09-28: Mirror Stub Policy Decision

### Finding
- `Obsidian/` mirror unique records are 24 files.
- Every mirror file is much smaller than its canonical destination and does not hash-match the destination.
- Therefore, the mirror files are historical stubs or partial duplicates, not better canonical sources.

### Policy outcome
- Keep all 24 mirror files in place under `Obsidian/` for provenance and forensic reference.
- Do not move these 24 files into canonical destinations.
- Do not overwrite existing canonical destinations.
- Exclude mirror files from default retrieval.
- Use canonical destination files as the active knowledge sources.

### Next step
- Publish the migration-batch plan for review and enable only safe automation once reviewed.

## 2026-09-28: Canonical QMD Cutover and Controlled Automation

### QMD cutover completed

- Retired the seven overlapping legacy collections from the active QMD index.
- Established nine canonical collections: `agent-memory`, `diversys-current`, `general-methods`, `governance`, `knowledge-wiki`, `raw-evidence`, `diversys-email-current`, `actions-current`, and `operations-current`.
- Added scoped collection context to every canonical collection.
- Restricted `actions-current` to the two live action-register notes, excluding historical action archives.
- Confirmed BM25 retrieval for the controlled digest and live action register.
- The `Obsidian/` mirror and `90_Archive/` remain excluded from default retrieval.

### Controlled automation completed

- Created `scripts/second_brain_digest.py`, a deterministic, evidence-first digest generator.
- Generated and indexed the first digest: `30_Operations/Digests/2026-09-28_Second_Brain_Digest.md`.
- Enabled a 3:05 AM Toronto file-only digest job and a 7:05 AM Toronto morning-brief job for `#alfred-main`.
- The automation does not move or edit sources, generate action items, or write semantic wiki notes.

### Deferred by design

- Semantic embedding remains deferred. On this two-core CPU VPS, QMD `query` invokes large model downloads and can trigger a Node/SQLite shutdown assertion. BM25 retrieval is the supported default until the QMD runtime issue is resolved.
