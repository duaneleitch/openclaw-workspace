#!/usr/bin/env python3
"""Create a reviewable, evidence-first daily second-brain digest.

This is intentionally conservative. It inventories already-reviewed source
notes and raw evidence. It does not change sources, create actions, or move files.
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path

VAULT = Path("/mnt/obsidian")
SOURCES = VAULT / "20_Knowledge" / "Sources"
DIGESTS = VAULT / "30_Operations" / "Digests"


def frontmatter_value(text: str, key: str) -> str | None:
    match = re.search(rf"(?m)^{re.escape(key)}:\s*(.+?)\s*$", text)
    return match.group(1).strip().strip('"') if match else None


def title_for(text: str, fallback: str) -> str:
    match = re.search(r"(?m)^#\s+(.+?)\s*$", text)
    return match.group(1).strip() if match else fallback


def related_raw_paths(text: str) -> list[str]:
    return re.findall(r"\[\[(10_Raw/[^\]|]+)", text)


def build_digest(day: str) -> tuple[str, int]:
    records: list[tuple[str, str, str, list[str]]] = []
    for source in sorted(SOURCES.glob("*.md")):
        text = source.read_text(encoding="utf-8")
        if frontmatter_value(text, "captured") != day:
            continue
        records.append((title_for(text, source.stem), frontmatter_value(text, "status") or "unclassified", source.relative_to(VAULT).as_posix(), related_raw_paths(text)))

    lines = [
        "---", "type: second_brain_digest", f"date: {day}",
        "mode: controlled_inventory", "actions_created: false", "---", "",
        f"# Second Brain Digest | {day}", "", "## Guardrails applied", "",
        "- Source material was not changed, moved, or deleted.",
        "- No action items or semantic wiki notes were created automatically.",
        "- This digest inventories reviewed source notes for human or agent review.",
        "", "## Sources captured", "",
    ]
    if not records:
        lines.append("No reviewed source notes were captured on this date.")
    else:
        for title, status, path, raw_paths in records:
            lines.extend([f"- **{title}**  ", f"  - Source note: [[{path}]]", f"  - Status: `{status}`"])
            lines.append("  - Raw evidence: " + ", ".join(f"[[{p}]]" for p in raw_paths) if raw_paths else "  - Raw evidence: needs review")

    lines.extend([
        "", "## Review queue", "",
        "- Confirm whether any reviewed source should become or update a canonical wiki note.",
        "- Confirm proposed links, decisions, risks, or actions before they are written to shared operational records.",
        "- Investigate any source note whose raw evidence link is missing.",
        "", "## Retrieval status", "",
        "- Canonical QMD collections are the default retrieval boundary.",
        "- The legacy `Obsidian/` mirror and `90_Archive/` remain excluded from default retrieval.",
        "- QMD semantic embedding is deferred on this CPU-only host; BM25 retrieval remains available.", "",
    ])
    return "\n".join(lines), len(records)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", default=dt.date.today().isoformat())
    parser.add_argument("--write", action="store_true", help="write the digest to the vault")
    parser.add_argument("--overwrite", action="store_true", help="replace an existing digest for this date")
    parser.add_argument("--brief", action="store_true", help="print a concise delivery-safe morning brief")
    args = parser.parse_args()
    try:
        dt.date.fromisoformat(args.date)
    except ValueError:
        parser.error("--date must use YYYY-MM-DD")
    digest, count = build_digest(args.date)
    destination = DIGESTS / f"{args.date}_Second_Brain_Digest.md"
    if args.brief:
        if destination.exists():
            print(
                f"🦾 Second-brain morning brief: {count} reviewed source(s) captured on {args.date}. "
                f"Digest: {destination}. No actions, source edits, moves, or deletions were automated."
            )
            return 0
        print(f"🦾 Second-brain morning brief: no digest was created for {args.date}.")
        return 0
    if not args.write:
        print(digest)
        print(f"\nPreview only: {count} reviewed source note(s); destination {destination}", file=sys.stderr)
        return 0
    DIGESTS.mkdir(parents=True, exist_ok=True)
    if destination.exists() and not args.overwrite:
        existing = destination.read_text(encoding="utf-8")
        if existing == digest:
            print(f"Digest already current: {destination} ({count} reviewed source note(s))")
            return 0
        print(f"Refusing to replace a changed existing digest: {destination}", file=sys.stderr)
        return 2
    temporary = destination.with_suffix(".md.tmp")
    temporary.write_text(digest, encoding="utf-8")
    temporary.replace(destination)
    print(f"Wrote {destination} ({count} reviewed source note(s))")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
