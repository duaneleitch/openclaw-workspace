# Health Score Framework

## What a Health Score Measures

A customer health score combines multiple signals into a single indicator of account stability and expansion potential.

## Signal Categories

### Behavioral Signals
- Login frequency (declining = risk)
- Feature adoption breadth (narrow = risk)
- Workflow completion rate (dropping = risk)
- Time-in-product trends

### Transactional Signals
- Contract value trends (shrinking = risk)
- Renewal proximity (approaching with no engagement = risk)
- Support ticket volume (spike = risk or deepening engagement)
- Payment history (failures = involuntary risk)

### Relationship Signals
- NPS/CSAT scores (declining = risk)
- Executive sponsor engagement (absent = risk)
- Product feedback volume (sudden silence = risk)
- Reference/willingness to advocate

## Weighting Guidance

| Category | Typical Weight |
|---|---|
| Behavioral | 40-50% |
| Transactional | 25-35% |
| Relationship | 15-25% |

Adjust weights based on your business model. Product-led growth leans heavier on behavioral; enterprise leans heavier on relationship.

## Threshold Design

| Score Range | Status | Action |
|---|---|---|
| 80-100 | Healthy | Nurture, expand |
| 60-79 | Watching | Monitor, check in |
| 40-59 | At Risk | Intervene within 7 days |
| 0-39 | Critical | Immediate outreach |

## Intervention Triggers

- Score drops 15+ points in 30 days
- Two consecutive periods below 60
- Key contact leaves or disengages
- Support ticket spike without resolution
- Feature usage drops below adoption threshold