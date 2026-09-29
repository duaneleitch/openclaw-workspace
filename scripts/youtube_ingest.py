#!/home/duane/.local/share/alfred-media/venv/bin/python
"""VPS-local YouTube capture with caption-first transcription and vault provenance."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from faster_whisper import WhisperModel
import imageio_ffmpeg


MEDIA_ROOT = Path("/home/duane/.local/share/alfred-media")
VENV_BIN = MEDIA_ROOT / "venv" / "bin"
YT_DLP = VENV_BIN / "yt-dlp"
DEFAULT_RAW_ROOT = Path("/mnt/obsidian/10_Raw/Video")
DEFAULT_NOTE_ROOT = Path("/mnt/obsidian/20_Knowledge/Sources")


def slugify(value: str) -> str:
    value = re.sub(r"[^A-Za-z0-9]+", "-", value).strip("-").lower()
    return value[:80] or "youtube-source"


def vtt_to_text(path: Path) -> str:
    lines: list[str] = []
    last = ""
    for raw in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw.strip()
        if not line or line == "WEBVTT" or "-->" in line or line.isdigit():
            continue
        line = re.sub(r"<[^>]+>", "", line)
        if line != last:
            lines.append(line)
            last = line
    return "\n".join(lines).strip()


def transcribe(audio: Path) -> str:
    model = WhisperModel("base.en", device="cpu", compute_type="int8", cpu_threads=2, num_workers=1)
    segments, _ = model.transcribe(str(audio), beam_size=5, vad_filter=True)
    return "\n".join(segment.text.strip() for segment in segments if segment.text.strip())


def run_capture(url: str, destination: Path, cookies: Path | None) -> None:
    command = [
        str(YT_DLP), "--no-playlist", "--js-runtimes", "node:/usr/bin/node",
        "--ffmpeg-location", imageio_ffmpeg.get_ffmpeg_exe(),
        "--write-info-json", "--write-thumbnail", "--write-subs", "--write-auto-subs",
        "--sub-langs", "en.*", "--sub-format", "vtt", "-f", "bestaudio/best",
        "-k", "-x", "--audio-format", "mp3", "-o", str(destination / "source.%(ext)s"), url,
    ]
    if cookies:
        command[1:1] = ["--cookies", str(cookies)]
    subprocess.run(command, check=True)


def write_source_note(note_path: Path, title: str, url: str, raw_path: Path, transcript_path: Path) -> None:
    note_path.parent.mkdir(parents=True, exist_ok=True)
    raw_relative = raw_path.relative_to("/mnt/obsidian")
    transcript_relative = transcript_path.relative_to("/mnt/obsidian")
    captured = datetime.now(ZoneInfo("America/Toronto")).date().isoformat()
    note_path.write_text(
        "---\n"
        "type: source\n"
        "source_type: youtube_video\n"
        f"captured: {captured}\n"
        "status: raw_processed\n"
        "actions_requested: false\n"
        "---\n\n"
        f"# {title}\n\n"
        f"- **Source:** {url}\n"
        f"- **Raw assets:** [[{raw_relative}]]\n"
        f"- **Transcript:** [[{transcript_relative}]]\n"
        "- **Action items:** Not created. Create only on Duane's request.\n\n"
        "## Processing Notes\n\n"
        "Captions were used when available. Otherwise, the VPS generated this transcript with local faster-whisper.\n\n"
        "## Summary\n\n"
        "_Pending review and summary._\n",
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    parser.add_argument("--cookies", type=Path, help="Netscape-format cookies file stored locally on the VPS")
    parser.add_argument("--raw-root", type=Path, default=DEFAULT_RAW_ROOT)
    parser.add_argument("--note-root", type=Path, default=DEFAULT_NOTE_ROOT)
    args = parser.parse_args()
    if args.cookies and not args.cookies.is_file():
        raise SystemExit(f"Cookies file not found: {args.cookies}")

    stamp = datetime.now(ZoneInfo("America/Toronto")).strftime("%Y-%m-%d_%H%M%S")
    destination = args.raw_root / f"{stamp}_{slugify(args.url)}"
    destination.mkdir(parents=True, exist_ok=False)
    run_capture(args.url, destination, args.cookies)

    info_files = list(destination.glob("*.info.json"))
    metadata = json.loads(info_files[0].read_text(encoding="utf-8")) if info_files else {}
    title = str(metadata.get("title") or destination.name)
    vtt_files = list(destination.glob("*.vtt"))
    transcript_text = vtt_to_text(vtt_files[0]) if vtt_files else ""
    source = "captions" if transcript_text else "local faster-whisper"
    if not transcript_text:
        audio_files = list(destination.glob("*.mp3"))
        if not audio_files:
            raise SystemExit("Capture completed but no MP3 was produced for transcription")
        transcript_text = transcribe(audio_files[0])
    transcript_path = destination / "transcript.txt"
    transcript_path.write_text(transcript_text + "\n", encoding="utf-8")

    note_name = f"{stamp[:10]}_{slugify(title)}.md"
    note_path = args.note_root / note_name
    write_source_note(note_path, title, args.url, destination, transcript_path)
    print(json.dumps({"raw_assets": str(destination), "transcript": str(transcript_path), "note": str(note_path), "transcript_source": source}))


if __name__ == "__main__":
    main()
