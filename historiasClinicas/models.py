from django.contrib.postgres.fields import ArrayField
from django.db import models
from pacientes.models import Paciente
from jsonfield import JSONField


class HistoriaClinica(models.Model):
    enfermedades = JSONField(default=list)
    tratamientos = JSONField(default=list)
    paciente = models.OneToOneField(Paciente, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.paciente.nombre + " " + self.paciente.apellido
