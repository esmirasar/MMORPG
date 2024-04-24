from django.db import models
from .category import CATEGORY
from django_ckeditor_5.fields import CKEditor5Field
from registration.models import User


# Модель поста
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = CKEditor5Field('Text', config_name='extends')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(null=True, blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY)

    def __str__(self):
        return f'{self.user}, {self.title}, {self.category}'


# Модель подписки на рассылку
class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    subscription = models.BooleanField(default=True)
