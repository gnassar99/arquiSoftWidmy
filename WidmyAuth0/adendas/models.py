from django.db import models

from historiasClinicas.models import HistoriaClinica

# Create your models here.
class Adenda(models.Model):
    historia = models.ForeignKey(HistoriaClinica, on_delete=models.CASCADE, default=None)
    descripcion = models.CharField(max_length=1000)
    dateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.historia.pk, self.descripcion)
