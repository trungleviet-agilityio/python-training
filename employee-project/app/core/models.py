from django.db import models

class Department(models.Model):
    """Department object."""
    name = models.CharField(max_length=100)
    description = models.TextField()
    # head_of_department = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.name
