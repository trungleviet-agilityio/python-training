# Git Commit Conventions

This document outlines the Git commit conventions for this project to ensure consistent, readable, and meaningful commit messages.

## Commit Message Format

Each commit message should follow this format:

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Type

The type of change being made:

- **feat**: A new feature (correlates with MINOR version)
- **fix**: A bug fix (correlates with PATCH version)
- **docs**: Documentation only changes
- **style**: Changes that do not affect the meaning of the code (white-space, formatting, etc.)
- **refactor**: A code change that neither fixes a bug nor adds a feature
- **perf**: A code change that improves performance
- **test**: Adding missing tests or correcting existing tests
- **chore**: Changes to the build process or auxiliary tools and libraries
- **ci**: Changes to CI configuration files and scripts
- **build**: Changes that affect the build system or external dependencies

### Scope

The scope of the change, which is optional. It should be the name of the module affected:

- **auth**: Authentication related changes
- **models**: Database model changes
- **views**: View logic changes
- **templates**: Template changes
- **static**: Static file changes
- **admin**: Admin interface changes
- **api**: API endpoint changes
- **tests**: Test suite changes
- **docs**: Documentation changes
- **deps**: Dependency changes

### Subject

A short description of the change:

- Use the imperative, present tense: "change" not "changed" nor "changes"
- Don't capitalize the first letter
- No period (.) at the end
- Keep it under 50 characters if possible

### Body

A more detailed description of the change:

- Use the imperative, present tense
- Include the motivation for the change and contrast with previous behavior
- Wrap at 72 characters

### Footer

Information about breaking changes and issue references:

- List any breaking changes
- Reference issues that this commit closes

## Examples

### Feature Addition

```
feat(auth): add social authentication with Google

Implement Google OAuth2 authentication flow to allow users to sign in with their Google accounts.
This includes:
- Adding necessary dependencies
- Creating OAuth2 client configuration
- Implementing callback handling
- Adding login button to templates

Closes #123
```

### Bug Fix

```
fix(models): correct user profile creation on registration

The user profile was not being created properly when a new user registered.
This fix ensures the profile is created with default values.

Fixes #456
```

### Documentation Update

```
docs(api): update API documentation for user endpoints

Add detailed documentation for all user-related API endpoints including:
- Authentication
- User profile management
- Password reset flow
```

### Code Refactoring

```
refactor(views): extract common form handling logic

Move repeated form validation and processing logic into a utility function
to reduce code duplication and improve maintainability.

This change affects the following views:
- UserRegistrationView
- ProfileUpdateView
- PasswordChangeView
```

## Step-by-Step Git Workflow

### 1. Setting Up Your Local Environment

#### Configure Git for This Repository

```bash
# Set your name and email for this repository only
git config user.name "Your Name"
git config user.email "your.email@example.com"

# Verify your configuration
git config --local --list
```

#### Install Pre-commit Hooks

```bash
# Install pre-commit
pip install pre-commit

# Install the pre-commit hooks
pre-commit install

# Run pre-commit on all files
pre-commit run --all-files
```

### 2. Starting a New Feature

#### Create a Feature Branch

```bash
# Make sure you're on the main development branch
git checkout develop

# Pull the latest changes
git pull origin develop

# Create and switch to a new feature branch
git checkout -b feature/user-authentication

# Verify you're on the new branch
git branch
```

### 3. Making Changes

#### Stage Your Changes

```bash
# Check the status of your changes
git status

# Add specific files
git add path/to/file1.py path/to/file2.py

# Add all changes in a directory
git add path/to/directory/

# Add all changes
git add .
```

#### Commit Your Changes

```bash
# Commit with a message following the convention
git commit -m "feat(auth): add user registration form"

# For more detailed commits, use the editor
git commit
```

When using `git commit` without `-m`, your default editor will open. Enter your commit message following the convention:

```
feat(auth): add user registration form

Implement a user registration form with the following features:
- Email validation
- Password strength requirements
- Terms of service acceptance
- CSRF protection

This form will be displayed at /register/ and will create a new user account
upon successful submission.
```

### 4. Pushing Your Changes

```bash
# Push your branch to the remote repository
git push -u origin feature/user-authentication
```

### 5. Creating a Pull Request

