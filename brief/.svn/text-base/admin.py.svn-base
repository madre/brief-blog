#coding=utf-8
"""
__create_time__ = '13-10-13'
__author__ = 'Madre'
"""
from django.contrib import admin
from brief.models import Brief


class BriefAdmin(admin.ModelAdmin):
    list_display = ('pk', 'brief', 'createtime', 'thumbnail', 'updatetime')
    list_display_links = ['brief']
    date_hierarchy = 'createtime'
    search_fields = ['brief', ]


admin.site.register(Brief, BriefAdmin)