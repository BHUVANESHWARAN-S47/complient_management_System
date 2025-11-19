# Smart Complaint Portal - Configuration

## Server URLs

### Backend API
- URL: http://localhost:8000
- API Documentation: http://localhost:8000/docs
- Health Check: http://localhost:8000/health

### Frontend
- URL: http://localhost:3000
- Home Page: http://localhost:3000/index.html
- Login Page: http://localhost:3000/login.html
- Dashboard: http://localhost:3000/dashboard.html
- Submit Complaint: http://localhost:3000/submit.html

## How to Start

### Option 1: Using the start script (Windows)
```bash
start.bat
```

### Option 2: Manual start
1. Start Backend:
```bash
cd backend
python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

2. Start Frontend (in a new terminal):
```bash
python serve_frontend.py
```

## Features

### Connected Features
- ✅ User Login (connects to `/api/auth/login`)
- ✅ Submit Complaint (connects to `/api/complaints`)
- ✅ AI-powered spam detection
- ✅ ML-based complaint classification
- ✅ Recurrence detection

### API Endpoints Available
- POST `/api/auth/login` - User authentication
- POST `/api/complaints` - Create complaint
- GET `/api/complaints/{complaint_id}` - Get complaint details
- POST `/api/complaints/forward` - Forward complaint
- POST `/api/complaints/forward/batch` - Batch forward
- POST `/api/complaints/{complaint_id}/feedback` - Submit feedback
- GET `/api/complaints/{complaint_id}/history` - Get complaint history

## Test Credentials
You can login with any username/password - the backend currently uses mock authentication.

## Tech Stack
- Backend: FastAPI (Python)
- Frontend: HTML, Tailwind CSS, JavaScript
- AI/ML: Mock ML models (can be replaced with real models)
