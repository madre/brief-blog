#coding=utf-8
# Create your views here.
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render
from brief.forms import BriefCreateForm

from brief.models import Brief
from utils.renders import JSONResponseMixin


class BriefDetailView(JSONResponseMixin, DetailView):
    context_object_name = 'brief_detail'
    model = Brief
    template_name = "brief_detail.html"

    def get_object(self):
        result = get_object_or_404(Brief, pk=self.kwargs['pk'])
        return result

    def get(self, request, *args, **kwargs):
        # DetailView中已经包含了这部分，默认不需要写，除非有特别需要，比如当前要判断是否返回json
        context = self.get_object()
        if self.json_required(request):
            # 示例，笨方法返回json数据。 问题在:什么情况应该把返回queryset和返回json混合在一个view里面
            return self.render_to_response(context)
        return render(request, self.template_name, {self.context_object_name: context})


class BriefListView(ListView):
    context_object_name = 'brief_list'
    template_name = "brief_list.html"
    paginate_by = 7

    def get_queryset(self):
        return Brief.objects.order_by("-createtime")


class BriefCreateView(CreateView):
    form_class = BriefCreateForm
    template_name = 'brief_form.html'