from django.db import models

class Department(models.Model):
    """Department object."""
    name = models.CharField(max_length=100)
    description = models.TextField()
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE, null=True, blank=True, related_name='departments')

    def __str__(self):
        return self.name


class Contact(models.Model):
    """Contact object."""
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15, null=False)
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.street_address}, {self.city}, {self.state} {self.postal_code}"


class Employee(models.Model):
    """Employee object."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees', null=True, blank=True)
    resume = models.FileField(upload_to='employee_resumes/', null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Project(models.Model):
    """Project object."""
    title = models.CharField(max_length=100)
    employees = models.ManyToManyField(Employee, related_name='projects', through='ProjectEmployee')

    def __str__(self):
        return self.title


class ProjectEmployee(models.Model):
    """Intermediate model to represent the relationship between Project and Employee."""
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.employee} - {self.project}"
