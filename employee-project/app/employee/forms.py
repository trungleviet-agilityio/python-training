from django import forms

from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ("first_name", "last_name")
        
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
        }
