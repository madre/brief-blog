#coding=utf-8
from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User


class Brief(models.Model):
    brief = models.CharField('七嘴八舌', max_length=1000)
    thumbnail = models.ImageField('配图', upload_to='brief', null=True, blank=True)
    user = models.ForeignKey(User, default=1)
    createtime = models.DateTimeField(auto_now_add=True)
    updatetime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'albums_brief'
        verbose_name = "简语"
        verbose_name_plural = "简语"

    def __unicode__(self):
        return self.brief

    def get_absolute_url(self):
        return reverse('brief_detail', kwargs={'pk': self.pk})

