from django import forms

class LoginForm(forms.Form): 
    nome = forms.CharField(label="Úsuario", max_length=12)
    senha = forms.CharField(label="Senha", widget=forms.PasswordInput)

