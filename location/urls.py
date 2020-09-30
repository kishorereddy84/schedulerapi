from django.urls import path, include, re_path

from rest_framework import routers


from . import views


urlpatterns = [
    re_path(r'^api/locations/$', views.location_list),
    re_path(r'^api/locations/(\d+)$', views.location_detail),
    re_path(r'^api/locationtimings/(\d+)$', views.locationtimings_list),
    re_path(r'^api/locationtimings/$', views.default_location_schedule),

]
