# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def validate_input(self, post_data):
        errors = []
        if len(post_data['name']) < 2:
            errors.append("name is to short")

        if not post_data["name"].isalpha():
            errors.append("only letters in name")

        if len(post_data['age']) == 0:
            errors.append("please put an age")
            
        elif int(post_data["age"]) > 65:
            errors.append("Your to old go away")
        return errors

class Username(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()


    objects = UserManager()
