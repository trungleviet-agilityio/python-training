# Troubleshooting Guide: Shell & Environment

This guide helps you resolve common shell and environment issues when setting up or working with this Django project.

## 1. 'command not found: uv' or 'command not found: pre-commit'

If you install tools like uv or pre-commit with pip and get a 'command not found' error, you may need to add ~/.local/bin to your PATH.

### For zsh users:
```bash
export PATH=$PATH:~/.local/bin
```
To make this permanent, add the above line to your ~/.zshrc file:
```bash
echo 'export PATH=$PATH:~/.local/bin' >> ~/.zshrc
source ~/.zshrc
```

### For bash users:
Add the export line to your ~/.bashrc and run:
```bash
echo 'export PATH=$PATH:~/.local/bin' >> ~/.bashrc
source ~/.bashrc
```

After this, you should be able to run uv and pre-commit from any directory.

## 2. Virtual Environment Activation Issues
- Ensure you are in the project directory.
- Try recreating the virtual environment if activation fails.

## 3. Python Version Issues
- Ensure you're using Python 3.12 or higher.
- Check your version with:
  ```bash
  python --version
  ```

## 4. Dependency Installation Issues
- If installation fails, try updating pip:
  ```bash
  pip install --upgrade pip
  ```
- Check for system-level dependencies (e.g., PostgreSQL).

## 5. Database Issues
- If migrations fail, try:
  ```bash
  python src/manage.py migrate --run-syncdb
  ```
- Check database connection settings in your .env file.

## More Help
- Check the [Django Documentation](https://docs.djangoproject.com/)
- Review the project [README](../README.md)
- Search for similar issues on [Stack Overflow](https://stackoverflow.com/) 