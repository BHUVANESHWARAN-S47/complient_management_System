-- Extended Smart Complaint Portal Database Schema
-- Multi-Role System with Admin, User (Citizen), and Volunteer roles

-- ====================================
-- Users Table
-- ====================================
CREATE TABLE users (
    user_id VARCHAR(36) PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(255) NOT NULL,
    phone_number VARCHAR(20),
    role VARCHAR(20) NOT NULL CHECK (role IN ('admin', 'user', 'volunteer')),
    is_active BOOLEAN DEFAULT TRUE,
    volunteer_status VARCHAR(20) CHECK (volunteer_status IN ('pending', 'approved', 'active')),
    volunteer_region VARCHAR(100),
    volunteer_categories TEXT, -- JSONB for PostgreSQL, TEXT for SQLite
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP,
    converted_from_user_at TIMESTAMP
);

-- Indexes for Users table
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_role ON users(role);
CREATE INDEX idx_users_volunteer_status ON users(volunteer_status);

-- ====================================
-- Sessions Table
-- ====================================
CREATE TABLE sessions (
    session_id VARCHAR(36) PRIMARY KEY,
    user_id VARCHAR(36) NOT NULL,
    token VARCHAR(255) UNIQUE NOT NULL,
    selected_role VARCHAR(20) NOT NULL CHECK (selected_role IN ('admin', 'user', 'volunteer')),
    ip_address VARCHAR(45),
    user_agent TEXT,
    expires_at TIMESTAMP NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Indexes for Sessions table
CREATE INDEX idx_sessions_token ON sessions(token);
CREATE INDEX idx_sessions_user_id ON sessions(user_id);

-- ====================================
-- Volunteer Conversion Requests Table
-- ====================================
CREATE TABLE volunteer_conversion_requests (
    request_id VARCHAR(36) PRIMARY KEY,
    user_id VARCHAR(36) NOT NULL,
    motivation TEXT,
    preferred_regions TEXT, -- JSONB for PostgreSQL, TEXT for SQLite
    preferred_categories TEXT, -- JSONB for PostgreSQL, TEXT for SQLite
    status VARCHAR(20) DEFAULT 'pending' CHECK (status IN ('pending', 'approved', 'rejected')),
    reviewed_by VARCHAR(36),
    review_notes TEXT,
    requested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    reviewed_at TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (reviewed_by) REFERENCES users(user_id)
);

-- ====================================
-- Feedback Table
-- ====================================
CREATE TABLE feedback (
    feedback_id VARCHAR(36) PRIMARY KEY,
    complaint_id VARCHAR(36) NOT NULL,
    user_id VARCHAR(36) NOT NULL,
    rating INTEGER CHECK (rating >= 1 AND rating <= 5),
    resolution_satisfaction INTEGER CHECK (resolution_satisfaction >= 1 AND resolution_satisfaction <= 5),
    process_satisfaction INTEGER CHECK (process_satisfaction >= 1 AND process_satisfaction <= 5),
    response_time_rating INTEGER CHECK (response_time_rating >= 1 AND response_time_rating <= 5),
    comments TEXT,
    suggestions TEXT,
    sentiment_score DECIMAL(3,2),
    sentiment_class VARCHAR(20) CHECK (sentiment_class IN ('positive', 'neutral', 'negative')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (complaint_id) REFERENCES complaints(id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Indexes for Feedback table
CREATE INDEX idx_feedback_complaint_id ON feedback(complaint_id);
CREATE INDEX idx_feedback_rating ON feedback(rating);
CREATE INDEX idx_feedback_created_at ON feedback(created_at);

-- ====================================
-- Volunteer Actions Table
-- ====================================
CREATE TABLE volunteer_actions (
    action_id VARCHAR(36) PRIMARY KEY,
    volunteer_id VARCHAR(36) NOT NULL,
    complaint_id VARCHAR(36) NOT NULL,
    action_type VARCHAR(50) NOT NULL CHECK (action_type IN ('verify', 'support_evidence', 'priority_vote')),
    verification_status VARCHAR(20) CHECK (verification_status IN ('legitimate', 'suspicious', 'spam')),
    evidence_url TEXT,
    priority_vote INTEGER CHECK (priority_vote >= 1 AND priority_vote <= 5),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (volunteer_id) REFERENCES users(user_id),
    FOREIGN KEY (complaint_id) REFERENCES complaints(id)
);

-- ====================================
-- Password Reset Tokens Table
-- ====================================
CREATE TABLE password_reset_tokens (
    token_id VARCHAR(36) PRIMARY KEY,
    user_id VARCHAR(36) NOT NULL,
    reset_token VARCHAR(255) UNIQUE NOT NULL,
    expires_at TIMESTAMP NOT NULL,
    used BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE INDEX idx_reset_token ON password_reset_tokens(reset_token);

-- ====================================
-- Extend Complaints Table
-- ====================================
-- Add new columns to existing complaints table
ALTER TABLE complaints ADD COLUMN submitted_by VARCHAR(36);
ALTER TABLE complaints ADD COLUMN citizen_name VARCHAR(255);
ALTER TABLE complaints ADD COLUMN citizen_contact VARCHAR(100);
ALTER TABLE complaints ADD COLUMN is_verified BOOLEAN DEFAULT FALSE;
ALTER TABLE complaints ADD COLUMN verified_by VARCHAR(36);
ALTER TABLE complaints ADD COLUMN verified_at TIMESTAMP;
ALTER TABLE complaints ADD COLUMN volunteer_priority_score DECIMAL(3,2);

-- Add foreign key constraints
-- ALTER TABLE complaints ADD FOREIGN KEY (submitted_by) REFERENCES users(user_id);
-- ALTER TABLE complaints ADD FOREIGN KEY (verified_by) REFERENCES users(user_id);

-- ====================================
-- Create default admin user (password: admin123)
-- ====================================
-- Password hash for 'admin123' using bcrypt
INSERT INTO users (user_id, username, email, password_hash, full_name, role, is_active)
VALUES (
    '00000000-0000-0000-0000-000000000001',
    'admin',
    'admin@smartcomplaint.com',
    '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5NU7QW3dXUCvq', -- admin123
    'System Administrator',
    'admin',
    TRUE
);

-- Create sample user accounts
INSERT INTO users (user_id, username, email, password_hash, full_name, phone_number, role, is_active)
VALUES 
(
    '00000000-0000-0000-0000-000000000002',
    'john_doe',
    'john@example.com',
    '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5NU7QW3dXUCvq', -- password123
    'John Doe',
    '+1234567890',
    'user',
    TRUE
),
(
    '00000000-0000-0000-0000-000000000003',
    'jane_smith',
    'jane@example.com',
    '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5NU7QW3dXUCvq', -- password123
    'Jane Smith',
    '+1234567891',
    'volunteer',
    TRUE
);

-- Update volunteer status for Jane
UPDATE users SET volunteer_status = 'active', volunteer_region = 'Downtown District' WHERE user_id = '00000000-0000-0000-0000-000000000003';
