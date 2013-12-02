#coding=utf-8
"""
__create_time__ = '13-10-18'
__author__ = 'Madre'
"""
from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

from .views import *

urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/$', ResourceDetailView.as_view(), name='resource_detail'),
    url(r'^$', ResourceListView.as_view(), name='resource_list'),
    url(r'^all/$', ResourceListView.as_view(), name='resource_all'),
    url(r'^topic/(?P<pk>\d+)/$', TopicDetailView.as_view(), name='topic_detail'),
    url(r'^topic/(?P<slug>[-\w]+)/$', TopicDetailView.as_view(), name='topic_slug'),
    #url(r'^topic/$', TopicDetailView.as_view(), name='topic_detail'),
    #url(r'^topic/(?P<slug>[-\w]+)/documentation/$', RedirectView.as_view(url='/resource/', permanent=True)),
)