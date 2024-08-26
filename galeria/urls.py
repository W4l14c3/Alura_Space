#Cada app será responsavel por cuidar das proprias rotas.
from django.urls import path
#Abaixo nos chamamos as funções que renderizam as paginas.html da views.py
from galeria.views import index, imagem

urlpatterns = [
    path('', index),
    path('imagem/', imagem)
]