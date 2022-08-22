import os
from fpdf import FPDF
from django.conf import settings

def pdf_generator(data_obj):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=15)
    def pdfattr(val1,val2,txtstr,dobjattr,line,alignment):
        pdf.cell(val1, val2, txt="{fielsname}: {dobj}".format(fielsname=txtstr,dobj=dobjattr),ln=line, align=alignment)
    pdfattr(100,10,"Clinic Name",data_obj.clinic_name,1,'C')
    pdfattr(100, 10, "clinic_logo", data_obj.clinic_logo, 1, 'C')
    pdfattr(100, 10, "physician_name", data_obj.physician_name, 1, 'C')
    pdfattr(100, 10, "physcian_contact", data_obj.physcian_contact, 1, 'C')
    pdfattr(100, 10, "patient_FirstName", data_obj.patient_FirstName, 1, 'C')
    pdfattr(100, 10, "patient_LastName", data_obj.patient_LastName, 1, 'C')
    pdfattr(100, 10, "patientDOB", data_obj.patientDOB, 1, 'C')
    pdfattr(100, 10, "patientContact", data_obj.patientContact, 1, 'C')
    pdfattr(100, 10, "description", data_obj.description, 1, 'C')
    # pdf.cell(100, 10, txt="Clinic Name: {}".format(data_obj.clinic_name),ln=1, align='C')
    # pdf.cell(200, 10, txt="Clinic Logo : Logo",ln=1, align='C')
    # pdf.cell(200, 10, txt="Physician Name : {}".format(data_obj.physician_name),ln=1, align='C')
    # pdf.cell(100, 10, txt="Clinic Description : {}".format(data_obj.description),ln=2, align='C')
    filename = data_obj.clinic_name + "_" + data_obj.physician_name + ".pdf"
    media_path = "media\generatedPdfs\{}".format(filename)
    output_file_path = os.path.join(settings.BASE_DIR, media_path)
    pdf.output(output_file_path)
    return output_file_path, filename


