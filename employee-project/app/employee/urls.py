from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('employees/', views.EmployeeListView.as_view(), name='employee-list'),
    path('employee/create/', views.EmployeeCreateView.as_view(), name='employee-create'),
    path('employee/<int:pk>/edit/', views.EmployeeEditView.as_view(), name='employee-edit'),
    path('employee/<int:pk>/delete/', views.EmployeeDeleteView.as_view(), name='employee-delete'),
    # path('contacts/', views.contact_list, name='contact-list'),
    path('departments/', views.DepartmentListView.as_view(), name='department-list'),
    path('department/create/', views.DepartmentCreateView.as_view(), name='department-create'),
    path('department/<int:pk>/edit/', views.DepartmentEditView.as_view(), name='department-edit'),
    path('department/<int:pk>/delete/', views.DepartmentDeleteView.as_view(), name='department-delete'),
    # path('projects/', views.project_list, name='project-list'),
]
