# AI Support Agent Strategy Report for Diversys

## Executive Summary
Diversys can deploy an AI Support Agent to extend coverage outside business hours, improve response speed for international clients, and scale support without immediate headcount growth. With low current ticket volume, the primary value is readiness for growth, 24x5 or 24x7 coverage, faster first response, and consistent answers. The AI agent should operate with human escalation, strict guardrails, and full audit logging to protect client trust and data privacy.

Recommended approach: a three phase rollout over eight months with a controlled pilot, then scale. Focus on Zendesk and chat first, then deeper Jira integration.

## Company Context and Fit
Diversys provides recycling management software with compliance, reporting, and data integrity at the core. The company highlights AI capabilities in its product positioning. An AI Support Agent aligns with that posture and supports a modern customer experience standard, while creating operational leverage as volume grows.

Public positioning signals:
- Operational data accuracy and compliance
- High trust ecosystems
- Growth and global reach

Source: https://www.diversys.com/

## Objectives
Primary objectives:
- After hours coverage from 5:00 p.m. to 9:00 a.m.
- Faster first response and triage
- Scale support without adding headcount immediately
- Consistent knowledge delivery and reduced rework

Secondary objectives:
- Capture recurring issues and trends
- Improve knowledge base quality and reuse
- Reduce escalation delays

## Current State Assumptions
- Support team: one person
- Ticket volume: fewer than 10 per month
- Channels: email and chat
- Tools: Zendesk and Jira
- Current average time to first response: 20 minutes

## What the AI Support Agent Is
A controlled, multi channel assistant that:
- Answers common support questions
- Triage and classifies tickets
- Retrieves relevant knowledge base content
- Escalates complex or sensitive issues to a human
- Logs all interactions for QA and audit

## How It Works at Diversys
### Channels
- Zendesk for email tickets
- Chat integration
- Jira for escalation and engineering handoff

### Typical flow
1) Incoming ticket or chat
2) AI agent attempts answer using approved knowledge sources
3) If confidence is high, respond with guidance and resolution steps
4) If confidence is low, tag and escalate to human
5) Create or link a Jira issue when needed
6) Log all interactions for QA

## Benefits
### 1) Scale without immediate headcount growth
- Pilot safely at low volume
- Avoid backlog as volume increases

### 2) Faster response and improved coverage
- Immediate first response after hours
- Better experience for international time zones

### 3) Consistency and quality
- Standardized answers
- Reduced variance across shifts and new hires

### 4) Better knowledge management
- Identifies knowledge gaps
- Converts tribal knowledge into reusable assets

## Security and Trust Considerations
Security is critical for Diversys. Recommended approach:
- Data minimization in prompts
- No sensitive data sent to external LLMs without contractual assurance
- Restrict AI to approved knowledge base content
- Full audit logs of all AI responses
- Human in the loop for sensitive categories

Risk controls:
- Confidence thresholds for auto response
- Escalation for low confidence or sensitive keywords
- Admin approval for new knowledge entries
- Scheduled review of high impact responses

## Cost Considerations and Ranges
These are directional ranges. Actual costs depend on volume, model choice, and tooling.

### Platform and tooling
- AI orchestration platform: $3,000 to $25,000 per year
- Knowledge base and connectors: $1,000 to $10,000 per year
- Zendesk and Jira integration: low to moderate integration cost

### LLM usage
- Low volume likely under $200 to $500 per month
- Higher volume could reach $1,000 to $3,000 per month

### Implementation and support
- Initial implementation: $15,000 to $60,000
- Ongoing tuning and governance: $1,000 to $5,000 per month

## Comparison to Hiring
Hiring one additional support resource:
- Fully loaded cost often $80,000 to $120,000 per year
- AI agent can operate 24x5 or 24x7 for a fraction of that cost
- AI does not replace human support but reduces pressure on hiring timelines

## Roadmap and Timeline
Target: eight months total with clear go or no go gates.

### Phase 1: Discovery and design, 4 to 6 weeks
- Define use cases and escalation rules
- Audit knowledge base quality
- Establish data handling and security policy

### Phase 2: Pilot, 8 to 10 weeks
- Limited scope, after hours only
- Zendesk and chat integration
- Measure response speed, deflection rate, and QA

### Phase 3: Scale, 12 to 16 weeks
- Expand coverage and confidence thresholds
- Add Jira escalation automation
- Improve knowledge base coverage

## KPIs for Board Oversight
- First response time
- After hours coverage rate
- Deflection rate
- Resolution time
- Customer satisfaction
- Escalation accuracy
- Knowledge base coverage and freshness

## Risks and Mitigations
1) Wrong answers
- Mitigation: confidence thresholds, limited domain, strict knowledge sources

2) Security exposure
- Mitigation: data minimization, no sensitive data in prompts, audit logs

3) Low adoption
- Mitigation: transparent customer messaging, clear escalation path, internal training

## Strategic Recommendation
Proceed with a phased AI Support Agent rollout. This creates scalable support coverage without immediate headcount growth and positions Diversys as an innovation forward partner.

## Decision Request for the Board
Approve a phased pilot with a defined investment range and a go or no go gate after the pilot.

## Next Steps
1) Confirm desired coverage level and KPI targets
2) Select AI platform and integration approach
3) Begin discovery and knowledge base audit
4) Launch pilot and report metrics to leadership
