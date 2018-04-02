from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^register$', views.register),
    url(r'^users/new$', views.new),    
    url(r'^login$', views.login),
    url(r'^users$', views.users)                                  
]