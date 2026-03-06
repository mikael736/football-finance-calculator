# Git Setup & GitHub Workflow

## Initial Setup (One-time)

### 1. Initialize Git in Your Project
```bash
# Make sure you're in the project folder
cd football-finance-calculator

# Initialize git
git init

# Add all files
git add .

# Create first commit
git commit -m "Initial commit: Football finance calculator"
```

### 2. Create GitHub Repository

1. Go to https://github.com
2. Click "+" → "New repository"
3. Repository name: `football-finance-calculator`
4. Description: "Women's football club financial analysis tool"
5. **Important:** Make it **Public** (required for free Streamlit hosting)
6. **Do NOT** check "Initialize with README" (we already have one)
7. Click "Create repository"

### 3. Connect Local Project to GitHub

GitHub will show you commands. Use these:

```bash
# Add GitHub as remote
git remote add origin https://github.com/YOUR_USERNAME/football-finance-calculator.git

# Push your code
git branch -M main
git push -u origin main
```

Replace `YOUR_USERNAME` with your actual GitHub username.

## Daily Workflow (Every time you make changes)

### Making and Pushing Changes

```bash
# 1. Make changes to app.py (or other files)

# 2. Check what changed
git status

# 3. Add all changes
git add .

# 4. Commit with a descriptive message
git commit -m "Add expense breakdown table"

# 5. Push to GitHub
git push
```

### Good Commit Messages Examples

✅ Good:
- "Add wage ratio slider"
- "Fix profit calculation bug"
- "Improve layout with columns"
- "Add detailed breakdown section"

❌ Bad:
- "Update"
- "Changes"
- "Fix"
- "asdf"

## Common Git Commands

```bash
# See what files changed
git status

# See what specifically changed in files
git diff

# View commit history
git log --oneline

# Undo changes to a file (before committing)
git checkout -- app.py

# See remote repository URL
git remote -v
```

## Troubleshooting

### "I made a commit but want to change the message"
```bash
git commit --amend -m "New better message"
git push --force  # Only if you haven't shared the commit yet
```

### "I want to undo my last commit (but keep changes)"
```bash
git reset --soft HEAD~1
```

### "GitHub asks for username/password constantly"
Set up SSH keys or use GitHub CLI:
```bash
# Install GitHub CLI: https://cli.github.com/
gh auth login
```

### "I pushed to the wrong branch"
Don't worry! GitHub shows all branches. Just make sure to push to `main` next time.

## Sharing Your Code

Once pushed to GitHub, share this URL:
```
https://github.com/YOUR_USERNAME/football-finance-calculator
```

Your colleague can:
1. Click the URL
2. Click green "Code" button
3. Download ZIP or clone with:
   ```bash
   git clone https://github.com/YOUR_USERNAME/football-finance-calculator.git
   ```
