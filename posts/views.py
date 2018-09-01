# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Posts
# Create your views here.
def add(request):
    user = request.user
    return render(request,'./posts/add.html',{"user":user})

def blogged(request):
    print "hello"
    if request.method == 'POST':
        data = Posts()
        data.title = request.POST.get('title')
        data.body = request.POST.get('body')
        data.save()
        user = request.user
        return render(request, "dashboard/dashboard.html",{'user_name':user})
    else:
        return render(request, 'posts/add.html')

def viewblog(request):
    posts = Posts.objects.all()
    print posts
    user = request.user

    return render(request, 'dashboard/dashboard.html', {'context1':posts,'user_name':user })


def details(request, id):
    posts = Posts.objects.get(id=id)
    user = request.user
    return render(request, 'dashboard/dashboard.html', {'context1':posts, 'user_name':user})