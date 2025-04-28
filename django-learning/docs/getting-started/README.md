# Getting Started

This directory contains documentation to help you get started with the Django project.

## Contents

- [Installation](./installation.md): Instructions for installing the project
- [Configuration](./configuration.md): Guide for configuring the project
- [Development Setup](./development-setup.md): Instructions for setting up a development environment
- [Troubleshooting Guide](./troubleshooting.md): Shell and environment setup issues

## Quick Start

1. Install the project dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Configure the project:
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

3. Run migrations:
   ```bash
   python manage.py migrate
   ```

4. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

6. Visit http://localhost:8000/ in your browser

## Development Workflow

1. Create a new branch for your feature:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes and commit them:
   ```bash
   git add .
   git commit -m "Add your feature"
   ```

3. Push your branch to the remote repository:
   ```bash
   git push origin feature/your-feature-name
   ```

4. Create a pull request for your changes

## Testing

Run the tests with:
```bash
python manage.py test
```

## Documentation

- [Architecture](../architecture/README.md): Overview of the project architecture
- [Patterns](../patterns/README.md): Design patterns used in the project
- [API](../api/README.md): API documentation
- [Deployment](../deployment/README.md): Deployment instructions
- [Maintenance](../maintenance/README.md): Maintenance procedures 