from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('employees/', views.employee_list, name='employee-list'),
    path('contacts/', views.contact_list, name='contact-list'),
    path('departments/', views.department_list, name='department-list'),
    path('projects/', views.project_list, name='project-list'),
]
