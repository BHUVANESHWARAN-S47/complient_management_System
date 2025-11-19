"""
MongoDB Integration for Smart Complaint Portal
This script demonstrates how to integrate MongoDB for persistent user storage
"""

from pymongo import MongoClient
from passlib.context import CryptContext
from datetime import datetime
import os
from typing import Optional

# Security configuration
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# MongoDB connection
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(MONGO_URI)
db = client.smartcomplaint
users_collection = db.users

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def register_user(username: str, email: str, password: str, full_name: str, phone_number: Optional[str] = None):
    """Register a new user in MongoDB"""
    # Check if user already exists
    if users_collection.count_documents({'$or': [{'username': username}, {'email': email}]}) > 0:
        return {"error": "User already exists"}
    
    # Hash password
    password_hash = hash_password(password)
    
    # Create user document
    user_doc = {
        'user_id': str(datetime.now().timestamp()),  # Simple ID generation
        'username': username,
        'email': email,
        'password_hash': password_hash,
        'full_name': full_name,
        'phone_number': phone_number,
        'role': 'user',
        'is_active': True,
        'created_at': datetime.now(),
        'updated_at': datetime.now()
    }
    
    # Insert user into MongoDB
    result = users_collection.insert_one(user_doc)
    
    if result.inserted_id:
        return {"success": True, "user_id": user_doc['user_id']}
    else:
        return {"error": "Failed to register user"}

def authenticate_user(username_or_email: str, password: str):
    """Authenticate user against MongoDB"""
    # Find user
    user = users_collection.find_one({
        '$or': [
            {'username': username_or_email},
            {'email': username_or_email}
        ]
    })
    
    if not user:
        return {"error": "User not found"}
    
    # Verify password
    if verify_password(password, user['password_hash']):
        return {"success": True, "user": user}
    else:
        return {"error": "Invalid password"}

def get_all_users():
    """Get all users from MongoDB"""
    users = list(users_collection.find({}))
    # Remove password hashes for security
    for user in users:
        user.pop('password_hash', None)
    return users

# Example usage
if __name__ == "__main__":
    print("MongoDB Integration Test")
    print("=" * 30)
    
    # Test registration
    result = register_user("testuser", "test@example.com", "password123", "Test User")
    print(f"Registration result: {result}")
    
    # Test authentication
    auth_result = authenticate_user("testuser", "password123")
    print(f"Authentication result: {auth_result}")
    
    # Show all users
    users = get_all_users()
    print(f"Total users: {len(users)}")
    for user in users:
        print(f"  - {user['username']} ({user['email']})")