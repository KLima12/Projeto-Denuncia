from django.db import models
import uuid
from django.contrib.auth.models import User # Importa o modelo User

class Denuncia(models.Model): 

    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('em_analise', 'Em Análise'),
        ('resolvido', 'Resolvido'),
        ('rejeitado', 'Rejeitado'),
    ]
    protocolo = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='imagens/', blank=True) # Usando blank para dizer que não é obrigatório enviar uma imagem
    data_envio = models.DateField(auto_now=True) # Data e horário atualizada automaticamente
    email = models.EmailField()  
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    responsavel = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True) # Usa User do Django
    resposta = models.TextField(blank=True, null=True) # Resposta do responsavel

    def __str__(self):
        return f"{self.titulo} - {self.protocolo}"




    