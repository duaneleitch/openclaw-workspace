# Claude Code VPS Integration Plan

## Executive Summary

This plan outlines how to add Claude Code to the VPS environment to enable technical/development work alongside the existing OpenClaw ecosystem. Claude Code will serve as a dedicated development agent while Alfred (main) continues as the chief of staff orchestrator.

---

## Current Environment Snapshot

| Component | Status | Details |
|-----------|--------|---------|
| **OS** | Ubuntu 24.04.4 LTS (Noble Numbat) | VPS environment |
| **Node.js** | v22.22.2 | Installed globally |
| **npm** | 10.9.7 | Installed globally |
| **OpenClaw** | Installed | Primary agent orchestration platform |
| **Claude Code** | Not installed | To be added per this plan |
| **User** | duane | Home: /home/duane |
| **Workspace** | /home/duane/.openclaw/workspace | Main working directory |

---

## Phase 1: Prerequisites and Preparation

### 1.1 System Requirements Check

**Memory Assessment**
```bash
# Check current memory usage
free -h

# Check available swap
swapon --show

# Check disk space
df -h
```

**Recommendation:** Claude Code requires minimum 4GB RAM for basic operation, 8GB+ recommended for larger codebases. If VPS is memory-constrained, configure swap or consider upgrading.

### 1.2 API Key Configuration

Claude Code requires an Anthropic API key with appropriate rate limits.

**Steps:**
1. Verify `ANTHROPIC_API_KEY` is set in environment or add to `~/.bashrc`:
   ```bash
   export ANTHROPIC_API_KEY="your-key-here"
   ```
2. Alternative: Store in secure location like `/home/duane/.config/claude/config.json`

### 1.3 Directory Structure Preparation

Create dedicated directories for Claude Code operations:

```bash
# Claude Code workspace (separate from OpenClaw workspace)
mkdir -p ~/claude-code/projects
mkdir -p ~/claude-code/sessions
mkdir -p ~/claude-code/config

# Projects directory for active development
mkdir -p ~/projects

# Git repositories directory
mkdir -p ~/git
```

---

## Phase 2: Claude Code Installation

### 2.1 Installation Method Options

#### Option A: NPM Global Install (Recommended)
```bash
# Using the same pattern as OpenClaw (which is in ~/.npm-global)
npm install -g @anthropics/claude-code

# Verify installation
which claude
claude --version
```

**Pros:** Matches existing OpenClaw installation pattern, easy updates via npm

#### Option B: Direct Installation Script
```bash
# Claude Code's official install script
curl -fsSL https://claude.ai/install.sh | bash
```

**Pros:** Gets latest version, handles dependencies

#### Option C: Manual Download
```bash
# Download specific version from GitHub releases
cd /tmp
wget https://github.com/anthropics/claude-code/releases/download/v0.2.x/claude-code-x.x.x-linux-x64.tar.gz
tar -xzf claude-code-*.tar.gz
sudo mv claude /usr/local/bin/
```

### 2.2 Post-Installation Configuration

**Create Claude Code config directory:**
```bash
mkdir -p ~/.config/claude
```

**Configuration file** (`~/.config/claude/config.json`):
```json
{
  "apiKey": "${ANTHROPIC_API_KEY}",
  "defaultModel": "claude-sonnet-4-20250514",
  "autoUpdate": true,
  "telemetryEnabled": false,
  "editor": {
    "preferred": "vim"
  }
}
```

---

## Phase 3: Integration with OpenClaw Ecosystem

### 3.1 Agent Architecture Design

```
┌─────────────────────────────────────────────────────────────┐
│                      DISCORD CHANNELS                       │
├──────────────┬──────────────┬────────────────┬───────────────┤
│ #alfred-main │ #alfred-ops  │ #dev-technical │ #claude-code  │
└──────┬───────┴──────┬───────┴───────┬────────┴───────┬───────┘
       │              │               │                │
       ▼              ▼               ▼                ▼
┌──────────┐  ┌──────────┐   ┌──────────────┐  ┌──────────┐
│  Alfred  │  │alfred-ops│   │ agent-support │  │ claude   │
│  (Main)  │  │          │   │    -lead      │  │  (Dev)   │
└────┬─────┘  └──────────┘   └───────────────┘  └────┬─────┘
     │                                                │
     │         ┌──────────────────────┐               │
     └────────►│   OpenClaw Gateway   │◄──────────────┘
               │   (Orchestration)    │
               └──────────────────────┘
                            │
                            ▼
                    ┌───────────────┐
                    │  VPS Host     │
                    │ Ubuntu 24.04  │
                    └───────────────┘
```

