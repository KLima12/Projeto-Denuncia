from django.urls import path
from .import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('listar_denuncias/', views.listar_denuncias,
         name='listar_denuncias'),
    path('responder/<int:id>/',
         views.responder_denuncia, name='responder_denuncia'),
]
