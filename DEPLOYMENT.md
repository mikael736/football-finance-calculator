# Deploying to Streamlit Community Cloud

## Prerequisites

✅ Code is on GitHub (public repository)
✅ App works locally (`streamlit run app.py`)
✅ `requirements.txt` is in your repository

## Deployment Steps (5 minutes)

### 1. Go to Streamlit Cloud
Visit: https://share.streamlit.io

### 2. Sign In
Click "Sign in" → Choose "Continue with GitHub"

Authorize Streamlit to access your GitHub account.

### 3. Deploy New App

1. Click "New app" button
2. You'll see a form with three fields:

**Repository:**
- Select: `YOUR_USERNAME/football-finance-calculator`

**Branch:**
- Use: `main`

**Main file path:**
- Enter: `app.py`

3. Click "Deploy!"

### 4. Wait for Deployment

- Initial deployment takes 2-3 minutes
- You'll see build logs scrolling
- Status will change from "Building..." to "Running"

### 5. Get Your URL

Once deployed, you'll get a URL like:
```
https://football-finance-calculator-xxxxx.streamlit.app
```

or you can customize it to:
```
https://YOUR-CUSTOM-NAME.streamlit.app
```

## Using Your App

### Share the URL
Send the URL to anyone - they can use it directly in their browser.
No installation needed!

### Making Updates

Every time you push to GitHub:
```bash
git add .
git commit -m "Update calculations"
git push
```

Streamlit Cloud automatically:
1. Detects the push
2. Rebuilds the app
3. Deploys the update (takes ~1 minute)

Just refresh the browser to see changes!

## App Settings (Optional)

Click the "☰" menu on your app page to access:

- **Settings**: Change app name, URL
- **Reboot**: Force restart if app is stuck
- **Delete**: Remove the deployment
- **Logs**: View error messages

## Troubleshooting

### App won't deploy - "ModuleNotFoundError"

**Problem:** Missing package in `requirements.txt`

**Solution:**
1. Add the missing package to `requirements.txt`
2. Commit and push:
   ```bash
   git add requirements.txt
   git commit -m "Add missing dependency"
   git push
   ```
3. Streamlit will auto-redeploy

### App shows error after deployment

**Check the logs:**
1. Go to your app's page on share.streamlit.io
2. Click "Manage app" → "Logs"
3. Look for error messages in red

**Common fixes:**
- Ensure all file paths are relative (not absolute like `C:/Users/...`)
- Check that `requirements.txt` has all needed packages
- Verify your code runs locally first

### App is slow

**Solutions:**
- Use `@st.cache_data` decorator for expensive calculations
- Optimize data loading
- Consider upgrading to Streamlit Cloud paid tier (if needed)

### "Repository not found"

**Solution:**
- Make sure repository is **Public** on GitHub
- Private repos need Streamlit Cloud paid plan

## Managing Multiple Deployments

You can deploy multiple apps from the same GitHub account:
- Different repositories → Different apps
- Same repository, different branches → Different apps
- Same repository, different main files → Different apps

## Updating Your Deployment

### Change App Name/URL
1. Go to share.streamlit.io
2. Find your app
3. Click "⚙️" Settings
4. Edit "App URL" or "App name"

### Take App Offline (Temporarily)
1. Click "⚙️" Settings
2. Click "Reboot app" → "Delete app"
3. Redeploy when ready

## Cost

Streamlit Community Cloud is **100% FREE** for:
- Public GitHub repositories
- Unlimited apps
- Unlimited visitors

Paid plans exist for:
- Private repositories
- More resources
- Custom domains
- Team collaboration

For your use case, **free tier is perfect**!

## Best Practices

1. **Test locally before pushing**
   - Run `streamlit run app.py`
   - Fix any errors
   - Then push to GitHub

2. **Use descriptive commit messages**
   - Helps track what changed
   - Useful when debugging

3. **Monitor your app**
   - Check logs occasionally
   - Test after major updates

4. **Keep dependencies updated**
   - Periodically update `requirements.txt`
   - Test locally after updates

## Final Checklist

Before sharing with stakeholders:

- [ ] App runs without errors
- [ ] All inputs have reasonable defaults or validation
- [ ] Results display correctly
- [ ] Layout looks good on desktop (check mobile too!)
- [ ] README.md has deployment URL
- [ ] Commit and push any final changes

Then share the URL! 🚀
