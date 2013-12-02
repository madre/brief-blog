#coding=utf-8
"""
__create_time__ = '13-10-18'
__author__ = 'Madre'
"""
from django.contrib import admin
from resource.models import Resource, ResourceType, Topic


class ResourceTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'help_text')
    list_display_links = ['name']


class TopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'help_text', 'official_website')
    list_display_links = ['name']
    search_fields = ['name', 'official_website']


class ResourceAdmin(admin.ModelAdmin):
    list_display = ('resource_type', 'title', 'help_text', 'show')
    list_display_links = ['title']
    list_editable = ['show']
    date_hierarchy = 'createtime'
    list_filter = ['resource_type', 'title']
    search_fields = ['title', 'description', 'help_text']


admin.site.register(ResourceType, ResourceTypeAdmin)
admin.site.register(Resource, ResourceAdmin)
admin.site.register(Topic, TopicAdmin)

