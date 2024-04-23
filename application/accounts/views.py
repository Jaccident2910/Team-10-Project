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
from django.contrib.auth.models import User
from .models import Account
from .forms import SignupUserCreationForm, SignupEmployerCreationForm  
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic.list import ListView

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


class RankingsView(ListView):
    template_name = "rankings.html"
    
    def get_queryset(self):
        #queryset = User.objects.all()
        queryset = Account.objects.all().order_by('-puzzles_finished').values('id','user__username','puzzles_finished')
        return queryset

    '''
    def get_context_data(self, **kwargs):
        context = super(RankingsView, self).get_context_data(**kwargs)
        all_accounts = Account.objects.all().order_by('-puzzles_finished').values()
        all_users = User.objects.all()
        context.update({'accounts': all_accounts})
        context.update({'users': all_users})
        return context
    '''






'''
class SignUpView(CreateView):
    form_class = SignupUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
'''