import joblib

model = joblib.load(r"C:\Users\anoodhivi\2025-2026 projects\truth-checker-ai\models\fake_news_model.pkl")
vectorizer = joblib.load(r"C:\Users\anoodhivi\2025-2026 projects\truth-checker-ai\models\vectorizer.pkl")


def check_news(news_text):
    transformed_text = vectorizer.transform([news_text])
    prediction = model.predict(transformed_text)[0]
    return "❌ Fake News" if prediction == 0 else "✅ Real News"

# Example
if __name__ == "__main__":
    sample = input("Enter news text: ")
    result = check_news(sample)
    print(result)