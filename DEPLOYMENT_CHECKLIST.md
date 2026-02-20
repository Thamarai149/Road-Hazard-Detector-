# ✅ Deployment Checklist - Render Backend

Quick checklist to deploy your AI Road Hazard Detector backend to Render.

## 📋 Pre-Deployment Checklist

### 1. Code Preparation
- [x] Backend code ready in `backend/` folder
- [x] `requirements.txt` exists with all dependencies
- [x] `app.py` configured for production
- [x] `.gitignore` configured to exclude sensitive files
- [x] Health check endpoint at `/health`
- [x] CORS configured for mobile app access

### 2. GitHub Setup
- [ ] Git installed on your computer
- [ ] GitHub account created
- [ ] Repository created on GitHub
- [ ] Code pushed to GitHub

### 3. Render Setup
- [ ] Render account created at [render.com](https://render.com)
- [ ] GitHub connected to Render
- [ ] Ready to deploy

## 🚀 Deployment Steps

### Step 1: Push to GitHub (5 minutes)

```bash
# Navigate to project
cd C:\EE

# Initialize git (if not done)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit - AI Road Hazard Detector"

# Add remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/ai-road-hazard-detector.git

# Push to GitHub
git push -u origin main
```

**Verify**: Check GitHub repository to see your files

### Step 2: Deploy on Render (5 minutes)

1. **Go to Render Dashboard**
   - Visit [dashboard.render.com](https://dashboard.render.com)
   - Sign in with GitHub

2. **Create New Web Service**
   - Click **"New +"** → **"Web Service"**
   - Click **"Connect account"** (if needed)
   - Select your repository: `ai-road-hazard-detector`
   - Click **"Connect"**

3. **Configure Service**
   ```
   Name: ai-road-hazard-detector-api
   Region: Oregon (US West) or closest to you
   Branch: main
   Root Directory: backend
   Runtime: Python 3
   Build Command: pip install -r requirements.txt
   Start Command: uvicorn app:app --host 0.0.0.0 --port $PORT
   Instance Type: Free
   ```

4. **Deploy**
   - Click **"Create Web Service"**
   - Wait 2-5 minutes for deployment
   - Watch logs for success message

### Step 3: Get Your API URL (1 minute)

After deployment completes, you'll get a URL like:
```
https://ai-road-hazard-detector-api.onrender.com
```

**Test it**:
- Visit: `https://your-url.onrender.com/`
- Visit: `https://your-url.onrender.com/health`
- Visit: `https://your-url.onrender.com/docs`

### Step 4: Update Mobile App (2 minutes)

**Option A: In-App Settings** (Recommended)
1. Open mobile app
2. Go to **Settings** tab
3. Tap **"Backend Server URL"**
4. Enter your Render URL: `https://your-url.onrender.com`
5. Tap **"Save"**
6. Test by marking a pothole

**Option B: Update Code**
1. Edit `mobile/lib/services/backend_service.dart`
2. Change line 7:
   ```dart
   static String _baseUrl = 'https://your-url.onrender.com';
   ```
3. Rebuild APK:
   ```bash
   cd mobile
   flutter build apk --release
   ```

### Step 5: Test Everything (5 minutes)

- [ ] Backend health check works
- [ ] API docs accessible at `/docs`
- [ ] Mobile app connects to backend
- [ ] Can mark pothole manually
- [ ] Hazard appears in Statistics
- [ ] Map shows hazard markers

## 📊 Your Deployment URLs

Fill in after deployment:

```
GitHub Repository: https://github.com/_______________/ai-road-hazard-detector
Render Dashboard: https://dashboard.render.com/web/_______________
Backend API: https://_______________.onrender.com
API Docs: https://_______________.onrender.com/docs
Health Check: https://_______________.onrender.com/health
```

## ⚠️ Important Notes

### Free Tier Behavior
- **Sleeps after 15 minutes** of inactivity
- **First request takes ~30 seconds** to wake up
- **Subsequent requests are fast**
- **750 hours/month** limit (enough for development)

### Keep Backend Awake (Optional)
Use [UptimeRobot](https://uptimerobot.com) to ping every 14 minutes:
1. Sign up at uptimerobot.com
2. Add new monitor
3. URL: `https://your-url.onrender.com/health`
4. Interval: 14 minutes

### Upgrade to Paid ($7/month)
Benefits:
- No sleep/downtime
- Faster performance
- Custom domains
- Better for production

## 🐛 Troubleshooting

### Build Failed
**Check**:
- `requirements.txt` is in `backend/` folder
- All dependencies are listed
- No syntax errors in `app.py`

**Solution**:
```bash
# Test locally first
cd backend
pip install -r requirements.txt
python app.py
```

### App Can't Connect
**Check**:
- Backend URL is correct in app settings
- URL starts with `https://` not `http://`
- No trailing slash in URL
- Backend is not sleeping (visit URL in browser first)

**Solution**:
- Test URL in browser: `https://your-url.onrender.com/health`
- Should return: `{"status": "healthy"}`

### Service Keeps Sleeping
**Solution**:
- Use UptimeRobot (free)
- Or upgrade to paid tier ($7/month)

## 🔄 Making Updates

After making code changes:

```bash
# Commit changes
git add .
git commit -m "Update: description of changes"
git push

# Render will automatically redeploy! 🚀
```

## 📱 Mobile App Configuration

### Default Backend URL
The app comes with a default local URL. You MUST update it to your Render URL.

### Two Ways to Update:

1. **In-App** (No rebuild needed)
   - Settings → Backend Server URL
   - Enter Render URL
   - Save

2. **In Code** (Requires rebuild)
   - Edit `backend_service.dart`
   - Change `_baseUrl`
   - Rebuild APK

## 🎯 Success Criteria

Your deployment is successful when:

✅ Backend accessible at Render URL
✅ `/health` returns healthy status
✅ `/docs` shows API documentation
✅ Mobile app connects successfully
✅ Can create hazards from app
✅ Statistics show data
✅ Map displays hazards

## 📚 Additional Resources

- **Render Docs**: [render.com/docs](https://render.com/docs)
- **GitHub Guide**: See `GITHUB_DEPLOYMENT_GUIDE.md`
- **Render Guide**: See `RENDER_DEPLOYMENT_GUIDE.md`
- **API Docs**: Visit your `/docs` endpoint

## 🎉 Deployment Complete!

Once all checkboxes are marked, your app is fully deployed and accessible from anywhere!

**Your backend is now:**
- ✅ Running in the cloud
- ✅ Accessible from anywhere
- ✅ Auto-deploying from GitHub
- ✅ Free to use (750 hours/month)
- ✅ HTTPS enabled automatically

**Next Steps:**
1. Share your app with friends
2. Test on different devices
3. Monitor usage in Render dashboard
4. Consider upgrading for production use

---

**Need help?** Check the troubleshooting section or Render documentation.

**Total Time**: ~20 minutes from start to finish! 🚀
