from django import forms

from core.models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ("first_name", "last_name")
        
        labels = {
            "first_name": "Your First Name",
            "last_name": "Your Last Name",
        }
