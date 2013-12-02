#coding=utf-8
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.views.generic import RedirectView

admin.autodiscover()

from blog.views import HomeView
urlpatterns = patterns('',
    # Examples:
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^brief/', include('brief.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^albums/', include('albums.urls')),
    url(r'^translation/', include('translation.urls')),
    url(r'^resource/', include('resource.urls')),
    url(r'^ckeditor/', include('ckeditor.urls')),

    # 将后台的url修改下
    url(r'^admin/$', RedirectView.as_view(url='/', permanent=True)),
    url(r'^grappelli/', include('grappelli.urls')),  # 美化后台界面的url
    url(r'^backend/', include(admin.site.urls)),
    url(r'^backdoc/', include('django.contrib.admindocs.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
