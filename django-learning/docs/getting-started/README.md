# Getting Started

This section contains guides for setting up and running the project, including installation, configuration, and troubleshooting.

## Contents

### Installation
- [Installation Guide](installation.md): How to set up the project

### Configuration
- [Development Setup](development-setup.md): Environment configuration and development tools
- [Configuration Guide](configuration.md): Project settings and environment variables
- [SSH Setup](ssh-setup.md): Setting up SSH for secure access

### Troubleshooting
- [Troubleshooting Guide](troubleshooting.md): Common issues and solutions

## How to Use This Documentation

1. **New to the Project**: Start with the [Installation Guide](installation.md)
2. **Development Setup**: Follow the [Development Setup](development-setup.md) guide
3. **Configuration**: Refer to the [Configuration Guide](configuration.md)
4. **SSH Setup**: Check the [SSH Setup](ssh-setup.md) guide
5. **Troubleshooting**: Use the [Troubleshooting Guide](troubleshooting.md) for common issues

## Contributing to Getting Started Documentation

When contributing to getting started documentation:

1. Follow the established structure and organization
2. Use consistent formatting and style
3. Include practical examples and code snippets
4. Keep information up-to-date with code changes
5. Add cross-references to related documentation

## Relationship to Other Documentation

This documentation is related to:

- [Best Practices](../best-practices/README.md): Development standards and practices
- [Project](../project/README.md): Project-specific implementation details
- [Tools](../tools/README.md): Development tools and utilities

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