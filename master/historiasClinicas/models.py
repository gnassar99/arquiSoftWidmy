from django.contrib.postgres.fields import ArrayField
from django.db import models
from dj_cqrs.mixins import MasterMixin
from pacientes.models import Paciente

class HistoriaClinica(models.Model):
    CQRS_ID = 'historiaClinica_model'
    enfermedades = ArrayField(models.CharField(max_length=255))
    tratamientos = ArrayField(models.CharField(max_length=255))
    paciente = models.OneToOneField(Paciente, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.paciente.nombre + " " + self.paciente.apellido
