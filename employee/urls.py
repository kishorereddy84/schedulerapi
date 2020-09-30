from django.urls import path, include, re_path

from rest_framework import routers


from . import views

router = routers.DefaultRouter()

urlpatterns = [
    path('list', include(router.urls)),
    re_path(r'^api/employees/$', views.employees_list),
    re_path(r'^api/employees/(\d+)$', views.employee_detail),
    re_path(r'^api/employeeavailability/$',
            views.default_employee_availability),
    re_path(r'^api/employeeavailability/(\d+)$',
            views.employeeavailability_list),


]
