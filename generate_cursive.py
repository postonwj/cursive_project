from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Register the newly created TTF
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

def draw_trace_letter(c, letter, x, y):
    """Draw a large, traceable letter in dotted style."""
    c.setFont('CursiveTrace', 100)
    c.setStrokeColorRGB(0, 0, 0)
    # For simplicity, just draw letter normally (replace with dotted font or effects as desired)
    c.drawString(x, y, letter)

def draw_practice_line(c, y):
    """Draw empty practice line with guidelines."""
    draw_guidelines(c, y)
    c.setStrokeColorRGB(0, 0, 0)
    c.setLineWidth(1)
    c.line(1*inch, y + 0.1*inch, PAGE_WIDTH - 1*inch, y + 0.1*inch)

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

    # Tracing Row: A A A A A A A
    c.setFont('CursiveTrace', 36)
    c.drawString(margin, y, "A   A   A   A   A   A   A")
    draw_guidelines(c, y)
    y -= line_height

    # Practice Row: empty guidelines
    draw_guidelines(c, y)
    y -= line_height

    draw_guidelines(c, y)
    y -= line_height

    # Themed word: A is for Apple
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