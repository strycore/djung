# -*- coding: utf-8 -*-
# pylint: disable=E1101
"""Main app views"""
from django.http import Http404
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required


def home(request):
    """Homepage view"""
    return render(request, 'home.html')
