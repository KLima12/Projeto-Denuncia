from django.contrib import admin
from .models import Denuncia

@admin.register(Denuncia)
class DenunciaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'protocolo', 'status', 'data_envio') # Registra o modelo Denuncia no Django Admin.
    search_fields = ('titulo', 'protocolo', 'descricao') # Define quais colunas aparecem na lista de denúncias no painel.
    list_filter = ('status', 'data_envio') # Permite buscar por título, protocolo ou descrição.
    readonly_fields = ('protocolo', 'data_envio') # Adiciona filtros por status e data de envio.


