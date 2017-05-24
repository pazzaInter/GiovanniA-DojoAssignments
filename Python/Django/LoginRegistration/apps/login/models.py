# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class UserManager(models.Manager):

    def validate(self, data):
        response = []

        # check first_name
        if data['first_name'].isalpha() and len(data['first_name']) > 1:
            response.append([True, '', ''])
        else:
            response.append([False, 'First name must be all letters and at least 2 characters', 'first_name'])

        # check last_name
        if data['last_name'].isalpha() and len(data['last_name']) > 1:
            response.append([True, '', ''])
        else:
            response.append([False, 'Last name must be all letters and at least 2 characters', 'last_name'])

        # check email
        if len(data['email']) > 4:
            response.append([True, '', ''])
        else:
            response.append([False, 'Must be a valid Email format', 'email'])

        # check password
        if len(data['password']) > 7:
            if data['password'] == data['c_password']:
                response.append([True, '', ''])
            else:
                response.append([False, 'Passwords must match', 'c_password'])
        else:
            response.append([False, 'Password must be at least 8 characters', 'password'])

        # check for any errors and return approriate message if so, no errors then just return successful message
        errors = 0
        for each in response:
            if not each[0]:
                errors += 1
        if errors > 0:
            return response
        return [True, '', '']

class User(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = UserManager()
