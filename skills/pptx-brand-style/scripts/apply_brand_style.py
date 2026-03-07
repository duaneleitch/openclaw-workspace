import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor

# --- Brand Config ---
NAVY       = RGBColor(0x23, 0x16, 0x8B)
TEAL       = RGBColor(0x5D, 0xDE, 0xD2)
WHITE      = RGBColor(0xFF, 0xFF, 0xFF)
GREY_TEXT  = RGBColor(0x33, 0x33, 0x33)
FONT_NAME  = 'Archivo'

PANEL_PCT     = 0.35

FOOTER_HEIGHT = Inches(0.5)


def _add_rect(slide, left, top, width, height, fill_rgb):
    shape = slide.shapes.add_shape(1, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill_rgb
    shape.line.fill.background()
    sp_tree = slide.shapes._spTree
    sp_tree.remove(shape._element)
    sp_tree.insert(2, shape._element)
    return shape


def apply_brand_layout(prs):
    sw = prs.slide_width
    sh = prs.slide_height
    panel_w   = int(sw * PANEL_PCT)
    content_l = panel_w + Inches(0.3)
    content_w = sw - content_l - Inches(0.2)
    content_t = Inches(0.3)

    for slide_idx, slide in enumerate(prs.slides):
        layout_name = slide.slide_layout.name.lower()
        is_title_slide = (slide_idx == 0) or ('title' in layout_name and 'content' not in layout_name)

        if is_title_slide:
            _add_rect(slide, 0, 0, sw, sh, NAVY)
            for shape in slide.shapes:
                if shape.has_text_frame:
                    for para in shape.text_frame.paragraphs:
                        para.font.name = FONT_NAME
                        para.font.color.rgb = WHITE
                        for run in para.runs:
                            run.font.name = FONT_NAME
                            run.font.color.rgb = WHITE
            continue

        _add_rect(slide, 0, 0, panel_w, sh, NAVY)
        _add_rect(slide, panel_w, sh - FOOTER_HEIGHT, sw - panel_w, FOOTER_HEIGHT, TEAL)

        for shape in slide.shapes:
            if not shape.has_text_frame:
                continue
            if shape.left < panel_w:
                shape.left  = content_l
                shape.top   = max(shape.top, content_t)
                shape.width = content_w
            if shape.left + shape.width > sw - Inches(0.2):
                shape.width = sw - shape.left - Inches(0.2)
            for para in shape.text_frame.paragraphs:
                para.font.name = FONT_NAME
                for run in para.runs:
                    run.font.name = FONT_NAME
                    try:
                        if run.font.color.type is None or run.font.color.rgb == WHITE:
                            run.font.color.rgb = GREY_TEXT
                    except Exception:
                        run.font.color.rgb = GREY_TEXT
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python apply_brand_style.py <path/to/deck.pptx>")
        sys.exit(1)
    path = sys.argv[1]
    prs = Presentation(path)
    apply_brand_layout(prs)
    prs.save(path)
    print(f"Brand style applied: {path}")
