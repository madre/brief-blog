#coding=utf-8
# Create your views here.
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from blog.models import Blog, CATEGORY, Tag
from translation.models import Translation
from albums.models import Albums


class HomeView(ListView):
    context_object_name = 'blogs'
    model = Blog
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['albums'] = Albums.objects.order_by("index")[0:3]
        context['sidepanel'] = Translation.objects.order_by("index", "-createtime")[0:7]
        return context


class BlogDetailView(DetailView):
    context_object_name = 'blog'
    model = Blog
    template_name = "blog_detail.html"

    def get_object(self):
        blog = get_object_or_404(Blog, pk=self.kwargs['pk'])
        return blog
    
    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context['sidepanel'] = Blog.objects.filter(position='sidepanel').order_by("index", "createtime")[0:5]
        return context


class BlogListView(ListView):
    context_object_name = 'blog_list'
    template_name = "blog_list.html"
    paginate_by = 7

    def get_queryset(self):
        category = get_object_or_404(CATEGORY, slug=self.kwargs['slug'])
        month = self.kwargs.get('month')
        year = self.kwargs.get('year')
        if month and year:
            result = Blog.objects.filter(category=category, show=True,
                                         createtime__year=self.kwargs["year"],
                                         createtime__month=month
                                         ).exclude(position='sidepanel').order_by('-createtime')
        elif year:
            result = Blog.objects.filter(category=category, show=True,
                                         createtime__year=self.kwargs["year"],
                                         ).exclude(position='sidepanel').order_by('-createtime')
        else:
            result = Blog.objects.filter(category=category, show=True).exclude(position='sidepanel')
        return result

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(BlogListView, self).get_context_data(**kwargs)
        # Add in the publisher
        context['slug'] = self.kwargs['slug']
        context['archive'] = Blog.objects.filter(show=True).dates('createtime', 'month', order='DESC')
        context['tags'] = Tag.objects.filter(blog__category__slug=self.kwargs['slug']).distinct()
        context['sidepanel'] = Blog.objects.filter(category__slug=self.kwargs['slug'], show=True, position='sidepanel')
        return context


class BlogByTagsView(ListView):
    context_object_name = 'blog_list'
    template_name = "blog_list.html"
    paginate_by = 7

    def get_queryset(self):
        result = Blog.objects.filter(category__slug=self.kwargs['slug'], tags__name=self.kwargs['tags'],
                                     show=True).exclude(position='sidepanel')
        return result

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(BlogByTagsView, self).get_context_data(**kwargs)
        # Add in the publisher
        context['slug'] = self.kwargs['slug']
        context['archive'] = Blog.objects.filter(show=True).dates('createtime', 'month', order='DESC')
        context['tags'] = Tag.objects.filter(blog__category__slug=self.kwargs['slug']).distinct()
        context['sidepanel'] = Blog.objects.filter(tags__name=self.kwargs['tags'], category__slug=self.kwargs['slug'],
                                                   show=True, position='sidepanel')
        return context
