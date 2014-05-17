# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


#class Document(models.Model):
#    title = models.CharField(max_length=255)
#    slug = models.SlugField()
#    author = models.ForeignKey(User)
#    content = models.TextField()
#    created_at = models.DateTimeField(auto_now=True)
#
#    class Meta:
#        ordering = ['-created_at']
#
#    def __unicode__(self):
#        return self.title
#
#    def get_absolute_url(self):
#        return '/my-object/%s-%d' % (self.slug, self.id)
#
#    def save(self, *args, **kwargs):
#        self.slug = slugify("%s-%d" % (self.title, self.id))