### 3.2 Claude Code Agent Configuration

**Agent Definition** (to add to OpenClaw agents):

```yaml
# Agent: claude-dev
name: claude-dev
role: Technical Development Agent
description: |
  Claude Code instance for technical/development work.
  Handles code reviews, debugging, architecture discussions,
  and hands-on development tasks.

model: claude-sonnet-4-20250514

systemPrompt: |
  You are Claude, a technical development agent integrated
  into Duane's OpenClaw environment. You work alongside
  Alfred (the chief of staff) and other specialized agents.

  Your focus:
  - Code review and analysis
  - Debugging and troubleshooting
  - Architecture and design discussions
  - Development task execution
  - Technical documentation

  When uncertain about business context or cross-functional
  coordination, escalate to Alfred or the appropriate agent.

capabilities:
  - exec
  - read
  - write
  - edit
  - browser
  - web_search
  - web_fetch

workspaces:
  - /home/duane/claude-code/projects
  - /home/duane/projects
  - /home/duane/git

# Spawn configuration
spawn:
  command: claude
  args: ["--session", "{{sessionKey}}"]
  workingDir: "{{projectDir || '/home/duane/claude-code/projects'}}"
```

### 3.3 Integration Points

#### A. Discord Channel Setup
Create or designate a channel for Claude Code:
- **Option 1:** New channel `#claude-code-dev`
- **Option 2:** Use existing `#dev-technical` or `#agent-support-lead`

#### B. Session Management
Claude Code sessions should be:
- Persistent for long-running development tasks
- Bound to specific projects
- Accessible via OpenClaw's session management

#### C. Handoff Protocol
Define when Alfred delegates to Claude Code:

| Trigger | Action |
|---------|--------|
| "Claude, review this code" | Spawn claude-dev session |
| "Debug this error" | Route to claude-dev |
| "Write a script to..." | Route to claude-dev |
| "Technical architecture question" | Route to claude-dev |
| "Business/process question" | Stay with Alfred |

---

## Phase 4: Tool and Capability Mapping

### 4.1 Claude Code Tool Access

Claude Code should have access to:

| Tool | Purpose | Notes |
|------|---------|-------|
| `read` | Read files | Full access to project directories |
| `write` | Create files | Within designated workspaces |
| `edit` | Modify files | With approval for sensitive files |
| `exec` | Run commands | Sandboxed or gated for safety |
| `browser` | Web research | For technical documentation |
| `web_search` | Search | Technical topics, Stack Overflow |
| `web_fetch` | Fetch content | API docs, GitHub repos |

### 4.2 Integration with Existing Tools

**Git Integration:**
```bash
# Claude Code should be able to:
git clone <repo>
git status
git diff
git commit
git push
```

**Docker Integration (if applicable):**
```bash
# Container management for development environments
docker build
docker run
docker-compose up
```

**Language Support:**
- Node.js/TypeScript (already available)
- Python (if installed)
- Go (if needed)
- Rust (if needed)
- Shell scripting

---

## Phase 5: Workflow Design

### 5.1 Common Development Workflows

#### Workflow A: Code Review
```
1. User shares code/PR in Discord
2. Alfred receives message
3. Alfred spawns claude-dev session
4. Claude Code:
   - Fetches the code
   - Analyzes structure and logic
   - Identifies issues/improvements
   - Provides structured review
5. Results posted back to Discord
6. Session closes or remains open for follow-up
```

#### Workflow B: Debugging Session
```
1. User describes error/symptom
2. Alfred routes to claude-dev
3. Claude Code:
   - Reads relevant files
   - Runs diagnostic commands
   - Searches for similar issues
   - Proposes fixes
4. Iterates with user until resolved
5. Documents solution in memory
```

#### Workflow C: Script/Tool Creation
```
1. User requests automation
2. Claude Code:
   - Designs approach
   - Writes initial implementation
   - Tests in safe environment
   - Delivers final script
3. Alfred reviews for operational fit
4. Deployed to appropriate location
```

### 5.2 Session Persistence Strategy

| Session Type | Duration | Persistence |
|--------------|----------|-------------|
| Quick Q&A | 5-15 min | Ephemeral, auto-close |
| Code review | 15-45 min | Ephemeral, results saved |
| Debugging | 30-120 min | Persistent until resolved |
| Development | Hours/days | Named session, project-bound |

