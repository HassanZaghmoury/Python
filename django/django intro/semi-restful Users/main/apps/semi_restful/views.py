# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from .models import *
from models import Username

from django.contrib import messages


def index(request):
    alluser = Username.objects.all()
    context = {
        "auser": alluser
    }
    return render(request, "semi_restful/index.html", context)

def new(request):
    print "got to New"
    return render(request, "semi_restful/new.html")

def create(request):
    errors = Username.objects.validate_input(request.POST)
    if(len(errors) > 0):
        for error in errors:#this will loop over list of errors
            messages.error(request, error)#this is the message that we put in models
        return redirect("/new")
    else:
        new_user = Username.objects.create(first_name=request.POST["first_name"], last_name=request.POST["last_name"], email=request.POST["email"], created_at=request.POST["created_at"],)
        return redirect('show')

def show(request, id):
    auser = Username.objects.get(id=id)
    context = {
        "oneuser": auser,

    }
    return render(request, "show.html", context)

def delete(request, id):
    Username.objects.filter(id=id).delete()
    return redirect("/")

def edit(request):
    print "something edit"

def update(request):
    print "edit"