'''
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm

from django.views.generic import CreateView
from .forms import SignupUserCreationForm
'''

from django.contrib.auth import forms  
from django.shortcuts import redirect, render  
from django.contrib import messages  
from django.contrib.auth.forms import UserCreationForm  
from .forms import SignupUserCreationForm, SignupEmployerCreationForm  
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
# Create your views here.


class SignupFormView(FormView):
    form_class = SignupUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    def form_valid(self, form):
        form.save()
        return(super().form_valid(form))

class EmployerSignupFormView(FormView):
    form_class = SignupEmployerCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/EmployerSignup.html"

    def form_valid(self, form):
        form.save()
        return(super().form_valid(form))



'''
class SignUpView(CreateView):
    form_class = SignupUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
'''