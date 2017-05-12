# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
import datetime

def index(request):
    print "I am showing the time and date"
    context = {
    'date_hour': datetime.datetime.now()
    }
    return render(request, 'current_time/index.html', context)
