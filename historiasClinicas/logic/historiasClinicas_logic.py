from ..models import HistoriaClinica as historiaClinica

def get_historiasClinicas():
    historiasClinicas = historiaClinica.objects.all()
    return historiasClinicas

def get_historiaClinica(var_pk):
    historiaClinica = historiaClinica.objects.get(pk=var_pk)
    return historiaClinica

def update_historiaClinica(var_pk, new_var):
    historiaClinica = get_historiaClinica(var_pk)
    historiaClinica.name = new_var["name"]
    historiaClinica.save()
    return historiaClinica

def create_historiaClinica(var):
    historiaClinica = historiaClinica(name=var["name"])
    historiaClinica.save()