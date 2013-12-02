#coding=utf-8
"""
__create_time__ = '13-10-18'
__author__ = 'Madre'
"""
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from resource.models import Resource, Topic


class ResourceListView(ListView):
    context_object_name = 'resource_list'
    template_name = "resource_list.html"
    model = Resource

    def get_context_data(self, **kwargs):
        context = super(ResourceListView, self).get_context_data(**kwargs)
        context["topic_list"] = Topic.objects.all()
        return context


class ResourceDetailView(DetailView):
    context_object_name = 'resource'
    model = Resource
    template_name = "resource_detail.html"

    def get_object(self):
        resource = get_object_or_404(Resource, pk=self.kwargs['pk'])
        return resource

    def get_context_data(self, **kwargs):
        context = super(ResourceDetailView, self).get_context_data(**kwargs)
        context["topic_list"] = Topic.objects.all()
        return context


class TopicDetailView(DetailView):
    context_object_name = 'topic'
    model = Topic
    template_name = "topic_detail.html"

    def get_object(self):
        topic = get_object_or_404(Topic, pk=self.kwargs['pk'])
        return topic

    def get_context_data(self, **kwargs):
        context = super(TopicDetailView, self).get_context_data(**kwargs)
        context["topic_list"] = Topic.objects.all()
        return context