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
REVIEW_QUEUE = VAULT / "00_Inbox" / "Review_Queue"
AUTO_PUBLICATION = VAULT / "30_Operations" / "Auto_Publication"


def frontmatter_value(text: str, key: str) -> str | None:
    match = re.search(rf"(?m)^{re.escape(key)}:\s*(.+?)\s*$", text)
    return match.group(1).strip().strip('"') if match else None


def title_for(text: str, fallback: str) -> str:
    match = re.search(r"(?m)^#\s+(.+?)\s*$", text)
    return match.group(1).strip() if match else fallback


def related_raw_paths(text: str) -> list[str]:
    return re.findall(r"\[\[(10_Raw/[^\]|]+)", text)


def existing_review_for(source: Path) -> Path | None:
    """Return an existing review packet for this source, if one is present."""
    if not REVIEW_QUEUE.exists():
        return None
    for review in REVIEW_QUEUE.glob("*.md"):
        if source.stem in review.read_text(encoding="utf-8"):
            return review
    return None


def create_review_packet(day: str, source: Path) -> tuple[Path, bool]:
    """Create a review-only packet without modifying source or canonical notes."""
    existing = existing_review_for(source)
    if existing:
        return existing, False
    text = source.read_text(encoding="utf-8")
    title = title_for(text, source.stem)
    raw_paths = related_raw_paths(text)
    destination = REVIEW_QUEUE / f"{source.stem}_Compilation_Review.md"
    raw_block = "\n".join(f"- [[{path}]]" for path in raw_paths) or "- No linked raw evidence found; investigate before publication."
    packet = "\n".join([
        "---",
        "type: knowledge_compilation_review",
        "status: review_required",
        f"created: {day}",
        "generated_by: controlled_second_brain_digest",
        f'source_note: "[[{source.stem}]]"',
        "actions_requested: false",
        "---",
        "",
        f"# Compilation Review: {title}",
        "",
        "## Source and provenance",
        "",
        f"- Source note: [[{source.relative_to(VAULT).as_posix()}]]",
        f"- Capture date: {frontmatter_value(text, 'captured') or 'not recorded'}",
        f"- Source type: {frontmatter_value(text, 'source_type') or 'not recorded'}",
        "- Raw evidence:",
        raw_block,
        "",
        "## Review required",
        "",
        "- Check whether existing canonical knowledge already covers the source.",
        "- Identify only claims traceable to the source that merit a refinement or new note.",
        "- Do not publish a canonical note, create action items, edit sources, move files, or delete files.",
        "",
        "## Reviewer decision",
        "",
        "- [ ] Accept no-change recommendation",
        "- [ ] Approve a targeted canonical refinement",
        "- [ ] Request additional analysis",
        "",
    ])
    REVIEW_QUEUE.mkdir(parents=True, exist_ok=True)
    destination.write_text(packet, encoding="utf-8")
    return destination, True


def create_review_packets(day: str, records: list[tuple[str, str, str, list[str]]]) -> int:
    created = 0
    for _, _, source_path, _ in records:
        _, was_created = create_review_packet(day, VAULT / source_path)
        created += int(was_created)
    return created


def auto_publication_summary(day: str) -> tuple[int, int, int]:
    """Return auto-published, review-required, and no-change counts from the audit log."""
    log = AUTO_PUBLICATION / f"{day}_Auto_Publication_Log.md"
    if not log.exists():
        return 0, 0, 0
    text = log.read_text(encoding="utf-8")
    return (
        text.count("Decision: auto_published"),
        text.count("Decision: review_required"),
        text.count("Decision: no_change_existing_coverage"),
    )


def write_auto_publication_candidates(day: str, records: list[tuple[str, str, str, list[str]]]) -> Path:
    """Write the deterministic candidate set for the post-digest compiler."""
    AUTO_PUBLICATION.mkdir(parents=True, exist_ok=True)
    destination = AUTO_PUBLICATION / f"{day}_Candidates.md"
    lines = [
        "---",
        "type: auto_publication_candidates",
        f"date: {day}",
        "generated_by: controlled_second_brain_digest",
        "---",
        "",
        f"# Auto-Publication Candidates | {day}",
        "",
        "Only the source paths listed below may be evaluated by the post-digest compiler.",
        "",
    ]
    if not records:
        lines.append("No candidates.")
    else:
        for title, status, source_path, raw_paths in records:
            lines.extend([
                f"- Source: {source_path}",
                f"  - Title: {title}",
                f"  - Status: {status}",
                "  - Raw evidence: " + ", ".join(raw_paths) if raw_paths else "  - Raw evidence: none",
            ])
    destination.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return destination


def build_digest(day: str) -> tuple[str, list[tuple[str, str, str, list[str]]]]:
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
        "- The digest itself does not create action items, modify sources, move files, or delete files.",
        "- Eligible sources may be handled by the separate governed auto-publication job; all others remain review-only.",
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
        "- BM25 is the fast default. Semantic retrieval is available when needed; its first CPU-only query may initialize more slowly.", "",
    ])
    return "\n".join(lines), records


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
    digest, records = build_digest(args.date)
    count = len(records)
    destination = DIGESTS / f"{args.date}_Second_Brain_Digest.md"
    if args.brief:
        if destination.exists():
            auto_published, review_required, no_change = auto_publication_summary(args.date)
            print(
                f"🦾 Second-brain morning brief: {count} reviewed source(s) captured on {args.date}. "
                f"Auto-publication: {auto_published} published, {review_required} routed to review, "
                f"{no_change} covered already. Digest: {destination}. "
                "No actions, source edits, moves, or deletions were automated by the digest."
            )
            return 0
        print(f"🦾 Second-brain morning brief: no digest was created for {args.date}.")
        return 0
    if not args.write:
        print(digest)
        print(f"\nPreview only: {count} reviewed source note(s); destination {destination}", file=sys.stderr)
        return 0
    DIGESTS.mkdir(parents=True, exist_ok=True)
    write_auto_publication_candidates(args.date, records)
    if destination.exists() and not args.overwrite:
        existing = destination.read_text(encoding="utf-8")
        created_reviews = create_review_packets(args.date, records)
        if existing == digest:
            print(f"Digest already current: {destination} ({count} reviewed source note(s), {created_reviews} new review packet(s))")
            return 0
        print(
            f"Digest preserved: {destination} ({count} reviewed source note(s), {created_reviews} new review packet(s)); "
            "current generator output differs but overwrite was not requested."
        )
        return 0
    temporary = destination.with_suffix(".md.tmp")
    temporary.write_text(digest, encoding="utf-8")
    temporary.replace(destination)
    created_reviews = create_review_packets(args.date, records)
    print(f"Wrote {destination} ({count} reviewed source note(s), {created_reviews} new review packet(s))")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
