---
name: excalidraw-diagram
description: Create Excalidraw diagram JSON files that make visual arguments. Use when the user wants to visualize workflows, architectures, or concepts.
---

# Excalidraw Diagram Creator

Generate .excalidraw JSON files that argue visually, not just display information.

## Setup
If the user asks you to set up this skill (renderer, dependencies, etc.), see README.md for instructions.

## Customization
All colors and brand-specific styles live in references/color-palette.md. Read it before generating any diagram and use it as the single source of truth for all color choices: shape fills, strokes, text colors, evidence artifact backgrounds, and everything.

To make this skill produce diagrams in your own brand style, edit color-palette.md. Everything else in this file is universal design methodology and Excalidraw best practices.

---

## Core Philosophy
Diagrams should argue, not display. A diagram is a visual argument that shows relationships, causality, and flow that words alone cannot express. The shape should be the meaning.

The Isomorphism Test: If you removed all text, would the structure alone communicate the concept? If not, redesign.

The Education Test: Could someone learn something concrete from this diagram, or does it just label boxes? A good diagram teaches by showing real formats, real event names, and concrete examples.

---

## Depth Assessment (Do This First)
Before designing, determine what level of detail this diagram needs.

### Simple or conceptual diagrams
Use abstract shapes when:
- Explaining a mental model or philosophy
- The audience does not need technical specifics
- The concept is the abstraction

### Comprehensive or technical diagrams
Use concrete examples when:
- Diagramming a real system, protocol, or architecture
- The diagram will be used to teach or explain
- The audience needs to understand what things actually look like
- You are showing how multiple technologies integrate

For technical diagrams, include evidence artifacts.

---

## Research Mandate (For Technical Diagrams)
Before drawing anything technical, research the actual specifications. If you are diagramming a protocol, API, or framework:
1. Look up the actual JSON or data formats
2. Find the real event names, method names, or API endpoints
3. Understand how the pieces connect
4. Use real terminology, not generic placeholders

Bad: "Protocol" → "Frontend"
Good: "AG-UI streams events (RUN_STARTED, STATE_DELTA, A2UI_UPDATE)" → "CopilotKit renders via createA2UIMessageRenderer()"

Research makes diagrams accurate and educational.

---

## Evidence Artifacts
Evidence artifacts are concrete examples that prove your diagram is accurate and help viewers learn. Include them in technical diagrams.

Artifact types and render guidance:
- Code snippets: Dark rectangle with syntax-colored text
- Data or JSON examples: Dark rectangle with colored text
- Event or step sequences: Timeline pattern with line, dots, and labels
- UI mockups: Nested rectangles mimicking real UI
- Real input content: Rectangle showing the sample content
- API or method names: Use real names from docs, not placeholders

Example: For a diagram about a streaming protocol, show the actual event names from the spec, a code snippet showing how to connect, and what the streamed data looks like.

Example: For a diagram about a data transformation pipeline, show sample input data, sample output data, and intermediate states if relevant.

Key principle: show what things actually look like, not just what they are called.

---

## Multi-Zoom Architecture
Comprehensive diagrams operate at multiple zoom levels simultaneously.

Level 1: Summary flow
A simplified overview showing the full pipeline or process at a glance.

Level 2: Section boundaries
Labeled regions that group related components. These create visual rooms that help viewers understand what belongs together.

Level 3: Detail inside sections
Evidence artifacts, code snippets, and concrete examples within each section. This is where the educational value lives.

For comprehensive diagrams, aim to include all three levels. The summary gives context, the sections organize, and the details teach.

---

## Bad vs Good
Bad: equal boxes with labels
Good: each concept has a shape that mirrors its behavior

Bad: card grid layout
Good: visual structure matches conceptual structure

Bad: icons decorating text
Good: shapes are the meaning

Bad: same container for everything
Good: distinct visual vocabulary per concept

Bad: everything in a box
Good: free-floating text with selective containers

---

