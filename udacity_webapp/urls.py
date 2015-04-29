from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^search/', include('search.urls',namespace="search")),
    url(r'^testform/', include('testform.urls',namespace="testform")),
    url(r'^unit2/', include('rot13.urls',namespace="rot13")),
    url(r'^signup/', include('signup.urls',namespace="signup"))

    # Examples:
    # url(r'^$', 'udacity_webapp.views.home', name='home'),
    # url(r'^udacity_webapp/', include('udacity_webapp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
