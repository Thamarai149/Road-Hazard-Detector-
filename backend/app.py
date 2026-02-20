"""
🚗 AI Road Hazard Detector - Production Backend API
FastAPI server for mobile app integration with real-time hazard detection

Endpoints:
- POST /api/hazard -> Save hazard from mobile app
- GET /api/hazards -> List all hazards for map display
- POST /api/detect -> Run YOLO inference on uploaded image
- GET /api/hazards/nearby -> Get hazards near location
- GET /api/stats -> Get detection statistics
- DELETE /api/hazard/{id} -> Delete specific hazard
"""

import os
import json
import cv2
import numpy as np
from contextlib import asynccontextmanager
from fastapi import FastAPI, File, UploadFile, HTTPException, Form, Query, Body
from fastapi.responses import JSONResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from typing import List, Optional, Dict, Any
from datetime import datetime, timedelta
from pydantic import BaseModel
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create necessary directories
os.makedirs("backend/uploads", exist_ok=True)
os.makedirs("backend/data", exist_ok=True)

# In-memory storage (replace with database in production)
HAZARDS_FILE = "backend/data/hazards.json"
hazards_db = []

# Load existing hazards
def load_hazards():
    global hazards_db
    try:
        if os.path.exists(HAZARDS_FILE):
            with open(HAZARDS_FILE, 'r') as f:
                hazards_db = json.load(f)
                logger.info(f"Loaded {len(hazards_db)} hazards from storage")
    except Exception as e:
        logger.error(f"Error loading hazards: {e}")
        hazards_db = []

def save_hazards():
    try:
        with open(HAZARDS_FILE, 'w') as f:
            json.dump(hazards_db, f, indent=2)
    except Exception as e:
        logger.error(f"Error saving hazards: {e}")

# Lifespan event handler
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    logger.info("=" * 60)
    logger.info("🚗 AI Road Hazard Detector API - Starting")
    logger.info("=" * 60)
    load_hazards()
    logger.info(f"✓ Loaded {len(hazards_db)} hazards from storage")
    logger.info("✓ API ready for mobile app connections")
    logger.info("✓ Documentation available at /docs")
    logger.info("=" * 60)
    
    yield
    
    # Shutdown
    logger.info("Shutting down API server...")
    save_hazards()
    logger.info(f"✓ Saved {len(hazards_db)} hazards to storage")

# Initialize FastAPI app with lifespan
app = FastAPI(
    title="🚗 AI Road Hazard Detector API",
    description="Production-ready backend for mobile hazard detection app",
    version="2.0.0",
    lifespan=lifespan
)

# CORS middleware for mobile app access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your mobile app domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic models
class HazardReport(BaseModel):
    latitude: float
    longitude: float
    hazard_type: str
    speed: float = 0.0
    timestamp: str

class HazardResponse(BaseModel):
    id: str
    status: str
    message: str

# ==================== MAIN ENDPOINTS FOR MOBILE APP ====================

@app.get('/')
async def root():
    """API root with system information"""
    return {
        "app": "🚗 AI Road Hazard Detector API",
        "version": "2.0.0",
        "status": "online",
        "total_hazards": len(hazards_db),
        "endpoints": {
            "POST /api/hazard": "Save hazard detection from mobile app",
            "GET /api/hazards": "Get all hazards for map display",
            "POST /api/detect": "Run AI detection on image",
            "GET /api/hazards/nearby": "Get hazards near location (lat, lng, radius_m)",
            "GET /api/stats": "Get detection statistics",
            "DELETE /api/hazard/{id}": "Delete specific hazard"
        },
        "documentation": "/docs"
    }

