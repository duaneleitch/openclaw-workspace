# OpenClaw Gateway Recovery and Remote Access Notes

## Goal
Keep the local OpenClaw gateway stable while allowing secure remote dashboard access from trusted devices.

## Current Recommended Pattern
1. Keep OpenClaw gateway bound to loopback in config.
2. Use Tailscale Serve HTTPS as the remote access path.
3. Pair/approve new devices when prompted.

## Local Stability
- Verify status:
  - `openclaw gateway status`
- Local dashboard URL:
  - `http://127.0.0.1:18789/`

## Remote Access via Tailscale
- Remote URL (tailnet only):
  - `https://srv1429500.tail8f4a6f.ts.net`
- Serve target:
  - proxy to `http://127.0.0.1:18789`

## Pairing and Device Approval
When remote UI says pairing is required:
- List devices:
  - `openclaw devices list`
- Approve newest pending request:
  - `openclaw devices approve --latest`

## Watchdog
A systemd timer checks local gateway health periodically and attempts restart if unavailable.

Paths:
- Script: `~/.local/bin/openclaw-gateway-watchdog.sh`
- Service: `~/.config/systemd/user/openclaw-gateway-watchdog.service`
- Timer: `~/.config/systemd/user/openclaw-gateway-watchdog.timer`
- Log: `~/.openclaw/logs/gateway-watchdog.log`

## Security Notes
- Never commit or share tokens/passwords.
- Do not store auth secrets in repo files.
- Use config file lookup at runtime when needed.
