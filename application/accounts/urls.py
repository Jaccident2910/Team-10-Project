from django.urls import path

from .views import SignupFormView, EmployerSignupFormView, RankingsView


urlpatterns = [
    path("signup/", SignupFormView.as_view(), name="signup"),
    path("employersignup/", EmployerSignupFormView.as_view(), name="employersignup"),
    path("rankings/", RankingsView.as_view(), name="rankings"),
]