from django import forms
from django.forms import Textarea
from .models import Denuncia


class DenunciaForm(forms.ModelForm):
    class Meta:
        model = Denuncia
        fields = ["titulo", "imagem", "descricao", "email"]
        widgets = {
            'descricao': Textarea(attrs={'cols': 80, 'rows': 10}),
        }


class ConsultarProtocoloForm(forms.Form):
    protocolo = forms.CharField(
        label="Digite seu protocolo da denuncia", max_length=50)
