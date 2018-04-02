from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^surveys$', views.surveys),
    url(r'^newsurveys$', views.newsurveys)                    
]