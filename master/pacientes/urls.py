from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('pacientes/', views.paciente_list, name='pacienteList'),
    path('pacientecreate/', csrf_exempt(views.paciente_create), name='pacienteCreate'),
    path('pacienteupdate/<int:pk>/', csrf_exempt(views.paciente_view), name='pacienteUpdate'),
]