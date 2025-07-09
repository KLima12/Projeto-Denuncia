from django import forms
from django.forms import Textarea
from .models import Denuncia


class DenunciaForm(forms.ModelForm):
    class Meta:
        model = Denuncia
        fields = ["nome","titulo", "categoria","descricao","imagem" ,"email", "cep", "endereco","bairro", "numero", "estado", "ponto_de_referencia"]
        widgets = {
            'descricao': Textarea(attrs={'cols': 80, 'rows': 10}),
            'ponto_de_referencia': Textarea(attrs={'rows': 3, 'placeholder': 'Ex: Em frente à padaria Pão do Céu, ao lado de uma árvore grande.'}),
            
        }

    # Aqui fiz uma lógica no formulário. Se o nome não for fornecido, o úsuario terá o nome 'Anônimo' salvo no banco de dados.
    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if not nome: # Se não tiver o nome
            return 'Anônimo' # Retorna anônimo
        return nome
    
    def clean(self): 
        cleaned_data = super().clean()

        # Pegue os valores dos campos de localização
        cep = cleaned_data('cep')
        endereco = cleaned_data('endereco')
        ponto_de_referencia = cleaned_data.get('ponto_de_referencia')

        if not (cep or endereco) and not ponto_de_referencia:
            # Se nem o endereço estruturado nem o ponto de referencia foram preenchidos, gera um erro.
            raise forms.ValidationError(
                "Por favor, forneça uma localização. Preencha o CEP, o endereço manual ou um ponto de referência"
            )
        return cleaned_data
    
class ConsultarProtocoloForm(forms.Form):
    protocolo = forms.CharField(
        label="Digite seu protocolo da denuncia", max_length=50)
    

