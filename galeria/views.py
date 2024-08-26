#Essa pagina é responsavel por renderizar e exibir as paginas web.
from django.shortcuts import render


#Funções que iram receber a requisição e responder com a pagina requisitada.
def index(request):
    return render (request, 'galeria/index.html')

def imagem(request):
    return render(request, 'galeia/imagem.html')
