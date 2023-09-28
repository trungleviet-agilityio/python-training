from audioop import reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import NoReverseMatch, reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import  get_object_or_404, redirect, render

from .models import Employee

from .forms import EmployeeForm

def home(request):
    return render(request, 'employee/home.html')


# EmployeeListView will be updated to handle POST requests for form submission.
class EmployeeListView(ListView):
    model = Employee
    template_name = 'employee/employee_list.html'
    context_object_name = 'employees'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employee_form'] = EmployeeForm()  # Create an empty form for creating employees
        return context

    def post(self, request, *args, **kwargs):
        employee_form = EmployeeForm(request.POST)
        if employee_form.is_valid():
            employee_form.save()
        return redirect('employee-list')


class EmployeeCreateView(CreateView):
    # Handle create an employee
    model = Employee
    template_name = 'employee/employee_form.html'
    form_class = EmployeeForm
    success_url = reverse_lazy('employee-list')

    def form_valid(self, form):
        # Customize behavior for a valid form submission
        employee = form.save()  # Save the employee
        return super().form_valid(form)  # Call the parent class's form_valid method


class EmployeeEditView(UpdateView):
    model = Employee
    template_name = 'employee/employee_form.html'
    form_class = EmployeeForm
    success_url = reverse_lazy('employee-list')

    def get(self, request, *args, **kwargs):
        employee = self.get_object()
        data = {
            'first_name': employee.first_name,
            'last_name': employee.last_name,
        }
        return JsonResponse(data)

    def form_valid(self, form):
        form.save()

        return super().form_valid(form)

    def get_object(self, queryset=None):
        return get_object_or_404(self.model, pk=self.kwargs['employee_id'])


class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'employee/delete_confirmation_modal.html'
    success_url = reverse_lazy('employee-list')

    # Override the get_success_url method to return the success URL with any necessary query parameters
    def get_success_url(self):
        return self.success_url

    def get_object(self, queryset=None):
        # Get the employee object based on the employee_id from the URL
        return Employee.objects.get(pk=self.kwargs['employee_id'])

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = EmployeeForm(request.POST)

        print(self.object)

        if form.is_valid() and form.cleaned_data['confirm_delete']:
            self.object.delete()
            return redirect(self.get_success_url())

        return render(
            request,
            self.template_name,
            context={'employee': self.object, 'form': form}
        )


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
