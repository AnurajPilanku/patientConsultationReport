#https://stackabuse.com/working-with-pdfs-in-python-adding-images-and-watermarks/
import sys

ClinicName   =""
Cliniclogo  =""
PhysicianName=""
PhysicianContact=""
PatientfirstName =""
PatientLastName=""
PatientDob =""
PatientContact=""
inputtxtPath=""
pdfFilePath=""


from fpdf import FPDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size = 15)
f = open(inputtxtPath, "r")
for x in f:
	pdf.cell(200, 10, txt = x, ln = 1, align = 'C')
pdf.output(pdfFilePath)
