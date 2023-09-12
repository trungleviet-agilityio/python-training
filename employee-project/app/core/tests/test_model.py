"""
Tests for models.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models

def create_user(email='user@example.com', password='testpass123'):
    """Create a return a new user."""
    return get_user_model().objects.create_user(email, password)

class ModelTests(TestCase):
    """Test models"""

    def setUp(self):
        # Create a superuser
        self.user = get_user_model().objects.create_superuser(
            username='testuser',
            email='test@example.com',
            password='test123',
        )

        # Create departments
        self.department_hr = models.Department.objects.create(
            name="Human Resources",
            description="This is the Human Resources department."
        )
        self.department_marketing = models.Department.objects.create(
            name="Marketing",
            description="This is the Marketing department."
        )

    def test_create_superuser(self):
        """Test creating a superuser"""
        self.assertTrue(self.user.is_superuser)
        self.assertTrue(self.user.is_staff)

    def test_create_department(self):
        """Test creating a department is successful"""
        self.assertEqual(self.department_hr.name, "Human Resources")
        self.assertEqual(self.department_hr.description, "This is the Human Resources department.")

        self.assertEqual(self.department_marketing.name, "Marketing")
        self.assertEqual(self.department_marketing.description, "This is the Marketing department.")