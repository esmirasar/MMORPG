from django.urls import path
from .views import RegistrView, accept, SignInView, accept_in, logout_user

urlpatterns = [
    path('', RegistrView.as_view(), name='registration'),
    path('accept/<str:token>/', accept, name='accept'),
    path('sign-in/', SignInView.as_view(), name='sign-in'),
    path('accept-in/<str:token>/', accept_in, name='accept-in'),
    path('logout/', logout_user, name='logout')
]