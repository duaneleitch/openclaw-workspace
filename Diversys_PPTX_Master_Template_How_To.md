# Diversys PowerPoint Master Template – How To Use It

This guide explains how to use the Diversys master template when you (or Alfred) create new slide decks.

---

## 1. Where the Master Template Lives

**File:** `Diversys_Master_Template_v1.pptx`  
**Folder:** `/mnt/obsidian/20_PowerPoint/Templates/`

Treat this file as **read-only**. Always create a copy for a specific presentation.

---

## 2. What The Template Contains

The master is based on the AI Support Agent deck with Diversys styling applied:

- **Slide size:** 16:9 widescreen
- **Title style:**
  - Centered title, Archivo, **38 pt**, brand color
  - Consistent top margin across slides
- **Footer bar (content slides):**
  - Navy bar along the full width at the bottom
  - Centered white text ("Temp" by default, can be replaced with date/tagline)
- **First slide:**
  - Full-bleed hero image with Diversys branding
  - Editable **"Temp"** text block in the lower middle (date placeholder)
- **Content slides:**
  - Branded title + body layouts
  - Colors, fonts, and spacing aligned with Diversys brand rules

You can build almost any Diversys deck from this starting point.

---

## 3. Creating a New Deck From the Master (Manual)

When you build a new presentation yourself:

1. **Copy the master file**
   - In your file system:  
     Copy `Diversys_Master_Template_v1.pptx` to:
     
     `/mnt/obsidian/20_PowerPoint/Presentations/<New_Deck_Name>.pptx`
   - Example:  
     `/mnt/obsidian/20_PowerPoint/Presentations/Customer_Onboarding_Strategy_v1.pptx`

2. **Open the new deck in PowerPoint**

3. **Update the title slide**
   - Change the main title text (e.g., "CUSTOMER ONBOARDING STRATEGY")
   - Click the **Temp** text block in the lower middle of the slide and replace it with:
     - The date, or
     - A short context line (e.g., "Q2 2026", "CalRecycle E-Waste", etc.)

4. **Update or replace content slides**
   - Reuse the existing content layouts (titles + bullets) for:
     - Executive summary
     - Objectives
     - Current state
     - Roadmap, etc.
   - For each slide:
     - Edit the title directly in the title placeholder
     - Edit or replace the bullet/paragraph content in the body placeholder
   - All slides will preserve:
     - Title styling (38 pt, centered)
     - Footer bar and footer text styling

5. **Adjust the footer text as needed**
   - On content slides, the footer text defaults to **Temp**
   - You can replace this with:
     - The presentation title
     - A short tagline
     - A date range
   - Change once and then duplicate slides to reuse it.

6. **Save and use**
   - Keep `_v1`, `_v2` etc. to track versions as you iterate.

---

## 4. Creating a New Deck Using Alfred

When you want Alfred to build the deck for you, use a prompt like this:

> Use `Diversys_Master_Template_v1.pptx` in `/mnt/obsidian/20_PowerPoint/Templates` as the base.  
> Create a new deck named `Customer_Onboarding_Strategy_v1.pptx` in `/mnt/obsidian/20_PowerPoint/Presentations`.  
> Apply the same styling as the master (title size, footer, fonts, colors).  
> Here is the slide content:
> 1. Title slide – title: `Customer Onboarding Strategy`, Temp/date text: `April 2026`  
> 2. Executive Summary – bullets: `...`  
> 3. Objectives – bullets: `...`  
> 4. Current State – bullets: `...`  
> 5. Roadmap – bullets: `...`

What Alfred will do:

1. Copy the master template to create `<Your_Deck_Name>.pptx` in the Presentations folder.
2. Update slide 1 with your title and Temp/date text.
3. Build the remaining slides using the existing title/body/footer layouts and Diversys brand styling.
4. Avoid touching or overwriting `Diversys_Master_Template_v1.pptx`.

---

## 5. When You Want to Evolve the Template

As we refine the brand look over time, we should:

1. **Update the master carefully**
   - Open `Diversys_Master_Template_v1.pptx`
   - Adjust fonts, colors, spacings, or hero slide once
   - Save as a **new version**, for example:  
     `Diversys_Master_Template_v2.pptx`

2. **Switch future decks to the new master**
   - In your prompts, start referencing `Diversys_Master_Template_v2.pptx`
   - Leave older decks on v1 unless you explicitly ask to restyle them.

3. **Keep a short changelog** (optional but helpful)
   - In a note (e.g., `20_PowerPoint/Template_Changelog.md`), track:
     - Date
     - Template version
     - Changes (e.g., "Increased title size to 38 pt", "Updated hero image", etc.)

---

## 6. Quick Checklist When Starting a New Deck

1. Copy the master:  
   `Diversys_Master_Template_v1.pptx` → new file in `Presentations/`
2. Rename the file with a clear topic + version.
3. Update the title slide text + Temp/date.
4. Fill in or duplicate content slides and edit titles/bullets.
5. Check:
   - Titles are centered and readable
   - Footer bar is full width and text is centered
   - Temp/date or footer text is correct
6. Save and, if needed, ask Alfred to do a final pass for consistency.

---

If you’d like, I can next: (a) create a `Template_Changelog.md` alongside this, and (b) strip AI-specific text from a copy of the master so you have a truly blank Diversys template with the same layouts.