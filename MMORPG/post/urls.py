from django.urls import path
from .views import PostListView, PostListDetailView, PostCreateView, PostUpdateView, subscription
from response.views import ResponseCreateView

urlpatterns = [
    path('', PostListView.as_view(), name="post_list"),
    path('<int:pk>/', PostListDetailView.as_view(), name="post_id"),
    path('post_create/', PostCreateView.as_view(), name="post_create"),
    path('post_update/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('post_update/<int:pk>/response_create/', ResponseCreateView.as_view(), name='response_create'),
    path('subscription/', subscription, name='subscription'),
]
