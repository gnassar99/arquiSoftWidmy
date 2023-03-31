from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('pacientes/<int:pk>', views.paciente_view, name='paciente_view'),
    path('pacientes/', views.pacientes_view, name='pacientes_view'),
    # path('', views.pacientes_view, name='pacientes_view'),
    #path('<int:pk>', views.paciente_view, name='paciente_view'),
]

