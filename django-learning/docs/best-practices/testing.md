# Django Testing Best Practices

## Overview
This guide covers testing strategies and best practices for Django projects, including unit tests, integration tests, and end-to-end testing.

## Testing Levels

### 1. Unit Testing
```python
# Example unit test for a model
from django.test import TestCase
from .models import Post

class PostModelTest(TestCase):
    def setUp(self):
        self.post = Post.objects.create(
            title="Test Post",
            content="Test Content",
            status="draft"
        )

    def test_post_creation(self):
        self.assertEqual(self.post.title, "Test Post")
        self.assertEqual(self.post.status, "draft")

    def test_post_str_representation(self):
        self.assertEqual(str(self.post), "Test Post")
```

### 2. View Testing
```python
# Example view test
from django.test import TestCase, Client
from django.urls import reverse

class PostViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.post = Post.objects.create(
            title="Test Post",
            content="Test Content"
        )

    def test_post_list_view(self):
        response = self.client.get(reverse('post-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_list.html')
```

### 3. Form Testing
```python
# Example form test
from django.test import TestCase
from .forms import PostForm

class PostFormTest(TestCase):
    def test_valid_form(self):
        form_data = {
            'title': 'Test Post',
            'content': 'Test Content',
            'status': 'draft'
        }
        form = PostForm(data=form_data)
        self.assertTrue(form.is_valid())
```

## Test Organization

### 1. Directory Structure
```
tests/
├── __init__.py
├── test_models.py
├── test_views.py
├── test_forms.py
└── test_utils.py
```

### 2. Test Categories
- Model tests
- View tests
- Form tests
- Template tests
- API tests
- Utility function tests

## Testing Tools

### 1. Django Test Client
```python
from django.test import Client

client = Client()
response = client.get('/posts/')
```

### 2. Factory Boy
```python
import factory
from .models import Post

class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Sequence(lambda n: f'Post {n}')
    content = factory.Faker('text')
```

### 3. Coverage.py
```bash
# Run tests with coverage
coverage run --source='.' manage.py test
coverage report
coverage html
```

## Best Practices

1. **Test Isolation**
   - Each test should be independent
   - Use setUp() for common setup
   - Clean up after tests

2. **Meaningful Test Names**
   - Use descriptive names
   - Follow pattern: test_<what>_<expected_behavior>

3. **Test Coverage**
   - Aim for high coverage
   - Focus on critical paths
   - Include edge cases

4. **Performance**
   - Use appropriate test classes
   - Minimize database operations
   - Use bulk operations when possible

## Common Patterns

### 1. Testing Permissions
```python
def test_post_permissions(self):
    # Test authenticated user
    self.client.login(username='testuser', password='testpass')
    response = self.client.get(reverse('post-create'))
    self.assertEqual(response.status_code, 200)

    # Test unauthenticated user
    self.client.logout()
    response = self.client.get(reverse('post-create'))
    self.assertEqual(response.status_code, 302)
```

### 2. Testing API Endpoints
```python
from rest_framework.test import APITestCase

class PostAPITest(APITestCase):
    def test_create_post(self):
        url = reverse('api:post-list')
        data = {
            'title': 'Test Post',
            'content': 'Test Content'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
```

## Continuous Integration

### 1. GitHub Actions Example
```yaml
name: Django Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.9'
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      - name: Run tests
        run: |
          python manage.py test
```

## Resources
- [Django Testing Documentation](https://docs.djangoproject.com/en/stable/topics/testing/)
- [Factory Boy Documentation](https://factoryboy.readthedocs.io/)
- [Coverage.py Documentation](https://coverage.readthedocs.io/) 