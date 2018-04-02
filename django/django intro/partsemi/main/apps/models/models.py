# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def validate_input(self, post_data):
        errors = []
        if len(post_data['first_name']) < 2:
            errors.append("first name is to short")

        if not post_data["first_name"].isalpha():
            errors.append("only letters in first name")

        if len(post_data['last_name']) < 2:
            errors.append("last name is to short")

        if not post_data["last_name"].isalpha():
            errors.append("only letters in last name")
        return errors

class Username(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)

    objects = UserManager()
