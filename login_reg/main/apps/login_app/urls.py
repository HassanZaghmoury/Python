from django.conf.urls import url, include
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.create),
    url(r'^success$', views.success),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),    
    url(r'^aditem$', views.aditem),
    url(r'^(?P<id>\d+)/delete$', views.delete),
    # url(r'^(?P<id>\d+)/edit$', views.edit),

]
