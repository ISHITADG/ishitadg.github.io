# Quick Start Guide

## ✅ What's Ready

- ✅ Jekyll site structure complete
- ✅ All content pages created (Home, About, News, Publications, Research, Education, Contact)
- ✅ Google Scholar scraper tested and working (found 14 publications!)
- ✅ GitHub Actions workflow configured
- ✅ Custom styling and layouts implemented
- ✅ SVU 2025 workshop integrated into News section

## 🚀 Deploy to GitHub Pages

### Step 1: Initialize Git Repository

```bash
git init
git add .
git commit -m "Initial commit: Academic portfolio website"
```

### Step 2: Create GitHub Repository

1. Go to https://github.com/new
2. Repository name: `ISHITADG.github.io` (must match exactly)
3. Make it **Public** (required for free GitHub Pages)
4. Click "Create repository"

### Step 3: Push to GitHub

```bash
git branch -M main
git remote add origin https://github.com/ISHITADG/ISHITADG.github.io.git
git push -u origin main
```

### Step 4: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** → **Pages**
3. Under "Source", select:
   - **Deploy from a branch**
   - Branch: `main`
   - Folder: `/ (root)`
4. Click **Save**

### Step 5: Wait for Build

- Check the **Actions** tab for build status
- Your site will be live at: `https://ISHITADG.github.io`
- Usually takes 1-2 minutes

## 📝 Next Steps After Deployment

1. **Update Personal Information**
   - Edit `_config.yml` with your details
   - Update `about.md` with your actual career trajectory
   - Fill in `education.md` with your educational background

2. **Test Publication Updates**
   - The GitHub Actions workflow will run monthly automatically
   - Or trigger manually: Actions → Update Publications → Run workflow

3. **Customize Content**
   - Add your photo to the homepage
   - Update research interests in `research.md`
   - Verify contact information in `contact.md`

## 🎨 Customization

- **Colors**: Edit CSS variables in `assets/css/custom.css`
- **Content**: Edit markdown files in the root directory
- **Layout**: Modify files in `_layouts/` directory

## 📊 Current Status

- **Publications Found**: 14
- **Recent Publications (last 3 months)**: 0 (will update as new papers are published)
- **Workshop**: SVU 2025 integrated and ready

## 🐛 Troubleshooting

If the site doesn't build:
- Check Actions tab for errors
- Verify `_config.yml` is valid YAML
- Ensure repository is public

If publications don't update:
- Check Actions workflow logs
- Google Scholar may block automated requests (this is normal)
- Consider using SerpAPI for more reliable access

---

**Your website is ready to deploy!** 🎉

