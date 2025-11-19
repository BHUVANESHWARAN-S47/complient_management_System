# Smart Complaint Portal (SC)

An AI-powered complaint management system with end-to-end features including spam filtering, ML classification, recurrence detection, and SLA management.

## Features

- **Landing Page**: Introduction to the portal with key features
- **Login System**: User authentication (mock implementation)
- **Dashboard**: Overview of metrics and access to all modules
- **Complaint Submission**: Form for citizens to submit complaints with auto-category prediction
- **Spam Filtering**: Review and manage spam complaints
- **Classification**: View and modify complaint categorization
- **Recurrence Detection**: Identify recurring complaint patterns
- **Routing & Escalation**: Manage complaint assignments and SLA tracking

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript with Tailwind CSS
- **Backend**: Python FastAPI
- **Database**: PostgreSQL (with SQLite fallback)
- **ML Components**: 
  - scikit-learn for spam detection
  - sentence-transformers + FAISS for duplicate detection
- **Containerization**: Docker + docker-compose

## Setup Instructions

1. **Prerequisites**:
   - Docker and Docker Compose installed
   - Git

2. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd smart-complaint-portal
   ```

3. **Run with Docker Compose**:
   ```bash
   docker-compose up --build
   ```

4. **Access the application**:
   - Frontend: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

## Project Structure

```
smart-complaint-portal/
├── frontend/           # HTML/CSS/JS frontend files
├── backend/            # FastAPI backend application
│   ├── main.py         # Main application file
│   ├── requirements.txt # Python dependencies
│   └── Dockerfile      # Backend Docker configuration
├── ml/                 # Machine learning components
├── data/               # Sample data fixtures
├── tests/              # Test files
├── docker-compose.yml  # Docker Compose configuration
└── README.md           # This file
```

## API Endpoints

- `POST /api/auth/login` - User authentication
- `POST /api/complaints` - Submit a new complaint
- `GET /api/complaints/{id}` - Get complaint details
- `POST /api/complaints/forward` - Forward a complaint
- `POST /api/complaints/forward/batch` - Batch forward complaints
- `POST /api/complaints/{id}/feedback` - Submit feedback
- `GET /api/complaints/{id}/history` - Get complaint history

## Development

To run the backend locally without Docker:

1. Install dependencies:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   python main.py
   ```

## Testing

Run the test suite:
```bash
cd backend
python -m pytest ../tests/test_api.py -v
```

All 8 tests should pass, covering:
- Health check endpoint
- Authentication
- Complaint creation and retrieval
- Complaint forwarding (single and batch)
- Feedback submission
- Complaint history retrieval

## Machine Learning

The project includes frameworks for:
- Spam detection using TF-IDF + Logistic Regression
- Duplicate detection using sentence-transformers + FAISS
- Classification with confidence scoring

Run the sample spam classifier training:
```bash
cd backend
python ../ml/train_spam_classifier.py
```

## Sample Data

Generate sample complaint data:
```bash
cd data
python generate_fixtures.py
```

This creates a complaints.jsonl file with 200+ sample complaints.

## Database Schema

The database schema is defined in [database_schema.sql](database_schema.sql) and includes tables for:
- complaints
- forwards
- forward_audit
- clusters

The schema supports both PostgreSQL/PostGIS and SQLite.

## Demo Script

1. Start the application with `docker-compose up`
2. Open the browser at http://localhost:8000
3. Navigate through the pages to see all features
4. Submit sample complaints
5. View spam filtering and classification
6. Check recurrence detection
7. Test routing and escalation features

See [script.md](script.md) for detailed demo instructions.

## Documentation

- [CHANGELOG.md](CHANGELOG.md) - Feature tracking and roadmap
- [SUMMARY.md](SUMMARY.md) - Comprehensive project overview
- [database_schema.sql](database_schema.sql) - Database structure

## License

This project is for demonstration purposes only.