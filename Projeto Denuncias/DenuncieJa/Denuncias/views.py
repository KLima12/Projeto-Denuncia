from django.shortcuts import render


def home(request):
    return render(request, "Denuncias/index.html")


def denuncia(request):
    return render(request, "Denuncias/denuncia.html")
