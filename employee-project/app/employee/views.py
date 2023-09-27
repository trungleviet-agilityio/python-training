from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import  get_object_or_404, redirect, render

from .models import Employee

from .forms import EmployeeForm

def home(request):
    return render(request, 'employee/home.html')


class EmployeeListView(View):
    template_name = 'employee/employee_list.html'

    def get(self, request, *args, **kwargs):
        employees = Employee.objects.all()
        context = {
            'employees': employees,
            'employee_form': EmployeeForm(),  # Create an empty form for creating employees
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee-list')
        else:
            # Handle form errors
            pass


class EmployeeCreateView(CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employee/employee_form.html'
    success_url = reverse_lazy('employee-list')


class EmployeeEditView(View):
    template_name = 'employee/employee_list.html'  # Use the same template as the employee list

    def get(self, request, employee_id, *args, **kwargs):
        employee = get_object_or_404(Employee, pk=employee_id)
        context = {
            'employees': Employee.objects.all(),
            'employee_form': EmployeeForm(instance=employee),
        }
        return render(request, self.template_name, context)

    def put(self, request, employee_id, *args, **kwargs):
        employee = get_object_or_404(Employee, pk=employee_id)
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee-list')
        else:
            # Handle form errors
            pass


class EmployeeDeleteView(View):
    def delete(self, request, employee_id, *args, **kwargs):
        employee = get_object_or_404(Employee, pk=employee_id)
        employee.delete()
        return redirect('employee-list')


def contact_list(request):
    contacts = [
        {"street_address": "123 Main St", "city": "New York", "state": "NY", "postal_code": "10001", "phone_number": "123-456-7890"},
        {"street_address": "456 Elm St", "city": "Los Angeles", "state": "CA", "postal_code": "90001", "phone_number": "987-654-3210"},
        {"street_address": "789 Oak St", "city": "Chicago", "state": "IL", "postal_code": "60601", "phone_number": "555-123-4567"},
    ]    
    return render(request, 'employee/contact_list.html', {'contacts': contacts})


def department_list(request):
    departments = [
        {"name": "HR", "description": "Human Resources"},
        {"name": "Engineering", "description": "Software Development"},
        {"name": "Sales", "description": "Sales and Marketing"},
    ]    
    return render(request, 'employee/department_list.html', {'departments': departments})


def project_list(request):
    projects = [
        {"title": "Project A"},
        {"title": "Project B"},
        {"title": "Project C"},
    ]    
    return render(request, 'employee/project_list.html', {'projects': projects})
