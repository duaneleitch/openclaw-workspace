# 2026-07-20 Monday AI Process Remediation Plan

## Context
This note processes the 2026-07-20 call between Duane and Roger Barlow. The transcript is not just a status discussion. It defines a practical operating problem that needs to be solved in process, tooling, ownership, and automation.

The core issue is not simply that a customer received inaccurate release information. The deeper issue is that project-critical status is being managed across too many boards, too many manual updates, and too many disconnected systems. That creates lag, ambiguity, duplicate work, and customer-facing errors.

## What Actually Happened
For ENCORP, items were shown in Monday.com as committed to a release. The customer used that board as a source of truth for regression testing. At the last minute, some items were pulled from the release. Those changes were not reflected in the source-of-truth board quickly enough. As a result:
- Duane communicated a list that was accurate based on the board at the time
- the board itself was later changed after the customer had already acted on it
- the customer wasted testing effort on items that were not actually included
- the issue exposed a deeper process failure, not just a one-time communication miss

## Root Problems Identified in the Call
### 1. Source-of-truth lag
The release decision changed before the board changed.

### 2. Manual cross-system updates
Jira, Confluence, and Monday are not synchronized, so release and story changes rely on humans updating multiple places.

### 3. Missing traceability
Some Monday items do not have linked stories. Some customer requests do not cleanly map to Jira or Confluence work items.

### 4. Too many boards
The project is being managed across roughly seven active boards per customer, with legacy boards still creating clutter and confusion.

### 5. Weak release-gate validation
Customer-facing communication can be sent before final validation that board data matches actual release contents.

### 6. Ownership ambiguity
People are doing work inside a system they do not own, while Duane remains accountable for customer-visible accuracy.

## Decision-Level Interpretation
Roger's message is blunt but clear:
- manual updating is below the acceptable bar
- Monday should not be the place where truth is manually reconstructed
- Atlassian should be the operational source of truth
- Monday should be a downstream, customer-appropriate projection of that truth
- AI and agents should reduce manual coordination, not sit on top of broken manual workflows

## Required End State
### Operating model
- Jira and or Confluence hold primary engineering and release truth
- Monday becomes a presentation and project coordination layer, not a manual duplication layer
- customer-visible data is automatically updated from upstream systems
- every customer item has traceability to a story, release, and owner
- no customer-facing release communication goes out without automated or explicit validation

## Plan A: Simplify 7 boards into 3 boards
This is the recommended target model.

### Board 1: Integrated Project Board
Purpose: day-to-day delivery management for Duane and internal stakeholders.

Track in this board:
- milestones
- major workstreams
- dependencies
- action items
- decisions requiring follow-up
- owner
- due date
- status
- escalation flag
- customer impact flag

Suggested groups:
- Milestones
- Active Workstreams
- Open Decisions
- Open Actions
- Risks and Dependencies
- Closed

Suggested key columns:
- Item type
- Workstream
- Owner
- Status
- Due date
- Priority
- Dependency
- Escalation
- Customer-facing
- Linked Jira item
- Linked Confluence page
- Linked feedback item
- Last validated

### Board 2: Customer Feedback and Release Board
Purpose: customer-visible board for request tracking, release targeting, and testing readiness.

Track in this board:
- customer request or defect ID
- description
- release target
- release confidence
- linked Jira story
- linked upstream requirement or Confluence page
- test readiness
- actual shipped release
- status

Required rule:
No item can be marked committed unless a linked Jira issue exists.

Recommended release states:
- Proposed
- Planned
- In Build
- In QA
- Committed
- Shipped
- Deferred
- Blocked

Recommended confidence field:
- Low
- Medium
- High

Critical policy:
Use Planned until release inclusion is locked. Only move to Committed after release signoff.

### Board 3: Internal Risk and Governance Board
Purpose: internal-only board for risks, decisions, stakeholder concerns, and sensitive governance items.

Track in this board:
- risk ID
- risk statement
- trigger
- mitigation
- owner
- due date
- severity
- project impact
- status
- linked project item

This keeps sensitive items off customer-visible boards.

## Migration How-To: 7 Boards to 3 Boards
### Step 1: Inventory current boards
For each current board, capture:
- board name
- purpose
- audience
- whether customer-facing
- duplicate fields
- unique fields worth preserving
- board owner
- active vs legacy

### Step 2: Archive legacy boards
Archive boards that are informational only, stale, or superseded.
Do not migrate noise.

### Step 3: Export active board data
Export the active boards to CSV.
Use one worksheet per board if you consolidate in Excel first.

### Step 4: Normalize field names
Standardize fields such as:
- Owner
- Status
- Due Date
- Release
- Story ID
- Customer ID
- Risk Level
- Decision Needed

### Step 5: Use AI to propose merged structure
Prompt example:
"You are a Monday.com solution architect. I am consolidating seven project boards into three boards: an integrated project board, a customer feedback and release board, and an internal risk and governance board. Based on the attached CSV exports, recommend the target schema, deduplicate overlapping fields, map each current board to a target board, and identify which columns should remain internal-only."

### Step 6: Review manually
Do not let AI decide field mapping unchecked.
Validate:
- customer visibility boundaries
- mandatory identifiers
- release-related fields
- risk/privacy separation

