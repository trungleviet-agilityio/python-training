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

    def test_create_superuser(self):
        """Test creating a superuser"""
        user = get_user_model().objects.create_superuser(
            'test@example.com',
            'test123',
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def setUp(self):
        # Create test department
        self.department_hr = Department.objects.create(name="Human Resources")
        self.department_marketing = Department.objects.create(name="Marketing")

    def test_create_department(self):
        """Test creating a department is successful"""
        self.assertEqual(self.department_hr.name, "Human Resources")
        self.assertEqual(self.department_marketing.name, "Marketing")