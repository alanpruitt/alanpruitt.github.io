import os
from reportlab.lib.pagesizes import inch
from reportlab.lib import colors
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            super().showPage()
        super().save()

    def draw_page_number(self, page_count):
        self.saveState()
        self.setFont("Helvetica-Bold", 14)
        self.setFillColor(colors.HexColor("#A0AEC0"))
        # Draw slide indicator in the bottom right corner
        self.drawRightString(1080 - 100, 90, f"{self._pageNumber} / {page_count}")
        self.restoreState()

def wrap_text(text, max_width, font_name, font_size, c):
    lines = []
    for raw_line in text.split('\n'):
        if not raw_line:
            lines.append("")
            continue
        words = raw_line.split(' ')
        current_line = []
        for word in words:
            test_line = ' '.join(current_line + [word])
            if c.stringWidth(test_line, font_name, font_size) <= max_width:
                current_line.append(word)
            else:
                if current_line:
                    lines.append(' '.join(current_line))
                    current_line = [word]
                else:
                    lines.append(word)
        if current_line:
            lines.append(' '.join(current_line))
    return lines

def create_carousel():
    # Square format: 15 inches x 15 inches at 72 DPI = 1080x1080 px
    page_size = (1080, 1080)
    pdf_path = "essay_37_linkedin_carousel.pdf"
    
    c = NumberedCanvas(pdf_path, pagesize=page_size)
    
    slides = [
        # Slide 1: Title
        {
            "tag": "ESSAY 37 LAUNCH",
            "title": "What If I Didn't?",
            "subtitle": "Future-Proofing Course Fleets with WCAG 3.0 Cognitive Accessibility",
            "footer": "Coach Alan | Curriculum-as-Code"
        },
        # Slide 2: The Compliance Trap
        {
            "tag": "THE CORE PROBLEM",
            "title": "Beyond Binary Compliance",
            "subtitle": "Passing contrast ratios and alt-text checks isn't enough. When students read complex kinesiology and nutrition texts on mobile devices, dense paragraphs create heavy cognitive bottlenecks.",
            "footer": "Accessibility is about human comprehension."
        },
        # Slide 3: The WCAG 3.0 Shift
        {
            "tag": "EMERGING STANDARDS",
            "title": "The WCAG 3.0 Shift",
            "subtitle": "Moving away from rigid pass/fail checks toward holistic, outcome-based scoring that makes cognitive accessibility a first-class citizen in curriculum design.",
            "footer": "Targeting proactive alignment ahead of 2028."
        },
        # Slide 4: Engineering the Fix
        {
            "tag": "CURRICULUM-AS-CODE",
            "title": "Automating Cognitive Optimization",
            "subtitle": "• Built custom Python readability linters\n• Automatically parsed 378 master files\n• Converted dense blocks into scannable lists\n• Preserved strict clinical fencing (###)",
            "footer": "Slow is Smooth, Smooth is Fast."
        },
        # Slide 5: Call to Action
        {
            "tag": "READ THE FULL ESSAY",
            "title": "Explore the Full Breakdown",
            "subtitle": "Dive into the complete technical essay on my Substack and discover how automated engineering scales equitable digital learning.",
            "footer": "Link in post description above"
        }
    ]

    for slide in slides:
        # Background - Deep Professional Dark Slate
        c.setFillColor(colors.HexColor("#0F172A"))
        c.rect(0, 0, 1080, 1080, fill=1, stroke=0)

        # Top Accent Tag
        c.setFillColor(colors.HexColor("#38BDF8")) # Accent Cyan
        c.setFont("Helvetica-Bold", 16)
        c.drawString(100, 920, slide["tag"].upper())

        # Main Title (wrapped and positioned)
        c.setFillColor(colors.HexColor("#FFFFFF"))
        c.setFont("Helvetica-Bold", 52)
        title_lines = wrap_text(slide["title"], 880, "Helvetica-Bold", 52, c)
        y_title = 830
        for t_line in title_lines:
            c.drawString(100, y_title, t_line)
            y_title -= 64

        # Subtitle / Body Content (wrapped and positioned)
        c.setFillColor(colors.HexColor("#CBD5E1"))
        c.setFont("Helvetica", 32)
        
        y_pos = min(720, y_title - 30)
        subtitle_lines = wrap_text(slide["subtitle"], 880, "Helvetica", 32, c)
        for line in subtitle_lines:
            c.drawString(100, y_pos, line)
            y_pos -= 52

        # Footer divider line
        c.setStrokeColor(colors.HexColor("#334155"))
        c.setLineWidth(2)
        c.line(100, 140, 980, 140)

        # Footer Text
        c.setFillColor(colors.HexColor("#94A3B8"))
        c.setFont("Helvetica", 20)
        c.drawString(100, 90, slide["footer"])

        c.showPage()

    c.save()
    print(f"✅ LinkedIn Carousel PDF successfully generated: {pdf_path}")

if __name__ == "__main__":
    create_carousel()
