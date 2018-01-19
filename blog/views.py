# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.utils import timezone

from django.shortcuts import render, get_object_or_404

#To including code -we need to include model we have written in the models.py file - import
from .models import Post

# Create your views here.
def post_list(request):
    #we want published blog posts sorted by published_date
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
    #render() -- Combines a given template with a given context dictionary and returns an HttpResponse object with that rendered text.

#create a post detail view of primary key
  #we want to get one and only one blog post. To do this, we can use querysets, like this:
#first define the pot_detail function:
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
