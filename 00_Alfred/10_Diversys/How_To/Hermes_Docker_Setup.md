# Hermes Docker Setup

## Commands

### 1) Create the data directory
```bash
mkdir -p ~/.hermes
```

### 2) Start the Hermes setup wizard
```bash
docker run --platform linux/amd64 -it --rm -v ~/.hermes:/opt/data nousresearch/hermes-agent setup
```

### 3) If you exit partway through, restart setup
```bash
docker run --platform linux/amd64 -it --rm -v ~/.hermes:/opt/data nousresearch/hermes-agent setup
```

### 4) Start the messaging gateway
```bash
hermes gateway start
```

### 5) Check for issues
```bash
hermes doctor
```

## Setup choices used

- Setup type: Full setup
- Provider: OpenAI Codex
- TTS: Keep current (Edge TTS)
- Terminal backend: Docker
- Persist filesystem across sessions: yes
- CPU: 4
- Memory: 8192 MB
- Disk: 51200 MB
- Max iterations: 90
- Tool progress mode: new
- Compression threshold: 0.7
- Session reset: inactivity + daily reset
- Inactivity timeout: 1440 minutes
- Daily reset hour: 4
- Platform: Telegram only
- Gateway service: User service
