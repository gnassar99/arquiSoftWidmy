from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.historiasClinicas_view, name='historiasClinicas_view'),
    path('historiasClinicas/', views.historiasClinicas_view, name='historias_clinicas_view'),
    path('<int:pk>', views.historiasClinica_view, name='historiasClinica_view'),
]
