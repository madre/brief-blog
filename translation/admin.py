#coding=utf-8
"""
__create_time__ = '13-10-13'
__author__ = 'Madre'
"""
from django.contrib import admin
from translation.models import Translation


class TranslationAdmin(admin.ModelAdmin):
    list_display = ('m_type', 'title', 'tran_title', 'user', 'index', 'show')
    list_display_links = ['title']
    list_editable = ['show', 'index']
    date_hierarchy = 'createtime'
    list_filter = ['show', 'title']
    search_fields = ['title', 'origin_content', 'tran_content', 'o_t_content']


admin.site.register(Translation, TranslationAdmin)
