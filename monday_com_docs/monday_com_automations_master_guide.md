# Monday.com Automations - Master Guide for Support Agents

## Document Information
- **Version**: 1.0
- **Last Updated**: June 2026
- **Purpose**: Comprehensive training resource for support agents
- **Scope**: End-user automation features, notification settings, and board-level configurations

---

## Table of Contents

1. [Overview of Monday.com Automations](#1-overview-of-mondaycom-automations)
2. [Automation Concepts](#2-automation-concepts)
3. [Pre-built Automation Recipes](#3-pre-built-automation-recipes)
4. [Creating Custom Automations](#4-creating-custom-automations)
5. [Notification Configuration](#5-notification-configuration)
6. [Board-Level Automation Management](#6-board-level-automation-management)
7. [Triggers Reference](#7-triggers-reference)
8. [Actions Reference](#8-actions-reference)
9. [Troubleshooting](#9-troubleshooting)
10. [FAQ](#10-faq)

---

## 1. Overview of Monday.com Automations

### What Are Automations?
Monday.com automations are workflow rules that automatically perform actions when specific conditions are met. They help teams:
- Reduce manual repetitive tasks
- Ensure consistent processes
- Keep team members informed
- Maintain data accuracy

### Key Features
- **No-code builder**: Create automations without programming
- **Pre-built recipes**: Use templates for common scenarios
- **Custom workflows**: Build tailored automations
- **Cross-board support**: Connect multiple boards
- **AI-powered**: Advanced automation capabilities

### Plan Limitations
| Plan | Automation Limits |
|------|-------------------|
| Free | Limited per board |
| Basic | Increased limits |
| Standard | Higher limits |
| Pro/Enterprise | Unlimited or very high limits |

---

## 2. Automation Concepts

### The Automation Formula
Every automation follows this structure:
```
[TRIGGER] + [CONDITION (optional)] -> [ACTION]
```

**Example**:
- **Trigger**: When status changes
- **Condition**: And only if priority is High
- **Action**: Notify the assigned person

### Triggers
Events that start the automation:
- Status changes
- Date arrives
- Item created
- Column updated
- Person assigned
- Time-based triggers

### Conditions
Optional filters that control when the automation runs:
- Status equals/is not
- Priority level
- Date comparisons
- Assignment checks

### Actions
What happens when the trigger fires:
- Send notifications
- Update columns
- Create items
- Move items
- Send emails
- Integration actions

---

## 3. Pre-built Automation Recipes

### Recipe Categories

#### Status Change Recipes
| Recipe Name | Use Case |
|-------------|----------|
| When status changes to X, notify Y | Alert team when work progresses |
| When status changes to X, create item | Auto-create follow-up tasks |
| When status changes to X, move item | Organize completed work |
| When status changes to X, archive item | Auto-archive finished items |

#### Date-Based Recipes
| Recipe Name | Use Case |
|-------------|----------|
| When date arrives, notify someone | Deadline reminders |
| When date arrives, change status | Auto-update on due dates |
| Every day at X time | Daily recurring tasks |
| When date arrives and status is X | Conditional deadline alerts |

#### Assignment Recipes
| Recipe Name | Use Case |
|-------------|----------|
| When person is assigned, notify them | Alert assignees |
| When person is assigned, set date to today | Track assignment time |
| When item is created, assign someone | Auto-route new work |

#### Notification Recipes
| Recipe Name | Use Case |
|-------------|----------|
| When any column changes, notify someone | Track all updates |
| When status changes, notify the team | Keep everyone informed |
| When item is created, notify someone | Alert on new items |
| Send email notification on trigger | External notifications |

### Using a Recipe

1. Navigate to your board
2. Click "Automate" (top right)
3. Select "Browse pre-made recipes"
4. Choose a category or search
5. Click a recipe to customize
6. Fill in underlined variables
7. Click "Add to board"

---

## 4. Creating Custom Automations

### Step-by-Step Process

#### Step 1: Access Automation Center
1. Open your Monday.com board
2. Click "Automate" button (top right)
3. Select "Create custom automation"

#### Step 2: Select Trigger
Common triggers:
- When status changes
- When date arrives
- When item created
- When column changes
- When person assigned
- Every time period

#### Step 3: Add Conditions (Optional)
Filter when automation runs:
1. Click "Add condition"
2. Select condition type
3. Configure parameters
4. Test logic

#### Step 4: Select Actions
Common actions:
- Notify someone
- Send email
- Change status
- Create item
- Move item
- Assign person
- Set date

#### Step 5: Configure Variables
- Click underlined placeholders
- Select specific values
- Use dynamic variables when available

#### Step 6: Save and Activate
1. Name your automation
2. Click "Create automation"
3. Toggle on/off as needed

### Best Practices
- **Name clearly**: Use descriptive names like "Notify PM when High priority items completed"
- **Test first**: Create test items to verify automation works
- **Start simple**: Build basic automations before complex ones
- **Document**: Keep notes on what each automation does

---

## 5. Notification Configuration

### Email Notification Setup

#### Daily Digest Configuration
1. Click profile picture (top right)
2. Select "Notifications"
3. Configure email preferences:
   - Daily digest: Summary once per day
   - Weekly digest: Summary once per week
   - Instant: Real-time for important events
   - None: Disable emails

#### Board-Specific Notifications
1. Open specific board
2. Click "Bell" icon
3. Configure:
   - Subscribe/unsubscribe from board
   - Choose notification frequency
   - Select event types

### Notification Types

| Type | Description |
|------|-------------|
| Item assignments | When assigned to you |
| Status changes | When subscribed items change status |
| Due dates | Approaching or past due |
| Mentions | When @mentioned in comments |
| Updates | Changes to subscribed items |
| Replies | Responses to your comments |

### Notification Channels
- **Email**: Sent to registered email
- **In-app**: Within Monday.com interface
- **Desktop**: Browser notifications
- **Mobile**: Push notifications (app required)
- **Slack/Teams**: Integration notifications

---

## 6. Board-Level Automation Management

### Accessing Board Automations
1. Navigate to board
2. Click "Automate" button
3. View Automation Center

### Managing Automations

#### View Active Automations
- See all automations for the board
- Check activation status
- View run history

#### Enable/Disable
- Toggle switch to activate/deactivate
- Useful for temporary pauses
- Does not delete configuration

#### Edit Automations
1. Click automation name
2. Modify trigger/action/condition
3. Save changes

#### Delete Automations
1. Find automation in list
2. Click delete icon
3. Confirm deletion

#### Copy/Duplicate
1. Find automation
2. Click duplicate
3. Modify as needed
4. Save new version

### Cross-Board Automations

#### Creating Cross-Board Actions
1. Create automation on source board
2. Select action: "Create item in [board]"
3. Map columns between boards
4. Configure data flow

#### Use Cases
- Auto-create tasks in project board from sales board
- Sync data between related boards
- Escalate items to different teams

---

## 7. Triggers Reference

### Item-Based Triggers

| Trigger | Description | Use Case |
|---------|-------------|----------|
| When item created | New item added to board | Auto-assign, set dates |
| When item moved to group | Item changes groups | Reorganize, notify |
| When column changes | Any column updated | Track all changes |
| When status changes | Status column updated | Workflow progression |
| When person assigned | Assignment column updated | Notify assignees |
| When date arrives | Date column reaches value | Deadlines, reminders |
| When date changes | Date column modified | Reschedule alerts |
| When item archived | Item moved to archive | Cleanup notifications |
| When item deleted | Item removed | Backup triggers |

### Time-Based Triggers

| Trigger | Description | Use Case |
|---------|-------------|----------|
| Every day at X | Daily recurring | Daily summaries |
| Every week on X | Weekly recurring | Weekly reports |
| Every month on X | Monthly recurring | Monthly reviews |
| When date arrives | Specific date reached | Deadlines |
| When date arrives and status is X | Conditional deadline | Status-aware reminders |

### Communication Triggers

| Trigger | Description | Use Case |
|---------|-------------|----------|
| When someone mentions you | @name in comment | Direct alerts |
| When new comment added | Any comment | Activity tracking |
| When file uploaded | Attachment added | Document notifications |

### Sub-Item Triggers

| Trigger | Description | Use Case |
|---------|-------------|----------|
| When sub-item created | Child item added | Parent updates |
| When sub-item status changes | Child status updated | Progress tracking |
| When sub-item date arrives | Child deadline | Parent reminders |

---

## 8. Actions Reference

### Notification Actions

| Action | Description | Parameters |
|--------|-------------|------------|
| Notify someone | In-app notification | Person/team, message |
| Send email | Email notification | Recipients, subject, body |
| Send Slack message | Slack integration | Channel, message |
| Send Teams message | MS Teams integration | Channel, message |

### Item Actions

| Action | Description | Parameters |
|--------|-------------|------------|
| Create an item | New item in board | Board, column values |
| Create sub-item | Child item | Parent item, values |
| Move item to group | Change group | Target group |
| Move item to board | Transfer to different board | Target board, mappings |
| Archive item | Move to archive | - |
| Delete item | Remove permanently | - |
| Duplicate item | Copy existing | - |
| Change item name | Update name | New name |

### Column Actions

| Action | Description | Parameters |
|--------|-------------|------------|
| Change status | Update status column | New status value |
| Set date to today | Current date | Date column |
| Change date | Set specific date | Date column, value |
| Assign person | Update person column | Person to assign |
| Change priority | Update priority column | Priority level |
| Change label/tags | Update labels | Tag values |
| Change text | Update text column | New text |
| Change numbers | Update numeric column | New value |
| Change dropdown | Update dropdown | Selected option |

### Integration Actions

| Action | Description | Use Case |
|--------|-------------|----------|
| Send webhook | HTTP request | External systems |
| Create ticket | In external system | Support workflows |
| Post to social | Social media update | Marketing |
| Send form response | Form submission | Data collection |

---

## 9. Troubleshooting

### Common Issues

#### Automation Not Triggering
**Symptoms**: Automation doesn't run when expected

**Solutions**:
1. Check if automation is enabled
2. Verify trigger conditions are met
3. Confirm user has permissions
4. Check automation limits (plan restrictions)
5. Review column names haven't changed

#### Notifications Not Sending
**Symptoms**: Users don't receive notifications

**Solutions**:
1. Check notification preferences
2. Verify email address is correct
3. Check spam/junk folders
4. Confirm user is subscribed to board/item
5. Review notification frequency settings

#### Automation Running Too Often
**Symptoms**: Multiple notifications/duplicate actions

**Solutions**:
1. Add conditions to filter triggers
2. Check for duplicate automations
3. Review trigger specificity
4. Add "only if" conditions

#### Cross-Board Automation Not Working
**Symptoms**: Items not created in target board

**Solutions**:
1. Verify board permissions
2. Check column mapping
3. Confirm target board exists
4. Review automation limits

### Error Messages

| Error | Meaning | Solution |
|-------|---------|----------|
| "Automation limit reached" | Plan restriction | Upgrade plan or delete old automations |
| "Column not found" | Column renamed/deleted | Update automation with new column name |
| "User not found" | Person no longer in workspace | Update automation with active user |
| "Permission denied" | Insufficient rights | Check board/team permissions |

### Debugging Steps

1. **Verify trigger**: Manually trigger the event (e.g., change status)
2. **Check conditions**: Confirm all conditions are met
3. **Review permissions**: Ensure automation owner has rights
4. **Test with simple automation**: Create basic automation to test
5. **Check run history**: View automation execution logs

---

## 10. FAQ

### General Questions

**Q: How many automations can I create?**
A: Depends on your plan. Free has limited automations, Pro/Enterprise have unlimited or very high limits.

**Q: Can I automate across different workspaces?**
A: Cross-board automations work within the same workspace. Cross-workspace requires API/integration.

**Q: Do automations work on mobile?**
A: Yes, automations run server-side and work regardless of how items are created/modified.

**Q: Can I import/export automations?**
A: Not directly, but you can duplicate boards with their automations.

### Notification Questions

**Q: Why am I not receiving email notifications?**
A: Check notification preferences, spam folders, and ensure you're subscribed to relevant boards/items.

**Q: Can I customize notification emails?**
A: Yes, when using "Send email" action, you can customize subject and body.

**Q: How do daily digests work?**
A: Daily digests summarize activity from the past 24 hours and send at your configured time.

### Technical Questions

**Q: Can automations trigger other automations?**
A: Yes, if Automation A creates an item, it can trigger Automation B that watches for new items.

**Q: Are there automation logs?**
A: Yes, check the automation center for run history and status.

**Q: Can I use formulas in automations?**
A: Formula columns can be triggers, but cannot be directly modified by automations.

### Troubleshooting Questions

**Q: My automation stopped working. What happened?**
A: Check if columns were renamed, users removed, or plan limits reached.

**Q: Can I test an automation before enabling?**
A: Create test items and run through trigger manually to verify.

**Q: How do I get help with automations?**
A: Check Monday.com Help Center, community forums, or contact support.

---

## Quick Reference Card

### Creating Your First Automation
1. Click "Automate" on board
2. Choose "Browse recipes" or "Create custom"
3. Select trigger
4. Add conditions (optional)
5. Select action
6. Configure variables
7. Name and save

### Setting Up Daily Notifications
1. Create custom automation
2. Trigger: "Every day at [time]"
3. Action: "Send email" or "Notify"
4. Configure recipients and message
5. Save and enable

### Common Automation Patterns
- Status change -> Notify team
- Date arrives -> Send reminder
- Item created -> Assign person
- Priority High -> Notify manager
- Weekly -> Send digest

---

## Resources

### Official Links
- Help Center: https://support.monday.com
- Developer Docs: https://developer.monday.com
- Academy: https://academy.monday.com
- Community: https://community.monday.com

### External Resources
- YouTube: Search "Monday.com automation tutorial"
- Reddit: r/mondaydotcom
- Blog: https://monday.com/blog

---

*End of Master Guide*
*For updates, check the official Monday.com documentation*
