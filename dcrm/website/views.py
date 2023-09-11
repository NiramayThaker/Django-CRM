from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . import forms

# @login_required(login_url='login/')
# Create your views here.
def home(request):

    # else:
    return render(request, "home.html")


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['pswd']
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            messages.success(request, "Login Successfull")
            return redirect('home')
        else:
            messages.error(request, "Couldn't log in")
            return redirect('home')
        
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    messages.success(request, "User logged out.!")
    return redirect('home')


def register_user(request):
    reg_form = forms.RegistrationForm()

    context = {'reg_form': reg_form}
    return render(request, "user_reg.html", context=context)
