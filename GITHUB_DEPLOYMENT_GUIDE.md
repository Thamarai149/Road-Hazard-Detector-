# 📦 GitHub Deployment Guide

Complete guide to push your AI Road Hazard Detector project to GitHub.

## 🎯 What You'll Deploy

- ✅ Backend API (FastAPI)
- ✅ Mobile App (Flutter)
- ✅ Documentation
- ✅ Configuration files

## 📋 Prerequisites

- Git installed on your computer
- GitHub account
- Your project ready

## 🚀 Step-by-Step Guide

### 1. Install Git (if not installed)

**Windows:**
```bash
# Download from: https://git-scm.com/download/win
# Or use winget:
winget install Git.Git
```

**Verify installation:**
```bash
git --version
```

### 2. Configure Git

```bash
# Set your name
git config --global user.name "Your Name"

# Set your email (use your GitHub email)
git config --global user.email "your.email@example.com"

# Verify configuration
git config --list
```

### 3. Create GitHub Repository

1. Go to [github.com](https://github.com)
2. Click **"+"** → **"New repository"**
3. Fill in details:
   - **Repository name**: `ai-road-hazard-detector`
   - **Description**: `AI-powered mobile app for detecting road hazards with real-time alerts`
   - **Visibility**: Choose Public or Private
   - **DO NOT** initialize with README (we already have one)
4. Click **"Create repository"**

### 4. Initialize Git in Your Project

```bash
# Navigate to your project root
cd C:\EE

# Initialize git repository
git init

# Check status
git status
```

### 5. Add Files to Git

```bash
# Add all files
git add .

# Check what will be committed
git status

# If you see unwanted files, they should be in .gitignore
```

### 6. Create First Commit

```bash
# Commit with message
git commit -m "Initial commit: AI Road Hazard Detector with Flutter mobile app and FastAPI backend"

# Verify commit
git log
```

### 7. Connect to GitHub

```bash
# Add remote repository (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/ai-road-hazard-detector.git

# Verify remote
git remote -v
```

### 8. Push to GitHub

```bash
# Push to main branch
git push -u origin main

# If you get an error about 'master' vs 'main', rename branch:
git branch -M main
git push -u origin main
```

### 9. Verify Upload

1. Go to your GitHub repository
2. Refresh the page
3. You should see all your files! 🎉

## 📁 Repository Structure

Your GitHub repo will contain:

```
ai-road-hazard-detector/
├── backend/                    # FastAPI backend
│   ├── app.py                 # Main API server
│   ├── requirements.txt       # Python dependencies
│   ├── data/                  # Hazard data storage
│   ├── model/                 # AI models
│   └── uploads/               # Uploaded images
├── mobile/                    # Flutter mobile app
│   ├── lib/                   # Dart source code
│   ├── android/               # Android configuration
│   ├── assets/                # Images, fonts
│   └── pubspec.yaml          # Flutter dependencies
├── ai/                        # AI training scripts
│   ├── train.py
│   ├── inference.py
│   └── dataset.yaml
├── docs/                      # Documentation
│   ├── architecture.md
│   ├── deployment.md
│   └── documentation.md
├── .gitignore                 # Files to ignore
├── README.md                  # Project overview
├── RENDER_DEPLOYMENT_GUIDE.md # Backend deployment guide
└── GITHUB_DEPLOYMENT_GUIDE.md # This file
```

## 🔄 Making Updates

### After making changes:

```bash
# Check what changed
git status

# Add changed files
git add .

# Or add specific files
git add backend/app.py
git add mobile/lib/main.dart

# Commit with descriptive message
git commit -m "Add new feature: voice alerts"

# Push to GitHub
git push
```

### Common Git Commands:

```bash
# View commit history
git log

# View changes before committing
git diff

# Undo changes to a file
git checkout -- filename

# Create a new branch
git checkout -b feature-name

# Switch branches
git checkout main

# Merge branch
git merge feature-name

# Pull latest changes
git pull
```

## 🔐 Security Best Practices

### Files Already in .gitignore:

- ✅ `backend/data/hazards.json` (user data)
- ✅ `backend/uploads/*` (uploaded images)
- ✅ `mobile/build/` (compiled files)
- ✅ `.venv/` (Python virtual environment)
- ✅ `*.apk` (optional - large binary files)
- ✅ `*.pt` (AI model files - large)
- ✅ `google-services.json` (Firebase credentials)
- ✅ `*.keystore` (Android signing keys)

### Never Commit:

- ❌ API keys or secrets
- ❌ Database passwords
- ❌ Private keys
- ❌ User data
- ❌ Large binary files (>100MB)

### If You Accidentally Committed Secrets:

```bash
# Remove file from git but keep locally
git rm --cached path/to/secret-file

# Add to .gitignore
echo "path/to/secret-file" >> .gitignore

# Commit the removal
git commit -m "Remove sensitive file"
git push

# IMPORTANT: Change the exposed secret immediately!
```

## 📝 Writing Good Commit Messages

### Format:
```
<type>: <short description>

<optional longer description>
```

### Types:
- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `style:` Code formatting
- `refactor:` Code restructuring
- `test:` Adding tests
- `chore:` Maintenance tasks

### Examples:
```bash
git commit -m "feat: add manual pothole marking with GPS coordinates"
git commit -m "fix: resolve camera permission crash on Android 13"
git commit -m "docs: update deployment guide with Render instructions"
git commit -m "refactor: simplify backend service API calls"
```

## 🌿 Branching Strategy

### For Solo Development:
```bash
# Work directly on main
git checkout main
# Make changes
git add .
git commit -m "Update feature"
git push
```

### For Team Development:
```bash
# Create feature branch
git checkout -b feature/voice-alerts

# Make changes
git add .
git commit -m "Add voice alert feature"

# Push feature branch
git push -u origin feature/voice-alerts

# Create Pull Request on GitHub
# After review, merge to main
```

## 📊 GitHub Features to Use

### 1. README.md
- Already created ✅
- Shows on repository homepage
- Update with project status

### 2. Issues
- Track bugs and features
- Create issue templates
- Assign to team members

### 3. Projects
- Organize tasks with Kanban board
- Track progress
- Link issues and PRs

### 4. Releases
- Tag versions (v1.0.0, v1.1.0)
- Attach APK files
- Write release notes

### 5. GitHub Actions (CI/CD)
- Auto-build APK on push
- Run tests automatically
- Deploy to Render

## 🔧 Troubleshooting

### Error: "Permission denied (publickey)"

**Solution:**
```bash
# Use HTTPS instead of SSH
git remote set-url origin https://github.com/YOUR_USERNAME/ai-road-hazard-detector.git
```

### Error: "Repository not found"

**Solution:**
- Check repository name spelling
- Verify you have access to the repository
- Use correct GitHub username

### Error: "Large files detected"

**Solution:**
```bash
# Remove large file from git
git rm --cached path/to/large-file

# Add to .gitignore
echo "path/to/large-file" >> .gitignore

# Commit
git commit -m "Remove large file"
```

### Error: "Merge conflict"

**Solution:**
```bash
# Pull latest changes
git pull

# Open conflicted files and resolve manually
# Look for <<<<<<< HEAD markers

# After resolving
git add .
git commit -m "Resolve merge conflict"
git push
```

## 📱 Sharing Your Project

### Make Repository Public:
1. Go to repository **Settings**
2. Scroll to **Danger Zone**
3. Click **Change visibility**
4. Select **Public**

### Add Description and Topics:
1. Go to repository homepage
2. Click **⚙️** next to About
3. Add description
4. Add topics: `flutter`, `fastapi`, `ai`, `mobile-app`, `road-safety`

### Create a Good README:
- Project description ✅
- Features list ✅
- Installation instructions ✅
- Screenshots/GIFs
- Demo video link
- License information

## 🎓 Learning Resources

- [Git Documentation](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com/)
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
- [GitHub Learning Lab](https://lab.github.com/)

## ✅ Deployment Checklist

- [ ] Git installed and configured
- [ ] GitHub account created
- [ ] Repository created on GitHub
- [ ] Local repository initialized
- [ ] .gitignore file in place
- [ ] All files added and committed
- [ ] Remote repository connected
- [ ] Code pushed to GitHub
- [ ] Repository visible on GitHub
- [ ] README.md displays correctly
- [ ] No sensitive data committed
- [ ] Repository description added
- [ ] Topics/tags added

## 🎉 Success!

Your project is now on GitHub! 🚀

**Next Steps:**
1. ✅ Deploy backend to Render (see RENDER_DEPLOYMENT_GUIDE.md)
2. ✅ Update mobile app with Render URL
3. ✅ Build and test APK
4. ✅ Share your project!

**Your Repository:**
```
https://github.com/YOUR_USERNAME/ai-road-hazard-detector
```

---

**Need Help?** Check GitHub documentation or create an issue in your repository.
