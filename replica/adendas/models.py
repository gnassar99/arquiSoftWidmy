from django.db import models
from dj_cqrs.mixins import ReplicaMixin
from historiasClinicas.models import HistoriaClinica

# Create your models here.
class Adenda(models.Model):
    CQRS_ID = 'adenda_model'
    CQRS_CUSTOM_SERIALIZATION = True

    historia = models.ForeignKey(HistoriaClinica, on_delete=models.CASCADE, default=None)
    descripcion = models.CharField(max_length=1000)
    dateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.historia.pk, self.descripcion)
    
    @staticmethod
    def _handle_historia(mapped_data):
        historia = HistoriaClinica.objects.get(pk=mapped_data)
        return historia
    
    @classmethod
    def cqrs_create(cls, sync, mapped_data, previous_data=None, meta=None):
        historia = cls._handle_historia(mapped_data['historia'])
        return Adenda.objects.create(
            id=mapped_data['id'],
            historia=historia,
            descripcion=mapped_data['descripcion'],
            dateTime=mapped_data['dateTime'],
            cqrs_revision=mapped_data['cqrs_revision'],
            cqrs_updated=mapped_data['cqrs_updated'],
        )
    
    def cqrs_update(self, sync, mapped_data, previous_data=None, meta=None):
        historia = self._handle_historia(mapped_data['historia'])
        self.historia = historia
        self.descripcion = mapped_data['descripcion']
        self.dateTime = mapped_data['dateTime']
        self.cqrs_revision = mapped_data['cqrs_revision']
        self.cqrs_updated = mapped_data['cqrs_updated']
        self.save()
        return self
