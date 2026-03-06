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

## Slide Patterns
### Title Slide
- Title in Archivo, 36–40pt, Deep Blue
- Subtitle in Fira Sans, 18–20pt, Warm Dark Grey
- Add thin accent line in Bright Blue under title

### Section Divider Slide
- All caps section header in Fira Mono, 20–24pt
- Dashed horizontal divider line in Warm Grey 2

### Content Slide
- Headline in Archivo 28–32pt
- Body in Fira Sans 18–20pt
- Use callout boxes for key points (Bright Seagreen or Bright Blue fills)

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
