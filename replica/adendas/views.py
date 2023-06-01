from django.shortcuts import render
from .forms import AdendaForm
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .logic.adendas_logic import create_adenda, get_adendas
from django.contrib.auth.decorators import login_required
from widmy.auth0backend import getRole
from django.views.decorators.csrf import csrf_exempt

from django.http import JsonResponse
from pymongo import MongoClient
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.parsers import JSONParser
from django.conf import settings
from bson.objectid import ObjectId
import json



@csrf_exempt
@login_required
def adenda_list(request):
    client = MongoClient(settings.MONGO_CLI)
    db = client.monitoring_db
    adendas = db['adendas']
    role = getRole(request)
    if role == "Medico":
        data=adendas.find({})
        context = {
            'adenda_list': data
        }
        client.close()
        return render(request, 'adenda/adendas.html', context)
    else:
        return HttpResponse("Unauthorized User")

@csrf_exempt
@login_required
def adenda_create(request):
    client = MongoClient(settings.MONGO_CLI)
    db = client.monitoring_db
    adendas = db['adendas']
    role = getRole(request)
    if role == "Medico" or role == "Enfermero":
        if request.method == 'POST':
            form = AdendaForm(request.POST)
            if form.is_valid():
                data=form.cleaned_data
                adendas.insert(data)
                messages.add_message(request, messages.SUCCESS, 'Adenda created successfully')
                client.close()
                return HttpResponseRedirect(reverse('adendaCreate'))
            else:
                print(form.errors)
        else:
            form = AdendaForm()

        context = {
            'form': form,
        }
        client.close()
        return render(request, 'adenda/adendaCreate.html', context)
    else:
        return HttpResponse("Unauthorized User")
