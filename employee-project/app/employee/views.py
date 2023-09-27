from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import  get_object_or_404, redirect, render

from .models import Employee

from .forms import EmployeeForm

def home(request):
    return render(request, 'employee/home.html')


class EmployeeListView(ListView):
    model = Employee
    template_name = 'employee/employee_list.html'
    context_object_name = 'employees'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employee_form'] = EmployeeForm()  # Create an empty form for creating employees
        return context


class EmployeeCreateView(CreateView):
    model = Employee
    template_name = 'employee/employee_form.html'
    form_class = EmployeeForm
    success_url = reverse_lazy('employee-list')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        # Customize behavior for a valid form submission
        employee = form.save()  # Save the employee
        return HttpResponseRedirect(self.get_success_url())  # Redirect to the success URL

    def form_invalid(self, form):
        # Customize behavior for an invalid form submission
        return self.render_to_response(self.get_context_data(form=form))


class EmployeeEditView(UpdateView):
    model = Employee
    template_name = 'employee/employee_form.html'
    form_class = EmployeeForm
    success_url = reverse_lazy('employee-list')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        # Customize behavior for a valid form submission
        employee = form.save()  # Save the employee
        return HttpResponseRedirect(self.get_success_url())  # Redirect to the success URL

    def form_invalid(self, form):
        # Customize behavior for an invalid form submission
        return self.render_to_response(self.get_context_data(form=form))


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
