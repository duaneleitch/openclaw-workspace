## Purpose
A low-noise heartbeat configuration for OpenClaw. Use this file when you want proactive support without frequent interruptions. On each heartbeat, do a quick scan, notify only when something important changed, otherwise stay quiet (`HEARTBEAT_OK` behavior is expected in many setups).

## Core Rules
- Be proactive, not chatty.
- Prefer lightweight checks first.
- If nothing important changed, stay quiet.
- Batch low-priority items into the next heartbeat.
- Use concise, structured updates only when action is needed.
- Do not include secrets in this file.

## What Counts as Important (Notify)
Send a heartbeat update only if one or more of these are true:
1. An urgent deadline or commitment is due soon (within 24 hours)
2. A customer risk / escalation likely needs same-day attention
3. A leadership follow-up is at risk of being missed
4. A material KPI or operating signal worsened (if data exists)
5. A blocked item needs a decision, approval, or missing input

## What to Check Each Heartbeat (Fast Scan)
### 1) Urgency and Deadlines
Check for:
- due soon commitments
- missed follow-ups
- urgent requests
- obvious blockers

If found:
- send a short alert with recommended next step

### 2) Open Loops
Check for:
- promised follow-ups not completed
- drafts waiting on review
- decisions waiting on owner confirmation
- unresolved risk items

If found and important:
- batch into a short follow-up summary

### 3) Upcoming Prep Needs (if calendar/task access exists)
Check for:
- meetings requiring prep today / tomorrow
- deadlines before next review cycle
- missing materials for important reviews

If prep is needed:
- send a short prep brief (objective, decisions, what to prepare)

### 4) Customer Outcomes Signals (if data sources exist)
Quick scan for:
- escalation spikes
- onboarding delays
- adoption weakness
- retention risk indicators

Only notify if the signal appears material.

## Daily Mini Brief (Once Per Day, Business Hours)
If no urgent issue exists, optionally send one short daily operator brief:
- Top 1 to 3 focus items
- Top risk or blocker
- One recommended proactive move

Keep this very short.

## Weekly Mini Review (First Business Day Heartbeat)
Once per week, send a lightweight summary:
- top priorities this week
- biggest risk signal
- key follow-ups
- one process or alignment improvement suggestion

Do not generate a long report unless requested.

## Notification Format (Use This)
When notifying, keep it tight:
- **What changed**
- **Why it matters**
- **Next action**
- **Due / timing**
- **Assumptions** (if needed)

## Agent Usage During Heartbeat (Lite)
Stay lightweight by default.
- Use main agent only for basic checks and short summaries
- Spawn specialists only when there is a clear signal:
- `retainforge` for customer risk / adoption / retention
- `deliverygrid` for onboarding / implementation process issues
- `signalbridge` for handoff / pre-to-post sales issues
- `metricpilot` for KPI changes / trends / RCA
- `execpen` only if a polished leadership update is needed
- `ironcheck` only for high impact recommendations

## Noise Control
### Send immediately
- urgent within 24h
- customer escalation risk
- blocked priority work
- leadership commitment at risk

### Batch
- non-urgent follow-ups
- optional improvements
- documentation hygiene
- low-severity observations

### Stay quiet
- no material changes
- only informational noise
- incomplete signal with low confidence and no urgency

## Business Context Defaults (for this workspace)
Optimize heartbeat behavior for:
- executive operator support
- customer outcomes and retention
- operational excellence
- cross-functional follow-through
- practical action over status chatter

## Environment Placeholders (Fill In)
- Time zone: America/Toronto
- Business hours start: `8:00 a.m.`
- Business hours end: `5:00 p.m.`
- Weekend behavior: `Urgent only`
- Morning brief time: `8:00 a.m.`
- Daily brief enabled: `no`
- Weekly mini review enabled: `no`

## Maintenance Rule
Update this file when:
- heartbeat is too noisy
- heartbeat misses important things
- new data sources are connected
- alert timing preferences change
