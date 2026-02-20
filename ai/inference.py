"""AI inference helper using ultralytics YOLOv8.
Provides a simple detect_image function that returns detections.
"""
import importlib
import cv2
import numpy as np
from typing import List, Dict, Any

# Dynamic import to avoid static analyzer issues
YOLO = None
try:
    mod = importlib.import_module("ultralytics.yolo")
    YOLO = getattr(mod, "YOLO", None)
except Exception:
    try:
        mod = importlib.import_module("ultralytics")
        YOLO = getattr(mod, "YOLO", None)
    except Exception:
        YOLO = None


class YoloDetector:
    def __init__(self, model_path: str = "model/yolov8n.pt", conf_threshold: float = 0.3):
        self.model = None
        self.conf_threshold = conf_threshold
        if YOLO is None:
            raise RuntimeError("YOLO not available: install ultralytics")
        self.model = YOLO(model_path)

    def detect_image(self, image: np.ndarray) -> List[Dict[str, Any]]:
        """Run YOLO on BGR OpenCV image. Returns list of detections.

        Each detection: {class, confidence, xyxy}
        """
        results = self.model(image)
        detections = []
        for r in results:
            boxes = getattr(r, 'boxes', None)
            if boxes is None:
                continue
            for box in boxes:
                conf = float(box.conf[0])
                if conf < self.conf_threshold:
                    continue
                cls = int(box.cls[0])
                xyxy = [int(v) for v in box.xyxy[0].tolist()]
                label = self.model.names[cls] if hasattr(self.model, 'names') else str(cls)
                detections.append({
                    'class': label,
                    'confidence': conf,
                    'xyxy': xyxy,
                })
        return detections


def annotate_image(image: np.ndarray, detections: List[Dict[str, Any]]) -> np.ndarray:
    out = image.copy()
    for d in detections:
        x1, y1, x2, y2 = d['xyxy']
        label = f"{d['class']} {d['confidence']:.2f}"
        cv2.rectangle(out, (x1, y1), (x2, y2), (0, 0, 255), 2)
        cv2.putText(out, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
    return out
