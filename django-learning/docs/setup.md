# Project Setup Guide

This guide details the setup of our Django 5 project with modern best practices and design patterns.

## Development Environment

### Prerequisites

- Python 3.12+
- `uv` package installer
- Git
- PostgreSQL (optional, for production)

### Initial Setup

1. **Create Project Directory**
   ```bash
   mkdir django5
   cd django5
   ```

2. **Initialize Git Repository**
   ```bash
   git init
   ```

3. **Create Virtual Environment**
   ```bash
   uv venv
   source .venv/bin/activate
   ```

4. **Install Dependencies**
   ```bash
   uv pip install -r requirements/dev.txt
   ```

## Project Structure

```
django5/
├── docs/                  # Documentation
├── requirements/          # Requirements files
│   ├── base.txt          # Base requirements
│   └── dev.txt           # Development requirements
├── src/                  # Source code
│   ├── api/             # API app
│   │   ├── models.py    # Base models
│   │   ├── serializers.py # Base serializers
│   │   └── urls.py      # API URLs
│   ├── core/            # Project configuration
│   │   ├── settings.py  # Settings
│   │   └── urls.py      # Main URLs
│   ├── users/           # Custom user app
│   │   ├── models.py    # User model
│   │   └── signals.py   # User signals
│   └── manage.py        # Django management script
├── .env                 # Environment variables
├── .gitignore          # Git ignore rules
└── README.md           # Project documentation
```

## Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
```

### Database Setup

1. **Development (SQLite)**
   ```bash
   python src/manage.py migrate
   ```

2. **Production (PostgreSQL)**
   Update `DATABASE_URL` in `.env`:
   ```
   DATABASE_URL=postgres://user:password@localhost:5432/dbname
   ```

### Create Superuser

```bash
python src/manage.py createsuperuser
```

## Development Tools

### Code Formatting

```bash
# Format code
black src
isort src

# Check formatting
flake8 src
```

### Type Checking

```bash
mypy src
```

### Testing

```bash
pytest
```

## Running the Project

1. **Development Server**
   ```bash
   python src/manage.py runserver
   ```

2. **Access Points**
   - Admin interface: http://localhost:8000/admin/
   - API root: http://localhost:8000/api/
   - Debug toolbar: http://localhost:8000/__debug__/

## Next Steps

1. Review the [Design Patterns](./patterns/README.md) documentation
2. Follow the [Learning Path](../README.md#learning-path)
3. Complete the exercises in each section
4. Apply patterns to your own features

## Troubleshooting

### Common Issues

1. **Database Migrations**
   ```bash
   python src/manage.py makemigrations
   python src/manage.py migrate
   ```

2. **Static Files**
   ```bash
   python src/manage.py collectstatic
   ```

3. **Package Installation**
   ```bash
   uv pip install -r requirements/dev.txt --upgrade
   ```

### Getting Help

- Check the [Django Documentation](https://docs.djangoproject.com/)
- Review the [Django Design Patterns Book](https://www.packtpub.com/product/django-design-patterns-and-best-practices/9781783986644)
- Search for similar issues on [Stack Overflow](https://stackoverflow.com/) 