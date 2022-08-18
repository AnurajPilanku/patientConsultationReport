import os
from fpdf import FPDF
from django.conf import settings

def pdf_generator(data_obj):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=15)
    pdf.cell(100, 10, txt="Clinic Name: {}".format(data_obj.clinic_name),
             ln=1, align='C')
    pdf.cell(200, 10, txt="Clinic Logo : Logo",
             ln=1, align='C')
    pdf.cell(200, 10, txt="Physician Name : {}".format(data_obj.physician_name),
             ln=1, align='C')
    pdf.cell(100, 10, txt="Clinic Description : {}".format(data_obj.description),
             ln=2, align='C')
    filename = data_obj.clinic_name + "_" + data_obj.physician_name + ".pdf"
    media_path = "media\generatedPdfs\{}".format(filename)
    output_file_path = os.path.join(settings.BASE_DIR, media_path)
    pdf.output(output_file_path)
    return output_file_path, filename


