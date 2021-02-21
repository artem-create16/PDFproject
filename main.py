from fpdf import FPDF


def add_image():
    pdf = FPDF()
    pdf.add_page()
    URL = "https://pulpbits.net/wp-content/uploads/2014/01/Tabby-Cat-Images.jpg"
    pdf.image(name=URL, x=10, y=10, w=190)
    pdf.output("add_image.pdf")

add_image()

