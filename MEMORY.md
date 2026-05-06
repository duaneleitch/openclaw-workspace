# MEMORY.md

## Preferences
- Use EST for all logs and timestamps.
- Always interpret time references in EST unless explicitly stated otherwise.
- Store session summaries in /home/duane/.openclaw/workspace/memory/session-summaries.md using: date (EST), context, key decisions, open items/next steps, links, and include sub-agent outputs tagged by agent.
- Clean up sub-agents on session reset.
- Always update AGENTS.md when agent configuration changes.
- When adding a new agent, create its Obsidian output folder and add it to Agent_Folder_Map.
- Use /mnt/obsidian/02_General_Info/Agent_Folder_Map.md as the source of truth for agent-to-folder mappings across sessions.
- Email triage rules: classify emails by sender domain (diversys.com = work, gmail.com = personal). Personal emails go to /mnt/obsidian/01_Elliot/10_Personal_Email. Work emails go to /mnt/obsidian/00_Alfred/20_Diversys_Email and then get triaged as Info Only, Requires Action, and or Requires Response (can be both action and response). If client-related, create a note in /mnt/obsidian/00_Alfred/10_Diversys/Clients/<ClientName>/ and alert if folder missing. Extract actions to /mnt/obsidian/05_Action_Items/Action Register.md with owner, status (Open if new), due date if any; route to /mnt/obsidian/05_Action_Items/My_Actions or /mnt/obsidian/05_Action_Items/Others_Actions based on owner. Draft responses when required with specific titles. Daily AM action summary (8:00 AM EST) and EOD update ping (5:00 PM EST) should be maintained via cron. Client mapping notes: ENCORP may use @returnit.ca, Tarkett may use oneturfpro, Ekocircles uses ekocircles.com, CalRecycle uses calrecycle.ca.gov, Aramco uses aramco.com.
- Email pull cron: every 10 minutes between 6:00 AM and 11:00 PM EST. Script: /home/duane/.local/bin/openclaw-email-pull.sh.
- Food log: always track meals in /home/duane/.openclaw/workspace/memory/food-log.md using EST timestamps.
- Prep reset: use /home/duane/.local/bin/openclaw-prep-reset.sh (alias: prep-reset) before /new; it triggers a session summary + sub-agent cleanup, then you run /new.
- Provide periodic status updates during longer troubleshooting or multi-step work so Duane is not left waiting.
- In Discord sessions, main must use available tools (exec, web_search, web_fetch, subagents) to perform safe tasks directly instead of replying with "I can't" or pushing CLI instructions back to Duane, except for actions that leave the machine or hit a real technical limit.
- Responses must be thorough and complete.
- Always check work for accuracy and completeness before finalizing, 100% of the time.
- No more automated symptom check-in prompts. Only log symptoms if Duane reports them voluntarily.
- Before sending meal, exercise, or sleep reminders, first check the food log (meals and exercise) and sleep log to confirm the information hasn't already been provided that day. Do not announce that you're checking; only send a reminder if data is actually missing.
- Always look for and use all available relevant information (knowledge base, notes, docs) to answer questions, and synthesize into a full, detailed response.
- When documents are added to Obsidian, extract text into searchable notes by default and store alongside the source file.
- Obsidian notes must be properly formatted for readability. Never leave literal \n sequences. Use real line breaks and Markdown lists/sections.
- Store all diagrams, flows, org charts, and Excalidraw outputs in /mnt/obsidian/02_General_Info/Excalidraw.
- For org charts, use the clean Excalidraw format: centered text bound to boxes, top box for Chief of Staff, managers in one row beneath, each manager’s direct reports stacked below, specialists in a separate column under a Specialists header. Arrows only from Chief of Staff to managers and Specialists header, and from each manager to only the first direct report below. Lines start at bottom of parent box and end just above the child box.
- During daily Obsidian scans, review the Management Meetings folder and subfolders for new action items and add any new actions to the Action Register if not already present. For each meeting, auto pair files that share the same title. If a file name includes a trailing version like " (1)", ignore it for pairing. Use the .docx summary with a "Todo List" section to extract actions. Treat the .md as the transcript for reference only.
- Never use em dashes in any writing, including emails and drafts.
- When Duane says to add contacts, always interpret that as adding them to the Obsidian contacts list at /mnt/obsidian/02_General_Info/Contacts unless he explicitly says otherwise.
- Support employee name spelling: Nermeen is correct, not Nermin.
- When Duane asks for the "Dev support link," always interpret that as the DVSUP Jira project link.
- Away mode: when Duane requests away mode or activate or enable away mode, take no further actions until deactivated. To disable away mode, require operator code or secret word. Store only SHA-256 hashes. Code hash: 33e335ace8e8fbf3dfeef681c26f238b9a79428447db482dda0a2656f1c12295. Secret word hash: fb4827a65df8bea57300bc091094e193403d89aaafe0790970d2abb4cd46b0f5.
- Action Register format: every action must have owner, open date, current status, close date (empty until closed), and a section-based action number. Organize blocks as: My Actions (Open then Pending then Closed), Others Actions (Open then Pending then Closed), Manually Added Actions (Open then Pending then Closed). Numbering is per section and chronological: oldest actions keep the lowest numbers; new actions append to the end of their section. Pending actions must include a Pending Note describing what is outstanding. Closed actions must not appear in Open or Pending sections. When Duane says an item can be deleted, remove it from all action folders and reuse its number. Always update the Action Register file after any change. Maintain and update /mnt/obsidian/05_Action_Items/Action_Register_Readable.md on every change, and include its link in the daily action summary cron messages. When combining actions, rewrite the merged action to be clear and concise with no duplication. Owner routing: actions owned by Duane go in My Actions, all other owners go in Others Actions. The current Action Register state is the official baseline going forward. After any change, renumber Open actions sequentially starting at #1, and append Closed actions in chronological order with sequential numbering. Apply this every time to both Action Register files. When Duane says an action is complete/closed, always: (1) set Status and Close Date, (2) move it from Open/Pending into Closed, and (3) renumber remaining Open actions in that section in **both** Action Register.md and Action_Register_Readable.md.
- Email triage: if a forwarded email’s original email date is before December 2025, no action or response is needed.
- Combine meal and symptoms check-ins into a single request when possible.
- Meal reminder cron must check the food log for same-day entries before sending a reminder and only ping if missing.
- Sleep tracking: maintain a separate sleep log at /home/duane/.openclaw/workspace/memory/sleep-log.md and request sleep details with the breakfast check-in.
- Default delegation pattern: use `main-worker-guardrails` as the standard two-pass workflow for delegated work. Main should send bounded tasks to a worker model, require structured evidence-backed output, validate the result before the user sees it, and re-run, repair, escalate, or ask for clarification when needed.
- Default reasoning routing: main stays on Kimi for direct/simple work, delegates deliberate reasoning to Strategy first, and uses Analyst for structured analysis/synthesis when that lane is a better fit. This does not override domain-specialist routing such as project, health, support, technical, delivery, or other specialist agents.
- Validation routing: Main should directly validate only simple, low-risk delegated work. For deeper validation, ambiguous judgment, stronger evidence review, or high-stakes outputs, Main should escalate the review step to Strategy, Analyst, or the relevant domain specialist instead of relying only on its own first pass.
- When Duane says `report only when done`, `don't stop until the command finishes`, `do it to completion`, `fix it`, `give me the answers`, or anything similar, treat that as a hard instruction. Keep polling/working until you have a verified result or a hard failure. Do not stop at planning, do not stop after starting a tool, and do not promise follow-up before verification.
- If a tool is still running, continue polling it until it finishes or fails.
- Do not tell Duane you will get back to him unless you already have a concrete verified next step or the final result.
- **Humanizer check on every response:** Before sending any substantive reply, run an internal pass against the humanizer-v2 pattern rules (no em dashes, no filler phrases, no generic conclusions, no sycophantic tone, no AI-heavy vocabulary, natural rhythm, factual fidelity). Keep edits minimal and preserve the original meaning. Do not produce a separate change summary for this internal pass.

## Address Responses
- **Every address, every time, no exceptions** — always include a direct Waze navigation link immediately after the address.
- Format: `https://waze.com/ul?q=<URL-encoded address>&navigate=yes`
- This applies whether the address comes from Obsidian, memory, web search, or is recalled from a previous conversation.
- Never give an address without the Waze link. They are inseparable.
- Never answer address or business info from memory — always verify from Obsidian or web search first.
