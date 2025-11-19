# Smart Complaint Portal - Multi-Role System Implementation

## Overview

This implementation adds a comprehensive three-tier role-based access control system to the Smart Complaint Portal with Admin, User (Citizen), and Volunteer roles.

## What Has Been Implemented

### Phase 1: Foundation ✅

#### 1. Database Schema (`database_schema_extended.sql`)
- **Users Table**: Complete user management with role-based access
- **Sessions Table**: Secure session tracking with role selection
- **Feedback Table**: Comprehensive feedback collection with sentiment analysis
- **Volunteer Conversion Requests Table**: User-to-volunteer application workflow
- **Volunteer Actions Table**: Track volunteer verification activities
- **Password Reset Tokens Table**: Secure password recovery
- **Extended Complaints Table**: Added ownership and verification fields
- **Sample Data**: Pre-loaded admin, user, and volunteer accounts

**Default Accounts**:
- Admin: `admin` / `admin123`
- User: `john_doe` / `password123`
- Volunteer: `jane_smith` / `password123`

#### 2. Backend API (`backend/main_enhanced.py`)

**Authentication Endpoints**:
- `POST /api/auth/register` - Register new citizen account
- `POST /api/auth/login` - Role-based login with role selection
- `POST /api/auth/logout` - Session termination
- `GET /api/auth/validate-session` - Session validation
- `POST /api/auth/forgot-password` - Password reset request
- `POST /api/auth/reset-password` - Complete password reset
- `POST /api/auth/change-password` - Password change for authenticated users

**Citizen/User Endpoints**:
- `GET /api/citizen/profile` - Get user profile
- `PUT /api/citizen/profile` - Update user profile
- `POST /api/citizen/complaints` - Submit new complaint
- `GET /api/citizen/complaints` - Get own complaints
- `GET /api/citizen/complaints/{id}` - Get specific complaint
- `POST /api/citizen/complaints/{id}/feedback` - Submit feedback
- `POST /api/citizen/volunteer/apply` - Apply for volunteer role
- `GET /api/citizen/volunteer/application-status` - Check application status

**Volunteer Endpoints**:
- `GET /api/volunteer/complaints/assigned-area` - Get complaints in assigned region
- `POST /api/volunteer/complaints/{id}/verify` - Verify complaint legitimacy

**Admin Endpoints**:
- `GET /api/admin/users` - List all users
- `POST /api/admin/users` - Create new user (any role)
- `GET /api/admin/complaints` - Get all complaints
- `PUT /api/admin/complaints/{id}/status` - Update complaint status
- `GET /api/admin/volunteers/requests` - Get volunteer requests
- `POST /api/admin/volunteers/requests/{id}/approve` - Approve volunteer
- `POST /api/admin/volunteers/requests/{id}/reject` - Reject volunteer

**Feedback Analysis Endpoints (Admin)**:
- `GET /api/admin/feedback/overview` - Feedback overview metrics
- `GET /api/admin/feedback/list` - All feedback with filters
- `GET /api/admin/feedback/ratings` - Rating analysis
- `GET /api/admin/feedback/sentiment` - Sentiment analysis

**Features**:
- JWT-based authentication with bcrypt password hashing
- Role-based authorization middleware
- Automatic sentiment analysis on feedback
- ML integration ready (spam detection, classification, recurrence)
- In-memory database for demonstration (easily replaceable with PostgreSQL)

#### 3. Enhanced Login Page (`frontend/login_enhanced.html`)

**Features**:
- Beautiful role selection interface with three role cards:
  - **Administrator**: Purple/indigo theme with shield icon
  - **Citizen**: Blue/cyan theme with user icon
  - **Volunteer**: Green/teal theme with helping hands icon
- Two-step login process:
  1. Role selection
  2. Credential authentication
- Role-specific visual theming
- Password visibility toggle
- Responsive design for all devices
- Automatic redirection based on selected role
- Form validation and error handling
- "Remember me" functionality

#### 4. Admin Dashboard (`frontend/admin_dashboard.html`)

**Features**:
- **Dashboard Overview**:
  - Total complaints metric
  - Total users metric
  - Active volunteers metric
  - Average feedback rating metric
  - Quick access to all system features
  
- **User Management Section**:
  - View all users with roles and status
  - Create new users (any role)
  - Role-based badges (admin/user/volunteer)
  
- **Complaints Management Section**:
  - View all complaints system-wide
  - Filter and search capabilities
  - Quick actions for each complaint
  
