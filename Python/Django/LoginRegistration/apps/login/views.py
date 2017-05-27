# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import User

def index(request):
    return render(request, 'login/index.html')

def login(request):
    if request.method == "POST":
        credentials = {
            'email': request.POST['email'],
            'password': request.POST['password'],
        }
        print 'Checking credentials'
        valid = User.objects.login(credentials)
        if valid[0]:
            print 'credentials verified'
            request.session['first_name'] = User.objects.get(email=request.POST['email']).first_name
            return redirect('/success')
        else:
            print 'Somethings wrong'
            # create error messages
            messages.error(request, valid[1], extra_tags=valid[2])
            return redirect('/')
    return redirect('/')

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
            print "User created"
            request.session['first_name'] = User.objects.get(email=request.POST['email']).first_name
            print "name assigned to session"
            return redirect('/success')
        else:
            for each in validation:
                messages.error(request, each[1], extra_tags=each[2])
            return redirect('/')
    return redirect('/')

def success(request):
    if 'first_name' in request.session:
        context = {
            'user': request.session['first_name']
        }
        return render(request, 'login/success.html', context)
    return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')
