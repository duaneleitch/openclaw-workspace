# NemoClaw Complete How-To Guide

> Sources: https://nemoclawai.io | https://nemoclawai.io/install | https://nemoclawai.io/docs/
> Compiled: 2026-03-27 | Covers: Overview, How It Works, Architecture, Install, Quickstart, All How-To Guides, Reference, Troubleshooting

---

## Table of Contents

1. What Is NemoClaw?
2. How It Works
3. Architecture
4. System Requirements
5. Installation
6. Onboard Wizard and Initial Configuration
7. Connecting and Running Your First Agent
8. Switching Inference Models
9. Managing Network Requests (Approvals)
10. Customizing the Network Policy
11. Network Policy Reference (Baseline)
12. Deploying to a Remote GPU Instance
13. Setting Up the Telegram Bridge
14. Monitoring Sandbox Activity
15. Full CLI Reference
16. Upgrading and Uninstalling
17. Troubleshooting

---

## 1. What Is NemoClaw?

NemoClaw is an open source reference stack by NVIDIA that simplifies running OpenClaw always-on assistants safely. It incorporates policy-based privacy and security guardrails, giving operators control over their agents' behavior and data handling.

NemoClaw uses open source NVIDIA Nemotron models alongside the NVIDIA OpenShell runtime (part of the NVIDIA Agent Toolkit) — a secure environment designed for executing AI agents more safely. This enables self-evolving agents to run in clouds, on-prem, RTX PCs, and DGX Spark.

### Core Capabilities

| Capability | Description |
|---|---|
| Sandbox OpenClaw | Creates an OpenShell sandbox pre-configured for OpenClaw, with strict filesystem and network policies applied from first boot |
| Route Inference | Configures OpenShell inference routing so agent traffic flows through cloud-hosted Nemotron 3 Super 120B via build.nvidia.com |
| Manage the Lifecycle | Handles blueprint versioning, digest verification, and sandbox setup |
| Privacy Router | Intelligent routing between local Nemotron models and cloud providers; sensitive data stays on-device |
| Network Policy Engine | Default-deny outbound networking; every external connection requires operator approval with full audit trail |
| Multi-Platform | Supports GeForce RTX, RTX PRO, DGX Station, and DGX Spark |

### The Problem It Solves

Autonomous AI agents like OpenClaw can make arbitrary network requests, access the host filesystem, and call any inference endpoint. Without guardrails, this creates security, cost, and compliance risks that grow as agents run unattended.

### Benefits

| Benefit | Description |
|---|---|
| Sandboxed execution | Every agent runs inside an OpenShell sandbox with Landlock, seccomp, and network namespace isolation. No access granted by default |
| NVIDIA cloud inference | Agent traffic routes through cloud-hosted Nemotron 3 Super 120B via build.nvidia.com, transparent to the agent |
| Declarative network policy | Egress rules defined in YAML. Unknown hosts are blocked and surfaced to the operator for approval |
| Single CLI | The nemoclaw command orchestrates the full stack: gateway, sandbox, inference provider, and network policy |
| Blueprint lifecycle | Versioned blueprints handle sandbox creation, digest verification, and reproducible setup |

### Use Cases

| Use Case | Description |
|---|---|
| Always-on assistant | Run an OpenClaw assistant with controlled network access and operator-approved egress |
| Sandboxed testing | Test agent behavior in a locked-down environment before granting broader permissions |
| Remote GPU deployment | Deploy a sandboxed agent to a remote GPU instance for persistent operation |

---

## 2. How It Works

NemoClaw combines a lightweight CLI plugin with a versioned blueprint to move OpenClaw into a controlled sandbox.

### The Flow

```
nemoclaw onboard
     |
     v
nemoclaw plugin
     |
     v
blueprint runner
     |
     v
openshell CLI (sandbox · gateway · inference · policy)
     |
     v
OpenShell Sandbox:
  - OpenClaw agent
  - NVIDIA inference (routed)
  - Strict network policy
  - Filesystem isolation
```

### Design Principles

**Thin plugin, versioned blueprint**
The plugin stays small and stable. Orchestration logic lives in the blueprint and evolves on its own release cadence.

**Respect CLI boundaries**
The nemoclaw CLI is the primary interface. Plugin commands are available under `openclaw nemoclaw` but do not override built-in OpenClaw commands.

**Supply chain safety**
Blueprint artifacts are immutable, versioned, and digest-verified before execution.

