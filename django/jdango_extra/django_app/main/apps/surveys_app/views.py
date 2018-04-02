from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def surveys(request):
    response ="Placeholder to display all the surveys created"
    return HttpResponse(response)

def newsurveys(request):
    response ="placeholder for users to add a new survey"
    return HttpResponse(response)