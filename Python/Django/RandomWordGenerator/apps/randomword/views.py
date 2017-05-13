# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
import urllib2
import random

# our website with a list of random words
word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"

# pull words from our site
response = urllib2.urlopen(word_site)

# assign our words to a variable
txt = response.read()

# place each word within a list
WORDS = txt.splitlines()
attempts = 0

def index(request):
    global attempts
    # picks a random word from our list
    rand_word = random.choice(WORDS).upper()

    # adds one to our number of attempts
    attempts += 1

    context = {
        'word': rand_word,
        'attempts': attempts
    }

    return render(request, 'randomword/index.html', context)
