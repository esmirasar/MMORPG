from django.db import models
from registration.models import User
from post.models import Post


# Модель отклика
class Response(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField(max_length=100)
    date_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'User {self.user} response to post! Text: {self.text}'
