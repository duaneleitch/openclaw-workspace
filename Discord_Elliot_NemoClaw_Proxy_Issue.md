# Discord in NemoClaw sandbox: REST OK, gateway proxy OK, WebSocket connects via proxy (HTTP 200 CONNECT), but bot stays offline and receives no events

## Environment

**Host / stack**

- Host: Mac Mini M4 (2024), macOS (Apple Silicon)
- Docker Desktop on external APFS‑encrypted SSD (`/Volumes/AI-Storage/Docker`)
- NemoClaw installed via `curl -fsSL https://www.nvidia.com/nemoclaw.sh | bash`
- OpenShell installed via `curl -LsSf https://raw.githubusercontent.com/NVIDIA/OpenShell/main/install.sh | sh`
- Gateway container: `openshell-cluster-nemoclaw` (with `--restart=always`)
- NemoClaw sandbox: `elliot`
- OpenClaw inside sandbox: `2026.3.11 (29dc654)`

**Proxy**

- NemoClaw/OpenShell proxy: `http://10.200.0.1:3128`
- Env in sandbox:
  - `https_proxy=http://10.200.0.1:3128`
  - `no_proxy=127.0.0.1,localhost,::1`
- TLS trust:
  - `NODE_EXTRA_CA_CERTS=/etc/openshell-tls/openshell-ca.pem`

**Models/providers**

- Primary: `nvidia/nemotron-3-super-120b-a12b`
- Fallbacks:
  - `anthropic/claude-sonnet-4-6`
  - `openai-codex/gpt-5.1`
- All three providers working from inside sandbox

**Telegram**

- Bot: `@Elliot_nemo_bot`
- Status: **fully working** via same proxy/policy setup

---

## Summary

Inside a NemoClaw sandbox:

- Telegram integration works end‑to‑end.
- Discord:
  - Authenticates.
  - REST calls work.
  - Proxy is enabled for REST + gateway.
  - Guild and user IDs resolve correctly.
  - Bot can **send** messages (e.g. “Elliot just landed” on startup).
- But:
  - Bot is **offline** in the server member list.
  - No message events are ever logged or dispatched.
  - Even with DNS and proxy tunneling confirmed working, the bot never receives events.

So Discord is “half‑working”: REST is fine, WebSocket / gateway events never show up in OpenClaw, and the bot stays offline.

---

## Config snippets

### Discord config inside sandbox (`openclaw config get channels.discord`)

```json5
{
  "enabled": true,
  "token": "__OPENCLAW_REDACTED__",
  "proxy": "http://10.200.0.1:3128",
  "groupPolicy": "allowlist",
  "streaming": "off",
  "guilds": {
    "1485613117802152116": {
      "requireMention": false,
      "users": ["805234778244775966"]
    }
  }
}
```

- `channels.discord.proxy` set explicitly to the NemoClaw proxy.
- Guild allowlisted with my user ID in `users`.
- `requireMention=false` so it should respond to all messages from that user in the guild.

### OpenShell / NemoClaw policy (network) — relevant bits

All relevant policies include `/usr/local/bin/node` to match the `#!/usr/bin/env node` launcher:

```yaml
network_policies:
  discord:
    name: discord
    endpoints:
      - host: discord.com
        port: 443
        protocol: rest
        tls: terminate
        enforcement: enforce
        rules:
          - allow:
              method: GET
              path: /**
          - allow:
              method: POST
              path: /**
          - allow:
              method: PUT
              path: /**
          - allow:
              method: PATCH
              path: /**
          - allow:
              method: DELETE
              path: /**
      - host: gateway.discord.gg
        port: 443
        protocol: rest
        tls: terminate
        enforcement: enforce
        rules:
          - allow:
              method: GET
              path: /**
          - allow:
              method: POST
              path: /**
    binaries:
      - path: /usr/local/bin/openclaw
      - path: /usr/local/bin/node
  telegram:
    # ... includes /usr/local/bin/node and works fine ...
  nvidia:
    # ... includes /usr/local/bin/node and works fine ...
  # etc.
```

Policy applied via:

```bash
openshell policy set --policy ~/elliot-policy-fix.yaml --wait elliot
```

and confirmed loaded:

> ✓ Policy version 7 loaded (active version: 7)

---

## Logs

### Gateway startup (inside sandbox)

```text
[discord] [default] Discord Message Content Intent is limited; bots under 100 servers can use it without verification.
[discord] [default] starting provider (@Elliot)
[discord] discord: rest proxy enabled
[discord] discord: gateway proxy enabled
[discord] discord channels resolved: guild:1485613117802152116→1485613117802152116 (guild:dl_70's_server2)
[discord] discord channel users resolved: 805234778244775966→805234778244775966
[discord] logged in to discord as 1486090155876945970 (Elliot)
```

Earlier in the process, before fixes, we saw:

```text
[discord] discord gateway error: Error: getaddrinfo EAI_AGAIN gateway.discord.gg
[discord] gateway: WebSocket connection closed with code 1006
```

After adding `/etc/hosts` entries for `gateway.discord.gg` we moved to:

```text
[discord] discord gateway error: Error: connect ETIMEDOUT 162.159.133.234:443
```

After setting `channels.discord.proxy` and restarting gateway, the EAI_AGAIN / ETIMEDOUT errors disappear. Startup logs look clean (as shown above), but:

