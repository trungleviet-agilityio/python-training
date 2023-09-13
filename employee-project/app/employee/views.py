from django.shortcuts import render


def home(request):
    return render(request, 'employee/home.html')


def employee_list(request):
    employees = [
        {"first_name": "John", "last_name": "Doe", "department": "HR"},
        {"first_name": "Jane", "last_name": "Smith", "department": "Engineering"},
        {"first_name": "Alice", "last_name": "Johnson", "department": "Sales"},
    ]
    return render(request, 'employee/employee_list.html', {'employees': employees})


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
