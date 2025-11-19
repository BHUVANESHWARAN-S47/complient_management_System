#!/bin/bash

# Smart Complaint Portal Demo Script

echo "🚀 Starting Smart Complaint Portal Demo"

# Step 1: Start the application
echo "🔧 Starting application with Docker Compose..."
docker-compose up -d

# Wait for services to start
echo "⏳ Waiting for services to start..."
sleep 10

# Step 2: Check if services are running
echo "🔍 Checking service status..."
docker-compose ps

# Step 3: Ingest sample data (in a real implementation, this would load JSONL fixtures)
echo "📊 Ingesting sample complaints..."
# This would be implemented with a script that sends POST requests to /api/complaints

# Step 4: Open UI in browser
echo "🌐 Opening Smart Complaint Portal in browser..."
# On Linux/Mac:
# xdg-open http://localhost:8000
# On Windows:
# start http://localhost:8000

echo "✅ Demo setup complete!"
echo ""
echo "📋 Demo Steps:"
echo "1. Open your browser and go to http://localhost:8000"
echo "2. Navigate through the landing page"
echo "3. Click 'Login' and use any username/password (mock auth)"
echo "4. Explore the dashboard with metrics"
echo "5. Submit a sample complaint using the 'Submit Complaint' form"
echo "6. View auto-category prediction"
echo "7. Check the 'Spam Filtering' page to see spam scores"
echo "8. Visit 'Classification' to see ML categorization"
echo "9. Explore 'Recurrence Detection' for pattern identification"
echo "10. Use 'Routing & Escalation' to manage complaint assignments"
echo "11. Test SLA tracking and escalation simulation"
echo ""
echo "💡 Tips:"
echo "- Watch for the auto-category prediction as you type"
echo "- Try the undo functionality after forwarding complaints"
echo "- Notice the SLA status changes based on time remaining"
echo ""
echo "🛑 To stop the demo, run: docker-compose down"