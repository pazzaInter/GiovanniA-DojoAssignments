# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
from .models import *

def index(request):
    return render(request, 'validation/index.html')

def validate(request):
    print request.POST['username']
    username = request.POST['username']
    if User.objects.validate(username)[0]:
        User.objects.create(username = username)
        messages.add_message(request, messages.SUCCESS, 'The username you entered "' + str(username) + '" is valid. Thank you!')
        return redirect('/success')
    elif not User.objects.validate(username)[0]:
        messages.add_message(request, messages.ERROR, User.objects.validate(username)[1])
        return redirect('/')

def success(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'validation/success.html', context)

def delete(request, id):
    User.objects.get(id = id).delete()
    return redirect('/success')
