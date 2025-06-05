from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"), # Vazio para home
    path('denuncia/', views.denuncia, name="denuncia"),
    path("confirmacao/<str:protocolo>", views.confirmacao, name="confirmacao"),
    path("consultar/", views.consultar_denuncia, name="consultar"),
    path("ver_denuncia/<str:protocolo>", views.ver_denuncia,name="ver_denuncia"),
]
