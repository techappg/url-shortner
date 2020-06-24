from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

from shortner import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', views.home, name="home"),
    url(r'^url-shortner/$', views.shrink, name="url-shortner"),
    url(r'^(?P<inputURL>[0-9a-zA-Z]+)/$', views.retrieve, name="virivu"),
]