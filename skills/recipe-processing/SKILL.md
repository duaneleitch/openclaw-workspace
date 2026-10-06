---
name: recipe-processing
description: Process recipes from videos, images, documents, web pages, pasted text, and other sources into canonical Obsidian recipe notes, automatically researching and clearly labeling missing critical recipe details.
user-invocable: false
---

# Recipe Processing

Use this skill whenever JEV determines that inbound content is a recipe or substantially contains a recipe.

Duane should not need to identify the source as a recipe or ask for this workflow explicitly.

## Goals

Create or update a complete, useful canonical recipe artifact in Obsidian while preserving the original source, provenance, and the distinction between source-derived information and researched additions.

## Workflow

1. Preserve the original source and its provenance according to shared source-governance rules.
2. Extract all recipe information actually present in the source, including when available:
   - title
   - ingredients
   - quantities
   - preparation steps
   - temperatures
   - cook or bake times
   - yield or servings
   - equipment
   - sauces, garnishes, or optional components
   - creator notes or special techniques
3. Identify missing information that materially affects the ability to reproduce the recipe.
4. Automatically research missing critical information when reliable external research is available. Do not wait for Duane to ask.
5. Prefer reliable sources that closely match the recipe technique, ingredient ratios, cuisine, and preparation method.
6. Do not silently invent missing values.
7. Clearly distinguish:
   - information directly supplied by the original source
   - researched additions or inferred completion values
8. For every researched addition, preserve enough provenance to identify where it came from.
9. If reliable research does not support a missing value, leave it explicitly marked as unavailable rather than guessing.
10. Create or update the canonical recipe note using the shared Obsidian Router.
11. Link the canonical recipe to the preserved raw/source material using vault-relative paths.
12. Verify the canonical recipe artifact exists and contains the expected information before reporting success.
13. Retain only concise durable facts or the canonical vault-relative recipe path in Hindsight when useful.

## Automatic Research Completion

Missing critical fields should be researched automatically when possible, including:

- ingredient quantities
- oven, air-fryer, grill, oil, or cooking temperature
- cook, bake, fry, rest, or chill time
- serving yield
- preparation ratios
- sauce quantities
- food-safety temperatures when relevant
- other information required to reproduce the recipe successfully

Research must not overwrite source-provided information merely because another source differs.

If research supplements the recipe, label the addition clearly in the canonical note, for example:

`Researched addition: 350°F frying oil temperature based on comparable coconut shrimp recipes.`

Use concise citations, source links, or provenance notes appropriate to the artifact.

## Classification and Routing

JEV is responsible for recognizing that the inbound source is a recipe.

The source may arrive as:

- Facebook, Reddit, YouTube, or other video
- screenshot or image
- PDF
- Word document
- web page
- pasted text
- audio
- another supported source type

Do not require Duane to state that it is a recipe.

## Completion Standard

Do not stop after producing only:

- a raw source folder
- a transcript
- a generic source note
- a list of missing fields

When the source is a recipe, the expected durable output is the canonical recipe artifact.

A successful completion should normally report only:

- canonical recipe path
- source preservation status
- whether automatic research enrichment was used
- any material fields that remain genuinely unresolved

Return one concise user-facing completion response unless Duane asks for more detail.
