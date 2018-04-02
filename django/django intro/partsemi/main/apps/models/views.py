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
        new_user = Username.objects.create(first_name=request.POST["first_name"], last_name=request.POST["last_name"], email=request.POST["email"])
        return redirect('/success')

def success(request):
    something = Username.objects.all()
    context = {
        "data": something
    }
    return render(request, 'models/success.html', context)

def delete(request, id):
    Username.objects.get(id=id).delete()
    return redirect("/new")

def show(request, id):
    something = Username.objects.get(id=id)
    context = {
        "data": something
    }
    return render(request, 'models/show.html', context)

def edit(request, id):
    edituser = Username.objects.filter(id=id)
    if len(edituser) > 0:
        edituser1 = edituser[0]
        context = {
            "useredit": edituser1
        }
        return render(request, "models/edit.html", context)

def update(request, id):
    update_list = Username.objects.filter(id=id)
    if len(update_list) > 0:
        updateuser = update_list[0]
        updateuser.first_name = request.POST['first_name']
        updateuser.last_name = request.POST['last_name']
        updateuser.email = request.POST['email']
        updateuser.save()
    return redirect("/{}/edit".format(id))