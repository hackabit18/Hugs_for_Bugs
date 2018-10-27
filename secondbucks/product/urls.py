from . import views
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

urlpatterns = [
    #/
    url('^$', views.index, name='index'),
]