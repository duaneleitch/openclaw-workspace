---
name: pptx-brand-style
description: Apply Diversys brand styling to PowerPoint decks (colors, typography, spacing, section headers, and layout rules). Use when creating or restyling PPTX decks to match brand guidelines and produce more polished, visual slides.
---

# PowerPoint Brand Styling Skill

Apply the Diversys brand system to PPTX decks. This skill standardizes color palette, typography, spacing, and slide layout patterns for consistent, polished visuals.

## Core Rules
- Use pure white background for all slides: #FFFFFF
- Apply brand colors from references/brand-colors.md
- Use the font hierarchy in references/typography.md
- Prefer 2-column layouts for dense slides
- Convert long bullet lists into 3–5 visual blocks
- Add a section divider line beneath each section title
- Default content slide layout includes a curved navy panel and a full-width footer bar

## Slide Patterns
### Title Slide
- Full-bleed photo with Deep Blue overlay at 60–70% opacity
- Title in Archivo, 36–40pt, True White
- Subtitle in Fira Sans, 18–20pt, Warm Grey 1
- Add thin accent line in Bright Blue under title

### Section Divider Slide
- All caps section header in Fira Mono, 20–24pt
- Dashed horizontal divider line in Warm Grey 2

### Two-Panel Value Slide
- Left 40–55%: Deep Blue curved panel with title and 1–2 key points in white
- Right 45–60%: white content area with 3–5 bullets or cards
- Optional icon circle row using Bright Seagreen or Bright Blue outlines

### Content Slide
- Headline in Archivo 28–32pt
- Body in Fira Sans 18–20pt
- Use callout boxes for key points (Bright Seagreen or Bright Blue fills)
- Add full-width footer bar in Deep Blue with short tagline in white

### Process Timeline Slide
- Horizontal step strip with 3–7 steps
- Step circles in Accent Yellow with Deep Blue numbers
- Connector line in Warm Grey 2

### Lifecycle Diagram Slide
- Circular or ring diagram centered
- Use Bright Seagreen and Bright Blue for segments
- Caption below in Fira Sans 14pt

### Diagram Slide
- Add diagram centered with caption below in Fira Sans 14pt

## Implementation Guidance
- Use scripts/ if deterministic formatting is required
- Maintain brand palette in references/brand-colors.md
- Maintain typography rules in references/typography.md

## When to Use
- Creating new decks
- Styling existing decks
- Converting text-heavy slides into visual layouts
