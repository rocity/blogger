# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models


class Post(models.Model):
    PUBLISHED = 1
    DRAFT = 2
    ARCHIVED = 3

    STATUSES = (
        (PUBLISHED, 'Published'),
        (DRAFT, 'Draft'),
        (ARCHIVED, 'Archived'),
    )

    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='author')
    category = models.ManyToManyField('blog.Category')
    heading = models.CharField(max_length=50)
    body = models.TextField()
    cover = models.ImageField(upload_to='covers')
    status = models.SmallIntegerField(choices=STATUSES, default=DRAFT)

    date_modified = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Post - {}".format(self.heading)


class Category(models.Model):
    name = models.CharField(max_length=50)
    icon = models.ImageField(upload_to='icons')

    def __str__(self):
        return "Category - {}".format(self.name)

    def get_active_posts_with_category_count(self):
        return Post.objects.filter(category=self.id).count()
