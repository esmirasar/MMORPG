import os

import dotenv
from django.db.models.signals import post_save
from django.dispatch import receiver
from dotenv import load_dotenv

from .models import Token, User
from django.core.mail import EmailMultiAlternatives

load_dotenv()


# Сигнал на отправку ссылки на регистрацию и вход
@receiver(post_save, sender=Token)
def my_handler(sender, instance, created, **kwargs):
    print(instance.username)
    if instance.username:
        message = EmailMultiAlternatives(subject='accept',
                                         to=[instance.email])

        html_content = (f'<h1>Здравствуйте, {instance.username}</h1>'
                        f'<p>Для регистрации перейдите по <a href="{os.getenv("HREF")}accept/{instance.token}/">ссылке</a></p>')

        message.attach_alternative(content=html_content,
                                   mimetype='text/html')
        message.send()

    else:
        message = EmailMultiAlternatives(subject='sign-in',
                                         to=[instance.email])

        html_content = (f'<h1>Здравствуйте, {instance.username}!</h1>'
                        f'<p>Для входа перейдите по  <a href="{os.getenv("HREF")}accept-in/{instance.token}/">ссылке</a></p>')

        message.attach_alternative(content=html_content,
                                   mimetype='text/html')
        message.send()
