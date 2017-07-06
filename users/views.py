# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

from .forms import LoginForm


def login(request):
    login_form = LoginForm()

    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                auth_login(request, user)
                return redirect('/')
            else:
                login_form.add_error(None, 'There are no users that match your credentials.')

    context = {
        'login_form': login_form
    }
    return render(request, 'users/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('login')
