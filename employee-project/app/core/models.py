from django.db import models

class Department(models.Model):
    """Department object."""
    name = models.CharField(max_length=100)
    description = models.TextField()
    # head_of_department = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.name


class Contact(models.Model):
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15, null=False)

    def __str__(self):
        return f"{self.street_address}, {self.city}, {self.state} {self.postal_code}"
