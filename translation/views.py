#coding=utf-8
"""
__create_time__ = '13-10-16'
__author__ = 'Madre'
"""
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Translation


class TranslationDetailView(DetailView):
    context_object_name = 'translation'
    model = Translation
    template_name = "ts_detail.html"

    def get_object(self):
        translation = get_object_or_404(Translation, pk=self.kwargs['pk'])
        return translation


class TranslationListView(ListView):
    context_object_name = 'translation_list'
    template_name = "ts_list.html"
    paginate_by = 7
    model = Translation

    def get_context_data(self, **kwargs):
        context = super(TranslationListView, self).get_context_data(**kwargs)
        context['sidepanel'] = Translation.objects.filter(position='sidepanel')
        return context
