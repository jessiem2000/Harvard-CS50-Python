from fpdf import FPDF

name = input("Name: ")

class PDF(FPDF):
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_font("helvetica", style="B", size=32)
    pdf.cell(0, 60, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align='C')
    pdf.image("shirtificate.png", w = pdf.epw,)
    pdf.set_font("Times", style = "B", size = 28)
    pdf.set_text_color(255, 255, 255)
    pdf.text(x = 65, y = 130, text = f"{name} took CS50")
    pdf.output("shirtificate.pdf")



