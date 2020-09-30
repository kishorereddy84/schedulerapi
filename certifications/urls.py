from django.urls import path,include,re_path

from rest_framework import routers


from . import views


urlpatterns = [
    re_path(r'^api/certifications/$', views.certifications_list),
    re_path(r'^api/certifications/(\d+)$', views.certification_detail),
]