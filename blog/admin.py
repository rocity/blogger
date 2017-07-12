# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from blog.models import Post, Category, Comment


class CommentAdmin(admin.ModelAdmin):
    '''
        Admin View for Comment
    '''
    list_display = ('username', 'body', )


admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment, CommentAdmin)
