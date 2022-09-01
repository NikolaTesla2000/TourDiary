from django.urls import path
from . import views  # '.' works in a similar way as 'this',signifies the same dir
from django.conf.urls import url

urlpatterns = [
    url(r'^$',views.welcome),
    url(r'index',views.index),
    url(r'^Images/(?P<value>[\w-]+)/$', views.Images,name="views_images"),
    url(r'contact',views.contact),
]