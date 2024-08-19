#Essa pagina é responsavel por fazer o roteamento das requisições.
#Aqui as requisições serão roteadas para os apps responsaveis por exemplo galeria/urls.py que vai rotear para as paginas que serão renderizadas pela view.

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('galeria.urls'))#Incluimos as rotas da galeria.
]