# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited
def index(request):
  response = "Hello, I am your first request!"
  return HttpResponse(response)

def test(request):
  response = "hello, i am a test"
  return HttpResponse(response)