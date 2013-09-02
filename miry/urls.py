from django.conf.urls import patterns, include, url
from settings import MEDIA_ROOT

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
import views
import kursy.views

urlpatterns = patterns('',
    url(r'^$', kursy.views.index),
    url(r'^kursy/', include('miry.kursy.urls')),

    url(r'^user/', include('miry.users.urls')),
    # Examples:
    # url(r'^$', 'miry.views.home', name='home'),
    # url(r'^miry/', include('miry.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': MEDIA_ROOT}),
)
