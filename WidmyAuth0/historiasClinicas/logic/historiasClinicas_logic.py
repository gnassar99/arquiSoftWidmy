from ..models import HistoriaClinica as historiaClinica
from pacientes.models import Paciente

def get_historiasClinicas():
    historiasClinicas = historiaClinica.objects.all()
    return historiasClinicas

def get_historiaClinica(var_pk):
    historiaClinica = historiaClinica.objects.get(pk=var_pk)
    return historiaClinica

def update_historiaClinica(pk, form):
    historiaClinica = get_historiaClinica(pk)
    if "enfermedades" in form:
        historiaClinica.enfermedades = form["enfermedades"]
    if "tratamientos" in form:
        historiaClinica.tratamientos = form["tratamientos"]
    historiaClinica.save()
    return ()


"""def create_historiaClinica(var):
    paciente = Paciente.objects.get(pk=var["paciente_id"])
    historiaClinica = historiaClinica(paciente=paciente)
    if "enfermedades" in var:
        historiaClinica.enfermedades = var["enfermedades"]
    if "tratamientos" in var:
        historiaClinica.tratamientos = var["tratamientos"]
    historiaClinica.save()
    return historiaClinica"""
def create_historiaClinica(form):
    historiaClinica = form.save()
    historiaClinica.save()
    return ()


