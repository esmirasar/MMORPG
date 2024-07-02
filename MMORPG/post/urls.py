from django.urls import path
from .views import PostListView, PostListDetailView, PostCreateView, PostUpdateView, subscription

urlpatterns = [
    path('', PostListView.as_view(), name="post_list"),
    path('<int:pk>/', PostListDetailView.as_view(), name="post_id"),
    path('post_create/', PostCreateView.as_view(), name="post_create"),
    path('post_update/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('subscription/', subscription, name='subscription'),
]
