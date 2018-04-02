# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import re
from .models import User, Additem


# Create your views here.
def index(request):
    return render(request, "login_app/index.html")


def create(request):
    print "create page"
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    password = request.POST['password']
    password_confirmation = request.POST['password_confirmation']
    isValid = True

    if not EMAIL_REGEX.match(request.POST['email']):
        isValid = False
        messages.add_message(request, messages.INFO, 'enter vaild email')
    if len(email) < 1:
        isValid = False               
        messages.add_message(request, messages.INFO, 'please enter email')
    if len(first_name) < 2:
        isValid = False
        messages.add_message(request, messages.INFO, 'enter vaild first name')
    if len(last_name) < 2:
        isValid = False
        messages.add_message(request, messages.INFO, 'enter vaild last name')
    if len(password) < 7:
        isValid = False
        messages.add_message(request, messages.INFO, 'password must have at least 8 characters')
    if password_confirmation != password:
        isValid = False
        messages.add_message(request, messages.INFO, 'passwords must match')

    if User.objects.filter(email=email).count() > 0:
        isValid = False
        messages.add_message(request, messages.INFO, 'email already in use')
    # if hired_date.blank:
    #     isValid = False
    #     messages.add_message(request, messages.INFO, 'enter hired date')
    if isValid == False:
        return redirect("/")

    else:
        new_user = User.objects.create(first_name=request.POST["first_name"], last_name=request.POST["last_name"], email=request.POST["email"], date_hired=request.POST["date_hired"], password=request.POST["password"])
        request.session['user'] = new_user.id
        return redirect("/success")

def success(request):
    userid = request.session['user']
    id_info = User.objects.get(id=userid)
    all_entries = Additem.objects.all()
    context = {
      "login_names":id_info,
      "item_info":all_entries

    }
    print "success page"
    return render(request, "login_app/success.html", context)


def login(request):
    email = request.POST['email_login']
    password = request.POST['password_login']    
    isValid = True
    database_user = User.objects.filter(email=email)
    if database_user.count() == 0:
        isValid = False
        messages.add_message(request, messages.INFO, 'no email found')

    if database_user[0].password != password:
        isValid = False
        messages.add_message(request, messages.INFO, 'wrong password')

    if isValid == False:
        return redirect("/")

    else:
        request.session['user'] = database_user[0].id
        return redirect('/success')

def logout(request):
    del request.session["user"]
    return redirect("/")

def delete(request):
    del request.session["item"]
    return redirect("/success")


def aditem(request):
    userid = request.session['user']
    id_info = User.objects.get(id=userid)
    aditem = request.POST.get('aditem')
    Additem.objects.create(item=request.POST["aditem"])
    return redirect("/success")