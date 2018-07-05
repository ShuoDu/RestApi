# -*- coding:utf8 -*-
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib import admin
from app01 import views


urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^admin/', admin.site.urls),
    url(r'^publist/', views.Publishers.as_view(), name="publist"),
    url(r'^pubdetail/(?P<pk>[0-9]+)$', views.PublishersDetail.as_view(), name="pubdetail"),
    url(r'^booklist/', views.Book.as_view()),
    url(r'^bookdetail/(?P<pk>[0-9]+)$', views.BookDetail.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
urlpatterns = format_suffix_patterns(urlpatterns)