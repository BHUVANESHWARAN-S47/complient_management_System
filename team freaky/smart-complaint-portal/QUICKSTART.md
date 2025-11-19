# Quick Start Guide - Smart Complaint Portal Multi-Role System

## 🚀 Get Started in 5 Minutes

### Prerequisites
- Python 3.8 or higher
- Modern web browser (Chrome, Firefox, Edge)
- Terminal/Command Prompt

### Step 1: Install Dependencies (2 minutes)

```bash
cd "c:\Users\hyper\Downloads\complaint system by arun c\team freaky\smart-complaint-portal\backend"
pip install -r requirements.txt
```

### Step 2: Start the Backend Server (30 seconds)

```bash
python main_enhanced.py
```

You should see:
```
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

### Step 3: Access the Application (30 seconds)

Open your browser and navigate to:
```
file:///c:/Users/hyper/Downloads/complaint system by arun c/team freaky/smart-complaint-portal/frontend/login_enhanced.html
```

Or serve the frontend using:
```bash
cd "c:\Users\hyper\Downloads\complaint system by arun c\team freaky\smart-complaint-portal"
python serve_frontend.py
```

Then visit: `http://localhost:3000/login_enhanced.html`

### Step 4: Login with Demo Accounts (1 minute)

#### Option 1: Login as Administrator
1. Click on **"Administrator"** role card
2. Enter credentials:
   - Username: `admin`
   - Password: `admin123`
3. Click **"Sign In"**
4. You'll be redirected to the Admin Dashboard

#### Option 2: Login as Citizen/User
1. Click on **"Citizen"** role card
2. Enter credentials:
   - Username: `john_doe`
   - Password: `password123`
3. Click **"Sign In"**
4. You'll be redirected to the User Dashboard

#### Option 3: Login as Volunteer
1. Click on **"Volunteer"** role card
2. Enter credentials:
   - Username: `jane_smith`
   - Password: `password123`
3. Click **"Sign In"**
4. You'll be redirected to the Volunteer Dashboard

## 🎯 What to Try

### As Administrator
✅ **View Dashboard Metrics**
- Total complaints count
- Total users count
- Active volunteers
- Average feedback rating

✅ **Manage Users**
- Navigate to "User Management"
- View all users with their roles
- Create new users (any role)

✅ **View All Complaints**
- Navigate to "All Complaints"
- See system-wide complaint data
- Filter and search complaints

✅ **Analyze Feedback**
- Navigate to "Feedback Analysis"
- View sentiment distribution
- Check rating trends
- Read user comments

✅ **Manage Volunteer Applications**
- Navigate to "Volunteer Management"
- Approve or reject volunteer requests
- Assign regions and categories

### As User/Citizen
✅ **Submit a Complaint**
- Click "Submit Complaint"
- Fill in title and description
- See ML-powered category prediction
- Submit and track

✅ **Track Your Complaints**
- View "My Complaints" dashboard
- See active and resolved counts
- Check status of each complaint

✅ **Update Profile**
- Navigate to "My Profile"
- Update name, email, phone
- Save changes

✅ **Apply to Volunteer**
- Navigate to "Become a Volunteer"
- Fill motivation and preferences
- Submit application for admin review

### As Volunteer
✅ **Verify Complaints**
- View complaints in assigned area
- Mark as legitimate, suspicious, or spam
- Add supporting evidence

✅ **Vote on Priority**
- Access community complaints
- Vote on priority (1-5)
- Add verification notes

## 🔧 Testing the API Directly

### Using curl

**Test Authentication:**
```bash
curl -X POST http://localhost:8000/api/auth/login \
  -H "Content-Type: application/json" \
  -d "{\"username_or_email\":\"admin\",\"password\":\"admin123\",\"selected_role\":\"admin\"}"
```

**Get All Users (Admin Only):**
```bash
curl -X GET http://localhost:8000/api/admin/users \
  -H "Authorization: Bearer YOUR_TOKEN_HERE"
```

**Submit a Complaint:**
```bash
curl -X POST http://localhost:8000/api/citizen/complaints \
  -H "Authorization: Bearer YOUR_TOKEN_HERE" \
  -H "Content-Type: application/json" \
  -d "{\"title\":\"Test Complaint\",\"description\":\"Test description\",\"category\":\"sanitation\",\"location\":{\"lat\":0,\"lon\":0}}"
```

### Using Postman or Insomnia

1. Import the following base URL: `http://localhost:8000`
2. Create a POST request to `/api/auth/login`
3. Add JSON body:
```json
{
  "username_or_email": "admin",
  "password": "admin123",
  "selected_role": "admin"
}
```
4. Copy the returned token
5. Use it in Authorization header for subsequent requests:
```
Authorization: Bearer YOUR_TOKEN
```

## 📋 Common Tasks

