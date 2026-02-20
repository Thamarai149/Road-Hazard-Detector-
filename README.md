# 🚗 AI Road Hazard Detector - Backend API

Production-ready FastAPI backend for the mobile hazard detection app with automatic startup and manual pothole marking.

## ✨ New Features

### 🔄 Auto-Start Backend Connection
- App automatically checks backend connection on startup
- Shows connection status in splash screen
- Seamless integration with mobile app

### 📍 Manual Pothole Capture
- **Orange floating button** to manually mark potholes
- Captures GPS coordinates (latitude/longitude) automatically
- Shows location details before confirming
- Instant sync with backend server

### 🤖 Automatic Detection
- Real-time camera-based detection
- Auto-saves hazards with GPS data
- Voice alerts for detected hazards

## 🚀 Quick Start

### Windows (with Anaconda)

**Quick Start (Recommended):**
```bash
# Double-click to run
quick_start.bat
```

**Full Setup:**
```bash
# Double-click to run
start_server.bat
```

Or manually:

```bash
# Activate conda environment
conda activate base

# Install dependencies
pip install -r requirements.txt

# Start server
python app.py
```

### Linux/Mac

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start server
python app.py
```

## 📡 API Endpoints

### Mobile App Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/hazard` | Save hazard from mobile app |
| `GET` | `/api/hazards` | Get all hazards for map |
| `GET` | `/api/hazards/nearby` | Get hazards near location |
| `POST` | `/api/detect` | Run AI detection on image |
| `GET` | `/api/stats` | Get detection statistics |
| `DELETE` | `/api/hazard/{id}` | Delete specific hazard |

### System Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | API information |
| `GET` | `/health` | Health check |
| `GET` | `/docs` | Interactive API documentation |

## 📱 Mobile App Configuration

### Backend Connection

The mobile app automatically connects to the backend on startup. Update the IP address to match your computer:

**Find your IP address:**

Windows:
```bash
ipconfig
# Look for "IPv4 Address" under your active network adapter
```

Linux/Mac:
```bash
ifconfig
# or
ip addr show
```

**Update mobile app backend URL:**

In `mobile/lib/services/backend_service.dart`:

```dart
// Replace with your computer's IP address
static const String baseUrl = 'http://YOUR_IP_ADDRESS:5000';
```

### Mobile App Features

#### Manual Pothole Marking
1. Open the app and grant camera/location permissions
2. Wait for GPS to acquire location (shown in status panel)
3. Tap the **orange floating button** (📍) to mark a pothole
4. Review location details in confirmation dialog
5. Tap "Mark Pothole" to save with GPS coordinates

#### Automatic Detection
1. Tap the **green "Start" button** to begin automatic detection
2. App captures images every 2 seconds
3. AI detects potholes automatically
4. Hazards saved with GPS coordinates and speed
5. Voice alerts notify you of detected hazards

#### View on Map
- Navigate to "Map" tab to see all marked hazards
- View your current location
- See nearby hazards with distance

## 🔄 Auto-Start Guide

For detailed instructions on automatically starting the backend, see [AUTO_START_GUIDE.md](backend/AUTO_START_GUIDE.md).

**Quick Options:**
1. **Manual Start** - Run `quick_start.bat` before launching app
2. **Task Scheduler** - Auto-start on Windows login
3. **Windows Service** - Run as background service
4. **Docker** - Containerized deployment

## 🗄️ Data Storage

By default, hazards are stored in `backend/data/hazards.json`.

For production, consider using:
- MongoDB (already supported via `db.py`)
- PostgreSQL with PostGIS
- Firebase Realtime Database

## 🔧 Configuration

### Port Configuration

Default port is `5000`. To change:

```python
# In app.py, modify:
uvicorn.run(app, host="0.0.0.0", port=YOUR_PORT)
```

### CORS Configuration

For production, update allowed origins:

```python
# In app.py:
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://your-domain.com"],  # Specify your domain
    ...
)
```

## 📊 API Usage Examples

### Save Hazard (from mobile app)

