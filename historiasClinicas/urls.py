from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('', views.historiasClinicas_view, name='historiasClinicas_view'),
    path('historias/', views.historiasClinicas_view, name='historiaList'),
    path('historiacreate/', csrf_exempt(views.historiasClinicas_view), name='historiacreate'),
]
