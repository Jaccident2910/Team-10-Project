from django.urls import path

from .views import signUp


urlpatterns = [
    path("signup/", signUp, name="signup"),
]