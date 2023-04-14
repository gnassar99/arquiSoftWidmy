from django.shortcuts import render
from .forms import AdendaForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .logic.adendas_logic import create_adenda, get_adendas

def adenda_list(request):
    adendas = get_adendas()
    context = {
        'adenda_list': adendas
    }
    return render(request, 'Adenda/adendas.html', context)

def adenda_create(request):
    if request.method == 'POST':
        form = AdendaForm(request.POST)
        if form.is_valid():
            create_adenda(form)
            messages.add_message(request, messages.SUCCESS, 'adenda creada exitosamente')
            return HttpResponseRedirect(reverse('adendaCreate'))
        else:
            print(form.errors)
    else:
        form = AdendaForm()

    context = {
        'form': form,
    }

    return render(request, 'Adenda/adendaCreate.html', context)

# Create your views here.
