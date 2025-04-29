# Getting Started

This directory contains documentation to help you get started with the Django project.

## Contents

- [Installation](./installation.md): Instructions for installing the project
- [Configuration](./configuration.md): Guide for configuring the project
- [Development Setup](./development-setup.md): Instructions for setting up a development environment
- [SSH Setup](./ssh-setup.md): Guide for setting up SSH for secure connections
- [Troubleshooting Guide](./troubleshooting.md): Common issues and solutions

## Quick Start

1. Install the project dependencies:
   ```bash
   uv pip install -r requirements/dev.txt
   ```

2. Configure the project:
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

3. Run migrations:
   ```bash
   python src/manage.py migrate
   ```

4. Create a superuser:
   ```bash
   python src/manage.py createsuperuser
   ```

5. Run the development server:
   ```bash
   python src/manage.py runserver
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
pytest
```

## Next Steps

After getting started with the project, you may want to explore:

- [Patterns](../patterns/README.md): Design patterns used in the project
- [Best Practices](../best-practices/README.md): Development guidelines and best practices
- [Tools](../tools/README.md): Development tools and utilities
- [Project Documentation](../project/README.md): Project-specific documentation 