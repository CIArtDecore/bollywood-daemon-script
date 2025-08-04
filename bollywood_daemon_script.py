import os
from fpdf import FPDF
import textwrap

# Create output directory if it doesn't exist
output_folder = "output"
os.makedirs(output_folder, exist_ok=True)

# Create a PDF object
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Helvetica", size=12)

# Sample story/script content (replace this with your actual content)
script_text = """
VAIDEHI (serene): Why do I hear the thunder even in silence?

DAEMON (grinning): Because I bring the storm where peace used to live.

HANUMAN (roars): You will not pass through fire when Vaidehi becomes fire itself.

NARRATOR: And thus begins the tale of courage, laughter, and celestial chaos!
"""

# Wrap long lines safely to prevent FPDFException
for line in script_text.strip().split("\n"):
    if len(line.strip()) == 0:
        pdf.ln(10)  # Blank line
    else:
        wrapped = textwrap.wrap(line.strip(), width=100)
        for wline in wrapped:
            pdf.multi_cell(0, 10, wline, align='L')

# Output PDF file
output_path = os.path.join(output_folder, "bollywood_daemon_movie.pdf")
pdf.output(output_path)

print(f"PDF successfully generated at: {output_path}")
