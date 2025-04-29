# Pre-commit Hooks

Pre-commit hooks are scripts that run automatically before each commit to ensure code quality and consistency. This document explains how to set up and use pre-commit hooks in our Django project.

## Overview

Pre-commit hooks help maintain code quality by:

- Formatting code consistently
- Checking for linting issues
- Ensuring proper file hygiene
- Preventing problematic code from being committed

## Installation

1. Install pre-commit:

```bash
pip install pre-commit
```

2. Install the git hooks:

```bash
pre-commit install
```

## Configuration

Our project uses a `.pre-commit-config.yaml` file to configure the hooks. The current configuration includes:

```yaml
# Exclude markdown files and the config itself from pre-commit hooks
exclude: '\.(md|yaml)$'

repos:
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
    -   id: trailing-whitespace
    -   id: end-of-file-fixer
    -   id: check-yaml
    -   id: check-added-large-files
    -   id: check-ast
    -   id: check-json
    -   id: check-merge-conflict
    -   id: detect-private-key

-   repo: https://github.com/psf/black
    rev: 24.2.0
    hooks:
    -   id: black
        args: [--line-length=88]

-   repo: https://github.com/pycqa/isort
    rev: 5.13.2
    hooks:
    -   id: isort
        args: ["--profile", "black", "--filter-files"]

-   repo: https://github.com/pycqa/flake8
    rev: 7.0.0
    hooks:
    -   id: flake8
        additional_dependencies: [
            'flake8-docstrings',
            'flake8-quotes',
            'flake8-bugbear',
            'flake8-comprehensions',
        ]
        args: [--max-line-length=88]

-   repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.8.0
    hooks:
    -   id: mypy
        additional_dependencies: [
            'types-PyYAML',
            'types-requests',
            'types-setuptools',
            'types-python-dateutil',
            'types-six',
            'django-stubs',
        ]
        args: [--ignore-missing-imports]

-   repo: https://github.com/PyCQA/bandit
    rev: 1.7.7
    hooks:
    -   id: bandit
        args: ["-c", "pyproject.toml"]
        additional_dependencies: ["bandit[toml]"]

-   repo: https://github.com/asottile/pyupgrade
    rev: v3.15.0
    hooks:
    -   id: pyupgrade
        args: [--py311-plus]

# Ruff for fast linting and auto-fixing
-   repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.8.3
    hooks:
    -   id: ruff
    -   id: ruff-format
```

## Available Hooks

### Pre-commit Hooks

These hooks perform basic file hygiene checks:

- `trailing-whitespace`: Removes trailing whitespace
- `end-of-file-fixer`: Ensures files end with a newline
- `check-yaml`: Validates YAML files
- `check-added-large-files`: Prevents large files from being committed
- `check-ast`: Ensures Python files are valid
- `check-json`: Validates JSON files
- `check-merge-conflict`: Prevents merge conflict markers from being committed
- `detect-private-key`: Prevents private keys from being committed

### Code Formatting

- **black**: Python code formatting
- **isort**: Python import sorting
- **ruff-format**: Fast Python code formatting

### Linting and Type Checking

- **flake8**: Python linting
- **mypy**: Python type checking
- **pyupgrade**: Python version compatibility
- **ruff**: Fast Python linting

### Security

- **bandit**: Python security checks
- **detect-private-key**: Prevents accidental key commits

## Configuration in pyproject.toml

Ruff's behavior is configured in the `pyproject.toml` file:

```toml
[tool.ruff]
line-length = 88
target-version = "py311"
select = [
    "E",  # pycodestyle errors
    "W",  # pycodestyle warnings
    "F",  # pyflakes
    "I",  # isort
    "B",  # flake8-bugbear
    "C4", # flake8-comprehensions
    "UP", # pyupgrade
    "N",  # pep8-naming
    "ANN", # flake8-annotations
    "S",  # flake8-bandit
    "A",  # flake8-builtins
    "COM", # flake8-commas
    "C90", # mccabe complexity
    "D",  # pydocstyle
    "T10", # flake8-debugger
    "EM",  # flake8-errmsg
    "EXE", # flake8-executable
    "ISC", # flake8-implicit-str-concat
    "G",  # flake8-logging-format
    "INP", # flake8-no-pep420
    "PIE", # flake8-pie
    "T20", # flake8-print
    "PYI", # flake8-pyi
    "PT",  # flake8-pytest-style
    "Q",  # flake8-quotes
    "RSE", # flake8-raise
    "RET", # flake8-return
    "SLF", # flake8-self
    "SIM", # flake8-simplify
    "TID", # flake8-tidy-imports
    "TCH", # flake8-type-checking
    "ARG", # flake8-unused-arguments
    "PTH", # flake8-use-pathlib
    "ERA", # flake8-eradicate
    "PD",  # pandas-vet
    "PGH", # pygrep-hooks
    "PL",  # pylint
    "TRY", # tryceratops
]
ignore = [
    "D100", # Missing docstring in public module
    "D101", # Missing docstring in public class
    "D102", # Missing docstring in public method
    "D105", # Missing docstring in magic method
    "D106", # Missing docstring in public nested class
    "D107", # Missing docstring in __init__
    "D200", # One-line docstring should fit on one line
    "D205", # 1 blank line required between summary line and description
    "D400", # First line should end with a period
]

[tool.ruff.format]
quote-style = "double"
indent-style = "space"
skip-magic-trailing-comma = false
line-ending = "auto"
```

