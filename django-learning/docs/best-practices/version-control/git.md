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

## Branch Naming Conventions

### Format
```
<type>/<description>
```

### Types
- **feature**: New feature development
- **bugfix**: Bug fixes
- **hotfix**: Urgent fixes for production issues
- **docs**: Documentation updates
- **refactor**: Code refactoring
- **test**: Test additions or modifications
- **chore**: Maintenance tasks

### Description
- Use lowercase letters and hyphens
- Be brief but descriptive
- Include issue number if applicable

### Examples
- `feature/user-authentication`
- `bugfix/login-validation`
- `docs/api-endpoints`
- `refactor/auth-middleware`
- `test/user-registration`
- `hotfix/security-patch`

## Pre-commit Hooks

For information about pre-commit hooks, including configuration, required hooks, and best practices, please refer to the [Pre-commit Hooks](../../tools/pre_commit_hooks.md) documentation.

## Code Review Standards

For detailed information about code review standards, please refer to the [Code Review Guide](../development/review.md).

### Pull Request Guidelines

1. **Title Format**
   - Follow commit message format
   - Include ticket number if applicable

2. **Description Template**
   ```markdown
   ## Changes
   - Detailed list of changes
   
   ## Testing
   - Testing steps performed
   
   ## Screenshots
   - If applicable
   
   ## Checklist
   - [ ] Tests added/updated
   - [ ] Documentation updated
   - [ ] Pre-commit hooks pass
   ```

3. **Review Process**
   - At least one approval required
   - All comments must be resolved
   - CI checks must pass
   - Commits must be signed

### Review Checklist

1. **Code Quality**
   - Follows project style guide
   - No duplicate code
   - Proper error handling
   - Efficient algorithms

2. **Testing**
   - Unit tests added/updated
   - Integration tests if needed
   - Edge cases covered

3. **Security**
   - No sensitive data exposed
   - Input validation
   - Proper authentication/authorization

4. **Documentation**
   - Code comments where needed
   - API documentation updated
   - README updated if needed

## Branch Management

For information about automatic branch deletion and branch protection rules, please refer to the [GitHub Actions](github-actions.md) documentation.

## Related Documentation

- [Git Workflow](git-workflow.md): Detailed workflow process and commit verification setup
- [GitHub Actions](github-actions.md): Automated workflows and branch management
- [Development Workflow](../development/workflow.md): Development process and practices
- [Code Review Guide](../development/review.md): Code review guidelines and process