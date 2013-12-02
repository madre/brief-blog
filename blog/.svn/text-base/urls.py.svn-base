#coding=utf-8
"""
__create_time__ = '13-10-13'
__author__ = 'Madre'
"""
from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

from .views import *

urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/$', BlogDetailView.as_view(), name='blog_detail'),
    url(r'^(?P<slug>[-\w]+)/$', BlogListView.as_view(), name='blog_list'),
    url(r'^(?P<slug>[-\w]+)/(?P<tags>[-\w]+)/$', BlogByTagsView.as_view(), name='blog_tags'),
    url(r'^topic/(?P<slug>[-\w]+)/documentation/$', RedirectView.as_view(url='/resource/', permanent=True)),
    url(r'^(?P<slug>[-\w]+)/(?P<year>\d{4})/$', BlogListView.as_view(), name="yearly_archive"),
    url(r'^(?P<slug>[-\w]+)/(?P<year>\d{4})/(?P<month>\d{2})/$', BlogListView.as_view(), name="monthly_archive"),
    #url(r'^tag/(?P<tag>[\w-]+)/$', BlogListView.as_view(), name='tag_archive'),
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
