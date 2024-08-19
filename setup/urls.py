#Essa pagina é responsavel por fazer o roteamento das requisições.
#Aqui as requisições serão roteadas para os apps responsaveis por exemplo galeria/urls.py que vai rotear para as paginas que serão renderizadas pela view.
#Exemplo de roteamento: setup.urls recebe a requisição para galeria, como as rotas da galeria estão incluidas ela responde chamando a index da views, que por sua vez renderiza a index.html da templates.

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('galeria.urls')),#Incluimos as rotas da galeria.
]