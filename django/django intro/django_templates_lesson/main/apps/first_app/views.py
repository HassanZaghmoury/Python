# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import *

# Create your views here.
def index(request):
    response = "placeholder to later display all the list of blogs"
    return HttpResponse(response)

def new(request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)

def create(request):
    return redirect("/")
    

def blog_number(request, something):
    return HttpResponse("placeholder to blog number  " + something)

def edit(request, something):
    return HttpResponse("placeholder to edit blog number  " + something)

def delete(request, something):
    return HttpResponse("placeholder to delete blog  " + something)

  # views.py
def index(request):
    context = {
        "email" : "blog@gmail.com",
        "name" : "mike"
    }
    return render(request, "ourApp/index.html", context)