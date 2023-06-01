from django.shortcuts import render
from .logic import historiasClinicas_logic as hc
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

from django.http import JsonResponse
from pymongo import MongoClient
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.parsers import JSONParser
from django.conf import settings
from bson.objectid import ObjectId
import json
from django.contrib.auth.decorators import login_required
from widmy.auth0backend import getRole

from .forms import HistoriaForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse


@csrf_exempt
@login_required
def historiasClinica_view(request, pk):
    client = MongoClient(settings.MONGO_CLI)
    db = client.monitoring_db
    historias = db['historias']
    role = getRole(request)
    if request.method == 'GET':
        data = historias.find({'_id': ObjectId(pk)})
        historiasClinica = serializers.serialize('json', [data,],fields=('enfermedades', 'tratamientos'))
        historiasClinica = json.dumps(json.loads(serializers.serialize('json', [data,])), indent=4)
        return render(request, 'historia/historias.html', historiasClinica)

    if request.method == 'PUT' and role == "Medico":
        data = json.loads(request.body)
        historias.update({"_id": ObjectId(pk)}, {"$set": data})
        historiasClinica = serializers.serialize('json', [data,],fields=('enfermedades', 'tratamientos'))
        historiasClinica = json.dumps(json.loads(serializers.serialize('json', [data,])), indent=4)
        return HttpResponse(historiasClinica, 'application/json')
    else:
        return HttpResponse("Unauthorized User")
    
@csrf_exempt
@login_required
def historia_list(request):
    client = MongoClient(settings.MONGO_CLI)
    db = client.monitoring_db
    historia = db['historias']

    role = getRole(request)
    if role == "Medico":
        data=historia.find({})
        context = {
            'historia_list': data
        }
        client.close()
        return render(request, 'historia/historias.html', context)
    else:
        return HttpResponse("Unauthorized User")

@csrf_exempt
@login_required
def historia_create(request):
    client = MongoClient(settings.MONGO_CLI)
    db = client.monitoring_db
    historia = db['historias']
    role = getRole(request)
    if request.method == 'POST':
        if role == "Medico":
            form = HistoriaForm(request.POST)
            if form.is_valid():
                data=form.cleaned_data
                historia.insert(data)
                messages.add_message(request, messages.SUCCESS, 'Historia Clinica creada con exito')
                client.close()
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
    client.close()
    return render(request, 'historia/historiaCreate.html', context)
