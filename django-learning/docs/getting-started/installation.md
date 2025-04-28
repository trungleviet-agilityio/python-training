# Installation Guide

This guide will help you install and set up the Django project on your local machine.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.12 or higher
- Git
- PostgreSQL (optional, for production)
- `uv` package installer (recommended) or `pip`

## Step 1: Clone the Repository

```bash
git clone <repository-url>
cd django5
```

## Step 2: Set Up Virtual Environment

Using `uv` (recommended):
```bash
uv venv
source .venv/bin/activate  # On Unix/macOS
# OR
.venv\Scripts\activate  # On Windows
```

Using `venv`:
```bash
python -m venv .venv
source .venv/bin/activate  # On Unix/macOS
# OR
.venv\Scripts\activate  # On Windows
```

## Step 3: Install Dependencies

Using `uv` (recommended):
```bash
uv pip install -r requirements/dev.txt
```

Using `pip`:
```bash
pip install -r requirements/dev.txt
```

## Step 4: Set Up Environment Variables

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Edit the `.env` file with your settings:
   ```env
   DEBUG=True
   SECRET_KEY=your-secret-key-here
   ALLOWED_HOSTS=localhost,127.0.0.1
   DATABASE_URL=sqlite:///db.sqlite3
   ```

## Step 5: Initialize Database

```bash
python src/manage.py migrate
```

## Step 6: Create Superuser

```bash
python src/manage.py createsuperuser
```

## Step 7: Run Development Server

```bash
python src/manage.py runserver
```

Visit http://localhost:8000/ in your browser to verify the installation.

## Troubleshooting

### Common Issues

1. **Python Version**
   - Ensure you're using Python 3.12 or higher
   - Check version with: `python --version`

2. **Virtual Environment**
   - If activation fails, ensure you're in the project directory
   - Try recreating the virtual environment

3. **Dependencies**
   - If installation fails, try updating pip: `pip install --upgrade pip`
   - Check for system-level dependencies (e.g., PostgreSQL)

4. **Database**
   - If migrations fail, try: `python src/manage.py migrate --run-syncdb`
   - Check database connection settings in `.env`

### Getting Help

- Check the [Django Documentation](https://docs.djangoproject.com/)
- Review project [README](../README.md)
- Search for similar issues on [Stack Overflow](https://stackoverflow.com/)

## Next Steps

1. Review the [Configuration Guide](./configuration.md)
2. Set up your [Development Environment](./development-setup.md)
3. Follow the [Learning Path](../README.md#learning-path) 