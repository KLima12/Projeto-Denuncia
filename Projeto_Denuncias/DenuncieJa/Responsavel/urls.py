from django.urls import path
from .import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('denuncias/', views.denuncias_pendentes, name="denuncias"),
]