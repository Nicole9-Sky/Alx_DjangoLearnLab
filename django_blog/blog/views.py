from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegistrationForm

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("blog-home")
    else:
        form = UserRegisterForm()
    return render(request, "blog/register.html", {"form": form})

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("blog-home")
    else:
        form = AuthenticationForm()
    return render(request, "blog/login.html", {"form": form})

def user_logout(request):
    logout(request)
    return redirect("blog-home")

@login_required
def profile(request):
    return render(request, "blog/profile.html")
