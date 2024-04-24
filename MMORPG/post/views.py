from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView
from .models import Post, Subscription
from .forms import PostCreateForm, PostUpdateForm
from django.urls import reverse_lazy, reverse
import datetime
import os
from dotenv import load_dotenv

load_dotenv()


# Представление списка постов
class PostListView(ListView):
    model = Post
    template_name = 'post_templates/post.html'
    context_object_name = 'post_list1'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['not_subscribe'] = not Subscription.objects.filter(user_id=self.request.user.pk)
        return context


# Представление детальной информации 1 поста
class PostListDetailView(DetailView):
    model = Post
    template_name = 'post_templates/post_detail.html'
    context_object_name = 'post_detail'


# Представление создания поста
class PostCreateView(LoginRequiredMixin, CreateView):
    success_url = reverse_lazy('post_list')
    model = Post
    form_class = PostCreateForm
    template_name = 'post_templates/post_create.html'

    def form_valid(self, form):
        data = form.save(commit=False)
        data.user_id = self.request.user.pk
        data.save()
        return super().form_valid(form)


# Представление редактирования поста
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostUpdateForm
    template_name = 'post_templates/post_update.html'

    def get_success_url(self, **kwargs):
        return reverse('post_id', kwargs={'pk': self.get_form_kwargs()['instance'].pk})

    def form_valid(self, form):
        data = form.save(commit=False)
        data.time_update = datetime.datetime.now()
        data.save()
        return super().form_valid(form)


# Подписка
def subscription(request):
    Subscription.objects.create(user_id=request.user.pk)
    return redirect('post_list')
