from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page
from django.views import generic
from django.urls import path

from . import views

urlpatterns = [
    url('^$', views.ConstructHomeView.as_view(), name="index"),
    
]