#Cada app será responsavel por cuidar das proprias rotas.
from django.urls import path
from galeria.views import index

urlpatterns = [
    path('', index)
]