from django.urls import path
from . import views
from .views import (
    EmployeeView,
)

urlpatterns = [
    path('', views.home, name='home'),
    path('employees/', views.EmployeeView.as_view(), name='employee-list-create'),
    path('contacts/', views.contact_list, name='contact-list'),
    path('departments/', views.department_list, name='department-list'),
    path('projects/', views.project_list, name='project-list'),
]