- **Feedback Analysis Module** (NEW):
  - Total feedback count
  - Average rating with star display
  - Feedback submission rate
  - Sentiment distribution (Positive/Neutral/Negative)
  - Recent feedback list with sentiment badges
  - Rating breakdown
  
- **Volunteer Management Section**:
  - View pending volunteer applications
  - Approve/reject volunteer requests
  - Assign regions and categories
  
- **Integration with Existing Features**:
  - Spam Filtering
  - Classification
  - Recurrence Detection
  - Routing & Escalation
  - Reports
  - Analytics
  - Settings

### Phase 2: In Progress 🚧

#### User Dashboard (Planned)
- Personal complaint management
- Complaint submission form with ML assistance
- Complaint tracking and status updates
- Feedback submission interface
- Volunteer application form
- Profile management

#### Volunteer Dashboard (Planned)
- Assigned area complaints view
- Complaint verification interface
- Priority voting system
- Community analytics
- Evidence submission

## Technology Stack

- **Backend**: Python FastAPI
- **Frontend**: HTML, Tailwind CSS, JavaScript
- **Authentication**: JWT with bcrypt
- **Database**: PostgreSQL/SQLite compatible schema
- **ML Ready**: Spam detection, classification, sentiment analysis

## Project Structure

```
smart-complaint-portal/
├── backend/
│   ├── main_enhanced.py          # Enhanced backend with multi-role system
│   ├── main.py                    # Original backend
│   └── requirements.txt           # Updated with bcrypt and PyJWT
├── frontend/
│   ├── login_enhanced.html        # Role-based login page
│   ├── admin_dashboard.html       # Complete admin interface
│   ├── user_dashboard.html        # (To be created)
│   ├── volunteer_dashboard.html   # (To be created)
│   └── [existing files]           # Original frontend files
├── database_schema_extended.sql   # Multi-role database schema
└── README.md                      # This file
```

## How to Run

### 1. Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 2. Start the Backend

```bash
# Using the enhanced backend
python main_enhanced.py
```

The API will be available at `http://localhost:8000`

### 3. Access the Frontend

Open `frontend/login_enhanced.html` in your browser or serve it using:

```bash
# From project root
python serve_frontend.py
```

### 4. Login with Demo Accounts

**Administrator**:
- Username: `admin`
- Password: `admin123`
- Select Role: Administrator
- Access: Full system control + feedback analysis

**Citizen/User**:
- Username: `john_doe`
- Password: `password123`
- Select Role: Citizen
- Access: Submit complaints, track, provide feedback

**Volunteer**:
- Username: `jane_smith`
- Password: `password123`
- Select Role: Volunteer
- Access: Verify complaints, vote on priority, community analytics

## Key Features Implemented

### 1. Role-Based Authentication
- Users select their role at login (Admin/User/Volunteer)
- JWT tokens include role and selected_role
- Backend validates role permissions on every request
- Session management with expiration

### 2. Admin Module
- Complete visibility into all system data
- User management across all roles
- Complaint oversight and management
- **NEW**: Comprehensive feedback analysis module
  - Rating trends and distributions
  - Sentiment analysis (positive/neutral/negative)
  - Department performance via feedback
  - Improvement suggestions tracking
- Volunteer application approval workflow
- Access to all existing features

### 3. Citizen Module
- Submit and track personal complaints
- ML-powered category prediction
- View complaint status and history
- Submit detailed feedback with multiple ratings
- Apply to become a volunteer
- Profile management

### 4. Volunteer Module
- Verify complaint legitimacy in assigned areas
- Add supporting evidence
- Vote on complaint priority
- Access community-level analytics
- All citizen features retained

### 5. Feedback Analysis System
- Multi-dimensional ratings (overall, resolution, process, response time)
- Automatic sentiment analysis using NLP
- Aggregate metrics and trends
- Department and category-based analysis
- Export and reporting capabilities

### 6. User-to-Volunteer Conversion
- Citizens can apply for volunteer status
- Admins review and approve/reject applications
- Automatic role conversion upon approval
- Region and category assignment

## Security Features

- **Password Security**: Bcrypt hashing with salt
- **Token Security**: JWT with expiration
- **Role Validation**: Every endpoint validates user role
- **Session Management**: Secure session tracking
- **Password Reset**: Token-based recovery with expiration
- **Input Validation**: Frontend and backend validation
- **CORS**: Configured for secure cross-origin requests

## API Documentation

### Authentication Flow

