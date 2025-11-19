import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_login():
    response = client.post("/api/auth/login", json={
        "username": "testuser",
        "password": "testpass"
    })
    assert response.status_code == 200
    assert "token" in response.json()
    assert "user_id" in response.json()

def test_create_complaint():
    response = client.post("/api/complaints", json={
        "title": "Test Complaint",
        "description": "This is a test complaint",
        "category": "sanitation",
        "location": {"lat": 12.34, "lon": 56.78},
        "attachments": [],
        "language_tag": "en"
    })
    assert response.status_code == 200
    data = response.json()
    assert "complaint_id" in data
    assert data["title"] == "Test Complaint"
    assert "spam_score" in data
    assert "predicted_class" in data

def test_get_complaint():
    # First create a complaint
    create_response = client.post("/api/complaints", json={
        "title": "Test Complaint",
        "description": "This is a test complaint",
        "category": "sanitation",
        "location": {"lat": 12.34, "lon": 56.78},
        "attachments": [],
        "language_tag": "en"
    })
    complaint_id = create_response.json()["complaint_id"]
    
    # Then retrieve it
    response = client.get(f"/api/complaints/{complaint_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["complaint_id"] == complaint_id
    assert data["title"] == "Test Complaint"

def test_forward_complaint():
    # First create a complaint
    create_response = client.post("/api/complaints", json={
        "title": "Test Complaint",
        "description": "This is a test complaint",
        "category": "sanitation",
        "location": {"lat": 12.34, "lon": 56.78},
        "attachments": [],
        "language_tag": "en"
    })
    complaint_id = create_response.json()["complaint_id"]
    
    # Then forward it
    response = client.post("/api/complaints/forward", 
        json={
            "complaint_id": complaint_id,
            "recipient_department": "Sanitation Dept",
            "recipient_officer_id": "OFF-001",
            "recipient_officer_name": "John Doe",
            "remarks": "Urgent attention needed",
            "follow_up_date": "2025-12-31T10:00:00",
            "priority_level": "High",
            "status": "Pending",
            "notify_channels": ["email", "sms"]
        },
        headers={"X-User-Id": "USER-001"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "forward_id" in data
    assert data["complaint_id"] == complaint_id
    assert "sla_deadline" in data
    assert "undo_token" in data

def test_submit_feedback():
    # First create a complaint
    create_response = client.post("/api/complaints", json={
        "title": "Test Complaint",
        "description": "This is a test complaint",
        "category": "sanitation",
        "location": {"lat": 12.34, "lon": 56.78},
        "attachments": [],
        "language_tag": "en"
    })
    complaint_id = create_response.json()["complaint_id"]
    
    # Then submit feedback
    response = client.post(f"/api/complaints/{complaint_id}/feedback", json={
        "citizen_rating": 5,
        "comments": "Great service!"
    })
    assert response.status_code == 200
    assert "message" in response.json()

def test_get_complaint_history():
    # First create a complaint
    create_response = client.post("/api/complaints", json={
        "title": "Test Complaint",
        "description": "This is a test complaint",
        "category": "sanitation",
        "location": {"lat": 12.34, "lon": 56.78},
        "attachments": [],
        "language_tag": "en"
    })
    complaint_id = create_response.json()["complaint_id"]
    
    # Then get its history
    response = client.get(f"/api/complaints/{complaint_id}/history")
    assert response.status_code == 200
    data = response.json()
    assert "audit_trail" in data
    assert "forward_history" in data

def test_batch_forward():
    # First create complaints
    complaint_ids = []
    for i in range(3):
        create_response = client.post("/api/complaints", json={
            "title": f"Test Complaint {i}",
            "description": f"This is test complaint {i}",
            "category": "sanitation",
            "location": {"lat": 12.34, "lon": 56.78},
            "attachments": [],
            "language_tag": "en"
        })
        complaint_ids.append(create_response.json()["complaint_id"])
    
    # Then batch forward them
    response = client.post("/api/complaints/forward/batch",
        json=complaint_ids,
        headers={"X-User-Id": "USER-001"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "results" in data
    assert len(data["results"]) == 3