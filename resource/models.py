#coding=utf-8
"""
__create_time__ = '13-10-17'
__author__ = 'Madre'
"""
from django.contrib.auth.models import User
from django.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify


class Topic(models.Model):
    name = models.CharField(max_length=60, unique=True)
    slug = models.SlugField(max_length=255)
    help_text = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    thumbnail = models.ImageField(upload_to='topics', null=True, blank=True)
    official_website = models.URLField(null=True, blank=True)

    class Meta:
        ordering = ['name', ]
        verbose_name = "主题/题材"
        verbose_name_plural = "主题/题材"

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('topic_detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        if self.description and not self.help_text:
            self.help_text = self.description.replace("\n", " ")[:220]
        super(Topic, self).save(*args, **kwargs)


class ResourceType(models.Model):
    name = models.CharField(max_length=60, unique=True)
    slug = models.SlugField(max_length=255)
    help_text = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        ordering = ['name', ]
        verbose_name = "代码类型"
        verbose_name_plural = "代码类型"

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('resource_list', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(ResourceType, self).save(*args, **kwargs)

LEVELS = ['beginner', 'intermediate', 'advanced']


class Resource(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, blank=True, default='')
    url = models.URLField(unique=True)
    help_text = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True, default='')
    resource_type = models.ForeignKey(ResourceType)
    level = models.CharField('Difficulty Level', max_length=30, choices=zip(LEVELS, LEVELS))
    topics = models.ManyToManyField(Topic)
    user = models.ForeignKey(User)
    #rating = RatingField(range=5, weight=10, use_cookies=True, allow_delete=True)
    createtime = models.DateTimeField(auto_now_add=True, editable=False)
    updatetime = models.DateTimeField(auto_now=True, editable=False)
    show = models.BooleanField(default=True)

    class Meta:
        ordering = ['-createtime', ]
        verbose_name = "资源"
        verbose_name_plural = "资源"

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('resource_detail', kwargs={'pk': self.id})

    def save(self, *args, **kwargs):
        #INFO Checks if present because admins have option to change slug
        if not self.slug:
            self.slug = slugify(self.name)
        if self.description and not self.help_text:
            self.help_text = self.description.replace("\n", " ")[:220]
        super(Resource, self).save(*args, **kwargs)
