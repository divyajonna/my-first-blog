# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

#To including code -we need to include model we have written in the models.py file - import
from .models import Post

# Create your views here.
def post_list(request):
    #we want published blog posts sorted by published_date
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
#render() -- Combines a given template with a given context dictionary and returns an HttpResponse object with that rendered text.
