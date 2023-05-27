from django.contrib.postgres.fields import ArrayField
from django.db import models
from pacientes.models import Paciente

class HistoriaClinica(models.Model):
    CQRS_ID = 'historiaClinica_model'
    CQRS_CUSTOM_SERIALIZATION = True

    enfermedades = ArrayField(models.CharField(max_length=255))
    tratamientos = ArrayField(models.CharField(max_length=255))
    paciente = models.OneToOneField(Paciente, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.paciente.nombre + " " + self.paciente.apellido
    
    @staticmethod
    def _handle_paciente(mapped_data):
        paciente = Paciente.objects.get(pk=mapped_data)
        return paciente
    
    @classmethod
    def cqrs_create(cls, sync, mapped_data, previous_data=None, meta=None):
        paciente = cls._handle_paciente(mapped_data['paciente'])
        return HistoriaClinica.objects.create(
            id=mapped_data['id'],
            enfermedades=mapped_data['enfermedades'],
            tratamientos=mapped_data['tratamientos'],
            paciente=paciente,
            cqrs_revision=mapped_data['cqrs_revision'],
            cqrs_updated=mapped_data['cqrs_updated'],
        )
    
    def cqrs_update(self, sync, mapped_data, previous_data=None, meta=None):
        paciente = self._handle_paciente(mapped_data['paciente'])
        self.enfermedades = mapped_data['enfermedades']
        self.tratamientos = mapped_data['tratamientos']
        self.paciente = paciente
        self.cqrs_revision = mapped_data['cqrs_revision']
        self.cqrs_updated = mapped_data['cqrs_updated']
        self.save()
        return self
