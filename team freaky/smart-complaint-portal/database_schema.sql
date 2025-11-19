-- Smart Complaint Portal Database Schema
-- PostgreSQL/PostGIS with SQLite compatibility

-- Complaints table
CREATE TABLE complaints (
    id VARCHAR(36) PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    category VARCHAR(50) NOT NULL,
    original_location GEOMETRY(POINT, 4326), -- PostGIS geometry type
    attachments JSONB, -- PostgreSQL JSONB type
    spam_score DECIMAL(3,2), -- Range 0.00 - 1.00
    predicted_class VARCHAR(50),
    ml_confidence_score DECIMAL(3,2), -- Range 0.00 - 1.00
    recurrence_flag BOOLEAN DEFAULT FALSE,
    cluster_id VARCHAR(36), -- Foreign key to clusters table
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    soft_delete BOOLEAN DEFAULT FALSE
);

-- Forwards table (complaint routing/assignment)
CREATE TABLE forwards (
    forward_id VARCHAR(36) PRIMARY KEY,
    complaint_id VARCHAR(36) NOT NULL, -- Foreign key to complaints table
    recipient_department VARCHAR(100) NOT NULL,
    recipient_officer_id VARCHAR(36) NOT NULL,
    recipient_officer_name VARCHAR(100) NOT NULL,
    remarks TEXT,
    follow_up_date TIMESTAMP,
    priority_level VARCHAR(20) NOT NULL, -- Normal, High, Urgent
    status VARCHAR(20) DEFAULT 'Pending', -- Pending, Assigned, Resolved, Escalated
    sla_deadline TIMESTAMP NOT NULL,
    sla_status VARCHAR(20) DEFAULT 'On-Track', -- On-Track, At-Risk, Breached
    recurrence_flag BOOLEAN DEFAULT FALSE,
    previous_occurrences_count INTEGER DEFAULT 0,
    cluster_id VARCHAR(36), -- Foreign key to clusters table
    duplicate_similarity_score DECIMAL(3,2), -- Range 0.00 - 1.00
    ml_confidence_score DECIMAL(3,2), -- Range 0.00 - 1.00
    forwarded_by VARCHAR(36) NOT NULL, -- User ID of person who forwarded
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    undo_token VARCHAR(36), -- Token for undo functionality
    undo_expires_at TIMESTAMP, -- Expiration time for undo functionality
    FOREIGN KEY (complaint_id) REFERENCES complaints(id)
);

-- Forward audit trail
CREATE TABLE forward_audit (
    id VARCHAR(36) PRIMARY KEY,
    forward_id VARCHAR(36) NOT NULL, -- Foreign key to forwards table
    action_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    actor VARCHAR(36) NOT NULL, -- User ID of person who performed action
    action VARCHAR(50) NOT NULL, -- Accept, Reject, Forward, Escalate, Undo, etc.
    meta JSONB, -- Additional metadata about the action
    FOREIGN KEY (forward_id) REFERENCES forwards(forward_id)
);

-- Clusters table (for recurring complaint patterns)
CREATE TABLE clusters (
    cluster_id VARCHAR(36) PRIMARY KEY,
    centroid_location GEOMETRY(POINT, 4326), -- PostGIS geometry type
    complaint_count INTEGER DEFAULT 0,
    severity VARCHAR(20) DEFAULT 'Low', -- Low, Medium, High
    last_seen TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for performance
CREATE INDEX idx_complaints_created_at ON complaints(created_at);
CREATE INDEX idx_complaints_category ON complaints(category);
CREATE INDEX idx_complaints_spam_score ON complaints(spam_score);
CREATE INDEX idx_complaints_recurrence_flag ON complaints(recurrence_flag);
CREATE INDEX idx_forwards_complaint_id ON forwards(complaint_id);
CREATE INDEX idx_forwards_sla_deadline ON forwards(sla_deadline);
CREATE INDEX idx_forwards_sla_status ON forwards(sla_status);
CREATE INDEX idx_forwards_priority_level ON forwards(priority_level);
CREATE INDEX idx_forward_audit_forward_id ON forward_audit(forward_id);
CREATE INDEX idx_clusters_last_seen ON clusters(last_seen);

-- SQLite compatibility notes:
-- 1. Replace GEOMETRY with TEXT for location fields
-- 2. Replace JSONB with TEXT for attachments and meta fields
-- 3. Use VARCHAR instead of TEXT where needed
-- 4. Remove PostGIS-specific functions