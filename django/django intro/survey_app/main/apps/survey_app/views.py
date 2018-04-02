# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, "survey_app/index.html")

def create(request):
    # return render(request, "survey_app/success.html")
    if request.method == "POST":
        print "*"*80
	print request.POST
    print request.POST['name']
    print request.POST['location']
    print request.POST['language']
    print request.POST['comment']
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']    
    
    if 'counter' not in request.session:
        request.session['counter'] = 1
    else:
        request.session['counter'] = request.session['counter'] + 1
    print request.session['counter']
    print "*"*80
    return redirect("/success")

def success(request):
    return render(request, "survey_app/success.html")