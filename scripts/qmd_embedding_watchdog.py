#!/usr/bin/env python3
"""Keep the initial QMD embedding queue moving until it reaches zero pending."""

from __future__ import annotations

import re
import subprocess
from pathlib import Path


LOG = Path("/home/duane/.openclaw/workspace/.state/qmd-embedding-worker.log")
LOCK = Path("/home/duane/.cache/qmd/.qmd-embed.lock")


def worker_running() -> bool:
    """Use QMD's PID lock, which also recognizes its detached Node worker."""
    try:
        pid = int(LOCK.read_text(encoding="utf-8").strip())
    except (OSError, ValueError):
        return False
    return Path(f"/proc/{pid}").exists()


def pending_count() -> int | None:
    try:
        result = subprocess.run(["qmd", "status"], capture_output=True, text=True, timeout=8)
    except subprocess.TimeoutExpired:
        return None
    match = re.search(r"Pending:\s+(\d+) need embedding", result.stdout)
    if match:
        return int(match.group(1))
    if re.search(r"Vectors:\s+\d+ embedded", result.stdout):
        return 0
    return None


def main() -> int:
    if worker_running():
        print("QMD embedding worker is active.")
        return 0
    pending = pending_count()
    if pending is None:
        print("QMD queue state unavailable; will retry on the next watchdog run.")
        return 0
    if pending == 0:
        print("QMD embedding queue is complete.")
        return 0
    LOG.parent.mkdir(parents=True, exist_ok=True)
    with LOG.open("ab", buffering=0) as log:
        subprocess.Popen(
            ["nice", "-n", "15", "qmd", "embed", "--timeout", "0", "--max-docs-per-batch", "8", "--max-batch-mb", "4"],
            stdin=subprocess.DEVNULL,
            stdout=log,
            stderr=log,
            start_new_session=True,
        )
    print(f"Restarted QMD embedding worker with {pending:,} pending vectors.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
