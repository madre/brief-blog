#coding=utf-8
"""
__create_time__ = '13-10-13'
__author__ = 'Madre'
"""
from django.contrib import admin
from django import forms
from albums.models import Albums, Pictures, CATEGORY


class AlbumsAdminForm(forms.ModelForm):
    class Meta:
        model = Albums

    def __init__(self, *arg, **kwargs):
        # 可以使用form预置或改写某字段的值
        super(AlbumsAdminForm, self).__init__(*arg, **kwargs)
        self.fields['category'].choices = [(csc.id, csc.name) for csc in CATEGORY.objects.filter(m_type='picture')]


class AlbumsAdmin(admin.ModelAdmin):
    form = AlbumsAdminForm
    list_display = ('category', 'title', 'description', 'index')
    list_display_links = ['title']
    list_editable = ['index']
    date_hierarchy = 'createtime'
    list_filter = ['category', 'title']
    search_fields = ['title', 'description']


class PicturesAdmin(admin.ModelAdmin):
    list_display = ('albums', 'title', 'index', 'createtime', 'updatetime')
    list_display_links = ['title']
    list_editable = ['index']
    date_hierarchy = 'createtime'
    search_fields = ['title', ]


admin.site.register(Albums, AlbumsAdmin)
admin.site.register(Pictures, PicturesAdmin)
