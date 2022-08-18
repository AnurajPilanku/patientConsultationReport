from django.forms import ModelForm
from .models import Consultation


class ConsultationForm(ModelForm):

    class Meta:
        model = Consultation
        fields = ['clinic_name', 'physician_name', 'description']