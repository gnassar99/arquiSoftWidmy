from django.db import models
from dj_cqrs.mixins import MasterMixin

# Create your models here.
class Paciente(models.Model):
    CQRS_ID = 'paciente_model'
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField(default=0)
    telefono = models.IntegerField(default=0)
    email = models.CharField(max_length=100, default='')
    fechaNacimiento = models.DateField(null=True, blank=True, default=None)
    triage = models.CharField(max_length=100, default='')    

    def __str__(self):
        return self.nombre + ' ' + self.apellido
    