# usuarios/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser


from livros.models import Livro

class User(AbstractUser):
   
    livros_lidos = models.ManyToManyField(Livro, related_name='lido_por', blank=True)
    livros_lendo = models.ManyToManyField(Livro, related_name='lendo_por', blank=True)
    livros_quero_ler = models.ManyToManyField(Livro, related_name='desejado_por', blank=True)
    def __str__(self):
        return self.username