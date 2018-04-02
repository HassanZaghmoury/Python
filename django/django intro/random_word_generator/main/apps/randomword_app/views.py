# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
import random
from random import * 
import string

# Create your views here.
def index(request):
    if 'counter' not in request.session:
            request.session['counter'] = 1
    else:
        request.session['counter'] = request.session['counter'] + randint(1,10)
    print request.session['counter']
    print "*"*80
    context = {
        "random": request.session['counter']
    }
    return render(request, 'randomword_app/index.html', context)

def delete(request):
    del request.session["counter"]
    return redirect("/")