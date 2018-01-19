# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.utils import timezone

from django.shortcuts import render, get_object_or_404

from .forms import PostForm

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

#to define our form
def post_new(request):

    #to save the form once details filled up
    if request.method =="POST":
        form=PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author=request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
        return render(request, 'blog/post_edit.html', {'form': form})
#to edit our form
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
