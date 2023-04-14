from ..models import Measurement

def get_adendas():
    queryset = Adenda.objects.all().order_by('-dateTime')[:10]
    return (queryset)

def create_adenda(form):
    measurement = form.save()
    measurement.save()
    return ()