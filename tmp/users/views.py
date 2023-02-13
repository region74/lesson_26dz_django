from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from .forms import RegUser
from django.views.generic import CreateView
from .models import User


class UserLogin(LoginView):
    template_name = 'users/login.html'

class UserCreate(CreateView):
    model=User
    template_name = 'users/registration.html'
    form_class = RegUser
    success_url = reverse_lazy('users:login')
# Create your views here.
