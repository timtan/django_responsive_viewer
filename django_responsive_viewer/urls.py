__author__ = 'tim'
from django.conf.urls import patterns, include, url
from .views import responsive_listing



urlpatterns = patterns('',
    url(r'^$', responsive_listing)
)

