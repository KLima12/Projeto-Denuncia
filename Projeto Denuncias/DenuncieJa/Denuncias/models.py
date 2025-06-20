from django.db import models
import uuid
from django.contrib.auth.models import User  # Importa o modelo User


class Denuncia(models.Model):

    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('resolvido', 'Resolvido'),
    ]

    CATEGORIAS = [
        ('meio_ambiente', 'Meio Ambiente'),
        ('maus_tratos_animais', 'Maus-tratos a Animais'),
        ('perturbacao_sossego', 'Perturbação do Sossego'),
        ('obra_irregular', 'Obra Irregular'),
        ('acumulo_lixo', 'Acúmulo de Lixo'),
        ('poluicao_sonora', 'Poluição Sonora'),
        ('seguranca_publica', 'Segurança Pública'),
        ('violencia_domestica', 'Violência Doméstica'),
        ('tráfico_drogas', 'Tráfico de Drogas'),
        ('saude_publica', 'Saúde Pública'),
        ('outros', 'Outros'),
    ]
    nome = models.CharField(max_length=30, default="Anônimo")
    protocolo = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True)
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    categoria = models.CharField(max_length=50, choices=CATEGORIAS)
    
    endereco = models.CharField(max_length=300) # Obrigatório
    cidade = models.CharField("Cidade", max_length=100)
    bairro = models.CharField("Bairro", max_length=100)
    numero = models.CharField("Número", max_length=20)
    cep = models.CharField("CEP", max_length=9, null=True) # Não obrigatório
    
    numero = models.CharField
    
    # Usando blank para dizer que não é obrigatório enviar uma imagem
    imagem = models.ImageField(upload_to='imagens/', blank=True)
    # Data e horário atualizada automaticamente
    data_envio = models.DateField(auto_now=True)
    email = models.EmailField()
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='pendente')
    responsavel = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)  # Usa User do Django
    # Resposta do responsavel
    resposta = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.titulo} - {self.protocolo}"
