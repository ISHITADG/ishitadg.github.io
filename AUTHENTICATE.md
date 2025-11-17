# GitHub Authentication Guide

## Current Status
Your code is ready to push, but GitHub authentication is needed.

## Option 1: Personal Access Token (Recommended)

### Step 1: Create Token
1. Go to: https://github.com/settings/tokens
2. Click **"Generate new token"** → **"Generate new token (classic)"**
3. Name it: "Website Deployment"
4. Select scopes: ✅ **repo** (all checkboxes under repo)
5. Click **"Generate token"**
6. **COPY THE TOKEN** (you won't see it again!)

### Step 2: Push with Token
```bash
git push -u origin main
```
When prompted:
- Username: `ISHITADG`
- Password: **paste your token** (not your GitHub password)

## Option 2: GitHub CLI (Easiest)

```bash
# Install GitHub CLI (if not installed)
brew install gh

# Authenticate
gh auth login

# Then push
git push -u origin main
```

## Option 3: SSH Key Setup

```bash
# Generate SSH key (if you don't have one)
ssh-keygen -t ed25519 -C "your_email@example.com"

# Add to ssh-agent
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# Copy public key
cat ~/.ssh/id_ed25519.pub

# Add to GitHub: https://github.com/settings/keys
# Click "New SSH key", paste the key, save

# Then push
git push -u origin main
```

## Quick Test
After authenticating, test with:
```bash
git push -u origin main
```

Your site will be available at:
- If repo is `ISHITADG.github.io`: https://ISHITADG.github.io
- If repo is `website`: https://ISHITADG.github.io/website (or configure custom domain)

