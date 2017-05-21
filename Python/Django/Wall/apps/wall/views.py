# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import User, Message, Comment
import datetime

# Create your views here.
def index(request):
    request.session['user'] = User.objects.get(first_name='Lebron').id
    context = {
    'users': User.objects.all(),
    'messages': Message.objects.all(),
    'comments': Comment.objects.all(),
    }
    return render(request, 'wall/index.html', context)

def post_message(request):
    if request.method == 'POST':
        new_message = {
            'message': request.POST['message'],
            'user_id': User.objects.get(first_name='Lebron'),
            'created_at': datetime.datetime.now(),
            'updated_at': datetime.datetime.now(),
        }
        add_message = Message(**new_message)
        add_message.save()
        return redirect('/')
    else:
        print 'Your message was not posted'
    return redirect('/')

def post_comment(request):
    if request.method == 'POST':
        new_comment = {
            'comment': request.POST['comment'],
            'message_id': Message.objects.get(id = request.POST['message_id']),
            'user_id': User.objects.get(first_name='Lebron'),
            'created_at': datetime.datetime.now(),
            'updated_at': datetime.datetime.now(),
        }
        add_comment = Comment(**new_comment)
        add_comment.save()
        return redirect('/')
    else:
        print 'Your comment was not posted'
    return redirect('/')
