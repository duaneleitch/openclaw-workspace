# Source Governance

## Capture Lifecycle

1. **Inbox:** record the request or unprocessed item.
2. **Raw:** preserve original asset, metadata, and transcript without editorial changes.
3. **Source note:** create a concise, linked record with provenance and processing status.
4. **Knowledge:** publish reusable insights only after review or a governed digest.
5. **Archive:** retain superseded or historical material without deleting it.

## Minimum Provenance

Every externally sourced item should retain:

- origin or source URL
- capture date
- source type
- raw asset or transcript link where available
- processing status
- whether actions were requested

## Protection Rules

- Raw files are append-only at the folder level and immutable at the file level.
- A summary may never replace its source.
- Media ingestion creates no action items by default.
- An agent must not move an existing Markdown file without a migration manifest entry and path map.
