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

## Step 2: Install uv (Recommended)

```bash
pip install uv
```

> **Tip for zsh users:**
> If you get `zsh: command not found: uv` after installing, try:
> ```bash
> hash -r
> export PATH=$PATH:~/.local/bin
> source ~/.zshrc
> ```
> Or restart your terminal to refresh your PATH.

## Step 3: Set Up Virtual Environment

Using `uv` (recommended):
```bash
uv venv
source .venv/bin/activate  # On Unix/macOS or zsh
# OR
.venv\Scripts\activate  # On Windows
```

Using `venv`:
```bash
python -m venv .venv
source .venv/bin/activate  # On Unix/macOS or zsh
# OR
.venv\Scripts\activate  # On Windows
```

## Step 4: Install Dependencies

Using `uv` (recommended):
```bash
uv pip install -r requirements/dev.txt
```

Using `pip`:
```bash
pip install -r requirements/dev.txt
```

## Step 5: Set Up Environment Variables

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

## Step 6: Initialize Database

```bash
python src/manage.py migrate
```

## Step 7: Create Superuser

```bash
python src/manage.py createsuperuser
```

## Step 8: Run Development Server

```bash
python src/manage.py runserver
```

Visit http://localhost:8000/ in your browser to verify the installation.

## Troubleshooting

For shell and environment issues (e.g., command not found for uv or pre-commit), see [Troubleshooting Guide](./troubleshooting.md).

## Next Steps

1. Review the [Configuration Guide](./configuration.md)
2. Set up your [Development Environment](./development-setup.md)
3. Follow the [Learning Path](../README.md#learning-path)
