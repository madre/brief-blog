#coding=utf-8
from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User
from blog.models import CATEGORY


class Albums(models.Model):
    category = models.ForeignKey(CATEGORY)
    title = models.CharField('标题', max_length=255, null=True, blank=True)
    description = models.TextField('描述', max_length=500, null=True, blank=True)
    thumbnail = models.ImageField('封面', upload_to='albums', null=True, blank=True)
    index = models.IntegerField('排序', max_length=11, default=0)
    createtime = models.DateTimeField(auto_now_add=True, editable=False)
    updatetime = models.DateTimeField(auto_now=True, editable=False)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-createtime',]
        verbose_name = "相册"
        verbose_name_plural = "相册"


class Pictures(models.Model):
    albums = models.ForeignKey(Albums)
    title = models.CharField('描述', max_length=255, null=True, blank=True)
    thumbnail = models.ImageField('图片', upload_to='pictures', null=True, blank=True)
    index = models.IntegerField('排序', max_length=11, default=0)
    createtime = models.DateTimeField(auto_now_add=True, editable=False)
    updatetime = models.DateTimeField(auto_now=True, editable=False)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-createtime',]
        verbose_name = "图片"
        verbose_name_plural = "图片"
