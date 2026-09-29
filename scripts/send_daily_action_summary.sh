#!/usr/bin/env bash
set -euo pipefail

usage() {
  echo "Usage: $0 --channel CHANNEL --target TARGET [--dry-run]" >&2
  exit 2
}

channel=""
target=""
dry_run=false
while (($#)); do
  case "$1" in
    --channel) channel="${2:-}"; shift 2 ;;
    --target) target="${2:-}"; shift 2 ;;
    --dry-run) dry_run=true; shift ;;
    *) usage ;;
  esac
done
[[ -n "$channel" && -n "$target" ]] || usage

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
summary_file="$(mktemp)"
trap 'rm -f "$summary_file"' EXIT

python3 "$script_dir/daily_action_summary.py" > "$summary_file"

awk '
  /^---MESSAGE BREAK---$/ { if (message != "") { print message; print "\034"; message="" }; next }
  { message = message $0 "\n" }
  END { if (message != "") print message }
' "$summary_file" | while IFS= read -r -d $'\034' message; do
  if [[ "$dry_run" == true ]]; then
    printf 'TARGET %s:%s\n%s\n---\n' "$channel" "$target" "$message"
  else
    openclaw message send --channel "$channel" --target "$target" --message "$message"
  fi
done
