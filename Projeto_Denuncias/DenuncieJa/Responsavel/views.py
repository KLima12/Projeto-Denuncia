from django.shortcuts import render, redirect
from django.contrib.auth.models import User # Importando o User
from django.contrib.auth import authenticate # Importa Autentificação
from django.http import HttpResponse 
from Denuncias.models import Denuncia # Importando o banco de dados Denuncias de outro app
from .forms import LoginForm

def home(request): 
    return render(request, "responsavel/home.html")

def login(request): 
    """View de login para usuario"""
    if request.method == "GET":
        form = LoginForm() 
        return render(request, "responsavel/login.html", context={'form': form})
    else: 
        form = LoginForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            senha = form.cleaned_data['senha']
            user = authenticate(username=nome, password=senha)
        if user: 
            return redirect("denuncias")
        else:
            return HttpResponse('Email ou senha invalidos')

def denuncias_pendentes(request): 
    """Listar as denuncias pendentes que faltam respostas"""
    pendentes = Denuncia.objects.filter(status="pendente")
    print("Quantidade de denúncias:", pendentes.count())
    for denuncia in pendentes:
        print(f"Título: {denuncia.titulo}, Protocolo: {denuncia.protocolo}, Status: {denuncia.status}")
    return render(request, "responsavel/denuncias.html", {"pendentes": pendentes})