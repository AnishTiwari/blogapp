from __future__ import unicode_literals
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .forms import UserForm

from django.shortcuts import render, HttpResponseRedirect,redirect


# Create your views here.

def index(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return render(request, 'dashboard/dashboard.html')
    context = {
        "form": form,
    }
    return render(request, 'register/register.html', context)
