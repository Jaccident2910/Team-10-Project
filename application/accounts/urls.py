from django.urls import path

from .views import SignupFormView


urlpatterns = [
    path("signup/", SignupFormView.as_view(), name="signup"),
]