from django.urls import path
from .views import UserRegistrationView
from django.contrib.auth.views import LoginView


urlpatterns = [
    path("create", UserRegistrationView.as_view(), name="user_registration"),
    path("login", LoginView.as_view(template_name="login.html"), name="login"),
]
