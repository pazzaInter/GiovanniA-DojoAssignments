# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import User

def index(request):
    return render(request, 'login/index.html')

def login(request):
    pass
    if request.method == "POST":
        return redirect('/success')

def register(request):
    if request.method == "POST":
        print "-"*100
        registration = {
            'first_name' : request.POST['first_name'],
            'last_name' : request.POST['last_name'],
            'email' : request.POST['email'],
            'password' : request.POST['password'],
            'c_password' : request.POST['c_password'],
        }
        validation = User.objects.validate(registration)
        if len(validation) < 4:
            del registration['c_password']
            print registration
            User.objects.create(**registration)
            return redirect('/success')
        else:
            for each in validation:
                messages.error(request, each[1], extra_tags=each[2])
            return redirect('/')

    return redirect('/')

def success(request):
    context = {
        'user': User.objects.get(id=1)
    }
    return render(request, 'login/success.html', context)
