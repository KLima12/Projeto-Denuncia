from django.shortcuts import render, redirect
from .forms import Denuncia
from .models import Denuncia
from django.contrib import messages # Para mensagens de sucesso/erro


def home(request):
    return render(request, "Denuncias/index.html")


def denuncia(request):
    if request.method == 'POST':
        form = Denuncia(request.POST, request.FILES) # Inclui request.FILES para o campo de imagem
        if form.is_valid():
            form.save() # Salvando os dados no banco de dados
            messages.success(request, 'Denúncia enviada com sucesso!')
            return redirect('confirmacao') # Redireciona para mesma página
        else: 
            messages.error(request, 'Erro ao enviar a denúncia. Verifique os dados.')
    else: 
        form = Denuncia() # Formulário vazio para requisições GET
    return render(request, "Denuncias/denuncia.html", context={'form': form})

def confirmacao(request): 
    return render(request, "Denuncias/confirmacao.html")

def consultar_denuncia(request): 
    if request.method == "GET": 
        protocolo = request.GET.get("protocolo") # Pegando protocolo que vem do formulario
        if protocolo: # Verificando se o protocolo existe
            denuncia = Denuncia.objects.filter(protocolo=protocolo) # Filtrando as denuncias no banco de dados
            return redirect('ver_denuncia', protocolo=denuncia.protocolo) # redireciona para a exibição da denúncia.
        else: 
            consultar = None
            return render(render, "consultar_denuncia", {'erro': "Protocolo inexistente"})
        
    return render(request, "Denuncias/consultar.html")

def ver_denuncia(request, protocolo):
    return render(request, "ver_denuncia.html", protocolo)