from fpdf import FPDF
import sys


class shirtpdf(FPDF):
    def header(self):
        self.image("shirtificate.png", h=190, y=60)
        self.set_font("helvetica", "B", 50)
        self.cell(w=self.w-20, h=30, align="C", txt="CS50 Shirtificate")


def main():
    shirtificate(input("Name: ").title())


def shirtificate(name):
    pdf = shirtpdf(orientation='portrait', unit='mm',
                   format='A4', font_cache_dir='DEPRECATED')
    pdf.add_page()
    pdfname = "cert_" + name
    name = name + " took CS50"
    pdf.set_font("helvetica", "B", 22)
    pdf.set_text_color(255, 255, 255)
    pdf.text(x=(105-len(name)*2), y=120, txt=name)
    pdf.output(pdfname + ".pdf")


if __name__ == "__main__":
    main()
