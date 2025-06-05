from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import DenunciaForm
from .models import Denuncia
from django.contrib import messages # Para mensagens de sucesso/erro
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.email_service import envia_email


def home(request):
    return render(request, "Denuncias/index.html")


def denuncia(request):
    if request.method == 'POST':
        form = DenunciaForm(request.POST, request.FILES) # Inclui request.FILES para o campo de imagem
        if form.is_valid():
            denuncia = form.save() # Salvando os dados no banco de dados e colocando na variavel denuncia.
            protocolo = denuncia.protocolo # Pegando protocolo salvo que está na variavel denuncia
            email = denuncia.email
            messages.success(request, 'Denúncia enviada com sucesso!')
            if email: 
                envia_email(email, protocolo)
            return redirect('confirmacao', protocolo) # Redireciona para página de confirmação
        else: 
            messages.error(request, 'Erro ao enviar a denúncia. Verifique os dados.')
    else: 
        form = DenunciaForm() # Formulário vazio para requisições GET
    return render(request, "Denuncias/denuncia.html", context={'form': form})

def confirmacao(request, protocolo):
    return render(request, "Denuncias/confirmacao.html", {'protocolo': protocolo})

def consultar_denuncia(request): 
    if request.method == "GET": 
        protocolo = request.GET.get("protocolo") # Pegando protocolo que vem do formulario
        if protocolo: # Verificando se o protocolo existe
            return redirect('ver_denuncia', protocolo) # redireciona para a exibição da denúncia com o protocolo.
        
    return render(request, "Denuncias/consultar.html")

def ver_denuncia(request, protocolo):
    # usando values_list() para retornar uma lista de tuplas (Isso é bom para não pesar minha aplicação, já que eu quero buscar somente alguns dados e não todos)
    # contexto = [
    #     {"titulo": titulo, "resposta": resposta, "status": status, "responsavel": responsavel} 
    #     for titulo, resposta, status, responsavel in Denuncia.objects.filter(protocolo=protocolo).values_list("titulo", "status", "resposta", "responsavel") # Quero buscar esses
    # ]

    denuncia = Denuncia.objects.filter(protocolo=protocolo).select_related("responsavel")
    return render(request, "Denuncias/ver_denuncia.html", {"denuncia": denuncia})