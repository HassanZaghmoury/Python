# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    response ="Placeholder to later display all the list of blogs"
    return HttpResponse(response)

def new(request):
    response ="placeholder to display a new form to create a new blog"
    return HttpResponse(response)

def create(request):
    return redirect("/")

def show(request, number):
    # print number
    context ={
        "number":number
    }
    return render(request, "blogs_app/show.html", context)

def edit(request, number):
    print number
    return HttpResponse("placeholder to edit blog " + number)

def delete(request, number):
    return redirect("/")

