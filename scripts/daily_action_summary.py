#!/usr/bin/env python3
"""Render Duane's canonical open Action Register into daily messages."""

from __future__ import annotations

import argparse
from pathlib import Path


DEFAULT_REGISTER = Path("/mnt/obsidian/05_Action_Items/Action_Register_Readable.md")
REGISTER_LINK = (
    "obsidian://open?vault=Obsidian&file="
    "05_Action_Items%2FAction_Register_Readable.md"
)


def parse_open_actions(path: Path) -> list[dict[str, str]]:
    actions: list[dict[str, str]] = []
    in_open_section = False
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if line == "## Open Actions":
            in_open_section = True
            continue
        if in_open_section and line.startswith("## "):
            break
        if not in_open_section or not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) != 7 or not cells[0].startswith("A-"):
            continue
        actions.append({
            "id": cells[0],
            "action": cells[1],
            "priority": cells[2],
            "due": cells[3],
            "next_step": cells[4],
        })
    return actions


def action_line(action: dict[str, str]) -> str:
    metadata = [action["priority"]]
    if action["due"]:
        metadata.append(f"due {action['due']}")
    line = f"• **{action['id']}** ({', '.join(metadata)}): {action['action']}"
    if action["next_step"]:
        line += f"\n  Next: {action['next_step']}"
    return line


def split_messages(text: str, limit: int) -> list[str]:
    messages: list[str] = []
    current = ""
    for line in text.splitlines():
        candidate = line if not current else f"{current}\n{line}"
        if current and len(candidate) > limit:
            messages.append(current)
            current = line
        else:
            current = candidate
    if current:
        messages.append(current)
    return messages


def render(actions: list[dict[str, str]]) -> str:
    lines = ["**Daily action items**"]
    if actions:
        lines.append(f"\n**My open actions ({len(actions)})**")
        lines.extend(action_line(action) for action in actions)
    else:
        lines.append("\nNo open actions are currently in the register.")
    lines.extend([
        "",
        f"**Open the Action Register:** <{REGISTER_LINK}>",
        "Reply with an ID and update, for example: `A-003 closed` or `A-007 pending: awaiting X`.",
    ])
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--register", type=Path, default=DEFAULT_REGISTER)
    parser.add_argument("--chunk-size", type=int, default=1800)
    args = parser.parse_args()
    if not args.register.is_file():
        raise SystemExit(f"Action register not found: {args.register}")
    for index, message in enumerate(
        split_messages(render(parse_open_actions(args.register)), args.chunk_size), start=1
    ):
        if index > 1:
            print(f"**Daily action items (continued {index})**")
        print(message)
        print("\n---MESSAGE BREAK---\n")


if __name__ == "__main__":
    main()
