# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django import forms

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    password_confirmation = models.CharField(max_length=255)
    date_hired = models.DateTimeField(auto_now_add= False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Additem(models.Model):
    item = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return "[%s] %s" % (self.item)