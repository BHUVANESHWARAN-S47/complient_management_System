# Changelog

All notable changes to the Smart Complaint Portal project will be documented in this file.

## [1.0.0] - 2025-11-13

### 🎉 Initial Release

#### ✅ Implemented Features

**Frontend (HTML/CSS/JS)**
- Landing page with logo, title, and feature cards
- Login page with username/password form
- Dashboard with metric cards and module grid
- Complaint submission form with auto-category prediction
- Spam filtering page with complaint table and actions
- Classification page with predicted classes and confidence scores
- Recurrence detection page with cluster cards and heatmap
- Routing & escalation page with SLA tracking and actions

**Backend (FastAPI)**
- REST API with endpoints for:
  - Authentication (mock implementation)
  - Complaint ingestion with spam scoring
  - Complaint retrieval
  - Complaint forwarding (single and batch)
  - Feedback submission
  - Complaint history retrieval
- Mock ML implementations for:
  - Spam detection (random scores 0.01-0.99)
  - Classification (random categories with confidence 0.60-0.99)
  - Recurrence detection (random clusters)
  - Routing confidence (random scores)

**Infrastructure**
- Dockerfile for backend service
- docker-compose.yml with backend, PostgreSQL, and Redis services
- Requirements file with all Python dependencies

**Data**
- Project structure for sample data fixtures (JSONL format)

#### ⏳ Partially Implemented Features

**ML Components**
- Framework in place for scikit-learn spam classifier
- Framework in place for sentence-transformers + FAISS duplicate detection
- Training scripts and notebooks structure planned but not implemented
- Model artifacts structure planned but not implemented

**Database**
- Schema defined for complaints, forwards, forward_audit, and clusters tables
- PostgreSQL/PostGIS support planned but using in-memory storage for demo
- SQLite fallback planned but not implemented

**Advanced Features**
- SLA calculation implemented with configurable deadlines
- Escalation simulation with status tracking (On-Track/At-Risk/Breached)
- Undo-forward functionality with 5-minute window
- Audit trail for complaint history
- Notification simulation (UI elements in place)

#### 🚫 Omitted Features (Planned for Future Releases)

**Security & Privacy**
- Real authentication system (JWT tokens, password hashing)
- PII masking toggle for attachments
- Role-based access control

**Advanced ML**
- Actual trained models for spam detection
- Real SBERT embeddings and FAISS indexing
- Actual duplicate detection with similarity >= 0.75
- Real routing confidence scores

**Testing**
- pytest tests for core endpoints
- Integration tests for ML components
- Performance benchmarks

**Documentation**
- Detailed API documentation beyond OpenAPI
- User guides for each module
- Deployment guides for production environments

### 📋 Next Steps

1. **Implement actual ML models**:
   - Train spam classifier with TF-IDF + LogisticRegression
   - Implement SBERT embeddings and FAISS indexing
   - Create duplicate detection with real similarity scoring

2. **Database Integration**:
   - Replace in-memory storage with PostgreSQL/PostGIS
   - Implement soft-delete functionality
   - Add proper indexing for performance

3. **Security Enhancements**:
   - Implement JWT-based authentication
   - Add password hashing with passlib
   - Implement role-based access control

4. **Testing**:
   - Write comprehensive pytest tests
   - Add ML model evaluation metrics
   - Implement CI/CD pipeline

5. **Advanced Features**:
   - Real-time notification system
   - Advanced analytics and reporting
   - Mobile-responsive design