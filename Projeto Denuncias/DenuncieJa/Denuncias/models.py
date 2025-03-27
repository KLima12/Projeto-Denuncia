from django.db import models
import uuid

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
    imagem = models.ImageField(upload_to='imagens/')
    data_envio = models.DateField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    responsavel = models.ForeignKey('Responsavel', on_delete=models.SET_NULL, null=True, blank=True)
    resposta = models.TextField(blank=True, null=True) # Resposta do responsavel

    def __str__(self):
        return f"{self.titulo} - {self.protocolo}"


class Responsavel(models.Model): 
    nome = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nome 
    