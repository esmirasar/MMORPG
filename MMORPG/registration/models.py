from django.db import models
from django.contrib.auth.models import AbstractUser


# Переопределение модели пользователя
class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)


# Модель токена
class Token(models.Model):
    token = models.CharField(max_length=255)
    username = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
