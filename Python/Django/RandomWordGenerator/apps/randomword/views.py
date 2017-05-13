# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
import urllib2
import random

# website with a list of random words
word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"

# pull words from our site
response = urllib2.urlopen(word_site)

# assign our words to a variable
txt = response.read()

# place each word within a list
WORDS = txt.splitlines()

def index(request):
    # picks a random word from our list
    rand_word = random.choice(WORDS).upper()

    # check to see if we are counting attempts, if yes then keep adding 1, else start at 1
    if 'attempts' in request.session:
        request.session['attempts'] += 1
    else:
        request.session['attempts'] = 1

    context = {
        'word': rand_word,
        'attempts': request.session['attempts']
    }

    return render(request, 'randomword/index.html', context)