@app.post('/api/hazard', response_model=HazardResponse)
async def save_hazard(
    latitude: float = Form(...),
    longitude: float = Form(...),
    hazard_type: str = Form(...),
    speed: float = Form(0.0),
    timestamp: str = Form(...)
):
    """
    Save hazard detection from mobile app
    Called when mobile app detects a road hazard
    """
    try:
        # Generate unique ID
        hazard_id = f"H{len(hazards_db) + 1:06d}"
        
        # Create hazard record
        hazard = {
            'id': hazard_id,
            'type': hazard_type,
            'latitude': float(latitude),
            'longitude': float(longitude),
            'speed': float(speed),
            'timestamp': timestamp,
            'created_at': datetime.now().isoformat(),
            'severity': 'high' if speed > 50 else 'medium' if speed > 30 else 'low',
            'status': 'active'
        }
        
        # Add to database
        hazards_db.append(hazard)
        save_hazards()
        
        logger.info(f"✓ Hazard saved: {hazard_id} at ({latitude}, {longitude})")
        
        return HazardResponse(
            id=hazard_id,
            status="success",
            message=f"Hazard {hazard_id} saved successfully"
        )
        
    except Exception as e:
        logger.error(f"Error saving hazard: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get('/api/hazards')
async def get_all_hazards(
    limit: int = Query(100, description="Maximum number of hazards to return"),
    offset: int = Query(0, description="Number of hazards to skip"),
    type: Optional[str] = Query(None, description="Filter by hazard type")
):
    """
    Get all hazards for map display
    Used by mobile app to show hazards on map
    """
    try:
        # Filter by type if specified
        filtered_hazards = hazards_db
        if type:
            filtered_hazards = [h for h in hazards_db if h.get('type') == type]
        
        # Sort by timestamp (newest first)
        sorted_hazards = sorted(
            filtered_hazards,
            key=lambda x: x.get('timestamp', ''),
            reverse=True
        )
        
        # Apply pagination
        paginated = sorted_hazards[offset:offset + limit]
        
        logger.info(f"✓ Returned {len(paginated)} hazards (total: {len(hazards_db)})")
        
        return {
            "total": len(filtered_hazards),
            "count": len(paginated),
            "offset": offset,
            "limit": limit,
            "hazards": paginated
        }
        
    except Exception as e:
        logger.error(f"Error fetching hazards: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get('/api/hazards/nearby')
async def get_nearby_hazards(
    lat: float = Query(..., description="Latitude"),
    lng: float = Query(..., description="Longitude"),
    radius_m: float = Query(1000.0, description="Search radius in meters")
):
    """
    Get hazards near a specific location
    Used for proximity alerts in mobile app
    """
    try:
        # Simple distance calculation (approximate)
        # For production, use proper geospatial queries
        delta = radius_m / 111000  # Convert meters to degrees (approximate)
        
        nearby = []
        for hazard in hazards_db:
            h_lat = hazard.get('latitude', 0)
            h_lng = hazard.get('longitude', 0)
            
            # Simple bounding box check
            if (abs(h_lat - lat) <= delta and abs(h_lng - lng) <= delta):
                # Calculate approximate distance
                lat_diff = (h_lat - lat) * 111000
                lng_diff = (h_lng - lng) * 111000 * np.cos(np.radians(lat))
                distance = np.sqrt(lat_diff**2 + lng_diff**2)
                
                if distance <= radius_m:
                    hazard_copy = hazard.copy()
                    hazard_copy['distance_m'] = round(distance, 2)
                    nearby.append(hazard_copy)
        
        # Sort by distance
        nearby.sort(key=lambda x: x['distance_m'])
        
        logger.info(f"✓ Found {len(nearby)} hazards within {radius_m}m of ({lat}, {lng})")
        
        return {
            "center": {"latitude": lat, "longitude": lng},
            "radius_m": radius_m,
            "count": len(nearby),
            "hazards": nearby
        }
        
    except Exception as e:
        logger.error(f"Error finding nearby hazards: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post('/api/detect')
async def detect_hazard_from_image(image: UploadFile = File(...)):
    """
    Run YOLO detection on uploaded image
    Returns detected hazards with confidence scores
    """
    try:
        # Read image
        contents = await image.read()
        nparr = np.frombuffer(contents, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        if img is None:
            raise HTTPException(status_code=400, detail="Invalid image format")
        
        # Try to load YOLO detector
        try:
            from detector import detect_hazard
            
            # Run detection
            processed_img, hazard_detected = detect_hazard(img)
            
            return {
                "status": "success",
                "hazard_detected": hazard_detected,
                "confidence": 0.85 if hazard_detected else 0.0,
                "message": "Pothole detected!" if hazard_detected else "No hazards detected"
            }
            
        except ImportError:
            # Fallback: simulate detection
            logger.warning("YOLO detector not available, using simulation")
            
            # Simple simulation based on image properties
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            variance = cv2.Laplacian(gray, cv2.CV_64F).var()
            
            # Low variance might indicate road damage
            hazard_detected = variance < 100
            
            return {
                "status": "success",
                "hazard_detected": hazard_detected,
                "confidence": 0.65 if hazard_detected else 0.0,
                "message": "Possible hazard detected (simulation)" if hazard_detected else "No hazards detected",
                "note": "Using simulation mode - YOLO model not loaded"
            }
            
    except Exception as e:
        logger.error(f"Error in detection: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get('/api/stats')
async def get_statistics():
    """
    Get detection statistics
    Used for statistics screen in mobile app
    """
    try:
        if not hazards_db:
            return {
                "total_hazards": 0,
                "by_type": {},
                "by_severity": {},
                "recent_24h": 0,
                "average_speed": 0.0
            }
        
        # Calculate statistics
        total = len(hazards_db)
        
        # Count by type
        by_type = {}
        for h in hazards_db:
            htype = h.get('type', 'unknown')
            by_type[htype] = by_type.get(htype, 0) + 1
        
        # Count by severity
        by_severity = {}
        for h in hazards_db:
            severity = h.get('severity', 'unknown')
            by_severity[severity] = by_severity.get(severity, 0) + 1
        
        # Recent 24h
        now = datetime.now()
        recent_24h = 0
        for h in hazards_db:
            try:
                h_time = datetime.fromisoformat(h.get('timestamp', ''))
                if (now - h_time).total_seconds() < 86400:
                    recent_24h += 1
            except:
                pass
        
        # Average speed
        speeds = [h.get('speed', 0) for h in hazards_db if h.get('speed', 0) > 0]
        avg_speed = sum(speeds) / len(speeds) if speeds else 0.0
        
        return {
            "total_hazards": total,
            "by_type": by_type,
            "by_severity": by_severity,
            "recent_24h": recent_24h,
            "average_speed": round(avg_speed, 2),
            "last_updated": datetime.now().isoformat()
        }
        
    except Exception as e:
        logger.error(f"Error calculating stats: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.delete('/api/hazard/{hazard_id}')
async def delete_hazard(hazard_id: str):
    """
    Delete a specific hazard
    Admin function for hazard management
    """
    try:
        global hazards_db
        
        # Find and remove hazard
        initial_count = len(hazards_db)
        hazards_db = [h for h in hazards_db if h.get('id') != hazard_id]
        
        if len(hazards_db) < initial_count:
            save_hazards()
            logger.info(f"✓ Deleted hazard: {hazard_id}")
            return {"status": "success", "message": f"Hazard {hazard_id} deleted"}
        else:
            raise HTTPException(status_code=404, detail=f"Hazard {hazard_id} not found")
            
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error deleting hazard: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post('/api/hazards/clear')
async def clear_all_hazards(confirm: bool = Body(..., embed=True)):
    """
    Clear all hazards (admin function)
    Requires confirmation
    """
    if not confirm:
        raise HTTPException(status_code=400, detail="Confirmation required")
    
    try:
        global hazards_db
        count = len(hazards_db)
        hazards_db = []
        save_hazards()
        
        logger.warning(f"⚠️ Cleared all {count} hazards")
        
        return {
            "status": "success",
            "message": f"Cleared {count} hazards",
            "count": count
        }
        
    except Exception as e:
        logger.error(f"Error clearing hazards: {e}")
        raise HTTPException(status_code=500, detail=str(e))

# ==================== HEALTH CHECK ====================

@app.get('/health')
async def health_check():
    """Health check endpoint for monitoring"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "hazards_count": len(hazards_db),
        "storage": "file-based",
        "version": "2.0.0"
    }

# ==================== RUN SERVER ====================

if __name__ == "__main__":
    import uvicorn
    
    print("\n" + "=" * 60)
    print("🚗 AI Road Hazard Detector - Backend API Server")
    print("=" * 60)
    print("Starting server on http://0.0.0.0:5000")
    print("API Documentation: http://localhost:5000/docs")
    print("=" * 60 + "\n")
    
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=5000,
        log_level="info",
        access_log=True
    )
