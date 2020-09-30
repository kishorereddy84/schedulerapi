from django.urls import path, include, re_path

from rest_framework import routers


from . import views


urlpatterns = [
    re_path(r'^api/departments/$', views.department_list),
    re_path(r'^api/departments/(\d+)$', views.department_detail),
    re_path(r'^api/departmenttimings/(\d+)$', views.departmenttimings_list),
    re_path(r'^api/departmenttimings/$', views.default_department_schedule),

]
