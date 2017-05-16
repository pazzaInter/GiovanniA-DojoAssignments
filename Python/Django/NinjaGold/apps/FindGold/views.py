# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
import random
import datetime

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'logs' not in request.session:
        request.session['logs'] =[]
    return render(request, 'FindGold/index.html')

def process(request):
    print '-'*20
    timestamp = datetime.datetime.now().strftime("%Y/%m/%d %I:%M %p")
    if 'farm' in request.POST:
        new_gold = random.randint(10,20)
        request.session['gold'] += new_gold
        location = 'farm'

    elif 'cave' in request.POST:
        new_gold = random.randint(5,10)
        request.session['gold'] += new_gold
        location = 'cave'

    elif 'house' in request.POST:
        new_gold = random.randint(2,5)
        request.session['gold'] += new_gold
        location = 'house'
    elif 'casino' in request.POST:
        earns_takes = random.randint(0,1)
        new_gold = random.randint(0,50)
        location = 'casino'
        if earns_takes == 0: # lose gold
            request.session['gold'] -= new_gold
            request.session['logs'].append((0, 'Entered a casino and lost ' + str(new_gold) + ' golds... Ouch. (' + str(timestamp) + ')'))
            return redirect('/')
        elif earns_takes == 1: # earn gold
            request.session['gold'] += new_gold

    request.session['logs'].append((1, 'Earned ' + str(new_gold) + ' golds from the ' + location + '! (' + str(timestamp) + ')'))
    return redirect('/')

def new(request):
    request.session.clear()
    return redirect('/')
