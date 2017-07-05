# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='author')
    heading = models.CharField(max_length=50)
    body = models.TextField()
    cover = models.ImageField()

    date_modified = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)


class Category(models.Model):
    name = models.CharField(max_length=50)
    icon = models.ImageField()
