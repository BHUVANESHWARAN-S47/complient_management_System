import json
import random
from datetime import datetime, timedelta
import uuid

# Sample data
categories = ["sanitation", "traffic", "infrastructure", "public_safety", "utilities"]
descriptions = [
    "Garbage not collected for weeks in sector 5",
    "Street light not working near metro station",
    "Water supply issue in residential area",
    "Potholes on main road causing traffic jams",
    "Broken sewer line causing overflow",
    "Traffic signal malfunctioning at intersection",
    "Street flooding due to blocked drain",
    "Power outage in apartment complex",
    "Broken bench in public park",
    "Overgrown grass in public garden"
]

# Generate 200 complaints
complaints = []

for i in range(200):
    # Randomly decide if this should be a duplicate (10% chance)
    is_duplicate = random.random() < 0.1
    
    if is_duplicate and i > 0:
        # Use an existing complaint's description
        base_complaint = complaints[random.randint(0, len(complaints) - 1)]
        description = base_complaint["description"]
    else:
        description = random.choice(descriptions)
    
    complaint = {
        "complaint_id": str(uuid.uuid4()),
        "title": f"Complaint #{i+1}",
        "description": description,
        "category": random.choice(categories),
        "created_at": (datetime.now() - timedelta(days=random.randint(0, 30))).isoformat(),
        "location": {
            "lat": round(random.uniform(12.0, 13.0), 6),
            "lon": round(random.uniform(77.0, 78.0), 6)
        },
        "attachments": [],
        "language_tag": "en"
    }
    
    complaints.append(complaint)

# Save to JSONL file
with open("complaints.jsonl", "w") as f:
    for complaint in complaints:
        f.write(json.dumps(complaint) + "\n")

print(f"Generated {len(complaints)} complaints in complaints.jsonl")