### Step 7: Build target boards in Monday
Create the three boards and configure groups, columns, permissions, and views.

### Step 8: Import mapped data
Import cleaned CSVs.
Spot-check 10 to 20 representative items.

### Step 9: Freeze old boards
Set old boards to archived or read-only after cutover.

### Step 10: Publish board operating rules
Document:
- what belongs in each board
- who can update what
- what is system-synced vs manual-only
- what cannot be customer-visible

## Plan B: Jira/Confluence to Monday.com Sync Model
Recommended architecture:
- Jira = issue, sprint, release, workflow source of truth
- Confluence = requirements, notes, release context, supporting documentation
- Monday = project coordination and customer-friendly status projection

### Minimum field set to sync from Jira into Monday
For every synced item, bring across:
- Jira key
- summary
- status
- assignee
- priority
- target release or fix version
- updated date
- linked epic
- linked customer or program tag
- blocked flag
- QA status if available

### Additional fields that should exist upstream if missing
If these do not exist today, add them upstream:
- customer account
- customer-visible flag
- release confidence
- linked customer request or DFW number
- primary stakeholder
- deployment scope: customer-specific or platform-wide

### Confluence usage
Confluence should not be the only operational source for mutable delivery status. Use it for:
- requirement pages
- release notes context
- process documentation
- decision logs
- linked narrative that supports Jira items

### Sync rules
1. If a Jira issue changes release, Monday release field updates automatically.
2. If a Jira issue is removed from a release, Monday item status moves from Committed to Deferred or Planned automatically.
3. If a Monday item lacks a Jira key, it cannot show Committed.
4. If customer request exists without Jira issue, flag Missing Story Link.
5. If Jira item is updated after release lock cutoff, flag exception and notify owner.

## Agentic Automation Design
### Goal
Remove manual status propagation and replace it with governed sync plus exception handling.

### Agent responsibilities
#### Agent 1: Data Sync Agent
Runs on schedule or webhook.
Responsibilities:
- pull Jira issue updates
- pull release changes
- reconcile against Monday records
- update mapped Monday fields
- stamp last sync time

#### Agent 2: Traceability Agent
Responsibilities:
- find Monday items missing Jira links
- find customer requests missing story coverage
- find mismatched DFW to Jira mappings
- produce exception queue

#### Agent 3: Release Integrity Agent
Responsibilities:
- compare release candidate items vs Monday committed items
- flag items marked committed that are not in release
- flag release moves after lock date
- generate pre-release validation report

#### Agent 4: Executive Reporting Agent
Responsibilities:
- generate risk summary
- generate milestone status summary
- identify top 3 blockers
- prepare PowerPoint-ready outline or export

## Release Control Process
This is the process that would have prevented the ENCORP issue.

### T-3 to T-1 days before release
- Product finalizes candidate release set in Jira
- sync agent updates Monday automatically
- release integrity agent compares committed items to actual release set
- exceptions routed to Duane and Product owner

### Release lock
- Monday customer-facing board can only display Committed for items present in locked release set
- anything removed becomes Deferred automatically

### Before customer communication
Duane or PM must review one generated validation report:
- items committed
- items deferred since prior check
- items missing story links
- items changed after lock

### After release
- shipped release fields update from Jira/fixVersion or release tagging
- testing view in Monday reflects actual shipped items only

## Practical How-To for the DFW / customer-request linkage problem
### Required rule
Every customer request item needs one of the following:
- a linked Jira issue
- an explicit no-story-needed reason
- a flagged exception status

### If no clean match exists
Use a triage queue:
- New customer request
- Candidate story match found
- Needs product mapping
- Story created
- Linked and validated

### Mandatory fields
- Customer request ID or DFW number
- Customer name
- request summary
- linked Jira key
- linked release
- owner
- mapping confidence

This lets you see what has not yet been translated into product work.

## Recommendations
### Recommended path
1. Consolidate active boards to 3
2. Define Jira as source of truth for mutable release status
3. Add missing upstream fields for customer and release traceability
4. Implement automated sync before more manual cleanup
5. Add release integrity validation before customer communication
6. Stop manually sending extracted test lists unless they are system-generated from validated board state

### What to stop doing
- manually updating multiple boards with the same release facts
- marking items committed without linked Jira stories
- using Monday as a hand-maintained reconstruction of product truth
- sending customer test lists without final release validation

## Outputs to create next
1. Monday board field map
2. current-board-to-target-board migration matrix
3. Jira-to-Monday field mapping spec
4. release validation checklist
5. exception report template
6. stakeholder email template for corrective action and new process

## Suggested corrective-action email structure
- what happened
- impact to customer
- root cause
- corrective actions implemented
- ownership by role
- effective date
- validation mechanism before future customer communication

## Q&A Readiness Notes
After reading this note and the linked transcript, an agent should be able to answer:
- what failed in the ENCORP release communication process
- why seven boards is too many
- what the target three-board model should be
- why Jira should be the source of truth
- how Monday should be used after automation
- what fields must sync to prevent release errors
- how to detect missing customer-request to story links
- what release gating should happen before customer communication