**OpenShell-native for new installs**
For users without an existing OpenClaw installation, NemoClaw recommends `openshell sandbox create` directly rather than forcing a plugin-driven bootstrap.

**Reproducible setup**
Running setup again recreates the sandbox from the same blueprint and policy definitions.

### Plugin and Blueprint

NemoClaw is split into two components:

- **The plugin** — A TypeScript package that powers the `nemoclaw` CLI and registers commands under `openclaw nemoclaw`. Handles user interaction and delegates orchestration work to the blueprint.

- **The blueprint** — A versioned Python artifact containing all the logic for creating sandboxes, applying policies, and configuring inference. The plugin resolves, verifies, and executes the blueprint as a subprocess.

### Sandbox Creation

When you run `nemoclaw onboard`:

1. The plugin downloads the blueprint artifact, checks version compatibility, and verifies the digest
2. The blueprint determines which OpenShell resources to create or update (gateway, inference providers, sandbox, network policy)
3. The blueprint calls OpenShell CLI commands to create the sandbox and configure each resource
4. After the sandbox starts, the agent runs inside it with all network, filesystem, and inference controls in place

### Inference Routing

Inference requests from the agent never leave the sandbox directly. OpenShell intercepts every inference call and routes it to the configured provider (Nemotron 3 Super 120B through build.nvidia.com by default). You can switch models at runtime without restarting the sandbox.

### Network and Filesystem Policy

The sandbox starts with a strict baseline policy defined in `openclaw-sandbox.yaml`:

- **Network**: Only endpoints listed in the policy are allowed. When the agent tries to reach an unlisted host, OpenShell blocks the request and surfaces it in the TUI for operator approval.
- **Filesystem**: The agent can write to `/sandbox` and `/tmp`. All other system paths are read-only.

Approved endpoints persist for the current session but are not saved to the baseline policy file.

---

## 3. Architecture

NemoClaw has two main components: a TypeScript plugin that integrates with the OpenClaw CLI, and a Python blueprint that orchestrates OpenShell resources.

### NemoClaw Plugin Structure

```
nemoclaw/
├── src/
│   ├── index.ts          Plugin entry — registers all commands
│   ├── cli.ts            Commander.js subcommand wiring
│   ├── commands/
│   │   ├── launch.ts     Fresh install into OpenShell
│   │   ├── connect.ts    Interactive shell into sandbox
│   │   ├── status.ts     Blueprint run state + sandbox health
│   │   ├── logs.ts       Stream blueprint and sandbox logs
│   │   └── slash.ts      /nemoclaw chat command handler
│   └── blueprint/
│       ├── resolve.ts    Version resolution, cache management
│       ├── fetch.ts      Download blueprint from OCI registry
│       ├── verify.ts     Digest verification, compatibility checks
│       ├── exec.ts       Subprocess execution of blueprint runner
│       └── state.ts      Persistent state (run IDs)
├── openclaw.plugin.json  Plugin manifest
└── package.json          Commands declared under openclaw.extensions
```

### NemoClaw Blueprint Structure

```
nemoclaw-blueprint/
├── blueprint.yaml                      Manifest — version, profiles, compatibility
├── orchestrator/
│   └── runner.py                       CLI runner — plan / apply / status
├── policies/
│   └── openclaw-sandbox.yaml           Strict baseline network + filesystem policy
```

### Blueprint Lifecycle

```
resolve --> verify digest --> plan --> apply --> status
```

- **Resolve**: Plugin locates the blueprint artifact and checks version against `min_openshell_version` and `min_openclaw_version` constraints in `blueprint.yaml`
- **Verify**: Plugin checks the artifact digest against the expected value
- **Plan**: Runner determines what OpenShell resources to create or update (gateway, providers, sandbox, inference route, policy)
- **Apply**: Runner executes the plan by calling `openshell` CLI commands
- **Status**: Runner reports current state

### Sandbox Environment

The sandbox runs the `ghcr.io/nvidia/openshell-community/sandboxes/openclaw` container image.

Inside the sandbox:
- OpenClaw runs with the NemoClaw plugin pre-installed
- Inference calls are routed through OpenShell to the configured provider
- Network egress is restricted by the baseline policy in `openclaw-sandbox.yaml`
- Filesystem access is confined to `/sandbox` and `/tmp` for read-write; system paths are read-only

### Inference Routing Path

```
Agent (sandbox) --> OpenShell gateway --> NVIDIA cloud (build.nvidia.com)
```

---

## 4. System Requirements

### Operating System

