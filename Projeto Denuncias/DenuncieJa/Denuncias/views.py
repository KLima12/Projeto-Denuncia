from django.shortcuts import render, redirect
from .forms import DenunciaForm, ConsultarProtocoloForm
from .models import Denuncia
from django.contrib import messages  # Para mensagens de sucesso/erro
from DenuncieJa.core.email_service import envia_email


def home(request):
    return render(request, "Denuncias/index.html")


def denuncia(request):
    if request.method == 'POST':
        # Inclui request.FILES para o campo de imagem
        form = DenunciaForm(request.POST, request.FILES)
        if form.is_valid():
            # Salvando os dados no banco de dados e colocando na variavel denuncia.
            denuncia = form.save()
            # Pegando protocolo salvo que está na variavel denuncia
            protocolo = denuncia.protocolo
            email = denuncia.email
            messages.success(request, 'Denúncia enviada com sucesso!')
            if email:
                envia_email(email, protocolo)
            # Redireciona para página de confirmação
            return redirect('confirmacao', protocolo)
        else:
            messages.error(
                request, 'Erro ao enviar a denúncia. Verifique os dados.')
    else:
        form = DenunciaForm()  # Formulário vazio para requisições GET
    return render(request, "Denuncias/denuncia.html", context={'form': form})


def confirmacao(request, protocolo):
    return render(request, "Denuncias/confirmacao.html", {'protocolo': protocolo})


def consultar_denuncia(request):
    if request.method == 'GET':
        form = ConsultarProtocoloForm()
        return render(request, "Denuncias/consultar.html", {"form": form})
        # return redirect('ver_denuncia', protocolo)


def ver_denuncia(request, protocolo):
    # usando values_list() para retornar uma lista de tuplas (Isso é bom para não pesar minha aplicação, já que eu quero buscar somente alguns dados e não todos)
    # contexto = [
    #     {"titulo": titulo, "resposta": resposta, "status": status, "responsavel": responsavel}
    #     for titulo, resposta, status, responsavel in Denuncia.objects.filter(protocolo=protocolo).values_list("titulo", "status", "resposta", "responsavel") # Quero buscar esses
    # ]

    denuncia = Denuncia.objects.filter(
        protocolo=protocolo).select_related("responsavel")
    return render(request, "Denuncias/ver_denuncia.html", {"denuncia": denuncia})
