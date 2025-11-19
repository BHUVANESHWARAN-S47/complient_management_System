@echo off
echo Starting Smart Complaint Portal...
echo.

echo Installing backend dependencies...
cd backend
pip install -r requirements.txt
echo.

echo Starting backend server on port 8000...
start "Backend API" cmd /k "python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload"
timeout /t 5

cd ..
echo Starting frontend server on port 3000...
start "Frontend Server" cmd /k "python serve_frontend.py"

echo.
echo =========================================
echo Smart Complaint Portal is starting...
echo Backend API: http://localhost:8000
echo Frontend: http://localhost:3000
echo API Docs: http://localhost:8000/docs
echo =========================================
echo.
echo Press any key to stop all servers...
pause > nul
taskkill /FI "WindowTitle eq Backend API*" /T /F
taskkill /FI "WindowTitle eq Frontend Server*" /T /F
