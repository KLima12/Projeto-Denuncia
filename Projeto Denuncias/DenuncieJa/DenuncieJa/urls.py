from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Denuncias.urls')),  # Vazio para home
    path('responsavel/', include('Responsavel.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
