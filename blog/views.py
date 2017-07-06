# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

from blog.models import Post


def index(request):
    posts = Post.objects.all()

    context = {
        'posts': posts
    }
    return render(request, 'blog/index.html', context)


def post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    context = {
        'post': post
    }
    return render(request, 'blog/post.html', context)