| Platform | Support |
|---|---|
| Ubuntu 22.04+ | Recommended |
| macOS (Apple Silicon) | Via Colima or Docker Desktop |
| Windows | Via WSL2 + Docker Desktop |

> Note: Podman on macOS is not yet supported.

### Required Software

- **Node.js**: v20+ (v22 recommended). Auto-installed by the install script via nvm if not present.
- **Container Runtime**: Docker Engine 20+ on Linux; Colima or Docker Desktop on macOS; Docker Desktop with WSL backend on Windows.

### Hardware

| Component | Minimum | Recommended |
|---|---|---|
| RAM | 8 GB | 16 GB |
| Disk | 20 GB free | 40 GB free |
| GPU | Optional | 8 GB+ VRAM for local Nemotron inference |

> Without a GPU, inference routes through the NVIDIA Cloud API (requires an NVIDIA API key).

### NVIDIA API Key

Get a free API key from [build.nvidia.com](https://build.nvidia.com). Required for cloud inference (the default mode). Stored in `~/.nemoclaw/credentials.json` after first run of `nemoclaw onboard`.

---

## 5. Installation

> **Important**: NemoClaw currently requires a **fresh installation of OpenClaw**. Do not install on top of an existing OpenClaw setup.

### One-Liner Install (Recommended)

```bash
curl -fsSL https://www.nvidia.com/nemoclaw.sh | bash
```

Works on Linux (Ubuntu 22.04+), macOS (Apple Silicon via Colima/Docker Desktop), and Windows (WSL2 + Docker Desktop).

The script:
- Installs the NemoClaw CLI and its dependencies
- Auto-installs Node.js via nvm if not present
- Runs `nemoclaw onboard` to complete setup

### Verify the Installation

After install, verify the CLI is working:

```bash
nemoclaw list
```

If the command is recognized and lists sandboxes (even an empty list), the CLI is installed correctly.

---

## 6. Onboard Wizard and Initial Configuration

### Run the Wizard

```bash
nemoclaw onboard
```

The wizard performs the following steps:

1. Runs preflight checks (cgroup v2 verification on Ubuntu 24.04, DGX Spark, WSL2)
2. Prompts for your **NVIDIA API key** (stored in `~/.nemoclaw/credentials.json`)
3. Prompts for a **sandbox name** (must follow RFC 1123 rules: lowercase alphanumeric + hyphens, start and end with alphanumeric; uppercase is auto-lowercased; e.g., `my-assistant`, `dev1`)
4. Creates an OpenShell gateway
5. Registers the NVIDIA inference provider with the Nemotron 3 Super 120B model
6. Builds the sandbox image and creates the sandbox
7. Applies the baseline network policy

### What Each Configuration Step Does

**Step 1 — Select Your Models**
Choose between:
- Nemotron 3 Super 120B (local, full privacy)
- Nemotron 3 Nano 4B (edge)
- Cloud models (OpenAI, Anthropic)

The Privacy Router handles automatic selection at runtime.

**Step 2 — Configure Privacy Policies**
Define which data categories stay local and which can be routed to cloud models. Defaults to maximum privacy (everything local).

**Step 3 — Set Network Policies**
Configure outbound network rules. Default is deny-all. Approve specific domains and APIs the agent needs to access.

**Step 4 — Test Your Sandbox**
Run a test agent inside the OpenShell sandbox to verify isolation, network policies, and model routing are working correctly.

> All configuration is stored in `~/.nemoclaw/config.yaml`. You can edit this file directly.

---

## 7. Connecting and Running Your First Agent

### Connect to the Sandbox

```bash
nemoclaw my-assistant connect
```

This opens an interactive session with the OpenClaw agent running inside the sandbox.

> If the TUI view is not a good fit for very long responses, use the CLI form instead (see below).

### Run Your First Prompt

```bash
openclaw agent --agent main --local -m "Hello from my secure sandbox" --session-id test
```

The agent processes the prompt using the configured Nemotron model through the OpenShell gateway. This is the recommended workaround when you need the full response printed directly in the terminal.

---

## 8. Switching Inference Models

You can change the active inference model while the sandbox is running. No restart is required.

### Switch to a Different Model

```bash
openshell inference set --provider nvidia-nim --model nvidia/nemotron-3-super-120b-a12b
```

This requires the `NVIDIA_API_KEY` environment variable (stored in `~/.nemoclaw/credentials.json` during onboard).

### Verify the Active Model

```bash
openclaw nemoclaw status
```

Add `--json` for machine-readable output:

```bash
openclaw nemoclaw status --json
```

The output includes: active provider, model, and endpoint.

### Available Models

| Model ID | Label | Context Window | Max Output |
|---|---|---|---|
| nvidia/nemotron-3-super-120b-a12b | Nemotron 3 Super 120B | 131,072 | 8,192 |
| nvidia/llama-3.1-nemotron-ultra-253b-v1 | Nemotron Ultra 253B | 131,072 | 4,096 |
| nvidia/llama-3.3-nemotron-super-49b-v1.5 | Nemotron Super 49B v1.5 | 131,072 | 4,096 |
| nvidia/nemotron-3-nano-30b-a3b | Nemotron 3 Nano 30B | 131,072 | 4,096 |

### Inference Profile: Default

| Field | Value |
|---|---|
| Profile | default |
| Provider | NVIDIA cloud (nvidia-nim) |
| Model | nvidia/nemotron-3-super-120b-a12b |
| Endpoint | integrate.api.nvidia.com |
| Credential | NVIDIA_API_KEY environment variable |
| Use Case | Production — requires an NVIDIA API key |

---

## 9. Managing Network Requests (Operator Approvals)

OpenShell uses a **default-deny** outbound networking model. When the agent tries to reach an endpoint not in the policy, the request is blocked and presented in the TUI for operator approval.

### Open the TUI

Start the OpenShell terminal UI to monitor sandbox activity:

```bash
openshell term
```

For a remote sandbox:

```bash
ssh my-gpu-box 'cd /home/ubuntu/nemoclaw && . .env && openshell term'
```

The TUI displays:
- Sandbox state and active inference provider
- A live feed of network activity
- Blocked egress requests awaiting operator approval

### How a Blocked Request Appears

When the agent attempts to reach an unlisted endpoint, OpenShell blocks the connection and displays:

- Host and port of the destination
- Binary that initiated the request
- HTTP method and path (if available)

### Approve or Deny

Use the TUI approval prompt:

- **Approve**: Adds the endpoint to the running policy for the current session
- **Deny**: Keeps the endpoint blocked

Approved endpoints remain in the running policy until the sandbox stops. They are **not** persisted to the baseline policy file.

### Run the Guided Walkthrough

To observe the full approval flow in a guided session:

```bash
./scripts/walkthrough.sh
```

Opens a split tmux session with the TUI on the left and the agent on the right. Requires `tmux` and `NVIDIA_API_KEY`.

---

## 10. Customizing the Network Policy

Add, remove, or modify the endpoints the sandbox is allowed to reach. Supports both static changes (persisted) and dynamic changes (current session only).

### Static Changes (Persisted Across Restarts)

1. Open `nemoclaw-blueprint/policies/openclaw-sandbox.yaml`
2. Add or modify endpoint entries. Each entry in the `network` section defines an endpoint group with:
   - `endpoints` — host and port pairs
   - `binaries` — executables allowed to use this endpoint
   - `rules` — HTTP methods and paths permitted
3. Apply the updated policy by re-running the wizard:
   ```bash
   nemoclaw onboard
   ```
4. Verify:
   ```bash
   openclaw nemoclaw status
   ```

### Dynamic Changes (Current Session Only)

1. Create a YAML file with the endpoints to add (same format as the baseline policy)
2. Apply the policy update to the running sandbox:
   ```bash
   openshell policy set <policy-file>
   ```

The change takes effect immediately but resets to baseline when the sandbox stops.

---

## 11. Network Policy Reference (Baseline)

### Filesystem Access

| Path | Access |
|---|---|
| /sandbox, /tmp, /dev/null | Read-write |
| /usr, /lib, /proc, /dev/urandom, /app, /etc, /var/log | Read-only |

The sandbox process runs as a dedicated `sandbox` user and group. Landlock LSM enforcement applies on a best-effort basis.

### Default Allowed Network Endpoints

| Policy | Endpoints | Binaries | Rules |
|---|---|---|---|
| claude_code | api.anthropic.com:443, statsig.anthropic.com:443, sentry.io:443 | /usr/local/bin/claude | All methods |
| nvidia | integrate.api.nvidia.com:443, inference-api.nvidia.com:443 | /usr/local/bin/claude, /usr/local/bin/openclaw | All methods |
| github | github.com:443 | /usr/bin/gh, /usr/bin/git | All methods, all paths |
| github_rest_api | api.github.com:443 | /usr/bin/gh | GET, POST, PATCH, PUT, DELETE |
| clawhub | clawhub.com:443 | /usr/local/bin/openclaw | GET, POST |
| openclaw_api | openclaw.ai:443 | /usr/local/bin/openclaw | GET, POST |
| openclaw_docs | docs.openclaw.ai:443 | /usr/local/bin/openclaw | GET only |
| npm_registry | registry.npmjs.org:443 | /usr/local/bin/openclaw, /usr/local/bin/npm | GET only |
| telegram | api.telegram.org:443 | Any binary | GET, POST on /bot*/** |

All endpoints use TLS (port 443).

### Inference Policy Note

The baseline policy allows only the local inference route. External inference providers are reached through the OpenShell gateway, not by direct sandbox egress.

---

## 12. Deploying to a Remote GPU Instance

Run NemoClaw on a remote GPU instance through [Brev](https://brev.nvidia.com) for always-on persistent operation.

> **Warning**: The `nemoclaw deploy` command is **experimental** and may not work as expected.

### Prerequisites

- The [Brev CLI](https://brev.nvidia.com) installed and authenticated
- An NVIDIA API key from [build.nvidia.com](https://build.nvidia.com)
- NemoClaw installed locally

### Deploy the Instance

```bash
nemoclaw deploy <instance-name>
```

Replace `<instance-name>` with a name for your remote instance (e.g., `my-gpu-box`).

The deploy script performs the following on the VM:
- Installs Docker and the NVIDIA Container Toolkit (if a GPU is present)
- Installs the OpenShell CLI
- Runs `nemoclaw setup` (creates gateway, registers providers, launches sandbox)
- Starts auxiliary services (Telegram bridge, cloudflared tunnel)

### Reconnect to the Remote Sandbox

Run `nemoclaw deploy <instance-name>` again to reconnect to an existing instance.

### Monitor the Remote Sandbox

```bash
ssh <instance-name> 'cd /home/ubuntu/nemoclaw && set -a && . .env && set +a && openshell term'
```

### Run a Test Prompt on Remote

```bash
openclaw agent --agent main --local -m "Hello from the remote sandbox" --session-id test
```

### Configure GPU Type

The deploy script uses the `NEMOCLAW_GPU` environment variable to select the GPU type.

Default: `a2-highgpu-1g:nvidia-tesla-a100:1`

```bash
export NEMOCLAW_GPU="a2-highgpu-1g:nvidia-tesla-a100:2"
nemoclaw deploy <instance-name>
```

---

## 13. Setting Up the Telegram Bridge

Forward messages between a Telegram bot and the OpenClaw agent running inside the sandbox. The Telegram bridge is an auxiliary service managed by `nemoclaw start`.

### Prerequisites

- A running NemoClaw sandbox (local or remote)
- A Telegram bot token from [@BotFather](https://t.me/BotFather)

### Step 1 — Create a Telegram Bot

1. Open Telegram and send `/newbot` to [@BotFather](https://t.me/BotFather)
2. Follow the prompts to create a bot
3. Save the bot token you receive

### Step 2 — Set the Environment Variable

```bash
export TELEGRAM_BOT_TOKEN=<your-bot-token>
```

### Step 3 — Start Auxiliary Services

```bash
nemoclaw start
```

This launches:
- **Telegram bridge** — forwards messages between Telegram and the agent
- **cloudflared tunnel** — provides external access to the sandbox

The Telegram bridge only starts when `TELEGRAM_BOT_TOKEN` is set.

### Verify the Services

```bash
nemoclaw status
```

The output shows the status of all auxiliary services.

### Send a Message

Open Telegram, find your bot, and send a message. The bridge forwards it to the OpenClaw agent inside the sandbox and returns the agent's response.

### Restrict Access by Chat ID

To restrict which Telegram chats can interact with the agent:

```bash
export ALLOWED_CHAT_IDS="123456789,987654321"
nemoclaw start
```

### Stop the Services

```bash
nemoclaw stop
```

---

## 14. Monitoring Sandbox Activity

Use the NemoClaw status, logs, and TUI tools together to inspect sandbox health, trace agent behavior, and diagnose problems.

### Check Sandbox Health

```bash
openclaw nemoclaw status
```

Key fields in the output:
- **Sandbox state**: running, stopped, or error
- **Blueprint run ID**: identifier for the most recent blueprint execution
- **Inference provider**: active provider, model, and endpoint

Add `--json` for machine-readable output:

```bash
openclaw nemoclaw status --json
```

> If you run this from **inside** the sandbox, host-level details are not available. Run `openshell sandbox list` on the host instead. The status command detects the sandbox context and reports "active (inside sandbox)" in this case.

### View Logs

Stream recent log output:

```bash
openclaw nemoclaw logs
```

Follow in real time:

```bash
openclaw nemoclaw logs -f
```

Show a specific number of lines:

```bash
openclaw nemoclaw logs -n 100
```

View logs for a specific blueprint run:

```bash
openclaw nemoclaw logs --run-id <id>
```

### Monitor Network Activity in the TUI

```bash
openshell term
```

The TUI shows:
- Active network connections from the sandbox
- Blocked egress requests awaiting operator approval
- Inference routing status

For a remote sandbox, SSH to the instance and run `openshell term` there.

### Test Inference

```bash
nemoclaw my-assistant connect
openclaw agent --agent main --local -m "Test inference" --session-id debug
```

If inference fails:
1. Run `openclaw nemoclaw status` to confirm active provider and endpoint
2. Run `openclaw nemoclaw logs -f` to view error messages from the blueprint runner
3. Verify that the inference endpoint is reachable from the host

---

## 15. Full CLI Reference

NemoClaw provides two command interfaces:
- **Plugin commands** run under the `openclaw nemoclaw` namespace inside the OpenClaw CLI
- **Standalone nemoclaw binary** handles host-side setup, deployment, and service management

Both are installed when you run `npm install -g nemoclaw`.

---

### Plugin Commands (openclaw nemoclaw)

#### `openclaw nemoclaw launch`

Bootstrap OpenClaw inside an OpenShell sandbox. If NemoClaw detects an existing host installation, launch stops unless you pass `--force`.

```bash
openclaw nemoclaw launch [--force] [--profile <profile>]
```

| Flag | Description |
|---|---|
| --force | Skip ergonomics warning and force plugin-driven bootstrap |
| --profile \<profile\> | Blueprint profile to use. Default: `default` |

#### `openclaw nemoclaw status`

Display sandbox health, blueprint run state, and inference configuration.

```bash
openclaw nemoclaw status [--json]
```

| Flag | Description |
|---|---|
| --json | Output as JSON for programmatic consumption |

#### `openclaw nemoclaw logs`

Stream blueprint execution and sandbox logs.

```bash
openclaw nemoclaw logs [-f] [-n <count>] [--run-id <id>]
```

| Flag | Description |
|---|---|
| -f, --follow | Follow log output, like `tail -f` |
| -n, --lines \<count\> | Number of lines to show. Default: 50 |
| --run-id \<id\> | Show logs for a specific blueprint run |

#### `/nemoclaw` Slash Command

Available inside the OpenClaw chat interface:

| Subcommand | Description |
|---|---|
| /nemoclaw status | Show sandbox and inference state |

---

### Standalone Host Commands (nemoclaw binary)

#### `nemoclaw onboard`

Run the interactive setup wizard. Creates an OpenShell gateway, registers inference providers, builds the sandbox image, and creates the sandbox. Use for new installs and for recreating a sandbox after policy or configuration changes.

```bash
nemoclaw onboard
```

The first run prompts for your NVIDIA API key and saves it to `~/.nemoclaw/credentials.json`.

#### `nemoclaw list`

List all registered sandboxes with their model, provider, and policy presets.

```bash
nemoclaw list
```

#### `nemoclaw deploy` *(Experimental)*

Deploy NemoClaw to a remote GPU instance through Brev.

```bash
nemoclaw deploy <instance-name>
```

#### `nemoclaw <name> connect`

Connect to a sandbox by name.

```bash
nemoclaw my-assistant connect
```

#### `nemoclaw <name> status`

Show sandbox status, health, and inference configuration.

```bash
nemoclaw my-assistant status
```

#### `nemoclaw <name> logs`

View sandbox logs. Use `--follow` to stream output in real time.

```bash
nemoclaw my-assistant logs [--follow]
```

#### `nemoclaw <name> destroy`

Stop the NIM container and delete the sandbox. Removes the sandbox from the registry.

```bash
nemoclaw my-assistant destroy
```

#### `nemoclaw <name> policy-add`

Add a policy preset to a sandbox. Presets extend the baseline network policy with additional endpoints.

```bash
nemoclaw my-assistant policy-add
```

#### `nemoclaw <name> policy-list`

List available policy presets and show which ones are applied to the sandbox.

```bash
nemoclaw my-assistant policy-list
```

#### `nemoclaw start`

Start auxiliary services (Telegram bridge and cloudflared tunnel). Requires `TELEGRAM_BOT_TOKEN` for the Telegram bridge.

```bash
nemoclaw start
```

#### `nemoclaw stop`

Stop all auxiliary services.

```bash
nemoclaw stop
```

#### `nemoclaw status`

Show the sandbox list and the status of auxiliary services.

```bash
nemoclaw status
```

#### `nemoclaw setup-spark`

Set up NemoClaw on DGX Spark. Applies cgroup v2 and Docker fixes required for Ubuntu 24.04. Run with `sudo` on the Spark host. After fixes complete, prompts you to run `nemoclaw onboard` to continue setup.

```bash
sudo nemoclaw setup-spark
```

---

### OpenShell CLI Commands

#### `openshell term`

Open the OpenShell TUI to monitor sandbox activity and approve network egress requests. Run on the host where the sandbox is running.

```bash
openshell term
```

For a remote Brev instance, SSH to the instance and run `openshell term` there, or use a port-forward to the gateway.

#### `openshell inference set`

Switch the active inference model at runtime.

```bash
openshell inference set --provider nvidia-nim --model <model-id>
```

#### `openshell policy set`

Apply a dynamic policy update to a running sandbox.

```bash
openshell policy set <policy-file>
```

#### `openshell sandbox list`

List the underlying sandbox state (useful when running status from inside the sandbox).

```bash
openshell sandbox list
```

---

## 16. Upgrading and Uninstalling

### Upgrading NemoClaw

Keep NemoClaw up to date to get the latest security patches and features.

**npm install:**
```bash
npm update -g nemoclaw
```

**pip install:**
```bash
pip install --upgrade nemoclaw
```

**From source:**
```bash
cd NemoClaw && git pull && pip install -e .
```

**Docker:**
```bash
docker pull ghcr.io/nvidia/nemoclaw:latest && docker restart nemoclaw
```

Check the changelog at [github.com/NVIDIA/NemoClaw/releases](https://github.com/NVIDIA/NemoClaw/releases) for what's new.

### Uninstalling NemoClaw

**npm install:**
```bash
npm uninstall -g nemoclaw
```

**pip install:**
```bash
pip uninstall nemoclaw
```

**From source:**
```bash
rm -rf ~/NemoClaw
```

**Docker:**
```bash
docker stop nemoclaw && docker rm nemoclaw && docker rmi ghcr.io/nvidia/nemoclaw:latest
```

### Remove User Data (Optional)

This deletes all blueprints, sandbox configs, and model data. Back up anything you need first.

**macOS/Linux:**
```bash
rm -rf ~/.nemoclaw
```

**Windows (PowerShell):**
```powershell
rmdir /s /q %USERPROFILE%\.nemoclaw
```

---

## 17. Troubleshooting

### Installation Issues

---

**`nemoclaw` not found after install**

If you use nvm or fnm to manage Node.js, the installer may not update your current shell's PATH. The binary is installed but the shell session does not know where to find it.

```bash
source ~/.bashrc
# or for zsh:
source ~/.zshrc
```

Or open a new terminal window.

---

**Installer fails on unsupported platform**

NemoClaw requires Linux Ubuntu 22.04 LTS or later. Verify you are running a supported Linux distribution.

---

**Node.js version is too old**

NemoClaw requires Node.js 20 or later.

```bash
node --version
```

If below v20:
```bash
nvm install 20
nvm use 20
```

Then re-run the installer.

---

**Docker is not running**

```bash
sudo systemctl start docker
```

On macOS with Docker Desktop, open the Docker Desktop application and wait for it to finish starting before retrying.

---

**npm install fails with permission errors**

Do not run npm with sudo. Instead, configure npm to use a directory you own:

```bash
mkdir -p ~/.npm-global
npm config set prefix ~/.npm-global
export PATH=~/.npm-global/bin:$PATH
```

Add the `export` line to `~/.bashrc` or `~/.zshrc` to make it permanent, then re-run the installer.

---

**Port 18789 already in use**

The NemoClaw gateway uses port 18789 by default.

```bash
lsof -i :18789
kill <PID>
```

If the process doesn't exit, use `kill -9 <PID>` to force-terminate it. Then retry onboarding.

---

### Onboarding Issues

---

**Cgroup v2 errors during onboard (Ubuntu 24.04, DGX Spark, WSL2)**

Docker may not be configured for cgroup v2 delegation. The onboard preflight check detects this.

```bash
sudo nemoclaw setup-spark
nemoclaw onboard
```

---

**Invalid sandbox name**

Sandbox names must follow RFC 1123 subdomain rules: lowercase alphanumeric characters and hyphens only, must start and end with an alphanumeric character. Uppercase letters are automatically lowercased.

Use names like `my-assistant` or `dev1`.

---

**Sandbox creation fails on DGX**

On DGX machines, sandbox creation can fail if the gateway's DNS has not finished propagating or a stale port forward from a previous onboard run is still active.

```bash
nemoclaw onboard
```

The wizard cleans up stale port forwards and waits for gateway readiness automatically.

---

**Colima socket not detected (macOS)**

Newer Colima versions use `~/.config/colima/default/docker.sock` instead of the legacy `~/.colima/default/docker.sock`. NemoClaw checks both paths. If neither is found:

```bash
colima status
```

Verify Colima is running.

---

### Runtime Issues

---

**Sandbox shows as stopped**

```bash
nemoclaw onboard
```

This recreates the sandbox from the same blueprint and policy definitions.

---

**Status shows "not running" inside the sandbox**

Expected behavior. When running `openclaw nemoclaw status` inside an active sandbox, host-side sandbox state and inference configuration are not inspectable. The status command detects the sandbox context and reports "active (inside sandbox)" instead.

Run `openshell sandbox list` on the host to check the actual sandbox state.

---

**Inference requests time out**

1. Check the active provider and endpoint: `openclaw nemoclaw status`
2. Verify your NVIDIA API key is valid
3. Check for network policy rules that may block the connection

---

**Agent cannot reach an external host**

OpenShell blocks outbound connections to hosts not listed in the network policy.

```bash
openshell term
```

Use the TUI to see blocked requests and approve them. To permanently allow an endpoint, add it to the network policy file.

---

**Blueprint run failed**

```bash
openclaw nemoclaw logs --run-id <id>
```

Omit `--run-id` to view logs from the most recent run. Use `--follow` to stream logs in real time while debugging.

---

## Quick Reference Card

| Task | Command |
|---|---|
| Install NemoClaw | `curl -fsSL https://www.nvidia.com/nemoclaw.sh \| bash` |
| Run onboard wizard | `nemoclaw onboard` |
| List sandboxes | `nemoclaw list` |
| Connect to sandbox | `nemoclaw my-assistant connect` |
| Test the agent (CLI) | `openclaw agent --agent main --local -m "Hello" --session-id test` |
| Check status | `openclaw nemoclaw status` |
| Open TUI monitor | `openshell term` |
| Switch inference model | `openshell inference set --provider nvidia-nim --model <model>` |
| Apply dynamic policy | `openshell policy set <policy-file>` |
| View logs (live) | `openclaw nemoclaw logs -f` |
| Deploy to remote GPU | `nemoclaw deploy <instance-name>` |
| Start Telegram bridge | `nemoclaw start` |
| Stop auxiliary services | `nemoclaw stop` |
| Destroy sandbox | `nemoclaw my-assistant destroy` |
| DGX Spark setup | `sudo nemoclaw setup-spark` |
| Upgrade NemoClaw | `npm update -g nemoclaw` |
| Uninstall NemoClaw | `npm uninstall -g nemoclaw` |
| Remove user data | `rm -rf ~/.nemoclaw` |

---

## Resources

- Homepage: <https://nemoclawai.io>
- Install Guide: <https://nemoclawai.io/install>
- Docs Root: <https://nemoclawai.io/docs>
- Quickstart: <https://nemoclawai.io/docs/get-started/quickstart>
- Overview: <https://nemoclawai.io/docs/about/overview>
- How It Works: <https://nemoclawai.io/docs/about/how-it-works>
- Architecture: <https://nemoclawai.io/docs/reference/architecture>
- Commands: <https://nemoclawai.io/docs/reference/commands>
- Inference Profiles: <https://nemoclawai.io/docs/reference/inference-profiles>
- Network Policies: <https://nemoclawai.io/docs/reference/network-policies>
- Troubleshooting: <https://nemoclawai.io/docs/reference/troubleshooting>
- NVIDIA API Keys: <https://build.nvidia.com>
- Brev (Remote GPU): <https://brev.nvidia.com>
- GitHub Repository: <https://github.com/NVIDIA/NemoClaw>
- GitHub Issues: <https://github.com/NVIDIA/NemoClaw/issues/new>
- Discord Community: <https://discord.gg/XFpfPv9Uvx>
