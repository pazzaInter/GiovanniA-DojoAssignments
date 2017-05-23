# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.exceptions import ObjectDoesNotExist
from django.db import models

class UserManager(models.Manager):
    def validate(self, username):
        if len(username) > 8 and len(username) < 16:
            try:
                self.get(username = username)
                return (False, "Username already taken, choose another")
            except ObjectDoesNotExist:
                return (True, "") # username meets length requirement and not taken
        elif len(username) < 9:
            return (False, "Username must be between 8 and 16 characters.") # username is not long enough
        elif len(username) > 15:
            return (False, "Username must be between 8 and 16 characters.") # username is too long

class User(models.Model):
    # first_name = models.CharField(max_length = 45)
    # last_name = models.CharField(max_length = 45)
    # email = models.CharField(max_length = 200)
    # hashpw = models.CharField(max_length = 255)
    username = models.CharField(max_length = 15)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = UserManager()
