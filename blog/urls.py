from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.post_list, name='post_list'),

    #URL in the  file to point Django to a view named post_detail, that will show an entire blog post

    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),

    #URL in the  file to point Django to a view named post_new, that will show an entire blog post
    url(r'^post/new/$', views.post_new, name='post_new'),
]
