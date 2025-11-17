#!/bin/bash
# Deployment script for ISHITADG.github.io

echo "=========================================="
echo "Deploying to GitHub Pages"
echo "=========================================="
echo ""

# Check if remote exists
if git remote get-url origin &>/dev/null; then
    echo "✓ Remote 'origin' already configured"
    git remote set-url origin https://github.com/ISHITADG/ISHITADG.github.io.git
else
    echo "✓ Adding remote 'origin'"
    git remote add origin https://github.com/ISHITADG/ISHITADG.github.io.git
fi

echo ""
echo "=========================================="
echo "Next Steps:"
echo "=========================================="
echo ""
echo "1. Create the repository on GitHub:"
echo "   Go to: https://github.com/new"
echo "   Repository name: ISHITADG.github.io"
echo "   Make it PUBLIC (required for GitHub Pages)"
echo "   Click 'Create repository'"
echo ""
echo "2. Push your code:"
echo "   git push -u origin main"
echo ""
echo "3. Enable GitHub Pages:"
echo "   Go to: Settings → Pages"
echo "   Source: Deploy from a branch"
echo "   Branch: main, Folder: / (root)"
echo ""
echo "4. Your site will be live at:"
echo "   https://ISHITADG.github.io"
echo ""
echo "=========================================="

