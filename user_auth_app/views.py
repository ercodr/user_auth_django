from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def loginPage(req):
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(req, "User not found!")
        
        user = authenticate(req, username=username, password=password)
        if user:
            login(req, user)
            return redirect('home')

    return render(req, 'user_auth_app/login.html')


def registerPage(req):
    return render(req, 'user_auth_app/register.html')


@login_required(login_url='login')
def homePage(req):
    return render(req, 'user_auth_app/home.html')


@login_required(login_url='login')
def logoutUser(req):
    logout(req)
    return redirect('login')