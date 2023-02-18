from django.urls import path
from .views import UserRegistrationView


urlpatterns = [path("create", UserRegistrationView.as_view(), name="user_registration")]
