from django.db import models

# Create your models here.

class Consultation(models.Model):
    clinic_name = models.CharField(max_length=50, blank=True, null=True)
    physician_name = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField()
    pdf_form = models.FileField(upload_to="generatedPdfs")