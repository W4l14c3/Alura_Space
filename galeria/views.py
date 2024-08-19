#Essa pagina é responsavel por renderizar e exibir as paginas web.
from django.shortcuts import render


#Função que ira receber a requisição e responder com a pagina requisitada.
def index(request):
    return render (request, 'index.html')