## Usage

### Running Hooks Manually

To run the hooks on all files:

```bash
pre-commit run --all-files
```

To run the hooks on specific files:

```bash
pre-commit run --files path/to/file1.py path/to/file2.py
```

To run a specific hook:

```bash
pre-commit run black --all-files
```

### Hook Management

```bash
# Install pre-commit hooks
pre-commit install

# Run hooks on all files
pre-commit run --all-files

# Run specific hook
pre-commit run black --all-files

# Clean pre-commit cache
pre-commit clean

# Update hooks to latest versions
pre-commit autoupdate
```

### Skipping Hooks

To skip pre-commit hooks for a specific commit:

```bash
git commit -m "Your commit message" --no-verify
```

## Best Practices

1. **Line Length Consistency**
   - All Python formatting tools (black, flake8, ruff) use 88 characters
   - This matches Black's default line length

2. **Type Checking**
   - mypy is configured to ignore missing imports
   - Additional type stubs are included for common packages

3. **Security**
   - bandit is configured to use project-specific settings
   - Private key detection is enabled

4. **Performance**
   - ruff is used for fast linting
   - pyupgrade ensures Python version compatibility

5. **File Exclusions**
   - Markdown and YAML files are excluded from hooks
   - Large files are checked before commit

## VS Code Integration

To integrate pre-commit hooks with VS Code, install the following extensions:

- Python extension
- Pylance
- Ruff

Configure VS Code settings in `.vscode/settings.json`:

```json
{
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
        "source.organizeImports": true
    },
    "python.formatting.provider": "black",
    "python.linting.enabled": true,
    "python.linting.flake8Enabled": true,
    "python.linting.mypyEnabled": true,
    "python.linting.pylintEnabled": false,
    "python.linting.flake8Args": [
        "--max-line-length=88",
        "--extend-ignore=D100,D101,D102,D105,D106,D107,D200,D205,D400",
        "--docstring-convention=google",
        "--quotes=double"
    ],
    "python.linting.mypyArgs": [
        "--ignore-missing-imports"
    ],
    "[python]": {
        "editor.defaultFormatter": "ms-python.python",
        "editor.formatOnSave": true,
        "editor.codeActionsOnSave": {
            "source.organizeImports": true
        }
    },
    "files.exclude": {
        "**/__pycache__": true,
        "**/.pytest_cache": true,
        "**/*.pyc": true
    }
}
```

## Troubleshooting

### Common Issues

1. **Hooks are not running**
   - Ensure pre-commit is installed: `pip install pre-commit`
   - Ensure hooks are installed: `pre-commit install`
   - Check that the `.pre-commit-config.yaml` file exists

2. **Hooks are failing**
   - Run `pre-commit run --all-files` to see detailed error messages
   - Fix the issues reported by the hooks
   - Commit the changes and try again

3. **Hooks are too slow**
   - Consider using Ruff instead of multiple linters
   - Exclude unnecessary files from checks
   - Use caching for pre-commit hooks

4. **Hook Failures**
   ```bash
   # Skip hooks temporarily (not recommended)
   git commit -m "message" --no-verify
   
   # Run specific hook with verbose output
   pre-commit run black --all-files -v
   ```

5. **Common Issues**
   - Line length mismatches: Ensure all tools use 88 characters
   - Import sorting conflicts: Use isort with black profile
   - Type checking errors: Add missing type stubs or ignore imports

## Resources

- [Pre-commit Documentation](https://pre-commit.com/)
- [Ruff Documentation](https://beta.ruff.rs/docs/)
- [VS Code Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) 