
from django.db import models

class Genero(models.Model):
   
    nome = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nome

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=150)
    ano_publicacao = models.IntegerField(null=True, blank=True)
    nacionalidade = models.CharField(max_length=100, blank=True)
    sinopse = models.TextField()
    paginas = models.IntegerField()
    tempo_medio_leitura = models.DurationField()
    capa = models.ImageField(upload_to='capas_livros/', null=True, blank=True)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, related_name='livros')

    def __str__(self):
        return self.titulo