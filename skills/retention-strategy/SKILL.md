---
name: retention-strategy
description: Guides customer retention and churn prevention strategy, including health scoring, segmentation, intervention playbooks, and lifecycle retention programs. Use when reducing churn, building retention programs, identifying at-risk customers, designing health score frameworks, creating intervention playbooks, improving onboarding retention, or analyzing voluntary vs involuntary churn patterns. Also use when asked about customer lifetime value, loyalty programs, dunning management, or retention metrics.
---

# Retention Strategy

Customer retention and churn prevention framework. Acquiring new customers costs 5-25x more than retaining; a 5% retention improvement can increase profitability 25-95%.

## Initial Assessment

Before producing output, assess the retention context:

1. **Churn type**: Voluntary (active cancel) vs involuntary (payment failure)
2. **Signals**: Login frequency, feature usage, support tickets, NPS/CSAT trends
3. **Stage**: Onboarding, adoption, expansion, renewal

## Churn Types

| Type | Share | Causes |
|---|---|---|
| Voluntary | 60-80% | Pricing, missing features, poor onboarding, relationship breakdown |
| Involuntary | 20-40% | Payment failures, expired cards, billing issues |

Most churn is predictable 30-90 days before cancellation via behavioral signals.

## Proactive vs Reactive

| Approach | Conversion Rate |
|---|---|
| Reactive (after cancel) | 15-20% |
| Proactive (before decision) | 60-80% |

Always prioritize early warning systems over win-back campaigns.

## Retention Strategies

- **Health scoring**: Behavioral + transactional + relationship signals
- **Loyalty programs**: 5-15 percentage point retention lift
- **Segmentation**: Predictive modeling for at-risk cohorts
- **Onboarding**: Prevent low value realization early
- **Dunning**: Retry logic + pre-expiry card updates for involuntary churn

## User Value and Feedback

- **Product value**: Registration, feature usage, payment
- **Marketing value**: Testimonials, customer stories, webinar guests, feedback, bug reports, feature requests
- **Feedback analysis**: Email, community, reviews; AI-assisted analysis; prioritize by impact; route to product vs ops

Avoid treating users only as MAU/registration denominators.

## Lifecycle Integration

Retention occurs after conversion and requires ongoing investment in customer success, not isolated campaigns.

Map touchpoints: onboarding -> adoption -> expansion -> renewal.

## Output Format

When producing a retention deliverable, include:

1. **Churn analysis**: Voluntary vs involuntary; key signals
2. **Retention tactics**: Organized by lifecycle stage
3. **Health score framework**: Indicators, weighting, thresholds (if applicable)
4. **Intervention playbook**: At-risk triggers and recommended actions

## Detailed References

- For health score design and intervention templates, see [references/health-scoring.md](references/health-scoring.md)
- For dunning and involuntary churn playbooks, see [references/dunning-playbook.md](references/dunning-playbook.md)

## Related Skills

- email-marketing: Onboarding sequences, win-back campaigns
- pmf-strategy: Retention as PMF signal; churn as anti-signal
- cold-start-strategy: First users; differs from retention
- analytics-tracking: Usage data, churn signals
- traffic-analysis: Attribution, retention cohort analysis