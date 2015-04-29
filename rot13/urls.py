from django.conf.urls import patterns, url
from rot13 import views

urlpatterns = patterns('',
    url(r'^rot13/$', views.cipher),
)
