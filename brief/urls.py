#coding=utf-8
"""
__create_time__ = '13-10-13'
__author__ = 'Madre'
"""
from django.conf.urls import patterns, include, url

from .views import *

urlpatterns = patterns('',
    url(r'^create/$', BriefCreateView.as_view(), name="brief_create"),
    url(r'^(?P<pk>\d+)/$', BriefDetailView.as_view(), name="brief_detail"),
    url(r'^$', BriefListView.as_view(), name="brief"),
)


