# Git Workflow & Commit Verification Guide

This guide covers the Git workflow process and commit verification setup for this project.

## 1. Professional Git Workflow

### Branching Strategy
- **main**: Always production-ready. Only merge tested, reviewed code here.
- **feature/**: For new features or updates (see naming in git_conventions.md)
- **bugfix/**: For bug fixes
- **hotfix/**: For urgent production fixes

### Development Workflow

1. **Start from main**
   ```bash
   git checkout main
   git pull origin main
   ```

2. **Create Feature Branch**
   ```bash
   git checkout -b feature/your-feature
   ```

3. **Development Process**
   - Make changes in small, logical commits
   - Follow commit message conventions (see git_conventions.md)
   - Push changes regularly
   ```bash
   git push -u origin feature/your-feature
   ```

4. **Pull Request Process**
   - Create PR on GitHub
   - Request reviews
   - Address feedback
   - Ensure all checks pass

5. **Merging**
   - Squash and merge to main
   - Delete feature branch
   - Update local repository
   ```bash
   git checkout main
   git pull origin main
   git branch -d feature/your-feature
   ```

## 2. Commit Verification Setup

### Why Required?
- Ensures code authenticity
- Prevents unauthorized commits
- Maintains repository security
- Required for all contributions

### SSH Key Setup

1. **Check/Create SSH Keys**
   ```bash
   # List existing keys
   ls -la ~/.ssh/
   
   # Create if needed
   ssh-keygen -t ed25519 -C "your.email@example.com"
   ```

2. **Configure Git**
   ```bash
   # SSH signing setup
   git config --local gpg.format ssh
   git config --local user.signingkey ~/.ssh/id_ed25519.pub
   git config --local commit.gpgsign true
   git config --local gpg.ssh.allowedsignersfile ~/.ssh/allowed_signers
   
   # Create allowed signers file
   echo "your.email@example.com $(cat ~/.ssh/id_ed25519.pub)" > ~/.ssh/allowed_signers
   chmod 644 ~/.ssh/allowed_signers
   ```

3. **GitHub Configuration**
   - Go to GitHub Settings > SSH Keys
   - Add new SSH key
   - Select "Signing Key" type
   - Paste your public key
   - Save key

4. **Verify Setup**
   ```bash
   # Test commit signing
   git commit --allow-empty -S -m "test: verify signing"
   git log --show-signature -1
   ```

### Troubleshooting

1. **Invalid Key Errors**
   ```bash
   # Fix allowed_signers format
   echo "your.email@example.com $(cat ~/.ssh/id_ed25519.pub)" > ~/.ssh/allowed_signers
   
   # Fix line endings
   sed -i 's/\r$//' ~/.ssh/allowed_signers
   ```

2. **Permission Issues**
   ```bash
   # Set correct permissions
   chmod 600 ~/.ssh/id_ed25519
   chmod 644 ~/.ssh/id_ed25519.pub
   chmod 644 ~/.ssh/allowed_signers
   ```

3. **Pre-commit Conflicts**
   ```bash
   # Temporary skip
   git commit --no-verify -S -m "message"
   ```

4. **Verification Check**
   ```bash
   # Check configuration
   git config --local --list | grep -E "gpg|sign|user"
   
   # Expected output:
   # gpg.format=ssh
   # user.signingkey=~/.ssh/id_ed25519.pub
   # commit.gpgsign=true
   ```

## 3. CI/CD Integration

### Automated Checks
- Commit signature verification
- Pre-commit hook validation
- Test suite execution
- Code quality metrics

### Required Status Checks
- All commits must be signed
- CI pipeline must pass
- Code review approved
- No merge conflicts

## 4. Emergency Procedures

### Hotfix Process
1. Branch from main
2. Fix critical issue
3. Expedited review
4. Deploy immediately
5. Backport to development

### Recovery Steps
1. **Revert Bad Merge**
   ```bash
   git revert -m 1 <merge-commit>
   ```

2. **Fix Broken Build**
   ```bash
   git checkout -b hotfix/fix-build
   # Make fixes
   git push -u origin hotfix/fix-build
   ```

## 5. Best Practices

1. **Regular Synchronization**
   ```bash
   git checkout main
   git pull origin main
   git checkout your-branch
   git merge main
   ```

2. **Clean History**
   - Squash related commits
   - Write clear commit messages
   - Keep changes focused

3. **Security**
   - Always sign commits
   - Protect SSH keys
   - Review access permissions

4. **Maintenance**
   - Delete merged branches
   - Update dependencies
   - Monitor build status 