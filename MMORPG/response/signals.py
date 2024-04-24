from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Response
from django.core.mail import EmailMultiAlternatives


# Сигнал на отправку уведомлений на создание и принятие отклика
@receiver(post_save, sender=Response)
def my_handler(sender, instance, created, **kwargs):
    if created:

        message = EmailMultiAlternatives(subject='Запись создана!',
                                         to=[instance.post.user.email], )
        html_content = f'Здравствуйте! Запись создана!'

        message.attach_alternative(content=html_content,
                                   mimetype='text/html')
        message.send()

    else:
        message = EmailMultiAlternatives(subject='Запись принята!',
                                         to=[instance.user.email], )
        html_content = f'Здравствуйте! Запись принята!'

        message.attach_alternative(content=html_content,
                                   mimetype='text/html')
        message.send()
