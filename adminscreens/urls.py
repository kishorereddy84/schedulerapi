from django.urls import path, include, re_path

from rest_framework import routers


from . import views


urlpatterns = [
    re_path(r'^api/emprequired/$', views.requiredemp_list),
    re_path(r'^api/emprequired/(\d+)$', views.requiredemp_detail),
]
