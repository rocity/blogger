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


def dashboard(request):
    user = request.user

    published_posts_count = Post.objects.filter(author=user, status=Post.PUBLISHED).count()
    draft_posts_count = Post.objects.filter(author=user, status=Post.DRAFT).count()
    archived_posts_count = Post.objects.filter(author=user, status=Post.ARCHIVED).count()

    context = {
        'published_posts_count': published_posts_count,
        'draft_posts_count': draft_posts_count,
        'archived_posts_count': archived_posts_count
    }

    return render(request, 'blog/dashboard.html', context)

def dashboard_my_posts(request):
    user = request.user

    # All posts (unfiltered)
    user_posts = Post.objects.filter(author=user)

    context = {
        'posts': user_posts
    }
    return render(request, 'blog/dashboard_my_posts.html', context)
