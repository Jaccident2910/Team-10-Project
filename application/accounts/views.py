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
from django.http import HttpResponseRedirect
from django.urls import reverse
from os import path
import pickle

# Create your views here.
def trophies(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("signup"))
    if request.user.account.solved_puzzles:
        solved_puzzles = pickle.loads(request.user.account.solved_puzzles)
    else:
        solved_puzzles = set()
    trophies = []
    for puzzle in solved_puzzles:
        trophies.append(f"{puzzle}.png")
    return render(request, "trophies.html", {"trophies": trophies})
    

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


def rankings(request):
    queryset = Account.objects.all().order_by('-puzzles_finished').values('id','user__username','user__email','puzzles_finished','solved_puzzles')
    for user in queryset:
        if user["solved_puzzles"]:
            user["solved_puzzles"] = pickle.loads(user["solved_puzzles"])
        else: user["solved_puzzles"] = set()
    return render(request, "rankings.html", {"object_list": queryset})

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