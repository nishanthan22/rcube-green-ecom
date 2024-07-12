from django.shortcuts import render, redirect
from django.contrib.auth import logout


# Create your views here.
def user_login(request):
    return render(request, "login.html")


def user_logout(request):
    logout(request)
    return redirect("/")

