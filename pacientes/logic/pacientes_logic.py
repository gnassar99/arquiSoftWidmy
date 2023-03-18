from models import Paciente

def getPacientes():
    pacientes = Paciente.objects.all()
    return pacientes