from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Denuncias.urls')), # Vazio para home
    path('responsavel/', include('Responsavel.urls')),
]
