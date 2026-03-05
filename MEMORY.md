# MEMORY.md

## Preferences
- Use EST for all logs and timestamps.
- Always interpret time references in EST unless explicitly stated otherwise.
- Store session summaries in /home/duane/.openclaw/workspace/memory/session-summaries.md using: date (EST), context, key decisions, open items/next steps, links, and include sub-agent outputs tagged by agent.
- Clean up sub-agents on session reset.
- Always update AGENTS.md when agent configuration changes.
- When adding a new agent, create its Obsidian output folder and add it to Agent_Folder_Map.
- Use /mnt/obsidian/00_General_Info/Agent_Folder_Map.md as the source of truth for agent-to-folder mappings across sessions.
- Email triage rules: classify emails by sender domain (diversys.com = work, gmail.com = personal). Personal emails go to /mnt/obsidian/06_Personal_Email. Work emails go to /mnt/obsidian/07_Diversys_Email and then get triaged as Info Only, Requires Action, and or Requires Response (can be both action and response). If client-related, create a note in /mnt/obsidian/05_Diversys/Clients/<ClientName>/ and alert if folder missing. Extract actions to /mnt/obsidian/08_Action_Items/Action Register.md with owner, status (Open if new), due date if any; route to /mnt/obsidian/08_Action_Items/My_Actions or /mnt/obsidian/08_Action_Items/Others_Actions based on owner. Draft responses when required with specific titles. Daily AM action summary (8:00 AM EST) and EOD update ping (5:00 PM EST) should be maintained via cron. Client mapping notes: ENCORP may use @returnit.ca, Tarkett may use oneturfpro, Ekocircles uses ekocircles.com, CalRecycle uses calrecycle.ca.gov, Aramco uses aramco.com.
- Email pull cron: every 10 minutes between 6:00 AM and 11:00 PM EST. Script: /home/duane/.local/bin/openclaw-email-pull.sh.
- Food log: always track meals in /home/duane/.openclaw/workspace/memory/food-log.md using EST timestamps.
- Prep reset: use /home/duane/.local/bin/openclaw-prep-reset.sh (alias: prep-reset) before /new; it triggers a session summary + sub-agent cleanup, then you run /new.
- Provide periodic status updates during longer troubleshooting or multi-step work so Duane is not left waiting.
- Responses must be thorough and complete.
- Always check work for accuracy and completeness before finalizing, 100% of the time.
- Always look for and use all available relevant information (knowledge base, notes, docs) to answer questions, and synthesize into a full, detailed response.
- When documents are added to Obsidian, extract text into searchable notes by default and store alongside the source file.
- Obsidian notes must be properly formatted for readability. Never leave literal \n sequences. Use real line breaks and Markdown lists/sections.
- Store all diagrams, flows, org charts, and Excalidraw outputs in /mnt/obsidian/00_General_Info/Excalidraw.
- For org charts, use the clean Excalidraw format: centered text bound to boxes, top box for Chief of Staff, managers in one row beneath, each manager’s direct reports stacked below, specialists in a separate column under a Specialists header. Arrows only from Chief of Staff to managers and Specialists header, and from each manager to only the first direct report below. Lines start at bottom of parent box and end just above the child box.
- During daily Obsidian scans, review the Management Meetings folder and subfolders for new action items and add any new actions to the Action Register if not already present. For each meeting, auto pair files that share the same title. If a file name includes a trailing version like " (1)", ignore it for pairing. Use the .docx summary with a "Todo List" section to extract actions. Treat the .md as the transcript for reference only.
- Never use em dashes in any writing, including emails and drafts.
- Away mode: when Duane requests away mode or activate or enable away mode, take no further actions until deactivated. To disable away mode, require operator code or secret word. Store only SHA-256 hashes. Code hash: 33e335ace8e8fbf3dfeef681c26f238b9a79428447db482dda0a2656f1c12295. Secret word hash: fb4827a65df8bea57300bc091094e193403d89aaafe0790970d2abb4cd46b0f5.
- Action Register format: every action must have owner, open date, current status, close date (empty until closed), and a section-based action number. Organize blocks as: My Actions (Open then Pending then Closed), Others Actions (Open then Pending then Closed), Manually Added Actions (Open then Pending then Closed). Numbering is per section and chronological: oldest actions keep the lowest numbers; new actions append to the end of their section. Pending actions must include a Pending Note describing what is outstanding. Closed actions must not appear in Open or Pending sections. When Duane says an item can be deleted, remove it from all action folders and reuse its number. Always update the Action Register file after any change. Maintain and update /mnt/obsidian/08_Action_Items/Action_Register_Readable.md on every change, and include its link in the daily action summary cron messages. When combining actions, rewrite the merged action to be clear and concise with no duplication. Owner routing: actions owned by Duane go in My Actions, all other owners go in Others Actions. The current Action Register state is the official baseline going forward. After any change, renumber Open actions sequentially starting at #1, and append Closed actions in chronological order with sequential numbering. Apply this every time to both Action Register files.
- Email triage: if a forwarded email’s original email date is before December 2025, no action or response is needed.
- Combine meal and symptoms check-ins into a single request when possible.
- Meal reminder cron must check the food log for same-day entries before sending a reminder and only ping if missing.
- Sleep tracking: maintain a separate sleep log at /home/duane/.openclaw/workspace/memory/sleep-log.md and request sleep details with the breakfast check-in.
