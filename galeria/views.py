#Essa pagina é responsavel por renderizar e exibir as paginas web.
from django.shortcuts import render



#Funções que iram receber a requisição e responder com a pagina requisitada.
def index(request):
    #Este dicionario vai ser carregado junto com a pagina index.
    dados = {
    1:  {"nome": "Nebulosa de Carina",
        "legenda": "webbtelescope.org / NASA / James Webb"},
    2:  {"nome": "Galáxia NGC 1079",
       "legenda": "nasa.org / NASA / Hubble"}
    }

    return render (request, 'galeria/index.html', {"cards": dados})

def imagem(request):
    return render(request, 'galeria/imagem.html')
