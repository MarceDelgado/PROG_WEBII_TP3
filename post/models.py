from django.db import models
from django.contrib.auth.models import User



class Post(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fechaDepublicacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Comment(models.Model):
   post = models.ForeignKey(Post, related_name='comments',on_delete=models.CASCADE)  # Relación con Post
   author = models.ForeignKey(User, on_delete=models.CASCADE)  # Autor del comentario
   content = models.TextField()  # Contenido del comentario
   created_date = models.DateTimeField(auto_now_add=True)  # Fecha de creación

   def __str__(self):
        return f'Comment de {self.author.username} en {self.post.titulo}'
