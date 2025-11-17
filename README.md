# Academic Portfolio Website

A professional academic website built with Jekyll and hosted on GitHub Pages. This site automatically fetches publications from Google Scholar and showcases research, career trajectory, and professional information.

## Features

- 🎨 **Modern Design**: Clean, responsive design with gradient accents and smooth animations
- 📚 **Auto-Updated Publications**: Automatically fetches publications from Google Scholar via GitHub Actions
- 📰 **Latest News Section**: Highlights recent publications (last 3 months) and workshop activities
- 🎓 **Workshop Integration**: Showcases SVU 2025 Workshop at ICCV 2025
- 📱 **Mobile Responsive**: Fully responsive design that works on all devices
- ⚡ **Fast Loading**: Optimized for performance with minimal dependencies

## Site Structure

```
.
├── _config.yml          # Jekyll configuration
├── _layouts/            # Page layouts
├── _publications/       # Auto-generated publication files
├── _data/               # Data files (recent publications JSON)
├── assets/css/          # Custom styles
├── scripts/             # Python scripts for fetching publications
├── .github/workflows/   # GitHub Actions workflows
├── index.html           # Homepage
├── about.md             # About page
├── news.md              # Latest news page
├── publications.md      # All publications page
├── research.md          # Research interests page
├── education.md         # Education page
├── contact.md           # Contact page
└── README.md            # This file
```

## Setup Instructions

### Prerequisites

- Ruby (2.7 or higher)
- Bundler gem
- Python 3.9+ (for publication scraper)
- Git

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/ISHITADG/ISHITADG.github.io.git
   cd ISHITADG.github.io
   ```

2. **Install Ruby dependencies**
   ```bash
   bundle install
   ```

3. **Install Python dependencies** (for publication scraper)
   ```bash
   pip install -r scripts/requirements.txt
   ```

4. **Run Jekyll locally**
   ```bash
   bundle exec jekyll serve
   ```

5. **View the site**
   Open your browser to `http://localhost:4000`

### Fetching Publications

To manually fetch publications from Google Scholar:

```bash
python scripts/fetch_publications.py
```

This will:
- Fetch all publications from your Google Scholar profile
- Generate markdown files in `_publications/`
- Create a JSON file with recent publications (last 3 months) in `_data/recent_publications.json`

**Note**: Google Scholar may block automated requests. If the scraper doesn't work, consider:
- Using [SerpAPI](https://serpapi.com/google-scholar-api) for more reliable access
- Manually updating publications
- Using the GitHub Actions workflow (runs monthly automatically)

## GitHub Pages Deployment

### Initial Setup

1. **Create the repository**
   - Create a new repository named `ISHITADG.github.io` on GitHub
   - Make sure it's public (required for free GitHub Pages)

2. **Push your code**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/ISHITADG/ISHITADG.github.io.git
   git push -u origin main
   ```

3. **Enable GitHub Pages**
   - Go to repository Settings → Pages
   - Under "Source", select "Deploy from a branch"
   - Choose branch: `main` and folder: `/ (root)`
   - Click Save

4. **Wait for deployment**
   - GitHub will build and deploy your site automatically
   - Usually takes 1-2 minutes
   - Your site will be available at `https://ISHITADG.github.io`

### Automatic Updates

The site includes a GitHub Actions workflow that:
- Runs monthly to fetch new publications from Google Scholar
- Automatically commits and pushes updates
- Located at `.github/workflows/update-publications.yml`

You can also trigger it manually:
- Go to Actions tab in your repository
- Select "Update Publications" workflow
- Click "Run workflow"

## Customization

### Update Personal Information

Edit `_config.yml` to update:
- Name, email, social links
- Site title and description
- Navigation menu items

### Update Content Pages

- **About**: Edit `about.md` with your career trajectory
- **Research**: Edit `research.md` with your research interests
- **Education**: Edit `education.md` with your educational background
- **Contact**: Edit `contact.md` with your contact information

### Customize Styling

- Edit `assets/css/custom.css` for custom styles
- Modify colors in CSS variables at the top of the file
- Update `_layouts/default.html` for layout changes

### Google Scholar ID

Update the Google Scholar ID in:
- `_config.yml` (under `author.google_scholar`)
- `scripts/fetch_publications.py` (SCHOLAR_ID variable)

## Troubleshooting

### Jekyll Build Errors

- Make sure all dependencies are installed: `bundle install`
- Check Ruby version: `ruby -v` (should be 2.7+)
- Clear Jekyll cache: `bundle exec jekyll clean`

### Publication Scraper Not Working

- Google Scholar may block automated requests
- Try using SerpAPI or manual updates
- Check the script output for error messages
- Ensure Python dependencies are installed: `pip install -r scripts/requirements.txt`

### GitHub Pages Not Updating

- Check Actions tab for build errors
- Ensure `_config.yml` is valid YAML
- Verify repository is public (for free GitHub Pages)
- Check Pages settings in repository Settings

## License

This website template is open source and available for personal and academic use.

## Credits

- Built with [Jekyll](https://jekyllrb.com/)
- Theme inspired by [al-folio](https://github.com/alshedivat/al-folio)
- Icons from [Font Awesome](https://fontawesome.com/) and [Academicons](https://jpswalsh.github.io/academicons/)

## Support

For issues or questions:
- Open an issue on GitHub
- Check the [Jekyll documentation](https://jekyllrb.com/docs/)
- Review [GitHub Pages documentation](https://docs.github.com/en/pages)

---

**Last Updated**: January 2025

