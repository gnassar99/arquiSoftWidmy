from ..models import paciente

def get_pacientes():
    pacientes = paciente.objects.all()
    return pacientes

def get_paciente(var_pk):
    paciente = paciente.objects.get(pk=var_pk)
    return paciente

def update_paciente(var_pk, new_var):
    paciente = get_paciente(var_pk)
    paciente.name = new_var["name"]
    paciente.save()
    return paciente

def create_paciente(var):
    paciente = paciente(name=var["name"])
    paciente.save()