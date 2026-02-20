## System Architecture

Components:
- Mobile App (Flutter): captures camera frames and GPS, sends images/detections to backend.
- Backend (FastAPI): endpoints for inference, reporting hazards, and serving hazards to clients.
- AI Module (Python): YOLOv8 model for detection and CV fallbacks.
- Database (MongoDB): stores hazard documents with location and image URL.

Data flow:
1. Mobile app captures a frame and GPS coordinates.
2. App either runs local inference or sends image to `/detect` endpoint.
3. If hazard detected, app POSTs to `/report` with metadata and image.
4. Backend saves image to storage (or cloud) and inserts a hazard doc in MongoDB.
5. Map UI queries `/hazards` or `/hazards/nearby` to show markers.
