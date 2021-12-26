from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the IJR index.")


def judecatori(request):
    return HttpResponse("Hello, world. You're at the IJR Judecatori.")


def procese(request):
    return HttpResponse("Hello, world. You're at the IJR Procese.")


def programari(request):
    return HttpResponse("Hello, world. You're at the IJR Programari.")
