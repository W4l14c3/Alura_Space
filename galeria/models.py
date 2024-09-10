from django.db import models

# Essa classe é um model pois representa uma tabela no banco de dados
class Fotografia(models.Model):
    nome = models.CharField(max_length=100,  null=False, blank=False)
    legenda = models.CharField(max_length=150,  null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    foto = models.CharField(max_length=100,  null=False, blank=False)

    # Função str subscrita que retorna o nome de um campo da classe fotografia.
    def __str__(self):
        return f"Fotografia [nome={self.nome}]"