1. Go to the GitHub repository
2. Click on "Pull requests"
3. Click "New pull request"
4. Select your feature branch as the compare branch
5. Fill in the PR template with details about your changes
6. Submit the pull request

### 6. Addressing Review Comments

```bash
# Make the requested changes
# Stage your changes
git add .

# Commit your changes
git commit -m "fix(auth): address review comments on registration form"

# Push your changes
git push origin feature/user-authentication
```

### 7. Merging Your Changes

Once your pull request is approved:

1. Squash and merge your pull request on GitHub
2. Delete the feature branch
3. Update your local repository:

```bash
# Switch to the develop branch
git checkout develop

# Pull the latest changes
git pull origin develop

# Delete your local feature branch
git branch -d feature/user-authentication
```

## Pre-commit Hooks

### What Are Pre-commit Hooks?

Pre-commit hooks are scripts that run automatically before a commit is created. They can check your code for style issues, run tests, and ensure that your code meets certain standards.

### Available Hooks in This Project

1. **commit-msg**: Validates commit message format
2. **trailing-whitespace**: Removes trailing whitespace
3. **end-of-file-fixer**: Ensures files end with a newline
4. **check-yaml**: Validates YAML files
5. **check-added-large-files**: Prevents large files from being committed
6. **check-ast**: Ensures Python files are syntactically valid
7. **check-json**: Validates JSON files
8. **check-merge-conflict**: Prevents merge conflict markers from being committed
9. **detect-private-key**: Prevents private keys from being committed
10. **black**: Formats Python code
11. **isort**: Sorts Python imports
12. **flake8**: Lints Python code
13. **mypy**: Type checks Python code
14. **bandit**: Checks for security issues
15. **pyupgrade**: Upgrades Python syntax

### Running Pre-commit Hooks Manually

```bash
# Run pre-commit on all files
pre-commit run --all-files

# Run pre-commit on specific files
pre-commit run --files path/to/file1.py path/to/file2.py

# Run a specific hook
pre-commit run black --all-files
```

### Skipping Pre-commit Hooks

In rare cases, you might need to skip pre-commit hooks:

```bash
# Skip pre-commit hooks for a single commit
git commit -m "feat(auth): add user registration form" --no-verify
```

## Best Practices

1. **Keep Commits Focused**
   - Each commit should represent a single logical change
   - Avoid mixing unrelated changes in a single commit

2. **Write Clear Messages**
   - Be specific about what changed and why
   - Use present tense and imperative mood
   - Reference issue numbers when applicable

3. **Review Before Committing**
   - Check that your commit message follows the convention
   - Ensure all changes are intentional
   - Verify that tests pass

4. **Branch Naming**
   - Use descriptive branch names that reflect the purpose
   - Format: `type/description`
   - Examples:
     - `feature/user-authentication`
     - `bugfix/login-error`
     - `docs/api-documentation`

5. **Pull Request Workflow**
   - Create feature branches from the main development branch
   - Keep branches up to date with the main branch
   - Squash commits when merging to maintain a clean history

## Git Workflow

1. **Feature Development**
   - Create a feature branch from the main development branch
   - Make small, focused commits
   - Push changes and create a pull request

2. **Code Review**
   - Request reviews from team members
   - Address feedback and make necessary changes
   - Ensure all checks pass

3. **Merging**
   - Squash and merge feature branches
   - Delete feature branches after merging
   - Update issue status

## Troubleshooting

### Common Issues

#### Pre-commit Hooks Not Running

```bash
# Reinstall pre-commit hooks
pre-commit uninstall
pre-commit install
```

#### Commit Message Validation Failing

Make sure your commit message follows the format:
```
<type>(<scope>): <subject>
```

For example:
```
feat(auth): add user registration form
```

#### Git Configuration Issues

```bash
# Check your Git configuration
git config --list

# Reset your Git configuration for this repository
git config --local --unset user.name
git config --local --unset user.email
git config --local user.name "Your Name"
git config --local user.email "your.email@example.com"
```

## Resources

- [Conventional Commits](https://www.conventionalcommits.org/)
- [Angular Commit Message Guidelines](https://github.com/angular/angular/blob/master/CONTRIBUTING.md#-commit-message-format)
- [GitHub Flow](https://guides.github.com/introduction/flow/)
- [Pre-commit Documentation](https://pre-commit.com/) 