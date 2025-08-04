from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Helvetica", size=12)
        self.set_text_color(50, 50, 50)
        self.cell(0, 10, "Simran vs Daemon: The Swiss Masala Movie", ln=True, align="C")

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", size=8)
        self.set_text_color(128)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

# Create PDF instance
pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Helvetica", size=12)

# Movie content (you can replace this with your script)
movie_script = """
Title: Simran vs The Chocolate Daemon

Scene 1: Switzerland - Snowy Mountains
Simran (Kajol) laughs loudly, smashing a chocolate cake the daemon offered.

Simran: "Main koi abla naari nahi hoon, samjhe?!"
Daemon: *runs away scared*
Hanuman Ji: "Ram naam satya hai! Yeh cake nahi, daanav ka jaal hai!"

Scene 2: Bollywood Dance Battle
SRK: "Main hoon Raj, tumhara chocolate lover!"
Simran: *drops kick on daemon’s head*
Hanuman Ji: *performs bhangra*

Scene 3: Moral of the story
Stay away from suspicious desserts and believe in your inner Durga!
"""

# Replace any em dash or curly quotes with standard characters
safe_script = (
    movie_script.replace("—", "-")
    .replace("“", '"')
    .replace("”", '"')
    .replace("‘", "'")
    .replace("’", "'")
)

pdf.multi_cell(0, 10, safe_script)

# Save PDF
pdf.output("Simran_vs_Daemon_Script.pdf")
