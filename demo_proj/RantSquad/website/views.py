from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from .models import Post

# Create your views here.
def index(request):
    return render(request, 'website/index.html')

def profile(request):
    posts = Post.objects.all()
    return render(request, 'website/profile.html',{'posts':posts})
