from django.conf.urls import patterns, url
from testform import views

urlpatterns = patterns('',
    url(r'^$', views.form),
    url(r'^thanks/$', views.thanks_handler),
)
