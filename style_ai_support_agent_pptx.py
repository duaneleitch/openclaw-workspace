from pathlib import Path
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.util import Pt

pptx_path = Path('/mnt/obsidian/20_PowerPoint/Presentations/AI_Support_Agent.pptx')
prs = Presentation(pptx_path)

# Brand colors
DEEP_BLUE = RGBColor(0x23, 0x16, 0x8B)
BRIGHT_BLUE = RGBColor(0x4E, 0x3D, 0xEC)
BRIGHT_SEA = RGBColor(0x5D, 0xDE, 0xD2)
WARM_BLACK = RGBColor(0x1F, 0x1C, 0x19)
WARM_GREY = RGBColor(0x5D, 0x57, 0x4F)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)

# Fonts (fallbacks if not installed)
FONT_TITLE = "Archivo"
FONT_BODY = "Fira Sans"
FONT_LABEL = "Fira Mono"

for slide in prs.slides:
    # Set white background
    fill = slide.background.fill
    fill.solid()
    fill.fore_color.rgb = WHITE

    for shape in slide.shapes:
        if not shape.has_text_frame:
            continue
        for p in shape.text_frame.paragraphs:
            for r in p.runs:
                # Title vs body heuristic
                if shape == slide.shapes.title:
                    r.font.name = FONT_TITLE
                    r.font.size = Pt(36)
                    r.font.bold = True
                    r.font.color.rgb = DEEP_BLUE
                else:
                    r.font.name = FONT_BODY
                    r.font.size = Pt(20)
                    r.font.color.rgb = WARM_BLACK

# Add a simple accent line to title slide
slide0 = prs.slides[0]
line = slide0.shapes.add_shape(1, 0, 140, prs.slide_width, Pt(2))  # line
line.fill.solid()
line.fill.fore_color.rgb = BRIGHT_BLUE
line.line.color.rgb = BRIGHT_BLUE

prs.save(pptx_path)
print(pptx_path)
