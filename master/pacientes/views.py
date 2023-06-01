from .logic import pacientes_logic as pl
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from widmy.auth0backend import getRole


@csrf_exempt
@login_required
def pacientes_view(request):
    role = getRole(request)
    if request.method == 'GET':
        if role == "Gerente":
            id = request.GET.get("id", None)
            if id:
                paciente_dto = pl.get_paciente(id)
                paciente = serializers.serialize('json', [paciente_dto,])
                return HttpResponse(paciente, 'application/json')
            else:
                pacientes_dto = pl.get_pacientes()
                pacientes = serializers.serialize('json', pacientes_dto)
                return HttpResponse(pacientes, 'application/json')
        else:
            return HttpResponse("Unauthorized User")

    if request.method == 'POST':
        if role == "Gerente":
            paciente_dto = pl.create_paciente(json.loads(request.body))
            paciente = serializers.serialize('json', [paciente_dto,])
            return HttpResponse(paciente, 'application/json')
        else:
            return HttpResponse("Unauthorized User")


@login_required
@csrf_exempt
def paciente_view(request, pk):
    role = getRole(request)
    if request.method == 'GET':
        if role == "Paciente":
            paciente_dto = pl.get_paciente(pk)
            paciente = serializers.serialize('json', [paciente_dto,])
            return HttpResponse(paciente, 'application/json')
        else:
            return HttpResponse("Unauthorized User")

    if request.method == 'PUT':
        if role == "Gerente":
            paciente_dto = pl.update_paciente(pk, json.loads(request.body))
            paciente = serializers.serialize('json', [paciente_dto,])
            return HttpResponse(paciente, 'application/json')
        else:
            return HttpResponse("Unauthorized User")
