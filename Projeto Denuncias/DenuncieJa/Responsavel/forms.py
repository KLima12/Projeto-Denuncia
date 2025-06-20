from Denuncias.models import Denuncia
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='Nome do Usúario', max_length=50)
    password = forms.CharField(label="Senha", widget=forms.PasswordInput)


class RespostaForm(forms.ModelForm):
    class Meta:
        model = Denuncia
        fields = ['status', 'resposta']
        labels = {
            'resposta': "Resposta da denúncia"
        }
        widgets = {
            'resposta': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
