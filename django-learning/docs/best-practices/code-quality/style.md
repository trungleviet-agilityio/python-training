# Python Code Style Guide

## Overview
This guide outlines our Python code style standards, which follow Django and Python best practices.

## Code Formatting

### Black Auto-formatter
We use Black to maintain consistent code formatting:

```python
# Bad
def example_function(   x,y,z    ):
    return x+y+z

# Good (after Black formatting)
def example_function(x, y, z):
    return x + y + z
```

Configuration in `pyproject.toml`:
```toml
[tool.black]
line-length = 88
target-version = ['py39']
include = '\.pyi?$'
extend-exclude = '''
# A regex preceded with ^/ will apply only to files and directories
# in the root of the project.
^/docs/
'''
```

### EditorConfig
Our `.editorconfig` ensures consistent indentation and whitespace:

```ini
root = true

[*]
end_of_line = lf
insert_final_newline = true
trim_trailing_whitespace = true
charset = utf-8

[*.{py,rst,ini}]
indent_style = space
indent_size = 4

[*.{html,css,scss,json,yml,yaml,js}]
indent_style = space
indent_size = 2
```

## PEP 8 Compliance

### Line Length
- Code: 88 characters (Black default)
- Comments and docstrings: 79 characters
- Exception: Long strings and comments that cannot be broken

### Imports
- Group imports in the following order:
  1. Standard library imports
  2. Related third party imports
  3. Local application/library specific imports
- Use absolute imports
- Use `isort` for automatic import sorting

```python
# Standard library
import os
import sys

# Third party
import django
from django.db import models

# Local
from .models import User
from .utils import format_date
```

### String Formatting
Use f-strings for string interpolation when possible:

```python
# Bad
name = "World"
print("Hello, %s" % name)
print("Hello, {}".format(name))

# Good
name = "World"
print(f"Hello, {name}")
```

For complex cases, use prior variable assignment:

```python
# Bad
print(f"Total: {price * quantity * (1 + tax_rate):.2f}")

# Good
total = price * quantity * (1 + tax_rate)
print(f"Total: {total:.2f}")
```

## Naming Conventions

### Variables and Functions
- Use lowercase with underscores
- Be descriptive but concise
- Avoid single-letter names except for counters

```python
# Bad
def c(x):
    return x * 2

# Good
def calculate_double(value):
    return value * 2
```

### Classes
- Use CapWords convention
- Be descriptive and specific

```python
# Bad
class userprofile:
    pass

# Good
class UserProfile:
    pass
```

### Constants
- Use uppercase with underscores
- Define at module level

```python
# Bad
default_items_per_page = 10

# Good
DEFAULT_ITEMS_PER_PAGE = 10
```

## Documentation

### Docstrings
- Use triple double-quotes
- Follow Google style
- Include type hints

```python
def calculate_total(items: list[dict], tax_rate: float = 0.1) -> float:
    """Calculate total price including tax.

    Args:
        items: List of items with 'price' and 'quantity' keys.
        tax_rate: Tax rate as a decimal (default: 0.1).

    Returns:
        float: Total price including tax.

    Raises:
        ValueError: If items list is empty or tax_rate is negative.
    """
    if not items:
        raise ValueError("Items list cannot be empty")
    if tax_rate < 0:
        raise ValueError("Tax rate cannot be negative")
    
    subtotal = sum(item['price'] * item['quantity'] for item in items)
    return subtotal * (1 + tax_rate)
```

## Related Documentation

- [Pre-commit Hooks](../../tools/pre_commit_hooks.md): Code quality checks and formatting
- [Testing](testing.md): Testing guidelines and best practices
- [Project Structure](structure.md): Code organization guidelines 