from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.new),
    url(r'^create$', views.create),
    url(r'^(?P<something>\d+)$', views.blog_number),
    url(r'^(?P<something>\d+)/edit$', views.edit),
    url(r'^(?P<something>\d+)/delete$', views.delete),            
]
