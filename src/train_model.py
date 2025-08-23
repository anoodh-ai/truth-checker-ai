import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib


# 1. Load dataset
df = pd.read_csv(r"C:\Users\anoodhivi\2025-2026 projects\truth-checker-ai\data\news.csv")

# 2. Split features and labels
df['combined_text'] = df['title'].astype(str) + " " + df['news_url'].astype(str) + " " + df['source_domain'].astype(str)

# Features and labels
X = df['combined_text']
y = df['real']

# 3. Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. TF-IDF Vectorizer
vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# 5. Train Logistic Regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train_tfidf, y_train)

# 6. Predictions & Accuracy
y_pred = model.predict(X_test_tfidf)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

# 7. Save model & vectorizer
joblib.dump(model,  r"C:\Users\anoodhivi\2025-2026 projects\truth-checker-ai\models\fake_news_model.pkl")
joblib.dump(vectorizer, r"C:\Users\anoodhivi\2025-2026 projects\truth-checker-ai\models\vectorizer.pkl")
