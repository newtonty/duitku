from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse


def login_user(request):
  if request.method == "POST":
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      return HttpResponseRedirect(reverse('auth:login'))
    else:
      messages.error(request, ("There was an Error Logging In, Try Again..."))
      return HttpResponseRedirect(reverse('auth:login'))
  else:
    return render(request, 'auth/login.html', {})


def signup_user(request):
  if request.method == "POST":
    username = request.POST['username']
    password = request.POST['password']
    re_password = request.POST['re_password']
    full_name = request.POST['full_name']
    if password == re_password:
      user = User.objects.create_user(username=username, password=password, first_name=full_name)
      user.save()
      return HttpResponseRedirect(reverse("auth:login"))
    else:
      error_message = 'Your passwords did not match!'
      return render(request, 'auth/signup.html', {
        'error_message': error_message,
      })
  else:
    return render(request, 'auth/signup.html', {})


def logout_user(request):
  logout(request)
  return HttpResponseRedirect("/")