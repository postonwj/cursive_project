from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Register the converted TTF font (make sure the .ttf file exists)
pdfmetrics.registerFont(
    TTFont('CursiveTrace', 'FrbAmericanCursiveDotted.ttf')
)

PAGE_WIDTH, PAGE_HEIGHT = letter

def draw_guidelines(c, y):
    """Draw baseline, midline, and topline for handwriting practice."""
    c.setStrokeColorRGB(0.7, 0.7, 0.7)
    c.setLineWidth(1)
    # Baseline
    c.line(1*inch, y, PAGE_WIDTH - 1*inch, y)
    # Midline
    c.line(1*inch, y + 0.3*inch, PAGE_WIDTH - 1*inch, y + 0.3*inch)
    # Topline
    c.line(1*inch, y + 0.6*inch, PAGE_WIDTH - 1*inch, y + 0.6*inch)

def create_page(c):
    margin = 1 * inch
    spacing = 1 * inch
    line_height = 0.8 * inch
    start_y = PAGE_HEIGHT - margin - spacing

    # Title
    c.setFont('Helvetica-Bold', 18)
    c.drawString(margin, start_y, "Cursive Writing Practice: Letter A")

    y = start_y - spacing * 1.5

    # Tracing Row: Large Letter A for demonstration
    c.setFont('CursiveTrace', 72)
    c.drawString(margin, y, "A")
    y -= line_height

    # Tracing Row: multiple A's for practice
    c.setFont('CursiveTrace', 36)
    c.drawString(margin, y, "A   A   A   A   A   A   A")
    draw_guidelines(c, y)
    y -= line_height

    # Practice lines (empty with guidelines)
    for _ in range(3):
        draw_guidelines(c, y)
        y -= line_height

    # Themed word
    c.setFont('CursiveTrace', 28)
    c.drawString(margin, y, "A is for Apple")
    draw_guidelines(c, y)
    y -= line_height

    # Blank practice line
    draw_guidelines(c, y)

def main():
    c = canvas.Canvas("cursive_practice.pdf", pagesize=letter)
    create_page(c)
    c.showPage()
    c.save()
    print("PDF generated: cursive_practice.pdf")

if __name__ == "__main__":
    main()
