# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('dashboard')
            else:
                return render(request, 'dashboard/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'dashboard/login.html', {'error_message': 'Invalid login'})
    return render(request, 'dashboard/login.html')


def logout_user(request):
    auth.logout(request)
    return redirect('indexlogin')


@login_required()
def dashboard(request):
    user = request.user
    return render(request, 'dashboard/dashboard.html' ,{'user_name':user})