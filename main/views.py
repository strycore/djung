# -*- coding: utf-8 -*-
"""Main app views"""

# pylint: disable=E1101

from django.shortcuts import render


def home(request):
    """Homepage view"""
    return render(request, 'home.html')
