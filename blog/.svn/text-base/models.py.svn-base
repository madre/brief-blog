#coding=utf-8
from django.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

CATEGORY_CLASS = ['blog', 'picture', 'theme']


# Create your models here.
class CATEGORY(models.Model):
    name = models.CharField('栏目名称', max_length=60, unique=True)
    slug = models.SlugField('slug', max_length=255)
    help_text = models.CharField('简要说明', max_length=255, null=True, blank=True)
    description = models.TextField('详细说明', null=True, blank=True)
    thumbnail = models.ImageField('缩略图', upload_to='category', null=True, blank=True)
    official_website = models.URLField('跳转地址', null=True, blank=True)
    m_type = models.CharField('栏目类别', max_length=36, choices=zip(CATEGORY_CLASS, CATEGORY_CLASS))

    class Meta:
        ordering = ['name',]
        verbose_name = "网站栏目"
        verbose_name_plural = "网站栏目"
        #app_label = u"栏目分类"

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        if self.description and not self.help_text:
            self.help_text = self.description.replace("\n", " ")[:220]
        super(CATEGORY, self).save(*args, **kwargs)


class Tag(models.Model):
    """标签"""
    name = models.CharField(max_length=200, unique=True, verbose_name=u'名称')

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog_tags', kwargs={'tags': self.name})

    class Meta:
        verbose_name_plural = verbose_name = u'标签'


POSITION_CHOICES = ['sidepanel', 'home']


class Blog(models.Model):
    category = models.ForeignKey(CATEGORY)
    slug = models.SlugField('slug', max_length=255, blank=True, default='')
    title = models.CharField('标题', max_length=255, unique=True)
    thumbnail = models.ImageField('配图', upload_to='blog', null=True, blank=True)
    content = RichTextField()
    #content = models.TextField('内容')
    position = models.CharField('位置', max_length=36, choices=zip(POSITION_CHOICES, POSITION_CHOICES))
    index = models.IntegerField('排序', max_length=11, default=0)
    show = models.BooleanField('是否显示', default=True)
    user = models.ForeignKey(User)
    createtime = models.DateTimeField(auto_now_add=True, editable=False)
    updatetime = models.DateTimeField(auto_now=True, editable=False)
    tags = models.ManyToManyField(Tag, blank=True, verbose_name=u'标签')

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Blog, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-createtime',]
        verbose_name = "博客"
        verbose_name_plural = "博客"