### Create a New User Account

**Via UI:**
1. Navigate to registration page (if created)
2. Fill in details
3. Submit

**Via API:**
```bash
curl -X POST http://localhost:8000/api/auth/register \
  -H "Content-Type: application/json" \
  -d "{\"username\":\"newuser\",\"email\":\"new@example.com\",\"password\":\"password123\",\"full_name\":\"New User\",\"phone_number\":\"+1234567890\"}"
```

### Submit Feedback for a Complaint

1. Login as user who submitted the complaint
2. Navigate to "My Complaints"
3. Select a resolved complaint
4. Fill feedback form with:
   - Overall rating (1-5 stars)
   - Resolution satisfaction (1-5)
   - Process satisfaction (1-5)
   - Response time rating (1-5)
   - Comments
   - Suggestions

**Via API:**
```bash
curl -X POST http://localhost:8000/api/citizen/complaints/COMPLAINT_ID/feedback \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d "{\"complaint_id\":\"COMPLAINT_ID\",\"rating\":5,\"resolution_satisfaction\":5,\"process_satisfaction\":4,\"response_time_rating\":4,\"comments\":\"Great service!\",\"suggestions\":\"Keep it up\"}"
```

### Apply to Become a Volunteer

1. Login as a citizen/user
2. Navigate to "Become a Volunteer"
3. Fill motivation statement
4. Select preferred regions
5. Select preferred categories
6. Submit application
7. Wait for admin approval

### Approve a Volunteer Application

1. Login as admin
2. Navigate to "Volunteer Management"
3. View pending requests
4. Click "Approve" on an application
5. Request will be processed
6. User's role will be updated to volunteer

## 🛠️ Troubleshooting

### Backend Won't Start

**Error: Port 8000 already in use**
```bash
# Find and kill the process
# Windows:
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# Or change port in main_enhanced.py:
uvicorn.run(app, host="0.0.0.0", port=8001)
```

**Error: Module not found**
```bash
pip install --upgrade pip
pip install -r backend/requirements.txt
```

### Login Not Working

**Issue: Invalid credentials**
- Verify you're using the correct demo account
- Check caps lock is off
- Ensure backend is running

**Issue: CORS errors**
- Check browser console
- Verify API_BASE_URL in frontend files matches backend
- Ensure CORS is configured in backend

### API Returns 401 Unauthorized

- Token may have expired (24 hour expiration)
- Login again to get a new token
- Check Authorization header format: `Bearer YOUR_TOKEN`

### Data Not Loading

- Open browser console (F12) and check for errors
- Verify backend is running at http://localhost:8000
- Check network tab to see API responses
- Try refreshing the page

## 📊 Sample Data

The system comes pre-loaded with:
- 3 user accounts (admin, user, volunteer)
- Database tables ready for use
- No complaints initially (submit your own!)

## 🔐 Security Notes

**For Development:**
- Default SECRET_KEY is used (change for production)
- In-memory database (data lost on restart)
- All passwords are bcrypt hashed
- JWT tokens expire after 24 hours

**For Production:**
- Change SECRET_KEY in environment variables
- Use PostgreSQL database
- Enable HTTPS
- Implement rate limiting
- Add input sanitization
- Regular security audits

## 📚 Next Steps

1. **Explore All Features**:
   - Try each role's dashboard
   - Submit complaints as a user
   - Verify complaints as a volunteer
   - Analyze data as an admin

2. **Read Full Documentation**:
   - See `IMPLEMENTATION_README.md` for complete details
   - Review design document in `.qoder/quests/admin-module-setup.md`

3. **Customize**:
   - Add your own branding
   - Customize categories
   - Add departments
   - Configure regions

4. **Integrate Production Database**:
   - Set up PostgreSQL
   - Run database migrations
   - Update connection strings

5. **Deploy**:
   - Choose hosting platform
   - Configure environment variables
   - Set up CI/CD
   - Monitor and maintain

## 💡 Tips

- **Use Browser DevTools**: Press F12 to see API calls and debug
- **Check Console**: Logs show helpful information
- **Try All Roles**: Experience the system from different perspectives
- **Test Workflows**: Submit complaint → Verify as volunteer → Analyze as admin
- **Read API Responses**: They contain useful metadata and IDs

## 🎉 Success!

You now have a fully functional multi-role complaint management system with:
- ✅ Role-based authentication
- ✅ Admin, User, and Volunteer dashboards
- ✅ Complaint submission and tracking
- ✅ Feedback analysis with sentiment detection
- ✅ Volunteer conversion workflow
- ✅ Comprehensive API

**Happy Testing! 🚀**

---

For issues or questions, refer to:
- `IMPLEMENTATION_README.md` - Full documentation
- Design document - `.qoder/quests/admin-module-setup.md`
- Backend code - `backend/main_enhanced.py`
