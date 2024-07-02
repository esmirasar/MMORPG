from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Response
from .forms import ResponseCreateForm
from post.models import Post
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView
from .filters import ResponseFilter
from django.db.models.signals import post_save
from dotenv import load_dotenv

load_dotenv()


# Представление списка откликов
class ResponseListView(LoginRequiredMixin, ListView):
    model = Response
    template_name = 'response_templates/response.html'
    context_object_name = 'response_list'
    paginate_by = 3

    def get_queryset(self):
        queryset = Response.objects.filter(user=self.request.user)
        self.filterset = ResponseFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


# Представление детальной информации отклика
class ResponseDetailView(DetailView):
    model = Response
    template_name = 'response_templates/response_detail.html'
    context_object_name = 'response_detail'


# Представление для создания отклика
class ResponseCreateView(LoginRequiredMixin, CreateView):
    success_url = reverse_lazy('post_list')
    model = Response
    form_class = ResponseCreateForm
    template_name = 'response_templates/response_create.html'

    def form_valid(self, form):
        data = form.save(commit=False)
        data.user_id = self.request.user.pk
        data.post_id = self.kwargs['pk']
        data.save()

        # Отправка письма в signals.py

        return super().form_valid(form)


# Удаление отклика
@login_required
def delete_response(request, **kwargs):
    response = Response.objects.get(pk=kwargs['pk'])
    response.delete()
    return redirect('response_list')


# Принятие отклика
@login_required
def accept_response(request, **kwargs):
    response = Response.objects.get(pk=kwargs['pk'])
    response.active = True
    response.save()
    return redirect('response_list')
