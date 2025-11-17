# Deployment Guide

## Quick Start

1. **Create GitHub Repository**
   - Repository name must be: `ISHITADG.github.io`
   - Make it public (required for free GitHub Pages)

2. **Push Code to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Academic portfolio website"
   git branch -M main
   git remote add origin https://github.com/ISHITADG/ISHITADG.github.io.git
   git push -u origin main
   ```

3. **Enable GitHub Pages**
   - Go to: Settings → Pages
   - Source: Deploy from a branch
   - Branch: `main` / `(root)`
   - Click Save

4. **Wait for Build**
   - Check Actions tab for build status
   - Site will be live at: `https://ISHITADG.github.io`

## Post-Deployment Checklist

- [ ] Verify site is accessible at `https://ISHITADG.github.io`
- [ ] Test all navigation links
- [ ] Update personal information in `_config.yml`
- [ ] Fill in education details in `education.md`
- [ ] Update about page with actual career trajectory
- [ ] Test publication scraper: `python scripts/fetch_publications.py`
- [ ] Verify GitHub Actions workflow is enabled
- [ ] Check that recent publications appear in News section

## Customization Steps

### 1. Update Personal Information
Edit `_config.yml`:
- Name, email, social links
- Google Scholar ID (already set to `okBrMn8AAAAJ`)
- Site description

### 2. Update Content Pages
- **about.md**: Add your actual career trajectory
- **education.md**: Add your educational background
- **research.md**: Update with your specific research areas
- **contact.md**: Verify contact information

### 3. Test Publication Scraper
```bash
cd scripts
pip install -r requirements.txt
python fetch_publications.py
```

Note: Google Scholar may block automated requests. If it fails:
- Use SerpAPI (paid service)
- Manually add publications
- Wait for GitHub Actions to run (monthly)

### 4. Customize Styling
Edit `assets/css/custom.css` to change:
- Colors (CSS variables at top)
- Fonts
- Spacing and layouts

## GitHub Actions Setup

The workflow is already configured at `.github/workflows/update-publications.yml`.

It will:
- Run monthly on the 1st
- Fetch publications from Google Scholar
- Automatically commit updates

To trigger manually:
1. Go to Actions tab
2. Select "Update Publications"
3. Click "Run workflow"

## Troubleshooting

### Site Not Building
- Check Actions tab for errors
- Verify `_config.yml` is valid YAML
- Ensure repository is public

### Publications Not Updating
- Check Actions tab for workflow errors
- Verify Google Scholar ID is correct
- Consider using SerpAPI if scraper fails

### Styling Issues
- Clear browser cache
- Check CSS file path in `_layouts/default.html`
- Verify custom.css exists in `assets/css/`

## Next Steps

1. **Initial Content**: Fill in placeholder content with your actual information
2. **Test Locally**: Run `bundle exec jekyll serve` to preview changes
3. **Deploy**: Push to GitHub and verify site works
4. **Monitor**: Check Actions tab monthly to ensure publications update

## Support Resources

- [Jekyll Documentation](https://jekyllrb.com/docs/)
- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [Google Scholar API Alternatives](https://serpapi.com/google-scholar-api)

