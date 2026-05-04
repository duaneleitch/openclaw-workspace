# Dunning Playbook

## Involuntary Churn Prevention

Involuntary churn (payment failures, expired cards) accounts for 20-40% of total churn. It is the most preventable type.

## Pre-Expiry Card Updates

1. Send reminder 30 days before card expiry
2. Send reminder 14 days before card expiry
3. Send reminder 3 days before card expiry
4. Provide self-service card update link in every reminder

## Failed Payment Retry Logic

| Retry | Timing | Channel |
|---|---|---|
| 1st retry | Day 1 | Email + in-app banner |
| 2nd retry | Day 3 | Email + SMS |
| 3rd retry | Day 7 | Email + phone (high-value accounts) |
| 4th retry | Day 14 | Final notice email |
| Grace period end | Day 21-30 | Suspend access |

## Retry Optimization

- Retry on different days of the week (some cards succeed on payday)
- Retry on the 1st and 15th of the month (common payday dates)
- Use account updater services to get new card numbers automatically
- Track which retry patterns succeed for your customer base

## Communication Best Practices

- Lead with value received, not payment owed
- Keep the update process to 1-2 clicks
- Never shame or blame the customer
- Offer payment method alternatives (PayPal, bank transfer)
- For high-value accounts, assign a human to intervene before suspension

## Measurement

- Track recovery rate by retry attempt
- Track time-to-recovery distribution
- Compare involuntary churn rate before and after dunning improvements
- Monitor card updater hit rate