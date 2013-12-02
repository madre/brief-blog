#coding=utf-8
"""
__create_time__ = '13-10-16'
__author__ = 'Madre'
"""
from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import RedirectView, TemplateView

from .views import *


urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/$', TranslationDetailView.as_view(), name='translation_detail'),
    url(r'^$', TranslationListView.as_view(), name='translation'),
)
