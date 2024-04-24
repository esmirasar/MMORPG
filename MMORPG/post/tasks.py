from celery import shared_task

from django.core.mail import EmailMultiAlternatives


from datetime import date, timedelta

from post.models import Post
from .models import Subscription

# Еженедельная рассылка
@shared_task
def every_monday_newsletter():

    day_week = date.today()

    while day_week.weekday() != 0:
        day_week -= timedelta(1)

    weekly_posts = Post.objects.filter(data_creation__date__gte=day_week)

    html_content = (f'<h1>Новости недели</h1>'
                    f'<h2>На этой недели вышли обновления. Посмотреть можно на сайте</h2>')

    for user in Subscription.objects.all():
        message = EmailMultiAlternatives(subject='Новости недели',
                                         to=[user.email])
        message.attach_alternative(html_content, mimetype='text/html')
        message.send()