from django.shortcuts import render
from .forms import AdendaForm
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .logic.adendas_logic import create_adenda, get_adendas
from django.contrib.auth.decorators import login_required
from your_module.auth0_backend import getRole


@login_required
def adenda_list(request):
    role = getRole(request)
    if role == "Medico":
        adendas = get_adendas()
        context = {
            'adenda_list': adendas
        }
        return render(request, 'adenda/adendas.html', context)
    else:
        return HttpResponse("Unauthorized User")


@login_required
def adenda_create(request):
    role = getRole(request)
    if role == "Medico" or role == "Enfermero":
        if request.method == 'POST':
            form = AdendaForm(request.POST)
            if form.is_valid():
                create_adenda(form)
                messages.add_message(request, messages.SUCCESS, 'Adenda created successfully')
                return HttpResponseRedirect(reverse('adendaCreate'))
            else:
                print(form.errors)
        else:
            form = AdendaForm()

        context = {
            'form': form,
        }

        return render(request, 'adenda/adendaCreate.html', context)
    else:
        return HttpResponse("Unauthorized User")
