# Smart Complaint Portal Demo Script

## Prerequisites
- Docker and Docker Compose installed
- Git (optional, for cloning the repository)

## Setup Instructions

1. **Start the application**:
   ```bash
   docker-compose up --build
   ```

2. **Wait for services to start** (usually takes 1-2 minutes)

3. **Open the browser** and navigate to:
   - Frontend: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

## Demo Walkthrough

### 1. Landing Page
- Show the landing page with the "SC" logo
- Highlight the key features: Spam Filtering, ML Classification, Transparency Dashboard
- Click "Login" to proceed

### 2. Login
- Use any username/password (mock authentication)
- Click "Sign In"

### 3. Dashboard
- Show the dashboard with metric cards:
  - Total Complaints
  - Spam Filtered
  - Major Complaints
  - Subset Complaints
  - Recurrence Detected
  - Escalations Pending
  - Resolved Complaints
  - Active Volunteers
- Show the main modules grid with 8 boxes

### 4. Submit a Complaint
- Click "Submit Complaint" from the dashboard
- Fill out the form:
  - Enter citizen name
  - Enter location coordinates
  - Enter complaint description
  - Watch the auto-category prediction update as you type
  - Select a category
  - Upload evidence (optional)
  - Click "Submit Complaint"

### 5. Spam Filtering
- Navigate to "Spam Filtering" from the dashboard
- Show the table of complaints with spam scores
- Demonstrate accepting/rejecting complaints

### 6. Classification
- Navigate to "Classification" from the dashboard
- Show the table of complaints with predicted classes
- Demonstrate changing categories

### 7. Recurrence Detection
- Navigate to "Recurrence Detection" from the dashboard
- Show the cluster cards with locations and complaint counts
- Click "View AI Detected Patterns Details" to show the modal

### 8. Routing & Escalation
- Navigate to "Routing & Escalation" from the dashboard
- Show the table with SLA tracking
- Demonstrate assigning/escalating complaints
- Show the undo functionality with the toast notification

## API Testing

You can also test the API directly using the OpenAPI documentation at http://localhost:8000/docs

Key endpoints to demonstrate:
- POST /api/complaints - Submit a new complaint
- POST /api/complaints/forward - Forward a complaint
- POST /api/complaints/forward/batch - Batch forward complaints
- POST /api/complaints/{id}/feedback - Submit feedback
- GET /api/complaints/{id}/history - Get complaint history

## Stopping the Demo

To stop the application:
```bash
docker-compose down
```

## Troubleshooting

If you encounter any issues:
1. Make sure Docker is running
2. Check that ports 8000, 5432, and 6379 are not in use
3. Check the Docker logs: `docker-compose logs`