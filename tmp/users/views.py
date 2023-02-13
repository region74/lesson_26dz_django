from django.shortcuts import render
from django.contrib.auth.views import LoginView


class UserLogin(LoginView):
    template_name = 'users/login.html'

# Create your views here.