```bash
curl -X POST "http://localhost:5000/api/hazard" \
  -F "latitude=40.7128" \
  -F "longitude=-74.0060" \
  -F "hazard_type=pothole" \
  -F "speed=45.5" \
  -F "timestamp=2024-01-15T10:30:00"
```

### Get All Hazards

```bash
curl "http://localhost:5000/api/hazards?limit=10"
```

### Get Nearby Hazards

```bash
curl "http://localhost:5000/api/hazards/nearby?lat=40.7128&lng=-74.0060&radius_m=1000"
```

### Get Statistics

```bash
curl "http://localhost:5000/api/stats"
```

## 🧪 Testing

### Test with curl

```bash
# Health check
curl http://localhost:5000/health

# Get API info
curl http://localhost:5000/

# Get hazards
curl http://localhost:5000/api/hazards
```

### Test with Python

```python
import requests

# Save hazard
response = requests.post(
    'http://localhost:5000/api/hazard',
    data={
        'latitude': 40.7128,
        'longitude': -74.0060,
        'hazard_type': 'pothole',
        'speed': 45.5,
        'timestamp': '2024-01-15T10:30:00'
    }
)
print(response.json())

# Get hazards
response = requests.get('http://localhost:5000/api/hazards')
print(response.json())
```

## 🔍 Monitoring

### View Logs

The server logs all requests and operations:

```
INFO:     ✓ Hazard saved: H000001 at (40.7128, -74.0060)
INFO:     ✓ Returned 10 hazards (total: 127)
INFO:     ✓ Found 3 hazards within 1000m of (40.7128, -74.0060)
```

### Check Server Status

```bash
curl http://localhost:5000/health
```

Response:
```json
{
  "status": "healthy",
  "timestamp": "2024-01-15T10:30:00",
  "hazards_count": 127,
  "storage": "file-based",
  "version": "2.0.0"
}
```

## 🚗 Car Implementation

For in-car detection with camera:

```bash
# Run car detection system
python main_car.py

# Or headless mode (no display)
python main_car_headless.py
```

See `CAR_IMPLEMENTATION_GUIDE.md` for detailed setup.

## 📦 Dependencies

- **FastAPI**: Modern web framework
- **Uvicorn**: ASGI server
- **OpenCV**: Computer vision
- **Ultralytics**: YOLOv8 detection
- **NumPy**: Numerical operations
- **PyTorch**: Deep learning backend

## 🔒 Security Notes

For production deployment:

1. **Use HTTPS**: Configure SSL/TLS certificates
2. **Authentication**: Add API key or JWT authentication
3. **Rate Limiting**: Prevent API abuse
4. **Input Validation**: Already implemented via Pydantic
5. **CORS**: Restrict to specific domains
6. **Database**: Use proper database with authentication

## 🐛 Troubleshooting

### Port Already in Use

```bash
# Windows - Find and kill process on port 5000
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# Linux/Mac
lsof -ti:5000 | xargs kill -9
```

### Module Not Found

```bash
pip install -r requirements.txt --upgrade
```

### YOLO Model Not Loading

The API will fall back to simulation mode if YOLO is unavailable. To use real detection:

```bash
# Ensure model file exists
ls backend/model/yolov8n.pt

# Or download it
python -c "from ultralytics import YOLO; YOLO('yolov8n.pt')"
```

### Mobile App Can't Connect

1. Check firewall settings
2. Ensure both devices are on same network
3. Verify IP address is correct
4. Test with: `curl http://YOUR_IP:5000/health`

## 📈 Performance

- **Concurrent Requests**: Supports async operations
- **Response Time**: < 100ms for most endpoints
- **Detection Time**: ~200-500ms per image (depends on hardware)
- **Storage**: File-based (fast for < 10,000 hazards)

## 🔄 Updates

To update the backend:

```bash
git pull
pip install -r requirements.txt --upgrade
python app.py
```

## 📞 Support

For issues or questions:
- Check `/docs` endpoint for API documentation
- Review logs for error messages
- Ensure all dependencies are installed

## 📄 License

Part of AI Road Hazard Detector project.

---

**Ready to detect hazards! 🚗💨**
