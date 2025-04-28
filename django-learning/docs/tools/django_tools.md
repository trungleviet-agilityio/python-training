# Django Development Tools

This document outlines essential tools and utilities commonly used in Django development to improve productivity, code quality, and debugging capabilities.

## 1. Django Debug Toolbar

The Django Debug Toolbar is a configurable set of panels that display various debug information about the current request/response.

### Installation

```bash
pip install django-debug-toolbar
```

### Configuration

```python
# settings.py
INSTALLED_APPS = [
    ...
    'debug_toolbar',
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    ...
]

INTERNAL_IPS = [
    '127.0.0.1',
]

# urls.py
from django.urls import include, path

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
```

### Features
- SQL query inspection
- Request/response data
- Template rendering time
- Cache operations
- Signal handling

## 2. Django Extensions

A collection of custom management commands for Django.

### Installation

```bash
pip install django-extensions
```

### Configuration

```python
# settings.py
INSTALLED_APPS = [
    ...
    'django_extensions',
]
```

### Useful Commands

```bash
# Create a shell with IPython
python manage.py shell_plus

# Generate UML diagrams
python manage.py graph_models -a -o myapp_models.png

# Show URL patterns
python manage.py show_urls

# Run development server with Werkzeug
python manage.py runserver_plus
```

## 3. Coverage.py

Tool for measuring code coverage of Python programs.

### Installation

```bash
pip install coverage
```

### Usage

```bash
# Run tests with coverage
coverage run --source='.' manage.py test

# Generate report
coverage report

# Generate HTML report
coverage html
```

### Configuration

```ini
# .coveragerc
[run]
source = .
omit =
    */migrations/*
    */tests/*
    */venv/*
    manage.py

[report]
exclude_lines =
    pragma: no cover
    def __repr__
    raise NotImplementedError
```

## 4. Black

The uncompromising code formatter.

### Installation

```bash
pip install black
```

### Usage

```bash
# Format a file
black path/to/file.py

# Format entire project
black .

# Check what would be formatted
black --check .
```

### Configuration

```toml
# pyproject.toml
[tool.black]
line-length = 88
target-version = ['py37']
include = '\.pyi?$'
```

## 5. Flake8

A wrapper around PyFlakes, pycodestyle and McCabe.

### Installation

```bash
pip install flake8
```

### Usage

```bash
# Check code style
flake8 .

# Check specific file
flake8 path/to/file.py
```

### Configuration

```ini
# setup.cfg
[flake8]
max-line-length = 88
extend-ignore = E203
exclude = .git,__pycache__,build,dist
```

## 6. Django Test Plus

Useful testing utilities for Django.

### Installation

```bash
pip install django-test-plus
```

### Usage

```python
from test_plus.test import TestCase

class MyTestCase(TestCase):
    def test_something(self):
        self.get('my-url')
        self.response_200()
        self.assertTemplateUsed('my_template.html')
```

## 7. Django Crispy Forms

Better form rendering.

### Installation

```bash
pip install django-crispy-forms
```

### Configuration

```python
# settings.py
INSTALLED_APPS = [
    ...
    'crispy_forms',
    'crispy_bootstrap5',  # or your preferred template pack
]

CRISPY_TEMPLATE_PACK = 'bootstrap5'
```

### Usage

```python
# forms.py
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class MyForm(forms.Form):
    helper = FormHelper()
    helper.layout = Layout(
        'field1',
        'field2',
        Submit('submit', 'Submit')
    )
```

## 8. Django Compressor

Compresses linked and inline JavaScript or CSS into a single cached file.

### Installation

```bash
pip install django-compressor
```

### Configuration

```python
# settings.py
INSTALLED_APPS = [
    ...
    'compressor',
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
]
```

### Usage

```html
{% load compress %}

{% compress css %}
<link rel="stylesheet" href="{% static 'css/style1.css' %}">
<link rel="stylesheet" href="{% static 'css/style2.css' %}">
{% endcompress %}
```

## 9. Django Testing Tools

### pytest-django

A pytest plugin for Django.

#### Installation

```bash
pip install pytest-django
```

#### Configuration

```ini
# pytest.ini
[pytest]
DJANGO_SETTINGS_MODULE = your_project.settings
python_files = tests.py test_*.py *_tests.py
```

#### Usage

```python
# test_models.py
import pytest
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_user_creation():
    user = User.objects.create_user(username='testuser', password='12345')
    assert user.username == 'testuser'
    assert user.check_password('12345')
```