- Bot remains **offline** in Discord server member list.
- Sending a message in the guild produces **no additional log entries** in `/tmp/openclaw/openclaw-2026-03-25.log`.
- No `MESSAGE_CREATE` or equivalent handler output.
- No tool/agent activity.

In other words, Discord gateway appears “connected” from OpenClaw’s perspective, but **no events flow in**.

---

## Proxy tunneling test

To isolate whether the NemoClaw/OpenShell proxy supports CONNECT tunneling to `gateway.discord.gg`, this was run inside the sandbox:

```bash
node -e "const net=require('net');const s=net.connect(3128,'10.200.0.1',()=>{s.write('CONNECT gateway.discord.gg:443 HTTP/1.1\r\nHost: gateway.discord.gg:443\r\n\r\n');s.once('data',d=>{console.log(d.toString());s.destroy();});});s.on('error',e=>console.log('ERR',e.message));"
```

Result:

```text
HTTP/1.1 200 Connection Established
```

So the proxy **does** allow CONNECT to `gateway.discord.gg:443` and will tunnel TCP.

Combined with:

- DNS fixed (via `/etc/hosts` to address initial `EAI_AGAIN`).
- Policy allowing `gateway.discord.gg:443` with `/usr/local/bin/node`.
- `channels.discord.proxy` configured.

…this strongly suggests the remaining issue is in how the OpenClaw Discord provider, running inside NemoClaw, wires up the gateway WebSocket over the proxy.

---

## What works vs what doesn’t

### Works

- Nemotron / Anthropic / OpenAI providers from sandbox.
- Telegram (via `api.telegram.org` through proxy).
- Discord REST:
  - Bot logs in.
  - Can send messages to server (e.g. “Elliot just landed” on startup).
  - Slash commands deploy.
- Discord config:
  - `groupPolicy: "allowlist"`.
  - `guilds.<id>.users` includes my user ID.
  - `requireMention: false`.

### Doesn’t work

- Bot shows **offline** in server member list.
- No events logged when sending messages in the guild.
- No agent invocations on Discord messages.
- No `MESSAGE_CREATE` or similar traces in log after startup.

---

## Expected vs actual

**Expected**

With:

- DNS resolved.
- Proxy CONNECT confirmed (HTTP 200).
- `channels.discord.proxy` set.
- Guild + user allowlisted.
- Message Content Intent enabled on the app.

I would expect:

- Discord gateway WebSocket to connect via the proxy.
- Bot to appear **online**.
- Incoming messages in the allowlisted guild (from the allowlisted user) to produce log entries and invoke the configured agent.

**Actual**

- Gateway startup logs look healthy.
- Bot can send messages.
- Bot stays **offline**.
- No events logged, no responses, no evidence of incoming messages.

---

## Why this looks like an OpenClaw/NemoClaw integration bug

- Same sandbox + proxy + policy works perfectly for Telegram (including pairing and full bidirectional messaging).
- Manual CONNECT via `net.connect` to `10.200.0.1:3128` for `gateway.discord.gg:443` returns `HTTP/1.1 200 Connection Established`.
- REST calls to Discord work and respect `channels.discord.proxy`.
- DNS and proxy issues have been eliminated (EAI_AGAIN → ETIMEDOUT → clean after `/etc/hosts` + proxy).
- There are no new log entries at all at the moment messages are sent, which means **no events** are delivered to OpenClaw.

This points to how the Discord gateway client inside OpenClaw uses the proxy / TLS in this NemoClaw environment, not to config or policy.

---

## Ask (for upstream maintainers)

1. **Confirm** whether the Discord gateway client in OpenClaw supports WebSocket over HTTP CONNECT proxies in a NemoClaw/OpenShell sandbox, and which code path is used.
2. Investigate why, in this environment:
   - Discord REST works via proxy.
   - `channels.discord.proxy` logs “gateway proxy enabled”.
   - Proxy CONNECT to `gateway.discord.gg:443` is allowed (HTTP 200).
   - Yet the bot remains offline and no events are seen.
3. Provide a recommended configuration or patch that makes Discord gateway events flow in a NemoClaw sandbox with an outbound HTTP proxy.

Once a fix is available, Elliot’s Discord integration can be re-enabled end-to-end alongside the already-working Telegram channel.

---

## Gateway runtime notes (Elliot sandbox)

For completeness, this is how the OpenClaw gateway is kept running inside the `elliot` NemoClaw sandbox.

### Starting the gateway

Inside the sandbox:

```bash
nemoclaw elliot connect
nohup openclaw gateway >/tmp/openclaw-gateway.log 2>&1 &
```

- `nohup` detaches the process from the current terminal, so closing the shell does not stop the gateway.
- Logs go to `/tmp/openclaw-gateway.log`.
- As long as the `elliot` sandbox is running, the gateway stays alive.

### Health check

To verify the gateway is still reachable:

```bash
nemoclaw elliot connect
openclaw status
```

If you see:

```text
Gateway not reachable. Is it running and accessible?
```

…then restart:

```bash
openclaw gateway stop
nohup openclaw gateway >/tmp/openclaw-gateway.log 2>&1 &
```

This pattern has been reliable for keeping Telegram (`@Elliot_nemo_bot`) online between sessions.