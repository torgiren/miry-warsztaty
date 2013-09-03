from django.conf.urls import patterns, include, url
from views import *

urlpatterns = patterns('',
    url(r'^$', user_index),
    url(r'^login/', user_login),
    url(r'^register/', user_register),
    url(r'^logout/', user_logout),
    url(r'^preferencje/', user_preferencje),
    url(r'^preferencje_lista/', user_preferencje_lista),
)
