import os

from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Token, User
from .token import RANDOM_STRING
from django.contrib.auth import authenticate, login, logout


# Представление регистрации
class RegistrView(TemplateView):
    template_name = 'registration/registration.html'

    def post(self, *args, **kwargs):
        token = f'{self.request.POST["csrfmiddlewaretoken"]}+{RANDOM_STRING}'
        Token.objects.create(token=token,
                             username=self.request.POST['username'],
                             email=self.request.POST['email'],
                             password=self.request.POST['password'])
        # Отправка письма в signals.py
        return redirect('registration')


# Регистрация
def accept(request, **kwargs):
    token = kwargs['token']

    try:
        data = Token.objects.get(token=token)
    except:
        return HttpResponse('Error')

    User.objects.create_user(username=data.username,
                             email=data.email,
                             password=data.password)

    data.delete()

    return redirect('sign-in')


# Представление для входа
class SignInView(TemplateView):
    template_name = 'registration/sign_in.html'

    def post(self, *args, **kwargs):
        user = authenticate(email=self.request.POST['email'],
                            password=self.request.POST['password'])

        if user:
            token = f'{self.request.POST["csrfmiddlewaretoken"]}+{RANDOM_STRING}'
            Token.objects.create(token=token,
                                 email=self.request.POST['email'],
                                 password=self.request.POST['password'])
        # Отправка письма в signals.py
        return redirect('sign-in')


# Вход
def accept_in(request, **kwargs):
    data = Token.objects.get(token=kwargs['token'])

    user = authenticate(email=data.email,
                        password=data.password)

    login(request, user)

    data.delete()

    return redirect('post_list')


# Выход
def logout_user(request):
    logout(request)

    return redirect('sign-in')
