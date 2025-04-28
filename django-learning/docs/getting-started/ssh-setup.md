# SSH Key Setup Guide

This guide explains how to set up SSH keys for GitHub authentication.

## Generate a New SSH Key

```bash
# Generate a new ED25519 SSH key with your work email
ssh-keygen -t ed25519 -C "your.email@company.com" -f ~/.ssh/id_ed25519_work
```

## Configure SSH

1. Create or modify your SSH config file:

```bash
# Add GitHub configuration to SSH config
echo -e "Host github.com\n  IdentityFile ~/.ssh/id_ed25519_work\n  UseKeychain yes\n  AddKeysToAgent yes" >> ~/.ssh/config
```

2. Add your SSH key to the SSH agent:

```bash
# Start the SSH agent if not running
eval "$(ssh-agent -s)"

# Add the SSH key
ssh-add ~/.ssh/id_ed25519_work
```

## Add SSH Key to GitHub

1. Copy your SSH public key:
```bash
cat ~/.ssh/id_ed25519_work.pub
```

2. Go to GitHub:
   - Click your profile photo
   - Go to Settings
   - Navigate to "SSH and GPG keys"
   - Click "New SSH key"
   - Paste your public key
   - Give it a descriptive title (e.g., "Work Laptop")
   - Click "Add SSH key"

## Verify Configuration

Test your SSH connection:
```bash
ssh -T git@github.com
```

You should see a message like:
```
Hi username! You've successfully authenticated, but GitHub does not provide shell access.
```

## Update Git Configuration

Set your Git email to match your work email:
```bash
# Set email globally (for all repositories)
git config --global user.email "your.email@company.com"

# Or set email locally (for current repository only)
git config --local user.email "your.email@company.com"
```

## Troubleshooting

If you encounter authentication issues:

1. Check your SSH key is added to the agent:
```bash
ssh-add -l
```

2. Verify SSH configuration:
```bash
ssh -vT git@github.com
```

3. Ensure your Git remote uses SSH URL:
```bash
git remote -v
# Should show: git@github.com:username/repository.git
``` 