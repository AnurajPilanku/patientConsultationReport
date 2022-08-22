from django.db import models



# Create your models here.

class Consultation(models.Model):
    clinic_name = models.CharField(max_length=50, blank=True, null=True)
    clinic_logo=models.CharField(max_length=50, blank=True, null=True)
    physician_name = models.CharField(max_length=50, blank=True, null=True)
    physcian_contact=models.CharField(max_length=50, blank=True, null=True)
    patient_FirstName=models.CharField(max_length=50, blank=True, null=True)
    patient_LastName=models.CharField(max_length=50, blank=True, null=True)
    patientDOB=models.CharField(max_length=50, blank=True, null=True)
    patientContact=models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField()
    pdf_form = models.FileField(upload_to="generatedPdfs")