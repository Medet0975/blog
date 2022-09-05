from django.contrib.auth import views
from django.urls import path
from .views import UserCreateView


urlpatterns = [
    path("login/", views.LoginView.as_view(), name='login'),
    path("logout/", views.LogoutView.as_view(), name='logout'),
    path("register/", UserCreateView.as_view(), name='register'),
]