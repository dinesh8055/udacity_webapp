from django.conf.urls import patterns, url
from signup import views

urlpatterns = patterns('',
    url(r'^$', views.form),
    url(r'^thanks/$', views.thanks_handler),
)
