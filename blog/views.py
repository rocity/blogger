# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

from .models import Post, Category
from .forms import PostForm, CommentForm


def index(request):
    posts = Post.objects.all()

    context = {
        'posts': posts
    }
    return render(request, 'blog/index.html', context)


def post(request, post_id):
    post_obj = get_object_or_404(Post, id=post_id)
    comments = post_obj.comments.all()
    comment_form = CommentForm()

    if request.method == 'POST':
        comment_form = CommentForm(request.data)
        if comment_form.is_valid():
            comment_form.save()

    context = {
        'post': post_obj,
        'comments': comments,
        'comment_form': comment_form,
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


def dashboard_my_posts(request, post_status=None):
    user = request.user

    qs_filter = {
        'author': user
    }

    if post_status is not None:
        qs_filter = {
            'author': user,
            'status': post_status
        }

    # All posts (unfiltered)
    user_posts = Post.objects.filter(**qs_filter)

    context = {
        'posts': user_posts
    }
    return render(request, 'blog/dashboard_my_posts.html', context)


def dashboard_create_post(request):
    success = False
    post_id = None
    user = request.user
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.author = user
            f.save()

            success = True
            post_id = f.id

    context = {
        'form': form,
        'success': success,
        'post_id': post_id
    }

    return render(request, 'blog/dashboard_create_post.html', context)


def categories(request):
    categories_list = Category.objects.all()

    context = {
        'categories': categories_list
    }
    return render(request, 'blog/category_list.html', context)


def category(request, category_name):
    category_obj = get_object_or_404(Category, name__iexact=category_name)
    posts = Post.objects.filter(category=category)

    context = {
        'category': category_obj,
        'posts': posts,
    }

    return render(request, 'blog/posts_by_category.html', context)
