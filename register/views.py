from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def register(response):
    if response.method == "POST":
        print(response.POST)
        if response.POST['password1'] != response.POST['password2']:
            messages.error(response, "Password confirmation is not match")
            return render(response, 'register/register.html')
        user = User.objects.create_user(response.POST['username'], response.POST['email'], response.POST['password1'])
        user.save()
        messages.success(response, "Sign Up Successfully")
        return redirect('/login')
    return render(response, 'register/register.html')


def log_in(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.error(request, "Login Failed !")
            return redirect('/login')
    return render(request, 'login/login.html')


def log_out(request):
    logout(request)
    return redirect('/')