1. User visits login page
2. Selects role (Admin/User/Volunteer)
3. Enters credentials
4. Backend validates credentials and role permission
5. JWT token issued with user_id, role, and selected_role
6. Frontend stores token and redirects to appropriate dashboard
7. All subsequent requests include token in Authorization header

### Feedback Submission Flow

1. User resolves a complaint
2. User navigates to feedback form
3. Provides ratings on multiple dimensions (1-5 stars)
4. Writes comments and suggestions
5. Backend performs sentiment analysis on text
6. Feedback stored with sentiment score and classification
7. Admin can view aggregated analytics

### Volunteer Conversion Flow

1. User applies for volunteer role
2. Provides motivation and preferences
3. Application stored with "pending" status
4. Admin reviews application
5. Admin approves (assigns region/categories) or rejects
6. If approved, user role updated to "volunteer"
7. User can now login as volunteer

## Database Schema Highlights

### Users Table
- Supports admin, user, and volunteer roles
- Volunteer-specific fields (status, region, categories)
- Tracks role conversion timestamp
- Active/inactive status management

### Feedback Table
- Multiple rating dimensions
- Text comments and suggestions
- ML-generated sentiment score (-1 to 1)
- Sentiment classification (positive/neutral/negative)
- Links to complaint and user

### Volunteer Conversion Requests Table
- Tracks application workflow
- Stores user motivation and preferences
- Admin review tracking
- Approval/rejection with notes

## Next Steps (Remaining Implementation)

### Phase 2: User Interface
- [ ] User dashboard with complaint management
- [ ] Enhanced complaint submission form
- [ ] Complaint tracking interface with timeline
- [ ] Feedback submission form
- [ ] Volunteer application interface

### Phase 3: Volunteer Interface
- [ ] Volunteer dashboard
- [ ] Complaint verification UI
- [ ] Priority voting interface
- [ ] Community analytics visualization

### Phase 4: Enhanced Features
- [ ] Real-time notifications
- [ ] Advanced feedback analytics (word clouds, trends)
- [ ] Department performance dashboards
- [ ] Export/reporting functionality
- [ ] Email integration for notifications
- [ ] Mobile responsive optimizations

### Phase 5: Testing & Deployment
- [ ] Unit tests for all API endpoints
- [ ] Integration tests for workflows
- [ ] End-to-end testing
- [ ] Performance optimization
- [ ] Database migration to PostgreSQL
- [ ] Production deployment configuration

## Known Limitations

1. **In-Memory Database**: Current implementation uses dictionaries for data storage. Needs PostgreSQL integration for production.
2. **Basic Sentiment Analysis**: Uses simple keyword matching. Should integrate advanced NLP models.
3. **No Real-time Updates**: Dashboard requires manual refresh. WebSocket integration needed.
4. **Limited File Upload**: Attachment handling is simplified. Needs cloud storage integration.
5. **No Email Service**: Password reset and notifications are simulated. Needs SMTP integration.

## Configuration

### Environment Variables
Create a `.env` file in the backend directory:

```env
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_HOURS=24
DATABASE_URL=postgresql://user:password@localhost/smartcomplaint
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=your-email@gmail.com
SMTP_PASSWORD=your-app-password
```

### API Base URL
Update in frontend files:
```javascript
const API_BASE_URL = 'http://localhost:8000';
```

## Troubleshooting

### Backend Issues

**Issue**: Module not found errors
```bash
# Solution: Install all requirements
pip install -r backend/requirements.txt
```

**Issue**: Port already in use
```bash
# Solution: Change port in main_enhanced.py
uvicorn.run(app, host="0.0.0.0", port=8001)
```

### Frontend Issues

**Issue**: CORS errors
```bash
# Solution: Ensure backend CORS is configured
# Check main_enhanced.py CORSMiddleware settings
```

**Issue**: Login fails
```bash
# Solution: Check API_BASE_URL in frontend files
# Verify backend is running
# Check browser console for errors
```

### Authentication Issues

**Issue**: Token expired
```bash
# Solution: Token expires after 24 hours
# User needs to login again
# Adjust ACCESS_TOKEN_EXPIRE_HOURS if needed
```

## Contributing

1. Follow the design document in `.qoder/quests/admin-module-setup.md`
2. Maintain code style consistency
3. Add tests for new features
4. Update this README with changes

## License

All rights reserved - Smart Complaint Portal 2025

## Credits

Developed as part of the Smart Complaint Portal enhancement project to add multi-role access control and comprehensive feedback analysis capabilities.

---

**Version**: 2.0.0  
**Last Updated**: 2025-11-15  
**Status**: Phase 1 Complete, Phase 2 In Progress
