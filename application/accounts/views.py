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
from .forms import SignupUserCreationForm  
from django.urls import reverse_lazy
# Create your views here.



def signUp (request):  
    if request.POST == 'POST':  
        form = SignupUserCreationForm()  
        if form.is_valid():  
            print("valid form!")
            form.save()
            redirect(reverse_lazy("login"))  
    else:  
        form = SignupUserCreationForm()  
    context = {  
        'form':form  
    }  
    return render(request, 'registration/signup.html', context)  



'''
class SignUpView(CreateView):
    form_class = SignupUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
'''