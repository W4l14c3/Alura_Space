#Essa pagina é responsavel por renderizar e exibir as paginas web.
from django.shortcuts import render
from django.http import HttpResponse

#Função que ira receber a requisição e responder com a pagina requisitada.
def index(request):
    return HttpResponse('<h1>Alura Space</h1><p>Bem vindo ao espaço<p>')
