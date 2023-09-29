from django import forms
from django.core.validators import RegexValidator
from .models import Contact, Department, Employee, Project

class EmployeeForm(forms.ModelForm):
    confirm_delete = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput()
    )

    # Regular expression to ensure the name fields do not contain numbers
    name_validator = RegexValidator(
        regex=r'^[A-Za-z]+$',
        message='Name should only contain letters.',
        code='invalid_name'
    )

    first_name = forms.CharField(validators=[name_validator])
    last_name = forms.CharField(validators=[name_validator])

    class Meta:
        model = Employee
        fields = ("first_name", "last_name", "department")

        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "department": "Department",
        }


class DepartmentForm(forms.ModelForm):
    confirm_delete = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput()
    )

    class Meta:
        model = Department
        fields = ("name", "description")

        labels = {
            "name": "Name",
            "description": "Description",
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            "street_address",
            "city",
            "state",
            "postal_code",
            "phone_number",
        )

        labels = {
            "street_address": "Street Address",
            "city": "City",
            "state": "State",
            "postal_code": "Postal Code",
            "phone_number": "Phone Number",
        }


class ProjectForm(forms.ModelForm):
    employees = forms.ModelMultipleChoiceField(
        queryset=Employee.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False  # Optional, remove this line if you want at least one employee to be selected
    )

    class Meta:
        model = Project
        fields = ("title", "employees")