from Django import HttpResponse

def home(request):
    return HttpResponse("Hello, world. Django views.")