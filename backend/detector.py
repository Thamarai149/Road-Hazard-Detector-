import cv2
import numpy as np
from ultralytics import YOLO
import os
import logging
import torch

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Optimize PyTorch for low memory environments (like Render Free Tier)
try:
    torch.set_num_threads(1)
    logger.info("✓ PyTorch threads limited to 1 for memory optimization")
except Exception as e:
    logger.warning(f"Could not set torch threads: {e}")

# Base directory of the backend
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Path to the model - using the one in backend/model/
MODEL_PATH = os.path.join(BASE_DIR, "model", "yolov8n.pt")

# Initialize model
model = None
try:
    if os.path.exists(MODEL_PATH):
        model = YOLO(MODEL_PATH)
        logger.info(f"✓ YOLO model loaded from {MODEL_PATH}")
    else:
        logger.warning(f"⚠️ Model not found at {MODEL_PATH}, using default yolov8n.pt")
        model = YOLO("yolov8n.pt")
except Exception as e:
    logger.error(f"❌ Error loading YOLO model: {e}")

def detect_hazard(image: np.ndarray):
    """
    Detects road hazards (potholes, cracks) in an image using YOLOv8.
    
    Args:
        image: BGR image from OpenCV
        
    Returns:
        tuple: (processed_image, hazard_detected, confidence)
    """
    if model is None:
        logger.error("YOLO model not initialized")
        return image, False, 0.0
    
    try:
        # Run inference
        # conf=0.25 is a reasonable default for detection
        results = model.predict(image, conf=0.25, verbose=False)
        
        hazard_detected = False
        max_conf = 0.0
        annotated_image = image.copy()
        
        for result in results:
            if len(result.boxes) > 0:
                hazard_detected = True
                # Get the highest confidence score
                conf_scores = result.boxes.conf.tolist()
                if conf_scores:
                    max_conf = max(conf_scores)
                
                # Annotate image
                annotated_image = result.plot()
                break
                
        return annotated_image, hazard_detected, max_conf
        
    except Exception as e:
        logger.error(f"Error during detection: {e}")
        return image, False, 0.0
