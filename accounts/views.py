from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from accounts.forms import UserCreationForm


# Create your views here.


def login_view(request):
    if request.user.is_authenticated:
        return redirect("landing_page")
    context = {"error_messages": []}
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged In")
            return HttpResponseRedirect(request.GET.get('next', '/profile'))
        else:
            context["error_messages"] = ["Invalid Username or Passwords"]

    return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect("login")


def register_view(request):
    if request.user.is_authenticated:
        return redirect("landing_page")
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully created an account")
            return redirect("login")
    else:
        form = UserCreationForm()
    context = {
        "form": form
    }
    return render(request, "signup.html", context)


@login_required
def profile_view(request):
    return render(request, "userProfile.html")
