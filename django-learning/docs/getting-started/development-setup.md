# Development Environment Setup

This guide will help you set up your development environment for working with the Django project.

## IDE Setup

### VS Code (Recommended)

1. Install VS Code extensions:
   - Python
   - Django
   - Python Test Explorer
   - GitLens
   - EditorConfig
   - Prettier
   - ESLint

2. Configure VS Code settings:
   ```json
   {
     "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python",
     "python.linting.enabled": true,
     "python.linting.pylintEnabled": true,
     "python.formatting.provider": "black",
     "editor.formatOnSave": true,
     "editor.codeActionsOnSave": {
       "source.organizeImports": true
     },
     "[python]": {
       "editor.defaultFormatter": "ms-python.python",
       "editor.formatOnSave": true
     }
   }
   ```

3. Configure debugging:
   ```json
   {
     "version": "0.2.0",
     "configurations": [
       {
         "name": "Django",
         "type": "python",
         "request": "launch",
         "program": "${workspaceFolder}/src/manage.py",
         "args": ["runserver"],
         "django": true,
         "justMyCode": true
       },
       {
         "name": "Python: Current File",
         "type": "python",
         "request": "launch",
         "program": "${file}",
         "console": "integratedTerminal",
         "justMyCode": true
       }
     ]
   }
   ```

## Development Tools

### Code Formatting

1. Install formatting tools:
   ```bash
   uv pip install black isort flake8
   ```

2. Configure Black:
   ```ini
   # pyproject.toml
   [tool.black]
   line-length = 88
   target-version = ['py312']
   include = '\.pyi?$'
   ```

3. Configure isort:
   ```ini
   # pyproject.toml
   [tool.isort]
   profile = "black"
   multi_line_output = 3
   include_trailing_comma = true
   force_grid_wrap = 0
   use_parentheses = true
   line_length = 88
   ```

### Testing Tools

1. Install testing tools:
   ```bash
   uv pip install pytest pytest-django pytest-cov
   ```

2. Configure pytest:
   ```ini
   # pytest.ini
   [pytest]
   DJANGO_SETTINGS_MODULE = core.settings
   python_files = tests.py test_*.py *_tests.py
   addopts = --reuse-db --cov=. --cov-report=html
   ```

### Debugging Tools

1. Install debugging tools:
   ```bash
   uv pip install django-debug-toolbar ipdb
   ```

2. Configure Django Debug Toolbar:
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
   ```

## Git Setup

1. Configure Git:
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "your.email@example.com"
   ```

2. Create .gitignore:
   ```
   # Python
   __pycache__/
   *.py[cod]
   *$py.class
   *.so
   .Python
   .env
   .venv/
   venv/
   ENV/

   # Django
   *.log
   local_settings.py
   db.sqlite3
   db.sqlite3-journal
   media/
   staticfiles/

   # IDE
   .idea/
   .vscode/
   *.swp
   *.swo

   # Testing
   .coverage
   htmlcov/
   .pytest_cache/
   ```

## Development Workflow

1. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make changes and format code:
   ```bash
   black src
   isort src
   flake8 src
   ```

3. Run tests:
   ```bash
   pytest
   ```

4. Commit changes:
   ```bash
   git add .
   git commit -m "Add your feature"
   ```

5. Push changes:
   ```bash
   git push origin feature/your-feature-name
   ```

## Useful Commands

### Django Management

```bash
# Create migrations
python src/manage.py makemigrations

# Apply migrations
python src/manage.py migrate

# Create superuser
python src/manage.py createsuperuser

# Collect static files
python src/manage.py collectstatic

# Run development server
python src/manage.py runserver
```

### Testing

```bash
# Run all tests
pytest

# Run specific test file
pytest src/users/tests.py

# Run with coverage
pytest --cov=src

# Run with debugger
pytest --pdb
```

### Code Quality

```bash
# Format code
black src
isort src

# Check code style
flake8 src

# Type checking
mypy src
```

## Next Steps

1. Review the [Project Structure](../README.md#project-structure)
2. Learn about [Django Design Patterns](../knowledge/patterns/README.md)
3. Start developing your first feature 