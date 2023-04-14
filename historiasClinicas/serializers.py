from rest_framework import serializers
from . import models


class HistoriaSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'enfermedades', 'tratamientos', 'paciente',)
        model = models.HistoriaClinica