from django import forms
from .models import Adenda

class AdendaForm(forms.ModelForm):
    class Meta:
        model = Adenda
        fields = [
            'historia',
            'descripcion',
            #'dateTime',
        ]

        labels = {
            'historia' : 'HistoriaClinica',
            'descripcion' : 'Descripcion',
            #'dateTime' : 'Date Time',
        }