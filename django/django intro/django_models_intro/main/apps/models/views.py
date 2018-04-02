# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import *
from models import Username

from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'models/index.html')

def new(request):
    return render(request, 'models/new.html')

def create(request):
    errors = Username.objects.validate_input(request.POST)
    if(len(errors) > 0):
        for error in errors:#this will loop over list of errors
            messages.error(request, error)#this is the message that we put in models
        return redirect("/new")
    else:
        new_user = Username.objects.create(name=request.POST["name"], age=request.POST["age"])
        return redirect('/success')

def success(request):
    something = Username.objects.all()
    context = {
        "names": something
    }
    return render(request, 'models/success.html', context)