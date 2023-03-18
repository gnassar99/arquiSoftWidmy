from models import HistoriaClinica

def getHistoriasClinicas():
    historiasClinicas = HistoriaClinica.objects.all()
    return historiasClinicas