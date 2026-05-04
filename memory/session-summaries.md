# Session Summaries

## 2026-04-21 07:58 AM EDT
- Context: Worked through Hermes on Duane's Mac mini, running in Docker, with model routing and Docker-backed sandbox issues.
- Key decisions:
  - Switched Hermes primary model from `qwen3:30b-a3b` to `llama3.1:70b`.
  - Added fallback order in config: `gemma4:26b`, then `qwen3:30b-a3b`.
  - Confirmed Hermes is already on version `0.10.0`.
  - Identified the real sandbox bug as host-path translation failure in Docker-on-Docker on macOS, not a simple memory issue.
  - Chose a short-term workaround instead of a deeper permanent source fix during the live session.
- What was changed:
  - Updated `/Users/duaneleitch/.hermes/config.yaml` so primary is Llama 70B and fallbacks are Gemma 4 26B then Qwen 30B A3B.
  - Updated `/Users/duaneleitch/hermes-compose/docker-compose.yml` to include:
    - `TERMINAL_SANDBOX_DIR=/Users/duaneleitch/.hermes/sandboxes`
    - `HOST_HERMES_HOME=/Users/duaneleitch/.hermes`
  - Rebuilt and restarted the Hermes container.
  - Applied an in-container patch to `/opt/hermes/tools/credential_files.py` so `_resolve_hermes_home()` returns `HOST_HERMES_HOME` when `HERMES_HOME` is `/opt/data`.
  - Cleared stale `hermes-*` helper containers.
- Verified outcomes:
  - Hermes chat/model flow works with Llama as primary.
  - Docker-backed helper containers no longer remain stuck in `Created` after clearing stale containers and applying the workaround.
- Open items / next steps:
  - Make the workaround durable by baking the patch into the Docker image or otherwise applying it automatically at build/start time.
  - Revisit whether upstream Hermes has or later adds a proper host-path translation fix for containerized Docker-on-Docker macOS deployments.
  - If desired later, add Ollama cloud provider support after the Docker deployment is stabilized.
- Links:
  - Config: `/Users/duaneleitch/.hermes/config.yaml`
  - Compose: `/Users/duaneleitch/hermes-compose/docker-compose.yml`
  - Patched file inside container: `/opt/hermes/tools/credential_files.py`
  - Source: MEMORY.md#L5

