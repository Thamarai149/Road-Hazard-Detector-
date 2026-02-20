# 🚀 Quick Start - Deploy to Render in 10 Minutes

## Step 1: Push to GitHub (3 minutes)

```bash
# Add new files
git add .

# Commit
git commit -m "Ready for Render deployment"

# Push (if you haven't already)
git push
```

## Step 2: Deploy on Render (5 minutes)

1. Go to **[render.com](https://render.com)** → Sign in with GitHub
2. Click **"New +"** → **"Web Service"**
3. Select your repository: `ai-road-hazard-detector`
4. Configure:
   - **Root Directory**: `backend`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn app:app --host 0.0.0.0 --port $PORT`
   - **Instance**: Free
5. Click **"Create Web Service"**

## Step 3: Update Mobile App (2 minutes)

1. Copy your Render URL (e.g., `https://your-app.onrender.com`)
2. Open mobile app → Settings
3. Update "Backend Server URL" with your Render URL
4. Save and test!

## ✅ Done!

Your backend is now live in the cloud! 🎉

**Test it:**
- Visit: `https://your-url.onrender.com/health`
- Should return: `{"status": "healthy"}`

---

**Full guides available:**
- `DEPLOYMENT_CHECKLIST.md` - Complete checklist
- `RENDER_DEPLOYMENT_GUIDE.md` - Detailed instructions
- `GITHUB_DEPLOYMENT_GUIDE.md` - GitHub setup
