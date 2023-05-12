from django import forms
from .models import HistoriaClinica

class HistoriaForm(forms.ModelForm):
    class Meta:
        model = HistoriaClinica
        fields = [
            'enfermedades',
            'tratamientos',
            'paciente',
        ]
        labels = {
            'enfermedades': 'Enfermedades',
            'tratamientos': 'Tratemientos',
            'paciente': 'Paciente'
        }