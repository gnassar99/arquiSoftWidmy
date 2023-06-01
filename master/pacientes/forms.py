from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = [
            'nombre',
            'apellido',
            'edad',
            'telefono',
            'email',
            'fechaNacimiento',
            'triage',
        ]
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'edad': 'Edad',
            'telefono': 'Telefono',
            'email': 'Email',
            'fechaNacimiento': 'Fecha de Nacimiento',
            'triage': 'Triage',
        }