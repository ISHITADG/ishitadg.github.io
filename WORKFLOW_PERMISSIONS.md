# Enable Workflow Permissions

## Issue Fixed ✅
- Added `permissions: contents: write` to the workflow
- Updated checkout action to v4
- Fixed git push configuration

## One More Step Required

You need to enable workflow write permissions in your repository settings:

1. **Go to**: https://github.com/ISHITADG/website/settings/actions
2. Scroll down to **"Workflow permissions"**
3. Select: **"Read and write permissions"**
4. Check: ✅ **"Allow GitHub Actions to create and approve pull requests"** (optional but recommended)
5. Click **"Save"**

## Why This Is Needed

GitHub Actions workflows need explicit permission to push changes back to the repository. By default, workflows only have read access for security reasons.

## After Enabling

The "Update Publications" workflow will be able to:
- ✅ Fetch publications from Google Scholar
- ✅ Commit changes automatically
- ✅ Push updates to your repository

This workflow runs monthly to keep your publications up to date!

