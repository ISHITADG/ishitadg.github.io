# Check GitHub Pages Status

## What You've Done ✅
- Set up Jekyll page in GitHub Actions
- Code is pushed to GitHub

## Next Steps:

### 1. Check GitHub Actions Build Status
Go to: https://github.com/ISHITADG/website/actions

Look for:
- ✅ Green checkmark = Build successful
- ❌ Red X = Build failed (check logs)
- 🟡 Yellow circle = Still building

### 2. Verify GitHub Pages is Enabled
Go to: https://github.com/ISHITADG/website/settings/pages

Should show:
- **Source**: Deploy from a branch (or GitHub Actions)
- **Branch**: main (or gh-pages)
- **Status**: "Your site is live at..." or "Your site is ready to be published"

### 3. Check Your Site URL
Your site should be available at:
- **https://ISHITADG.github.io/website/**

(Note: If you see a 404, wait 1-2 minutes for GitHub to propagate)

### 4. If Build Failed
Check the Actions logs for errors. Common issues:
- Missing dependencies
- Jekyll build errors
- Configuration issues

### 5. If You Want Root Domain (https://ISHITADG.github.io)
Rename repository to `ISHITADG.github.io`:
1. Go to Settings → General
2. Scroll to "Repository name"
3. Change `website` to `ISHITADG.github.io`
4. Update `_config.yml` baseurl to `""`

## Quick Test
Try visiting: https://ISHITADG.github.io/website/

If it works, you're all set! 🎉

