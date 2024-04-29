from django.urls import path
from django.views.generic.base import TemplateView 
from .views import SignupFormView, EmployerSignupFormView, RankingsView
from . import views


urlpatterns = [
    path("signup/", SignupFormView.as_view(), name="signup"),
    path("employersignup/", EmployerSignupFormView.as_view(), name="employersignup"),
    path("rankings/", RankingsView.as_view(), name="rankings"),
    path("trophies/", views.trophies, name="trophies"),
    path("", TemplateView.as_view(template_name="accountPage.html"), name="accountHome"),
]