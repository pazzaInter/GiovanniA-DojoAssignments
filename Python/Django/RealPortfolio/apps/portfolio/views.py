# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
    print "This is rendering Home page-index"
    return render(request, 'portfolio/index.html')

def testimonials(request):
    print "This is rendering testimonials page"
    return render(request, 'portfolio/testimonials.html')

def about(request):
    print "This is rendering about me"
    return render(request, 'portfolio/about.html')

def projects(request):
    print "This is rendering my projects"
    return render(request, 'portfolio/projects.html')
