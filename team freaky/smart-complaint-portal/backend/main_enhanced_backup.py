from fastapi import FastAPI, Depends, HTTPException, Header, Body
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import uuid
from datetime import datetime, timedelta
import json
import os

app = FastAPI(title="Smart Complaint Portal API", version="1.0.0")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mock database storage
COMPLAINTS_DB = {}
FORWARDS_DB = {}
CLUSTERS_DB = {}

# Models
class ComplaintCreate(BaseModel):
    title: str
    description: str
    category: str
    location: dict  # {lat, lon}
    attachments: List[str] = []
    language_tag: str = "en"

class ComplaintResponse(BaseModel):
    complaint_id: str
    title: str
    description: str
    category: str
    location: dict
    attachments: List[str]
    language_tag: str
    spam_score: float
    predicted_class: str
    ml_confidence_score: float
    recurrence_flag: bool
    cluster_id: Optional[str]
    created_at: datetime
    updated_at: datetime

class ForwardRequest(BaseModel):
    complaint_id: str
    recipient_department: str
    recipient_officer_id: str
    recipient_officer_name: str
    remarks: str
    follow_up_date: datetime
    priority_level: str  # Normal, High, Urgent
    status: str = "Pending"
    notify_channels: List[str] = []
    forward_template_id: Optional[str] = None

class ForwardResponse(BaseModel):
    forward_id: str
    complaint_id: str
    recipient_department: str
    recipient_officer_id: str
    recipient_officer_name: str
    remarks: str
    follow_up_date: datetime
    priority_level: str
    status: str
    sla_deadline: datetime
    sla_status: str
    undo_token: str
    undo_expires_at: datetime
    recurrence_flag: bool
    previous_occurrences_count: int
    cluster_id: Optional[str]
    duplicate_similarity_score: float
    ml_confidence_score: float
    forwarded_by: str
    created_at: datetime
    updated_at: datetime

class FeedbackRequest(BaseModel):
    citizen_rating: int  # 1-5
    comments: str

class AuthRequest(BaseModel):
    username: str
    password: str

class AuthResponse(BaseModel):
    token: str
    user_id: str

# Helper functions
def get_current_user(x_user_id: str = Header(None)):
    if not x_user_id:
        raise HTTPException(status_code=401, detail="X-User-Id header required")
    return x_user_id

def calculate_sla_deadline(priority_level: str) -> datetime:
    now = datetime.now()
    if priority_level == "Urgent":
        return now + timedelta(hours=24)
    elif priority_level == "High":
        return now + timedelta(days=3)
    else:  # Normal
        return now + timedelta(days=7)

def get_sla_status(deadline: datetime) -> str:
    now = datetime.now()
    time_left = deadline - now
    total_time = deadline - (deadline - timedelta(days=7))  # Simplified
    
    if time_left.total_seconds() <= 0:
        return "Breached"
    elif time_left.total_seconds() <= total_time.total_seconds() * 0.2:
        return "At-Risk"
    else:
        return "On-Track"

# API Endpoints
@app.post("/api/auth/login", response_model=AuthResponse)
async def login(credentials: AuthRequest):
    # Mock authentication - in real app, verify credentials
    return AuthResponse(token=str(uuid.uuid4()), user_id=str(uuid.uuid4()))

@app.post("/api/complaints", response_model=ComplaintResponse)
async def create_complaint(complaint: ComplaintCreate):
    complaint_id = str(uuid.uuid4())
    
    # Simulate ML processing
    import random
    spam_score = random.uniform(0.01, 0.99)
    predicted_class = random.choice(["Sanitation", "Traffic", "Infrastructure", "Public Safety"])
    ml_confidence_score = random.uniform(0.60, 0.99)
    recurrence_flag = random.choice([True, False])
    cluster_id = str(uuid.uuid4()) if recurrence_flag else None
    
    complaint_data = ComplaintResponse(
        complaint_id=complaint_id,
        title=complaint.title,
        description=complaint.description,
        category=complaint.category,
        location=complaint.location,
        attachments=complaint.attachments,
        language_tag=complaint.language_tag,
        spam_score=spam_score,
        predicted_class=predicted_class,
        ml_confidence_score=ml_confidence_score,
        recurrence_flag=recurrence_flag,
        cluster_id=cluster_id,
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    
    COMPLAINTS_DB[complaint_id] = complaint_data.dict()
    return complaint_data

@app.get("/api/complaints/{complaint_id}", response_model=ComplaintResponse)
async def get_complaint(complaint_id: str):
    if complaint_id not in COMPLAINTS_DB:
        raise HTTPException(status_code=404, detail="Complaint not found")
    return ComplaintResponse(**COMPLAINTS_DB[complaint_id])

@app.post("/api/complaints/forward", response_model=ForwardResponse)
async def forward_complaint(forward: ForwardRequest, user_id: str = Depends(get_current_user)):
    if forward.complaint_id not in COMPLAINTS_DB:
        raise HTTPException(status_code=404, detail="Complaint not found")
    
    forward_id = str(uuid.uuid4())
    undo_token = str(uuid.uuid4())
    undo_expires_at = datetime.now() + timedelta(minutes=5)
    
    # Calculate SLA
    sla_deadline = calculate_sla_deadline(forward.priority_level)
    sla_status = get_sla_status(sla_deadline)
    
    # Simulate ML data
    import random
    recurrence_flag = random.choice([True, False])
    previous_occurrences_count = random.randint(0, 10)
    cluster_id = str(uuid.uuid4()) if recurrence_flag else None
    duplicate_similarity_score = random.uniform(0.0, 1.0)
    ml_confidence_score = random.uniform(0.60, 0.99)
    
    forward_data = ForwardResponse(
        forward_id=forward_id,
        complaint_id=forward.complaint_id,
        recipient_department=forward.recipient_department,
        recipient_officer_id=forward.recipient_officer_id,
        recipient_officer_name=forward.recipient_officer_name,
        remarks=forward.remarks,
        follow_up_date=forward.follow_up_date,
        priority_level=forward.priority_level,
        status=forward.status,
        sla_deadline=sla_deadline,
        sla_status=sla_status,
        undo_token=undo_token,
        undo_expires_at=undo_expires_at,
        recurrence_flag=recurrence_flag,
        previous_occurrences_count=previous_occurrences_count,
        cluster_id=cluster_id,
        duplicate_similarity_score=duplicate_similarity_score,
        ml_confidence_score=ml_confidence_score,
        forwarded_by=user_id,
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    
    FORWARDS_DB[forward_id] = forward_data.dict()
    return forward_data

@app.post("/api/complaints/forward/batch")
async def batch_forward(complaint_ids: List[str] = Body(...), user_id: str = Depends(get_current_user)):
    results = []
    for complaint_id in complaint_ids:
        # For this demo, we'll just return a simple success response
        results.append({"complaint_id": complaint_id, "success": True})
    return {"results": results}

@app.post("/api/complaints/{complaint_id}/feedback")
async def submit_feedback(complaint_id: str, feedback: FeedbackRequest):
    # In a real app, save feedback to database
    # For now, just return success
    return {"message": "Feedback submitted successfully"}

@app.get("/api/complaints/{complaint_id}/history")
async def get_complaint_history(complaint_id: str):
    # Return audit trail and forward history
    history = {
        "audit_trail": [],
        "forward_history": [f for f in FORWARDS_DB.values() if f["complaint_id"] == complaint_id]
    }
    return history

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)