## Simple vs Comprehensive (Know Which You Need)
Simple diagrams
- Generic labels: Input → Process → Output
- Named boxes: API, Database, Client
- Events or Messages label
- UI or Dashboard rectangle
- About 30 seconds to explain
- Viewer learns the structure

Comprehensive diagrams
- Specific content that shows what the input or output looks like
- Named boxes plus examples of real requests and responses
- Timeline with real event names from the spec
- Mockup showing actual UI elements and content
- About 2 to 3 minutes of teaching content
- Viewer learns the structure and the details

Simple diagrams are fine for abstract concepts, quick overviews, or when the audience already knows the details. Comprehensive diagrams are needed for technical architectures, tutorials, educational content, or when you want the diagram itself to teach.

---

## Container vs Free-Floating Text
Default to free-floating text. Add containers only when they serve a purpose.

Use a container when:
- It is the focal point of a section
- It needs visual grouping with other elements
- Arrows need to connect to it
- The shape itself carries meaning
- It represents a distinct thing in the system

Use free-floating text when:
- It is a label or description
- It is supporting detail or metadata
- It describes something nearby
- It is a section title, subtitle, or annotation

Typography as hierarchy: Use font size, weight, and color to create hierarchy without boxes.

Container test: For each boxed element, ask whether it would work as free-floating text. If yes, remove the container.

---

## Design Process (Do This Before Generating JSON)
Step 0: Assess depth required
- Simple or conceptual: Abstract shapes, labels, relationships
- Comprehensive or technical: Concrete examples, code snippets, real data

If comprehensive, do research first.

Step 1: Understand deeply
For each concept, ask:
- What does this concept do
- What relationships exist between concepts
- What is the core transformation or flow
- What would someone need to see to understand this

Step 2: Map concepts to patterns
Use a visual pattern that mirrors behavior:
- Spawns multiple outputs: Fan-out
- Combines inputs into one: Convergence
- Has hierarchy or nesting: Tree
- Is a sequence of steps: Timeline
- Loops or improves continuously: Spiral or cycle
- Is an abstract state or context: Cloud
- Transforms input to output: Assembly line
- Compares two things: Side-by-side
- Separates into phases: Gap or break

Step 3: Ensure variety
Each major concept must use a different visual pattern. Avoid uniform cards or grids.

Step 4: Sketch the flow
Mentally trace how the eye moves through the diagram. There must be a clear visual story.

Step 5: Generate JSON
Only after the above steps.

Step 6: Render and validate (mandatory)
After generating the JSON, run the render-view-fix loop until the diagram looks right. This is not optional.

---

## Large or Comprehensive Diagram Strategy
For comprehensive or technical diagrams, build the JSON one section at a time. Do not generate the entire file in a single pass.

Section-by-section workflow
Phase 1: Build each section
1. Create the base file with the JSON wrapper and the first section of elements
2. Add one section per edit, one section per pass
3. Use descriptive string IDs
4. Namespace seeds by section to avoid collisions
5. Update cross-section bindings as you go

Phase 2: Review the whole
Check cross-section arrows, spacing balance, and ID bindings. Fix issues before rendering.

Phase 3: Render and validate
Run the render-view-fix loop from the Render and Validate section.

Section boundaries
Plan sections around natural visual groupings. Typical sections:
- Entry point or trigger
- First decision or routing
- Main content
- Remaining phases or outputs

What not to do
- Do not generate the entire diagram in one response
- Do not use a coding agent to generate JSON
- Do not write a generator script

---

## Visual Pattern Library
Fan-out: Central element with arrows to multiple targets
Convergence: Multiple inputs merging to one output
Tree: Parent-child branching with lines and free-floating text
Spiral or cycle: Sequence with an arrow returning to start
Cloud: Overlapping ellipses with varied sizes
Assembly line: Input → Process → Output
Side-by-side: Two parallel structures with contrast
Gap or break: Visual whitespace or barrier between sections

