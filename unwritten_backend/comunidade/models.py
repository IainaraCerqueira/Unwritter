
from django.db import models

from usuarios.models import User
from livros.models import Livro, Genero

class Post(models.Model):
   
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
 
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, related_name='posts', null=True, blank=True)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, related_name='posts', null=True, blank=True)
    titulo = models.CharField(max_length=255)
    texto = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Post de {self.usuario.username} sobre {self.livro or self.genero}'

class Comentario(models.Model):

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comentarios')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentarios')
    texto = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentário de {self.usuario.username} no post {self.post.id}'