from django.forms import ModelForm,widgets
from .models import Consultation
#https://docs.djangoproject.com/en/4.0/topics/forms/modelforms/


class ConsultationForm(ModelForm):

    class Meta:
        model = Consultation
        #fields="__all__"
        fields = ['clinic_name','clinic_logo','physician_name','physcian_contact','patient_FirstName','patient_LastName','patientDOB','patientContact','description']
