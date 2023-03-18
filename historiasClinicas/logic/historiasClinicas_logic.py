from ..models import historiasClinica

def get_historiasClinicas():
    historiasClinicas = historiasClinica.objects.all()
    return historiasClinicas

def get_historiasClinica(var_pk):
    historiasClinica = historiasClinica.objects.get(pk=var_pk)
    return historiasClinica

def update_historiasClinica(var_pk, new_var):
    historiasClinica = get_historiasClinica(var_pk)
    historiasClinica.name = new_var["name"]
    historiasClinica.save()
    return historiasClinica

def create_historiasClinica(var):
    historiasClinica = historiasClinica(name=var["name"])
    historiasClinica.save()