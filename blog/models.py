from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):

    titulo = models.CharField(max_length=200)

    conteudo = models.TextField()

    data_postagem = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo
    
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_postagem = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo
    
class Comment(models.Model):
    # Relação com o Post (um Post tem muitos comentários)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    # Requisito: autor referencia o modelo User 
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    # Requisito: texto do comentário
    texto = models.TextField()

    # Requisito: data de postagem [cite: 131]
    data_postagem = models.DateTimeField(default=timezone.now)

    def __str__(self):
        # Mostra os primeiros 50 caracteres do comentário e o nome do autor
        return f'"{self.texto[:50]}..." por {self.autor.username}'
    
    class Meta:
        # Requisito: ordenar pelo mais recente primeiro
        ordering = ['-data_postagem']

    def __str__(self):
        return f'"{self.texto[:50]}..." por {self.autor.username}'