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

        # Create employees
        self.employee1 = models.Employee.objects.create(
            first_name="John",
            last_name="Doe",
            department=self.department_hr,
            resume='employee_resumes/john_doe_resume.pdf'
        )

        self.employee2 = models.Employee.objects.create(
            first_name="Jane",
            last_name="Smith",
            department=self.department_marketing,
            resume='employee_resumes/jane_smith_resume.pdf'
        )

        # Create projects
        self.project1 = models.Project.objects.create(
            title="Scream Truck"
        )
        self.project1.employees.add(self.employee1, self.employee2)

        self.project2 = models.Project.objects.create(
            title="Venonat"
        )
        self.project2.employees.add(self.employee2)

        # Create contacts
        self.contact1 = models.Contact.objects.create(
            street_address="123 Main St",
            city="New York",
            state="NY",
            postal_code="10001",
            phone_number="555-123-4567",
            employee=self.employee1
        )

        self.contact2 = models.Contact.objects.create(
            street_address="456 Elm St",
            city="Los Angeles",
            state="CA",
            postal_code="90001",
            phone_number="555-987-6543",
            employee=self.employee2
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

    def test_create_employee(self):
        """Test creating an employee is successful"""
        self.assertEqual(self.employee1.first_name, "John")
        self.assertEqual(self.employee1.last_name, "Doe")
        self.assertEqual(self.employee1.department, self.department_hr)
        self.assertEqual(self.employee1.resume, 'employee_resumes/john_doe_resume.pdf')

    def test_create_contact(self):
        """Test creating a contact is successful"""
        self.assertEqual(self.contact1.street_address, "123 Main St")
        self.assertEqual(self.contact1.city, "New York")
        self.assertEqual(self.contact1.state, "NY")
        self.assertEqual(self.contact1.postal_code, "10001")
        self.assertEqual(self.contact1.phone_number, "555-123-4567")
        self.assertEqual(self.contact1.employee, self.employee1)

        self.assertEqual(self.contact2.street_address, "456 Elm St")
        self.assertEqual(self.contact2.city, "Los Angeles")
        self.assertEqual(self.contact2.state, "CA")
        self.assertEqual(self.contact2.postal_code, "90001")
        self.assertEqual(self.contact2.phone_number, "555-987-6543")
        self.assertEqual(self.contact2.employee, self.employee2)

    def test_create_project(self):
        """Test creating a project is successful"""
        self.assertEqual(self.project1.title, "Scream Truck")
        self.assertEqual(list(self.project1.employees.all()), [self.employee1, self.employee2])

        self.assertEqual(self.project2.title, "Venonat")
        self.assertEqual(list(self.project2.employees.all()), [self.employee2])
