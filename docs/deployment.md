## Deployment Guide

Backend (FastAPI):
- Use `uvicorn backend.app:app --host 0.0.0.0 --port 8000` for local testing.
- For production, containerize with Docker and deploy to Render / Railway.
- Ensure MongoDB is reachable; use managed MongoDB Atlas for production.

AI Model:
- Include `model/yolov8n.pt` in artifact or use a mounted volume.
- For scalable inference, deploy as a separate service with GPU workers.

Mobile App:
- Build Flutter release and publish to Play Store / App Store.
- Use app config to point to backend URL.