---

## Phase 6: Security and Safety

### 6.1 Security Model

**Principle:** Claude Code operates with same security constraints as OpenClaw agents.

**Restrictions:**
- No access to `openclaw.json` or other secrets
- Cannot send email/post publicly without approval
- Cannot modify system configuration
- Sandbox for destructive operations

**Approval Gates:**
- File writes outside workspace require approval
- `exec` of sensitive commands requires approval
- Network requests to unknown endpoints require approval

### 6.2 Data Flow

```
User Request → Discord → OpenClaw Gateway → Claude Code Agent
                                               ↓
                                        Read/Write Files
                                        Execute Commands
                                               ↓
                                        Results → Discord
```

All actions logged for audit purposes.

---

## Phase 7: Testing and Validation

### 7.1 Pre-Deployment Testing

**Test Cases:**
1. Basic code review (read files, provide feedback)
2. File creation (write new script)
3. Command execution (run tests/build)
4. Web research (fetch documentation)
5. Error debugging (analyze logs)
6. Multi-file edits (refactoring)

### 7.2 Validation Checklist

- [ ] Claude Code installs successfully
- [ ] Can read files in workspace
- [ ] Can write files in workspace
- [ ] Can execute commands safely
- [ ] Integrates with Discord
- [ ] Respects OpenClaw security model
- [ ] Handoffs work correctly
- [ ] Sessions persist as expected

---

## Phase 8: Documentation and Maintenance

### 8.1 Documentation Updates

**Update these files:**
- `AGENTS.md` - Add claude-dev agent definition
- `MEMORY.md` - Add Claude Code usage patterns
- `TOOLS.md` - Document Claude Code commands
- Create `CLAUDE_CODE_USAGE.md` - User guide

### 8.2 Maintenance Procedures

**Weekly:**
- Check for Claude Code updates: `npm update -g @anthropics/claude-code`
- Review session logs for issues

**Monthly:**
- Audit security permissions
- Review and update system prompts
- Clean up old session files

---

## Implementation Timeline

| Phase | Duration | Tasks |
|-------|----------|-------|
| Phase 1 | 30 min | Prerequisites, API keys, directories |
| Phase 2 | 20 min | Installation, configuration |
| Phase 3 | 45 min | Agent setup, Discord integration |
| Phase 4 | 30 min | Tool configuration, permissions |
| Phase 5 | 30 min | Workflow testing |
| Phase 6 | 20 min | Security validation |
| Phase 7 | 45 min | Full testing |
| Phase 8 | 30 min | Documentation |

**Total Estimated Time:** ~4 hours

---

## Commands Summary

### Installation Commands
```bash
# Install Claude Code
npm install -g @anthropics/claude-code

# Verify
claude --version
```

### Configuration Commands
```bash
# Add to .bashrc
echo 'export ANTHROPIC_API_KEY="your-key"' >> ~/.bashrc

# Create directories
mkdir -p ~/claude-code/{projects,sessions,config}
```

### Daily Usage Commands
```bash
# Start Claude Code (direct)
claude

# Start with specific directory
claude --cwd ~/projects/my-repo

# OpenClaw spawn (via Discord)
/claude-dev "review this code: ..."
```

---

## Risk Mitigation

| Risk | Mitigation |
|------|------------|
| API rate limits | Monitor usage, have fallback model |
| Memory constraints | Configure swap, limit concurrent sessions |
| Security exposure | Strict tool permissions, approval gates |
| Integration issues | Test in isolation before Discord integration |
| Model availability | Configure fallback to other Claude models |

---

## Success Criteria

1. Claude Code responds to development requests via Discord
2. Can read/write files in designated workspaces
3. Can execute commands safely
4. Integrates cleanly with OpenClaw agent system
5. Handoffs between Alfred and Claude Code work smoothly
6. Security model respected (no unauthorized actions)
7. Performance acceptable (response time <30s for most tasks)

---

## Next Steps

1. Review and approve this plan
2. Obtain Anthropic API key (if not already configured)
3. Schedule implementation window
4. Execute Phase 1-2 (prerequisites and installation)
5. Test basic functionality
6. Proceed with OpenClaw integration
7. Document and hand over

---

*Plan created: 2026-06-16*
*For: Claude Code integration into VPS/OpenClaw environment*
*Owner: Alfred (main) → Handoff to claude-dev upon completion*
