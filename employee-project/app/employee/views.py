from audioop import reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import NoReverseMatch, reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import  get_object_or_404, redirect, render

from .models import Department, Employee

from .forms import DepartmentForm, EmployeeForm

def home(request):
    return render(request, 'employee/home.html')


# Employee List View
class EmployeeListView(ListView):
    model = Employee
    template_name = 'employee/employee_list.html'
    context_object_name = 'employees'


class EmployeeCreateView(View):
    template_name = 'employee/employee_form.html'

    def get(self, request):
        form = EmployeeForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee-list')
        return render(request, self.template_name, {'form': form})


class EmployeeEditView(UpdateView):
    model = Employee
    template_name = 'employee/employee_form.html'
    form_class = EmployeeForm
    success_url = '/employees/'


class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'employee/delete_confirmation.html'
    success_url = reverse_lazy('employee-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item'] = str(self.object)  # Pass the employee name to the template
        context['cancel_url'] = reverse_lazy('employee-list')
        return context


class DepartmentListView(ListView):
    model = Department
    template_name = 'employee/department_list.html'
    context_object_name = 'departments'


class DepartmentCreateView(View):
    model = Department
    template_name = 'employee/department_form.html'

    def get(self, request):
        form = DepartmentForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department-list')
        return render(request, self.template_name, {'form': form})


class DepartmentEditView(View):
    model = Department
    template_name = 'employee/department_form.html'

    def get(self, request, pk):
        department = self.model.objects.get(pk=pk)
        form = DepartmentForm(instance=department)
        return render(request, self.template_name, {'form': form, 'department': department})

    def post(self, request, pk):
        department = self.model.objects.get(pk=pk)
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('department-list')
        return render(request, self.template_name, {'form': form, 'department': department})


class DepartmentDeleteView(DeleteView):
    model = Department
    template_name = 'employee/delete_confirmation.html'
    success_url = reverse_lazy('department-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item'] = str(self.object)  # Pass the department name to the template
        context['cancel_url'] = reverse_lazy('department-list')
        return context