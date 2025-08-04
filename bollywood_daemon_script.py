from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Helvetica", size=12)

text = """bollywood_daemon_movie - A Human-Generated Bollywood Fantasy

Shah Rukh Khan as Vaidehi's Hero  
Kajol as Vaidehi (bold, powerful Durga)  
Salman Khan as the Daemon  
Aamir Khan as Hanuman  

The daemon tempts souls with Black Forest Cake filled with rum balls.  
Hanuman, chanting 'Shri Ram', counters with Satyanarayan prasad.

Vaidehi (Kajol) is no bechari. She fights with laughter, power, and love.  
Together, they save the souls and fly to heaven on Mt. Fuji.

#HumanGenerated #BollywoodFiction #PythonStory"""

pdf.multi_cell(0, 10, text)
pdf.output("bollywood_daemon_movie.pdf")
