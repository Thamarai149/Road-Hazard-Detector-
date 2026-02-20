## Project Documentation

Abstract, Problem statement, Objectives, Methodology, Technologies, Advantages, and Future scope.

### Problem Statement
Road hazards (potholes, cracks) cause accidents and vehicle damage. Manual reporting is slow.

### Objectives
- Real-time detection of potholes and cracks
- Geo-tagging each detection
- Centralized hazard map for authorities and drivers

### Methodology
- Use YOLOv8 to detect hazards; fall back to CV heuristics when model fails.
- Mobile app collects images + GPS and reports to backend.
- Backend stores hazards and serves map data.

### Technologies
- Python, Ultralyics YOLOv8, OpenCV
- FastAPI, MongoDB
- Flutter for mobile

### Future Scope
- Better models, active learning pipeline, dashboard analytics, push notifications.
