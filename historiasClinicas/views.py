from django.shortcuts import render

from .logic import historiasClinicas_logic as hc
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def historiasClinicas_view(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            historiasClinica_dto = hc.get_historiasClinica(id)
            historiasClinica = serializers.serialize('json', [historiasClinica_dto,],fields=('enfermedades', 'tratamientos'))
            historiasClinica = json.dumps(json.loads(serializers.serialize('json', historiasClinica_dto)), indent=4)
            return HttpResponse(historiasClinica, 'application/json')
        else:
            historiasClinicas_dto = hc.get_historiasClinicas()
            historiasClinicas = serializers.serialize('json', historiasClinicas_dto,fields=('enfermedades', 'tratamientos'))
            historiasClinicas = json.dumps(json.loads(serializers.serialize('json', historiasClinicas_dto)), indent=4)
            return HttpResponse(historiasClinicas, 'application/json')

    if request.method == 'POST':
        historiasClinica_dto = hc.create_historiasClinica(json.loads(request.body))
        historiasClinica = serializers.serialize('json', [historiasClinica_dto,],fields=('enfermedades', 'tratamientos'))
        historiasClinica = json.dumps(json.loads(serializers.serialize('json', [historiasClinica_dto,])), indent=4)
        return HttpResponse(historiasClinica, 'application/json')

@csrf_exempt
def historiasClinica_view(request, pk):
    if request.method == 'GET':
        historiasClinica_dto = hc.get_historiasClinica(pk)
        historiasClinica = serializers.serialize('json', [historiasClinica_dto,],fields=('enfermedades', 'tratamientos'))
        historiasClinica = json.dumps(json.loads(serializers.serialize('json', [historiasClinica_dto,])), indent=4)
        return HttpResponse(historiasClinica, 'application/json')

    if request.method == 'PUT':
        historiasClinica_dto = hc.update_historiasClinica(pk, json.loads(request.body))
        historiasClinica = serializers.serialize('json', [historiasClinica_dto,],fields=('enfermedades', 'tratamientos'))
        historiasClinica = json.dumps(json.loads(serializers.serialize('json', [historiasClinica_dto,])), indent=4)
        return HttpResponse(historiasClinica, 'application/json')