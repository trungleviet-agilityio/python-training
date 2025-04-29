# Pre-commit Hooks

Pre-commit hooks help maintain code quality by automatically checking code before each commit.

## Installation

1. Install pre-commit:
```bash
python -m pip install pre-commit
```

2. Install git hooks:
```bash
pre-commit install
```

## Configuration

Our `.pre-commit-config.yaml`:

```yaml
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
        language_version: python3.11
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
        additional_dependencies:
          - flake8-docstrings
          - flake8-bugbear
          - flake8-comprehensions
          - flake8-simplify
        args: [--max-line-length=88, --extend-ignore=E203]

-   repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.8.0
    hooks:
    -   id: mypy
        additional_dependencies: [types-all]
        args: [--strict]

-   repo: https://github.com/PyCQA/bandit
    rev: 1.7.7
    hooks:
    -   id: bandit
        args: ["-c", "pyproject.toml"]
        additional_dependencies: ["bandit[toml]"]

-   repo: https://github.com/charliermarsh/ruff-pre-commit
    rev: v0.3.3
    hooks:
    -   id: ruff
        args: [--fix, --exit-non-zero-on-fix]
```

## Hook Details

### Code Formatting

#### Black
- Python code formatter
- Line length: 88 characters
- Consistent style across the project
- Integrates with most editors

#### isort
- Import sorting
- Compatible with Black
- Groups imports by type
- Maintains consistent import order

### Code Quality

#### Flake8
- PEP 8 style guide enforcement
- Docstring checking
- Common bug detection
- Code complexity checking

#### MyPy
- Static type checking
- Type annotation validation
- Type inference
- Integration with stub files

#### Bandit
- Security linter
- Common vulnerability detection
- Best practice enforcement
- Configuration via pyproject.toml

#### Ruff
- Fast Python linter
- Combines multiple tools
- Auto-fixes common issues
- Configurable rule sets

### File Checks

#### Pre-commit-hooks
- trailing-whitespace: Removes trailing whitespace
- end-of-file-fixer: Ensures files end with newline
- check-yaml: Validates YAML files
- check-added-large-files: Prevents large file commits
- check-ast: Validates Python syntax
- check-json: Validates JSON files
- check-merge-conflict: Checks for merge conflicts
- detect-private-key: Prevents committing private keys

## Usage

### Running Hooks

```bash
# Run all hooks on staged files
pre-commit run

# Run all hooks on all files
pre-commit run --all-files

# Run specific hook
pre-commit run black --all-files
```

### Skipping Hooks

```bash
# Skip all hooks
git commit -m "message" --no-verify

# Skip specific hook
SKIP=black git commit -m "message"
```

## IDE Integration

### VS Code
1. Install "Pre-commit" extension
2. Configure settings:
```json
{
  "pre-commit.enabled": true,
  "pre-commit.autoLint": true,
  "pre-commit.requireConfig": true,
  "pre-commit.executablePath": "pre-commit"
}
```

### PyCharm
1. Install "File Watchers" plugin
2. Configure watchers for Black and isort
3. Enable "Run on save"

## Troubleshooting

### Common Issues

1. **Hook Installation Fails**
   ```bash
   # Reinstall hooks
   pre-commit uninstall
   pre-commit clean
   pre-commit install
   ```

2. **Black/isort Conflicts**
   - Ensure Black profile in isort config
   - Run Black before isort

3. **Performance Issues**
   - Use `ruff` for faster linting
   - Skip large files
   - Run only on staged files

### Getting Help

- Check [pre-commit documentation](https://pre-commit.com/)
- Review tool-specific docs
- Check project issue tracker

## Best Practices

1. **Regular Updates**
   ```bash
   # Update all hooks
   pre-commit autoupdate
   ```

2. **Configuration Management**
   - Keep hook versions pinned
   - Document hook purposes
   - Review configurations regularly

3. **Team Workflow**
   - Require hooks in CI
   - Document hook usage
   - Maintain consistent settings

## Related Documentation

- [Code Style Guide](../best-practices/code-quality/style.md)
- [Testing Guidelines](../best-practices/code-quality/testing.md)
- [Project Structure](../best-practices/code-quality/structure.md) 