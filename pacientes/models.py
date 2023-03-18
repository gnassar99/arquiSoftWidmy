from django.db import models

# Create your models here.
class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    # edad = models.IntegerField()    
    # telefono = models.IntegerField()
    # email = models.CharField(max_length=100)
    # fechaNacimiento = models.DateField()
    # triage = models.CharField(max_length=100)    

    def __str__(self):
        return self.nombre + ' ' + self.apellido
    