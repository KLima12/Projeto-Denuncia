from django.core.mail import send_mail # Função para enviar emails
from django.conf import settings
from django.contrib import messages # Para mensagens de sucesso/erro

def envia_email(protocolo,email):
    if email: 
        try: 
            send_mail(
            subject='Seu Protocolo de Denúncia',
            message=f'Seu protocolo é: {protocolo}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
            fail_silently=False,
        )
            return True
        except Exception as e:
            return str(e)  # Retorna o erro como string