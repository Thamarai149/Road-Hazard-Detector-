# 🚗 AI Road Hazard Detector

AI-powered mobile app for detecting and reporting road hazards in real-time with GPS tracking, voice alerts, and cloud backend.

## ✨ Features

### � Mobile App (Flutter)
- **Real-time Detection**: Camera-based AI hazard detection
- **Manual Marking**: Tap to mark potholes with GPS coordinates
- **Voice Alerts**: Text-to-speech warnings for detected hazards
- **Interactive Map**: View all hazards with OpenStreetMap
- **Route Planning**: Navigate with hazard-aware routing
- **Statistics**: Track detection metrics and trends
- **Cloud Sync**: Automatic backend synchronization

### 🔧 Backend API (FastAPI)
- **RESTful API**: Complete CRUD operations for hazards
- **Real-time Sync**: Instant data synchronization
- **Statistics**: Aggregated detection analytics
- **Cloud Ready**: Deploy on Render, AWS, or any cloud platform
- **Auto Documentation**: Interactive API docs at `/docs`

## 🚀 Quick Start

### Mobile App

```bash
cd mobile
flutter pub get
flutter run
```

### Backend API

```bash
cd backend
pip install -r requirements.txt
python app.py
```

Server runs at: `http://localhost:5000`

## 📦 Deployment

### Deploy Backend to Render (Free)

1. **Push to GitHub**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git push -u origin main
   ```

2. **Deploy on Render**:
   - Go to [render.com](https://render.com)
   - Create new Web Service
   - Connect your GitHub repo
   - Set root directory: `backend`
   - Deploy!

3. **Update Mobile App**:
   - Open app → Settings
   - Update Backend URL to your Render URL
   - Save and test

**📖 Detailed Guide**: See [RENDER_DEPLOYMENT_GUIDE.md](RENDER_DEPLOYMENT_GUIDE.md)

### Build Android APK

```bash
cd mobile
flutter build apk --release
```

APK location: `mobile/build/app/outputs/flutter-apk/app-release.apk`

## 📱 Mobile App Usage

### First Time Setup
1. Grant camera and location permissions
2. Go to Settings → Update Backend URL (if using cloud)
3. Return to Detection screen

### Detect Hazards
- **Automatic**: Tap green "Start" button for continuous detection
- **Manual**: Tap orange "+" button to mark current location

### View on Map
- Navigate to Map tab
- See all detected hazards
- Plan routes avoiding hazards

### Check Statistics
- View total hazards detected
- See recent activity (24h)
- Track by type and severity

## 🏗️ Project Structure

```
ai-road-hazard-detector/
├── backend/                    # FastAPI backend
│   ├── app.py                 # Main API server
│   ├── requirements.txt       # Python dependencies
│   ├── data/                  # Hazard storage
│   └── model/                 # AI models
├── mobile/                    # Flutter mobile app
│   ├── lib/
│   │   ├── main.dart         # App entry point
│   │   ├── services/         # Backend integration
│   │   └── screens/          # UI screens
│   ├── android/              # Android config
│   └── pubspec.yaml          # Flutter dependencies
├── ai/                        # AI training scripts
├── docs/                      # Documentation
├── .gitignore                # Git ignore rules
├── README.md                 # This file
├── GITHUB_DEPLOYMENT_GUIDE.md # GitHub setup
└── RENDER_DEPLOYMENT_GUIDE.md # Cloud deployment
```

## 🔧 Configuration

### Backend URL

**Option 1: In-App Settings** (Recommended)
- Open app → Settings
- Tap "Backend Server URL"
- Enter your URL
- Save

**Option 2: Code** 
Edit `mobile/lib/services/backend_service.dart`:
```dart
static String _baseUrl = 'https://your-api.onrender.com';
```

### Local Development

Find your IP address:
```bash
# Windows
ipconfig

# Linux/Mac
ifconfig
```

Use: `http://YOUR_IP:5000`

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/hazard` | Save new hazard |
| `GET` | `/api/hazards` | Get all hazards |
| `GET` | `/api/hazards/nearby` | Get nearby hazards |
| `GET` | `/api/stats` | Get statistics |
| `GET` | `/health` | Health check |
| `GET` | `/docs` | API documentation |

## 🛠️ Tech Stack

### Mobile
- **Flutter** - Cross-platform framework
- **Dart** - Programming language
- **Camera** - Real-time capture
- **Geolocator** - GPS tracking
- **Flutter Map** - OpenStreetMap integration
- **Flutter TTS** - Voice alerts

### Backend
- **FastAPI** - Modern Python web framework
- **Uvicorn** - ASGI server
- **Pydantic** - Data validation
- **Python 3.11+** - Programming language

### AI/ML
- **YOLOv8** - Object detection
- **OpenCV** - Image processing
- **PyTorch** - Deep learning

## 📊 Features in Detail

### Real-time Detection
- Captures frames every 2 seconds
- AI processes images for hazards
- Automatic GPS tagging
- Voice alerts on detection

### Manual Marking
- Orange floating button
- Captures current GPS location
- Shows location details
- Confirmation dialog

### Map Integration
- OpenStreetMap (no Google Maps API needed)
- Real-time location tracking
- Hazard markers with details
- Route planning with OSRM

### Statistics Dashboard
- Total hazards detected
- Recent activity (24h)
- Average speed tracking
- Breakdown by type and severity

## 🔒 Security

- ✅ Input validation with Pydantic
- ✅ CORS configuration
- ✅ HTTPS on Render (automatic)
- ✅ No hardcoded secrets
- ✅ Environment variable support

## 🐛 Troubleshooting

### Mobile App Can't Connect

1. Check backend is running
2. Verify URL in Settings
3. Ensure same WiFi network (local)
4. Test: `curl http://YOUR_URL/health`

### Build Errors

```bash
# Clean and rebuild
cd mobile
flutter clean
flutter pub get
flutter build apk
```

### Backend Issues

```bash
# Reinstall dependencies
cd backend
pip install -r requirements.txt --upgrade
python app.py
```

## 📚 Documentation

- [GitHub Deployment Guide](GITHUB_DEPLOYMENT_GUIDE.md) - Push to GitHub
- [Render Deployment Guide](RENDER_DEPLOYMENT_GUIDE.md) - Cloud hosting
- [Android Deployment](ANDROID_DEPLOYMENT.md) - APK building
- [Architecture](docs/architecture.md) - System design
- [API Documentation](docs/documentation.md) - API details

## 🎯 Roadmap

- [ ] iOS support
- [ ] Offline mode
- [ ] Image upload with hazards
- [ ] User authentication
- [ ] Community reporting
- [ ] Admin dashboard
- [ ] Push notifications
- [ ] Multi-language support

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## � License

This project is open source and available under the MIT License.

## 👥 Authors

- Your Name - Initial work

## 🙏 Acknowledgments

- Flutter team for amazing framework
- FastAPI for modern Python web framework
- OpenStreetMap for free mapping
- Ultralytics for YOLOv8

## 📞 Support

- 📧 Email: your.email@example.com
- 🐛 Issues: [GitHub Issues](https://github.com/YOUR_USERNAME/ai-road-hazard-detector/issues)
- � Docs: [Documentation](docs/)

---

**Made with ❤️ for safer roads**

🚗 Happy detecting! 🛣️
