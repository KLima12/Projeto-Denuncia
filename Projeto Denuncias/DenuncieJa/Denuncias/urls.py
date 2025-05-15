from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"), # Vazio para home
    path('denuncia/', views.denuncia, name="denuncia"),
    path("confirmacao/", views.confirmacao, name="confirmacao"),
    path("consultar/", views.consultar_denuncia, name="consultar"),
    path("ver_denuncia/", views.ver_denuncia,name="ver_denuncia"),
]
