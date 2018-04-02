from django.conf.urls import url, include
from django.contrib import admin
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name ='accounts'


urlpatterns = [
    url(r'^signup/$', views.signup_view, name="signup")   
]
