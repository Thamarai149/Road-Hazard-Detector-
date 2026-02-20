# 🚀 Render Deployment Guide

Deploy your AI Road Hazard Detector backend API on Render for free cloud hosting.

## 🎯 Why Render?

- ✅ Free tier (750 hours/month)
- ✅ Automatic HTTPS
- ✅ Auto-deploy from GitHub
- ✅ No credit card required
- ✅ Accessible from anywhere

## 📋 Prerequisites

- GitHub account
- Render account ([render.com](https://render.com))
- Code pushed to GitHub

## 🚀 Quick Start

### 1. Push to GitHub

```bash
cd C:\EE
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/ai-road-hazard-detector.git
git push -u origin main
```

### 2. Create Render Account

1. Go to [render.com](https://render.com)
2. Sign up with GitHub
3. Authorize Render

### 3. Deploy Backend

1. Click **"New +"** → **"Web Service"**
2. Connect your repository
3. Configure:
   - **Name**: `ai-road-hazard-api`
   - **Root Directory**: `backend`
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn app:app --host 0.0.0.0 --port $PORT`
   - **Instance**: Free
4. Click **"Create Web Service"**

### 4. Get Your URL

After deployment (2-5 minutes):
```
https://ai-road-hazard-api.onrender.com
```

### 5. Update Mobile App

In app Settings → Backend URL:
```
https://ai-road-hazard-api.onrender.com
```

## ⚠️ Free Tier Notes

- Sleeps after 15 min inactivity
- First request takes ~30s to wake
- Use UptimeRobot to keep alive

## ✅ Test Deployment

Visit:
- `https://your-app.onrender.com/`
- `https://your-app.onrender.com/health`
- `https://your-app.onrender.com/docs`

## 📚 Full Guide

See complete instructions in GITHUB_DEPLOYMENT_GUIDE.md

---

**Your backend is now live! 🎉**
