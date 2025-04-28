# Git Workflow & Commit Verification Guide

This guide covers a professional Git workflow for teams and how to optionally enable SSH commit signing for verified commits on GitHub.

---

## 1. Professional Git Workflow

### Branching Strategy
- **main**: Always production-ready. Only merge tested, reviewed code here.
- **feature/your-feature-name**: For new features or updates.
- **bugfix/your-bug-description**: For bug fixes.
- **docs/your-docs-update**: For documentation changes.

### Typical Workflow
1. **Start from main**
   ```bash
   git checkout main
   git pull origin main
   ```
2. **Create a new branch for your work**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Work and commit locally**
   - Make changes, commit often with clear messages.
4. **Push your branch**
   ```bash
   git push -u origin feature/your-feature-name
   ```
5. **Open a Pull Request (PR)**
   - Go to GitHub, open a PR from your branch to `main`.
   - Request reviews, address feedback.
6. **Merge after approval**
   - Only merge to `main` after review and all checks pass.
7. **Delete the feature branch after merging**
   ```bash
   git branch -d feature/your-feature-name
   git push origin --delete feature/your-feature-name
   ```

---

## 2. Commit Verification (Optional, Recommended for Teams)

### Why verify commits?
- Verified commits prove that the changes came from you, increasing trust and security in your repository.

### SSH Key Signing (Recommended for Simplicity)

#### Prerequisites
- Git version 2.34 or newer
- SSH key already set up for GitHub (see `docs/getting-started/ssh-setup.md`)

#### Enable SSH Commit Signing
1. **Configure Git to use SSH for signing:**
   ```bash
   git config --local gpg.format ssh
   git config --local user.signingkey ~/.ssh/id_ed25519_work.pub
   git config --local commit.gpgsign true
   ```
2. **Make a signed commit:**
   ```bash
   git commit -S -m "your commit message"
   ```
3. **Push as usual:**
   ```bash
   git push
   ```
4. **Check on GitHub:**
   - Your commits should show as "Verified".

#### References
- [GitHub Docs: Sign commits with SSH](https://docs.github.com/en/authentication/managing-commit-signature-verification/signing-commits-with-ssh-keys)
- [GitHub Docs: About commit signature verification](https://docs.github.com/en/authentication/managing-commit-signature-verification/about-commit-signature-verification)

### GPG Commit Signing (Advanced, Optional)
- See [GitHub Docs: Sign commits with GPG](https://docs.github.com/en/authentication/managing-commit-signature-verification/signing-commits)

### Troubleshooting SSH Commit Signing

- If you see errors like `invalid key^M` or `No principal matched`, your `allowed_signers` file may have Windows line endings or duplicate lines.
- To fix line endings, run:
  ```bash
  sed -i 's/\r$//' ~/.ssh/allowed_signers
  ```
- Open the file in a text editor and ensure only one line per key, for example:
  ```
  * ssh-ed25519 <your-public-key> <your-email>
  ```
- **Never commit your SSH keys or allowed_signers file to the repository. These are for your local machine only.**
- Save and try verifying your commit again:
  ```bash
  git log --show-signature -1
  ```
- The warnings should be gone and your commit should show a good signature.

---

## 3. Best Practices
- Use local Git config for user/email to avoid conflicts:
  ```bash
  git config --local user.name "Your Name"
  git config --local user.email "your.email@company.com"
  ```
- Keep commits focused and messages clear.
- Always branch from `main` and use PRs for merging.
- Delete feature branches after merging to keep the repo clean.

---

## 4. Troubleshooting
- If commit signing fails, check your SSH key setup and Git version.
- For more help, see the official GitHub documentation linked above. 