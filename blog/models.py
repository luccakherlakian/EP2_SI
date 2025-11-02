from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.nome

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_postagem = models.DateTimeField(default=timezone.now)

    categorias = models.ManyToManyField(Category)

    def __str__(self):
        return self.titulo

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    data_postagem = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-data_postagem']

    def __str__(self):
        return f'"{self.texto[:50]}..." por {self.autor.username}'