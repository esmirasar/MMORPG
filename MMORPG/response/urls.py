from django.urls import path
from .views import ResponseListView, ResponseDetailView, ResponseCreateView, delete_response, accept_response
from django.contrib.auth.views import TemplateView

urlpatterns = [
    path('', ResponseListView.as_view(), name='response_list'),
    path('<int:pk>/', ResponseDetailView.as_view(), name='response_detail'),
    path('not-response/', TemplateView.as_view(template_name='response_templates/not_response.html')),
    path('<int:pk>/delete-response/', delete_response, name='delete_response'),
    path('<int:pk>/accept-response/', accept_response, name='accept_response'),

]