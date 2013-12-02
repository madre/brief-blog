#coding=utf-8
# Create your views here.
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render

from albums.models import Albums, CATEGORY
from utils.renders import JSONResponseMixin

import logging


class AlbumsDetailView(JSONResponseMixin, DetailView):
    context_object_name = 'albums_detail'
    model = Albums
    template_name = "pic_detail.html"

    def get_object(self):
        albums = get_object_or_404(Albums, pk=self.kwargs['pk'])
        albums.pictures_set.all()
        return albums

    def get(self, request, *args, **kwargs):
        logging.info(request)
        # DetailView中已经包含了这部分，默认不需要写，除非有特别需要，比如当前要判断是否返回json
        context = self.get_object()
        if self.json_required(request):
            # 示例，笨方法返回json数据。 问题在:什么情况应该把返回queryset和返回json混合在一个view里面
            return self.render_to_response(context)
        return render(request, self.template_name, {self.context_object_name: context})


class AlbumsListView(ListView):
    context_object_name = 'albums_list'
    template_name = "pic_list.html"
    #paginate_by = 12

    def get_queryset(self):
        category = get_object_or_404(CATEGORY, slug=self.kwargs['slug'])
        return category.albums_set.order_by("index", "createtime")
