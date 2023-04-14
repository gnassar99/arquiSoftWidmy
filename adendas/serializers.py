from rest_framework import serializers
from . import models


class AdendaSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'historia', 'descripcion', 'time',)
        model = models.Adenda