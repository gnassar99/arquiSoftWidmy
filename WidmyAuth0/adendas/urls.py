from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('adendas/', views.adenda_list),
    path('adendacreate/', csrf_exempt(views.adenda_create), name='adendaCreate'),
]