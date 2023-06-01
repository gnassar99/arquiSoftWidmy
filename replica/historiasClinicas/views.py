from django.shortcuts import render
from .logic import historiasClinicas_logic as hc
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

from .forms import HistoriaForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from widmy.auth0backend import getRole

@csrf_exempt
@login_required
def historiasClinica_view(request, pk):
    role = getRole(request)
    if request.method == 'GET':
        historiasClinica_dto = hc.get_historiaClinica(pk)
        historiasClinica = serializers.serialize('json', [historiasClinica_dto,],fields=('enfermedades', 'tratamientos'))
        historiasClinica = json.dumps(json.loads(serializers.serialize('json', [historiasClinica_dto,])), indent=4)
        return render(request, 'historia/historias.html', historiasClinica)

    if request.method == 'PUT' and role == "Medico":
        historiasClinica_dto = hc.update_historiaClinica(pk, json.loads(request.body))
        historiasClinica = serializers.serialize('json', [historiasClinica_dto,],fields=('enfermedades', 'tratamientos'))
        historiasClinica = json.dumps(json.loads(serializers.serialize('json', [historiasClinica_dto,])), indent=4)
        return HttpResponse(historiasClinica, 'application/json')
    else:
        return HttpResponse("Unauthorized User")
    
@login_required
def historia_list(request):
    role = getRole(request)
    if role == "Medico":
        historias = hc.get_historiasClinicas()
        context = {
            'historia_list': historias
        }
        return render(request, 'historia/historias.html', context)
    else:
        return HttpResponse("Unauthorized User")

@login_required
def historia_create(request):
    role = getRole(request)
    if request.method == 'POST':
        if role == "Medico":
            form = HistoriaForm(request.POST)
            if form.is_valid():
                hc.create_historiaClinica(form)
                messages.add_message(request, messages.SUCCESS, 'Historia Clinica creada con exito')
                return HttpResponseRedirect(reverse('historiaCreate'))
            else:
                print(form.errors)
        else:
            return HttpResponse("Unauthorized User")
    else:
        form = HistoriaForm()

    context = {
        'form': form,
    }

    return render(request, 'historia/historiaCreate.html', context)
