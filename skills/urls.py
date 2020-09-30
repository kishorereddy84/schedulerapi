from django.urls import path,include,re_path

from rest_framework import routers


from . import views



urlpatterns = [
    re_path(r'^api/skills/$', views.skills_list),
    re_path(r'^api/skills/(\d+)$', views.skill_detail),
]