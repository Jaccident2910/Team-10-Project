from django.urls import path

from .views import SignupFormView, EmployerSignupFormView


urlpatterns = [
    path("signup/", SignupFormView.as_view(), name="signup"),
    path("employersignup/", EmployerSignupFormView.as_view(), name="employersignup"),
]