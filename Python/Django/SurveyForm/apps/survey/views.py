# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

def index(request):
    return render(request, 'survey/index.html')

def process(request):
    if request.method == 'POST':
        if 'times' not in request.session:
            request.session['times'] = 1
        else:
            request.session['times'] += 1

        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']

        return redirect('/result')
    else:
        return redirect('/')

def result(request):
    return render(request, 'survey/result.html')
