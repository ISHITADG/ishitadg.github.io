# Push to GitHub - Step by Step

## ✅ Current Status
- ✅ Git repository initialized
- ✅ All files committed
- ✅ Remote configured: `https://github.com/ISHITADG/ISHITADG.github.io.git`
- ✅ Branch set to `main`

## 🚀 Deploy Now

### Option 1: Create Repository via GitHub Web Interface

1. **Go to**: https://github.com/new
2. **Repository name**: `ISHITADG.github.io` (must match exactly!)
3. **Description**: "Academic portfolio website"
4. **Visibility**: Select **Public** (required for free GitHub Pages)
5. **DO NOT** initialize with README, .gitignore, or license
6. Click **"Create repository"**

### Option 2: Create Repository via GitHub CLI (if installed)

```bash
gh repo create ISHITADG.github.io --public --source=. --remote=origin --push
```

### Then Push Your Code

After creating the repository, run:

```bash
git push -u origin main
```

If you get an error about the repository not existing, wait a moment and try again.

## 📋 Enable GitHub Pages

After pushing:

1. Go to: https://github.com/ISHITADG/ISHITADG.github.io
2. Click **Settings** → **Pages** (left sidebar)
3. Under "Source":
   - Select **"Deploy from a branch"**
   - Branch: `main`
   - Folder: `/ (root)`
4. Click **Save**

## ⏱️ Wait for Build

- Check the **Actions** tab for build status
- Your site will be live at: **https://ISHITADG.github.io**
- Usually takes 1-2 minutes

## 🎉 Done!

Your academic portfolio website will be live!

