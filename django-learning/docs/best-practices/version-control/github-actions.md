# GitHub Actions & Branch Management Guide

This guide covers GitHub Actions workflows and branch management practices for this project.

## 1. Automatic Branch Deletion

### Overview
We use GitHub Actions to automatically delete branches after they are merged into the main branch. This helps maintain a clean repository and prevents accumulation of stale branches.

### Configuration

1. **Workflow File**
   Create `.github/workflows/delete-merged-branches.yml`:
   ```yaml
   name: Delete Merged Branches
   on:
     pull_request:
       types: [closed]
       branches:
         - main
   
   jobs:
     delete-merged-branches:
       runs-on: ubuntu-latest
       if: github.event.pull_request.merged == true
       steps:
         - name: Delete Branch
           uses: SvanBoxel/delete-merged-branch@main
           env:
             GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
           with:
             branch: ${{ github.event.pull_request.head.ref }}
   ```

2. **Branch Protection Rules**
   - Enable branch protection for `main`
   - Require pull request reviews
   - Require status checks to pass
   - Include administrators in restrictions

### How It Works

1. **Trigger**
   - Workflow runs when a PR is merged to main
   - Checks if PR was actually merged (not just closed)

2. **Process**
   - Uses GitHub API to delete the branch
   - Requires appropriate permissions
   - Logs deletion status

3. **Benefits**
   - Automated cleanup
   - Reduced repository clutter
   - Consistent branch management

### Troubleshooting

1. **Permission Issues**
   - Check GitHub token permissions
   - Verify branch protection settings
   - Ensure workflow has necessary access

2. **Failed Deletions**
   - Check workflow logs
   - Verify branch name format
   - Ensure branch exists

## 2. Branch Management Best Practices

### Naming Conventions
- `feature/*`: New features
- `bugfix/*`: Bug fixes
- `hotfix/*`: Urgent production fixes
- `release/*`: Release preparations

### Protection Rules
1. **Main Branch**
   - Require pull requests
   - Require approvals
   - Require status checks
   - No direct pushes

2. **Development Branch**
   - Similar to main but less strict
   - Allow rebase merging
   - Require basic checks

### Regular Maintenance
1. **Cleanup Schedule**
   - Weekly branch audits
   - Remove stale branches
   - Update protection rules

2. **Monitoring**
   - Track branch status
   - Monitor workflow runs
   - Review protection effectiveness

## 3. Additional Workflows

### Code Quality
- Linting
- Testing
- Security scanning

### Deployment
- Staging deployment
- Production deployment
- Environment management

### Documentation
- API documentation
- Changelog generation
- Version tagging

## 4. Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Branch Protection Rules](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/defining-the-mergeability-of-pull-requests/managing-a-branch-protection-rule)
- [Workflow Syntax](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)

## Related Documentation

- [Git Conventions](git.md): Commit message format and branch naming conventions
- [Git Workflow](git-workflow.md): Detailed workflow process and commit verification setup
- [Pre-commit Hooks](../../tools/pre_commit_hooks.md): Code quality checks and formatting
- [Development Workflow](../development/workflow.md): Development process and practices
- [Code Review Guide](../development/review.md): Code review guidelines and process 