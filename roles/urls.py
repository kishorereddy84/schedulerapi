
from django.urls import path,include,re_path

from rest_framework import routers


from . import views



urlpatterns = [
    re_path(r'^api/roles/$', views.roles_list),
    re_path(r'^api/roles/(\d+)$', views.role_detail),
]