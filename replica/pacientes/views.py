from django.http import JsonResponse
from pymongo import MongoClient
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.parsers import JSONParser
from django.conf import settings
from bson.objectid import ObjectId
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
    client = MongoClient(settings.MONGO_CLI)
    db = client.monitoring_db
    role = getRole(request)
    pacientes = db['pacientes']
    if request.method == 'GET':
        if role == "Gerente":
            result = []
            data = pacientes.find({})
            for dto in data:
                jsonData = {
                    'id': str(dto['_id']),
                    "paciente": dto['paciente'],
                }
                result.append(jsonData)
            client.close()
            return JsonResponse(result, safe=False)
        else:
            return HttpResponse("Unauthorized User")

    if request.method == 'POST':
        if role == "Gerente":
            data = JSONParser().parse(request)
            result = pacientes.insert(data)
            respo ={
                "MongoObjectID": str(result),
                "Message": "nuevo objeto en la base de datos"
            }
            client.close()
            return JsonResponse(respo, safe=False)
        else:
            return HttpResponse("Unauthorized User")


@login_required
@csrf_exempt
def paciente_view(request, pk):
    client = MongoClient(settings.MONGO_CLI)
    db = client.monitoring_db
    pacientes = db['pacientes']
    role = getRole(request)
    if request.method == 'GET':
        if role == "Paciente":
            data = pacientes.find({'_id': ObjectId(pk)})
            result = []
            for dto in data:
                jsonData ={
                    'id': str(dto['_id']),
                    "paciente": dto['paciente']
                }
                result.append(jsonData)
            client.close()
            return JsonResponse(result[0], safe=False)
        else:
            return HttpResponse("Unauthorized User")

    if request.method == 'PUT':
        if role == "Gerente":
            data = JSONParser().parse(request)
            result = pacientes.update(
                {'_id': ObjectId(pk)},
                {'$push': {'threshold': data}}
            )
            respo ={
                "MongoObjectID": str(result),
                "Message": "nuevo objeto en la base de datos"
            }
            return JsonResponse(respo, safe=False)
        else:
            return HttpResponse("Unauthorized User")
