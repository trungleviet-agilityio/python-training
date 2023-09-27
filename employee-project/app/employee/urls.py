from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('employees/', views.EmployeeListView.as_view(), name='employee-list'),
    path('employee/create/', views.EmployeeCreateView.as_view(), name='employee-create'),
    path('employee/<int:employee_id>/edit/', views.EmployeeEditView.as_view(), name='employee-edit'),
    path('employee/<int:employee_id>/delete/', views.EmployeeDeleteView.as_view(), name='employee-delete'),
    path('contacts/', views.contact_list, name='contact-list'),
    path('departments/', views.department_list, name='department-list'),
    path('projects/', views.project_list, name='project-list'),
]
