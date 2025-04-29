# Django Testing Best Practices

## Overview
This guide covers testing strategies and best practices for Django projects, following Python and Django testing standards.

## Testing Structure

### Directory Layout
```
app_name/
├── tests/
│   ├── __init__.py
│   ├── test_models.py
│   ├── test_views.py
│   ├── test_forms.py
│   ├── test_apis.py
│   └── test_utils.py
```

### Test Categories

1. **Unit Tests**
   - Test individual components
   - Mock dependencies
   - Fast execution

2. **Integration Tests**
   - Test component interactions
   - Use test database
   - Limited mocking

3. **Functional Tests**
   - Test complete features
   - End-to-end testing
   - Browser simulation

## Writing Tests

### Test Case Structure
```python
from django.test import TestCase
from django.urls import reverse
from .models import Post

class PostTests(TestCase):
    def setUp(self):
        """Set up test data."""
        self.post = Post.objects.create(
            title="Test Post",
            content="Test Content",
            status="draft"
        )

    def test_post_creation(self):
        """Test post object creation."""
        self.assertEqual(self.post.title, "Test Post")
        self.assertEqual(self.post.status, "draft")

    def test_post_str_representation(self):
        """Test string representation."""
        self.assertEqual(str(self.post), "Test Post")

    def tearDown(self):
        """Clean up test data."""
        self.post.delete()
```

### Test Naming Conventions
- Use descriptive names
- Follow `test_<what>_<expected>` pattern
- Group related tests in classes

```python
class UserAuthenticationTests(TestCase):
    def test_login_valid_credentials_succeeds(self):
        pass

    def test_login_invalid_password_fails(self):
        pass

    def test_login_nonexistent_user_fails(self):
        pass
```

### Assertions
Use specific assertions:
```python
# Bad
self.assertTrue(user.is_active)
self.assertTrue(response.status_code == 200)

# Good
self.assertIs(user.is_active, True)
self.assertEqual(response.status_code, 200)
```

## Testing Views

### Function-Based Views
```python
class PostViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.post = Post.objects.create(
            title="Test Post",
            content="Test Content"
        )
        self.url = reverse('post-detail', args=[self.post.id])

    def test_post_detail_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_detail.html')
        self.assertContains(response, self.post.title)
```

### Class-Based Views
```python
from django.test import RequestFactory

class PostListViewTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

    def test_post_list_view(self):
        request = self.factory.get(reverse('post-list'))
        request.user = self.user
        response = PostListView.as_view()(request)
        self.assertEqual(response.status_code, 200)
```

## Testing Models

### Model Validation
```python
class PostModelTests(TestCase):
    def test_title_max_length(self):
        post = Post(title='x' * 201)  # Max length is 200
        with self.assertRaises(ValidationError):
            post.full_clean()

    def test_status_choices(self):
        post = Post(title='Test', status='invalid')
        with self.assertRaises(ValidationError):
            post.full_clean()
```

### Model Methods
```python
class PostModelMethodTests(TestCase):
    def test_get_absolute_url(self):
        post = Post.objects.create(title='Test Post')
        expected_url = reverse('post-detail', args=[post.id])
        self.assertEqual(post.get_absolute_url(), expected_url)
```

## Testing Forms

### Form Validation
```python
class PostFormTests(TestCase):
    def test_valid_form(self):
        data = {
            'title': 'Test Post',
            'content': 'Test Content',
            'status': 'draft'
        }
        form = PostForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {'title': ''}  # Title is required
        form = PostForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)
```

## Testing APIs

### DRF Tests
```python
from rest_framework.test import APITestCase

class PostAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.client.force_authenticate(user=self.user)

    def test_create_post(self):
        data = {
            'title': 'Test Post',
            'content': 'Test Content'
        }
        response = self.client.post('/api/posts/', data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Post.objects.count(), 1)
```

## Mocking

### Using Mock Objects
```python
from unittest.mock import patch

class ExternalServiceTests(TestCase):
    @patch('myapp.services.external_api_call')
    def test_external_service(self, mock_api):
        mock_api.return_value = {'status': 'success'}
        result = process_external_data()
        self.assertEqual(result['status'], 'success')
        mock_api.assert_called_once()
```

## Test Coverage

### Configuration
```ini
# setup.cfg
[coverage:run]
source = .
omit =
    */migrations/*
    */tests/*
    manage.py
    */wsgi.py
    */asgi.py

[coverage:report]
exclude_lines =
    pragma: no cover
    def __str__
    raise NotImplementedError
```

### Running Coverage
```bash
# Run tests with coverage
coverage run manage.py test

# Generate report
coverage report

# Generate HTML report
coverage html
```

## Best Practices

1. **Test Organization**
   - One test file per source file
   - Group related tests in classes
   - Use descriptive names

2. **Test Data**
   - Use factories for complex objects
   - Clean up test data
   - Use realistic test data

3. **Performance**
   - Keep tests focused
   - Use appropriate test types
   - Optimize database operations

4. **Maintainability**
   - Document complex tests
   - Follow DRY principles
   - Use helper methods

## Related Documentation

- [Code Style Guide](style.md)
- [Project Structure](structure.md)
- [Pre-commit Hooks](../../tools/pre_commit_hooks.md) 