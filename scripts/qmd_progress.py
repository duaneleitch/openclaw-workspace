#!/usr/bin/env python3
"""Print a concise, delivery-safe QMD embedding progress update."""

from __future__ import annotations

import re
import subprocess
import sys
import json
from datetime import datetime, timezone
from pathlib import Path


CACHE = Path("/home/duane/.openclaw/workspace/.state/qmd-progress.json")


def cached_message() -> str:
    try:
        cached = json.loads(CACHE.read_text(encoding="utf-8"))
        return (
            f"🦾 QMD embedding update: {cached['done']:,} embedded chunks · "
            f"{cached['pending']:,} source records pending · "
            "worker is actively writing, so this is the last confirmed count."
        )
    except (FileNotFoundError, KeyError, ValueError):
        return "🦾 QMD embedding update: worker is actively writing; the index is temporarily busy."


def main() -> int:
    try:
        result = subprocess.run(["qmd", "status"], text=True, capture_output=True, timeout=8)
    except subprocess.TimeoutExpired:
        print(cached_message())
        return 0
    if result.returncode != 0:
        print("🦾 QMD progress check failed. The embedding worker will be inspected and repaired.")
        return result.returncode
    vectors = re.search(r"Vectors:\s+(\d+) embedded", result.stdout)
    pending = re.search(r"Pending:\s+(\d+) need embedding", result.stdout)
    if vectors and not pending:
        done = int(vectors.group(1))
        CACHE.parent.mkdir(parents=True, exist_ok=True)
        CACHE.write_text(json.dumps({
            "done": done,
            "pending": 0,
            "checked_at": datetime.now(timezone.utc).isoformat(),
        }), encoding="utf-8")
        print(f"🦾 QMD embedding complete: {done:,} embedded chunks · 0 source records pending.")
        return 0
    if not vectors or not pending:
        print("🦾 QMD progress is unavailable. The index format will be inspected.")
        return 2
    done = int(vectors.group(1))
    remaining = int(pending.group(1))
    state = "complete" if remaining == 0 else "running"
    CACHE.parent.mkdir(parents=True, exist_ok=True)
    CACHE.write_text(json.dumps({
        "done": done,
        "pending": remaining,
        "checked_at": datetime.now(timezone.utc).isoformat(),
    }), encoding="utf-8")
    print(f"🦾 QMD embedding update: {done:,} embedded chunks · {remaining:,} source records pending · {state}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
