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
    nome = models.CharField(max_length=30, blank=True, null=True) # Campo pode ser branco. # Pode ser armazenado como nulo no BD.
    protocolo = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True)
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    categoria = models.CharField(max_length=50, choices=CATEGORIAS)
    ponto_de_referencia = models.CharField("Ponto de Referência",max_length=50,
     blank=True, null=True, help_text="Caso não tenha o endereço completo, descreva o local aqui.")
    endereco = models.CharField(max_length=300, blank=True, null=True) # Obrigatório
    cidade = models.CharField("Cidade", max_length=100, blank=True, null=True)
    bairro = models.CharField("Bairro", max_length=100, blank=True, null=True)
    numero = models.CharField("Número", max_length=20, blank=True, null=True)
    cep = models.CharField("CEP", max_length=9, null=True, blank=True) # Não obrigatório
    estado = models.CharField("Estado (UF)", max_length=2, blank=True, null=True)
        
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
