# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def validate_input(self, post_data):
        
        # EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        # first_name = post_data['first_name']
        # last_name = post_data['last_name']
        # email = post_data['email']
        errors = []

        # # if not EMAIL_REGEX.match(post_data['email']):
        # #     errors.append("enter vaild email")

        # if len(post_data['email']) < 1:
        #     errors.append("please enter email")

        if len(post_data['first_name']) < 2:
            errors.append("enter vaild frist name")

        # if not post_data["first_name"].isalpha():
        #     errors.append("only letters in first_name")

        # if len(post_data['last_name']) < 2:
        #     errors.append("enter vaild last name")

        # if not post_data["last_name"].isalpha():
        #     errors.append("only letters in last name")
        # return errors

    # if User.objects.filter(email=email).count() > 0:
    #     messages.add_message(request, messages.INFO, 'email already in use')
    
        return errors

    # else:
    #     new_user = User.objects.create(first_name=request.POST["first_name"], last_name=request.POST["last_name"], email=request.POST["email"], date_hired=request.POST["date_hired"], password=request.POST["password"])
    #     request.session['user'] = new_user.id
    #     return redirect("/success")

class Username(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)

    objects = UserManager()