Lines as structure
Use lines as primary structural elements:
- Timelines: Line with dots and labels
- Trees: Trunk line plus branch lines, labels as free-floating text
- Dividers: Thin dashed lines
- Flow spines: Central line that elements relate to

---

## Shape Meaning
Default to no container. Add shapes only when they carry meaning. Aim for less than 30 percent of text inside containers.

- Labels, descriptions, details: Free-floating text
- Section titles, annotations: Free-floating text
- Timeline markers: Small ellipse
- Start or input: Ellipse
- End or output: Ellipse
- Decision or condition: Diamond
- Process or action: Rectangle
- Abstract state or context: Overlapping ellipses
- Hierarchy node: Lines plus text

---

## Color as Meaning
All colors must come from references/color-palette.md. Do not invent new colors.

- Each semantic purpose has a specific fill and stroke pair
- Free-floating text uses color for hierarchy
- Evidence artifacts use their own background and text scheme
- Pair darker strokes with lighter fills for contrast

If a concept does not fit a category, use Primary, Neutral, or Secondary.

---

## Modern Aesthetics
Roughness:
- 0 for clean, crisp edges
- 1 for hand-drawn feel

Stroke width:
- 1 for lines and dividers
- 2 for shapes and primary arrows
- 3 for emphasis, used sparingly

Opacity:
- Always use opacity 100

Small markers instead of shapes:
Use small dots as timeline markers, bullet points, connection nodes, or anchors.

---

## Layout Principles
Hierarchy through scale
- Hero: 300 by 150
- Primary: 180 by 90
- Secondary: 120 by 60
- Small: 60 by 40

Whitespace equals importance
The most important element should have at least 200 pixels of empty space around it.

Flow direction
Guide the eye left to right or top to bottom for sequences, radial for hub and spoke.

Connections required
If A relates to B, connect them with an arrow or line.

---

## Text Rules
The JSON text property contains only readable words.

Example:
{
  "id": "myElement1",
  "text": "Start",
  "originalText": "Start"
}

Settings: fontSize 16, fontFamily 3, textAlign center, verticalAlign middle.

---

## JSON Structure
{
  "type": "excalidraw",
  "version": 2,
  "source": "https://excalidraw.com",
  "elements": [ ... ],
  "appState": {
    "viewBackgroundColor": "#ffffff",
    "gridSize": 20
  },
  "files": {}
}

Element templates
See references/element-templates.md for copy-paste JSON templates for each element type.

---

## Render and Validate (Mandatory)
You cannot judge a diagram from JSON alone. After generating or editing the Excalidraw JSON, render it to PNG, view the image, and fix what you see until it is right.

How to render
cd .claude/skills/excalidraw-diagram/references && uv run python render_excalidraw.py <path-to-file.excalidraw>

This outputs a PNG next to the .excalidraw file. Then view the PNG.

The loop
1. Render and view
2. Audit against the original vision
3. Check for visual defects
4. Fix
5. Re-render and re-view
6. Repeat until it passes

When to stop
- The rendered diagram matches the conceptual design
- No text is clipped, overlapping, or unreadable
- Arrows route cleanly and connect to the right elements
- Spacing is consistent and the composition is balanced
- You would be comfortable showing it to someone without caveats

First-time setup
cd .claude/skills/excalidraw-diagram/references
uv sync
uv run playwright install chromium

---

## Quality Checklist
Depth and evidence
1. Research done
2. Evidence artifacts included
3. Multi-zoom included
4. Concrete over abstract
5. Educational value

Conceptual quality
6. Isomorphism
7. Argument
8. Variety
9. No uniform containers

Container discipline
10. Minimal containers
11. Lines as structure
12. Typography hierarchy

Structural
13. Connections
14. Flow
15. Hierarchy

Technical
16. Text clean
17. Font family 3
18. Roughness 0 for modern
19. Opacity 100
20. Container ratio under 30 percent

Visual validation
21. Rendered to PNG
22. No text overflow
23. No overlapping elements
24. Even spacing
25. Arrows land correctly
26. Readable at export size
27. Balanced composition
