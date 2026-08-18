from pathlib import Path

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT

RED = HexColor("#FF5C66")
YELLOW = HexColor("#FFCD3A")
BLUE = HexColor("#236DA5")
LIGHT_BG = HexColor("#F5FBFC")
DARK = HexColor("#222222")

styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    "TitleStyle", parent=styles["Title"],
    fontName="Times-Bold", fontSize=30, textColor=RED,
    alignment=TA_CENTER, spaceAfter=4
)

subtitle_style = ParagraphStyle(
    "SubtitleStyle", parent=styles["Normal"],
    fontName="Times-Bold", fontSize=16, textColor=YELLOW,
    alignment=TA_CENTER, spaceAfter=18
)

intro_style = ParagraphStyle(
    "IntroStyle", parent=styles["Normal"],
    fontName="Times-Roman", fontSize=11.5, textColor=BLUE,
    alignment=TA_LEFT, leading=16, spaceAfter=20
)

item_name_style = ParagraphStyle(
    "ItemNameStyle", parent=styles["Normal"],
    fontName="Times-Bold", fontSize=13.5, textColor=RED, spaceAfter=4
)

item_desc_style = ParagraphStyle(
    "ItemDescStyle", parent=styles["Normal"],
    fontName="Times-Roman", fontSize=10.5, textColor=DARK, leading=14
)

footer_style = ParagraphStyle(
    "FooterStyle", parent=styles["Normal"],
    fontName="Times-Italic", fontSize=9, textColor=BLUE,
    alignment=TA_CENTER
)

equipment = [
    (
        "HEPA-Filter Vacuum Cleaners",
        "Commercial backpack and upright vacuums fitted with HEPA filtration to "
        "capture fine dust, allergens, and debris from carpets, upholstery, and "
        "hard floors, leaving the air noticeably cleaner behind us."
    ),
    (
        "Hot Water Extraction Machine",
        "Used for carpet and upholstery shampooing. Hot water and cleaning "
        "solution are injected deep into the fibers and then extracted along "
        "with the loosened dirt and moisture."
    ),
    (
        "Pressure Washer",
        "High-pressure water equipment for exterior surfaces, driveways, and "
        "heavy-duty degreasing jobs such as kitchen exhaust hoods and "
        "commercial floors."
    ),
    (
        "Microfiber Cleaning Systems",
        "Colour-coded microfiber cloths and mop systems that trap dirt and "
        "bacteria effectively while preventing cross-contamination between "
        "different areas of a job site."
    ),
]

def build():
    output_path = Path(__file__).with_name("equipment-list.pdf")
    doc = SimpleDocTemplate(
        str(output_path),
        pagesize=letter,
        topMargin=0.9 * inch,
        bottomMargin=0.8 * inch,
        leftMargin=0.9 * inch,
        rightMargin=0.9 * inch,
    )

    story = []

    story.append(Paragraph("Cayden's Cleaning Company", title_style))
    story.append(Paragraph("Equipment List", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1.4, color=YELLOW, spaceAfter=18))

    story.append(Paragraph(
        "We use professional-grade equipment to make sure every job is done "
        "to a high standard, from a quick residential tidy-up to a full "
        "commercial kitchen deep clean. Below is a summary of the core "
        "equipment our teams bring to every booking.",
        intro_style
    ))

    for name, desc in equipment:
        story.append(Paragraph(name, item_name_style))
        story.append(Paragraph(desc, item_desc_style))
        story.append(Spacer(1, 14))

    story.append(Spacer(1, 10))
    story.append(HRFlowable(width="100%", thickness=1, color=BLUE, spaceAfter=10))
    story.append(Paragraph(
        "Email: info@caydenscleaningcompany.com &nbsp;|&nbsp; "
        "Phone: +1 (123) 456-7890",
        footer_style
    ))
    story.append(Paragraph("&copy; 2026 Cayden's Cleaning Company. All rights reserved.", footer_style))

    doc.build(story)
    return output_path

if __name__ == "__main__":
    output_path = build()
    print(f"Created {output_path}")
