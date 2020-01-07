from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from .forms import RegisterForm

# Create your views here.
def index(request):
    return render(request, 'website/index.html')

def login(request):
    return render(request, 'website/login.html')

def register(request):
    return render(request, 'website/register.html')

def profile(request):
    # context = {'register' : register}
    return render(request, 'website/profile.html')
