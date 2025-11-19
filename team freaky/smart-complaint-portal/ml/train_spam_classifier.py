"""
Simple spam classifier training script using TF-IDF and Logistic Regression
"""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import joblib
import json

def load_sample_data():
    """Load sample complaint data"""
    # In a real implementation, this would load from the JSONL fixtures
    # For this demo, we'll create sample data
    data = [
        ("This is a legitimate complaint about garbage collection", 0),
        ("Garbage not picked up for weeks", 0),
        ("Street light broken near metro station", 0),
        ("Water supply issue in my area", 0),
        ("Click here to claim your prize now!!!", 1),
        ("Congratulations! You've won a lottery!", 1),
        ("Get rich quick with this amazing offer", 1),
        ("Free money! Act now!", 1),
        ("Your account will be closed unless you verify", 1),
        ("Potholes causing traffic problems", 0),
        ("Broken sewer line causing overflow", 0),
        ("Traffic signal not working properly", 0),
        ("Make money fast with no effort", 1),
        ("Limited time offer! Buy now!", 1),
        ("Your subscription is expiring", 1),
        ("Street flooding due to blocked drain", 0),
        ("Power outage in apartment complex", 0),
        ("Urgent! Verify your account immediately", 1),
        ("Claim your reward today", 1),
        ("Infrastructure needs repair", 0)
    ]
    
    df = pd.DataFrame(data, columns=['text', 'label'])
    return df

def train_spam_classifier():
    """Train a simple spam classifier"""
    # Load data
    df = load_sample_data()
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        df['text'], df['label'], test_size=0.2, random_state=42
    )
    
    # Vectorize text
    vectorizer = TfidfVectorizer(max_features=1000, stop_words='english')
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)
    
    # Train model
    model = LogisticRegression(random_state=42)
    model.fit(X_train_vec, y_train)
    
    # Evaluate
    y_pred = model.predict(X_test_vec)
    print("Classification Report:")
    print(classification_report(y_test, y_pred))
    
    # Save model and vectorizer
    joblib.dump(model, 'spam_classifier_model.pkl')
    joblib.dump(vectorizer, 'tfidf_vectorizer.pkl')
    
    print("Model saved as 'spam_classifier_model.pkl'")
    print("Vectorizer saved as 'tfidf_vectorizer.pkl'")
    
    return model, vectorizer

def predict_spam(text, model, vectorizer):
    """Predict if a text is spam"""
    # Vectorize the text
    text_vec = vectorizer.transform([text])
    
    # Predict
    prediction = model.predict(text_vec)[0]
    probability = model.predict_proba(text_vec)[0]
    
    return prediction, probability

if __name__ == "__main__":
    # Train the model
    model, vectorizer = train_spam_classifier()
    
    # Test with sample texts
    test_texts = [
        "Garbage collection needs improvement in sector 7",
        "Congratulations! You have won $1000000! Click here now!",
        "Street light not working near the park",
        "Free iPhone! Limited time offer! Act now!!!"
    ]
    
    print("\nSample Predictions:")
    for text in test_texts:
        prediction, probability = predict_spam(text, model, vectorizer)
        label = "SPAM" if prediction == 1 else "NOT SPAM"
        confidence = max(probability)
        print(f"Text: {text}")
        print(f"Prediction: {label} (Confidence: {confidence:.2f})")
        print()