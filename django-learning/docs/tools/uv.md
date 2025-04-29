# UV - Fast Python Package Installer

[UV](https://github.com/astral-sh/uv) is a fast Python package installer and resolver written in Rust. It's designed to be a drop-in replacement for pip, with significant performance improvements.

## Installation

```bash
# On macOS or Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows (PowerShell)
irm https://astral.sh/uv/install.ps1 | iex
```

## Usage

UV can be used as a direct replacement for pip:

```bash
# Install dependencies
uv pip install -r requirements.txt

# Install a single package
uv pip install django

# Install development dependencies
uv pip install -r requirements.txt --extra-index-url https://pypi.org/simple
```

## Benefits

- **Speed**: UV is significantly faster than pip, especially for large dependency trees
- **Reliability**: UV uses a more reliable dependency resolver
- **Compatibility**: UV is fully compatible with pip's command-line interface
- **Caching**: UV has built-in caching for faster subsequent installations

## Best Practices

1. **Keep dependencies updated**: Regularly update your dependencies with `uv pip install -r requirements.txt --upgrade`
2. **Use virtual environments**: Always work in a virtual environment
3. **Commit often**: Make small, focused commits to make it easier to identify issues

## Troubleshooting

### Common Issues

1. **UV installation issues**:
   - Ensure you have the latest version of Rust installed
   - Check your system's PATH configuration
   - Try reinstalling with the `--force` flag

### Getting Help

- Check the [UV documentation](https://github.com/astral-sh/uv) 