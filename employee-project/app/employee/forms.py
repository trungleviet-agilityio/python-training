from django import forms
from django.core.validators import RegexValidator
from .models import Employee

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
