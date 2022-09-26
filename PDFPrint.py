# import pandas as pd
from tkinter import *
# import matplotlib
# from pylab import title, figure, xlabel, ylabel, xticks, bar, legend, axis, savefig
from fpdf import FPDF
from tkinter import messagebox
from tkPDFViewer import tkPDFViewer as pdfViewer
import PyPDF2


def view_pdf(path):
    # Initializing tk
    root = Tk()
    # Set the width and height of our root window.
    root.geometry("1000x750")
    # creating object of ShowPdf from tkPDFViewer.
    v1 = pdfViewer.ShowPdf()
    # Adding pdf location and width and height.
    v2 = v1.pdf_view(root,
                     pdf_location=path+"pdf",
                     width=50, height=100)

    # Placing Pdf in my gui.
    v2.pack()
    root.mainloop()


def print_pdf(profile, data):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_xy(0, 0)
    pdf.set_font('arial', 'B', 12)
    pdf.cell(60)
    pdf.cell(75, 10, "A Tabular and Graphical Report of Criminal Profile as Aforementioned Bellow", 0, 2, 'C')
    pdf.cell(90, 10, " ", 0, 2, 'C')
    pdf.cell(-40)
    pdf.image(profile, x=50, y=None, w=0, h=0, type='', link='')
    # pdf.cell(30, 10, '', 1, 0, 'C')
    pdf.cell(50, 10, '', 1, 0, 'C')
    pdf.cell(40, 10, '', 1, 0, 'C')
    # pdf.cell(40, 10, 'Mike', 1, 2, 'C')
    pdf.cell(-90)
    pdf.set_font('arial', '', 12)
    for i, item in enumerate(data.items()):
        # pdf.cell(40, 10, '--', 0, 0, 'C')
        pdf.cell(50, 10, '%s' % (item[0]), 1, 0, 'C')
        pdf.cell(40, 10, '%s' % (item[1].capitalize()), 1, 0, 'C')
        pdf.cell(40, 10, '--', 1, 2, 'C')
        pdf.cell(-90)
    pdf.cell(90, 10, " ", 0, 2, 'C')
    pdf.cell(-30)
    # pdf.image(profile, x=None, y=None, w=0, h=0, type='', link='')
    pdf.output(data["Name"] + '.pdf', 'F')
    messagebox.showinfo(f"Success", f"PDF file: {data['Name']} Successfully.")
    # Display PDF page
    view_pdf(data["Name"])


if __name__ == "__main__":
    print_pdf(None, [1, 2, 4.4])
    pass
