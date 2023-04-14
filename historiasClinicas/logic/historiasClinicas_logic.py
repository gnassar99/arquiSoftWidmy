from ..models import HistoriaClinica as historiaClinica

def get_historiasClinicas():
    historiasClinicas = historiaClinica.objects.all()
    return historiasClinicas

def get_historiaClinica(var_pk):
    historiaClinica = historiaClinica.objects.get(pk=var_pk)
    return historiaClinica

def update_historiaClinica(var_pk, new_var):
    historiaClinica = get_historiaClinica(var_pk)
    if "enfermedades" in new_var:
        historiaClinica.enfermedades = new_var["enfermedades"]
    if "tratamientos" in new_var:
        historiaClinica.tratamientos = new_var["tratamientos"]
    historiaClinica.save()
    return historiaClinica


def create_historiaClinica(var):
    paciente = Paciente.objects.get(pk=var["paciente_id"])
    historiaClinica = HistoriaClinica(paciente=paciente)
    if "enfermedades" in var:
        historiaClinica.enfermedades = var["enfermedades"]
    if "tratamientos" in var:
        historiaClinica.tratamientos = var["tratamientos"]
    historiaClinica.save()
    return historiaClinica
#def create_historiaClinica(form):
 #   historiaClinica = form.save()
  #  historiaClinica.save()
   # return ()


