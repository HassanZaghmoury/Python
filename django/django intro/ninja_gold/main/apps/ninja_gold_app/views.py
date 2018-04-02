# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
import random
import string
from random import * 


# Create your views here.
def index(request):
    if not "total" in request.session:
        request.session["total"] = 0
    if not "log" in request.session:
        request.session["log"] = []
    return render(request, 'ninja_gold_app/index.html')

def create(request):
    if request.POST['location'] == "farm":
        request.session["new"] = randint(10, 20)
        request.session["total"] += request.session["new"]
        request.session["log"].append("You farmed " + str(request.session["new"]))
    print "farm"
    if request.POST['location'] == "cave":
        request.session["new"] = randint(5, 10)
        request.session["total"] += request.session["new"]
        request.session["log"].append("You mined " + str(request.session["new"]))
    print "cave"
    if request.POST['location'] == "house":
        request.session["new"] = randint(2, 5)
        request.session["total"] += request.session["new"]
        request.session["log"].append("You got paid " + str(request.session["new"]) + " for cleaning")
    print "house"

    if request.POST['location'] == "casino":
        request.session["new"] = randint(-50, 50)
        request.session["total"] += request.session["new"]
        if request.session["new"] < 0:
            request.session["log"].append("You lost " + str(request.session["new"]) + " at the casino")
        else:
            request.session["log"].append("You made " + str(request.session["new"]) + " at the casino")
            
    print "casino"
    return redirect("/")


def restart(request):
    request.session.clear()
    return redirect("/")