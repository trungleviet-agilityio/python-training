from audioop import reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import NoReverseMatch, reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import  get_object_or_404, redirect, render

from .models import Contact, Department, Employee, Project

from .forms import ContactForm, DepartmentForm, EmployeeForm, ProjectForm

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
    
class ContactListView(ListView):
    model = Contact
    template_name = 'employee/contact_list.html'
    context_object_name = 'contacts'


class ContactCreateView(View):
    template_name = 'employee/contact_form.html'

    def get(self, request):
        form = ContactForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact-list')
        return render(request, self.template_name, {'form': form})


class ContactEditView(UpdateView):
    model = Contact
    template_name = 'employee/contact_form.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact-list')


class ContactDeleteView(DeleteView):
    model = Contact
    template_name = 'employee/delete_confirmation.html'
    success_url = reverse_lazy('contact-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item'] = str(self.object)  # Pass the contact details to the template
        context['cancel_url'] = reverse_lazy('contact-list')
        return context


class ProjectListView(ListView):
    model = Project
    template_name = 'employee/project_list.html'
    context_object_name = 'projects'


class ProjectCreateView(View):
    template_name = 'employee/project_form.html'

    def get(self, request):
        form = ProjectForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save()
            form.save_m2m()  # Save the many-to-many field
            return redirect('project-list')
        return render(request, self.template_name, {'form': form})


class ProjectEditView(View):
    template_name = 'employee/project_form.html'

    def get(self, request, pk):
        project = Project.objects.get(pk=pk)
        form = ProjectForm(instance=project)
        return render(request, self.template_name, {'form': form, 'project': project})

    def post(self, request, pk):
        project = Project.objects.get(pk=pk)
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()  # Save the project instance first
            project.employees.set(form.cleaned_data['employees'])  # Set the employees for the project
            return redirect('project-list')
        return render(request, self.template_name, {'form': form, 'project': project})


class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'employee/delete_confirmation.html'
    success_url = reverse_lazy('project-list')

    def get_template_names(self):
        return [self.template_name]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item'] = str(self.object)  # Pass the project title to the template
        context['cancel_url'] = reverse_lazy('project-list')
        return context


class ProjectDetailView(View):
    template_name = 'employee/project_detail.html'

    def get(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        employees = project.employees.all()
        return render(request, self.template_name, {'project': project, 'employees': employees})
