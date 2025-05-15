from django.shortcuts import render
from django.contrib.auth.models import User # Importando o User
from django.contrib.auth import authenticate # Importa Autentificação
from django.http import HttpResponse 
def home(request): 
    return render(request, "responsavel/home.html")

def login(request): 
    if request.method == "GET":
        return render(request, "responsavel/login.html")
    else: 
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        
        user = authenticate(username=username, password=senha)

        if user: 
            return render(request, "responsavel/respostas.html")
        else: 
            return HttpResponse('Email ou senha invalidos')