### pytest-cov

Pytest plugin for measuring code coverage.

#### Installation

```bash
pip install pytest-cov
```

#### Usage

```bash
# Run tests with coverage
pytest --cov=your_app

# Generate HTML report
pytest --cov=your_app --cov-report=html
```

### factory-boy

A library for creating test data.

#### Installation

```bash
pip install factory-boy
```

#### Usage

```python
# factories.py
import factory
from django.contrib.auth.models import User

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f'user{n}')
    email = factory.LazyAttribute(lambda obj: f'{obj.username}@example.com')
    is_staff = False

# tests.py
from .factories import UserFactory

def test_user_creation():
    user = UserFactory()
    assert user.username.startswith('user')
    assert '@example.com' in user.email
```

### django-test-plus

Additional testing utilities for Django.

#### Installation

```bash
pip install django-test-plus
```

#### Usage

```python
from test_plus.test import TestCase

class MyTestCase(TestCase):
    def test_login_required(self):
        self.get('my-protected-url')
        self.response_302()  # Redirects to login
        
        self.client.login(username='user', password='pass')
        self.get('my-protected-url')
        self.response_200()
```

### django-selenium-test-runner

Run Selenium tests with Django.

#### Installation

```bash
pip install django-selenium-test-runner
```

#### Configuration

```python
# settings.py
INSTALLED_APPS = [
    ...
    'selenium_test_runner',
]

SELENIUM_DRIVER = 'chrome'  # or 'firefox'
```

#### Usage

```python
from selenium_test_runner.test_case import SeleniumTestCase

class MySeleniumTest(SeleniumTestCase):
    def test_login(self):
        self.selenium.get(f'{self.live_server_url}/login/')
        username_input = self.selenium.find_element_by_name('username')
        username_input.send_keys('testuser')
        self.selenium.find_element_by_name('submit').click()
        self.assertIn('Welcome', self.selenium.page_source)
```

### django-debug-toolbar-force

Force Django Debug Toolbar in tests.

#### Installation

```bash
pip install django-debug-toolbar-force
```

#### Usage

```python
from debug_toolbar_force.middleware import DebugToolbarForceMiddleware

class MyTestCase(TestCase):
    def setUp(self):
        self.middleware = DebugToolbarForceMiddleware(get_response=None)
        self.middleware.process_request(self.request)
```

## Best Practices for Testing

1. **Test Organization**
   - Keep tests close to the code they test
   - Use meaningful test names
   - Group related tests in classes
   - Use fixtures and factories appropriately

2. **Test Coverage**
   - Aim for high test coverage
   - Focus on critical paths
   - Test edge cases
   - Use coverage reports to identify gaps

3. **Test Performance**
   - Use appropriate test databases
   - Minimize database operations
   - Use transaction management
   - Parallelize tests when possible

4. **Test Maintenance**
   - Keep tests up to date
   - Remove obsolete tests
   - Document test requirements
   - Use CI/CD for automated testing

## Best Practices

1. **Version Control**
   - Keep requirements.txt updated
   - Document tool configurations
   - Include tool-specific config files

2. **Development Workflow**
   - Use tools consistently across the team
   - Automate tool usage in CI/CD
   - Regular code quality checks

3. **Performance**
   - Enable caching for development tools
   - Use appropriate tool settings
   - Regular cleanup of cache files

4. **Security**
   - Keep tools updated
   - Review tool configurations
   - Use secure defaults

## Resources

- [Django Debug Toolbar Documentation](https://django-debug-toolbar.readthedocs.io/)
- [Django Extensions Documentation](https://django-extensions.readthedocs.io/)
- [Coverage.py Documentation](https://coverage.readthedocs.io/)
- [Black Documentation](https://black.readthedocs.io/)
- [Flake8 Documentation](https://flake8.pycqa.org/)
- [Django Test Plus Documentation](https://django-test-plus.readthedocs.io/)
- [Django Crispy Forms Documentation](https://django-crispy-forms.readthedocs.io/)
- [Django Compressor Documentation](https://django-compressor.readthedocs.io/)
- [pytest-django Documentation](https://pytest-django.readthedocs.io/)
- [pytest-cov Documentation](https://pytest-cov.readthedocs.io/)
- [factory-boy Documentation](https://factoryboy.readthedocs.io/)
- [django-selenium-test-runner Documentation](https://django-selenium-test-runner.readthedocs.io/)
- [django-debug-toolbar-force Documentation](https://django-debug-toolbar-force.readthedocs.io/)
