# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .forms import LoginForm


def login(request):
    login_form = LoginForm()
    if request.method == 'POST':
        pass

    context = {
        'login_form': login_form
    }
    return render(request, 'users/login.html', context)
