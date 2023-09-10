from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, "home.html")


def login(request):
    if request.method == "POST":
        user = request.POST(request)
        pass

    return render(request, "login.html")


def logout(request):
    logout(request.user)
