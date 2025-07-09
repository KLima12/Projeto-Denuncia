from django.shortcuts import render, redirect
from django.contrib.auth.models import User  # Importando o User
# Importa Autentificação
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as login_django
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from Denuncias.models import Denuncia
from Responsavel.forms import RespostaForm, LoginForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib import messages  # Para envio de mensagens na outra page


def home(request):
    return render(request, "responsavel/home.html")


def login(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, "responsavel/login.html", {"form": form})
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            senha = form.cleaned_data['password']

            user = authenticate(username=username, password=senha)

            if user:
                # Deixa o úsuario logado ainda quando for redirecionar
                login_django(request, user)
                return redirect('listar_denuncias')
        else:
            return HttpResponse('Email ou senha invalidos')


def logout(request):
    # Faz o logout do úsuario
    auth_logout(request)
    return redirect('login')


@login_required  # Só usuarios logados acessaram
def listar_denuncias(request):
    denuncias = Denuncia.objects.filter(status='pendente')
    return render(request, 'responsavel/listar_denuncias.html', {'denuncias': denuncias})


@login_required
def responder_denuncia(request, id):
    denuncia = get_object_or_404(Denuncia, id=id)

    if request.method == "POST":
        form = RespostaForm(request.POST, instance=denuncia) # Nesse instance, o formulario vai ser carregado com a instancia atual do banco de dados.
        if form.is_valid():
            form.save()
            # Aqui, vou enviar essa mensagem após eu responder uma denuncia
            messages.success(request, 'Denúncia respondida com sucesso!')
            return redirect('listar_denuncias')

    else:
        form = RespostaForm(instance=denuncia)  # Carrega os dados
    return render(request, 'responsavel/responder_denuncias.html', {"denuncia": denuncia, "form": form})
