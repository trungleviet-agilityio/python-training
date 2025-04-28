# Development Tools

This document describes the development tools used in the Django Blog project and how to set them up.

## UV - Fast Python Package Installer

[UV](https://github.com/astral-sh/uv) is a fast Python package installer and resolver written in Rust. It's designed to be a drop-in replacement for pip, with significant performance improvements.

### Installation

```bash
# On macOS or Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows (PowerShell)
irm https://astral.sh/uv/install.ps1 | iex
```

### Usage

UV can be used as a direct replacement for pip:

```bash
# Install dependencies
uv pip install -r requirements.txt

# Install a single package
uv pip install django

# Install development dependencies
uv pip install -r requirements.txt --extra-index-url https://pypi.org/simple
```

### Benefits

- **Speed**: UV is significantly faster than pip, especially for large dependency trees
- **Reliability**: UV uses a more reliable dependency resolver
- **Compatibility**: UV is fully compatible with pip's command-line interface
- **Caching**: UV has built-in caching for faster subsequent installations

## Pre-commit Hooks

Pre-commit hooks are used to ensure code quality before commits are made. They run various checks on your code to catch issues early.

### Installation

1. Install pre-commit:
```bash
uv pip install pre-commit
```

2. Install the git hooks:
```bash
pre-commit install
```

### Available Hooks

The following hooks are configured in `.pre-commit-config.yaml`:

- **pre-commit-hooks**: Basic file checks
  - trailing-whitespace
  - end-of-file-fixer
  - check-yaml
  - check-added-large-files
  - check-ast
  - check-json
  - check-merge-conflict
  - detect-private-key

- **black**: Code formatting
  - Ensures consistent code style

- **isort**: Import sorting
  - Organizes imports according to PEP 8

- **flake8**: Code linting
  - Checks for code style and potential errors
  - Includes docstring checking

- **mypy**: Static type checking
  - Ensures type safety in the codebase

- **bandit**: Security linting
  - Checks for common security issues

### Running Hooks Manually

You can run the hooks on all files:

```bash
pre-commit run --all-files
```

Or on specific files:

```bash
pre-commit run --files path/to/file.py
```

### Skipping Hooks

To skip pre-commit hooks for a specific commit:

```bash
git commit -m "Your message" --no-verify
```

## Configuration Files

### pyproject.toml

The `pyproject.toml` file contains configuration for various tools:

- **black**: Code formatting settings
- **isort**: Import sorting settings
- **flake8**: Linting settings
- **mypy**: Type checking settings
- **bandit**: Security checking settings
- **pytest**: Testing settings
- **coverage**: Code coverage settings

### .pre-commit-config.yaml

The `.pre-commit-config.yaml` file defines which hooks to run and their configurations.

## Best Practices

1. **Always run pre-commit hooks**: Don't skip the hooks unless absolutely necessary
2. **Keep dependencies updated**: Regularly update your dependencies with `uv pip install -r requirements.txt --upgrade`
3. **Use virtual environments**: Always work in a virtual environment
4. **Commit often**: Make small, focused commits to make it easier to identify issues
5. **Fix issues locally**: Address any issues found by the hooks before pushing your code

## Troubleshooting

### Common Issues

1. **Pre-commit hooks failing**:
   - Run `pre-commit clean` to clear the cache
   - Run `pre-commit autoupdate` to update hook versions
   - Check the specific error message for guidance

2. **UV installation issues**:
   - Ensure you have the latest version of Rust installed
   - Check your system's PATH configuration
   - Try reinstalling with the `--force` flag

3. **Type checking errors**:
   - Review the mypy documentation for the specific error
   - Consider adding type ignores for false positives
   - Update type stubs if needed

### Getting Help

- Check the [UV documentation](https://github.com/astral-sh/uv)
- Visit the [pre-commit documentation](https://pre-commit.com/)
- Consult the documentation for specific tools (black, isort, flake8, mypy, bandit) 